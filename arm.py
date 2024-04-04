start_range = int(input("Enter the start range: "))
end_range = int(input("Enter the end range: "))

print(f"Armstrong numbers in the range {start_range} to {end_range}:")

for num in range(start_range, end_range + 1):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = 0
    
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    
    if armstrong_sum == num:
        print(num)
