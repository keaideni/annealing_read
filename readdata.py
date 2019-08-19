class readc(object):

    def __init__(self, catadir, nocatadir, _catarow, _catacol, _nocatarow, _nocatacol):
        import os
        #import sys
        #from cProfile import label
        import numpy as np

        def cm2inch(value):
            return value/2.54
        ###############J\ta table##############
        #rwo = number of Js +1
        row = _catarow
        #col = number of tas +1
        col = _catacol

        path = os.path.abspath('.')
        path += "/"
        path += catadir

        #####################################read the self.catadata###########################
        catatemrow = 1
        self.catagap = np.ones((row-1, 2))

        self.catadata = np.zeros(shape = (row, col))
        for firstdir in os.listdir(path):
            firstdirname = path + "/" +firstdir
            #print(firstdir)

            if os.path.isdir(firstdirname) and firstdir[0] == 'c':
                self.catadata[catatemrow, 0] = float(firstdir[11:])
                catatemcol = 1
                for seconddir in os.listdir(firstdirname):
                    seconddirname = firstdirname + "/" + seconddir
                    if seconddir[3] >= "0" and seconddir[3] <= "9" and os.path.isdir(seconddirname):
                         self.catadata[0, catatemcol] = float(seconddir[3:])
                         catatemcol = catatemcol + 1

                catatemrow = catatemrow + 1

        self.catadata = self.catadata[: , self.catadata[0, :].argsort()]
        self.catadata = self.catadata[self.catadata[:, 0].argsort(), :]

        catagaprow = 0
        for firstdir in os.listdir(path):
            firstdirname = path + "/" +firstdir
            #print(firstdir)

            if os.path.isdir(firstdirname) and firstdir[0] == 'c':
                for i in range(row):
                    if self.catadata[i, 0] == float(firstdir[11:]):
                        catatemrow = i
                self.catagap[catagaprow, 0] = float(firstdir[11:])
                for seconddir in os.listdir(firstdirname):
                    seconddirname = firstdirname + "/" + seconddir
                    if seconddir[3] >= "0" and seconddir[3] <= "9" and os.path.isdir(seconddirname):
                        for i in range(col):
                            if self.catadata[0, i] == float(seconddir[3:]):
                                catatemcol = i

                        filecount = 0
                        for filedir in os.listdir(seconddirname):
                            filename = seconddirname + "/" + filedir
                            if filedir[-3:] == "out":
                                with open(filename) as f:
                                    datastr = f.read().split()
                                    for str in datastr:
                                        if str == "overlapf=":
                                            self.catadata[catatemrow, catatemcol] = self.catadata[catatemrow, catatemcol] + float(datastr[datastr.index(str)+1])
                                            filecount = filecount + 1

                                        if seconddir[3:] == "1" and str == "gap":
                                            self.catagap[catagaprow, 1] = min(self.catagap[catagaprow, 1] , abs(float(datastr[datastr.index(str)+1])))

                        #print(filecount)
                        self.catadata[catatemrow, catatemcol] = self.catadata[catatemrow, catatemcol]/filecount
                catagaprow = catagaprow + 1

                        #if seconddir[3:] == "1":



        ###################################read the self.nocatadata####################################
        row = _nocatarow
        col = _nocatacol
        catatemrow = 1

        path = os.path.abspath('.')
        path += "/"
        path += nocatadir

        self.nocatagap = np.ones((row-1, 2))

        self.nocatadata = np.zeros(shape = (row, col))
        for firstdir in os.listdir(path):
            if filedir[-3:] != 'out':
                continue
            firstdirname = path + "/" +firstdir
            #print(firstdir)

            if os.path.isdir(firstdirname) and firstdir[0] == 'n':
                self.nocatadata[catatemrow, 0] = float(firstdir[8:])
                catatemcol = 1
                for seconddir in os.listdir(firstdirname):
                    seconddirname = firstdirname + "/" + seconddir
                    if seconddir[3] >= "0" and seconddir[3] <= "9" and os.path.isdir(seconddirname):
                         self.nocatadata[0, catatemcol] = float(seconddir[3:])
                         catatemcol = catatemcol + 1

                catatemrow = catatemrow + 1

        self.nocatadata = self.nocatadata[: , self.nocatadata[0, :].argsort()]
        self.nocatadata = self.nocatadata[self.nocatadata[:, 0].argsort(), :]

        nocatagaprow = 0
        for firstdir in os.listdir(path):
            firstdirname = path + "/" +firstdir
            #print(firstdir)

            if os.path.isdir(firstdirname) and firstdir[0] == 'n':
                #print(firstdir)
                for i in range(row):
                    if self.nocatadata[i, 0] == float(firstdir[8:]):
                        catatemrow = i
                self.nocatagap[nocatagaprow, 0] = float(firstdir[8:])
                for seconddir in os.listdir(firstdirname):
                    seconddirname = firstdirname + "/" + seconddir
                    if seconddir[3] >= "0" and seconddir[3] <= "9" and os.path.isdir(seconddirname):
                        for i in range(col):
                            if self.nocatadata[0, i] == float(seconddir[3:]):
                                catatemcol = i

                        filecount = 0
                        for filedir in os.listdir(seconddirname):
                            if filedir[-3:] != 'out':
                                continue
                            filename = seconddirname + "/" + filedir
                            #print(filename)
                            with open(filename) as f:
                                datastr = f.read().split()
                                for str in datastr:
                                    if str == "overlapf=":
                                        self.nocatadata[catatemrow, catatemcol] = self.nocatadata[catatemrow, catatemcol] + float(datastr[datastr.index(str)+1])
                                        filecount = filecount + 1
                                    #############for gap#######################
                                    if seconddir[3:] == "1" and str == "gap":
                                        self.nocatagap[nocatagaprow, 1] = min(self.nocatagap[nocatagaprow, 1] , abs(float(datastr[datastr.index(str)+1])))

                        #print(filecount)
                        self.nocatadata[catatemrow, catatemcol] = self.nocatadata[catatemrow, catatemcol]/filecount
                nocatagaprow = nocatagaprow + 1





###############################read spectra########################################

# for firstdir in os.listdir(path):
#     firstdirname = path + "\\" +firstdir
#     #print(firstdir)
#
#     if os.path.isdir(firstdirname) and firstdir[0] == 'c':
#         float(firstdir[11:])

# filename = path + "\\nocata_J1\\spectra\\spectra1.out"
# spectralist = []
# with open(filename) as f:
#     datastr = f.read().split()
#     for i in range(len(datastr)):
#         #print(i)
#         if i%6 == 1:
#             spectralist.append(float(datastr[i]))
#         if i%6 == 3:
#             spectralist.append(float(datastr[i]))
#         if i%6 == 5:
#             spectralist.append(float(datastr[i]))
#
# spectra = np.array(spectralist).reshape((int(len(spectralist)/3), 3))
#
# #spectra.reshape((int(len(spectra)/3), 3))
#
#
# print(spectra)
        self.nocatagap = self.nocatagap[self.nocatagap[:,0].argsort(), :]
        self.catagap = self.catagap[self.catagap[:,0].argsort(), :]
        print(self.nocatadata)
        print(self.catadata)
        print(self.nocatagap)
        print(self.catagap)