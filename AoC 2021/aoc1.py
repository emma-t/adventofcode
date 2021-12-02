def count(l):
    count=0
    for i in range(len(l)-3):
        if l[i]+l[i+1]+l[i+2]<l[i+1]+l[i+2]+l[i+3]:
            count=count+1
    print(count)

questions=[]
lines=open('aoc1.txt').read().splitlines()
for line in lines:
    test=line.split('\t')
    questions.append(int(test[0]))

count(questions)
