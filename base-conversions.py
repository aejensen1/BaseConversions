def generate_numeric_set(base):
    numeric_set = []

    # Add digits 0-9
    for i in range(10):
        if i < base:
            numeric_set.append(str(i))
    
    # Add letters A-Z (only if base > 10)
    if base > 10:
        for i in range(26):
            if len(numeric_set) < base:
                numeric_set.append(chr(i + 65))  # 65 is the ASCII value for 'A'
    
    # Add letters a-z (only if base > 36)
    if base > 36:
        for i in range(26):
            if len(numeric_set) < base:
                numeric_set.append(chr(i + 97))  # 97 is the ASCII value for 'a'
    
    # Ensure base does not exceed 62
    if base > 62:
        print(f"Base {base} is too large. The maximum base allowed is 62. Defaulting to base 62.")
        return generate_numeric_set(62)

    return numeric_set

def convert_base(number, base1, base2):
    if base1 == base2:
        return number
    if base1 == 10:
        return from_base_10(int(number), base2)
    else:
        return to_base_10(number, base1, base2)

def to_base_10(number, base1, base2):
    numeric_set = generate_numeric_set(base1)
    translated_digits = []
    
    for digit in str(number):
        translated_digits.append(numeric_set.index(digit))  # Convert each digit to its base1 value
    
    sum = 0
    index = 0  # Exponent for base1
    for digit in translated_digits[::-1]:  # Process digits from right to left
        sum += digit * (base1 ** index)
        index += 1
    
    return from_base_10(sum, base2)

def from_base_10(number, base):
    numeric_set = generate_numeric_set(base)
    if number == 0:
        return numeric_set[0]
    
    result = []
    while number > 0:
        remainder = number % base
        result.insert(0, numeric_set[remainder])  # Prepend the corresponding character
        number //= base
    
    return ''.join(result)

# Example of usage
print("-----------------------")
print("Base Conversion Program")
print("-----------------------")
print("Bases can range from 2 to 62, with digits 0-9 and letters A-Z and a-z")
print("-----------------------")
base1 = int(input("Type the base to convert from: "))
base2 = int(input("Type the base to convert to: "))
number = (input("Type the number to convert: "))

converted_number = convert_base(number, base1, base2)
print(f"Converted number: {converted_number}")
