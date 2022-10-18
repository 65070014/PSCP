"""DDD"""
def main(xxx, gib):
    """DAW"""
    if xxx == "iPhone 13 mini":
        print(gibb_(xxx, gib))
    elif xxx == "iPhone 13":
        if gibb_(xxx, gib).isdigit() == True:
            print(int(gibb_(xxx, gib))+4000)
        else:
            print(gibb_(xxx, gib))
    elif xxx == "iPhone 13 Pro":
        if gibb_(xxx, gib).isdigit() == True:
            print(int(gibb_(xxx, gib))+13000)
        else:
            print(gibb_(xxx, gib))
    elif xxx == "iPhone 13 Pro Max":
        if gibb_(xxx, gib).isdigit() == True:
            print(int(gibb_(xxx, gib))+17000)
        else:
            print(gibb_(xxx, gib))
    else:
        print("Not Available")
def gibb_(xxx, gib):
    """FIND"""
    if gib == "128 GB":
        return "25900"
    elif gib == "256 GB":
        return "29900"
    elif gib == "512 GB":
        return "37900"
    elif gib == "1 TB" and "Pro" in xxx:
        return "45900"
    else:
        return "Not Available"
main(input(), input())
