#Author: Aditya (asaditya1195@gmail.com)


#To run this code: Install joblib (pip install joblib) for parallelization and Install matplotlib (pip install matplotlib) for plotting graphs
#Input: Directory containing all the .txt files corresponding to the output of the MC_kth_Distance_Plot code.
#Output: For every .txt file in the folder a .txt.png file will be created corresponding to the plot for that particular file.

import matplotlib.pyplot as plt
import glob, os

#Set directory path here
#os.chdir("./new/")

from joblib import Parallel, delayed
import multiprocessing

def processInput(filename):
	fo = open(filename, "r")
	cnt = 1;
	x = []
	y = []

	for line in fo.readlines():
		y.append(float(line))
		x.append(cnt)
		cnt += 1

	y.sort()

	# Uncomment the next two lines if you want to sparsify the plot further.
	# y = y[0::500]
	# x = x[0::500]
	
	plt.scatter(x, y, marker='.');

	# plt.show()
	plt.xlabel("Kth nearest Neighbour")
	plt.ylabel("Distance")

	plt.savefig(filename+".png")
	plt.clf()
	return;


files = []
for file in glob.glob("output_twitter.txt*"):
    files.append(file)

files.sort()

print files


num_cores = 8

results = Parallel(n_jobs=num_cores)(delayed(processInput)(file) for file in files)
