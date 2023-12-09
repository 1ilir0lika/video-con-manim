from manim import *
titolo=Tex("Intersezioni con gli assi").scale(2.3)
sotto_titolo=Tex("gli zeri di una funzione").scale(1.5)
autore=Text("Ilir Lika III B")
VGroup(titolo,sotto_titolo,autore).arrange(DOWN)
definizione=Text("DEFINIZIONE :")
plane=NumberPlane()
intro=Tex(r"""
               le intersezioni con l'asse dell'ascisse o 0 di una funzione sono 
               quei valori x per i quali la y é pari a 0,toccando l'asse
               """,
    tex_environment="{minipage}{25em}"
).scale_to_fit_width(14)
intro2=Tex(r"""
               le intersezioni con l'asse delle ordinate invece sono quei valori di y per i quali la x é pari a 0,toccando l'asse
               """,
    tex_environment="{minipage}{25em}"
).scale_to_fit_width(14)

VGroup(definizione,intro).arrange(DOWN)
come=Text("COME TROVARLO").scale(1.5)
esempio=Text("ESEMPIO").scale(1.5)
axes = Axes(axis_config={'tip_shape': StealthTip}).add_coordinates()
axes_labels = axes.get_axis_labels()
intera_graph = axes.plot(lambda x: 2*x+2, color=BLUE)
inter_dot = Dot([-1,0,0])
arrow = Arrow([2,2,0],inter_dot, buff=0)
inter_dot_text = Text('0 della funzione').next_to([2,2,0], UP).add_background_rectangle(color=BLACK)
#ne vanno fatte 2 perché a 0 si rompe tutto,chissa come mai
fratta_graph1 = axes.plot(lambda x: (1/(x+1)),x_range=(-5,-1.1),color=RED)
fratta_graph2 = axes.plot(lambda x: (1/(x+1)),x_range=(-0.9,5),color=RED)
inter_dot2 = Dot([0,1,0])
arrow2 = Arrow([2,2,0],inter_dot2, buff=0)
inter_dot2_text = Text('intersezione ascisse').next_to([2,2,0], UP).add_background_rectangle(color=BLACK)
intera_label = axes.get_graph_label(intera_graph, label="2x+1")
fratta_label = axes.get_graph_label(fratta_graph2, label=MathTex("\dfrac{1}{x+1}",color=RED))

class Zeri(Scene):
    def construct(self):
  
        sistema_ascisse=MathTex(r"""  
        \begin{cases}
            y &= 0 \\
            P(x) &= y 
        \end{cases}
        """
        )

        sistema_ascisse_sol=MathTex("P(x)=0")


        self.play(
            Write(titolo),
            FadeIn(sotto_titolo,shift=DOWN),
            FadeIn(autore,shift=DOWN),
        )
        self.wait(3)
        self.play(
            ReplacementTransform(sotto_titolo, intro),
            ReplacementTransform(titolo, definizione),
            FadeOut(autore),
        )
        self.wait(3)
        VGroup(come,sistema_ascisse).arrange(DOWN)
        self.play(
            ReplacementTransform(intro, sistema_ascisse),
            ReplacementTransform(definizione,come),
        )
        self.wait(3)
        self.play(ReplacementTransform(sistema_ascisse,sistema_ascisse_sol))
        self.wait(3)
        esempio.to_corner(UP + LEFT).scale(0.8)
        self.play(
            ReplacementTransform(come,esempio),
            ReplacementTransform(sistema_ascisse_sol,intera_graph),
            FadeIn(VGroup(axes,plane,intera_label,axes_labels))
            )
        self.wait(3)
        self.play(
            FadeIn(inter_dot,arrow,inter_dot_text)    
        )
        self.wait(3)
        self.play(
            FadeOut(VGroup(axes,plane,intera_label,axes_labels,inter_dot,arrow,inter_dot_text,intera_graph,esempio)),
            )
        self.wait(3)
class Zeri2(Scene):        
    def construct(self):    
        sistema_ordinate=MathTex(r"""  
        \begin{cases}
            x &= 0 \\
            P(x) &= y 
        \end{cases}
        """
        )

        sistema_ordinate_sol=MathTex("P(0)=y")
        self.play(
            FadeIn(VGroup(definizione.scale(1.5),intro2).arrange(DOWN))
        )
        self.wait(3)
        VGroup(come,sistema_ordinate).arrange(DOWN)
        self.play(
            FadeOut(VGroup(definizione)),
            ReplacementTransform(intro2,come),
            FadeIn(sistema_ordinate)
        )
        self.wait(3)

        self.play(ReplacementTransform(sistema_ordinate,sistema_ordinate_sol))
        self.wait(3)
        esempio.to_corner(UP + LEFT).scale(0.8)
        self.play(
            ReplacementTransform(come,esempio),
            FadeOut(sistema_ordinate_sol),
            FadeIn(VGroup(axes,plane,fratta_graph1,fratta_graph2,fratta_label,axes_labels))
        )
        self.wait(3)
        self.play(
            FadeIn(VGroup(inter_dot2,arrow2,inter_dot2_text))
        )
        self.wait(3)
