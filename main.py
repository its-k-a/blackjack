Card1 = int(input("Enter card number: "))
Card2 = int(input("Enter card number: "))

Card_sum = Card1 + Card2

is_21_or_over = Card_sum >= 21

print("You have 21 or over : " + str(is_21_or_over))