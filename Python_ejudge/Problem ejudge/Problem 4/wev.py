n = int(input("Enter a decimal number: "))
k = int(input("Enter the digit position (1-indexed): "))
result = []

if 0 <= n <= 1000000000 and 1 <= k <= 10:
    hex_digit_mapping = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    while n > 0:
        remain = n % 16
        n //= 16
        if remain in hex_digit_mapping:
            result.append(hex_digit_mapping[remain])
        else:
            result.append(str(remain))
    
    if k - 1 > len(result):
        print("0")
    else:
        print(result[-k])  # Extract k-th digit from the right
else:
    print("Invalid input")
