from w1833603_dict import functionDict
from w1833603_dict import assignValue

"""
I declare that my work contains no examples of misconduct, such as plagiarism, or
collusion.
Any code taken from other sources is referenced within my code solution.

Student ID: 20200624
Author: Ravija Vitharana
Date: 26th October 2022
Deadline: Thursday 7th December 2022 BEFORE 1:00 pm
"""



''' Part 1 - Main Version '''



# Variables
userInput = 'y'
result = ''
passMark = 0
deferMark = 0
failMark = 0

globalPassMark = 0
globalDeferMark = 0
globalFailMark = 0

globalProgressCounter = 0
globalExclude = 0
globalProgressTrailer = 0
globalModuleRetriever = 0

progressTrailer = 0
progress = 0
moduleRetriever = 0
exclude = 0
studentCount = 1

progressTrailerList = [0, 0, 0, 0]
progressList = [0, 0, 0, 0]
moduleRetrieverList = [0, 0, 0, 0]
excludeList = [0, 0, 0, 0]

resultList = []

progressResult = ''
trailerResult = ''
excludeResult = ''
retrieverResult = ''

studentID = ''

resultDict = {0: None}

value0 = 0
value1 = 0
value2 = 0
value3 = 0

progressionOutcome = []
studentIDList = []

counter = 0


# Printing the list data as per the requirements
def printListData(listValue):
    # Data printing from a list
    length = len(listValue)
    
    for i in range(0, length, 4):
        print(listValue[i], end="- ")

        for j in range(1 + i, 4 + i):
            print(listValue[j], end=",")


# Funtion to validate the range of mark entered
def rangeValidation(message, error="Integer Required"):
    while True:
        try:
            mark = int(input(message))

            if mark > 120:
                print(error)
                continue
            
            if mark % 20 != 0:
                print(error)

        except ValueError:
            print(error)
            continue

        else:
            return mark


# To store the progression outcomes in the first come basis
def assignList(listValue):
    global progressionOutcome
    progressionOutcome += [list(listValue)]
    return progressionOutcome
    

# Calculating the credit score
def creditScore(passMark, deferMark, failMark):
    while userInput == 'y':
        global studentID
        global resultList
        global studentIDList

        while True:
            studentID = input("Enter student ID (Eg: w1234567): ").lower()
            int_studentID = studentID[1:8]

            if len(studentID) != 8:
                print("Invalid student ID\nStudent ID should only have 8 characters\n")
                continue

            if studentID[0] != 'w':
                print("Student ID must start with 'w'\n")
                continue

            if not int_studentID.isdigit():
                print("Student ID must follow format (Eg: w1833603)\n")

            else:
                break
        j = 0

        studentIDList += [studentID]
        
        while 0 < len(studentID) == 8:
            while True:
                error = "Out of range"
                
                try:
                    passMark = int(input("Enter pass mark: "))

                    if passMark % 20 != 0:
                        print(error)
                        print()
                        continue

                        
                    deferMark = int(input("Enter defer mark: "))

                    if deferMark % 20 != 0:
                        print(error)
                        print()
                        continue

##                    if 120 < passMark + deferMark > 121:
##                        print(error)
##                        continue

                    
                    failMark = int(input("Enter fail mark: "))

                    if failMark % 20 != 0:
                        print(error)
                        print()
                        continue
                    
                    total = passMark + deferMark + failMark
            
                    # Exception Handling for total != 120
                    if total != 120:
                        print("Total Incorrect\n")

                except ValueError:
                    print("Integer required\n")
                    continue
                break
            
            
            
##            passMark = rangeValidation("Enter Pass mark: ", "Pass Mark Out of Range")
##            deferMark = rangeValidation("Enter Defer mark: ", "Defer Mark Out of Range")
##            failMark = rangeValidation("Enter Fail mark: ", "Fail Mark Out of Range")
                
##            total = passMark + deferMark + failMark
            
            # Exception Handling for total != 120
##            if total > 120 or total <= 0:
##                print("\'Total Incorrect\'")
##
##                passMark = int(input("Enter Pass mark: "))
##                deferMark = int(input("Enter Defer mark: "))
##                failMark = int(input("Enter Fail mark: "))
##

# Progress -->
            #For assign list  function
            global counter
            counter += 1

            if passMark == 120 and deferMark == 0 and failMark == 0:
                global result

                progressResult = "Progress"

                resultList += [progressResult]

                # The result
                print(progressResult)

                # writing data to the list
                progressList[0] = "Progress "
                progressList[1] = passMark
                progressList[2] = deferMark
                progressList[3] = failMark

                # Printing the list data with the requirements
                assignList(progressList)

                return progressList, resultList#, globalProgressList


# Trailer -->
            elif passMark == 100 and deferMark <= 20 and failMark <= 20:
                trailerResult = "Trailer"
                
                # The result
                print("Progress (module trailer)")

                # to add the data to the list and call later for the histogram
                resultList += [trailerResult]

                # # writing data to the list
                progressTrailerList[0] = "Progress (module trailer) "
                progressTrailerList[1] = passMark
                progressTrailerList[2] = deferMark
                progressTrailerList[3] = failMark

                # Printing the list data with the requirements
##                printListData(progressTrailerList)

                assignList(progressTrailerList)
            
                return progressTrailerList, resultList
            
