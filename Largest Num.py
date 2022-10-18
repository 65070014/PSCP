"""LargestNumber"""
def ngong():
    """Largest Num"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    numa = str(num1)+str(num2)+str(num3)
    numa2 = str(num1)+str(num3)+str(num2)
    numb = str(num2)+str(num1)+str(num3)
    numb2 = str(num2)+str(num3)+str(num1)
    numc = str(num3)+str(num1)+str(num2)
    numc2 = str(num3)+str(num2)+str(num1)
    numx = int(numa)
    if numa < numa2:
        numx = int(numa2)
    if numx < int(numb):
        numx = int(numb)
    if numx < int(numb2):
        numx = int(numb2)
    if numx < int(numc):
        numx = int(numc)
    if numx < int(numc2):
        numx = int(numc2)
    print(numx)
ngong()
