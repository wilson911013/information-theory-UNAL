from huffman import HuffmanEncoder, HuffmanDecoder

encode = True

if encode:
    huffmanEncoder = HuffmanEncoder("c.wav")
    huffmanEncoder.encode()

    huffmanDecoder = HuffmanDecoder(decompressed_file="c_decompressed.wav")
    huffmanDecoder.decode()
