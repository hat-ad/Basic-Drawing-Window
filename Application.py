from tkinter import *
from PIL import  Image, ImageDraw

class mainApplication:
    def __init__(self,master):
        self.oldx=None
        self.oldy=None
        self.can=None
        self.white=(255, 255, 255)

    def canvas(self,master):
        self.can=Canvas(master,height=350,width=350,bg="white")
        self.can.pack()
        self.image1 = Image.new("RGB", (400, 400),self.white)
        self.draw = ImageDraw.Draw(self.image1)


    def save(self):
        self.filename = "image.png"
        self.image1.save(self.filename)

    def draw_(self,event):
        if self.oldx and self.oldy:
            self.pen=self.can.create_line(self.oldx,self.oldy,event.x,event.y,smooth=TRUE,width=5)
            self.d=self.draw.line([self.oldx,self.oldy,event.x,event.y], fill="black", width=5)

        self.oldx=event.x
        self.oldy=event.y

    def __events__(self):
        self.can.bind('<B1-Motion>', self.draw_)

    def button(self,master):
        self.save_=Button(master,text="Save",command=self.save)
        self.clear=Button(master,text="Clear",command=lambda :self.can.delete("all"))
        self.save_.pack(side=BOTTOM)
        self.clear.pack(side=BOTTOM)


if __name__ == '__main__':
    root=Tk()
    root.minsize(height=400,width=400)
    root.maxsize(height=400,width=400)
    ob=mainApplication(root)
    ob.canvas(root)

    ob.button(root)
    ob.save()
    ob.__events__()
    root.mainloop()
