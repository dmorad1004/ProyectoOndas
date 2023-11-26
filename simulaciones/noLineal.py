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


# pi/14

PI = np.pi
THETA0 = PI/6
V0 = 0.0
T0 = 0
TF = 20
step = 0.001


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


def linearPendulum(t, x, v):
    """
  Ecuación diferencial para un péndulo  lineal.

  Parameters:
  - t: Tiempo actual
  - x: Posición angular actual
  - v: Velocidad angular actual

  Returns:
  -  Tasa de cambio de la velocidad angular
  """
    return -g/length * x


def graph_different_angles():
    initial_angle = PI/24

    fig, ax = plt.subplots(figsize=(10, 6))

    for i in [1, 2, 4, 6, 8, 10]:
        times, angles = RK4(nonLinearPendulum, i *
                            initial_angle, V0, T0, TF, step)
        ax.plot(times, angles, label=rf"{i} $\theta_{{0}}$")

    ax.set_xlabel(r'Tiempo(s)')
    ax.set_ylabel(r'$\theta(t)$')
    plt.legend()
    plt.savefig("./images/angulos.png", dpi=300)

    # Solución del sistema de ecuaciones utilizando Runge-Kutta de cuarto orden
t_sol, x_sol = RK4(nonLinearPendulum, THETA0, V0, T0, TF, step)
t_sol_lineal, x_sol_lineal = RK4(linearPendulum, THETA0, V0, T0, TF, step)


data = {'Time': t_sol, 'theta': x_sol}
df = pd.DataFrame(data)

df.to_csv('./data/nolinear.csv', index=False)

# Graficar la solución

# graph_different_angles()

plt.figure(figsize=(10, 6))
plt.plot(t_sol, x_sol, label=r'No lineal')
plt.plot(t_sol_lineal, x_sol_lineal, label='lineal')

# para ángulos pequeños
# plt.plot(t_sol, x_sol, marker="*", label='No lineal', markersize="5")
# plt.plot(t_sol_lineal, x_sol_lineal, label='lineal')

plt.xlabel(r'Tiempo(s)')
plt.ylabel(r'$\theta(t)$')

plt.legend()
plt.grid(True)
# plt.savefig("./images/pi25.png", dpi=300)
# plt.savefig("./images/linealidad.png", dpi=300)
plt.show()
