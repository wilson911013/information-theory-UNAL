import sys

def compress():
    with open("lzwEncoder.exe", "rb") as f:
        byte = f.read(1)
        while byte != b"":
            sys.stdout.write(str(ord(byte)) + "\n")
            byte = f.read(1)
compress()