from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import cv2
import threading
import os
import time
from threading import Thread
import numpy as np
import dlib
import datetime

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    r"/Users/davideuez/Desktop/Filtri_S-M/shape_predictor_68_face_landmarks.dat")

# Sprites for first filter
Tatoo2 = cv2.imread(
    r"/Users/davideuez/Desktop/Filtri_S-M/filtri/images/Tatoo2.png")
Tatoo = cv2.imread(
    r"/Users/davideuez/Desktop/Filtri_S-M/filtri/images/t-69-text-temporary-tattoo-ink-daze-69-tattoo-png-800_800.png")
Tatoo2 = cv2.cvtColor(Tatoo2, cv2.COLOR_BGR2BGRA)
Tatoo = cv2.cvtColor(Tatoo, cv2.COLOR_BGR2BGRA)

# Sprites for second filter
imgMustache = cv2.imread(
    r'/Users/davideuez/Desktop/Filtri_S-M/filtri/images/m.png', -1)
imgMustache = cv2.cvtColor(imgMustache, cv2.COLOR_BGR2BGRA)

Mono = cv2.imread(
    r'/Users/davideuez/Desktop/Filtri_S-M/filtri/images/Occhio.png', -1)
Mono = cv2.cvtColor(Mono, cv2.COLOR_BGR2BGRA)

# Initialize GUI object
root = Tk()
style = Style()
style.theme_use('classic')
root.title("Filtri S-M")
root.geometry("500x600")
root.configure(background='#508991')

title = Label(root, text='FILTRI S-M', font=('Verdana', 30),
              foreground='white', background='#508991')
title.pack(side=TOP, pady=20)

photo1 = PhotoImage(
    file=r"/Users/davideuez/Desktop/Filtri_S-M/filtri/images/Tatoo2.gif")
photo2 = PhotoImage(
    file=r"/Users/davideuez/Desktop/Filtri_S-M/filtri/images/mustache.gif")

# Resizing images to fit on buttons
photoimage1 = photo1.subsample(4, 4)
photoimage2 = photo2.subsample(9, 9)

# Create 5 buttons and assign their corresponding function to active sprites
btn1 = Button(root, text="Tattoos Filter",
              command=lambda: apply_filter_1(), image=photoimage1, compound=TOP)
btn1.pack(side="top", fill="both", expand="no", padx="5", pady="5")

btn2 = Button(root, text="BD-Loove Filter",
              command=lambda: apply_filter_2(), image=photoimage2, compound=TOP)
btn2.pack(side="top", fill="both", expand="no", padx="5", pady="5")

btn3 = Button(root, text="Filtro 3")
btn3.pack(side="top", fill="both", expand="no", padx="5", pady="5")

btn4 = Button(root, text="Filtro 4")
btn4.pack(side="top", fill="both", expand="no", padx="5", pady="5")

btn5 = Button(root, text="Filtro 5")
btn5.pack(side="top", fill="both", expand="no", padx="5", pady="5")

descriptionText = """\nHow to use the app:\n\n- Click one button above to open the camera with the filter\n- Press SPACE to take a screenshot or ESC to exit\n- If you like/dislike the photo you can save or delete it"""
description = Label(root, text=descriptionText, font=(
    'Montserrat', 14), foreground='white', background='#508991', justify=LEFT)
description.pack(side=TOP, pady=30)


def pnging1(img):

    mh, mw, mc = img.shape
    r = np.random.randint(0, 100, dtype='int')
    if r > 50:
        for i in range(mh):
            for j in range(mw):
                if img[i, j, 2] > 100 and img[i, j, 0] > 100 and img[i, j, 1] > 100:
                    img[i, j, 3] = 0
                img[i, j, 0] = 255
                img[i, j, 2] = 255
    else:
        for i in range(mh):
            for j in range(mw):
                if img[i, j, 2] > 100 and img[i, j, 0] > 100 and img[i, j, 1] > 100:
                    img[i, j, 3] = 0
                img[i, j, 1] = 250
                img[i, j, 2] = 0
                img[i, j, 0] = 154
    return img, Tatoo
    Tatoo2


tpng = pnging1(Tatoo)
tpng2 = pnging1(Tatoo2)


def pnging2(img):
    mh, mw, mc = img.shape
    for i in range(mh):
        for j in range(mw):
            if img[i, j, 2] > 100 and img[i, j, 0] > 100 and img[i, j, 1] > 100:
                img[i, j, 3] = 0
    return img


mpng = pnging2(imgMustache)
opng = pnging2(Mono)


