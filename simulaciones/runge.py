import numpy as np


def RK4(func, x0, v0, t0, tf, h):
    """
    Implementa el método de Runge-Kutta de cuarto orden para resolver ecuaciones diferenciales de segundo orden.

    Parameters:
    - func: Función que representa la ecuación diferencial = func(t, x, v)
    - x0: Valor inicial de posición en t0
    - v0: Valor inicial de velocidad en t0
    - t0: Valor inicial de tiempo
    - tf: Valor final de tiempo
    - h: Tamaño del paso

    Returns:
    - t_values: Lista de valores de tiempo
    - x_values: Lista de valores de posición correspondientes a los valores de tiempo
    """
    t_values = [t0]
    x_values = [x0]

    while t0 < tf:
        # Calcular las pendientes k1, k2, k3, y k4 para posición y velocidad
        k1x = h * v0
        k1v = h * func(t0, x0, v0)

        k2x = h * (v0 + k1v/2)
        k2v = h * func(t0 + h/2, x0 + k1x/2, v0 + k1v/2)

        k3x = h * (v0 + k2v/2)
        k3v = h * func(t0 + h/2, x0 + k2x/2, v0 + k2v/2)

        k4x = h * (v0 + k3v)
        k4v = h * func(t0 + h, x0 + k3x, v0 + k3v)

        # Actualizar posición y velocidad usando la fórmula de Runge-Kutta
        x0 = x0 + (k1x + 2*k2x + 2*k3x + k4x)/6
        v0 = v0 + (k1v + 2*k2v + 2*k3v + k4v)/6
        t0 = t0 + h

        # Agregar los valores calculados a las listas
        t_values.append(np.float64(t0))
        x_values.append(np.float64(x0))

    return np.array(t_values), np.array(x_values)
