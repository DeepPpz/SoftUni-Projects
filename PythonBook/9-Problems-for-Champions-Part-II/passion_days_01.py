from decimal import Decimal

budget = Decimal(input())
command = input()
purchases = 0

while command != "mall.Enter":
    command = input()
    
while True:
    command = input()
        
    if command == "mall.Exit":
        break

    for char in command:
        price = 0
            
        if char.isalpha():
            if char.isupper():  # upper
                price = Decimal(0.50) * ord(char)
        
            elif char.islower(): # lower
                price = Decimal(0.30) * ord(char)
        
        elif char == "%": # %
            price = Decimal(0.50) * budget
            if budget <= 0:
                continue
        
        elif char == "*":  # *
            budget += Decimal(10)
            continue
        
        else:
            price = ord(char)
        
        if price <= budget:
            purchases += 1
            budget -= Decimal(price)
        
if not purchases:
    print(f"No purchases. Money left: {budget:.2f} lv.")
else:
    print(f"{purchases} purchases. Money left: {budget:.2f} lv.")
