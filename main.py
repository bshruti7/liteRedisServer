# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from serializer_deserializer import RedisPackager
import re

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    new_list = ["*2\\r\\n$4\\r\\necho\\r\\n*2\\r\\n+FirstWord\\r\\n+SecondWord\\r\\n"]

    list_of_messages = [
        "$-1\\r\\n",
        "*1\\r\\n$4\\r\\nping\\r\\n",
        "*2\\r\\n$4\\r\\necho\\r\\n$11\\r\\nhello world\\r\\n",
        "*2\\r\\n$3\\r\\nget\\r\\n$3\\r\\nkey\\r\\n",
        "+OK\\r\\n",
        "-Error message\\r\\n",
        "$0\\r\\n\\r\\n",
        "+hello world\\r\\n",
        "*2\\r\\n$4\\r\\necho\\r\\n*2\\r\\n+FirstWord\\r\\n+SecondWord\\r\\n",
        ":7\\r\\n",
        "$6\\r\\nShruti\\r\\n",

    ]
    redis_client_obj = RedisPackager()
    redis_client_obj.process_multiple_messages(list_of_messages)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
