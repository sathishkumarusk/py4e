#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
file=input('Enter the file Name: ')
rd=open(file)
count=0
fin=0
for ln in rd:
    if ln.startswith('X-DSPAM-Confidence:'):
        rf=ln.find(' ')
        pr=ln[rf:]
        ans=pr.rstrip()
        count=count+1
        ts=float(ans)
        fin=ts + fin
tt=float(count)
res=fin/tt
print('Average spam confidence:', res)