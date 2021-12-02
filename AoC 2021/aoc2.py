def move(l):
    h=0
    d=0
    aim=0
    for i in range(len(l)):
        if l[i][0]=="f":
            h=h+int(l[i][-1])
            d=d+aim*int(l[i][-1])
        elif l[i][0]=="d":
            #d=d+int(l[i][-1])
            aim=aim+int(l[i][-1])
        else:
            #d=d-int(l[i][-1])
            aim=aim-int(l[i][-1])

    
    print(h*d)

questions=[]
lines=open('aoc2.txt').read().splitlines()
for line in lines:
    test=line.split('\t')
    questions.append(test[0])

move(questions)
