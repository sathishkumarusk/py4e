small=None
large=-1
while True:
    num=input('Enter the Numbers ')
    if num == 'done':
        break
    try :
        number=int(num)
    except:
        print ('Invalid input')
        continue
    if small is None :
        small = number
    if number > large :
        large=number
    elif number < small:
        small = number

print ('Maximum is', (large))
print ('Minimum is', (small))