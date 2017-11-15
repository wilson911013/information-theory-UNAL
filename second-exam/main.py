from huffman import HuffmanEncoder

huffmanEncoder = HuffmanEncoder("wind_of_change.wav")
code_table = huffmanEncoder.code_table()
huffmanEncoder.encode() 