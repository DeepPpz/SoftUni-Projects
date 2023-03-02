num = float(input())

result = ''

if num == 0:
    result = 'zero'
elif num > 0:
    if num < 1:
        result = 'small positive'
    elif num > 1000000:
        result = 'large positive'
    else:
        result = 'positive'

else:
    if abs(num) < 1:
        result = 'small negative'
    elif abs(num) > 1000000:
        result = 'large negative'
    else:
        result = 'negative'

print(result)