def apply_filter_1():

        # Capture from camera
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Effetto 1")
    cv2.moveWindow("Effetto 1", 400, 0)

    k = 0

    while True:
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        fh, fw, fc = frame.shape
        for face in faces:
            landmarks = predictor(gray, face)

            y2 = landmarks.part(5).y
            y1 = landmarks.part(29).y
            x1 = landmarks.part(3).x
            x2 = landmarks.part(37).x

            y1m = landmarks.part(20).y
            y2m = landmarks.part(42).y
            x1m = landmarks.part(18).x
            x2m = landmarks.part(27).x

            if k % 5 == 0:
                tpng = cv2.resize(Tatoo, (x2-x1, y2-y1),
                                  interpolation=cv2.INTER_CUBIC)
                tpng2 = cv2.resize(Tatoo2, (x2m-x1m, y2m-y1m),
                                   interpolation=cv2.INTER_CUBIC)
            th, tw, tc = tpng.shape
            t2h, t2w, t2c = tpng2.shape

            for i in range(fh):
                for j in range(fw):
                    if i < th and j < tw:
                        if tpng[i, j, 3] > 0:
                            frame[y1+i, x1+j] = tpng[i, j]
                    if i < t2h and j < t2w:
                        if tpng2[i, j, 3] > 0:
                            frame[y1m-i, x1m+j] = tpng2[i, j]

            k = k+1
            cv2.imshow("Effetto 1", frame)

        wait = cv2.waitKey(1)

        if wait % 256 == 27:  # ESC pressed
            print("Escape hit, closing...")
            break
        elif wait % 256 == 32:  # SPACE pressed
            takeSnapshot(frame)
            break

    cap.release()
    cv2.destroyAllWindows()


def apply_filter_2():

    # Capture from camera
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Effetto 2")
    cv2.moveWindow("Effetto 2", 400, 0)

    Z = -np.ones([9, 9], dtype=int)
    Z[5, 5] = 91

    K = -np.ones([9, 9], dtype=int)
    K[5, 5] = 60

    while True:
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        fh, fw, fc = frame.shape
        for face in faces:
            landmarks = predictor(gray, face)

            y2 = landmarks.part(5).y
            y1 = landmarks.part(29).y
            x1 = landmarks.part(4).x
            x2 = landmarks.part(12).x

            y1o = landmarks.part(44).y
            y2o = landmarks.part(30).y
            x1o = landmarks.part(37).x
            x2o = landmarks.part(46).x

            opng = cv2.resize(Mono, (x2o-x1o, y2o-y1o),
                              interpolation=cv2.INTER_AREA)
            mpng = cv2.resize(imgMustache, (x2-x1, y2-y1),
                              interpolation=cv2.INTER_AREA)

            mh, mw, mc = mpng.shape
            hh, hw, hc = opng.shape

            for i in range(fh):
                for j in range(fw):
                    if i < mh and j < mw:
                        if mpng[i, j, 3] > 0:
                            frame[y1+i, x1+j] = mpng[i, j]
                    if i < hh and j < hw:
                        if opng[i, j, 3] > 0:
                            frame[y1o+i, x1o+j] = opng[i, j]
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
            cv2.imshow("Effetto 2", frame)

        wait = cv2.waitKey(1)

        if wait % 256 == 27:  # ESC pressed
            print("Escape hit, closing...")
            break
        elif wait % 256 == 32:  # SPACE pressed
            takeSnapshot(frame)
            break

    cap.release()
    cv2.destroyAllWindows()


def createSnapWindow(frame, filename):

    # time.sleep(1)

    popup = Toplevel()
    popup.title("About this application...")

    imageFrame = Frame(popup)
    imageFrame.pack(side=TOP)

    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)
    label = Label(imageFrame, image=photo)
    label.image = photo
    label.pack()

    buttonsFrame = Frame(popup)
    buttonsFrame.pack(side=BOTTOM, fill="both")

    saveButton = Button(buttonsFrame, text="SAVE", command=popup.destroy)
    saveButton.pack(side=LEFT, fill="both", expand="yes", padx="5", pady="5")

    deleteButton = Button(buttonsFrame, text="DELETE", command=lambda: [
                          deleteSnapshot(filename), popup.destroy()])
    deleteButton.pack(side=LEFT, fill="both", expand="yes", padx="5", pady="5")


def takeSnapshot(frame):
    # grab the current timestamp and use it to construct the
    # output path

    ts = datetime.datetime.now()
    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
    p = os.path.sep.join(
        ('/Users/davideuez/Desktop/Filtri_S-M/filtri/output/', filename))

    # save the file
    cv2.imwrite(p, frame.copy())
    print("[INFO] saved {}".format(filename))

    createSnapWindow(frame, p)


def deleteSnapshot(filename):

    os.remove(filename)
    print("Snapshot has been deleted")


root.mainloop()
