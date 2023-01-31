print("--- Book Title Character Counter ---")

while True:
    string = input("Enter the title of the book: ")
    numChars = str(len(string))

    response = input("The length is "+numChars+" characters long. Type 'yes' to run the program again: ")

    if response.lower() != "yes":
        break