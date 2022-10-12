numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0] Answer: 3
numbers[-1] Answer: 2
numbers[3] Answer: 1
numbers[:-1] Answer: [3, 1, 4, 1, 5, 9]
numbers[3:4] Answer: [1]
5 in numbers Answer: True
7 in numbers Answer: False
"3" in numbers Answer: False
numbers + [6, 5, 3] Answer: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""
numbers[0] = "ten"
numbers[6] = 1
print(numbers[2:7])
print(9 in numbers)
