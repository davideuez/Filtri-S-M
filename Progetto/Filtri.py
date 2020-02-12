from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import cv2, threading, os, time
from threading import Thread
import numpy as np
import dlib
import datetime

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"/Users/Utente/Desktop/Filtri_S-M/shape_predictor_68_face_landmarks.dat")

# Sprites for first filter
Tatoo2 = cv2.imread(r"/Users/Utente/Desktop/Filtri_S-M/filtri/images/Tatoo2.png")
Tatoo = cv2.imread(r"/Users/Utente/Desktop/Filtri_S-M/filtri/images/t-69-text-temporary-tattoo-ink-daze-69-tattoo-png-800_800.png")
Tatoo2 = cv2.cvtColor(Tatoo2, cv2.COLOR_BGR2BGRA)
Tatoo = cv2.cvtColor(Tatoo, cv2.COLOR_BGR2BGRA)

# Sprites for second filter
imgMustache = cv2.imread(r'/Users/Utente/Desktop/Filtri_S-M/filtri/images/m.png',-1)
imgMustache = cv2.cvtColor(imgMustache, cv2.COLOR_BGR2BGRA)

Mono = cv2.imread(r'/Users/Utente/Desktop/Filtri_S-M/filtri/images/Occhio.png',-1)
Mono = cv2.cvtColor(Mono, cv2.COLOR_BGR2BGRA)

# Sprites for third filter
Lemmy = cv2.imread(r'/Users/Utente/Desktop/Filtri_S-M/filtri/images/MOUSTACHE-MD-2T.png',-1)
Lemmy = cv2.cvtColor(Lemmy, cv2.COLOR_BGR2BGRA)

Ray = cv2.imread(r"C:\Users\Utente\Desktop\Filtri_S-M/filtri/images\Occhiali.png")
Ray = cv2.cvtColor(Ray, cv2.COLOR_BGR2BGRA)

# Sprites for fourth filter
Dio = cv2.imread(r"C:\Users\Utente\Desktop\Filtri_S-M\filtri\images\JoJo.png")
Dio = cv2.cvtColor(Dio, cv2.COLOR_BGR2BGRA)

# Sprites Filter 5
GJ = cv2.imread(r"C:\Users\Utente\Desktop\Filtri_S-M\filtri\images\Eyepatch.png")
GJ = cv2.cvtColor(GJ, cv2.COLOR_BGR2BGRA)

GM = cv2.imread(r"C:\Users\Utente\Desktop\Filtri_S-M\filtri\images\Bandaid.png")
GM = cv2.cvtColor(GM, cv2.COLOR_BGR2BGRA)

# Initialize GUI object
root = Tk()
style = Style()
style.theme_use('classic')
root.title("Filtri S-M")
root.geometry("500x600")
root.configure(background='#508991')

title = Label(root, text = 'FILTRI S-M', font =('Verdana', 30), foreground='white', background ='#508991')
title.pack(side = TOP, pady = 20)

photo1 = PhotoImage(file = r"/Users/Utente/Desktop/Filtri_S-M/filtri/images/Tatoo2.gif")
photo2 = PhotoImage(file = r"/Users/Utente/Desktop/Filtri_S-M/filtri/images/mustache.gif")
photo3 = PhotoImage(file = r"/Users/Utente/Desktop/Filtri_S-M/filtri/images/Magnum_P.I._logo.gif")
photo4 = PhotoImage(file = r"/Users/Utente/Desktop/Filtri_S-M/filtri/images/jojo-lucca-comics-and-games-2019-araki-star-comics-week-day.gif")
  
# Resizing images to fit on buttons 
photoimage1 = photo1.subsample(4,4)
photoimage2 = photo2.subsample(9,9)
photoimage3 = photo3.subsample(15,15)
photoimage4 = photo4.subsample(20,20)

##Create 5 buttons and assign their corresponding function to active sprites
btn1 = Button(root, text="Tattoos Filter", command= lambda: apply_filter_1(), image = photoimage1, compound = TOP)
btn1.pack(side="top", fill="both", expand="no", padx="5", pady="5")

btn2 = Button(root, text="BD-Loove Filter", command= lambda: apply_filter_2(), image = photoimage2, compound = TOP)
btn2.pack(side="top", fill="both", expand="no", padx="5", pady="5")

btn3 = Button(root, text="Magnum P.I. Filter", command= lambda: apply_filter_3(), image = photoimage3, compound = TOP)
btn3.pack(side="top", fill="both", expand="no", padx="5", pady="5")

btn4 = Button(root, text="NANI?!?!?!!", command= lambda: apply_filter_4(), image = photoimage4, compound = TOP)
btn4.pack(side="top", fill="both", expand="no", padx="5", pady="5")

btn5 = Button(root, text="Filtro 5", command= lambda: apply_filter_5(), compound = TOP)
btn5.pack(side="top", fill="both", expand="no", padx="5", pady="5")

