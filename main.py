from turtle import Turtle, Screen
from zmija import Zmija
import time
from hrana import Hrana
from poeni import Poeni

screen = Screen()
screen.setup(500, 500)
screen.title("Moja zmija")
screen.bgcolor("blue")
screen.tracer(0)

zmija = Zmija()
hrana = Hrana()
poeni = Poeni()

screen.listen()
screen.onkey(zmija.zmija_gore, "Up")
screen.onkey(zmija.zmija_dole, "Down")
screen.onkey(zmija.zmija_levo, "Left")
screen.onkey(zmija.zmija_desno, "Right")


igra_ide = True


while igra_ide:
    screen.update()
    time.sleep(0.1)
    zmija.zmija_ide()

    if zmija.glava.distance(hrana) < 15:
        hrana.osvezi()
        zmija.produzi_zmiju()
        poeni.povecaj_poene()

    if zmija.glava.xcor() > 240 or zmija.glava.xcor() < -240 or zmija.glava.ycor() > 240 or zmija.glava.ycor() < -240:
        igra_ide = False
        poeni.kraj_igre()

    for segment in zmija.segmenti[1:]:
        if zmija.glava.distance(segment) < 10:
            igra_ide = False
            poeni.kraj_igre()



screen.exitonclick()
