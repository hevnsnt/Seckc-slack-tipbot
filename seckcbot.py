'''
seckc tipbot
'''
# -*- coding: utf-8 -*-
from commands import commands
from slackbot.bot import Bot, respond_to
import slackbot_settings


def parse(msg):
    '''helper function for parsing messages'''
    msg = msg.replace(u'\u201c', '"').replace(u'\u201d', '"')
    command = msg.split(" ")[0]
    command, query = command, msg[len(command)+1:]
    return command, query


@respond_to('.*'.replace(u'\u201c', '"').replace(u'\u201d', '"'))
def route(message):
    '''routes message to proper function'''
    user = message.body['user']
    text = message.body['text'].replace(u'\u201c', '"').replace(u'\u201d', '"')
    command, query = parse(text)
    if command.lower() in commands.keys():
        response, attachments = commands[command.lower()](query, user)
    else:
        response, attachments = commands['help']("", "")
    message.send_webapi(response, attachments)


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
