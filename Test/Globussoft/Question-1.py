def num_ways_dp(s):
    old = new = 1
    for i in range(len(s)-1):
        if int(s[i:i+2]) > 26: old = 0 
        if int(s[i+1]) == '0': new = 0 
        (old, new) = (new, old + new)
    return new

if __name__ == '__main__':
    number = input()
    while number != '0':
        print(num_ways_dp(number))
        number = input()