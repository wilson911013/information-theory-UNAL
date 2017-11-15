from huffman.compression import HuffmanEncoder, HuffmanDecoder

encode = True

if encode:
    huffmanEncoder = HuffmanEncoder("test_files/c.wav")
    huffmanEncoder.encode()

    huffmanDecoder = HuffmanDecoder(decompressed_file="test_files/c_decompressed.wav")
    huffmanDecoder.decode()
