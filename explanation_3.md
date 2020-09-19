# Huffman Encoding / Decoding Explanation
Encoding:
In this problem I used heapq which is a min-heap library to manage the priority queue so I could quickly grab the smallest priority items.  I then used a dictionary to store the characters corresponding binary representations so I could replace all the letters in a string without having to iterate over the binary tree that was generated of the characters.
The space complexity of this is O(n log(n)) as each character in the input will be stored only once in the tree and the returned encoded string will be matching the input in regards to length.
The runtime complexity of encoding is O(n) as each character in the input needs to be iterated over a couple of times and we drop constants in calculating runtime complexities.
Decoding:
I passed in the tree and iterated over the binary tree until all characters were found.
The space complexity of this is O(n) as we are returning the decoded string from an encoding string.  Each input results in one output and we are storing that output to be returned.
The runtime complexity of decoding is O(n) as we are traversing a binary tree looking for the resulting character. We iterate over each character exactly once to generate our results