from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
import tkinter.messagebox
import pathlib
from PIL import Image
# Đọc ảnh

win = Tk()
win.title("chinhsuaanh")
win.geometry('500x100')
def select_image():
    global image
    global tk_image
    global xoay
    global zoom
    global img

    # Mở hộp thoại chọn ảnh
    filename = askopenfilename(filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("GIF", "*.gif"), ("BMP", "*.bmp")])
    cv2.destroyAllWindows()
    xoay = 0
    zoom = 1
    # Nếu người dùng chọn ảnh
    if filename:
        # Đọc ảnh và lưu vào biến image
        image = cv2.imread(filename)
        img = image.copy()
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('AnhXam', img)
    else:
        # Nếu người dùng không chọn ảnh, hiển thị thông báo
        tkinter.messagebox.showwarning("Cảnh báo", "Bạn chưa chọn ảnh!")
def nutbam1():
    global image
    global xam
    global img
    # Kiểm tra xem ảnh đã được chọn chưa
    if (image is None):
        tkinter.messagebox.showwarning("Cảnh báo", "Bạn chưa chọn ảnh!")
        return
    blurred_image = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Laplacian(blurred_image, cv2.CV_8U, ksize=5)
    # Hiển thị ảnh gốc và ảnh đã tách biên
    cv2.imshow('Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
bt = Button(win, text="chọn ảnh", command=select_image)
bt.place(x=120, y=10)
bt1 = Button(win, text="tách biên", command=nutbam1)
bt1.place(x=200, y=10)
win.mainloop()