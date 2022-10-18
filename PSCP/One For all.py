"""_"""
def main(xxx):
    """_"""
    sss = ""
    ans = ""
    for i in range(1, xxx+1):
        ccc = input()+','
        sss += ccc
        if i == xxx:
            ccc += '_'+ str(sss.count(','))
        elif i%2 == 1:
            ccc += '*'*sss.count(',')
        elif i%2 == 0:
            ccc += '-'*sss.count(',')
        ans += ccc
    print(ans.replace(',', ''))
main(int(input()))