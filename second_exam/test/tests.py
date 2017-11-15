import filecmp
import unittest

from second_exam.huffman import HuffmanDecoder, HuffmanEncoder

class HuffmanTest(unittest.TestCase):
    def test_encoding_text_files(self):
            huffmanEncoder = HuffmanEncoder("text.txt")
            huffmanEncoder.encode()

            huffmanDecoder = HuffmanDecoder(
                decompressed_file="text_decompressed.txt")
            huffmanDecoder.decode()

            assert(filecmp.cmp("text.txt", "text_compressed.txt", shallow=False))
