import sys

class HuffmanCompression():
    def compress(file):
        pass

    def decompress(file):
        pass

class HuffmanNode():
    def __init__(self, symbol=None, weight=0):
        self.rigth = None
        self.left = None
        self.symbol = symbol
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return "{ " + str(self.symbol) + " : " + str(self.weight) + " } "

class HuffmanEncoder():
    def __init__(self, file_name):
        self.file_name = file_name

    def probablity_table(self):
        table = {}

        with open(self.file_name, "rb") as f:
            byte = f.read(1)
            while byte != b"":
                if byte not in table.keys():
                    table[byte] = 0
                table[byte] += 1

                byte = f.read(1)
        return table

    def huffman_tree(self):
        table = self.probablity_table()
        treeNodes = []
        for symbol in table.keys():
            treeNodes.append( HuffmanNode(symbol, table[symbol]) )
        treeNodes = sorted(treeNodes)
        
        for treeNode in treeNodes:
            print(str(treeNode))

    def encode():
        pass