from manim import *

class Intro(Scene):
    def construct(self):
        title = Tex("il teorema di ", "Bayes").scale(3)
        sotto=Tex("Ilir Lika "," Istituto Maria Immacolata ")
        VGroup(title, sotto).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(sotto, shift=DOWN),
            )  
        self.wait()

        titolo2=Tex("Problema 1")
        titolo2.to_corner(UP + LEFT)
        prob=Tex(r"""
        supponiamo che un giorno ti svegli e stai male,
                 così vai dal medico,
                 dopo aver effettuate dei test ti dice che hai una malattia rara
                 che ha solamente l'\textbf{1\% della popolazione},
                 così chiedi al medico quanto sia certo che tu ce l'abbia,
                 lui risponde dicendo che il test identifica correttamente il \textbf{90\% dei casi}
                       """,
            tex_environment="{minipage}{25em}"
        ).scale_to_fit_width(10)

        quesito=Tex("Qual'è la probabilità che tu abbia questa malattia?")
        self.play(
        LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in sotto]),
        Transform(title, titolo2)
        )
        self.wait(1)
        self.play(Write(prob))
        self.wait(7)
        self.play(Transform(prob,quesito))
        self.wait()    
        #self.play(LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in quesito]))
