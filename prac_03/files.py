# 1. Ask for the user's name and write it to name.txt using open/close
name = input("Enter your name: ")
name_file = open("name.txt", "w")
name_file.write(name)
name_file.close()

# 2. Read the name from name.txt and greet the user (new independent block)
name_file = open("name.txt", "r")
name_in_file = name_file.read().strip()
name_file.close()
print(f"Hi {name_in_file}!")

# 3. Read the first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
    print(first_number + second_number)

# 4. Print the total of all numbers in numbers.txt (any number of lines)
with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line)
    print(total)
