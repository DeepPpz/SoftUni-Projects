number = int(input())

text = ''

if number < 20:
    if number < 10:
        if number == 0:
            text = 'zero'
        elif number == 1:
            text = 'one'
        elif number == 2:
            text = 'two'
        elif number == 3:
            text = 'three'
        elif number == 4:
            text = 'four'
        elif number == 5:
            text = 'five'
        elif number == 6:
            text = 'six'
        elif number == 7:
            text = 'seven'
        elif number == 8:
            text = 'eight'
        elif number == 9:
            text = 'nine'

    else:
        if number == 10:
            text = 'ten'
        elif number == 11:
            text = 'eleven'
        elif number == 12:
            text = 'twelve'
        elif number == 13:
            text = 'thirteen'
        elif number == 14:
            text = 'fourteen'
        elif number == 15:
            text = 'fifteen'
        elif number == 16:
            text = 'sixteen'
        elif number == 17:
            text = 'seventeen'
        elif number == 18:
            text = 'eighteen'
        elif number == 19:
            text = 'nineteen'

elif 20 <= number < 100:
    if number // 10 == 2:
        text = 'twenty'
    elif number // 10 == 3:
        text = 'thirty'
    elif number // 10 == 4:
        text = 'forty'
    elif number // 10 == 5:
        text = 'fifty'
    elif number // 10 == 6:
        text = 'sixty'
    elif number // 10 == 7:
        text = 'seventy'
    elif number // 10 == 8:
        text = 'eighty'
    elif number // 10 == 9:
        text = 'ninety'

    if number % 10 == 1:
        text += ' one'
    elif number % 10 == 2:
        text += ' two'
    elif number % 10 == 3:
        text += ' three'
    elif number % 10 == 4:
        text += ' four'
    elif number % 10 == 5:
        text += ' five'
    elif number % 10 == 6:
        text += ' six'
    elif number % 10 == 7:
        text += ' seven'
    elif number % 10 == 8:
        text += ' eight'
    elif number % 10 == 9:
        text += ' nine'

elif number == 100:
    text = 'one hundred'

print(text)