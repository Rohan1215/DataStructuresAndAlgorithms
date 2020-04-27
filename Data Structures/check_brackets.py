# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    op= []
    for i, next in enumerate(text):
        if next in "([{":
            op.append([next,i])            
        if next in ")]}":
            if op:
                fig=op.pop(-1)
                if not are_matching(fig[0],next):
                    return i+1
            else:
                return i+1     
    if(op):
        return op[0][1]+1
    else:
        return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
