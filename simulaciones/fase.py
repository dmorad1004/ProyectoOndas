
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()
sns.set_context("notebook")

mass = 1
length = 3
g = 9.8

times = np.linspace(0, 4*np.pi, 100000)


def canonical_momentum_theta(E, m, g, l, theta):
    """
    Calcula el momento canónico respecto a theta 

    Parámetros:
    - E (float): Energía total del sistema.
    - m (float): Masa del objeto.
    - g (float): Aceleración debida a la gravedad.
    - l (float): Longitud del péndulo.
    - theta (float): Ángulo de desplazamiento desde la vertical.

    Retorna:
    float: Momento canónico respecto a theta para el sistema.
    """
    return 2*m*l**(2)*np.sqrt(E + m*g*l*np.cos(theta))


plt.figure(figsize=(10, 6))
plt.plot(times, canonical_momentum_theta(
    2, mass, g, length, times), 'b', label='E < mgl')
plt.plot(times, canonical_momentum_theta(mass*g*length, mass, g,
         length, times), 'r', label='E = mgl')
plt.plot(times, canonical_momentum_theta(2*mass*g*length, mass, g,
         length, times), 'y', label='E > mgl')

plt.plot(times, -canonical_momentum_theta(2, mass, g, length, times), 'b')
plt.plot(times, -canonical_momentum_theta(mass *
         g*length, mass, g, length, times), 'r')
plt.plot(times, -canonical_momentum_theta(2*mass *
         g*length, mass, g, length, times), 'y')


plt.xlabel(r'$\theta$')
plt.ylabel(r'$p_{\theta}$')
plt.legend()
plt.grid(True)
plt.savefig("./images/fase.png", dpi=300)
plt.show()
