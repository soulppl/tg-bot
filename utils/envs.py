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

