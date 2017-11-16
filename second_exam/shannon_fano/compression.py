from second_exam.common.abstractions import Compressor

class ShannonFanoEncoder(Compressor):
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
        
