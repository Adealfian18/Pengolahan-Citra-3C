import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import ttk
from tkinter import*
from PIL import ImageTk, Image

def greyscale():
    cv2.imshow("Greyscale", grey)
    
def tresholding():
    cv2.imshow('Thresholded', thresh1)
    
def log():
    cv2.imshow('LoG',laplacian1)
    
def histogram():
    plt.show()
    
def uploadimage():
    filename = filedialog.askopenfilename()
    image = Image.open('daun.jfif')
    image = image.resize([300, 300])
    image = ImageTk.PhotoImage(image)
    image_ = Label(app, image=image)
    image_.place(x=140, y=70)

def chckcombobox():
    if combobox.get() == "Greyscale":
        return greyscale()
    elif combobox.get() == "Tresholding":
        return tresholding()
    elif combobox.get() == "Histogram":
        return histogram()
    elif combobox.get() == "LoG":
        return log()
        

app = Tk()
app.title("Segmentasi Citra")
app.geometry("600x700")

judul = Label(app, text="Segmentasi Citra", font=('Helvetica',20))
judul.place(x=140, y=30)


btn_upload = Button(app, text="Upload", command=uploadimage)
btn_upload.place(x=140, y=60)

btn_aplly = Button(app, text="apply", command=chckcombobox)
btn_aplly.place(x=170, y=60)

combobox = ttk.Combobox(app, width=15, values= ['Grayscale','Tresholding', 'LoG','Histogram'])
combobox.place(x=140, y=80)




#* read image
image = cv2.imread('daun.jfif')

# convert to grayscale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# applying gaussian blur
blurred = cv2.GaussianBlur(grey, (3, 3), 0)

# thresholdin: Otsu's Binarization method
_, thresh1 = cv2.threshold(blurred, 127, 255,
                            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# show thresholded image

image = cv2.imread("daun.jfif")

#* display image
cv2.imshow("image", image)

# TODO : tuple untuk warna dari garis histogram
colors = ("red", "green", "blue")
chanel_ids = (0, 1, 2)

# TODO : membuat histogram berwarna
plt.figure()
plt.xlim([0, 256])

for channel, color in zip(chanel_ids, colors):
    histogram, bins = np.histogram(image[:, :, channel], bins=256, range=(0, 256))
    plt.plot(bins[:-1], histogram, color=color)
    
plt.title("Histogram")
plt.xlabel("Color Value")
plt.ylabel("Pixel Count")

# Apply Laplacian operator in some higher datatype
laplacian = cv2.Laplacian(blurred,cv2.CV_64F)

# But this tends to localize the edge towards the brighter side.
laplacian1 = laplacian/laplacian.max()


cv2.waitKey(0)
app.mainloop()
