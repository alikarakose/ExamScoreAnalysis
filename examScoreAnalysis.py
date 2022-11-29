import numpy as np
import matplotlib.pyplot as plt


noten=np.genfromtxt('examScores.csv',delimiter=",")

print(noten.shape)

hu=0.3
vort=0.3
klasur=0.4


matrikel=np.arange(1,len(noten)+1)
matrik2=matrikel.reshape([len(noten),1])


myNoten=np.concatenate((matrik2,noten),axis=1)

hausgaben=myNoten[:,1:4]
hausgabenDurch=hausgaben.mean(axis=1)
hasugabenMeanmitmatrik=np.concatenate((matrik2,hausgabenDurch.reshape([len(noten),1])),axis=1)

gesamtenote=(hu*hausgabenDurch)+(vort*myNoten[:,4])+(klasur*myNoten[:,5])
gesamtenote

gesamtmitmatrik=np.concatenate((matrik2,gesamtenote.reshape([len(noten),1])),axis=1)
gesamtmitmatrik


hasugabenMeanmitmatrik

gesamtmitmatrik


#%% Spalte der Liste, den Durchschnitt, die beste und die schlechteste Note mit argmin



print("Durchschnitt HA1 =  ", myNoten[:,1].mean(axis=0))
print("Beste HA1 id =  ",myNoten[np.argmin(myNoten[:,1])][0], "mit note", myNoten[np.argmin(myNoten[:,1])][1])

print("Durchschnitt HA2 =  ", myNoten[:,2].mean(axis=0))
print("Beste HA2 id =  ",myNoten[np.argmin(myNoten[:,2])][0], "mit note", myNoten[np.argmin(myNoten[:,2])][2])

print("Durchschnitt HA3 =  ", myNoten[:,3].mean(axis=0))
print("Beste HA3 id =  ",myNoten[np.argmin(myNoten[:,3])][0], "mit note", myNoten[np.argmin(myNoten[:,3])][2])

print("Durchschnitt HH =  ", hausgabenDurch.mean(axis=0))
print("Beste HH id =  ",myNoten[np.argmin(hausgabenDurch)][0], "mit note", myNoten[np.argmin(hausgabenDurch)][2])

print("Durchschnitt Vortrag =  ", myNoten[:,4].mean(axis=0))
print("Beste Vortrag id =  ",myNoten[np.argmin(myNoten[:,4])][0], "mit note", myNoten[np.argmin(myNoten[:,4])][2])

print("Durchschnitt Klasur =  ", myNoten[:,5].mean(axis=0))
print("Beste Klasur id =  ",myNoten[np.argmin(myNoten[:,5])][0], "mit note", myNoten[np.argmin(myNoten[:,5])][2])

print("Insgesamt Durchschnitt =  ", gesamtenote.mean(axis=0))
print("Insgesamt Beste =  ", gesamtmitmatrik[np.argmin(gesamtenote)][0],"mit note ",gesamtmitmatrik[np.argmin(gesamtenote)][1] )
print("Insgesamt Schlechteste id =  ", gesamtmitmatrik[np.argmax(gesamtenote)][0],"mit note ",gesamtmitmatrik[np.argmax(gesamtenote)][1] )


#%% mit argwhere
print("beste h1 sind " , myNoten[np.argwhere(myNoten[:,1]==myNoten[:,1].min())])  #h1

print("beste h2 sind " ,myNoten[np.argwhere(myNoten[:,2]==myNoten[:,2].min())][:,0,[0,2]])  #h2

print("beste h3 sind " ,myNoten[np.argwhere(myNoten[:,3]==myNoten[:,3].min())][:,0,[0,3]])  #h3

print("beste vortrag sind " ,myNoten[np.argwhere(myNoten[:,4]==myNoten[:,4].min())][:,0,[0,4]])  #Vortrag

print("beste klasur sind " ,myNoten[np.argwhere(myNoten[:,5]==myNoten[:,5].min())][:,0,[0,5]])  # klasur


print("Insgesamt Beste =  " , gesamtmitmatrik[np.argwhere(gesamtmitmatrik[:,1]==gesamtmitmatrik[:,1].min())])

print("HH Beste =  " , hasugabenMeanmitmatrik[np.argwhere(hasugabenMeanmitmatrik[:,1]==hasugabenMeanmitmatrik[:,1].min())])

#print("haufig Note = ", gesamtmitmatrik.mod())




#%% Darstellung

fig1=plt.figure(figsize=(9,6))
p1=fig1.add_subplot(111)
bin=np.array([1.0,1.3,1.7,2.0,2.3,2.7,3.0,3.3,3.7,4.0])
p1.hist(gesamtmitmatrik[:,1],bins=bin,edgecolor="red")


fig1.tight_layout()
fig1.show()

fig2=plt.figure(figsize=(9,6))
p2=fig2.add_subplot(111)
p2.scatter(gesamtmitmatrik[:,0],gesamtmitmatrik[:,1])






fig2.tight_layout()
fig2.show()



#%%piechart
a=gesamtmitmatrik[:,1]

b=np.sum((a>=1) & (a<=1.3))
c=np.sum((a>1.3) & (a<=1.7))
d=np.sum((a>1.7) & (a<=2))
e=np.sum((a>2) & (a<=2.3))
f=np.sum((a>2.3) & (a<=2.7))
g=np.sum((a>2.7) & (a<=3))
h=np.sum((a>3) & (a<=3.3))
k=np.sum((a>3.3) & (a<=3.7))
l=np.sum((a>3.7) & (a<=4))

myArray=[b,c,d,e,f,g,h,k,l]
mynpArray=np.array(myArray)


fig3=plt.figure(figsize=(9,6))
p3=fig3.add_subplot(111)
label=[1,2,3,4,5,6,7,8,9]


p3.pie(myArray,labels=label,autopct='%.1f%%')
p3.set_title("Pie")
print(myArray)







