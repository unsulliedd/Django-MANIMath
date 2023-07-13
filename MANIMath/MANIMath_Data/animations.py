from manim import *
from sympy import *
from sympy.abc import x
from manim import Line , Polygon
from manim.utils.color import Color
from numpy.polynomial.chebyshev import chebfit, chebval
import requests

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
config.background_color = BLACK
config.background_opacity = 1

#################################### Animations ####################################

################################ Derivative ################################

class Derivative(Scene):
    def construct(self):
        data = api_call()

        function_model = data["function_models"][-1]

        equation = function_model["equation"]
        x_range = [float(i) for i in function_model["x_range"].split(',')]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        domain = [float(i) for i in function_model["domain"].split(',')]
        text_color = function_model["text_color"]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        line_color = function_model["line_color"]
        scale = function_model["scale"]
        include_tip = function_model["include_tip"]
        include_numbers = function_model["include_numbers"]

        function = lambdify(x, sympify(equation))
        derivative = lambdify(x, sympify(equation).diff(x))
        func_str = sympify(equation)
        deriv_str = sympify(equation).diff(x)

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": include_tip, "include_numbers": include_numbers }
        ).set_color(axes_color).scale(scale)
        self.play(Create(axes))

        func_graph = axes.plot(function,x_range=domain ,color=equation_color)
        self.play(Create(func_graph))

        func_label = MathTex("f(x)=", latex(func_str), color=text_color).to_corner(UL)
        self.play(Write(func_label))

        self.wait(2)

        deriv_graph = axes.plot(derivative, color=line_color)
        self.play(Transform(func_graph, deriv_graph))

        deriv_label = MathTex("f'(x)=", latex(deriv_str), color=text_color).next_to(func_label, DOWN)
        self.play(Write(deriv_label))

        self.wait(2)

################################ Integral ###############################

class Integral(Scene):
    def construct(self):
        data = api_call()

        function_model = data["function_models"][-1]

        equation1 = function_model["equation"]
        equation2 = function_model["equation_2"]
        x_range = [float(i) for i in function_model["x_range"].split(',')]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        domain = [float(i) for i in function_model["domain"].split(',')]
        text_color = function_model["text_color"]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        line_color = function_model["line_color"]
        shape_color = function_model["shape_color"]
        scale = function_model["scale"]
        include_tip = function_model["include_tip"]
        include_numbers = function_model["include_numbers"]

        eq1 = sympify(equation1)
        eq2 = sympify(equation2)
        eq = eq1 - eq2
        roots = solve(eq, x)
        r1 = roots[0]
        r2 = roots[1]
        int_area = integrate(eq, (x, r1, r2))

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": include_tip, "include_numbers": include_numbers }
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels()

        self.play(Create(axes))
        self.play(Write(labels))

        curve_1 = axes.plot(lambda x: eval(equation1, {"x": x}), x_range=domain, color=equation_color)
        curve_2 = axes.plot(lambda x: eval(equation2, {"x": x}), x_range=domain, color=equation_color)

        line_1 = axes.get_vertical_line(axes.input_to_graph_point(r1, curve_1), color=line_color)
        line_2 = axes.get_vertical_line(axes.i2gp(r2, curve_2), color=line_color)

        area = axes.get_area(curve_2, [r1, r2], bounded_graph=curve_1, color=shape_color, opacity=0.95)

        curve_1_label = axes.get_graph_label(curve_1, label=MathTex(latex(eq1))).next_to(curve_1, 0.1, 3, DOWN).scale(0.8)
        curve_2_label = axes.get_graph_label(curve_2, label=MathTex(latex(eq2))).next_to(curve_2, 0.1, -2).scale(0.8)

        alan = Tex("Area = ",color=text_color).next_to(area, RIGHT)
        int_area_label = MathTex(latex(int_area),color=text_color).next_to(alan, RIGHT)

        self.play(Create(curve_1))
        self.play(Write(curve_1_label))
        self.play(Create(curve_2))
        self.play(Write(curve_2_label))
        self.play(Create(line_1))
        self.play(Create(line_2))
        self.play(Create(area))
        self.play(Write(alan))
        self.play(Write(int_area_label))
        
        self.wait(2)


################################ Backward Difference ################################