descriptionText = """\nHow to use the app:\n\n- Click one button above to open the camera with the filter\n- Press SPACE to take a screenshot or ESC to exit\n- If you like/dislike the photo you can save or delete it"""
description = Label(root, text = descriptionText, font =('Montserrat', 14), foreground='white', background ='#508991', justify = LEFT)
description.pack(side = TOP, pady=30)

def pnging1(img):

    mh,mw,mc = img.shape
    r = np.random.randint(0,100,dtype ='int')
    if r>50:
        for i in range(mh):
            for j in range(mw):
                if img[i,j,2]>100 and img[i,j,0]>100 and img[i,j,1]>100:
                    img[i,j,3]=0
                img[i,j,0]=255
                img[i,j,2]=255
    else:
        for i in range(mh):
            for j in range(mw):
                if img[i,j,2]>100 and img[i,j,0]>100 and img[i,j,1]>100:
                    img[i,j,3]=0
                img[i,j,1]=250
                img[i,j,2]=0
                img[i,j,0]=154
    return img, Tatoo; Tatoo2

def pnging2(img):
    mh,mw,mc = img.shape
    for i in range(mh):
        for j in range(mw):
            if img[i,j,2]>100 and img[i,j,0]>100 and img[i,j,1]>100:
                img[i,j,3]=0
    return img

def pnging3(img):
    mh,mw,mc = img.shape
    for i in range(mh):
        for j in range(mw):
            if img[i,j,2]>220 and img[i,j,0]>220 and img[i,j,1]>220:
                img[i,j,3]=0
    return img

def pnging4(img):
    mh,mw,mc = img.shape
    for i in range(mh):
        for j in range(mw):
            if img[i,j,2]<100 and img[i,j,0]<100 and img[i,j,1]<100:
                img[i,j,3]=0
    return img

gj_png = pnging3(GJ)
gm_png = pnging3(GM)
mpng = pnging2(imgMustache)
opng = pnging2(Mono)
tpng = pnging1(Tatoo)
tpng2 = pnging1(Tatoo2)
lpng = pnging3(Lemmy)
spng = pnging4(Ray)
nani = pnging3(Dio)

def apply_filter_1():

    # Capture from camera
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Effetto 1")
    cv2.moveWindow("Effetto 1", 400, 0)


    k=0

    while True:
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        fh,fw,fc = frame.shape
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
                
            if k%5 == 0:
                tpng = cv2.resize(Tatoo, (x2-x1,y2-y1), interpolation = cv2.INTER_CUBIC)
                tpng2 = cv2.resize(Tatoo2, (x2m-x1m,y2m-y1m), interpolation = cv2.INTER_CUBIC)
            th,tw,tc = tpng.shape        
            t2h,t2w,t2c = tpng2.shape
                
            for i in range(fh):
                for j in range(fw):
                    if i<th and j<tw:
                        if tpng[i,j,3]>0:    
                            frame[y1+i, x1+j] = tpng[i,j]
                    if i<t2h and j<t2w:
                        if tpng2[i,j,3]>0:    
                            frame[y1m-i, x1m+j] = tpng2[i,j]     
                                
            k=k+1
            cv2.imshow("Effetto 1", frame)
        
        wait = cv2.waitKey(1)

        if wait%256 == 27: # ESC pressed
            print("Escape hit, closing...")
            break
        elif wait%256 == 32: # SPACE pressed
            takeSnapshot(frame)
            break

    cap.release()
    cv2.destroyAllWindows()

