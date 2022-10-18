"""Surprising"""
def main():
    """Surprising"""
    num1 = float(input())
    num2 = float(input())
    num3 = num1-num2
    if num3 > num2:
        num3 -= num2
        if num2 - num3 > 2:
            print("Surprising")
        else:
            print("Not surprising")
    elif num2 <= 2:
        print("Not surprising")
    else:
        print("Surprising")
main()