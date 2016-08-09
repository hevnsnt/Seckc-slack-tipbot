"""
returns seckcoin address
"""
import json
from common import get_address

def deposit(msg, user_id):
    """
    returns user address
    :param msg: msg - unused - should be blank
    :user_id: user's id - used to get the wallet address and for flavor text
    """
    form = {
        'user_id': user_id,
        'user_address': get_address(user_id)
    }
    deposit_message = "<@{user_id}> your :skc: address is: {user_address}".format(**form)
    deposit_attachment = json.dumps(
        [{"fallback": "https://seckco.in/qr/{user_address}".format(**form),
          "color" : "good",
          "author_name" : "SecKCoin Bank and Trust",
          "image_url" : "https://seckco.in/qr/{user_address}".format(**form),
         }])
    return (deposit_message,
            deposit_attachment)

commands = {
    'deposit': deposit
}

help_text = [{
    'title': "balance:",
    'value': "Usage tipskc balance -- This will show your your current :skc: balance",
    'short': False
}]
