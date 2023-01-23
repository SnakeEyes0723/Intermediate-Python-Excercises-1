#Jacob Wieland
#I had to look up the try/except clauses for Python for this excercise, I found them here: https://docs.python.org/3/tutorial/errors.html
i = 0
sum = 0
while(i < 5):
    try:
        entry = int(input("Enter an integer: "))
        sum = sum + entry
        i = i + 1
    except ValueError:
        print("That was not a valid integer. Try again.")

print(sum)