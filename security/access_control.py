from config import AUTHORIZED_USERS

def is_user_authorized(user_id):
    return str(user_id) in AUTHORIZED_USERS
