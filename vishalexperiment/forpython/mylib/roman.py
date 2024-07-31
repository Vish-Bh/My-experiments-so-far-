def decimal2roman(num):
    num_val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    roman_val = [
        "M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // num_val[i]):
            roman_num += roman_val[i]
            num -= num_val[i]
        i += 1
    print(roman_num)

decimal2roman(10343)

def roman2decimal(num):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for i in range(len(num)):
        if i > 0 and roman[num[i]] > roman[num[i - 1]]:
            decimal += roman[num[i]] - 2 * roman[num[i - 1]]
        else:
            decimal += roman[num[i]]
    print(decimal)

roman2decimal('MC')