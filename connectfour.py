import turtle
import time


screen = turtle.Screen() # screen vil si vinduet med applikasjonen, mange bruker derfer "window" isteden for "screen"
screen.bgcolor("red") # forandrer bakgrunns-fargen


pen = turtle.Turtle() # pen er kort forklart det som tegner alt på applikasjonen, derfor kalles den pen
pointer = turtle.Turtle()
pointer.hideturtle()
pointer._tracer(0,0)
pointer.penup()
pen.hideturtle() # gjemmer pen slik at du ikke ser en stygg pil tegne alt
pen._tracer(0,0) # _tracer() funksjonen bestemmer hastigheten på hvordan ting blir tegnet
# når _tracer er (0,0) så er der ingen animasjon på det, altså at alt skjer på ett og ikke gradvis

turtle.setup(500, 500) # forandrer skjermstørrelsen slik den ish passer brettet

# connect4 blir senere brukt i draw_grid() som grid
# det connect4 bestemmer er hvor mange rader nedover (6) der er og hvor mange rader bortover (7) der er ved bruk av looping
connect4 = [[0 for c in range(7)] for x in range(6)]

def draw_grid(grid): # draw_grid() tegner brettet og konfigurerer det
    pen.goto(-185, 130) # beveger pen til coordinatene slik at brettet blir stilt mer til midten
    
    # hele denne løkken her lager og konfigurerer sirklene i brettet
    # for hver gang du velger en spiller tar sitt trekk så tegnes hele greien på nytt
    for rower in range(0, 6): # fra første sirkel nedover til siste sirkel nedover
        for col in range(0, 7): # fra første sirkel bortover til siste sirkel bortover
            if grid[rower][col] == 0: # sjekker om verdien til sirkelen er 0 som definert i connect4: "0 for c..."
                pen.fillcolor("white") # farger sirklene som ikke er brikke i hvite
            elif grid[rower][col] == 2: # om verdien 0 i connect4 blir 2 så farges den valgte sirkelen rød
                pen.fillcolor("red") # bestemmer rød-fargen for rød spiller
            elif grid[rower][col] == 1:# om verdien 0 i connect4 blir 1 så farges den valgte sirkelen gul
                pen.fillcolor("yellow") # bestemmer gul-fargen for rød spiller

            # tegner sirklene
            pen.begin_fill()
            pen.circle(28)
            pen.end_fill()
            # begin_fill fyller hele området i innsiden av formen du lager, som i dette tilfelle en sirkel
            # end_fill stopper fyllingen av området

            # beveger pen slik at sirklene har god avstand mellom hverandre
            pen.penup() 
            pen.forward(58)
            pen.pendown()
            # penup betyr at man tar pen opp fra arket, altså at du ikke tegner, og pendown det motsatte

            
        pen.setheading(270) # forandrer retningen til pen slik at sirklene ikke blir skeive
        pen.penup()
        # mye tegning for god plassering av sirkler
        pen.forward(58)
        pen.setheading(180)
        pen.forward(58 * 7)
        pen.setheading(0)
        
        pen.getscreen().update() # oppdaterer tegnebrettet bare i tilfelle det skulle trenges, den har fungert helt fint uten denne

# tegner brettet, altså det grid ligger på
# forskjell på grid og brett er det at grid er sirklene, brettet er bare en grå bakgrunn
def draw_board():
    pen.up()
    pen.setheading(0)
    pen.goto(-220, -200)
    pen.begin_fill()
    for b in range(4):
        pen.color("skyblue")
        pen.pendown()
        pen.forward(420)
        pen.left(90)
    pen.up()
    pen.end_fill()

