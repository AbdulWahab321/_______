data_a = ""
data_b = ""
with open("sample1.txt") as f:
    data_a = f.read()
with open("sample2.txt") as f2:
    data_b = f2.read()
def swap():
    filename = input("filename: ")
    if filename == "sample1.txt":
        print(data_b)
    elif filename == "sample2.txt":
        print(data_a)

while True:
    swap()
