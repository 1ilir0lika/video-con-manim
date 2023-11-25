from manim import *

class BooleanOperations(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        insiemi=["interi","razionali","irrazionali","trascendenti","computabili","reali","immaginari","complessi"]
        esempi=["-3","\dfrac{3}{2}","\sqrt{2}","\pi","\pi","e","\sqrt{-1}","\pi+2i"]
        ellipse1 = Ellipse(
            width=4.0, height=2.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        )
        title=Text("naturali")
        esempio=Text("1")
        esempio2=MathTex("-3")
        gruppo=VGroup(title,ellipse1,esempio2).arrange(UP)
        self.play(Write(title))
        self.play(Write(ellipse1))
        self.play(Write(esempio))
        self.wait()
        self.play(Write(esempio2))
        self.wait()
        for i in range(len(insiemi)-1):
            ellipse1 = Ellipse(
            width=i*2.3+7.0, height=i*2.5+4.0, fill_opacity=0.5-0.08*i, color=BLUE, stroke_width=10
            )
            title=Text(insiemi[i])
            esempio2=MathTex(esempi[i+1])
            gruppo=VGroup(title,ellipse1,esempio2).arrange(UP)
            self.play(Write(VGroup(title,ellipse1)))
            self.wait()
            self.play(Write(esempio2))
            self.play(self.camera.frame.animate.scale(1.3-0.05*i))
            self.wait()
        
        i=len(insiemi)-1
        complessi = Ellipse(
            width=i*2.3+7.0, height=i*2.5+4.0, fill_opacity=0.5-0.05*i, color=BLUE, stroke_width=10
        )
        title=Text(insiemi[i])
        gruppo=VGroup(title,complessi).arrange(UP)
        self.play(Write(VGroup(title,complessi)))
        self.wait()

