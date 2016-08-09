"""
tipping function
"""
import json
import re
from common import get_balance, set_amount, make_transaction, get_address


def parse(message):
    message = message.split(" ")
    target_user = re.match("\<\@(.*)\>", message[0])
    if target_user:
        message[0] = target_user.group(1)
        return message
    else:
        return None


def tip(msg, user_id):
    """
    either tips a person a random amount or tips them x seckc coins
    :param msg: <person recieving tip> <random x y | x>
    :param user_id: the id of the user doing the tipping
    """
    msg = parse(msg)
    if msg is None: #no target user
        return ("error", "")
    form = {
        'user_id': user_id,
        'target_user': msg[0],
        'balance': get_balance(user_id),
        'amount': set_amount(msg[1:]),
    }
    if form["amount"] is None: #we recieved a non-int
        return ("error", "")
    form['transaction'] = make_transaction(user_id, form['target_user'], form['amount'])
    form['user_address'] = get_address(user_id)
    form['target_user_address'] = get_address(form['target_user'])
    form['user_balance'] = get_balance(user_id)
    form['target_user_balance'] = get_balance(form['target_user'])
    ############# fill out data
    tip_attachment = json.dumps([{
        "fallback":"<@{user_id}> tipped <@{target_user}> {amount} :SKC:".format(**form),
        "color": "good",
        "author_name": "SecKCoin Bank and Trust",
        "footer": "Please note: Transactions require at least one block confirmation in order to appear (Up to 5 minutes)",
        "fields": [
            {
                "title": ":skc: Transaction Hash:",
                "value": form['transaction'],
                "short": False
            },
            {
                "title": "From: ",
                "value": """<@{user_id}>
<https://seckco.in/address/{user_address}|{user_address}>
Current Balance: {user_balance}""".format(**form),
                "short": True
            },
            {
                "title": "To: ",
                "value": """<@{target_user}>
<https://seckco.in/address/{target_user_address}|{target_user_address}>
Current Balance: {target_user_balance}""".format(**form),
                "short": True
            }
        ]}], indent=4)

    currency_icon = ":skc:"
    tip_pretext = ":money_with_wings:"
    tip_posttext = " (View transaction on <https://seckco.in/tx/%s|https://seckco.in>)" % form['transaction']
    tip_message = "%s <@%s> => <@%s> %s %s %s" % (tip_pretext, user_id,
                                                  form['target_user'], form['amount'],
                                                  currency_icon, tip_posttext)

    return (tip_message, tip_attachment)

commands = {
    "tip": tip
}


help_text = [{
    'title': "tip:",
    'value': "Usage 'tipskc tip @username amount' -- This will transfer the specified amount of :skc: to the other user. Also available 'tipskc tip @username random low high'",
    'short': False
}]