def apply_filter_2():

    # Capture from camera
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Effetto 2")
    cv2.moveWindow("Effetto 2", 400, 0)
    k=0
    while True:
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        fh,fw,fc = frame.shape
        
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
            
            if k%8==0:
                opng = cv2.resize(Mono, (x2o-x1o, y2o-y1o), interpolation = cv2.INTER_AREA)
                mpng = cv2.resize(imgMustache, (x2-x1, y2-y1), interpolation = cv2.INTER_AREA)

            mh,mw,mc = mpng.shape
            hh,hw,hc = opng.shape
            
            k=k+1

            for i in range(fh):
                for j in range(fw):
                    if i<mh and j<mw:
                        if mpng[i,j,3]>0:
                            frame[y1+i, x1+j] = mpng[i,j]
                    if i<hh and j<hw:
                        if opng[i,j,3]>0:
                            frame[y1o+i,x1o+j]=opng[i,j]
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
            cv2.imshow("Effetto 2", frame)

        wait = cv2.waitKey(1)

        if wait%256 == 27: # ESC pressed
            print("Escape hit, closing...")
            break
        elif wait%256 == 32: # SPACE pressed
            takeSnapshot(frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    
def apply_filter_3():

    # Capture from camera
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Effetto 3")
    cv2.moveWindow("Effetto 3", 400, 0)
    k=0
    while True:
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        fh,fw,fc = frame.shape
        for face in faces:
            landmarks = predictor(gray, face)
            
            y1 = landmarks.part(18).y
            y2 = landmarks.part(30).y
            x1 = landmarks.part(17).x
            x2 = landmarks.part(46).x+30
                   
            y2m = landmarks.part(9).y
            y1m = landmarks.part(28).y
            x1m = landmarks.part(4).x
            x2m = landmarks.part(12).x
            
            if k%10 == 0:
                spng = cv2.resize(Ray, (x2-x1,y2-y1), interpolation = cv2.INTER_CUBIC)
                lpng = cv2.resize(Lemmy, (x2m-x1m,y2m-y1m), interpolation = cv2.INTER_CUBIC)
            sh,sw,sc = spng.shape
            lh,lw,lc = lpng.shape
            k=k+1
            for i in range(fh):
                for j in range(fw):
                    if i<sh and j<sw:
                        if spng[i,j,3]>0:    
                            frame[y1+i, x1+j] = spng[i,j]
                    if i<lh and j<lw:
                        if lpng[i,j,3]>0:    
                            frame[y1m+i, x1m+j] = lpng[i,j]
            
            cv2.imshow("Effetto 3", frame)

        wait = cv2.waitKey(1)

        if wait%256 == 27: # ESC pressed
            print("Escape hit, closing...")
            break
        elif wait%256 == 32: # SPACE pressed
            takeSnapshot(frame)
            break

    cap.release()
    cv2.destroyAllWindows()

def apply_filter_4():
    # Capture from camera
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Effetto 4")
    cv2.moveWindow("Effetto 4", 400, 0)
    k=0
    while True:
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        fh,fw,fc = frame.shape
        for face in faces:
            landmarks = predictor(gray, face)
            
            y1 = landmarks.part(34).y - 150
            y2 = landmarks.part(9).y + 50
            x1 = landmarks.part(17).x
            x2 = landmarks.part(46).x+50
            
            
            if k%10 == 0:
                nani = cv2.resize(Dio, (x2-x1,y2-y1), interpolation = cv2.INTER_CUBIC)
                
            th,tw,tc = nani.shape
            
            jxl = landmarks.part(1).x-tw
            jxr = landmarks.part(17).x+tw
            
            for i in range(fh):
                for j in range(fw):
                    if i<th and j<tw:
                        if nani[i,j,3]>0:    
                            frame[y1+i, jxl+j] = nani[i,j]
                    
            Z = -np.ones([5,5], dtype = int)
            Z [3,3] = 25               
            k=k+1
            cv2.imshow("JoJo!", frame)

        wait = cv2.waitKey(1)

        if wait%256 == 27: # ESC pressed
            print("Escape hit, closing...")
            break
        elif wait%256 == 32: # SPACE pressed
            frame = cv2.filter2D(frame, -1, Z)
            takeSnapshot(frame)
            break

    cap.release()
    cv2.destroyAllWindows()

def apply_filter_5():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Effetto 4")
    cv2.moveWindow("Effetto 4", 400, 0)
    k=0
    while True:
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        fh,fw,fc = frame.shape
        for face in faces:
            landmarks = predictor(gray, face)
            y2 = landmarks.part(5).y
            y1 = landmarks.part(29).y
            x1 = landmarks.part(3).x
            x2 = landmarks.part(37).x
                   
            y1m = landmarks.part(20).y-30
            y2m = landmarks.part(15).y
            x1m = landmarks.part(18).x-10
            x2m = landmarks.part(16).x
            
            if k%8 == 0:
                gm_png = cv2.resize(GM, (x2-x1,y2-y1), interpolation = cv2.INTER_CUBIC)
                gj_png = cv2.resize(GJ, (x2m-x1m,y2m-y1m), interpolation = cv2.INTER_CUBIC)
            gmh,gmw,gmc = gm_png.shape        
            gjh,gjw,gjc = gj_png.shape
            
            for i in range(fh):
                for j in range(fw):
                    if i<gmh and j<gmw:
                        if gm_png[i,j,3]>0:    
                            frame[y1+i, x1+j] = gm_png[i,j]
                    if i<gjh and j<gjw:
                        if gj_png[i,j,3]>0:    
                            frame[y1m+i, x1m+j] = gj_png[i,j]  
                            
            k=k+1
            cv2.imshow("Effetto 3", frame)

        wait = cv2.waitKey(1)

        if wait%256 == 27: # ESC pressed
            print("Escape hit, closing...")
            break
        elif wait%256 == 32: # SPACE pressed
            takeSnapshot(frame)
            break

def createSnapWindow(frame, filename):

    
    #time.sleep(1)

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

    deleteButton = Button(buttonsFrame, text="DELETE", command= lambda: [deleteSnapshot(filename),popup.destroy()])
    deleteButton.pack(side=LEFT, fill="both", expand="yes", padx="5", pady="5")


def takeSnapshot(frame):
    # grab the current timestamp and use it to construct the
    # output path

    ts = datetime.datetime.now()
    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
    p = os.path.sep.join(('/Users/Utente/Desktop/Filtri_S-M/filtri/output/', filename))
     
    # save the file
    cv2.imwrite(p, frame.copy())
    print("[INFO] saved {}".format(filename))

    createSnapWindow(frame,p)

def deleteSnapshot(filename):

    os.remove(filename)
    print("Snapshot has been deleted")

root.mainloop()