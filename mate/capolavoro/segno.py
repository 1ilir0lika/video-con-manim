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
                vediamolo adesso da un punto di vista grafico
                """,
                tex_environment="{minipage}{25em}"
        ).scale_to_fit_width(14)
        self.play(
            FadeIn(intro,shift=DOWN)
        )
        self.wait(3)
        self.play(
            FadeOut(intro)
        )
        #definisci la funzione di prima
        funzione = lambda x: x**2-2*x-3
        #disegna la funzione
        graph = axes.plot(funzione, color=DARK_BLUE)
        #indica con 2 punti e 2 label le intersezioni con l'asse trovate prima
        intersezioni=VGroup(
            Dot([-1,0,0]),
            Dot([3,0,0]),
            Tex(r"$x=-1$").next_to([-1,0,0],DOWN).add_background_rectangle(color=BLACK),
            Tex(r"$x=3$").next_to([3,0,0],DOWN).add_background_rectangle(color=BLACK)
        )
        #disegna la funzione
        self.play(
            FadeIn(VGroup(axes,axes_labels)),
            Write(graph),
            Write(axes_labels),
        )
        self.wait(3)
        self.play(
            Write(intersezioni)
        )
        self.wait(3)
        #colora l'area negativa
        area_negativa=axes.get_area(graph,x_range=(-1,3), color=RED)
        self.play(
            Write(area_negativa)
        )
        self.wait(3)
        #colora l'area positiva
        area_positiva1=axes.get_area(graph,x_range=(3,6), color=GREEN)
        area_positiva2=axes.get_area(graph,x_range=(-7,-1), color=GREEN)
        self.play(
            Write(VGroup(area_positiva1,area_positiva2))
        )
        self.wait(3)
        self.play(
            FadeOut(VGroup(area_negativa,area_positiva1,area_positiva2,graph,intersezioni,axes,axes_labels))
        )
        self.wait(3)
