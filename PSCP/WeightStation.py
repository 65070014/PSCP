"""Wieght"""
def main():
    """Wieght"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = (num1*4)-(num2+num3+num4)
    if num2+num3+num4+num5 > 15000:
        print("Overweight")
    elif num2 < num1/2:
        print("Unbalance")
    elif num3 < num1/2:
        print("Unbalance")
    elif num4 < num1/2:
        print("Unbalance")
    elif num5 < num1/2:
        print("Unbalance")
    elif num2 > (num1/2)*3:
        print("Unbalance")
    elif num3 > (num1/2)*3:
        print("Unbalance")
    elif num4 > (num1/2)*3:
        print("Unbalance")
    elif num5 > (num1/2)*3:
        print("Unbalance")
    else:
        print("Pass "+'%.2f'%(num5))
main()
