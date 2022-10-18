"""sss"""
def main():
    """sss"""
    eiei = 10
    zaza = 0
    total = 0
    total2 = 0
    for zaza in range(1, eiei+1):
        zaza = int(input())
        if zaza <= 10:
            total += zaza
            zaza += 1
    for zaza in range(1, eiei+1):
        zaza = int(input())
        if zaza <= 10:
            total2 += zaza
            zaza += 1
    if total < total2:
        print("A")
    elif total2 < total:
        print("B")
    else:
        print("AB")
main()
