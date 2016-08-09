"""
seckcoin plugin to withdraw coins
"""
from common import make_transaction, set_amount

def parse(message):
    return map(str, message.split(" "))

def withdraw(msg, user_id):
    """
    :param msg: <wallet address> <amount>
    :param user_id: id of the user withdrawing their dosh
    withdraws some seckc coins to an external wallet
    """
    msg = parse(msg)
    form = {
        'user_id': user_id,
        'address': msg[0],
        'amount': set_amount(msg[1:])
    }
    if form['amount'] is None:
        return ("error", "")
    form['transaction'] = make_transaction(user_id, form['address'], form['amount'])
    withdraw_message = """<@{user_id}> => {address} {amount} :skc:
(View transaction on <https://seckco.in/tx/{transaction}|https:/seckco.in>)""".format(**form)
    withdraw_attachment = ""
    return (withdraw_message, withdraw_attachment)

commands = {
    'withdraw': withdraw,
}
help_text = [{
    'title': "withdraw:",
    'value': "Usage 'tipskc withdraw SecKCoinAddress amount' -- This will transfer :SKC: from the bot wallet to whatever address you specify (ex a Desktop wallet)",
    'short': False
}]
