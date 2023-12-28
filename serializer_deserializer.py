# "$-1\r\n"
# "*1\r\n$4\r\nping\r\n”
# "*2\r\n$4\r\necho\r\n$11\r\nhello world\r\n”
# "*2\r\n$3\r\nget\r\n$3\r\nkey\r\n”
# "+OK\r\n"
# "-Error message\r\n"
# "$0\r\n\r\n"
# "+hello world\r\n”


# Need to parse the inputs
# Decode what kind of message it is
# Identify a suitable response
# Encode a response
# Return a response
from RESPParser import RESPParser


class RedisPackager:

    def __init_(self, messages):
        self.messages = messages

    def process_multiple_messages(self, messages):
        for message in messages:
            self.deserialize(message)

    # Serialization: converting an object into a series of bytes for storage or transmission across devices
    def serialize(self):
        pass

    # Deserialization: reconstructing an object from a series of bytes or a string to
    # instantiate the object for consumption
    def deserialize(self, message):
        original_msg = message
        output = ""
        elements = RESPParser.split_by_delim(message, "\\r\\n")
        output = RESPParser.process_elements(elements)

        # Put data into the correct data structure
        print(f"Message {original_msg}, {elements}, Output: {output[0]}")







