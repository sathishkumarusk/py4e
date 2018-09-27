#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
file=input('Enter the File Name: ')
fopen=open(file)
this=dict() # Creating Empty Dictionary named THIS
bigcount=None 
bigword=None
for ln in fopen: #reading the Given file 
    if ln.startswith('From:'):  #checknig line start with From:
        spl=ln.split() #Split the lines
        cont=spl[1] #sticking value[1] in to cont
        this[cont]=this.get(cont,0)+1 #adding the Key and Value into dic

for k,v in this.items(): #itreting Key and Value creating dict into tuple (Dict.item() will create )
    if bigcount is None or v > bigcount: 
        bigword=k
        bigcount=v
print(bigword, bigcount)