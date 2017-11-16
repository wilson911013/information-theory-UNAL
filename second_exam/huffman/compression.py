import sys
import pickle
from second_exam.common.abstractions import Compressor

class HuffmanNode():
    def __init__(self, symbol=None, weight=0):
        self.right = None
        self.left = None
        self.symbol = symbol
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return "{ " + str(self.symbol) + " : " + str(self.weight) + " } "


class HuffmanEncoder(Compressor):
    def __init__(self, file_name, out_file="compressed.mau", symbol_size_in_bytes=1):
        super().__init__(file_name, out_file, symbol_size_in_bytes)

    def dfs(self, node, code):
        if node == None:
            return
        if node.symbol != None:
            self._code_table[node.symbol] = code
        self.dfs(node.left, code + "0")
        self.dfs(node.right, code + "1")

    def huffman_tree(self):
        table = self.probablity_table()
        treeNodes = []
        for symbol in table.keys():
            treeNodes.append(HuffmanNode(symbol, table[symbol]))

        treeNodes = sorted(treeNodes)
        while len(treeNodes) > 1:
            left = treeNodes.pop(0)
            right = treeNodes.pop(0)

            parent_weight = left.weight + right.weight
            parent = HuffmanNode(weight=parent_weight)
            parent.left = left
            parent.right = right
            treeNodes.append(parent)
            treeNodes = sorted(treeNodes)
        return parent

    def code_table(self):
        root = self.huffman_tree()
        self.dfs(root, "")
        return self._code_table


class HuffmanDecoder(HuffmanEncoder):
    def __init__(self, out_file="compressed.mau", decompressed_file="decompressed"):
        super().__init__(file_name="", out_file=out_file)
        self.decompressed_file = decompressed_file

    def probablity_table(self):
        with open(self.out_file + ".table", "rb") as f:
            table = pickle.load(f)
        return table

    def decode(self):
        code_table = self.code_table()
        root = self.huffman_tree()

        with open(self.out_file, "rb") as f:
            byte = f.read(1)
            additional = ord(byte)

            coded = ""
            byte = f.read(1)
            while byte != b"":
                coded += format(ord(byte), '08b')
                byte = f.read(1)

        decoded = []
        node = root
        assert(additional < 8 and additional >= 0)
        for bit in coded[: len(coded) - additional]:
            if bit == "0":
                node = node.left
            else:
                node = node.right

            if node.symbol != None:
                decoded.append(node.symbol)
                node = root

        with open(self.decompressed_file, "wb") as f:
            for byte in decoded:
                f.write(byte)
