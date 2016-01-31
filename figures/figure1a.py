import string
from GracePlot.GracePlot import *
from Numeric import *


ed=[-2.44, -2.60, -2.74, -2.84, -3.00, -3.12, -3.18, -3.16]

ed.reverse()
labels=['Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni' ,'Pt']
xvalues=range(len(ed))

p=GracePlot(3,4.0)
p.SetView(xmin=0.15,xmax=0.95,ymin=0.12,ymax=1.2)


d=Data(xvalues,ed,
       symbol=Symbol(symbol=circle,fillcolor=black,size=1.4),
       line=Line(linestyle=0))

        
p.plot(d)
p.xaxis(tick=Tick(SpecialTicks=SpecialTicks((0, 'Ti'), (1, 'V'), (2, 'Cr'), (3, 'Mn'), (4, 'Fe'), (5, 'Co'), (6, 'Ni'), (7, 'Pt'))))

p.text(x=0,y=-2.45,string='(a.)',font=2,charsize=1.6)

p.redraw()
p.xlabel('Subsurface Metal')
p.ylabel('d-band center (eV)')

p.save('figure_1a.eps')
p.save('figure_1a.pdf')
p.save('figure_1a.agr')
