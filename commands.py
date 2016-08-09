'''
imports all commands from ./plugins/
'''
import json
import os
import plugins
commands = {}
fields = [{
    'title': ":skc: How-To get Started:",
    'value': "http://coin.seckc.org",
    'short': False
}, {
    'title': "Bot Commands:",
}]

for name in os.listdir("plugins"):
    if name.endswith(".py") and "init" not in name:
        modulename = name[:-3]
        __import__("plugins."+modulename)
        module = getattr(plugins, modulename)
        commands.update(module.commands)
        if hasattr(module, 'help_text'):
            fields += module.help_text

fields += [{
    'title': "help:",
    'value': "Usage 'tipskc help' -- this will return this text",
}]


def help_function(_, __):
    """
    returns help
    """
    return ["Commands I understand are: ",
            json.dumps([{
                "color": "good",
                "fields": fields
            }])
           ]

commands['help'] = help_function