class BackwardDifference(Scene):
    def construct(self):
        data = api_call()

        function_model = data["function_models"][-1]

        equation = function_model["equation"]
        x_range = [float(i) for i in function_model["x_range"].split(',')]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        domain = [float(i) for i in function_model["domain"].split(',')]
        text_color = function_model["text_color"]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        line_color = function_model["line_color"]
        shape_color = function_model["shape_color"]
        scale = function_model["scale"]
        include_tip = function_model["include_tip"]
        include_numbers = function_model["include_numbers"]

        f = lambdify(x, sympify(equation))

        # Backward difference method
        def backward_diff(x, h):
            return (f(x) - f(x - h)) / h

        # Point at which to differentiate
        a = 1

        # Starting, ending, and step values for h
        h_start = 1.0
        h_end = 0.1
        h_step = -0.1

        # Generate list of h values
        h_values = np.arange(h_start, h_end + h_step, h_step)

        # Length of tangent line
        tangent_length = 2

        # Create axes
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": include_tip, "include_numbers": include_numbers }
        ).set_color(axes_color).scale(scale)
        self.play(Create(axes))

        # Create graph of function
        graph = axes.plot(f, x_range=domain, color=equation_color)
        self.play(Create(graph))

        # Add point at which to differentiate
        dot = Dot(color=shape_color).move_to(axes.coords_to_point(a, f(a)))
        self.play(FadeIn(dot))

        # Add label for derivative value
        label = MathTex(f"f'({a}) \\approx ?").next_to(dot, UP)
        self.play(Write(label))

        # Add label for h value
        h_label = MathTex(f"h = ?").next_to(label, UP)
        self.play(Write(h_label))

        # Initialize tangent line
        tangent = Line(
            start=axes.coords_to_point(a - tangent_length / 2, f(a)),
            end=axes.coords_to_point(a + tangent_length / 2, f(a)),
            stroke_width=2,
            color=line_color,
            z_index=1,
        )

        self.play(Create(tangent))

        # Initialize graph of backward difference approximation of derivative
        approx_graph = axes.plot(lambda x: backward_diff(x, h_start), x_range=domain, color=equation_color)
        self.play(Create(approx_graph))

        # Update tangent line and graph using backward difference for different values of h
        for h in h_values:
            # Calculate derivative
            derivative = backward_diff(a, h)

            # Calculate slope of tangent line
            slope = derivative

            # Calculate angle of rotation for tangent line
            angle = np.arctan(slope)

            # Update tangent line by rotating it around the point at which to differentiate
            new_tangent = Line(
                start=axes.coords_to_point(a - tangent_length / 2, f(a) - slope * tangent_length / 2),
                end=axes.coords_to_point(a + tangent_length / 2, f(a) + slope * tangent_length / 2),
                stroke_width=2,
                color=line_color,
                z_index=1,
            )

            self.play(Transform(tangent, new_tangent))

            # Update graph of backward difference approximation of derivative
            new_approx_graph = axes.plot(lambda x: backward_diff(x, h), x_range=domain, color=equation_color)

            self.play(Transform(approx_graph, new_approx_graph))

            # Update label for derivative value
            label_new = MathTex(f"f'({a}) \\approx {derivative:.2f}", color=text_color).next_to(dot, UP)
            self.play(Transform(label, label_new))

            # Update label for h value
            h_label_new = MathTex(f"h = {h:.2f}", color=text_color).next_to(label_new, UP)
            self.play(Transform(h_label, h_label_new))

            self.wait(1)

        self.wait(3)


################################ Chebyshev Approximation ################################

class ChebyshevApproximation(Scene):
    def construct(self):
        data = api_call()
        function_model = data["function_models"][-1]

        equation1 = function_model["equation"]
        x_range = [float(i) for i in function_model["x_range"].split(',')]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        shape_color = function_model["shape_color"]
        scale = function_model["scale"]
        point_1 = function_model["point_1"]
        point_2 = function_model["point_2"]

        function = lambdify(x, sympify(equation1))

        ax = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": False},
            tips=False,
        ).set_color(axes_color).scale(scale)
        labels = ax.get_axis_labels(x_label="x", y_label="y").set_color(axes_color)
        self.play(Create(ax), Write(labels))

        # Plot the function
        graph = ax.plot(function, color=equation_color)
        self.play(Create(graph))

        self.wait(2)

        # Approximate the function using Chebyshev Polynomials
        x_vals = np.linspace(point_1, point_2, 100)
        y_vals = function(x_vals)
        colors = [BLUE, GREEN, RED, ORANGE, PURPLE]
        cheb_graph = None
        dots = []
        for n in range(1, 6):
            coeffs = chebfit(x_vals, y_vals, n)
            cheb_approx = lambda x: chebval(x, coeffs)

            # Plot the Chebyshev approximation
            new_cheb_graph = ax.plot(cheb_approx, color=colors[n-1])
            if cheb_graph is not None:
                self.play(Transform(cheb_graph, new_cheb_graph))
                self.wait(0.5)
            else:
                self.play(Create(new_cheb_graph))
                cheb_graph = new_cheb_graph
                self.wait(0.5)

            # Find and plot the intersection points
            intersections = np.roots(coeffs - chebfit(x_vals, function(x_vals), n))
            intersections = intersections[np.isreal(intersections)]
            new_dots = [Dot(ax.c2p(x, function(x)), color=shape_color) for x in intersections]
            if new_dots:
                self.play(*[Create(dot) for dot in new_dots])
                self.wait(0.5)
                self.play(*[FadeOut(dot) for dot in dots])
                dots = new_dots
        self.wait(2)


