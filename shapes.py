import pgzrun



WIDTH=500
HEIGTH=500
TITLE="SHAPES"


r=100
g=200
b=241

def draw():
    rectangle = Rect(100,100,150,150)
    screen.fill((r,g,b))
    #screen.draw.filled_circle(rectangle,("red"))
    screen.draw.filled_circle((300,300),70,"black")


pgzrun.go()