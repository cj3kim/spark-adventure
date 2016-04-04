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

#    def writeToAccum (rdd):
        #words = rdd.collect()
        #if len(words) > 0: 
            #for word in words: 
                #accum.add(word)
            #print(accum.value)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: network_wordcount.py <hostname> <port>", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="IRC-Parser")
    ssc = StreamingContext(sc, 1)

    #accum = sc.accumulator({}, HashAccumParam())

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    lines.saveAsTextFiles("irc_logs");

    ssc.start()
    ssc.awaitTermination()
