year = int(input('Enter the year in YYYY format :'))
if year %4 == 0:
    if year %400 == 0:
        if year %100 == 0:
            print('Entered Year is a leap year')
        else:
            print('Entered Year is not a leap year')
    else:
        print('Entered Year is not a leap year')
else:
    print('Entered Year is not a leap year')
    