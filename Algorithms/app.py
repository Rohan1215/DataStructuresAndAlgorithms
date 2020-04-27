import sys

def get_change(m):
    c=0
    c+=m//10
    m=m%10
    c+=m//5
    m=m%5
    c+=m
    return c

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