############################# Boole's Rule ###############################

class BoolesRule(Scene):
    def construct(self):
        data = api_call()
        function_model = data["function_models"][-1]

        equation = function_model["equation"]
        x_range = [float(i) for i in function_model["x_range"].split(',')]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        shape_color = function_model["shape_color"]
        text_color = function_model["text_color"]
        scale = function_model["scale"]
        iteration = function_model["iteration"]
        point_1 = function_model["point_1"]
        point_2 = function_model["point_2"]

        function = lambdify(x, sympify(equation))

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": False},
            tips=False,
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels(x_label="x", y_label="y").set_color(axes_color)
        self.play(Create(axes), Write(labels))

        func_graph = axes.plot(function, color=equation_color)
        self.play(Create(func_graph))

        # Boole's rule implementation
        a = point_1
        b = point_2
        max_n = iteration
        trapezoids = VGroup()
        result = None
        for n in range(4, max_n+1, 4):
            h = (b-a)/n

            # Show points used in approximation
            points = [a + i*h for i in range(n+1)]
            dots = [Dot(axes.c2p(p, function(p))) for p in points]
            self.play(*[Create(dot) for dot in dots])

            # Show step-by-step calculation
            s = 0
            results = []
            for i, p in enumerate(points):
                if i == 0 or i == n:
                    coef = 7
                elif i % 4 == 1 or i % 4 == 3:
                    coef = 32
                else:
                    coef = 12

                s += coef * function(p)
                result_text = MathTex(f"{coef}f({p})")
                result_text.next_to(dots[i], UP)
                result_text.scale(0.8)
                results.append(result_text)
                self.play(Write(result_text))
                self.wait(0.5)

            s *= (2*h)/45
            result_new = MathTex(f"\\int_{{{a}}}^{{{b}}} f(x) dx \\approx {s:.4f}", color = text_color)
            result_new.to_edge(UP)
            self.play(Write(result_new))

            # Shade area under curve using trapezoids
            trapezoids_new = VGroup()
            for i in range(n):
                x1, y1, _ = axes.c2p(points[i], function(points[i]))
                x2, y2, _ = axes.c2p(points[i+1], function(points[i+1]))
                x3, y3, _ = axes.c2p(points[i+1], 0)
                x4, y4, _ = axes.c2p(points[i], 0)
                trapezoid_points = [[x1,y1,0], [x2,y2,0], [x3,y3,0], [x4,y4,0]]
                trapezoid = VMobject(fill_color=shape_color, fill_opacity=0.3)
                trapezoid.set_points_as_corners(trapezoid_points)
                trapezoids_new.add(trapezoid)
            self.play(Create(trapezoids_new))

            # Remove previous group of points and their labels
            if n < max_n:
                self.play(*[FadeOut(dot) for dot in dots])
                self.play(*[FadeOut(result_text) for result_text in results])
                self.play(FadeOut(trapezoids))
                trapezoids = trapezoids_new
                if result is not None:
                    self.play(FadeOut(result))
                    result = result_new

        self.wait(4)

############################# Adaptive Simpson ############################

