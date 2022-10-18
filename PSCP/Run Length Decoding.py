"""EEE"""
def main():
    """AWSD"""
    xxx = input()
    num = ""
    xxd = ""
    for i in xxx:
        if i.isalpha():
            xxd += i* int(num)
            num = ""
        else:
            num += i
    print(xxd, num)
main()