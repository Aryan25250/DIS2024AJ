while True:
    string = input("Enter title to count words for: ").split()

    numWords = len(string)

    plural = "s"
    if numWords == 1:
        plural = ""

    response = "Your title is "+str(numWords)+" word"+plural+" long."

    if numWords > 2:
        response += " Amazon product titles with 3 or more words don't sell as well. It is recommend that you shorten your title to 2 words or less."

    print(response)

    runAgainResponse = input("Respond with 'yes' to run the program again: ")

    if runAgainResponse.lower() != "yes":
        break

