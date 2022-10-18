"""PlanCD"""
def main():
    """PlanCD"""
    bbb = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if bbb == "Ascend":
        if num1 > num2:
            num1, num2 = num2, num1
        if num2 > num3:
            num2, num3 = num3, num2
        if num1 > num2:
            num1, num2 = num2, num1
        print('%.2f'%num1, '%.2f'%num2, '%.2f'%num3, sep=', ')
    elif bbb == "Descend":
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 < num3:
            num2, num3 = num3, num2
        if num1 < num2:
            num1, num2 = num2, num1
        print('%.2f'%num1, '%.2f'%num2, '%.2f'%num3, sep=', ')
main()
