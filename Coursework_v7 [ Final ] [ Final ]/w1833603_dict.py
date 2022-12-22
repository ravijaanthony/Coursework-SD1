# from w1833603_v11 import assignList
def assignValue(listValue):
    value0 = str(listValue[0])
    value1 = str(listValue[1])
    value2 = str(listValue[2])
    value3 = str(listValue[3])

    # duplicating code
    update = [value0, value1, value2, value3]
    return update


# This function will work on the dictionary "resultDict"
def functionDict(progressionOutcome, studentIDList, resultList, progressList, progressTrailerList, moduleRetrieverList, excludeList, resultDict):
    i = 0
    del resultDict[0]

    while i < len(resultList):
# Progress -->
        if resultList[i] == "Progress":
            
            for i in range(len(studentIDList)):
##                print(i)
                value = progressionOutcome[i]
                key = str(studentIDList[i][0:8])
                resultDict[key] = value
                continue

           # for key, value in resultDict.items():
           #     while True:
           #         print(key + " : " + assignValue(progressList)[0] + assignValue(progressList)[1] + "," +
           #               assignValue(progressList)[2] + "," + assignValue(progressList)[3])
           #         break
                break
            
        


# Trailer -->
        if resultList[i] == "Trailer":
            
            # Assigning the values to key, value in a dict
            for i in range(len(studentIDList)):
                value = progressionOutcome[i]
                key = str(studentIDList[i][0:8])
                resultDict[key] = value
                continue
            
##            # To print the dictionary line by line
##            for key, value in resultDict.items():
##                while True:
##                    print(key + " : " + assignValue(progressTrailerList)[0] + assignValue(progressTrailerList)[1] + "," +
##                          assignValue(progressTrailerList)[2] + "," + assignValue(progressTrailerList)[3])
##                    break
                break
          


# Retriever -->
        if resultList[i] == "Retriever":
            for i in range(2):
                value = progressionOutcome[i]
                key = str(studentIDList[i][0:8])
                resultDict[key] = value
##                print(i)
                continue
            
##            print(resultDict)

##            # To print the dictionary line by line
##            for key, value in resultDict.items():
##                while True:
##                    print(key + " : " + assignValue(moduleRetrieverList)[0] + assignValue(moduleRetrieverList)[1] + "," +
##                          assignValue(moduleRetrieverList)[2] + "," + assignValue(moduleRetrieverList)[3])
##                    break
                break

            


# Exclude -->
        if resultList[i] == "Exclude":
            for i in range(2):
                value = progressionOutcome[i]
                key = str(studentIDList[i][0:8])
                resultDict[key] = value
##                print(i)
                continue
            
            
##            # To print the dictionary line by line
##            for key, value in resultDict.items():
##                while True:
##                    print(key + " : " + assignValue(excludeList)[0] + assignValue(excludeList)[1] + "," +
##                          assignValue(excludeList)[2] + "," + assignValue(excludeList)[3])
##                    break
                break

                
        # Prints the dictionary
        

        i += 1
    print(resultDict)
