"""DAWD"""
def main():
    """DOC"""
    xxx = input()
    ccc = input()
    vvv = len(xxx)
    if ccc == "Domestic" and vvv == 9:
        print(xxx[0:1:], xxx[1:5:], xxx[5:9])
    elif ccc == "Domestic" and vvv == 10:
        print(xxx[0:2:], xxx[2:6:], xxx[6:10])
    elif ccc == "International" and vvv == 9:
        print("+66", xxx[1:5:], xxx[5:9])
    elif ccc == "International" and vvv == 10:
        print("+66"+ xxx[1:2:], xxx[2:6:], xxx[6:10])
main()
