#! usr/bin/env python
from scipy.interpolate import spline
import numpy as np
import matplotlib.pyplot as plt 
import csv

x_1 = []
y_1 = []

# x_2 = []
# y_2 = []

# x_3 = []
# y_3 = []

with open('/home/adarsh/Downloads/_slash_cross_track_error.csv','r') as csvFile1:
	reader1 = csv.reader(csvFile1)
	flag = False
	for row in reader1:
		if flag == False:
			flag = True
			continue
		# print float(row[0][:6])
		# print float(row[8])
		
		x_1.append(float(row[4]))
		y_1.append(float(row[2]))
	# x_1_new = np.linspace(min(x_1), max(x_1), 25)
	# y_1_new = spline(x_1, y_1, x_1_new)

# with open('/home/adarsh/Documents/Bag files_Pure_pursuit/Eight_path/eight_path_k_1.2_vel_10_/_slash_cross_track_error.csv','r') as csvFile2:
# 	reader2 = csv.reader(csvFile2)
# 	flag = False
# 	for row in reader2:
# 		if flag == False:
# 			flag = True
# 			continue
# 		# print float(row[0][:6])
# 		# print float(row[8])
		
# 		x_2.append(float(row[4]))
# 		y_2.append(float(row[2]))
# 	# x_2_new = np.linspace(min(x_2), max(x_2), 300)
# 	# y_2_new = spline(x_2, y_2, x_2_new)
# with open('/home/adarsh/Documents/Bag files_Pure_pursuit/Eight_path/eight_path_k_1.0_vel_10_/_slash_cross_track_error.csv','r') as csvFile3:
# 	reader3 = csv.reader(csvFile3)
# 	flag = False
# 	for row in reader3:
# 		if flag == False:
# 			flag = True
# 			continue
# 		# print float(row[0][:6])
# 		# print float(row[8])
		
# 		x_3.append(float(row[4]))
# 		y_3.append(float(row[2]))
	# x_3_new = np.linspace(min(x_3), max(x_3), 75)
	# y_3_new = spline(x_3, y_3, x_3_new)

plt.plot(x_1, y_1, label = 'k = 0.8', linewidth = 1.5)
# plt.plot(x_3, y_3, label = 'k = 1.0', linewidth = 1.5)
# plt.plot(x_2, y_2, label = 'k = 1.2', linewidth = 1.5)
plt.axis([0, 200, -0.4, 0.8 ])
plt.grid(True)
plt.legend()
plt.title('Crosstrack Error Plot(For velocity = 2.5 m/s)')
plt.xlabel('Distance Along Path(m)')
plt.ylabel('Crosstrack Error(m)')

plt.show()

csvFile1.close()
csvFile2.close()
csvFile3.close()
