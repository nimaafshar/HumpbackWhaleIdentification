
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *



name = globals()['name']

width = 200
height = 200
center = height//2
transparent = (255,0,0,0)
green = (0,128,0)

def save():
    filename = './mask/'+name[:-4]+'.png'
    image1.save(filename)

def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="green",width=3)
    draw.line([x1, y1, x2, y2],fill="green",width=3)

root = Tk()

# Tkinter create a canvas to draw on


# background_label = Label(root, image=photo)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# cv = Canvas(root, width=width, height=height,bg="white")
# cv.pack()
# background_label.pack()
image = PIL.Image.open('./train/'+name)
width , height = image.size
canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=0)
# canvas.create_rectangle(0,0,width,height, fill='white')
image = ImageTk.PhotoImage(image)
image_id = canvas.create_image(width,height, image=image)
canvas.move(image_id,-width/2,-height/2)
# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGBA", (width, height), transparent)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

canvas.pack(expand=YES, fill=BOTH)
canvas.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)
button=Button(text="save",command=save)
button.pack()
root.mainloop()
