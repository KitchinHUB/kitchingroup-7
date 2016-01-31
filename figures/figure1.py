import string
from GracePlot.GracePlot import *
from Numeric import *

def LoadData(filename):
    x=[]
    y=[]
    f=open(filename,'r')
    for line in f.xreadlines():
        data= string.split(line)
        x.append(string.atof(data[0]))
        y.append(string.atof(data[1]))

    f.close()
    x=array(x)
    y=array(y)
    
    efill=where(x<=0,x,0)
    dfill=where(x<=0,y,0)

    return x,y,efill,dfill

offset=3

list=['dband_Titanium.dat',
      'dband_Vanadium.dat',
      'dband_Chromium.dat',
      'dband_Manganese.dat',
      'dband_Iron.dat',
      'dband_Cobalt.dat',
      'dband_Nickel.dat',
      'dband_Platinum.dat']
labels=['Pt/Ti/Pt',
        'Pt/V/Pt',
        'Pt/Cr/Pt',
        'Pt/Mn/Pt',
        'Pt/Fe/Pt',
        'Pt/Co/Pt',
        'Pt/Ni/Pt',
        'Pt/Pt']
Nd=[9.35,9.32,9.31,9.30,9.30,9.30,9.32,9.27]
      
p=GracePlot(3,4.0)
p.g[0].SetView(xmin=0.15,xmax=0.95,ymin=0.12,ymax=1.2)
p._send('map color 3 to (225,225,225),"gray"')
p._send('map color 4 to (200,200,200),"gray10"')
p._send('map color 5 to (175,175,175),"gray20"')
p._send('map color 6 to (150,150,150),"gray40"')
p._send('map color 7 to (125,125,125),"gray60"')
p._send('map color 8 to (100,100,100),"gray80"')
p._send('map color 9 to (75,75,75),"gray80"')
p._send('map color 10 to (50,50,50),"gray80"')

p.xaxis(bar=Bar(linewidth=2))
p.yaxis(bar=Bar(linewidth=2))

DataSets=[]
for i in range(len(list)):
    e,d,ef,df=LoadData(list[i])
    data=Data(e,d+(7-i)*offset,line=Line(color=black),
	      legend='')
    fdata=Data(ef,df+(7-i)*offset,line=Line(filltype=1,
					    color=black,
					    fillcolor=10-i),
	       legend='')
    DataSets.append(data)
    DataSets.append(fdata)

        
p.plot(DataSets)
p.xlabel('E-E\sF\N (eV)')
p.ylabel('Density of States (arbitrary units)')
p.xaxis(-10,5,
        label=Label(font=6),
        tick=Tick(TickLabel=TickLabel(font=6)))

p.yaxis(0,35,
        label=Label(font=6),
        tick=Tick(TickLabel=TickLabel(font=6)))

p._send('xaxis label font 6')

for i in range(len(list)):
    p.text(labels[i],x=1.5,y=(7.0-i)*offset+0.5,charsize=1.5,font=6)
    p.text('%2.2f' % Nd[i],x=-9,y=(7.0-i)*offset+0.5,charsize=1.5,font=6)

p.text('N\sd',-9,25,charsize=1.5,font=6)
p.text('(b.)',-9.2,33,charsize=1.5,font=6)

p.save('figure_1b.eps')
p.save('figure_1b.pdf')
p.save('figure_1b.agr')
