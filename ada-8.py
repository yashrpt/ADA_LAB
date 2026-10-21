
from typing import Dict
import heapq


# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


# Huffman Coding class
class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    # Build Huffman Tree
    def build_tree(self, frequencies: Dict[str, int]) -> Node:
        if not frequencies:
            raise ValueError("Frequencies cannot be empty")

        if any(freq <= 0 for freq in frequencies.values()):
            raise ValueError("Frequencies must be positive")

        if any(len(char) != 1 for char in frequencies):
            raise ValueError("Each key must be a single character")

        heap = [
            Node(char, freq)
            for char, freq in frequencies.items()
        ]
        heapq.heapify(heap)

        # Handle a single character
        if len(heap) == 1:
            self.root = heap[0]
            self.codes = {self.root.char: "0"}
            return self.root

        # Combine the two lowest-frequency nodes
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(
                None,
                left.freq + right.freq,
                left,
                right
            )

            heapq.heappush(heap, merged)

        self.root = heap[0]
        self.codes = {}
        return self.root

    # Generate binary codes
    def generate_codes(self) -> Dict[str, str]:
        if self.root is None:
            raise ValueError("Build the Huffman tree first")

        if self.codes:
            return self.codes

        def traverse(node, code):
            if node is None:
                return

            # Leaf node represents a character
            if node.char is not None:
                self.codes[node.char] = code or "0"
                return

            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(self.root, "")
        return self.codes


# Main program
if __name__ == "__main__":
    frequencies = {
        'A': 5,
        'B': 9,
        'C': 12,
        'D': 13,
        'E': 16,
        'F': 45
    }

    coder = HuffmanCoder()

    coder.build_tree(frequencies)
    codes = coder.generate_codes()

    print("Character Frequencies:")
    for char, freq in frequencies.items():
        print(f"{char}: {freq}")

    print("\nHuffman Codes:")
    for char, code in sorted(codes.items()):
        print(f"{char}: {code}")
