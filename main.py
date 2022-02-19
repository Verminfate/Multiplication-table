from colorama import *

num1 = 15
num2 = 15

if num1 >= 100 or num2 >= 100:
    print(Fore.RED + "Please input numbers bellow 100 for propper formatting")
else:
    pass


two_row = False
if num2 >=10:
    two_row = True
else:
    two_row = False


def print_val(x):
    string = ""
    for i in range(1, num1 + 1):
        string += (f" {str(i * x).ljust(3, ' ')} ")
    print(string[1:3] + " ║" + Back.WHITE + Fore.BLACK + string + Back.RESET + Fore.RESET + "║")


x = 1
top_string = "     "
for i in range(1, num1 + 1):
    if i < 10:
        top_string += f"{i}    "
    else:
        top_string += f"{i}   "
print(top_string)
print("   ╔" + "═" * 5 * num1 + "╗")


for x in range(1, num2 + 1):
    print_val(x)
    x +=1


if two_row is True:
    print("   ╚" + "═" * 5*num1 + "╝")
else:
    print("   ╚" + "═" * 5*num1 + "╝")





