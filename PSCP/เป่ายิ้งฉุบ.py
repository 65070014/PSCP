"""เป่าเป่า"""
def main():
    """เป่ายิ้งฉุบบบบบ"""
    var = input()
    xxx = 0
    total = 0
    total2 = 0
    for i in range(2, len(var)+1, 2):
        score = 0
        scoree = 0
        xdd = var[xxx:i:]
        xxx += 2
        if xdd == "PR":
            score = 1
        if xdd == "RP":
            scoree = 1
        if xdd == "SP":
            score = 1
        if xdd == "PS":
            scoree = 1
        if xdd == "RS":
            score = 1
        if xdd == "SR":
            scoree = 1
        total += score
        total2 += scoree
    if total > total2:
        print("A win", end=" ")
        print(total, total2, sep='-')
    elif total < total2:
        print("B win", end=" ")
        print(total2, total, sep='-')
    else:
        print("DRAW", total)
main()