class AdaptiveSimpson(Scene):
    def construct(self):
        data = api_call()
        function_model = data["function_models"][-1]

        equation = function_model["equation"]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        shape_color = function_model["shape_color"]
        text_color = function_model["text_color"]
        scale = function_model["scale"]
        iteration = function_model["iteration"]

        f = lambdify(x, sympify(equation))

        # Adaptive Simpson's rule
        def adaptive_simpson(a, b, f, tol=1, depth=0):
            c = (a + b) / 2
            h = b - a
            fa = f(a)
            fb = f(b)
            fc = f(c)
            simpson_approx = h / 6 * (fa + 4 * fc + fb)
            d = (a + c) / 2
            e = (c + b) / 2
            fd = f(d)
            fe = f(e)
            simpson_approx_subintervals = h / 12 * (fa + 4 * fd + 2 * fc + 4 * fe + fb)
            if abs(simpson_approx - simpson_approx_subintervals) <= tol:
                return simpson_approx_subintervals
            else:
                return adaptive_simpson(a, c, f, tol / 2, depth + 1) + adaptive_simpson(c, b, f, tol / 2, depth + 1)

        # Parameters for the animation
        a = 0
        b = 2
        tol = iteration

        # Create axes
        axes = Axes(
            x_range=[a, b],
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": False},
            tips=False,
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels(x_label="x", y_label="y").set_color(axes_color)
        self.play(Create(axes), Write(labels))

        # Plot the function
        graph = axes.plot(f, color=equation_color)
        self.play(Create(graph))


        # Create the initial rectangle
        c = (a + b) / 2
        rectangle = Rectangle(
            width=b - a,
            height=f(c),
            stroke_width=2,
            fill_opacity=0.2,
            fill_color=shape_color,
            sheen_direction=UP,
            sheen_factor=0.3,
        ).move_to(axes.c2p((a + b) / 2, 0))
        self.play(Create(rectangle))

        # Show the integral value
        integral_text = MathTex(r"\text{Approximation: }", color=text_color).next_to(axes, UP)
        integral_value = MathTex(f"{adaptive_simpson(a, b, f, tol):.3f}",color=text_color).next_to(integral_text, RIGHT)
        self.play(Create(integral_text), Create(integral_value))

        self.wait(1)

        # Recursive function to split the interval
        def split_interval(a, b, depth=0):
            if depth > 3:  # Limit the depth
                return
            c = (a + b) / 2
            fc = f(c)
            left_rectangle = Rectangle(
                width=c - a,
                height=fc,
                stroke_width=1,
                fill_opacity=0.2,
                fill_color=shape_color,
                sheen_direction=UP,
                sheen_factor=0.3,
            ).move_to(axes.c2p((a + c) / 2, 0))
            right_rectangle = Rectangle(
                width=b - c,
                height=fc,
                stroke_width=1,
                fill_opacity=0.2,
                fill_color=shape_color,
                sheen_direction=UP,
                sheen_factor=0.3,
            ).move_to(axes.c2p((c + b) / 2, 0))
            self.play(Create(left_rectangle), Create(right_rectangle))
            self.wait(0.5)

            left_area = MathTex(f"{adaptive_simpson(a, c, f, tol / 2):.2f}",color=text_color).next_to(left_rectangle, UP).scale(0.5)
            right_area = MathTex(f"{adaptive_simpson(c, b, f, tol / 2):.2f}",color=text_color).next_to(right_rectangle, UP).scale(0.5)
            self.play(Create(left_area), Create(right_area))
            self.wait(0.5)
            
            self.remove(left_area,right_area)
            self.wait(0.5)

            split_interval(a, c, depth + 1)
            split_interval(c, b, depth + 1)

        # Start splitting the interval
        split_interval(a, b)

        self.wait(2)

############################# Left Endpoint Rule #############################

class LeftEndpointRule(Scene):
    def construct(self):
        data = api_call()
        function_model = data["function_models"][-1]

        equation = function_model["equation"]
        x_range = [float(i) for i in function_model["x_range"].split(',')]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        shape_color = function_model["shape_color"]
        text_color = function_model["text_color"]
        scale = function_model["scale"]
        iteration = function_model["iteration"]
        point_1 = function_model["point_1"]
        point_2 = function_model["point_2"]

        f = lambdify(x, sympify(equation))

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": False},
            tips=False,
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels(x_label="x", y_label="y").set_color(axes_color)
        self.play(Create(axes), Write(labels))

        # Plot the function
        graph = axes.plot(f, color=equation_color)
        self.play(Create(graph))

        # Variables for calculating the integral
        a = point_1  # Start point
        b = point_2  # End point
        n = iteration  # Number of subintervals
        dx = (b - a) / n  # Width of each subinterval

        area = 0
        for i in range(n):
            x1 = a + i * dx
            x2 = x1 + dx
            y1 = f(x1)
            points = [axes.c2p(x1, 0), axes.c2p(x1, y1), axes.c2p(x2, y1), axes.c2p(x2, 0)]
            rect = Polygon(*points, fill_opacity=0.5, fill_color=shape_color)
            self.play(Create(rect))
            rect_area = y1 * dx
            area += rect_area
            arrow = Arrow(start=rect.get_bottom(), end=rect.get_bottom() + DOWN * 0.5)
            area_text = MathTex(f"{rect_area:.2f}").next_to(arrow, DOWN)
            self.play(Create(arrow), Create(area_text))
            self.wait(0.5)

        total_area_text = MathTex(r"\text{Total Area: }", f"{area:.2f}", color=text_color).to_edge(UP)
        self.play(Create(total_area_text))

        self.wait()

################################ Riemann Sum ################################

class RiemannSum(Scene):
    def construct(self):
        data = api_call()
        function_model = data["function_models"][-1]

        equation = function_model["equation"]
        x_range = [float(i) for i in function_model["x_range"].split(',')]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        domain = [float(i) for i in function_model["domain"].split(',')]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        shape_color = function_model["shape_color"]
        text_color = function_model["text_color"]
        scale = function_model["scale"]
        iteration = function_model["iteration"]
        x = symbols('x')
        func = lambdify(x, sympify(equation))

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": False},
            tips=False,
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels(x_label="x", y_label="y").set_color(axes_color)
        self.play(Create(axes), Write(labels))

        # Plot the function
        graph = axes.plot(func, domain, color=equation_color)
        self.play(Create(graph))

        # Set the number of rectangles to use for the Riemann sum
        n = iteration

        # Calculate the width of each rectangle
        dx = (4 - 0) / n

        # Create the rectangles for the Riemann sum
        rects = VGroup()
        for i in range(n):
            x = i * dx
            y = func(x)
            rect = Rectangle(
                width=dx,
                height=y,
                fill_opacity=0.5,
                fill_color=shape_color
            )
            rect.next_to(axes.c2p(x, 0), UP, buff=0)
            rects.add(rect)
        self.play(Create(rects))

        # Add a label to show the value of the Riemann sum
        riemann_sum = sum([rect.height for rect in rects]) * dx
        riemann_sum_label = MathTex(f"\\sum f(x_i) \\Delta x = {riemann_sum:.2f}",color=text_color).to_edge(UP)
        self.play(Write(riemann_sum_label))

        self.wait(2)

############################

class TrapezoidalRule(Scene):
    def construct(self):
        data = api_call()
        function_model = data["function_models"][-1]

        equation = function_model["equation"]
        x_range = [float(i) for i in function_model["x_range"].split(',')]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        domain = [float(i) for i in function_model["domain"].split(',')]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        shape_color = function_model["shape_color"]
        text_color = function_model["text_color"]
        scale = function_model["scale"]
        iteration = function_model["iteration"]
        point_1 = function_model["point_1"]
        point_2 = function_model["point_2"]

        x = symbols('x')
        f = lambdify(x, sympify(equation))

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": False},
            tips=False,
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels(x_label="x", y_label="y").set_color(axes_color)
        self.play(Create(axes), Write(labels))

        # Plot the function
        graph = axes.plot(f, domain, color=equation_color)
        self.play(Create(graph))

        a = point_1  
        b = point_2 
        n = iteration  
        dx = (b - a) / n

        area = 0
        for i in range(n):
            x1 = a + i * dx
            x2 = x1 + dx
            y1 = f(x1)
            y2 = f(x2)
            points = [axes.c2p(x1, 0), axes.c2p(x1, y1), axes.c2p(x2, y2), axes.c2p(x2, 0)]
            trapezoid = Polygon(*points, fill_opacity=0.5, fill_color=shape_color)
            self.play(Create(trapezoid))
            trapezoid_area = (y1 + y2) * dx / 2
            area += trapezoid_area
            arrow = Arrow(start=trapezoid.get_bottom(), end=trapezoid.get_bottom() + DOWN * 0.5)
            area_text = MathTex(f"{trapezoid_area:.2f}", color=text_color).next_to(arrow, DOWN)
            self.play(Create(arrow), Create(area_text))
            self.wait(0.5)

        total_area_text = MathTex(r"\text{Total Area: }", f"{area:.2f}",color=text_color).to_edge(UP)
        self.play(Create(total_area_text))

        self.wait()


############################# Fourier Transform of Data #############################

class FourierTransformOfData(Scene):
    def construct(self):
        data = api_call()
        function_model = data["function_models"][-1]

        input_array = [int(i) for i in function_model["input_array"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        axes_color = function_model["axes_color"]
        text_color = function_model["text_color"]
        scale = function_model["scale"]

        # Create the axes
        axes = Axes(
            x_range=[0, len(input_array)],
            y_range=[-60, 60 ,6],
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": False, "include_numbers" : True}
        ).set_color(axes_color).scale(scale)
        self.play(Create(axes))

        # Create the data points
        data_points = [axes.c2p(x, y) for x, y in enumerate(input_array)]
        data_graph = VMobject().set_points_as_corners(data_points)
        self.play(Create(data_graph))

        # Create the label for the time domain
        time_label = Tex("Time Domain",color=text_color).next_to(axes, DOWN)
        frequency_label = Tex("Frequency Domain",color=text_color).next_to(axes, UP)
        self.play(Write(time_label))
        self.wait()

        # Transform the data into its Fourier transform
        fourier_transform = np.abs(np.fft.fftshift(np.fft.fft(input_array)))
        fourier_points = [axes.c2p(x, y) for x, y in enumerate(fourier_transform)]
        fourier_lines = [Line(axes.c2p(x, 0), point) for x, point in enumerate(fourier_points)]
        time_label.animate.next_to(axes, UP)

        self.play(
            *[Create(line) for line in fourier_lines],
            *[Uncreate(line) for line in data_graph],  
        )
        self.play(time_label.animate.next_to(axes, UP))
        self.play(FadeOut(time_label))
        self.play(Write(frequency_label))
        self.wait(0.5)

        # Connect the points with a line
        fourier_graph = VMobject().set_points_as_corners(fourier_points).set_color(BLUE)
        self.play(Create(fourier_graph))

        self.wait(2)

######################### Lagrange Polynomial #########################

class LagrangePolynomial(Scene):
    def construct(self):
        data = api_call()
        function_model = data["function_models"][-1]

        input_str = function_model["input_array"].split(',')
        input_array = [(int(input_str[i]), int(input_str[i+1])) for i in range(0, len(input_str), 2)]        
        x_range = [float(i) for i in function_model["x_range"].split(',')]
        y_range = [float(i) for i in function_model["y_range"].split(',')]
        x_length = function_model["x_length"]
        y_length = function_model["y_length"]
        equation_color = function_model["equation_color"]
        axes_color = function_model["axes_color"]
        scale = function_model["scale"]

        # Create the axes
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": False},
            tips=False,
        ).set_color(axes_color).scale(scale)

        # Create dots for the points

        dots = VGroup(*[Dot(axes.c2p(x, y)) for x, y in input_array])
        self.play(Create(dots))

        # Define the Lagrange basis polynomials
        def L(k, x):
            prod = 1
            for i, (xi, yi) in enumerate(input_array):
                if i != k:
                    prod *= (x - xi) / (input_array[k][0] - xi)
            return prod

        # Define the Lagrange polynomial
        def P(x):
            return sum([input_array[k][1] * L(k, x) for k in range(len(input_array))])

        # Create the graph of the Lagrange polynomial
        graph = axes.plot(P, [-10, 10], color=equation_color)
        self.play(Create(graph))

        self.wait(2)

############################## Newton Raphson ##############################

class NewtonRaphson(Scene):
    def __init__(self, **kwargs):
        func = "3*exp(x) - 4*cos(x)"
        sfunc = sympify(func)
        self.function = lambdify(x, sfunc)
        self.derivative = lambdify(x, sfunc.diff(x))
        super().__init__(**kwargs)

    def construct(self):
        data = api_call()
        root_finding_model = data["root_finding_models"][-1]

        equation = root_finding_model["equation"]
        x_range = [float(i) for i in root_finding_model["x_range"].split(',')]
        y_range = [float(i) for i in root_finding_model["y_range"].split(',')]
        x_length = root_finding_model["x_length"]
        y_length = root_finding_model["y_length"]
        iteration = root_finding_model["iteration"]
        text_color = root_finding_model["text_color"]
        equation_color = root_finding_model["equation_color"]
        axes_color = root_finding_model["axes_color"]
        line_color = root_finding_model["line_color"]
        shape_color = root_finding_model["shape_color"]
        scale = root_finding_model["scale"]
        include_tip = root_finding_model["include_tip"]
        include_numbers = root_finding_model["include_numbers"]

        function = lambdify(x, sympify(equation))
        derivative = lambdify(x, sympify(equation).diff(x))

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": include_tip, "include_numbers": include_numbers }
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels()

        self.play(Create(axes))
        self.play(Write(labels))

        
        graph = axes.plot(function, color=equation_color)
        self.add(graph)

        # Define the accuracy
        tol = 0.001

        # Define the initial point
        x0 = 1

        # Create a dot and a label for the initial point
        dot = Dot(axes.c2p(x0, function(x0)), color=shape_color)
        label = MathTex("x_0", color=text_color).next_to(dot, RIGHT)
        value_label = MathTex(f"f(x_0)={function(x0):.3f}",color=text_color).next_to(label, RIGHT)
        self.play(Create(dot), Write(label), Write(value_label))

        # Create a vertical line from the x-axis to the initial point
        line = Line(axes.c2p(x0, 0), dot.get_center(), color=line_color)
        self.play(Create(line))

        # Create a loop to find the root
        max_iterations = iteration
        counter = 0
        i = 1
        while abs(function(x0)) > tol and counter < max_iterations:
            # Calculate the next point using Newton's formula
            x1 = x0 - function(x0) / derivative(x0)

            # Create a dot and a label for the next point
            dot1 = Dot(axes.c2p(x1, function(x1)), color=shape_color)
            label1 = MathTex(f"x_{i}",color=text_color).next_to(dot1, RIGHT)
            value_label1 = MathTex(f"f(x_{i})={function(x1):.3f}",color=text_color).next_to(label1, RIGHT)

            # Create a line from the initial point to the next point
            line1 = Line(dot.get_center(), dot1.get_center(), color=line_color)

            # Create a tangent line at the initial point
            tangent = TangentLine(graph, alpha=x0, length=5, color=GREEN)

            # Animate the tangent line, the line and the next point
            self.play(Create(tangent))
            self.play(Create(line1))
            self.play(Transform(dot, dot1), Transform(label, label1), Transform(value_label, value_label1))

            # Create a vertical line from the x-axis to the next point
            line2 = Line(axes.c2p(x1, 0), dot.get_center(), color=shape_color)
            self.play(Create(line2))

            # Update the initial point
            x0 = x1
            i += 1
            counter += 1

        # Create a final label for the root
        root = MathTex(f"\\text{{Root}} \\approx {x0:.3f}",color=text_color).to_edge(DOWN)
        self.play(Write(root))

        self.wait(2)

############################### Regula Falsi ###############################

class RegulaFalsi(Scene):
    def construct(self):
        data = api_call()
        root_finding_model = data["root_finding_models"][-1]

        equation = root_finding_model["equation"]
        x_range = [float(i) for i in root_finding_model["x_range"].split(',')]
        y_range = [float(i) for i in root_finding_model["y_range"].split(',')]
        x_length = root_finding_model["x_length"]
        y_length = root_finding_model["y_length"]
        point_1 = root_finding_model["point_1"]
        point_2 = root_finding_model["point_2"]
        text_color = root_finding_model["text_color"]
        equation_color = root_finding_model["equation_color"]
        axes_color = root_finding_model["axes_color"]
        line_color = root_finding_model["line_color"]
        shape_color = root_finding_model["shape_color"]
        scale = root_finding_model["scale"]
        include_tip = root_finding_model["include_tip"]
        include_numbers = root_finding_model["include_numbers"]

        function = lambdify(x, sympify(equation))

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": include_tip, "include_numbers": include_numbers }
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels()

        self.play(Create(axes))
        self.play(Write(labels))

        # Add graph of function
        func_graph = axes.plot(function, color=equation_color)
        self.play(Create(func_graph))
        
        # Add starting points
        a = point_1
        b = point_2
        fa = function(a)
        fb = function(b)
        point_a = Dot(color=shape_color).move_to(axes.c2p(a, fa))
        point_b = Dot(color=shape_color).move_to(axes.c2p(b, fb))
        self.play(FadeIn(point_a), FadeIn(point_b))
        
        # Add vertical lines
        line_a = Line(axes.c2p(a, fa), axes.c2p(a, 0), color=line_color)
        line_b = Line(axes.c2p(b, fb), axes.c2p(b, 0), color=line_color)
        self.play(Create(line_a), Create(line_b))
        
        # Add iterations
        x_label = None
        for n in range(4):
            # Draw line between points a and b
            line = Line(axes.c2p(a, fa), axes.c2p(b, fb), color=line_color)
            self.play(Create(line))
            
            # Find intersection with x-axis
            c = (a*fb - b*fa) / (fb - fa)
            fc = function(c)
            intersection = line_intersection(line.get_start_and_end(), [axes.c2p(c, 0), axes.c2p(c, fc)])
            point_c = Dot(color=shape_color).move_to(intersection)
            self.play(FadeIn(point_c))
            
            # Update points
            if fa * fc < 0:
                b, fb = c, fc
                self.play(point_b.animate.move_to(point_c.get_center()))
                self.play(Transform(line_b, Line(axes.c2p(b, fb), axes.c2p(b, 0), color=line_color)))
            else:
                a, fa = c, fc
                self.play(point_a.animate.move_to(point_c.get_center()))
                self.play(Transform(line_a, Line(axes.c2p(a, fa), axes.c2p(a, 0), color=line_color)))
            
            # Update label
            if x_label is not None:
                self.remove(x_label)
            x_label = MathTex(f"x_{n+1} = {c:.2f}",color=text_color).next_to(point_c, DOWN)
            self.play(Write(x_label))      
            self.wait(1)
                    
        self.wait(2)

############################## Secant Method ##############################

class SecantMethod(Scene):
    def construct(self):
        data = api_call()
        root_finding_model = data["root_finding_models"][-1]

        equation = root_finding_model["equation"]
        x_range = [float(i) for i in root_finding_model["x_range"].split(',')]
        y_range = [float(i) for i in root_finding_model["y_range"].split(',')]
        x_length = root_finding_model["x_length"]
        y_length = root_finding_model["y_length"]
        point_1 = root_finding_model["point_1"]
        point_2 = root_finding_model["point_2"]
        text_color = root_finding_model["text_color"]
        equation_color = root_finding_model["equation_color"]
        axes_color = root_finding_model["axes_color"]
        line_color = root_finding_model["line_color"]
        shape_color = root_finding_model["shape_color"]
        scale = root_finding_model["scale"]
        include_tip = root_finding_model["include_tip"]
        include_numbers = root_finding_model["include_numbers"]

        function = lambdify(x, sympify(equation))

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": include_tip, "include_numbers": include_numbers }
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels()

        self.play(Create(axes))
        self.play(Write(labels))

        # Add graph of function
        func_graph = axes.plot(function, color=equation_color)
        self.play(Create(func_graph))
        
        # Add starting points
        x0 = point_1
        x1 = point_2
        fx0 = function(x0)
        fx1 = function(x1)
        point_x0 = Dot(color=shape_color).move_to(axes.c2p(x0, fx0))
        point_x1 = Dot(color=shape_color).move_to(axes.c2p(x1, fx1))
        self.play(FadeIn(point_x0), FadeIn(point_x1))
        
        # Add iterations
        x_label = None
        for n in range(4):
            # Draw line between points x0 and x1
            line = Line(axes.c2p(x0, fx0), axes.c2p(x1, fx1), color=line_color)
            self.play(Create(line))
            
            # Find intersection with x-axis
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            fx2 = function(x2)
            intersection = line_intersection(line.get_start_and_end(), [axes.c2p(x2, 0), axes.c2p(x2, fx2)])
            point_x2 = Dot(color=shape_color).move_to(intersection)
            self.play(FadeIn(point_x2))
            
            # Update points
            x0, x1 = x1, x2
            fx0, fx1 = fx1, fx2
            
            # Update label
            if x_label is not None:
                self.remove(x_label)
            x_label = MathTex(f"x = {x2:.2f}",color=text_color).next_to(point_x2, DOWN)
            self.play(Write(x_label))
            
            self.wait()
        
        self.wait()


############################## Bisection Method  ##############################

class BisectionMethod(Scene):
    def construct(self):
        data = api_call()
        root_finding_model = data["root_finding_models"][-1]

        equation = root_finding_model["equation"]
        x_range = [float(i) for i in root_finding_model["x_range"].split(',')]
        y_range = [float(i) for i in root_finding_model["y_range"].split(',')]
        x_length = root_finding_model["x_length"]
        y_length = root_finding_model["y_length"]
        iteration = root_finding_model["iteration"]
        point_1 = root_finding_model["point_1"]
        point_2 = root_finding_model["point_2"]
        text_color = root_finding_model["text_color"]
        equation_color = root_finding_model["equation_color"]
        axes_color = root_finding_model["axes_color"]
        line_color = root_finding_model["line_color"]
        shape_color = root_finding_model["shape_color"]
        scale = root_finding_model["scale"]
        include_tip = root_finding_model["include_tip"]
        include_numbers = root_finding_model["include_numbers"]

        function = lambdify(x, sympify(equation))

        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={"include_tip": include_tip, "include_numbers": include_numbers }
        ).set_color(axes_color).scale(scale)

        labels = axes.get_axis_labels()

        a = point_1
        b = point_2
        tolerance = 0.001
        max_iterations = iteration

        self.play(Create(axes))
        self.play(Write(labels))

        # Add graph of function
        func_graph = axes.plot(function, color=equation_color)
        self.play(Create(func_graph))

        # Create the graph of the equation
        graph = axes.plot(function, [a,b])
        self.play(Create(graph))

        # Create two vertical lines to show the initial interval
        interval_lines = VGroup(
            Line(start=axes.c2p(a, 0), end=axes.c2p(a, function(a)), color=line_color),
            Line(start=axes.c2p(b, 0), end=axes.c2p(b, function(b)), color=line_color)
        )
        self.play(Create(interval_lines))

        # Add labels to show the initial interval
        a_label = MathTex("a", "=", str(a)).next_to(interval_lines[0], LEFT)
        b_label = MathTex("b", "=", str(b)).next_to(interval_lines[1], RIGHT)
        self.play(Write(a_label), Write(b_label))

        # Apply the bisection method step by step
        interval_label = None
        for i in range(max_iterations):
            # Bisect the interval
            c = (a + b) / 2

            # Create a vertical line to show the midpoint of the interval
            midpoint_line = Line(
                start=axes.c2p(c, 0),
                end=axes.c2p(c, function(c)),
                color=shape_color
            )
            self.play(Create(midpoint_line))

            # Calculate the value of the function at the midpoint
            f_c = function(c)

            # Remove previous interval label if it exists
            if interval_label is not None:
                self.remove(interval_label)

            # Add a label to show how much the interval has been reduced
            interval_label = MathTex("b - a", "=", str(b - a), color=text_color).next_to(midpoint_line, UP)
            self.play(Write(interval_label))

            # Stop the loop if a root has been found or if the tolerance has been reached
            if abs(f_c) < tolerance or b - a < tolerance:
                break

            # Update the interval
            if self.function(a) * f_c < 0:
                b = c
                b_label[2].set_value(str(b))
            else:
                a = c
                a_label[2].set_value(str(a))
            self.wait()

        # Display final interval found by bisection method
        final_interval_label = MathTex(f"x = {a:.1f}, y = {b:.1f}", color=text_color).to_edge(UP)
        self.play(Write(final_interval_label))
        
        self.wait(2)
