class Projectiles:
    def __init__(self,x,y,color,radius, velocity):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.velocity = 6
 
    def Bolt(self,win):
        pygame.draw.circle(win ,self.color, (self.x,self.y), self.radius)


     
