jobs = []

def getJobsString():
    if len(jobs) == 0:
        return "You don't have any jobs in your to-do list\n"
    else:
        jobText = ""

        for i in range(len(jobs)):
            jobText += str(i+1)+". "+jobs[i]+"\n"

        return jobText

def addJob():
    jobName = input("Enter the name of the job you would like to add: ")
    jobs.append(jobName)

def removeJob():
    completed = False

    while not completed:
        jobIndex = int(input("Enter the number of the job you would like to remove: ")) - 1
        if not len(jobs) > jobIndex or len(jobs) <= 0:
            print("Entry doesn't exist")
        else:
            del jobs[jobIndex]
            completed = True

while True:
    thisJobs = getJobsString()
    print(thisJobs)

    finalResponse = None
    canRemove = False

    if len(jobs) > 0:
        canRemove = True

    while not finalResponse:
        inputText = "What would you like to do?\n(1) Add\n"
        if canRemove:
            inputText += "(2) Remove\n"

        response = input(inputText)

        if response == "1" or response.lower() == "add":
            finalResponse = "add"
        elif (response == "2" or response.lower() == "remove") and canRemove:
            finalResponse = "remove"

    if finalResponse == "add":
        addJob()
    elif finalResponse == "remove":
        removeJob()
