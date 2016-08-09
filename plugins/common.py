'''
common functions used in other files
'''
import random

def set_amount(msg):
    if msg:
        if msg[0].lower() == "random":
            try:
                return random.randint(int(msg[1]), int(msg[2]))
            except:
                return None
        else:
            try:
                return int(msg[0])
            except:
                return None
    else:
        return None

#these three need real logic
def make_transaction(userid, target_user, amount):
    #client.sendfrom(user_id, user_address(target_user), amount)
    return "random hash here"


def get_balance(user_id):
    #return client.getbalance(user_id)
    return 50


def get_address(user_id):
    return "user id hash"

commands = {}
