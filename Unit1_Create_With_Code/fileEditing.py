with open("myTextFile.txt","r") as file:
    print(file.read())

list = ["a","b","c"]

for item in list:
    with open("myTextFile.txt","a") as file:
        file.write(item)
        file.write("\n")

with open("myTextFile.txt","r") as file:
    print(file.read())