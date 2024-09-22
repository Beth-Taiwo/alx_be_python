user_input = int(input("Enter the size of the pattern: "))
rows = 0
while rows < user_input:
    for i in range(user_input):
        print("*", end="")
    print()
    rows += 1