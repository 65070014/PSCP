"""Frame"""
def main():
    """print frame"""
    num = int(input())
    numn = int(input())
    num3 = (numn//2)
    num4 = 1
    for i in range(numn//2):
        print(' '*num3+'*'*num)
        num3 = num3-1
    print('*'*num)
    for i in range(1, numn//2+1):
        print(' '*i+'*'*num)
        num4 = num4+1
main()
