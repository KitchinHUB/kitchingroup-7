import string
from GracePlot.GracePlot import *
from Numeric import *
import os
from Simulations.Dacapo import *
from Simulations.Dacapo.AtomProjectedDOS import *

def LoadData(filename):

    home='~/fysik/dacapo/Pt_3d/'

    sim=Simulation()
    sim.ados=AtomProjectedDOS()
    sim.UpdateFromNetCDFFile(os.path.join(home,filename))

    dband=sim.ados.GetDOS(atoms=[1,2,3,4],angularchannels=['d'],cutoffradius='infinite')
    filling=dband.GetIntegratedDOS()/4.0
    
    x,y=dband._GetData(relative=True)

    efill=where(x<=0,x,0)
    dfill=where(x<=0,y,0)

    return x,y,efill,dfill,filling

    
offset=3

list=['TiPt/Pt-Ti-Pt-Pt-relaxed_DIP.nc',
      'VPt/Pt-V-Pt-Pt-relaxed.nc',
      'CrPt/Pt-Cr-Pt-Pt-relaxed.nc',
      'MnPt/Pt-Mn-Pt-Pt-relaxed.nc',
      'FePt/Pt-Fe-Pt-Pt-relaxed.nc',
      'CoPt/Pt-Co-Pt-Pt-relaxed.nc',
      'NiPt/Pt-Ni-Pt-Pt-relaxed.nc',
      'Pt/Pt-relaxed.nc']



labels=['Pt/Ti/Pt',
        'Pt/V/Pt',
        'Pt/Cr/Pt',
        'Pt/Mn/Pt',
        'Pt/Fe/Pt',
        'Pt/Co/Pt',
        'Pt/Ni/Pt',
        'Pt/Pt']
      
p=GracePlot(3,4.0)
p.SetView(xmin=0.15,xmax=0.95,ymin=0.12,ymax=1.2)
p._send('map color 3 to (225,225,225),"gray"')
p._send('map color 4 to (200,200,200),"gray10"')
p._send('map color 5 to (175,175,175),"gray20"')
p._send('map color 6 to (150,150,150),"gray40"')
p._send('map color 7 to (125,125,125),"gray60"')
p._send('map color 8 to (100,100,100),"gray80"')
p._send('map color 9 to (75,75,75),"gray80"')
p._send('map color 10 to (50,50,50),"gray80"')


DataSets=[]
Nd=[]
for i in range(len(list)):
    e,d,ef,df,filling=LoadData(list[i])
    Nd.append(filling)
    
    data=Data(e,d+(7-i)*offset,
              line=Line(color=black),
              symbol=Symbol(symbol=None),
              legend='data')
    fdata=Data(ef,df+(7-i)*offset,
               line=Line(filltype=1,
                         color=black,
                         fillcolor=10-i),
               legend='fdata')
    
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
p.redraw()

p.text('(b.)',-9.2,33,charsize=1.5,font=6)

p.save('figure_1b.eps')
p.save('figure_1b.pdf')
p.save('figure_1b.agr')

