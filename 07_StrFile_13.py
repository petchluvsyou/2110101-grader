inp = input()
cum = []
word = ''
for x in inp:
    if 'a'<=x<='z' or 'A'<=x<='Z' or '0'<=x<='9':
        word+=x
    else:
        if len(word)!=0:
            cum.append(word)
        word = ''
if len(word)!=0:
    cum.append(word)
c = 0
for word in cum:
    if c==0:
        print(word.lower(),end='')
        c+=1
    else:
        print(word[0].upper()+word[1:].lower(),end='')