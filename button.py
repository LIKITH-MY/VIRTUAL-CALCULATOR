import cv2
import numpy as np

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value
        self.hover_alpha = 0

    def draw(self, frame, hover=False):
        x, y = self.pos
        if hover:
            self.hover_alpha = min(1, self.hover_alpha + 0.15)
        else:
            self.hover_alpha = max(0, self.hover_alpha - 0.15)

        base_color = np.array((50,50,50))
        hover_color = np.array((0,200,255))
        color = (1-self.hover_alpha)*base_color + self.hover_alpha*hover_color
        color = tuple(map(int, color))

        cv2.rectangle(frame,(x+5,y+5),(x+self.width+5,y+self.height+5),(30,30,30),cv2.FILLED)
        cv2.rectangle(frame,self.pos,(x+self.width,y+self.height),color,cv2.FILLED)

    def is_hover(self,x,y):
        bx,by=self.pos
        return bx<=x<=bx+self.width and by<=y<=by+self.height
