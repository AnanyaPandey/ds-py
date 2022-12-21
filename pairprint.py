def printunordered(stringarray):
    for i in range(0,len(stringarray)):
        for j in range(i+1,len(stringarray)):
            print(stringarray[i] + ',' + stringarray[j])

printunordered('hello world')