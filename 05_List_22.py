uids = []
grades = []
grade = ['A','B+','B','C+','C','D+','D','F','A']
while True:
    x = input()
    if x=='q':
        break
    a,b = x.split()
    uids.append(a)
    grades.append(b)
x = input().split()
for i in x:
    grades[uids.index(i)]=grade[grade.index(grades[uids.index(i)])-1]
ans = []
for i in range(len(uids)):
    ans.append([uids[i],grades[i]])
ans.sort()
for a,b in ans:
    print(a,b)