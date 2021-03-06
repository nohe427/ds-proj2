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
    if data is None or data is "":
        return None, None
    def _enumerate_count_of_characters(data: str) -> dict:
        chars = {}
        for char in data:
            if char in chars.keys():
                chars[char] += 1
            else:
                chars[char] = 1
        return chars
    def _sort_chars_to_heap(data: dict) -> list:
        ## See https://knowledge.udacity.com/questions/227455 for permission for heapq usage
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
                if curr_str == "":
                    map[node.char] = "0"
                else:
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
    if data is None or tree is None:
        return None
    decoded_str = ""

    if tree.left is None and tree.right is None:
        for _ in range(tree.frequency):
            decoded_str += tree.char
        return decoded_str

    base_root = tree
    for char in data:
        if char == '1':
            if base_root.right is not None:
                base_root = base_root.right
            else:
                decoded_str += base_root.char
                base_root = tree.right
        if char == '0':
            if base_root.left is not None:
                base_root = base_root.left
            else:
                decoded_str += base_root.char
                base_root = tree.left
    
    decoded_str += base_root.char

    return decoded_str

if __name__ == "__main__":
    print("\nTest 1 - Sample Test")

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("\nTest 2 - None Type Input")
    encoded_data, tree = huffman_encoding(None)
    print(encoded_data)
    # None
    print(tree)
    # None
    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)
    # None

    print("\nTest 3 - Single Letter Input")
    encoded_data, tree = huffman_encoding("f")
    print(encoded_data)
    # returns 0
    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)
    # returns f

    print("\nTest 4 - Empty String Input")
    encoded_data, tree = huffman_encoding("")
    print(encoded_data)
    # None
    print(tree)
    # None
    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)

    print("\nTest 5 - Repeated Single Character Input")

    a_great_sentence = "bbbbbbbbbbb"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))