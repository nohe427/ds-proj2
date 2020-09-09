# Huffman Encoding / Decoding Explanation
Encoding:
In this problem I used heapq which is a min-heap library to manage the priority queue so I could quickly grab the smallest priority items.  I then used a dictionary to store the characters corresponding binary representations so I could replace all the letters in a string without having to iterate over the binary tree that was generated of the characters.
Decoding:
I passed in the tree and iterated over the binary tree until all characters were found.