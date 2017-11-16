import sys

from compression.huffman import HuffmanDecoder
from compression.shannon import ShannonFanoDecoder

algortihm = sys.argv[1]
input_file_name = sys.argv[2]
output_file_name = sys.argv[3]

if algortihm == "huffman" or algortihm == "h":
    huffmanDecoder = HuffmanDecoder(input_file_name, output_file_name)
    huffmanDecoder.decode()
elif algortihm == "shannon" or algortihm == "s":
    shannonFanoDecoder = ShannonFanoDecoder(input_file_name, output_file_name)
    shannonFanoDecoder.decode()
else:
    print("The algorithm is not currently supported")