# check_if_winner gjør som navnet sier, den sjekker hver gang noen har spilt turen sin om der er noen som har fått 4 på rad enten diagonalt, vertikalt eller horizontalt
def check_if_winner(grid, color):
    # Vertikal sjekk
    for r in range(6): # looper gjennom alle vertikale sirkler
        for c in range(4): 
            if grid[r][c] == color and grid[r][c+1] == color and grid[r][c+2] == color and grid[r][c+3] == color: # sjekker om 4 verdier på rad i r (row) og c (column) er samme farge
                return color # returnerer fargen dersom det er samme fargen på alle sirklene
    # Horizontal sjekk
    for x in range(3): # looper x aksen
        for y in range(7): # looper y aksen
            if grid[x][y] == color and grid[x+1][y] == color and grid[x+2][y] == color and grid[x+3][y] == color: # samme greien som forrige bare horiontal
                return color # returnerer fargen dersom det er samme fargen på alle sirklene
    # Diagonalt sjekk
    for i in range(3): # looper rader
        for z in range(4): # looper kolonner
            if grid[i][z] == color and grid[i+1][z+1] == color and grid[i+2][z+2] == color and grid[i+3][z+3] == color: # sjekker om kolonnene og radene går diagonalt med samme farge
                return color # returnerer fargen dersom det er samme fargen på alle sirklene
    # Diagonalt igjen siden du kan gå dianoalt fra venste til høyre eller høyre til venstre, så to forskjellige retninger
    for d in range(5, 2, -1): # looper rader men andre veien
        for c in range(4): # looper kolonner men andre veien
            if grid[d][c] == color and grid[d-1][c+1] == color and grid[d-2][c+2] == color and grid[d-3][c+3] == color: # samme som forrige bare -+ istedenfor ++ (aka motsatt)
                return color # returnerer fargen dersom det er samme fargen på alle sirklene

    return 0 # returnerer 0 om ingen av loopene returneres, altså at ingen har vunnet så er check_if_winner() = 0

def display_winner(winners): # funksjon som kjøres når en vinner er deklarert
    if winners == 2: # om check_if_winner() er 2 så vinner rød
        pen.penup()
        pen.color("black")
        pen.goto(-10, -10)
        pen.write("RED WINS", True, align="center", font=("Comic sans MS", 60, "bold"))
        pen.getscreen().update()
        return True
    elif winners == 1: # om check_if_winner() er 1 så vinner gul
        pen.penup()
        pen.color("black")
        pen.goto(-10, -10)
        pen.write("YELLOW WINS", True, align="center", font=("Comic sans MS", 50, "bold"))
        pen.getscreen().update()
        return True

def click_coord(i, j):
    pointer.goto(i,j)
    print(pointer.xcor())

click = False

def on_click(i,j):
    global click
    click = True
    pointer.goto(i,j)

turtle.onscreenclick(on_click)
turtle.hideturtle()

def waitforclick():
    global click

    turtle.update()
    click = False

    while not click:
        turtle.update()
        time.sleep(.1)
    
    click = False

def get_mouse_click_coor(x, y):
    print(x,y)
    return x

def loop():
    for player_turn in range(1, 43):        

        waitforclick()
        turtle.onclick(on_click)
        x = pointer.xcor()

        if x == -10000:
            column = 0
        elif x <= -155 and x > -1000:
            print("section 1")
            column = 1
        elif x >= -156 and x <= -98:
            print("section 2")
            column = 2
        elif x >= -99 and x <= -40:
            print("section 3")
            column = 3
        elif x >= -39 and x <= 19:
            print("section 4")
            column = 4
        elif x >= 18 and x <= 77:
            print("section 5")
            column = 5
        elif x >= 78 and x <= 134:
            print("section 6")
            column = 6
        elif x >= 135:
            print("section 7")
            column = 7

        column_minus = column - 1
        while connect4[0][column_minus] != 0:
            # full kolonne, velg en annen en
            waitforclick()
            turtle.onclick(on_click)
            x = pointer.xcor()

            if x == -10000:
                column = 0
            elif x <= -155 and x > -1000:
                print("section 1")
                column = 1
            elif x >= -156 and x <= -98:
                print("section 2")
                column = 2
            elif x >= -99 and x <= -40:
                print("section 3")
                column = 3
            elif x >= -39 and x <= 19:
                print("section 4")
                column = 4
            elif x >= 18 and x <= 77:
                print("section 5")
                column = 5
            elif x >= 78 and x <= 134:
                print("section 6")
                column = 6
            elif x >= 135:
                print("section 7")
                column = 7
            column_minus = column - 1
        
        
        # stable sirklene på hverandre
        row = 5
        while connect4[row][column_minus] != 0:
            row = row - 1
        # finne ut fargen til den nåværende spilleren
        playerColor = int((player_turn % 2) + 1)
        if playerColor == 2:
            screen.bgcolor("yellow")
        elif playerColor == 1:
            screen.bgcolor("red")
        # plassere sirkelen i grid
        connect4[row][column_minus] = playerColor
        # tegne grid
        winner = check_if_winner(connect4, playerColor)
        draw_grid(connect4)
        if display_winner(winner):
            user_input = screen.textinput("Exit", "Type 'quit' to exit the game")
            while True:
                if user_input == 'quit':
                    print("Game has been exited!")
                    break
                else:
                    user_input = screen.textinput("Exit", "Type 'quit' to exit the game")
            break
        draw_grid(connect4)


draw_board()
draw_grid(connect4)
loop()