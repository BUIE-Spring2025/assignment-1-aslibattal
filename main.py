def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    dict_roman = { 1000:"M", 900:"CM", 500: "D", 400: "CD", 100: "C", 90:"XC",50:"L", 40:"XL",10:"X", 9:"IX", 5:"V",4:"IV", 1: "I"}
    roman= ""
    for number, symbol in dict_roman.items():
        while num >= number:
            roman += symbol
            num -= number
    return roman
print(int_to_roman(3))
print(int_to_roman(58))
print(int_to_roman(400))
print(int_to_roman(1994))
print(int_to_roman(3999))
