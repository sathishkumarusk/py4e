# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
file=input('Enter the File Name:')
this=dict()                                 #creating the Empty Dic
fopen=open(file)                            
for wds in fopen:
    if wds.startswith('From '):             #Searching Line Starts with FROM
        spl=wds.split()                     #spliting in to list
        ind=spl[5]                          #taking index '5' (Time)
        col=ind.split(':')                  #spliting time using ':' as a delimiter
        ver=col[0]                          #taking index 0 (Hours)
        this[ver]=this.get(ver,0)+1         #checking and adding to the dic with count
st=sorted(this.items())                     #Sorting the Dics as a tuples
for k, v in st:                             #Itretting the Key/Value from the tuple ST
    print(k,v)