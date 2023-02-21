import os
from dotenv import load_dotenv, find_dotenv


def print_envs(os):
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))


def get_forum_id():
    load_dotenv(find_dotenv())
    forum_id = os.getenv("FORUM_ID")
    return forum_id


def get_user_info_topic_id():
    load_dotenv(find_dotenv())
    topic_user_info_id = os.getenv("TOPIC_USER_INFO_ID")
    return topic_user_info_id


def get_rules_info_link():
    load_dotenv(find_dotenv())
    rules_info_link = os.getenv("RULES_INFO_LINK")
    return rules_info_link


def get_auth_user_message_timeout():
    load_dotenv(find_dotenv())
    auth_user_message_timeout = os.getenv("AUTH_USER_MESSAGE_TIMEOUT")
    return auth_user_message_timeout


