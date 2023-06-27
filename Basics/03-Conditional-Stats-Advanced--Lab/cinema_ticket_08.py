day = input()

if day in ['Monday', 'Tuesday', 'Friday']:
    print('12')
elif day in ['Wednesday', 'Thursday']:
    print('14')
elif day in ['Saturday', 'Sunday']:
    print('16')