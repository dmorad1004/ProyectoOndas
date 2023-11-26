import manim as mn
import numpy as np

PI = np.pi

data = np.genfromtxt("../simulaciones/data/nolinear.csv",
                     delimiter=",", skip_header=1, dtype=np.float64)

time_data = data[:, 0]
theta_data = data[:, 1]

time_data = np.trunc(time_data*1000)/1000


class NoLinearPendulum(mn.Scene):

    mn.CONFIG = {
        "frame_rate": 10
    }

    def construct(self):
        length = 3

        time = mn.ValueTracker(0)

        theta = mn.DecimalNumber().set_color(mn.BLACK).move_to(15 * mn.RIGHT)

        self.add(theta)

        def get_line(x, y):
            line = mn.Line(start=mn.ORIGIN, end=x *
                           mn.RIGHT + y * mn.UP, color=mn.BLUE)
            global vertical_line
            vertical_line = mn.DashedLine(
                start=line.get_start(), end=line.get_start() + 3 * mn.DOWN)
            return line

        line = mn.always_redraw(lambda: get_line(
            length * np.sin(theta.get_value()), -length * np.cos(theta.get_value())))
        self.add(line, vertical_line)

        def angle_arc(theta):
            global angle
            global arc_text
            if theta == 0:
                angle = mn.VectorizedPoint().move_to(10 * mn.RIGHT)
                arc_text = mn.VectorizedPoint().move_to(10 * mn.RIGHT)
            elif theta > 0:
                angle = mn.Angle(line, vertical_line, quadrant=(
                    1, 1), other_angle=True, color=mn.YELLOW, fill_opacity=0)
            else:
                angle = mn.Angle(line, vertical_line, quadrant=(
                    1, 1), other_angle=False, color=mn.YELLOW, fill_opacity=0)
            return angle

        angle = mn.always_redraw(lambda: angle_arc(theta.get_value()))
        self.add(angle)

        arctext = mn.MathTex(r"\theta").scale(0.5).add_updater(
            lambda m: m.next_to(angle, mn.DOWN))
        self.add(arctext)

        def get_ball(x, y):
            dot = mn.Dot(fill_color=mn.RED, fill_opacity=1).move_to(
                x * mn.RIGHT + y * mn.UP).scale(length)
            return dot

        ball = mn.always_redraw(lambda: get_ball(
            length * np.sin(theta.get_value()), -length * np.cos(theta.get_value())))
        self.add(ball)

        # Función para actualizar theta con respecto al tiempo

        def get_theta_at_time(t):
            time_trunc = t*1000
            # print(t, ",", time_trunc, ",", theta_data[int(time_trunc)])
            return theta_data[int(time_trunc)]

        # Usa la función en lugar de la actualización en tiempo real
        theta.add_updater(lambda m: m.set_value(
            get_theta_at_time(time.get_value())))

        self.play(time.animate.set_value(20),
                  rate_func=mn.linear, run_time=20)
