with open("menny.txt", 'r') as file:
    lines = file.readlines()

def payoff(s1,s2):
    prediction=[(23000,0.3),(22500,0.6),(22000,0.1)]
    payoff=0
    for i in range(3):
        if prediction[i][0]<s1:
            payoff+=s1-prediction[i][0]
        elif prediction[i][0]>s2:
            payoff+=prediction[i][0]-s2
    return payoff

t0call=[]
t0put=[]
pay=[]

for i in range(0,8):
    t0call.append(int((max((lines[2*i].split()[2]),(lines[2*i+1].split()[2])))))
print(t0call)
for i in range(0,8):
    t0put.append(int((max((lines[2*i+16].split()[2]),(lines[2*i+17].split()[2])))))
print(t0put)

for i in range(8):
    for j in range(i,8):
        print(21800+200*i,21800+200*j,t0call[j]+t0put[i],payoff(21800+200*i,21800+200*j),payoff(21800+200*i,21800+200*j)-(3.8/1200+1)*(t0call[j]+t0put[i]))


