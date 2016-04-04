#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
 Counts words in UTF8 encoded, '\n' delimited text received from the network every second.
 Usage: network_wordcount.py <hostname> <port>
   <hostname> and <port> describe the TCP server that Spark Streaming would connect to receive data.
 To run this on your local machine, you need to first run a Netcat server
    `$ nc -lk 9999`
 and then run the example
    `$ bin/spark-submit examples/src/main/python/streaming/network_wordcount.py localhost 9999`
"""
from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from pyspark import AccumulatorParam

class HashAccumParam(AccumulatorParam):
    def zero(self, initalValue):
        return {};

    def addInPlace(self, v1, v2):
        if v2 in v1:
            v1[v2] += 1;
        else: 
            v1[v2] = 1;
        return v1


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: network_wordcount.py <hostname> <port>", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="PythonStreamingNetworkWordCount")
    ssc = StreamingContext(sc, 1)

    accum = sc.accumulator({}, HashAccumParam())

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    words = lines.flatMap(lambda line: line.split(" "))
    counts = words.map(lambda word: (word, 1))\
                  .reduceByKey(lambda a, b: a+b)

    counts.pprint()

    def fn(rdd):
        words = rdd.collect()
        if len(words) > 0: 
            for word in words: 
                accum.add(word)
            print(accum.value)

    words.foreachRDD(fn)

    ssc.start()
    ssc.awaitTermination()



