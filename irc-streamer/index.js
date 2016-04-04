var irc  = require('irc');
var fs   = require("fs");
var path = require("path");

var config = require("./config.js");
var ircServer = config.irc.server;
var ircNick   = config.irc.nick;
var fileName  = config.file.name;
var ircChannels = config.irc.channels;
var outputLocation = config.file.outputLocation;

var filePath = path.join(__dirname, outputLocation, fileName);

var client = new irc.Client(ircServer, ircNick, { channels: ircChannels });

var outputFile = fs.createWriteStream(filePath, config.writeOptions);

client.addListener("message", function (from, channel, message) {
    outputFile.write(channel + " - " + from + " - " + message + "\n");
});

/*client.addListener("registered", function (message) {*/
  //console.log("registerd", message);
//});

//client.addListener('error', function(message) {
      //console.log('error: ', message);
//});

