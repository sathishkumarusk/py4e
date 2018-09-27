#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
file=input('Enter the File Name: ')
fopen=open(file)
mylist=list()
for lin in fopen: #going and reading line by line
    spl=lin.split() # spliting the line into LIST
    for itr in spl: #Itreting the LIST one by one
        if itr not in mylist: #Chcking the List the Itreting data in or not
            mylist.append(itr) #addig to the list
mylist.sort()
print(mylist)