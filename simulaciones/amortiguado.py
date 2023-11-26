
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from runge import RK4

sns.set()
sns.set_context("notebook")

# Valores iniciales, intervalo de tiempo, condiciones de gravedad y longitud de la cuerda
g = 9.8
length = 3


THETA0 = np.pi/4
V0 = 0.0
T0 = 0
TF = 20
step = 0.001
GAMMA = 0.25


def dampedPendulum(t, x, v):
    """ Calcula la derivada de la posición con respecto al tiempo para un péndulo amortiguado.

        Parámetros:
        - t : Tiempo.
        - x : Posición angular del péndulo en radianes.
        - v : Velocidad angular del péndulo en radianes por segundo.

        Retorna:
        - Tasa de cambio de la velocidad angular 

        """
    return (-g/length*np.sin(x))-GAMMA*v


def linealdampedPendulum(t, x, v):
    """ Calcula la derivada de la posición con respecto al tiempo para un péndulo amortiguado.

        Parámetros:
        - t : Tiempo.
        - x : Posición angular del péndulo en radianes.
        - v : Velocidad angular del péndulo en radianes por segundo.

        Retorna:
        - Tasa de cambio de la velocidad angular 

        """
    return (-g/length*x)-GAMMA*v


def nonLinearPendulum(t, x, v):
    """
   Ecuación diferencial para un péndulo no lineal.

   Parameters:
   - t: Tiempo actual
   - x: Posición angular actual
   - v: Velocidad angular actual

   Returns:
   - Tasa de cambio de la velocidad angular 
   """
    return -g/length * np.sin(x)

    # Solución del sistema de ecuaciones utilizando Runge-Kutta de cuarto orden
t_sol_damped, x_sol_damped = RK4(dampedPendulum, THETA0, V0, T0, TF, step)
t_sol_lineal_damped, x_sol_lineal_damped = RK4(
    linealdampedPendulum, THETA0, V0, T0, TF, step)
# t_sol_nonLinear, x_sol_nonLinear = RK4(
#     nonLinearPendulum, THETA0, V0, T0, TF, step)

# Gráfica de la solución


plt.figure(figsize=(10, 6))
plt.plot(t_sol_damped, x_sol_damped, label='Amortiguado No lineal')
plt.plot(t_sol_lineal_damped, x_sol_lineal_damped, label='Amortiguado Lineal')
plt.xlabel(r'Tiempo(s)')
plt.ylabel(r'$\theta(t)$')


plt.legend(loc='upper left', fontsize=8)

plt.grid(True)
# plt.savefig("./images/amortiguamiento.png", dpi=300, transparent=False)


plt.show()

data = {'Time': t_sol_damped, 'theta': x_sol_damped}
df = pd.DataFrame(data)

df.to_csv('./data/damped.csv', index=False)

data_lineal = {'Time': t_sol_lineal_damped, 'theta': x_sol_lineal_damped}
df = pd.DataFrame(data_lineal)

df.to_csv('./data/linealDamped.csv', index=False)
