import numpy as np
import scipy as sp
import scipy.interpolate
import matplotlib.pyplot as plt

# Generate some random data
x = np.array([10.816,11.9,12.6,13.9,14.7,16,18,20.5,21.6,22.6,23.3]) #ParteSuperior
y = np.array([11.181,11.85,12.6,12.4,12.05,12.25,12.25,11.4,10.7,10.5,10.25])#ParteSuperior

a = np.array([10.817,11.022,11.510,11.834,12.264,13.624,14.499,15.109,15.527])#ParteInferior
b = np.array([11.180,11.023,11.032,11.085,11.3,11.087,10.830,10.350,10.106])#ParteInferior

j = np.array([14.659,15.085,15.387,15.478,15.527])#Ala
k = np.array([4.839,6.067,8.03,9.019,10.106])#Ala

m = np.array([14.65,14.99,15.56,16.11,16.91,17.56,17.98,18.47,19.33,20.57,21.50,22.36,23.30])#Ala
n = np.array([4.83,4.71,4.83,5.23,6.08,7.33,8.34,9.56,9.50,9.99,9.91,10.09,10.25])#Ala

r = np.array([ 12.663,12.700,12.805,12.886])#Ojo
s = np.array([ 12.202,12.279,12.293,12.222])#Ojo

f = np.array([ 12.663,12.720,12.826,12.886])#Ojo
g = np.array([ 12.202,12.130,12.143,12.222])#Ojo
# Interpolate the data using a cubic spline to "new_length" samples
new_length = 30#Se establece el numero de puntos resultantes de la interpolacion de los puntos que van a conformar
new_x = np.linspace(x.min(), x.max(), new_length)#ParteSuperior
new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)#ParteSuperior

new_a = np.linspace(a.min(), a.max(), new_length)#ParteInferior
new_b = sp.interpolate.interp1d(a, b, kind='cubic')(new_a)#ParteInferior

new_j = np.linspace(j.min(), j.max(), new_length)#Ala
new_k = sp.interpolate.interp1d(j, k, kind='cubic')(new_j)#Ala

new_m = np.linspace(m.min(), m.max(), new_length)#Ala
new_n = sp.interpolate.interp1d(m, n, kind='cubic')(new_m)#Ala

new_r = np.linspace(r.min(), r.max(), new_length)#Ala
new_s = sp.interpolate.interp1d(r, s, kind='cubic')(new_r)#Ala

new_f = np.linspace(f.min(), f.max(), new_length)#Ala
new_g = sp.interpolate.interp1d(f, g, kind='cubic')(new_f)#Ala

# Plot the results
plt.figure('Interpolacion Pato')#Crea una ventana titulada "Interpolacion pato"
plt.subplot(2,1,1)#Divide la ventana en dos filas y una columna y ubica la grafica en el primer espacio
plt.plot(x, y, 'b.-')#grafica x y y usando color azul y lineas
plt.plot(a, b, 'b.-')
plt.plot(j, k, 'b.-')
plt.plot(m, n, 'b.-')
plt.plot(r, s, 'b.-')
plt.plot(f, g, 'b.-')
plt.title('Pato sin interpolar')#Establece el titulo de la grafica

plt.subplot(2,1,2)#Divide la ventana en dos filas y una columna y ubica la grafica en el segundo espacio
plt.plot(new_x, new_y, 'g.-')#grafica x y y usando color verde y lineas
plt.plot(new_a, new_b, 'g.-')
plt.plot(new_j, new_k, 'g.-')
plt.plot(new_m, new_n, 'g.-')
plt.plot(new_r, new_s, 'k.-')#grafica x y y usando color negro y lineas
plt.plot(new_f, new_g, 'k.-')
plt.title('Pato interpolado')#Establece el titulo de la grafica

plt.show()#Muestra la ventana 
