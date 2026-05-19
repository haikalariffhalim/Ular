seq = ""

try:
    with open("preproinsulin-seq-clean.txt", "r") as file:
        seq = file.read()
except:
    print("ERROR")

try:
    with open("lsinsulin-seq-clean.txt", "w") as file1:
        file1.write(seq[:24])
except:
    print("ERROR")


try:
    with open("binsulin-seq-clean.txt", "w") as file1:
        file1.write(seq[24:54])
except:
    print("ERROR")


try:
    with open("cinsulin-seq-clean.txt", "w") as file1:
        file1.write(seq[54:89])
except:
    print("ERROR")


try:
    with open("ainsulin-seq-clean.txt", "w") as file1:
        file1.write(seq[89:])
except:
    print("ERROR")
