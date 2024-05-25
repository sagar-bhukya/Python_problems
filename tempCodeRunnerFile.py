import pandas as pd
# dictionary problem
di={"sl":[1,2,3,4],
    "student":["A","B","C","D"],
    "ph":[50,30,90,80],
    "ch":[60,70,40,80],
    "mt":[67,80,60,75]}


di['total']=[]
di['avg']=[]
di['grade']=[] 
for i,j,k,l,m in zip(di['sl'],di['student'],di['ph'],di['ch'],di['mt']):
    to=k+l+m
    di['total'].append(to)

    avg=to/4
    di['avg'].append(avg)
    if avg >=60 and avg<100:
        di['grade'].append("A")
    elif avg >=50 and avg<60:
        di['grade'].append("B")
    else:
        di['grade'].append("C")

print(di)
data=pd.DataFrame(di)
print(data)


