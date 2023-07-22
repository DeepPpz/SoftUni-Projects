def letterize(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    hundreds = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    text = ''
    above_hundred = False
    
    if number < 0:
        text = "minus "
        number = abs(number)

    if 99 < number < 1000:
        text += f"{ones[number // 100]}-hundred and "
        number %= 100
        above_hundred = True

    if number == 0:
        if above_hundred:
            text = text.replace(" and ", "")
        else:
            text = "zero"
    
    elif number < 10:
        text += ones[number]
    
    elif number < 20:
        text += tens[number % 10]
    
    elif number < 100:
        if number % 10 == 0:
            text += f"{hundreds[number // 10]}"
        else:
            text += f"{hundreds[number // 10]} {ones[number % 10]}"
    
    elif number < 1000:
        text += f"{ones[number // 100]}-hundred"
    
    else:
        if "minus" in text:
            text = "too small"
        else:
            text = "too large"
    
    return text


for _ in range(int(input())):
    num = int(input())
    if not -99 <= num <= 99:
        result = letterize(num)
        print(result)
