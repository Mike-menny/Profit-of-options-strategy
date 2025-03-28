with open("menny.txt", 'r') as file:
    lines = file.readlines()
call=[]
put=[]
t0=[]
t1=[]
ind=0

for i in range(0,8):
    t0.append(int((max((lines[2*i].split()[2]),(lines[2*i+1].split()[2])))))
print(t0)

for i in range(0,8):
    strike=lines[2*i].split()[0]
    prediction=[(23000,0.3),(22500,0.6),(22000,0.1)]
    payoff=0
    for i in range(3):
        if prediction[i][0]<int(strike):
            payoff+=0
        else:
            payoff+=(prediction[i][0]-int(strike))*prediction[i][1]
    t1.append(payoff)

for i in range(8):
    print(lines[2*i].split()[0],t1[i]+t0[i]*(3.8/1200+1))
    

