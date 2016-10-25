my_string = raw_input("Enter the String to search: ")
my_old_string = my_string
my_string = my_string.lower()

filenames = ['A.txt', 'B.txt', 'D.txt' ] #File in drive to read

for files in filenames[:]:
    print("\nCurrently reading:", files)
    file = open(files, 'r')
    alllines = file.readlines()
    file.close()
    count = 0
    for eachline in alllines:
        eachline = eachline.lower()
        eachword = eachline.split()
        for word in eachword:
            word = word.lower()
            if (word == my_string):
                count+=1

    if (count == 0):
        print("\n\tString not found at ", files)
    else:
        print('\n\t\tTotal Word', my_old_string + ' found: ', count)
        print('\n\t\tFile name: ', files)
