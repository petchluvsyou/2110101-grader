def to_Thai( N ):
    N = str(N)
    x = len(N)
    d = {
        '0':'soon',
        '1':'neung',
        '2':'song',
        '3':'sam',
        '4':'si',
        '5':'ha',
        '6':'hok',
        '7':'chet',
        '8':'paet',
        '9':'kao',
        }
    while len(N)!=4:
        N='0'+N
    if N[0]=='0': print('',end='')
    else: print(d[N[0]]+' pun ',end='')
    if N[1]=='0': print('',end='')
    else: print(d[N[1]]+' roi ',end='')
    if N[2]=='0': print('',end='')
    elif N[2]=='1': print('sip ',end='')
    elif N[2]=='2': print('yi sip ',end='')
    else: print(d[N[2]]+' sip ',end='')
    if N[3]=='0' and x==1: print('soon',end=' ')
    elif N[3]=='0': print('',end='')
    elif N[3]=='1' and x!=1: print('et',end=' ')
    else: print(d[N[3]],end=' ')
    return ''

exec(input().strip())

#print(to_Thai(2222))