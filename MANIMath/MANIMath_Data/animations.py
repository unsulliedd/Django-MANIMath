from manim import *
from sympy import *
from manim.utils.color import Color 
import requests
import random

####################################  Api Call ####################################

def api_call():
    base_url = 'http://localhost:61000/api/models/'
    url = f'{base_url}'
    headers = {'Authorization': 'Token c345e2d3135f5ceb80374d5fe6cbff13d9dbbb7a'}
    try:
        response = requests.get(url, headers=headers) 
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        print('HTTP Error:', e.response.status_code)
        return None


#################################### Manim Config ####################################

config.media_dir = r"MANIMath_WebUI/static/media/manim"
config.background_color = WHITE
config.background_opacity = 1

#################################### Animations ####################################

############################## Integral ##############################

class Integral(Scene):
    def construct(self):
        data = api_call()

        equation1 = data["function_models"][-1]["equation1"]
        equation2 = data["function_models"][-1]["equation2"]
        t1 = -10
        t2 = 10

        # Takes a string of variable names separated by spaces or commas, and creates Symbols out of them
        x = symbols('x')

        # Converts an arbitrary expression to a type that can be used inside SymPy
        eq1 = sympify(equation1)
        eq2 = sympify(equation2)

        # Calculates the difference of equations
        eq = eq1 - eq2

        # Calculates the roots of the equation
        roots = solve((eq),(x))

        # Roots of quadratic equation
        r1 = roots[0]
        r2 = roots[1]

        # Calculates definite integral with respected roots
        int_area = integrate(eq,(x,r1,r2))

        ax = Axes(
            x_range=[-10, 10, 0.5],         # Intervals of the x-axis
            y_range=[-10, 10, 0.5],         # Intervals of the y-axis
            x_length=7,                    # Length of the x-axis
            y_length=7,                    # Length of the y-axis

            # Shows the roots of the equation on the x-axis
            # x_axis_config={"numbers_to_include": [r1, r2]},
            tips=False,
        ).set_color(BLACK)

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: eval(equation1,{"x": x}), x_range=[t1, t2], color=Color("#105080"))
        curve_2 = ax.plot(lambda x: eval(equation2,{"x": x}), x_range=[t1, t2], color=RED)

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(r1, curve_1), color=Color("#800080"))
        line_2 = ax.get_vertical_line(ax.i2gp(r2, curve_2), color=YELLOW)
        
        area = ax.get_area(curve_2, [r1, r2], bounded_graph=curve_1, color=Color("#452158"), opacity=0.95)

        curve_1_label = ax.get_graph_label(curve_1, label=MathTex(latex(eq1))).next_to(curve_1,0.1, 3,DOWN).scale(0.8)
        curve_2_label = ax.get_graph_label(curve_2, label=MathTex(latex(eq2))).next_to(curve_2,0.1,-2).scale(0.8)
        
        alan = Tex("Alan = ").next_to(area,RIGHT)

        int_area_label = MathTex(latex(int_area)).next_to(alan,RIGHT)

        self.play(Create(ax))
        self.play(Write(labels))
        self.play(Create(curve_1))
        self.play(Write(curve_1_label))
        self.play(Create(curve_2))
        self.play(Write(curve_2_label))
        self.play(Create(line_1))
        self.play(Create(line_2))
        self.play(Create(area))
        self.play(Write(alan))
        self.play(Write(int_area_label))
        g = VGroup(ax, labels, curve_1, curve_1_label, curve_2, curve_2_label, line_1, line_2, area, alan, int_area_label)
        self.play(g.animate.scale(0.5).to_corner(UP+LEFT*2))


#################################### Dictionary ####################################

animations = {
    "Integral": Integral,
}