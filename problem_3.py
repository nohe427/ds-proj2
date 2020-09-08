import sys
## See https://knowledge.udacity.com/questions/227455
import heapq

class Node(object):
    def __init__(self, char=None, frequency=None):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None
    def __lt__(self, value):
        return self.frequency < value.frequency
    def __eq__(self, value):
        return self.frequency == value.frequency
    def __str__(self):
        return f"Character {self.char}, Frequency {self.frequency}"
    def __repl__(self):
        return f"Character {self.char}, Frequency {self.frequency}"

def huffman_encoding(data: str):
    def _enumerate_count_of_characters(data: str) -> dict:
        chars = {}
        for char in data:
            if char in chars.keys():
                chars[char] += 1
            else:
                chars[char] = 1
        return chars
    def _sort_chars_to_heap(data: dict) -> list:
        ## See https://knowledge.udacity.com/questions/227455
        sorted_list = sorted(data.items(), key = lambda x: x[1])
        h = []
        for item in sorted_list:
            new_node = Node(item[0], item[1])
            heapq.heappush(h, (item[1], new_node))
        return h
    def _build_tree(h):
        while(len(h) > 1):
            elem_left = heapq.heappop(h)
            elem_right = heapq.heappop(h)
            new_node = Node(frequency=(elem_left[1].frequency + elem_right[1].frequency))
            new_node.left = elem_left[1]
            new_node.right = elem_right[1]
            heapq.heappush(h, (new_node.frequency, new_node))
        return h[0][1]
    def _generate_char_map(node, map, curr_str):
        if node:
            _generate_char_map(node.left, map, curr_str+"0")
            if node.char:
                map[node.char] = curr_str
            _generate_char_map(node.right, map, curr_str+"1")
    char_count = _enumerate_count_of_characters(data)
    sorted_chars = _sort_chars_to_heap(char_count)
    h = _build_tree(sorted_chars)
    char_map = {}
    _generate_char_map(h, char_map, "")
    for key, value in char_map.items():
        data = data.replace(key, value)
    return data,h

def huffman_decoding(data,tree):
    decoded_str = ""

    

    return decoded_str

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
    # a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))