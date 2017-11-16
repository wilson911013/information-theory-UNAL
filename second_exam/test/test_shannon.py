import filecmp
import unittest

import second_exam.compression.shannon as shannon


class TestShannon(unittest.TestCase):
    def compress_and_decompress_util(self, original_file, decompressed_file):
        shannonFanoEncoder = shannon.ShannonFanoEncoder(original_file)
        shannonFanoEncoder.encode()

        shannonFanoDecoder = shannon.ShannonFanoDecoder(decompressed_file=decompressed_file)
        shannonFanoDecoder.decode()

        assert(filecmp.cmp(original_file, decompressed_file, shallow=False))

    def test_encoding_text_files(self):
        original_file = "test_files/text.txt"
        decompressed_file = "test_files/text_decompressed.txt"
        self.compress_and_decompress_util(original_file, decompressed_file)

    # def test_encoding_wav_files(self):
    #     original_file = "test_files/c.wav"
    #     decompressed_file = "test_files/c_decompressed.wav"
    #     self.compress_and_decompress_util(original_file, decompressed_file)

    # def test_encoding_long_wav_files(self):
    #     original_file = "test_files/wind_of_change.wav"
    #     decompressed_file = "test_files/wind_of_change_decompressed.wav"
    #     self.compress_and_decompress_util(original_file, decompressed_file)
