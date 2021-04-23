import turtle

colours = ["#91576e", "#58b09d", "#93d65c", "#e0ae82", "#e88079"]

for i in range(5):
    for j in range(5):
        turtle.fillcolor(colours[j])
        turtle.begin_fill()
        turtle.circle(70)
        turtle.end_fill()
        turtle.right(30)
        
turtle.bye()