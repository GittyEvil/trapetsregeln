#importerar modul numpy, matplotlib och scipy med specifikt quad kommandot
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from matplotlib.widgets import Button, RadioButtons, CheckButtons

#a,b,n värden
n=int(input('välj intervall du vill ha(n):'))
a=int(input('Välj även vilken lägsta punkt du vill ha(a):'))
b=int(input('välj den högsta punkten du vill räkna imellan(b):'))

#f(x) i formeln
f= lambda x: (x**2+5*x+3) #(1*x**3-3*x**2+8

#sätter x och y värde för trapetsregeln
x = np.linspace(a,b,n+1)
y=f(x)

#plottar ut x och y 
X=np.linspace(a,b,n)
Y=f(X)

plt.plot(X,Y,)

#räknar ut den exakta arean under grafen(för en specifik intergral)
def integrand(x):
    return x**2+5*x+3
#räknar ut mellan visst värde på b och a.
ans, err = quad(integrand, a, b)

#Tagen från personal.math.ubc.ca,trapetsregeln som beror på hur många intergraler vi har.
for i in range(n):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

#trapz räknar ut arean under grafen, desto mer intervaller du har desto mer exakt svar får du
total_area=np.trapz(Y,X)

#titeln visar bara den exakta arean genom vanlig intergral och ungefärlig area.
plt.title(
f'exakt area: {ans}\n'
f"ungefärlig area: {total_area.round()}\n"
f'skillnad: {total_area.round()-ans}')

plt.show()
