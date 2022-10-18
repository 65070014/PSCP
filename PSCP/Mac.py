"""DOC"""
def main(mac):
    """DWAD"""
    macc = mac.replace(':', '').replace('-', '').replace('.', '')
    count, number = 0, 0
    check = ""
    if '-' in mac:
        for i in macc:
            count += 1
            if count == 2:
                i += '-'
                count = 0
            check += i
        number = 1
    elif ':' in mac:
        for i in macc:
            count += 1
            if count == 2:
                i += ':'
                count = 0
            check += i
        number = 2
    elif '.' in mac:
        for i in macc:
            count += 1
            if count == 4:
                i += '.'
                count = 0
            check += i
        number = 3
    if count_al(mac) == 1 or len(macc) != 12:
        print("ERROR")
    elif mac == check[0:len(check)-1]:
        print("VALID", number)
    else:
        print("ERROR")
def count_al(mac):
    """COUNT"""
    countal = 0
    alpha = list('GgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$%^&*)_+=~/|')
    for i in alpha:
        if mac.count(i) > 0:
            countal = 1
    return countal
main(input())
