"""files.py"""
"name.txt"

# 1
name = input("Name: ")
out_file = open("name.txt", "w")
print(f"{name}", file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

# 3
in_file = open("number.txt", "r")
first = int(in_file.readline().strip())
second = int(in_file.readline().strip())
sum_of_first_and_second = first + second
print(sum_of_first_and_second)
in_file.close()

# 4
in_file = open("number.txt", "r")
accumulation_of_all_numbers = 0
for line in in_file:
    accumulation_of_all_numbers += int(line.strip())
print(accumulation_of_all_numbers)

