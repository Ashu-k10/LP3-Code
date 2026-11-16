# Huffman Encoding
import heapq
from collections import Counter

class Node:
    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

def make_codes(root, code, codes):
    if root is None:
        return
    if root.left is None and root.right is None:
        codes[root.char] = code if code else "0"
        return
    make_codes(root.left, code + "0", codes)
    make_codes(root.right, code + "1", codes)

text = input("Enter text: ")
if not text:
    print("No text entered.")
else:
    frequency = Counter(text)
    heap = []
    order = 0
    for char, count in frequency.items():
        heapq.heappush(heap, (count, order, Node(char, count)))
        order += 1

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)
        parent = Node(None, freq1 + freq2, left, right)
        heapq.heappush(heap, (parent.frequency, order, parent))
        order += 1

    root = heap[0][2]
    codes = {}
    make_codes(root, "", codes)

    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(repr(char), ":", code)

    encoded_text = "".join(codes[char] for char in text)
    print("\nEncoded text:", encoded_text)