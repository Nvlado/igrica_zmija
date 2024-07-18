from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"

class Poeni(Turtle):
    def __init__(self):
        super().__init__()
        self.poeni = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.azuriraj_poene()
        self.ispisi_ime()

    def ispisi_ime(self):
        self.goto(-25, 200)
        self.write(f"Napravio Vladimir Nimčević", align="right", font=8)


    def azuriraj_poene(self):
        self.goto(150, 200)
        self.write(f"Poeni: {self.poeni}", align=ALIGNMENT, font=FONT)


    def kraj_igre(self):
        self.goto(0, 0)
        self.write(f"KRAJ IGRE", align=ALIGNMENT, font=FONT)

    def povecaj_poene(self):
        self.poeni += 1
        self.clear()
        self.azuriraj_poene()
        self.ispisi_ime()
