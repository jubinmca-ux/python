start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

result = []

for num in range(max(start, 1000), min(end, 9999) + 1):
    if all(int(digit) % 2 == 0 for digit in str(num)):
        root = int(num ** 0.5)
        if root * root == num:
            result.append(num)

print("Numbers:", result)
