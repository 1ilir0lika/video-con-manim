from manim import *
from numpy import sqrt,sin

class Funzioni(Scene):
    def construct(self):
        titolo=Tex("Intersezioni con gli assi").scale(1.5)
        sotto_titolo=Tex("gli zeri di una funzione").scale(1.5)
        autore=Text("Ilir Lika III B")
        VGroup(titolo,sotto_titolo,autore).arrange(DOWN)
        intro_intere=Tex(r"""
                       le intersezioni con gli assi o 0 di una funzione sono 
                       quei valori x per i quali la y é pari a 0,toccando l'asse ascisse
                       """,
            tex_environment="{minipage}{25em}"
        ).scale_to_fit_width(14)
        axes = Axes(axis_config={'tip_shape': StealthTip}).add_coordinates()
        axes_labels = axes.get_axis_labels()
        
        rand_graph = axes.plot(lambda x: 2*x+2^(x-sin(x)), color=BLUE)
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
        risposta_irrazionali2=MathTex("\left] -\infty,0 \left]").add_background_rectangle(color=BLACK)
        VGroup(risposta_irrazionali1,risposta_irrazionali2).scale(1.5).add_background_rectangle(color=BLACK).arrange(DOWN)

        self.play(
            Write(titolo),
            FadeIn(autore,shift=DOWN),
        )
        self.wait(3)
        self.play(
            Transform(titolo, intro_intere),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in autore]),
            FadeIn(dominio_intere,shift=DOWN),
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
        
