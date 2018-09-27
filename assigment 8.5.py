#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
file=input('Enter the File Name :')
fopen=open(file)
count=0
for lin in fopen:   #Reading line by line from file
    if lin.startswith('From:'): #Chekcing if line startswith From:
        spl=lin.split() #if Yes the split the Line (LIST)
        count=count+1
        print(spl[1]) #Printing index[1] that is the position of mail ID's
print('There were', count,'lines in the file with From as the first word')