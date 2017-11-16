import sys
import pickle

class Algorithm():
    def __init__(self, file_name, out_file="compressed.mau", symbol_size_in_bytes=1):
        self.file_name = file_name
        self.out_file = out_file
        self._code_table = {}
        self.symbol_size_in_bytes = symbol_size_in_bytes

    def probablity_table(self):
        table = {}

        with open(self.file_name, "rb") as f:
            byte = f.read(self.symbol_size_in_bytes)
            while byte != b"":
                if byte not in table.keys():
                    table[byte] = 0
                table[byte] += 1

                byte = f.read(self.symbol_size_in_bytes)
        return table
    
    def code_table():
        raise NotImplementedError("Please Implement this method")


class Compressor(Algorithm):
    def __init__(self, file_name, out_file="compressed.mau", symbol_size_in_bytes=1):
        super().__init__(file_name, out_file, symbol_size_in_bytes)

    def encode(self):
        code = ""
        code_table = self.code_table()
        with open(self.file_name, "rb") as f:
            byte = f.read(self.symbol_size_in_bytes)
            while byte != b"":
                code += code_table[byte]
                byte = f.read(self.symbol_size_in_bytes)

        with open(self.out_file, "wb") as f:
            additional = 0
            while len(code) % 8 != 0:
                code += "0"
                additional += 1

            f.write(bytes([additional]))

            i = 0
            while i < len(code):
                byte_str = code[i: i + 8]
                number = int(byte_str, 2)
                to_write = bytes([number])
                f.write(to_write)
                i += 8

        with open(self.out_file + ".table", "wb") as f:
            pickle.dump(self.probablity_table(), f, pickle.HIGHEST_PROTOCOL)
    
