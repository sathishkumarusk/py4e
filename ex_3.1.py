hrs=input('Enter the hours ')
hour=int(hrs)
rate=10.50
if hour<=40 :
    tel=hour*rate
    print(tel)
elif hour>40 :
    tel=(40*rate)+(hour-40)*1.5*rate
    print(tel)