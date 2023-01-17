import matplotlib.pyplot as plt 
import math
import numpy as np
width = 8 # 3 m
flow = 86.4 #8 m^3/s
if_SPE = 2
gravity= 9.807 # 9.807 m/s²
q_1= flow/width 


f_values = np.arange(0.0001,10,0.0001)

def Y(f):
     return math.cbrt(( flow**2 / ((width**2) * (gravity) * (f**2))) )
    

def E(depth):
     return depth + (flow**2 / (2 * gravity * (width*depth)**2))
 
def M(depth):
    return depth**2/2 + (q_1**2/gravity*depth)
    
y_results=[]
E_results= []
M_results=[]
for f in f_values:
    y_value= float("{:.6f}".format(Y(f)))

# finding the froud possible depths for different froud numbers
for f in f_values:
    y_value= float("{:.6f}".format(Y(f)))
    depth = min(y_value,10)
    energy = float("{:.6f}".format(E(depth)))
    moment = float("{:.6f}".format(M(depth)))
    M_results.append(moment)
    E_results.append(energy)
    y_results.append(depth)
    
# finding the critical depth and minimum energy
y_critical= math.cbrt(math.pow(q_1,2) / gravity)
Energy_min = y_critical + (math.pow(flow,2) /(2 * gravity * (y_critical*width)**2))
Energy_min= float("{:.4f}".format(Energy_min))
y_critical=float("{:.4f}".format(y_critical))



# Plot the first line
fig, ax = plt.subplots()
ax.plot(E_results,y_results, label='Line 1')
plt.xlabel("specific energy E" )
plt.ylabel("depth y")

# Find the intersection point of the vertical line and the data
x_intersect = Energy_min
y_intersect = y_critical

# Plot a vertical line from the x-axis to the intersection point
ax.plot([x_intersect, x_intersect], [0, y_intersect], color='red', linestyle='dotted')

# Find the intersection point of the horizontal line and the data
x_intersect = Energy_min
y_intersect = y_critical

# Plot a horizontal line from the y-axis to the intersection point
ax.plot([0, x_intersect], [y_intersect, y_intersect], color='red', linestyle='dotted')
ax.text(Energy_min, y_critical, f'({Energy_min}, {y_critical})', fontsize=8)


plt.show()
