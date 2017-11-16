import sys

from compression.huffman import HuffmanEncoder

algortihm = sys.argv[1]
input_file_name = sys.argv[2]
output_file_name = sys.argv[3]

if algortihm == "huffman" or algortihm == "h":
    huffmanEncoder = HuffmanEncoder(input_file_name, output_file_name)
    huffmanEncoder.encode()
else:
    print("The algorithm is not currently supported")