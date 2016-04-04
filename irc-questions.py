import irc.bot


class LogBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        print e.arguments[0]


def main():
    bot = LogBot('#node.js', 'hellworld', 'irc.freenode.net', 6667)
    bot.start()

if __name__ == '__main__':
    main()