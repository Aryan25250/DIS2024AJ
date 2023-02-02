print("\n=== Product Title Counter ===")

while True:
    string = input("\nEnter title or 'q' to quit: ")

    if string.lower() == "q":
        break

    numWords = len(string.split())

    response = "Word count: "+str(numWords)
    print(response)

    if numWords > 5:
        print("\n⚠️ WARNING ⚠️")
        print("Product titles longer than 5 words don't sell as well. It is recommended to shorten your title for optimal sales.")