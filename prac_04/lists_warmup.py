"""
CP1404 Practical
"""
numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] is 3
# numbers[-1] is 2
# numbers[3] is 1
# numbers[:-1] is [3, 1, 4, 1, 5, 9]
# numbers[3:4] is [1]
# 5 in numbers is True
# 7 in numbers is False
# "3" in numbers is False
# numbers + [6, 5, 3] is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1
numbers[0] = "ten"

# 2
numbers[-1] = 1

# 3
print(numbers[2:])

# 4
print(9 in numbers)