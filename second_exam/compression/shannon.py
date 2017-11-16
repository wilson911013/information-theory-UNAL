from . import abstractions
import pickle

class ShannonFanoEncoder(abstractions.Compressor):
    def __init__(self, file_name, out_file="compressed.mau", symbol_size_in_bytes=1):
        super().__init__(file_name, out_file, symbol_size_in_bytes)

    def shannon_recursion(self, sorted_table, code_so_far):
        if len(sorted_table) == 1:
            self._code_table[sorted_table[0][0]] = code_so_far
            return
        else:
            set_1 = []
            set_2 = []

            for element in sorted_table:
                if sum(x[1] for x in set_1) < sum(x[1] for x in set_2):
                    set_1.append(element)
                else:
                    set_2.append(element)

            self.shannon_recursion(set_1, code_so_far + "0")
            self.shannon_recursion(set_2, code_so_far + "1")

    def code_table(self):
        table = self.probablity_table()
        sorted_table = sorted(table.items(), key=lambda x: x[1], reverse=True)
        self.shannon_recursion(sorted_table, "")
        return self._code_table
        
class ShannonFanoDecoder(ShannonFanoEncoder):
    def __init__(self, out_file="compressed.mau", decompressed_file="decompressed", symbol_size_in_bytes=1):
        super().__init__(file_name="", out_file=out_file,
                         symbol_size_in_bytes=symbol_size_in_bytes)
        self.decompressed_file = decompressed_file

    def probablity_table(self):
        with open(self.out_file + ".table", "rb") as f:
            table = pickle.load(f)
        return table

    def decode(self):
        code_table = self.code_table()
        decode_table = { code_table[key] : key for key in code_table.keys() }

        with open(self.out_file, "rb") as f:
            byte = f.read(1)
            additional = ord(byte)

            coded = ""
            byte = f.read(1)
            while byte != b"":
                coded += format(ord(byte), '08b')
                byte = f.read(1)
            
        decoded = []
        matching_string = ""

        assert(additional < 8 and additional >= 0)
        
        for bit in coded[: len(coded) - additional]:
            if matching_string in decode_table.keys():
                decoded.append( decode_table[matching_string] )
                matching_string = ""
            matching_string += bit

        if(matching_string in decode_table.keys()):
            decoded.append( decode_table[matching_string] )

        with open(self.decompressed_file, "wb") as f:
            for byte in decoded:
                f.write(byte)
