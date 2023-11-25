from manim import *

class intro(Scene):
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

class risoluzione(Scene):
    def construct(self):
        titolo=Tex("Problema 1")
        titolo.to_corner(UP + LEFT)
        self.add(titolo)
        person =  SVGMobject(r"immagini/person.svg").set_color(GREEN)
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
        self.wait()
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
        sfida = Tex("Sfida").scale(3)
        sotto=Tex(r"""
                       provate a verificare la probabilità quando vengono effettuati 2 test
                       """
                       ,tex_environment="{minipage}{25em}"
                       )
        VGroup(sfida, sotto).arrange(DOWN)
        self.play(ReplacementTransform(prob,res))
        self.wait(0.3)
        self.play(FadeOut(Group(res,campione2,prob)))
        self.wait(1)
        self.play(
            Write(sfida),
            FadeIn(sotto, shift=DOWN)
            )
        self.wait(1)

class intro2(Scene):
    def construct(self):
        titolo=Tex("Problema 1")
        titolo.to_corner(UP + LEFT)
        self.add(titolo)
        titolo2=Tex("Problema 2")
        titolo2.to_corner(UP+LEFT)
        self.play(Transform(titolo,titolo2))
        context=Tex(r"""
                    questo problema è stato preso dal libro "pensieri lenti e veloci" scritto da  Daniel Kahneman
                    """,
                    tex_environment="{minipage}{25em}"
                    ).scale_to_fit_width(10)
        libro=ImageMobject(r"immagini/thinking.jpg").scale_to_fit_height(5)
        Group(context,libro).arrange(DOWN)
        self.play(
            FadeIn(libro),
            Write(context),
            )
        self.wait()
        prob=Tex(r"""
            Steve è molto timido e chiuso. Sempre
            disponibile, ha però scarso interesse per le persone o il mondo della
            realtà. Anima mite e ordinata, ha bisogno di ordine e struttura, e una
            passione per il dettaglio .
                       """,
            tex_environment="{minipage}{25em}"
        ).scale_to_fit_width(10)
        quesito=Tex("È più probabile che Steve sia un libraio o un contadino?")

        self.wait()
        self.play(
            FadeOut(libro),
            ReplacementTransform(context,prob),
            )
        self.wait(5)
        self.play(ReplacementTransform(prob,quesito))
        self.wait()

class risoluzione2(Scene):
    def construct(self):
        titolo2=Tex("Problema 2")
        titolo2.to_corner(UP+LEFT)
        self.add(titolo2)
        farmer=SVGMobject(r"immagini/farmer.svg").set_color(YELLOW_C)
        librarian=SVGMobject(r"immagini/librarian.svg").set_color(LIGHT_BROWN)
        num_librarians_per_row = 1
        num_farmers_per_row = 20
        num_rows = 7
        row = VGroup(
            *[librarian.copy() for _ in range(num_librarians_per_row)],
            *[farmer.copy() for _ in range(num_farmers_per_row)]
        ).arrange(RIGHT).scale_to_fit_width(10)
        people=VGroup(*[row.copy() for _ in range(num_rows)]).arrange(DOWN)
        contesto=Tex(r"""
                   Bisogna sapere che quand'è stato scritto il libro il rapporto tra i contadini ed i librai era di 1:20
                    """,
                    tex_environment="{minipage}{25em}"
                    ).scale_to_fit_width(10)
        self.play(Write(contesto))
        self.wait()
        self.play(ReplacementTransform(contesto,people))
        self.wait()
        #mettiamo che questi rapporti siano veri,overo che
        supposizione=Text("rispettano queste caratteristiche: \n il 60% dei librai \n il 10% dei contadini").add_background_rectangle(color=BLACK)
        self.play(Write(supposizione))
        self.wait()
        self.play(FadeOut(supposizione))
        self.wait()

class formula(Scene):
    def construct(self):

        self.wait()
