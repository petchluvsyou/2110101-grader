def index_of(grades, ID):
    ans = -1
    for i in range(len(grades)):
        if ID == grades[i][0]:
            ans = i
    return ans
def upgrade(grades, IDs):
    grade = ['A','B+','B','C+','C','D+','D','F','A']
    x = IDs
    for i in x:
        for j in range(len(grades)):
            if i == grades[j][0]:
                grades[j][1] = grade[grade.index(grades[j][1])-1]
    grades.sort()

exec(input())
exec(input())
exec(input())
