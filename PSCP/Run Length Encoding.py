"""EEE"""
def main():
    """AWSD"""
    xxx = input()
    xxx1 = list(xxx)
    xxx2 = []
    xx0 = 0
    i = 1
    j = 0
    while i < len(xxx1):
        if xxx1[i] == xxx1[i-1]:
            i += 1
        else:
            xxx2.append(i-j)
            xxx2.append(xxx1[i-1])
            j = i
            i += 1
    xxx2.append(i-j)
    xxx2.append(xxx1[i-1])
    for _ in range(0, len(xxx)+1, 2):
        xx0 += 4
    print(*xxx2[:xx0:], sep="", end="")
main()