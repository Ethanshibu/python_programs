def wrap(string, max_width):
    s = list(string)
    c=1
    for i in range(len(s)):
        if (i+1)%max_width == 0:
            s.insert(i+c,'\n')
            c+=1
    result = str(''.join(s))
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
