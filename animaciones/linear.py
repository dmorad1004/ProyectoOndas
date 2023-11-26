import manim as mn
import numpy as np

PI = np.pi


class LinearPendulum(mn.Scene):
    def construct(self):
        time = mn.ValueTracker(0)
        lenght = 3
        g = 9.8
        w = np.sqrt(g/lenght)
        # period = 2*PI/w
        max_theta = PI/14

        theta = mn.DecimalNumber().set_theta = mn.DecimalNumber(
        ).set_color(mn.BLACK).move_to(15*mn.RIGHT)
        theta.add_updater(lambda m: m.set_value(
            max_theta * np.cos(w*time.get_value())))
        self.add(theta)

        def get_line(x, y):
            line = mn.Line(start=mn.ORIGIN, end=x *
                           mn.RIGHT+y*mn.UP, color=mn.BLUE)
            global vertical_line

            vertical_line = mn.DashedLine(
                start=line.get_start(), end=line.get_start()+3*mn.DOWN)
            return line

        line = mn.always_redraw(lambda: get_line(
            lenght*np.sin(theta.get_value()), -lenght*np.cos(theta.get_value())))

        self.add(line, vertical_line)

        def angle_arc(theta):
            global angle
            global arc_text
            if theta == 0:
                angle = mn.VectorizedPoint().move_to(10*mn.RIGHT)
                arc_text = mn.VectorizedPoint().move_to(10*mn.RIGHT)
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
            dot = mn.Dot(fill_color=mn.BLUE, fill_opacity=1).move_to(
                x*mn.RIGHT+y*mn.UP).scale(lenght)
            return dot

        ball = mn.always_redraw(lambda: get_ball(
            lenght*np.sin(theta.get_value()), -lenght*np.cos(theta.get_value())))

        self.add(ball)
        self.play(time.animate.set_value(20),
                  rate_func=mn.linear, run_time=20)
