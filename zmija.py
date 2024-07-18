from turtle import Turtle

POCETNE_POZICIJE = [(10, 0), (20, 0), (30, 0)]
ZMIJA_GORE = 90
ZMIJA_DOLE = 270
ZMIJA_LEVO = 180
ZMIJA_DESNO = 0

class Zmija:
    def __init__(self):
        self.segmenti = []
        self.napravi_zmiju()
        self.glava = self.segmenti[0]

    def napravi_zmiju(self):
        for pozicija in POCETNE_POZICIJE:
            self.dodaj_segment(pozicija)

    def dodaj_segment(self, pozicija):
        novi_segment = Turtle()
        novi_segment.shape("square")
        novi_segment.color("white")
        novi_segment.penup()
        novi_segment.goto(pozicija)
        self.segmenti.append(novi_segment)

    def produzi_zmiju(self):
        self.dodaj_segment(self.segmenti[-1].position())

    def zmija_ide(self):
        for broj_segmenta in range(len(self.segmenti)-1, 0, -1):
            novi_x = self.segmenti[broj_segmenta - 1].xcor()
            novi_y = self.segmenti[broj_segmenta - 1].ycor()
            self.segmenti[broj_segmenta].goto(novi_x, novi_y)
        self.glava.forward(20)

    def zmija_gore(self):
        if self.glava.heading() != ZMIJA_DOLE:
            self.glava.setheading(ZMIJA_GORE)

    def zmija_dole(self):
        if self.glava.heading() != ZMIJA_GORE:
            self.glava.setheading(ZMIJA_DOLE)

    def zmija_levo(self):
        if self.glava.heading() != ZMIJA_DESNO:
            self.glava.setheading(ZMIJA_LEVO)

    def zmija_desno(self):
        if self.glava.heading() != ZMIJA_LEVO:
            self.glava.setheading(ZMIJA_DESNO)