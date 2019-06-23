import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc


def cm2inch(value):
    return value/2.54

##to make the label looks like the latex format.
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
#############show AParticle#################################

#plt.figure(num=1, figsize=(cm2inch(8), cm2inch(6)))


font={'family':'Times New Roman','size':10}

plt.rc('font',**font)

import readdata
from importlib import reload
reload(readdata)

data = readdata.readc("Oresult", 6, 11, 8, 11)

plt.figure(figsize = (cm2inch(8), cm2inch(8)))
plt.title(r"spin-$\frac{1}{2}$ with $J=0.5$")
plt.xscale("log")
plt.plot(data.catadata[0, :], data.catadata[1, :], "o-" ,linewidth = 0.5, label = r"with $H_c$")
plt.plot(data.nocatadata[0, :], data.nocatadata[1, :], "s-", linewidth = 0.5, label = r"without $H_c$")
plt.legend(loc = 2)
plt.xlim(1,1000)
plt.ylim(0, 1)
plt.yticks([0, 0.5, 1])
plt.xlabel(r"$t_a$")
plt.ylabel(r"$\langle \psi(t_a)|\psi_f\rangle$")
plt.tick_params(top=True, right=True, direction='in')
plt.tight_layout()
plt.savefig("/home/keaideni/WORK/WORK/files/articles/note_annealing/OJ05.eps")


plt.figure(figsize = (cm2inch(8), cm2inch(8)))
plt.title(r"spin-$\frac{1}{2}$ with $J=1$")
plt.xscale("log")
plt.plot(data.catadata[0, :], data.catadata[2, :], "o-" ,linewidth = 0.5, label = r"with $H_c$")
plt.plot(data.nocatadata[0, :], data.nocatadata[2, :], "s-", linewidth = 0.5, label = r"without $H_c$")
plt.legend(loc = 2)
plt.xlim(1,1000)
plt.ylim(0, 1)
plt.yticks([0, 0.5, 1])
plt.xlabel(r"$t_a$")
plt.ylabel(r"$\langle \psi(t_a)|\psi_f\rangle$")
plt.tick_params(top=True, right=True, direction='in')
plt.tight_layout()
plt.savefig("/home/keaideni/WORK/WORK/files/articles/note_annealing/OJ1.eps")


plt.figure(figsize = (cm2inch(8), cm2inch(8)))
plt.title(r"spin-$\frac{1}{2}$ with $J=3$")
plt.xscale("log")
plt.plot(data.catadata[0, :], data.catadata[3, :], "o-" , linewidth = 0.5, label = r"with $H_c$")
plt.plot(data.nocatadata[0, :], data.nocatadata[3, :], "s-" , linewidth = 0.5, label = r"without $H_c$")
plt.legend(loc = 2)
plt.xlim(1,1000)
plt.ylim(0,1)
plt.yticks([0, 0.5, 1])
plt.xlabel(r"$t_a$")
plt.ylabel(r"$\langle \psi(t_a)|\psi_f\rangle$")
plt.tick_params(top=True, right=True, direction='in')
plt.tight_layout()
plt.savefig("/home/keaideni/WORK/WORK/files/articles/note_annealing/OJ3.eps")



plt.figure(figsize = (cm2inch(8), cm2inch(8)))
plt.title(r"spin-$\frac{1}{2}$ with $J=5$")
plt.xscale("log")
plt.plot(data.catadata[0, :], data.catadata[4, :], "o-" , linewidth = 0.5, label = r"with $H_c$")
plt.plot(data.nocatadata[0, :], data.nocatadata[4, :], "s-" , linewidth = 0.5, label = r"without $H_c$")
plt.legend(loc = 2)
plt.xlim(1,1000)
plt.ylim(0,1)
plt.yticks([0, 0.5, 1])
plt.xlabel(r"$t_a$")
plt.ylabel(r"$\langle \psi(t_a)|\psi_f\rangle$")
plt.tick_params(top=True, right=True, direction='in')
plt.tight_layout()
plt.savefig("/home/keaideni/WORK/WORK/files/articles/note_annealing/OJ5.eps")


plt.figure(figsize = (cm2inch(8), cm2inch(8)))
plt.title(r"spin-$\frac{1}{2}$ with $J=10$")
plt.xscale("log")
plt.plot(data.catadata[0, :], data.catadata[5, :], "o-" , linewidth = 0.5, label = r"with $H_c$")
plt.plot(data.nocatadata[0, :], data.nocatadata[5, :], "s-" , linewidth = 0.5, label = r"without $H_c$")
plt.legend(loc = 2)
plt.xlim(1,1000)
plt.ylim(0,1)
plt.yticks([0, 0.5, 1])
plt.xlabel(r"$t_a$")
plt.ylabel(r"$\langle \psi(t_a)|\psi_f\rangle$")
plt.tick_params(top=True, right=True, direction='in')
plt.tight_layout()
plt.savefig("/home/keaideni/WORK/WORK/files/articles/note_annealing/OJ10.eps")




plt.figure(figsize = (cm2inch(8), cm2inch(8)))
plt.title(r"The minimal gap")
#plt.xscale("log")
plt.plot(data.catagap[:, 0], data.catagap[:, 1], "o-" , linewidth = 0.5, label = r"with $H_c$")
plt.plot(data.nocatagap[0:5, 0], data.nocatagap[0:5, 1], "s-" , linewidth = 0.5, label = r"without $H_c$")
plt.legend(loc = 2)
plt.xlim(0,10)
plt.ylim(0, 0.014)
#plt.yticks([0, 0.5, 1])
plt.tick_params(top=True, right=True, direction='in')
plt.xlabel(r"$J$")
plt.ylabel(r"$E_g$")
#plt.yaxis.set_label_coords(-0.1, 0.5)
plt.xticks([0, 5, 10])
plt.yticks([0, 0.006, 0.012, 0.014], [r"$0$", r"$0.6$", r"$1.2$", r"$\times 10^{-2}$"])
plt.tight_layout()
plt.savefig("/home/keaideni/WORK/WORK/files/articles/note_annealing/Ogap.eps")

pdata = readdata.readc("Presult", 2, 11, 2, 11)
plt.figure(figsize = (cm2inch(8), cm2inch(8)))
plt.title(r"spin-$\frac{1}{2}$ with $J=1$")
plt.xscale("log")
plt.plot(pdata.catadata[0, :], pdata.catadata[1, :], "o-" , linewidth = 0.5, label = r"with $H_c$")
plt.plot(pdata.nocatadata[0, :], pdata.nocatadata[1, :], "s-" , linewidth = 0.5, label = r"without $H_c$")
plt.legend(loc = 2)
plt.xlim(1,1000)
plt.ylim(0,1)
plt.yticks([0, 0.5, 1])
plt.xlabel(r"$t_a$")
plt.ylabel(r"$\langle \psi(t_a)|\psi_f\rangle$")
plt.tick_params(top=True, right=True, direction='in')
plt.tight_layout()
plt.savefig("/home/keaideni/WORK/WORK/files/articles/note_annealing/PJ1.eps")

plt.show()