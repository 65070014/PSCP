"""awdawf"""
def main():
    """dswa"""
    for _ in range(1, 11):
        ddd = 0
        xxx = input().replace('-', '')
        for j in xxx:
            ddd += int(j)
        try:
            if int(xxx) % int(ddd) != 0 or int(ddd) == 0 or xxx == 0:
                print("No")
            else:
                print("Yes")
        except ZeroDivisionError:
            print("No")
main()