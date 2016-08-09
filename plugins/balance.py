'''
tipseckc bot module to retrieve a user's balance
'''
from common import get_balance


def balance(msg, user_id):
    '''
    :param msg: message - unused should be blank
    :param user_id: user's id - used to get balance
    '''
    user_balance = get_balance(user_id)
    form = {
        'user_id': user_id,
        'user_balance': user_balance
    }
    balance_message = "<@{user_id}>: Your balance: {user_balance} :skc: SecKCoins".format(**form)
    balance_attachment = [{}]
    return (balance_message,
            balance_attachment)

commands = {
    "balance": balance
}

help_text = [{
    'title': "balance:",
    'value': "Usage tipskc balance -- This will show your your current :skc: balance",
    'short': False
}]
