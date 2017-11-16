import sys

from compression.huffman import HuffmanEncoder
from compression.shannon import ShannonFanoEncoder

algortihm = sys.argv[1]
input_file_name = sys.argv[2]
output_file_name = sys.argv[3]

if algortihm == "huffman" or algortihm == "h":
    huffmanEncoder = HuffmanEncoder(input_file_name, output_file_name)
    huffmanEncoder.encode()
elif algortihm == "shannon" or algortihm == "s":
    shannonFanoEncoder = ShannonFanoEncoder(input_file_name, output_file_name)
    shannonFanoEncoder.encode()
else:
    print("The algorithm is not currently supported")