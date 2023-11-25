from manim import *

class dots(Scene):
    def construct(self):
        titolo=Tex("Problema 1")
        titolo.to_corner(UP + LEFT)
        self.add(titolo)
        person =  SVGMobject(r"person.svg").set_color(GREEN)
        campione1 = Group(
            *[
                Group(
                    *[person.copy() for _ in range(10)]
                ).arrange(DOWN).scale_to_fit_height(4) 
                for _ in range(10)
            ]
        ).arrange(RIGHT).scale_to_fit_width(7)
        self.add(campione1)
        self.wait()
        campione1[0].set_color(YELLOW)
        self.play(Circumscribe(campione1[0]),color=YELLOW)
        fpos=Tex("falsi positivi").set_z_index(5).set_color(YELLOW).add_background_rectangle(color=BLACK)
        arrow_fpos=Arrow(start=fpos,end=campione1[0][5])
        self.play(Create(arrow_fpos))
        self.play(Write(fpos))
        self.wait()
        campione1[2][1].set_color(RED)
        self.play(Circumscribe(campione1[2][1]),color=RED)
        positivo=Tex("positivo").set_z_index(5).set_color(RED).add_background_rectangle(color=BLACK)
        arrow_pos=Arrow(start=positivo,end=campione1[2][1])
        self.play(ReplacementTransform(arrow_fpos,arrow_pos))
        self.play(ReplacementTransform(fpos,positivo))
        campione2 = Group(
            *[person.copy() for i in range(11)]
        )
        campione2.set_color(YELLOW)
        campione2[0].set_color(RED)
        campione2.arrange_in_grid(rows=4).scale_to_fit_height(7)
        arr3=Arrow(start=ORIGIN,end=campione2[0])
        self.play(
            ReplacementTransform(arrow_pos,arr3),
            ReplacementTransform(campione1,campione2),
            )
        prob=MathTex("\dfrac{1}{11}").set_z_index(5).set_color(YELLOW).add_background_rectangle(color=BLACK)
        res=Text("0.09% non il 90%").set_z_index(5).set_color(YELLOW).add_background_rectangle(color=BLACK)
        self.play(
            FadeOut(arr3),
            ReplacementTransform(positivo,prob),
            )
        self.wait()
        self.play(ReplacementTransform(prob,res))
 
        self.wait()
