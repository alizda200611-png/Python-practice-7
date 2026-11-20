total = float(input("Enter starting number: "))
user_input = 0
while user_input != "enough":
    user_input = input("enter a number or 'enough':")
    if user_input == "enough":
        break
    operator = input(" +, -, *, / ") 
    u = float(user_input)    
    if operator == "+":
        total += u
        print(total)
    elif operator == "-":
        total -= u
        print(total)
    elif operator == "*":
        total *= u
        print(total)
    elif operator == "/" and u == 0:
        print("cannot be divide by zero")
    elif operator == "/":
        total /= u
        print(total)
    else:
        print("invalid operator")