# Exclude -->
            elif passMark <= 40 and deferMark <= 40 and 80 <= failMark <= 120:
                excludeResult = "Exclude"

                # to add the data to the list and call later for the histogram
                resultList = resultList + [excludeResult]

                # The result
                print(excludeResult)


                # # writing data to the list
                excludeList[0] = "Exclude "
                excludeList[1] = passMark
                excludeList[2] = deferMark
                excludeList[3] = failMark

                # To store the user inputs in order
                assignList(excludeList)
                
                return excludeList, resultList


# Retriever -->
            elif passMark <= 80 and deferMark <= 120 and failMark <= 60:
                retrieverResult = "Retriever"

                # to add the data to the list and call later for the histogram
                resultList = resultList + [retrieverResult]
                

                # The result
                print("Module retriever")

                # # writing data to the list
                moduleRetrieverList[0] = "Retriever "
                moduleRetrieverList[1] = passMark
                moduleRetrieverList[2] = deferMark
                moduleRetrieverList[3] = failMark

                # To store the user inputs in order
                assignList(moduleRetrieverList)
                
                return moduleRetrieverList, resultList

        j += 1
    return resultList, progressionOutcome


# Function to calculate and print the histogram
def histogram(globalProgress, globalProgressTrailer, globalModuleRetriever, globalExclude, resultList, trailerResult,
              progressResult, retrieverResult, excludeResult):

    # histogram
    print("\n---------------------------------------------------------------")
    print("Histogram")

    i = 0
    trailerCount = 0
    progressCount = 0
    retrieverCount = 0
    excludeCount = 0

    for i in range(len(resultList)):

        if resultList[i] == "Trailer":
            trailerCount += 1
            i += 1
            continue

        if resultList[i] == "Progress":
            progressCount += 1
            i += 1
            continue

        if resultList[i] == "Retriever":
            retrieverCount += 1
            i += 1
            continue

        if resultList[i] == "Exclude":
            excludeCount += 1
            i += 1
            continue
        
    # Histogram star pattern
    print("Progress     " + str(progressCount) + "  : ", "* " * progressCount,
          "\nProgressTrailer " + str(trailerCount) + " : ", "* " * trailerCount,
          "\nModuleRetriever " + str(retrieverCount) + " : ", "* " * retrieverCount,
          "\nExclude       " + str(excludeCount) + " : ", "* " * excludeCount)

    print("\nStudents in total: ", len(resultList))

##    print(globalProgressTrailer + globalProgress + globalModuleRetriever + globalExclude, "outcomes in total")

    print("---------------------------------------------------------------")


creditScore(passMark, deferMark, failMark)


# Loop continue and exit
while userInput != 'q':
    print("\nWould you like to enter another set of data?")
    userInput = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
    print()

    if userInput == 'y':
        creditScore(passMark, deferMark, failMark)

    elif userInput == 'q':
        histogram(globalProgressCounter, globalProgressTrailer, globalModuleRetriever, globalExclude, resultList,
                  trailerResult, progressResult, retrieverResult, excludeResult)

    else:
        print("Invalid User Input")


# This function is for the list 
def listExtention(resultList, progressList, progressTrailerList, moduleRetrieverList, excludeList, progressionOutcome):
    i = 0
    index = progressionOutcome[i][0]
##    print(resultList)

    for i in range(len(resultList)):
# Progress -->
        if index == "Progress ":
            printListData(progressionOutcome[i])
            print()
            i+=1

# Trailer -->
        if index == "Progress (module trailer) ":
            printListData(progressionOutcome[i])
            print()
            i+=1
# Retreiver -->
        if index == "Retriever ":
            printListData(progressionOutcome[i])
            print()
            i+=1
            
# Exclude -->
        if index == "Exclude ":
            printListData(progressionOutcome[i])
            print()
            i+=1
            
    i += 1



''' Part 2 List (extension)'''

print("\nPart 2:")
listExtention(resultList, progressList, progressTrailerList, moduleRetrieverList, excludeList, progressionOutcome)



''' Part 3 - Text File (extension) '''

print("\nPart 3\nData has been appended to file \'data.txt\'")


# Auto closing file

with open("data.txt", "a") as f:
    i = 0
    f.write("\nPart 3\n")

    for i in range(len(resultList)):
##        print('resultList',resultList)

# Progress -->
        if resultList[i] == "Progress":
            trailer = progressionOutcome [i]
            progressionOutcome = assignList(progressList)
            f.write(str(trailer)+ '\n')
##            print()            
            continue


# Trailer -->
        elif resultList[i] == "Trailer":
            trailer = progressionOutcome [i]
            progressionOutcome = assignList(progressTrailerList)
            f.write(str(trailer)+ '\n')
##            print()            
            continue

# Retriever -->
        if resultList[i] == "Retriever":
            trailer = progressionOutcome [i]
            progressionOutcome = assignList(moduleRetrieverList)
            f.write(str(trailer)+ '\n')
##            print()            
            continue


# Exclude -->
        if resultList[i] == "Exclude":
            trailer = progressionOutcome [i]
            progressionOutcome = assignList(excludeList)
            f.write(str(trailer)+ '\n')
##            print()            
            continue
    i += 1



''' Part 4 – Dictionary (separate program)'''
print("\nPart 4")
functionDict(progressionOutcome, studentIDList, resultList, progressList, progressTrailerList, moduleRetrieverList, excludeList, resultDict)


