print("\n=== Product Title Counter ===")

while True:
    string = input("\nEnter title or 'q' to quit: ")

    if string.lower() == "q":
        quit()

    numWords = len(string.split())

    response = "Word count: "+str(numWords)
    print(response)

    if numWords > 2:
        print("\n⚠️ WARNING ⚠️")
        print("Product titles longer than 2 words don't sell as well. It is recommended to shorten your title to 2 words or less.")