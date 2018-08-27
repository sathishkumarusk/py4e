sc=input('Enter the Score between 0.0 - 1.0 ')
scr=float(sc)
if scr>1.0:
    print('the score is out of range')
elif scr >= 0.9:
    print('A')
elif scr >= 0.8:
    print('B')
elif scr >= 0.7:
    print('C')
elif scr >= 0.6:
    print('D')
elif scr < 0.6:
    print('F')