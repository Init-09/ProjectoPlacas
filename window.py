from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

def btn_clicked():
    print("Button Clicked")

def iniciar():
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizar()

def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)
        else:
            lblVideo.image = ""
            cap.release()

def finalizar():
    global cap
    cap.release()

window = Tk()

lblInfoVideoPath = Label(window, text="Aún no se ha seleccionado un video")
lblInfoVideoPath.grid(column=1, row=1)

window.geometry("996x720")
window.configure(bg = "#f2f2f2")
canvas = Canvas(
    window,
    bg = "#f2f2f2",
    height = 720,
    width = 996,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    883.5, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = iniciar,
    relief = "flat")

b0.place(
    x = 96, y = 597,
    width = 170,
    height = 68)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 392, y = 437,
    width = 170,
    height = 68)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 82, y = 436,
    width = 170,
    height = 68)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 799, y = 231,
    width = 170,
    height = 68)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 799, y = 564,
    width = 170,
    height = 68)

canvas.create_text(
    498.5, 46.0,
    text = "Sistema de control de placas",
    fill = "#000000",
    font = ("None", int(24.0)))


img023 = PhotoImage(file = f"img4.png")

# lblVideo = Label(window)(
#     139.5, 200.0)


canvas.create_text(
    139.5, 413.0,
    text = "Entrasdda",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    441.0, 413.0,
    text = "Salida",
    fill = "#000000",
    font = ("None", int(24.0)))


background_img1 = PhotoImage(file = f"img5.png")
background = canvas.create_image(
    883.5, 128.5,
    image=background_img1)



canvas.create_text(
    883.5, 152.5,
    text = "#xreiy0",
    fill = "#000000",
    font = ("None", int(18.0)))

canvas.create_text(
    884.0, 105.0,
    text = "Ticket",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    883.5, 388.5,
    text = "12/12/2021 6:00 am",
    fill = "#000000",
    font = ("None", int(18.0)))

canvas.create_text(
    884.0, 505.5,
    text = "12/12/2021 18:00 pm",
    fill = "#000000",
    font = ("None", int(18.0)))

canvas.create_text(
    883.5, 337.0,
    text = "Entrada",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    875.0, 454.0,
    text = "Salida",
    fill = "#000000",
    font = ("None", int(24.0)))


background_img2 = PhotoImage(file = f"img6.png")
background = canvas.create_image(
    876.0, 664.5,
    image=background_img2)

canvas.create_text(
    838.0, 667.5,
    text = "Lps.",
    fill = "#000000",
    font = ("None", int(18.0)))

canvas.create_text(
    896.0, 667.5,
    text = "1000",
    fill = "#000000",
    font = ("None", int(18.0)))

window.resizable(False, False)
window.mainloop()
