def is_leap(year):
    leap = False
    
    x=year/4
    y=year/100

    if(x%2==0):
        leap=True
        if(y%2==0):
            leap=False
            if(year%400==0):
                leap=True

    
    return leap

year = int(input())
print(is_leap(year))