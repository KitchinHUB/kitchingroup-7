%[files,labels,ed,dw,fd,rho_ef]=textread('Pt_3d_electonic_structure.csv','%s%s%n%n%n%n','headerlines',1);
rhod_ef=fliplr([1.65 2.04 2.80 3.58 4.23 4.78 4.78 5.19]);
rho_ef=[31.65 33.14 36.60 33.86 25.20 20.37 16.55 16.74];
close
figure(1)
sf=6.75/8;
ed=[-2.44 -2.60 -2.74 -2.84 -3.00 -3.12 -3.18 -3.16];
dw=[9.11 9.70 10.47 11.10 12.14 12.84 13.21 13.03];

set(gcf,'Units','inches','Position',[1 1 6.75 4],'PaperPositionMode','auto','PaperSize',[6.75 4])
clf
subplot(1,2,1)
hold on
plot(ed,sqrt(dw),'ko','MarkerFaceColor',[.5 .5 .5],'MarkerSize',8)
axis([-3.3 -2.5 3 3.7]) 
xlabel('d-band center (eV)','FontSize',10,'FontWeight','bold')
ylabel('d-band width^{0.5} (eV)','FontSize',10,'FontWeight','bold')
text(-2.7,3.65,'(a.)')

%x=[-3.5:.1:-2.5];
%y=1.01-0.801*x;
%plot(x,y,'Color','black')
hold off

set(gca,'Box','on')
set(gca,'Position',[0.13500    0.1500    0.3270    0.8150])
%text(-3.4,3.1,'W^{0.5}=-0.801\epsilon_d +1.01')

subplot(1,2,2)
[ax,h1,h2]=plotyy(ed,rho_ef,ed,rhod_ef)
set(ax(1),'Box','on','Position',[0.577977 0.15 0.327023 0.815])
set(ax(2),'Box','on','Position',[0.577977 0.15 0.327023 0.815])

set(h1,'MarkerFaceColor',[.8 .8 .8],'Marker','o','LineStyle','none','MarkerSize',8)
set(h2,'MarkerFaceColor',[.4 .4 .4],'Marker','s','LineStyle','none','MarkerSize',8)

axes(ax(1))
arrow([ed(3),rho_ef(3)],[ed(3)-.2,rho_ef(3)])
text(-3.15,38,'(b.)')

axes(ax(2))
arrow([ed(4),rhod_ef(4)],[ed(4)+0.2,rhod_ef(4)])

set(get(ax(1),'YLabel'),'String','\rho _{E_f} (arbitrary units)','FontSize',10,...
    'FontWeight','bold','Color','black')
set(ax,'YColor','black')
set(get(ax(2),'YLabel'),'String','\rho _{d_{E_f}}','FontSize',10,...
    'FontWeight','bold','Color','black')
xlabel('d-band center (eV)','FontSize',10)

a=findobj(gcf);

allaxes=findall(a,'Type','axes');
alllines=findall(a,'Type','line');
alltext=findall(a,'Type','text');

set(allaxes,'FontWeight','Bold','LineWidth',1,'FontSize',10);
set(alltext,'FontWeight','Bold','LineWidth',1,'FontSize',10,'Color','black');
set(alllines,'Linewidth',1,'Color','black');
% 
%print -dpng -r300 figure_2.png
print -depsc2 -tiff -r300 -zbuffer figure_2.eps2
