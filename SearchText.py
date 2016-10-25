myString = input("Enter the String to search: ")
myOldString = myString
myString = myString.lower()

filenames = ['A.txt', 'B.txt', 'D.txt' ] #File in drive to read

for files in filenames[:]:
    print ("\nCurrently reading:", files)
    file = open(files, 'r')
    alllines = file.readlines()
    file.close()
    count = 0
    for eachline in alllines:
        eachline = eachline.lower()
        eachword = eachline.split()
        for word in eachword:
            word = word.lower()
            if word == myString:
                count+=1
    if (count  == 0):
        print ("\n\tString not found at ", files)
    else:
        print ('\n\t\tTotal Word',myOldString + ' found: ', count)
        print ('\n\t\tFile name: ',files)
