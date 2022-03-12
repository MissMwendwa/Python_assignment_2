#propt user to input
User_says = input("Please enter a word to continue: ")

user_says = ["Quit", "quit"]
if user_says == 'Quit' or 'quit':
    class py_solution:
        def int_to_Roman(self, num):
            val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
            return roman_num

else: 
    print("Sorry we do not recognise the word!")