import pgzrun



WIDTH=800
HEIGHT=800
TITLE="SHAPES"


r=100
g=200
b=241

def draw():
    rectangle = Rect(100,100,150,150)
    screen.fill((r,g,b))
    screen.draw.filled_rect(rectangle,("green"))
    screen.draw.circle((300,300),70,"black")
    square = Rect (120,300,100,100)
    screen.draw.filled_rect(square,("yellow"))
    screen.draw.line((400,0,),(400,400), ("black"))

pgzrun.go()
