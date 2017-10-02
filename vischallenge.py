from scipy.io import netcdf
import time
import sys
import matplotlib.pyplot as plt

f = netcdf.netcdf_file("psiRZ.cdf", "r")

for v in f.variables:
    print v

rz = f.variables["pout_psiRZ"].data

print rz.shape		# 84 time steps, 65 x 65 magnetic field data
shape = rz.shape	# returns a tuple

for i in range(shape[0]):
    print "\r" + str(i),	# print the time step as a rolling odometer
    sys.stdout.flush()		# force printing to avoid buffering all values

    rz0 = rz[i][:][:]
    plt.imshow(rz0, origin="lower")
    plt.draw()
    plt.pause(.02)		# pause .02 seconds before drawing next frame
