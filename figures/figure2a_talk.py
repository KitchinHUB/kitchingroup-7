#%[files,labels,ed,dw,fd,rho_ef]=textread('Pt_3d_electonic_structure.csv','%s%s%n%n%n%n','headerlines',1);
from GracePlot import *
from math import *

rhod_ef=[1.65, 2.04, 2.80, 3.58, 4.23, 4.78, 4.78, 5.19].reverse()
rho_ef=[31.65, 33.14, 36.60, 33.86, 25.20, 20.37, 16.55, 16.74];

sf=6.75/8;
ed=[-2.44, -2.60, -2.74, -2.84, -3.00, -3.12, -3.18, -3.16];
dw=[9.11, 9.70, 10.47, 11.10, 12.14, 12.84, 13.21, 13.03];

p=GracePlot()
#p.SetView(0.15,0.15,0.9,1.1)
#set(gcf,'Units','inches','Position',[1 1 6.75 4],'PaperPositionMode','auto','PaperSize',[6.75 4])
d1=Data(ed,map(lambda x:sqrt(x), dw),
        symbol=Symbol(symbol=circle,fillcolor=orange,size=1.4),
        line=Line(linestyle=0),
	legend='data')

fit=Data([-3.2,-2.6],[-1.*-3.2+0.5,-1.*-2.6+0.5],
	 line=Line(linestyle=1,color=black,linewidth=4),
	 legend='y=0.5-x')
	 
p.plot(d1,fit)
p.xaxis(-3.3,-2.5)
p.yaxis(3,3.7)
p.xlabel('d-band center (eV)')
#p.ylabel("""\\x\\c\\z{1.4}V\\m{1}\\z{0.9}\\v{0.75}>>>>>\\N\\C\\f{}\M{1}d-band width""")
p.ylabel("""rms d-band width""")
#
#p.text(x=-2.6,y=3.65,string='(a.)',charsize=1.4,font=2)
p.save('figure2a_talk.png')


