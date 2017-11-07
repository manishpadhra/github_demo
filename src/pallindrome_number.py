# TODO: Find all one digit to 10 digit numbers for which abcd * 4 = dcba

def find_all_pallindrome_numbers():
    for number in range(1000,10000):
        rev_number=int(str(number)[::-1])
        prod=number*4
        if prod == rev_number:
            print(number)


find_all_pallindrome_numbers()