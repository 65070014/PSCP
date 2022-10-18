"""Laststand"""
def main():
    """Laststand"""
    xxx = input().replace('[', '').replace(']', '').split(',')
    for _ in range(1, len(xxx)+1):
        ccc = xxx.pop(0)
        print(ccc[len(ccc)-1:len(ccc)])
main()