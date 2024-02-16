def replace_digit_stringifiy(n: int) -> int:
    string = str(n)
    new_string = string.replace("0", "5")
    return int(new_string)

def replace_digit_reverse_and_rebuild(n: int) -> int:
    if n == 0:
        return 5
    
    temp = 0

    is_negative = n < 0
    if is_negative:
        n = abs(n)

    while n > 0:
        last_digit = n % 10

        if last_digit == 0:
            last_digit = 5
        
        temp = temp * 10 + last_digit

        n //= 10

    result = 0
    while temp > 0:
        result = result * 10 + temp % 10
        temp //= 10
    
    if is_negative:
        return -result
    
    return result


if __name__ == "__main__":
    # input, expected
    tests = [
        (120, 125),
        (0, 5),
        (5, 5),
        (100, 155),
        (-100, -155)
    ]

for input, expected in tests:
    got = replace_digit_stringifiy(input)
    if got != expected:
        print("Failed test case. Got: {}, Wanted: {}", got, expected)

    got = replace_digit_reverse_and_rebuild(input)
    if got != expected:
        print("Failed test case. Got: {}, Wanted: {}", got, expected)