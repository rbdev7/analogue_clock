from tkinter import Tk, Canvas
import time
import numpy
import clock

width = 400
height = 400

theta = 0.00175
r = 200

clock = clock.Clock()

tk = Tk()
# Find the center coordinates of the screen
posRight = int(tk.winfo_screenwidth()/2 - width/2)
posDown = int(tk.winfo_screenheight()/2 - height/2)

tk.title("Analogue Clock")
tk.geometry(str(width) + 'x' + str(height) + '+' + str(posRight) + '+' + str(posDown))

# Set the canvas to be the same width and height as the window and assign it to the window.
canvas = Canvas(tk,width=width,height=height)

centre = (width/2,height/2)
canvas.create_oval(3,3,397,397,outline="#f11")
canvas.pack()

# Create the hands
hour_hand = canvas.create_line(centre,100,0)
minute_hand = canvas.create_line(centre,200,0,fill="blue")
second_hand = canvas.create_line(centre,200,0,fill="red")

#for x in range(0, 60):
while(1):    
    clock.update()
    
    theta_h = 0.524 * clock.Hour
    theta_m = 0.105 * clock.Minutes
    theta_s = 0.105 * clock.Seconds
    
    # To rotate the hands 90 degrees to the left use "theta-pi/2"
    canvas.coords(hour_hand,[centre[0],centre[1],centre[0]+r*numpy.cos(theta_h-numpy.pi/2)/1.5,centre[1]+r*numpy.sin(theta_h-numpy.pi/2)/1.5])
    canvas.coords(minute_hand,[centre[0],centre[1],centre[0]+r*numpy.cos(theta_m-numpy.pi/2)/1.15,centre[1]+r*numpy.sin(theta_m-numpy.pi/2)/1.15])
    canvas.coords(second_hand,[centre[0],centre[1],centre[0]+r*numpy.cos(theta_s-numpy.pi/2)/1.1,centre[1]+r*numpy.sin(theta_s-numpy.pi/2)/1.1])
    tk.update()
    time.sleep(1)

tk.mainloop()
