import os
#import sys
#from cProfile import label
import numpy as np

def cm2inch(value):
    return value/2.54

row = 2 #J\ta table
col = 11

path = os.path.abspath('.')
path += "\\result"

#####################################read the catadata###########################
catatemrow = 1
catatemcol = 1
catadata = np.zeros(shape = (row, col))
for firstdir in os.listdir(path):
    firstdirname = path + "\\" +firstdir
    #print(firstdir)

    if os.path.isdir(firstdirname) and firstdir[0] == 'c':
        catadata[catatemrow, 0] = float(firstdir[11:])
        for seconddir in os.listdir(firstdirname):
            seconddirname = firstdirname + "\\" + seconddir
            if seconddir[3] >= "0" and seconddir[3] <= "9" and os.path.isdir(seconddirname):
                 catadata[0, catatemcol] = float(seconddir[3:])
                 catatemcol = catatemcol + 1

        catatemrow = catatemrow + 1

catadata = catadata[: , catadata[0, :].argsort()]
catadata = catadata[catadata[:, 0].argsort(), :]

for firstdir in os.listdir(path):
    firstdirname = path + "\\" +firstdir
    #print(firstdir)

    if os.path.isdir(firstdirname) and firstdir[0] == 'c':
        for i in range(row):
            if catadata[i, 0] == float(firstdir[11:]):
                catatemrow = i
        for seconddir in os.listdir(firstdirname):
            seconddirname = firstdirname + "\\" + seconddir
            if seconddir[3] >= "0" and seconddir[3] <= "9" and os.path.isdir(seconddirname):
                for i in range(col):
                    if catadata[0, i] == float(seconddir[3:]):
                        catatemcol = i

                filecount = 0
                for filedir in os.listdir(seconddirname):
                    filename = seconddirname + "\\" + filedir
                    with open(filename) as f:
                        datastr = f.read().split()
                        for str in datastr:
                            if str == "overlapf=":
                                catadata[catatemrow, catatemcol] = catadata[catatemrow, catatemcol] + float(datastr[datastr.index(str)+1])
                    filecount = filecount + 1
                #print(filecount)
                catadata[catatemrow, catatemcol] = catadata[catatemrow, catatemcol]/filecount

                #if seconddir[3:] == "1":



###################################read the nocatadata####################################
catatemrow = 1
catatemcol = 1
nocatadata = np.zeros(shape = (row, col))
for firstdir in os.listdir(path):
    firstdirname = path + "\\" +firstdir
    #print(firstdir)

    if os.path.isdir(firstdirname) and firstdir[0] == 'n':
        nocatadata[catatemrow, 0] = float(firstdir[8:])
        for seconddir in os.listdir(firstdirname):
            seconddirname = firstdirname + "\\" + seconddir
            if seconddir[3] >= "0" and seconddir[3] <= "9" and os.path.isdir(seconddirname):
                 nocatadata[0, catatemcol] = float(seconddir[3:])
                 catatemcol = catatemcol + 1

        catatemrow = catatemrow + 1

nocatadata = nocatadata[: , nocatadata[0, :].argsort()]
nocatadata = nocatadata[nocatadata[:, 0].argsort(), :]

for firstdir in os.listdir(path):
    firstdirname = path + "\\" +firstdir
    #print(firstdir)

    if os.path.isdir(firstdirname) and firstdir[0] == 'n':
        for i in range(row):
            if nocatadata[i, 0] == float(firstdir[8:]):
                catatemrow = i
        for seconddir in os.listdir(firstdirname):
            seconddirname = firstdirname + "\\" + seconddir
            if seconddir[3] >= "0" and seconddir[3] <= "9" and os.path.isdir(seconddirname):
                for i in range(col):
                    if nocatadata[0, i] == float(seconddir[3:]):
                        catatemcol = i

                filecount = 0
                for filedir in os.listdir(seconddirname):
                    filename = seconddirname + "\\" + filedir
                    with open(filename) as f:
                        datastr = f.read().split()
                        for str in datastr:
                            if str == "overlapf=":
                                nocatadata[catatemrow, catatemcol] = nocatadata[catatemrow, catatemcol] + float(datastr[datastr.index(str)+1])
                    filecount = filecount + 1
                #print(filecount)
                nocatadata[catatemrow, catatemcol] = nocatadata[catatemrow, catatemcol]/filecount

###############################read spectra########################################

# for firstdir in os.listdir(path):
#     firstdirname = path + "\\" +firstdir
#     #print(firstdir)
#
#     if os.path.isdir(firstdirname) and firstdir[0] == 'c':
#         float(firstdir[11:])

filename = path + "\\nocata_J1\\spectra\\spectra1.out"
spectralist = []
with open(filename) as f:
    datastr = f.read().split()
    for i in range(len(datastr)):
        #print(i)
        if i%6 == 1:
            spectralist.append(float(datastr[i]))
        if i%6 == 3:
            spectralist.append(float(datastr[i]))
        if i%6 == 5:
            spectralist.append(float(datastr[i]))

spectra = np.array(spectralist).reshape((int(len(spectralist)/3), 3))

#spectra.reshape((int(len(spectra)/3), 3))


print(spectra)
print(nocatadata)
print(catadata)
