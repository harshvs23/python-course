import pgzrun
music.play('bgm1')
music.set_volume(0.3)


b= Actor('ball',(50,50))
vx,vy = 3,3

def draw():
    screen.fill('white')
    b.draw()

def update():
    global vx,vy
    b.x += vx
    b.y += vy
    if b.right> 800 or b.left < 0:
        vx = -vx
        sounds.s1.play()
    if b.bottom> 600 or b.top < 0:
        vy = -vy
        sounds.s1.play()
pgzrun.go()
