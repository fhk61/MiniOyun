import turtle
import math
import random
import winsound

hakan = turtle.Screen()
hakan.title("Şehir Savunmaya Hoşgeldiniz")
hakan.bgcolor("black")
hakan.bgpic("space_station_defense_game_background.gif")
hakan.tracer(0)

player_vertices = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
hakan.register_shape("player", player_vertices)

dooku_vertices = ((0, 10), (5, 7), (3,3), (10,0), (7, 4), (8, -6), (0, -10), (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
hakan.register_shape("dooku", dooku_vertices)

class silah(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()

def get_heading_to(a,b):
    x1 = a.xcor()
    y1 = a.ycor()
    
    x2 = b.xcor()
    y2 = b.ycor()
    
    heading = math.atan2(y1-y2, x1-x2)
    heading = heading * 180.00 / 3.14159
    return heading       
        
player = silah()
player.color("white")
player.shape("player")
player.speed(0)
player.score = 0

missile = silah()
missile.color("blue")
missile.shape("arrow")
missile.speed = 1.5
missile.state = "ready"
missile.hideturtle()

pen = silah()
pen.hideturtle()
pen.color("white")
pen.goto(0,200)
pen.write("Score: 0", False, align = "center", font = ("Arial", 24, "normal"))



asteroids = []
colors = ["red" , "yellow"  , "purple","green"]
for i in range(4):
    
    dooku = silah()
    color = random.choice(colors)
    dooku.color(color)
    dooku.shape("dooku")
    
    dooku.speed = random.randint(4,6) / 45
    dooku.goto(0,0)
    heading = random.randint(0,360)
    distance = random.randint(300,400)
    dooku.setheading(heading)
    dooku.fd(distance)
    dooku.setheading(get_heading_to(player,dooku))
    asteroids.append(dooku)
    
def rotate_right():
    player.rt(10)
    
def rotate_left():    
    player.lt(10)

def fire_missile():
    if missile.state == "ready":
        winsound.PlaySound("3540.wav", winsound.SND_ASYNC)
        missile.goto(0,0)
        missile.showturtle()
        missile.setheading(player.heading())
        missile.state = "fire"




hakan.listen()
hakan.onkey(rotate_right, "Right")
hakan.onkey(rotate_left, "Left")
hakan.onkey(fire_missile, "space")



while True:
    
    for dooku in asteroids:
        hakan.update()
        player.goto (0, 0)
        
        if missile.state == "fire":
            missile.fd(missile.speed)
        
        if missile.xcor()<-400 or missile.xcor() > 400 or missile.ycor() > 400 or missile.ycor() < -400:
            missile.hideturtle()
            missile.state = "ready"
        
        
        dooku.fd(dooku.speed)
            
        
        if dooku.distance(missile) < 20:
            winsound.PlaySound("Explosion+1.wav", winsound.SND_ASYNC)
            heading = random.randint(0,360)
            distance = random.randint(400,500)
            dooku.setheading(heading)
            dooku.fd(distance)
            dooku.setheading(get_heading_to(player,dooku))
            missile.goto(1000,1000)
            missile.hideturtle()
            missile.state = "ready"
            dooku.speed += 0.03
            
            # Puanı Arttırma
            player.score += 10
            pen.clear()
            pen.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))
       
       
        if dooku.distance(player) < 20:
            # Reset Asteroid
            heading = random.randint(0, 360)
            distance = random.randint(500, 600)
            dooku.setheading(heading)
            dooku.fd(distance)
            dooku.setheading(get_heading_to(player, dooku))
            dooku.speed += 0.01
            print("Player killed!")
            
            # Puanı azaltma
            player.score -= 50
            pen.clear()
            pen.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))


       
       
       
    
hakan.mainloop()




