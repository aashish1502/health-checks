
def Ceaser(s):
    x=[]

    for i in s:
        if(i!='z'):
            x.append(chr(ord(i)+1))
        else:
            x.append('a')
    return ''.join(x)

def main():
    x=input()
    s=Ceaser(x)
    print(s)

main()
