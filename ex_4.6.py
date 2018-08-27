def computepay(h, r):
    if h < 40:
        hrs = h * r
        return hrs
    elif h > 40 :
        hrs = (40*r)+(h-40)*1.5*r
    return hrs
hour=input('Enter the hours ')
rate=input('Enter the rate')
h=int(hour)
r=float(rate)
pay=computepay(h, r)
print(pay)