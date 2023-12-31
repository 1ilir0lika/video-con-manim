from manim import *
from numpy import sqrt

class Funzioni(Scene):
    def construct(self):
        titolo=Tex("Il dominio ","di una funzione").scale(2.5)
        autore=Text("Ilir Lika III B")
        VGroup(titolo,autore).arrange(DOWN)
        intro_intere=Tex(r"""
                        Il dominio per le funzioni algebriche \\
                        intere coincide sempre con
                       """,
            tex_environment="{minipage}{25em}"
        ).scale_to_fit_width(14)
        intro_fratte=Tex(r"""
                        Il dominio per le funzioni algebriche \\
                        fratte coincide sempre con
                       """,
            tex_environment="{minipage}{25em}"
        ).scale_to_fit_width(14)
        intro_irrazionali=Tex(r"""
                        Il dominio per le funzioni irrazionali \\
                        fratte coincide sempre con
                       """,
            tex_environment="{minipage}{25em}"
        ).scale_to_fit_width(14)
        #dettagli_fratte=Tex(r"""
        #                dove x é quel valore tale da rendere il denominatore pari a 0,ovvero la condizione d'esistenza
        #               """,
        #    tex_environment="{minipage}{25em}"
        #).scale_to_fit_width(10)
        dettagli_fratte=MathTex('x|dividendo = 0').scale_to_fit_width(10)
        dettagli_irrazionali=MathTex('x|radicando < 0').scale_to_fit_width(10)

        dominio_intere=MathTex("\mathbb{R}").scale(5)
        dominio_fratte=MathTex("\mathbb{R}-\{x\}").scale(5)
        dominio_irrazionali=MathTex("\mathbb{R}-\{x\}").scale(5)
        esempio=Text("ESEMPIO").to_corner(UP + LEFT)
        VGroup(intro_intere, dominio_intere).arrange(DOWN)
        VGroup(intro_fratte, dominio_fratte,dettagli_fratte).arrange(DOWN)
        VGroup(intro_irrazionali, dominio_irrazionali,dettagli_irrazionali).arrange(DOWN)
        axes = Axes(axis_config={'tip_shape': StealthTip}).add_coordinates()
        axes_labels = axes.get_axis_labels()

        intera_graph = axes.plot(lambda x: 2*x+2, color=BLUE)
        #ne vanno fatte 2 perché a 0 si rompe tutto,chissa come mai
        fratta_graph1 = axes.plot(lambda x: (1/x)+1,x_range=(-5,-0.1),color=RED)
        fratta_graph2 = axes.plot(lambda x: (1/x)+1,x_range=(0.1,5),color=RED)
        irrazionale_graph=axes.plot(lambda x: sqrt(x)+2,x_range=(0,5),color=YELLOW)

        intera_label = axes.get_graph_label(intera_graph, label="2x+1")
        fratta_label = axes.get_graph_label(fratta_graph2, label=MathTex("\dfrac{1}{x}+1",color=RED))
        irrazionale_label = axes.get_graph_label(irrazionale_graph, label=MathTex("\sqrt{x}+2",color=YELLOW))

        risposta_intere=Tex("ogni x ha una y").scale(3).add_background_rectangle(color=BLACK)
        risposta_fratte=Tex("ogni x ha una y,tranne 0").scale(2).add_background_rectangle(color=BLACK)
        risposta_irrazionali1=Tex("ogni x ha una y,tranne per").add_background_rectangle(color=BLACK)
        #risposta_irrazionali2=MathTex("\[-\inf,0\]")
        risposta_irrazionali2=MathTex("\left] -\infty,0 [").add_background_rectangle(color=BLACK)
        VGroup(risposta_irrazionali1,risposta_irrazionali2).scale(1.5).add_background_rectangle(color=BLACK).arrange(DOWN)

        self.play(
            Write(titolo),
            FadeIn(autore,shift=DOWN),
        )
        self.wait(3)
        self.play(
            ReplacementTransform(titolo, intro_intere),
            ReplacementTransform(autore,dominio_intere),
        )
        self.wait(5)
        self.play(ReplacementTransform(dominio_intere,esempio),FadeOut(intro_intere))
        self.wait()
        self.add(axes)
        self.play(Write(intera_graph))
        self.wait()
        self.play(Write(intera_label))
        self.wait()
        self.add(risposta_intere)
        self.wait()
        self.play(FadeOut(risposta_intere,intera_graph,intera_label,axes,esempio))
        self.wait()
        self.play(
            Write(intro_fratte),
            FadeIn(dominio_fratte,shift=DOWN),
            Write(dettagli_fratte)
            )
        self.wait(5)
        self.play(ReplacementTransform(dominio_fratte,esempio),FadeOut(intro_fratte,dettagli_fratte))
        self.wait()
        self.add(axes)
        self.play(Write(VGroup(fratta_graph1,fratta_graph2)))
        self.wait()
        self.play(Write(fratta_label))
        self.wait()
        self.play(Write(risposta_fratte))
        self.wait()
        self.play(FadeOut(risposta_fratte,fratta_graph1,fratta_graph2,fratta_label,axes,esempio))
        self.wait()

        self.play(
            Write(intro_irrazionali),
            FadeIn(dominio_irrazionali,shift=DOWN),
            Write(dettagli_irrazionali)
            )
        self.wait(5)
        self.play(ReplacementTransform(dominio_irrazionali,esempio),FadeOut(intro_irrazionali,dettagli_irrazionali))
        self.wait()
        self.add(axes)
        self.play(Write(irrazionale_graph))
        self.wait()
        self.play(Write(irrazionale_label))
        self.wait()
        self.play(
            Write(risposta_irrazionali1),
            FadeIn(risposta_irrazionali2,shift=DOWN)
        )
        self.wait()
        self.play(FadeOut(irrazionale_graph,irrazionale_label,esempio,risposta_irrazionali1,risposta_irrazionali2))
        self.wait(3)

        self.play(Write(Text("ecco le funzioni a confronto").to_corner(UP)))
        self.wait()
        self.play(Write(VGroup(intera_graph,intera_label.add_background_rectangle())))
        self.wait()
        self.play(Write(VGroup(fratta_graph1,fratta_graph2,fratta_label)))
        self.wait()
        self.play(Write(VGroup(irrazionale_graph,irrazionale_label)))
        self.wait()
