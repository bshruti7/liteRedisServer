msg_type_map = {
        '+': "SimpleString",
        '-': "Error",
        ':': "Integer",
        '$': "BulkStrings",
        '*': "Array"
    }

from collections import deque
import copy as cp

class RESPParser:

    @classmethod
    def split_by_delim(cls, data, sep):
        my_list = data.split(sep)
        list_wo_nulls = []

        for item in my_list:
            if item:
                list_wo_nulls.append(item)
        return list_wo_nulls

    @classmethod
    def process_bulk_string(cls, bulk_string):
        msg_type = [0]
        processed_string = ""
        return processed_string

    @classmethod
    def process_single_entity(cls, element):
        msg_type = element[0]
        output = f"Msg type {msg_type_map.get(msg_type)},{element[1:]}"
        return output

    @classmethod
    def process_elements(cls, elements):
        stack = deque()
        # remember to store type of elements
        n = len(elements)
        for i in range(n-1, -1, -1):
            elem = elements[i]
            msg_type = elem[0]
            if msg_type in ('+', '-', ':'):
                stack.append((msg_type_map.get(msg_type), elem[1:]))
            elif msg_type == '*':
                local_list = []
                list_size = int(elem[1:])
                for _ in range(list_size):
                    popped_elem = stack.pop()
                    local_list.append(popped_elem)

                stack.append(cp.deepcopy(local_list))

            elif msg_type in '$':
                elem_to_add = ""
                if int(elem[1:]) == -1:
                    elem_to_add = None
                elif int(elem[1:]) == 0:
                    elem_to_add = "Empty"
                else:
                    elem_to_add = stack.pop()
                stack.append((msg_type_map.get('$'), elem_to_add))
            else:
                stack.append(elem)

        return list(stack)

