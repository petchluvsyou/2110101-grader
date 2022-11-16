nick = {
    'Robert':'Dick',
    'William':'Bill',
    'James':'Jim',
    'John':'Jack',
    'Margaret':'Peggy',
    'Edward':'Ed',
    'Sarah':'Sally',
    'Andrew':'Andy',
    'Anthony':'Tony',
    'Deborah':'Debbie',
    'Dick':'Robert',
    'Bill':'William',
    'Jim':'James',
    'Jack':'John',
    'Peggy':'Margaret',
    'Ed':'Edward',
    'Sally':'Sarah',
    'Andy':'Andrew',
    'Tony':'Anthony',
    'Debbie':'Deborah'
}
n = int(input())
for i in range(n):
    x = input()
    if x in nick.keys():
        print(nick[x])
    elif x in nick.values():
        print(list(nick))
    else:
        print('Not found')