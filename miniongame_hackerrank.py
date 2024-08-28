def minion_game(string1):
    s=list(string)
    scoreboard = {"Stuart":0,"Kevin":0}
    vow = []
    cons = []
#for consonant stuart
    for i in range(len(s)):
        if s[i].lower() not in 'aeiou':
            for j in range(i,len(s)+1):
                if s[i:j] not in cons:
                    cons.append(s[i:j])
                    scoreboard["Stuart"] += string.count(string[i:j])
            for j in range(len(s)-i):
                if s[i:j] not in cons:
                    cons.append(s[i:j])
                    scoreboard["Stuart"] += string.count(string[i:j])
#for vowel kevin
    for i in range(len(s)):
        if s[i].lower() in 'aeiou':
            for j in range(i,len(s)+1):
                if s[i:j] not in vow:
                    vow.append(s[i:j])
                    scoreboard["Stuart"] += string.count(string[i:j])
            for j in range(len(s)-i):
                if s[i:j] not in vow:
                    vow.append(s[i:j])
                    scoreboard["Stuart"] += string.count(string[i:j])
                    
    if scoreboard["Stuart"] > scoreboard["Kevin"]:
        print("Stuart",scoreboard["Stuart"])
    else:
        print("Kevin",scoreboard["Kevin"])
    print()
    print(vow)
    print()
    print(cons)
    print()
    print(string)
    print(s)


string=input("enter the string : ")
minion_game(string)
