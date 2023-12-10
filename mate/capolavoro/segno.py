from manim import *
titolo=Tex("Segno di una funzione").scale(2.3)
autore=Text("Ilir Lika III B")
VGroup(titolo,autore).arrange(DOWN)
definizione=Text("DEFINIZIONE :").scale(2.3)
plane=NumberPlane()
titolo_definizione=Tex("Definizione").scale(1.5)
definizione=Tex(r"""
               il segno di una funzione é il segno che assume la y per ogni valore di x
               """,
    tex_environment="{minipage}{25em}"
).scale_to_fit_width(14)

VGroup(titolo_definizione,definizione).arrange(DOWN)
come=Text("COME TROVARLO").scale(1.5)
procedura=Tex(r"""
                per trovare il segno di una funzione é sufficiente risolvere la disequazione $P(x)>0$ 
                """,
    tex_environment="{minipage}{25em}"
).scale_to_fit_width(14)
esempio_titolo=Text("ESEMPIO").scale(1.5)
esempio=Tex(r"""   
                $P(x)=x^2-2x-3$
                """,
    tex_environment="{minipage}{25em}"
).scale_to_fit_width(14)
esempio_sol1=Tex(r"""
                $x^2-2x-3>0$
                """,
    tex_environment="{minipage}{25em}"
).scale_to_fit_width(8)
esempio_sol2=Tex(r"""
                Intersezioni \\
                $x=\frac{2 \pm \sqrt{4-4(-3)}}{2} \\
                x=3 \quad \vee \quad x=-1$
                """,
    tex_environment="{minipage}{25em}"
).scale_to_fit_width(8)
conclusione_titolo=Text("CONCLUSIONE").scale(1.5)
conclusione=Tex(r"""
                possiamo perció dedurre che sará positiva negli intervalli \\
                $x \in (-\infty;-1) \cup (3;+\infty)$
                """,
    tex_environment="{minipage}{25em}"
).scale_to_fit_width(14)
axes = Axes(axis_config={'tip_shape': StealthTip}).add_coordinates()
axes_labels = axes.get_axis_labels()
intera_graph = axes.plot(lambda x: 2*x+2, color=BLUE)
inter_dot = Dot([-1,0,0])
arrow = Arrow([2,2,0],inter_dot, buff=0)
inter_dot_text = Text('0 della funzione').next_to([2,2,0], UP).add_background_rectangle(color=BLACK)

class intro(Scene):
    def construct(self):
        self.play(
            Write(titolo),
            FadeIn(autore,shift=DOWN)
        )
        self.wait(3)
        self.play(
            FadeOut(autore),
            ReplacementTransform(titolo, titolo_definizione),
            FadeIn(definizione,shift=DOWN)
        )
        self.wait(3)
        VGroup(come,procedura).arrange(DOWN)
        self.play(
            ReplacementTransform(titolo_definizione,come),
            ReplacementTransform(definizione,procedura)
        )
        self.wait(3)
        VGroup(esempio_titolo,esempio_sol1).arrange(DOWN)
        VGroup(esempio_titolo,esempio_sol2).arrange(DOWN)
        self.play(
            ReplacementTransform(come,esempio_titolo),
            ReplacementTransform(procedura,esempio_sol1),
        )
        self.wait(3)
        self.play(
            ReplacementTransform(esempio_sol1,esempio_sol2),
        )
        self.wait(3)
        VGroup(conclusione_titolo,conclusione).arrange(DOWN)
        self.play(
            ReplacementTransform(esempio_sol2,conclusione),
            ReplacementTransform(esempio_titolo,conclusione_titolo)
        )
        self.wait(3)
        self.play(
            FadeOut(conclusione),
            FadeOut(conclusione_titolo)
        )
        self.wait(3)
class visivo(Scene):        
    def construct(self):    
        intro=Tex(r"""
                vediamolo adeso da un punto di vista grafico
                """,
                tex_environment="{minipage}{25em}"
        ).scale_to_fit_width(20)
        self.play(
            FadeIn(intro,shift=DOWN)
        )
        self.wait(3)
        axes = Axes(axis_config={'tip_shape': StealthTip}).add_coordinates()
        axes_labels = axes.get_axis_labels()

#class negativi(Scene):
    #def construct(self):
