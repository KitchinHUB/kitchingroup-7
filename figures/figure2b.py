#%[files,labels,ed,dw,fd,rho_ef]=textread('Pt_3d_electonic_structure.csv','%s%s%n%n%n%n','headerlines',1);
from GracePlot import *
from math import *
from Numeric import *
rhod_ef=[1.65, 2.04, 2.80, 3.58, 4.23, 4.78, 4.78, 5.19]
rhod_ef.reverse()

rho_ef=array([31.65, 33.14, 36.60, 33.86, 25.20, 20.37, 16.55, 16.74])*0.17

sf=6.75/8;
ed=[-2.44, -2.60, -2.74, -2.84, -3.00, -3.12, -3.18, -3.16];
dw=[9.11, 9.70, 10.47, 11.10, 12.14, 12.84, 13.21, 13.03];

p=GracePlot(3.0,4)
p.SetView(0.15,0.15,0.9,1.25)
#set(gcf,'Units','inches','Position',[1 1 6.75 4],'PaperPositionMode','auto','PaperSize',[6.75 4])
d1=Data(ed,rho_ef,
        symbol=Symbol(symbol=square,fillcolor=black,size=1.4),
        line=Line(linestyle=0),
        legend='Density of states \\cW\C 0.17')

d2=Data(ed,rhod_ef,symbol=Symbol(symbol=circle,fillcolor=gray,size=1.4),
        line=Line(linestyle=0),
        legend='Density of d-states')

p.plot(d1,d2)
p.xaxis(-3.2,-2.4)
p.yaxis(1,7.5)
p.xlabel('d-band center (eV)')
p.ylabel('\\f{12}r\\f{2}\sE\sf\N (arbitrary units)')

p.text(x=-3.1,y=7,string='(b.)',charsize=1.4,font=2)

p.legend(x=-2.85,y=7.25,font=2,charsize=1.2)

p.save('figure2b.eps')
p.save('figure2b.pdf')
p.save('figure2b.agr')
