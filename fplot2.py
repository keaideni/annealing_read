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
#print("haha")
data = readdata.readc("result/cata", "result/nocata", 4, 11, 4, 11)
#print(data)

plt.figure(figsize = (cm2inch(8), cm2inch(8)))
plt.title(r"spin-$\frac{1}{2}$ with $J=0.5$")
plt.xscale("log")
# plt.plot(data.catadata[0, :], data.catadata[1, :], "o-" ,linewidth = 0.5, label = r"with $H_c$")
# plt.plot(data.nocatadata[0, :], data.nocatadata[1, :], "s-", linewidth = 0.5, label = r"without $H_c$")
# plt.plot(data.catadata[0, :], data.catadata[2, :], "o-" ,linewidth = 1, label = r"with $H_c$")
# plt.plot(data.nocatadata[0, :], data.nocatadata[2, :], "s-", linewidth = 1, label = r"without $H_c$")
plt.plot(data.catadata[0, :], data.catadata[3, :], "o-" ,linewidth = 3, label = r"with $H_c$")
plt.plot(data.nocatadata[0, :], data.nocatadata[3, :], "s-", linewidth = 3, label = r"without $H_c$")

plt.legend(loc = 2)
plt.xlim(1,1000)
plt.ylim(0, 1)
plt.yticks([0, 0.5, 1])
plt.xlabel(r"$t_a$")
plt.ylabel(r"$\langle \psi(t_a)|\psi_f\rangle$")
plt.tick_params(top=True, right=True, direction='in')
plt.tight_layout()
plt.show()
# #plt.savefig("/home/keaideni/WORK/WORK/files/articles/note_annealing/OJ05.eps")
#
#
# plt.figure(figsize = (cm2inch(8), cm2inch(8)))
# plt.title(r"spin-$\frac{1}{2}$ with $J=1$")
# plt.xscale("log")
# plt.plot(data.catadata[0, :], data.catadata[2, :], "o-" ,linewidth = 0.5, label = r"with $H_c$")
# plt.plot(data.nocatadata[0, :], data.nocatadata[2, :], "s-", linewidth = 0.5, label = r"without $H_c$")
# plt.legend(loc = 2)
# plt.xlim(1,1000)
# plt.ylim(0, 1)
# plt.yticks([0, 0.5, 1])
# plt.xlabel(r"$t_a$")
# plt.ylabel(r"$\langle \psi(t_a)|\psi_f\rangle$")
# plt.tick_params(top=True, right=True, direction='in')
# plt.tight_layout()


# data2 = readdata.readc("result/cata4", "result/nocata", 2, 11, 3, 11)
# print(data2)

# plt.figure(figsize = (cm2inch(8), cm2inch(8)))
# plt.title(r"spin-$\frac{1}{2}$ with $J=0.5$")
# plt.xscale("log")
# plt.plot(data2.catadata[0, :], data2.catadata[1, :], "o-" ,linewidth = 0.5, label = r"with $H_c4$")
# plt.plot(data2.nocatadata[0, :], data2.nocatadata[1, :], "s-", linewidth = 0.5, label = r"without $H_c$")
# plt.plot(data.catadata[0, :], data.catadata[1, :], "s-", linewidth = 0.5, label = r"with $H_c$")
#
# plt.legend(loc = 2)
# plt.xlim(1,500)
# plt.ylim(0, 1)
# plt.yticks([0, 0.5, 1])
# plt.xlabel(r"$t_a$")
# plt.ylabel(r"$\langle \psi(t_a)|\psi_f\rangle$")
# plt.tick_params(top=True, right=True, direction='in')
# plt.tight_layout()
# plt.show()
# plt.savefig("/Users/admin/WORK/annealing_result/haha.png")


plt.show()