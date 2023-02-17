import pickle

inputfile = open('mydata.dat', 'rb')

dct_in_file = pickle.load(inputfile)

inputfile.close()