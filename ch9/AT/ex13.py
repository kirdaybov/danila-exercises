import pickle

dct = {}

outputfile = open('mydata.dat', 'wb')

pickle.dump(dct, outputfile)

outputfile.close()