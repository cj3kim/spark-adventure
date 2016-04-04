module.exports = {
    file: {
        name: "irc-stream.txt",
        outputLocation: ".",
        writeOptions: {
           flags: 'a',
           encoding: "utf8",
           mode: 0666 
        }
    },
    irc: {
        server: "irc.freenode.net",
        nick: "BabyBartlett",
        channels: [
            "#express",
            "#java",
            "#python",
            "#javascript",
            "#haskell",
            "#Node.js",
            "#c",
            "#jobs",
            "#emacs"
        ]
    }
};
