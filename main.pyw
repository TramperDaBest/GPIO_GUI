try:
    import pygame
except:
    import os
    os.system('pip install pygame')
    import pygame
try:
    exec("from gpiozero import LED")
except:
    import os
    os.system('pip install gpiozero')
    exec("from gpiozero import LED")
d={}
pygame.init()
f_size=13
try:
    font=pygame.font.SysFont('freesans',f_size)
    text = font.render('GPIO', True, 'white')
except:
    try:
        font=pygame.font.SysFont(None,f_size)
    except:
        font=pygame.font.SysFont(pygame.font.get_fonts()[0])
SCREEN_WIDTH = 69
SCREEN_HEIGHT = 700-36
pinout=['3.3V','5V','GPIO','5V','GPIO','GND','GPIO','GPIO','GND','GPIO','GPIO','GPIO','GPIO', 'GND', 'GPIO', 'GPIO', '3.3V', 'GPIO', 'GPIO', 'GND', 'GPIO', 'GPIO', 'GPIO', 'GPIO', 'GND', 'GPIO', 'GPIO', 'GPIO', 'GPIO', 'GND', 'GPIO', 'GPIO', 'GPIO', 'GND', 'GPIO', 'GPIO', 'GPIO', 'GPIO', 'GND', 'GPIO']
gpio_off=(52, 50, 119)
gpio_on=(109, 50, 245)
class G1(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback, args,color):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
        self.args=args
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback(self.args,self)
def on_click(bcmn, thing):
    if bcmn:
        if d.__contains__(bcmn):
            if d[bcmn]:
                d[bcmn]=False
                thing.image.fill(gpio_off)
                exec(f"l{bcmn}.off()")
            else:
                d[bcmn]=True
                thing.image.fill(gpio_on)
                exec(f"l{bcmn}.on()")
        else:
            d[bcmn]=True
            thing.image.fill(gpio_on)
            exec(f"l{bcmn}=LED(bcmn)")
            exec(f"l{bcmn}.on()")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p1=G1(pygame.Surface((30, 30)), 3, 3, on_click,False,(41, 108, 50))        
p2=G1(pygame.Surface((30, 30)), 36, 3, on_click,False,(241, 50, 50))       
p3=G1(pygame.Surface((30, 30)), 3, 36, on_click,2,(52, 50, 119))
p4=G1(pygame.Surface((30, 30)), 36, 36, on_click,False,(241, 50, 50))      
p5=G1(pygame.Surface((30, 30)), 3, 69, on_click,3,(52, 50, 119))
p6=G1(pygame.Surface((30, 30)), 36, 69, on_click,False,(52, 50, 50))       
p7=G1(pygame.Surface((30, 30)), 3, 102, on_click,4,(52, 50, 119))
p8=G1(pygame.Surface((30, 30)), 36, 102, on_click,14,(52, 50, 119))        
p9=G1(pygame.Surface((30, 30)), 3, 135, on_click,False,(52, 50, 50))       
p10=G1(pygame.Surface((30, 30)), 36, 135, on_click,15,(52, 50, 119))       
p11=G1(pygame.Surface((30, 30)), 3, 168, on_click,17,(52, 50, 119))        
p12=G1(pygame.Surface((30, 30)), 36, 168, on_click,18,(52, 50, 119))       
p13=G1(pygame.Surface((30, 30)), 3, 201, on_click,27,(52, 50, 119))        
p14=G1(pygame.Surface((30, 30)), 36, 201, on_click,False,(52, 50, 50))     
p15=G1(pygame.Surface((30, 30)), 3, 234, on_click,22,(52, 50, 119))        
p16=G1(pygame.Surface((30, 30)), 36, 234, on_click,23,(52, 50, 119))       
p17=G1(pygame.Surface((30, 30)), 3, 267, on_click,False,(41, 108, 50))     
p18=G1(pygame.Surface((30, 30)), 36, 267, on_click,24,(52, 50, 119))       
p19=G1(pygame.Surface((30, 30)), 3, 300, on_click,10,(52, 50, 119))        
p20=G1(pygame.Surface((30, 30)), 36, 300, on_click,False,(52, 50, 50))
p21=G1(pygame.Surface((30, 30)), 3, 333, on_click,9,(52, 50, 119))
p22=G1(pygame.Surface((30, 30)), 36, 333, on_click,25,(52, 50, 119))       
p23=G1(pygame.Surface((30, 30)), 3, 366, on_click,11,(52, 50, 119))        
p24=G1(pygame.Surface((30, 30)), 36, 366, on_click,8,(52, 50, 119))        
p25=G1(pygame.Surface((30, 30)), 3, 399, on_click,False,(52, 50, 50))      
p26=G1(pygame.Surface((30, 30)), 36, 399, on_click,7,(52, 50, 119))        
p27=G1(pygame.Surface((30, 30)), 3, 432, on_click,0,(52, 50, 119))
p28=G1(pygame.Surface((30, 30)), 36, 432, on_click,1,(52, 50, 119))        
p29=G1(pygame.Surface((30, 30)), 3, 465, on_click,5,(52, 50, 119))
p30=G1(pygame.Surface((30, 30)), 36, 465, on_click,False,(52, 50, 50))     
p31=G1(pygame.Surface((30, 30)), 3, 498, on_click,6,(52, 50, 119))
p32=G1(pygame.Surface((30, 30)), 36, 498, on_click,12,(52, 50, 119))       
p33=G1(pygame.Surface((30, 30)), 3, 531, on_click,13,(52, 50, 119))        
p34=G1(pygame.Surface((30, 30)), 36, 531, on_click,False,(52, 50, 50))     
p35=G1(pygame.Surface((30, 30)), 3, 564, on_click,19,(52, 50, 119))        
p36=G1(pygame.Surface((30, 30)), 36, 564, on_click,16,(52, 50, 119))       
p37=G1(pygame.Surface((30, 30)), 3, 597, on_click,26,(52, 50, 119))        
p38=G1(pygame.Surface((30, 30)), 36, 597, on_click,20,(52, 50, 119))       
p39=G1(pygame.Surface((30, 30)), 3, 630, on_click,False,(52, 50, 50)) 
p40=G1(pygame.Surface((30, 30)), 36, 630, on_click,21,(52, 50, 119))
clock = pygame.time.Clock()
group = pygame.sprite.Group(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40)
running = True
while running:
    events=pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    group.update(events)
    group.draw(screen)
    for i in range(40):
        exec(f"text{i}=font.render(pinout[{i}],True,'white')")
    x=5
    y=10
    for i in range(40):
        exec(f"screen.blit(text{i},({x},{y}))")
        if x==5:
            x=38
        else:
            x=5
            y+=33
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
