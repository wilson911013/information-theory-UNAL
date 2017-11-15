from huffman import HuffmanEncoder

huffmanEncoder = HuffmanEncoder("goo.txt")
#table = huffmanEncoder.probablity_table()
#print(table)
code_table = huffmanEncoder.code_table()
huffmanEncoder.encode() 