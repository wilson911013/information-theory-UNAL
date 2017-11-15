import filecmp
import unittest

from second_exam.huffman.compression import HuffmanDecoder, HuffmanEncoder

class TestHuffman(unittest.TestCase):
    def test_encoding_text_files(self):
            huffmanEncoder = HuffmanEncoder("test_files/text.txt")
            huffmanEncoder.encode()

            huffmanDecoder = HuffmanDecoder(
                decompressed_file="test_files/text_decompressed.txt")
            huffmanDecoder.decode()

            assert(filecmp.cmp("test_files/text.txt",
                               "test_files/text_decompressed.txt", shallow=False))

