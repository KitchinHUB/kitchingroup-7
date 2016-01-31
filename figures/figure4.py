from GracePlot import *

labels=['Pt', 'Ni','Co','Fe','Mn','Cr','V','Ti']
ed=[-2.44, -2.60, -2.74, -2.84, -3.0, -3.12, -3.18, -3.16];
dissH_H=[-0.63, -0.27, -0.06, 0.05, 0.30, 0.49, 0.64, 0.75];
dissH_O=[-1.27, -0.61, -0.40,-0.29, -0.17, 0.18, 0.28, 0.78];
dissH_O_450=[-1.47, -0.82, -0.59, -0.54, -0.40, -0.07, 0.20, 0.63];

p=GracePlot(3.375,4)
p.SetView(.15,.15,.9,1.1)
hdata=Data(ed,dissH_H,symbol=Symbol(symbol=circle,fillcolor=black,size=1.4),
           line=Line(linestyle=0),
           legend='H\s2')

odata=Data(ed,dissH_O_450,symbol=Symbol(symbol=square,fillcolor=grey,size=1.4),
           line=Line(linestyle=0),
           legend='O\s2')

zero=Data([-3.2,-2.4],[0,0],
          symbol=Symbol(symbol=0),
          line=Line(color=black))

p.plot(hdata,odata,zero)
p.xaxis(-3.2,-2.4)
p.yaxis(-2,1)


p.legend(x=-2.6,y=0.7,font=2,charsize=1.3)

p.xlabel('d-band center (eV)')
p.ylabel('dissociative adsorption energy (eV)')

p._send('xaxis tick place normal')

p._send('altxaxis on')
p._send('altxaxis ticklabel font 2')
p._send('altxaxis ticklabel char size 1.4')
p._send('altxaxis ticklabel place opposite')
p._send('altxaxis ticklabel type spec')
p._send('altxaxis tick place opposite')
p._send('altxaxis tick spec %d' % (len(labels)-1))

for i in range(len(labels)-1):
    p._send('altxaxis tick major %d,%f' % (i,ed[i]))
    p._send('altxaxis ticklabel %d, "%s"' % (i,labels[i]))

p._send('altxaxis label place opposite')
p._send('altxaxis label char size 1.2')
p._send('altxaxis label font 2')
p._send('altxaxis label "Subsurface Metal"')


p.save('figure4.eps')
p.save('figure4.pdf')
p.save('figure4.agr')


