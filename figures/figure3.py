
from GracePlot import *
from Numeric import *
pt_rd=1.04
pt_ro=1.53

#Harrison spacing
rd=array([1.04,0.71,0.76,0.8,0.86,0.9,0.98,1.08])

ro=array([1.53,1.38,1.39,1.41,1.43,1.42,1.49,1.61])

tb_Wd=7.62*(rd*rd)**1.5/(ro*ro)**2.5

labels=['Pt','Ni','Co','Fe','Mn','Cr','V','Ti']

#interlayer spacing
d=array([2.34,2.04,2.04,2.05,2.01,2.04,2.10,2.14])
    
#matrix elements
V_pt3d=7.62*(rd*pt_rd)**1.5/d**5

#Real band data
W2=array([9.11,9.7,10.47,11.1,12.14,12.84,13.21,13.03])

W=sqrt(W2)


p=GracePlot(3.,4)
p.SetView(0.15,0.15,0.95,1.25)

d=Data(tb_Wd,W,symbol=Symbol(symbol=circle,fillcolor=red),
      line=Line(type=0))

# from best fit of the data
#width=0.92*V_pt3d/min(V_pt3d)+0.92

V_data=Data(V_pt3d,W,symbol=Symbol(symbol=circle,fillcolor=black),
       line=Line(type=0))

p.plot(V_data)

for i in range(len(labels)):
    p.text(labels[i],x=V_pt3d[i]+0.002,y=W[i],font=2,charsize=1.4)

p.xlabel('Pt-X Matrix Element (eV)')
p.ylabel('Pt rms d-band width (eV)')

p.save('figure3.eps')
p.save('figure3.pdf')
p.save('figure3.agr')


