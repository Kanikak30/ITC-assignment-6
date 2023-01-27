class idk():
    def __init__(me, list1):
        me.inp = list1
        me.out = []

    def sum(me):
        for i in me.inp:
            for j in me.inp:
                for k in me.inp:
                    if (i + j + k) ==0 and sorted([i,j,k]) not in me.out : me.out.append(sorted([i,j,k]))

add = idk(list(map(int,input().split())))
#print(add.inp)
add.sum()
print(add.out)
