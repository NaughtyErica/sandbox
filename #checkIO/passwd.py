def checkio(data: str) -> bool:
    check_num = False
    check_upper = False
    check_lower = False
    if len(data) >= 10:
        for char in data:
            if char.isdigit():
                check_num = True
            elif char.isupper():
                check_upper = True
            elif char.islower():
                check_lower = True
            elif not char.isalpha():
                return False
        if check_upper and check_num and check_lower:
            return True
        else:
            return False
    else:
        return False

# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasas5454asasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
