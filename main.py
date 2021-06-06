#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PIL import Image
from PIL import ImageFilter
from PyQt5.QtGui import QPixmap

app = QApplication([])
window1 = QWidget()

i = 0
spisok = QListWidget()
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()
knopka1 = QPushButton('папка')
knopka2 = QPushButton('влево')
knopka3 = QPushButton('вправо')
knopka4 = QPushButton('зеркально')
knopka5 = QPushButton('резкость')
knopka6 = QPushButton('Ч/Б')
text =QLabel("Имаге")

line1.addWidget(knopka1)
line1.addWidget(spisok)
line3.addWidget(knopka2)
line3.addWidget(knopka3)
line3.addWidget(knopka4)
line3.addWidget(knopka5)
line3.addWidget(knopka6)
line2.addWidget(text)

line2.addLayout(line3)
line5.addLayout(line1)
line5.addLayout(line2)
window1.setLayout(line5)

def open():
    workdir,_ = QFileDialog.getOpenFileName(caption= " ",directory= "C:\\",filter= "Image(*.png *.jpg )")
    text.setPixmap(QPixmap(workdir))

    spisok.insertItem(i,workdir)
    spisok.setCurrentRow(i)

def loading():
    picture = spisok.currentItem()
    text.setPixmap(QPixmap(picture.text()))
    
def light():
    picture = spisok.currentItem()
    img = Image.open(picture.text())
    img = img.convert("L")
    loading()

#открой файл с оригиналом картинки
def gray():
    with Image.open("image.jpg") as pig_dog:
        pig_gray = pig_dog.convert("L")
        text. hide()
        pixmapimageor = QPixmap("original.jpg")
        w, h = text. width(), text. height()
        pixmapimageor = pixmapimageor.scaled(w, h, Qt.KeepAspectRatio)

        text.setPixmap(pixmapimageor)
        text. show()
    #сделай оригинал изображения чёрно-белым
def filte():
    with Image.open("image.jpg") as pig_dog:
        pig_gg = pig_dog.filter(ImageFilter.BLUR)
        text. hide()
        pixmapimageor = QPixmap("original.jpg")
        w, h = text. width(), text. height()
        pixmapimageor = pixmapimageor.scaled(w, h, Qt.KeepAspectRatio)

        text.setPixmap(pixmapimageor)
        text. show()
    #сделай оригинал изображения размытым
def perevert():
    with Image.open("image.jpg") as pig_dog:
        pig_up = pig_dog.transpose(Image.ROTATE_90)
        text. hide()
        pixmapimageor = QPixmap("original.jpg")
        w, h = text. width(), text. height()
        pixmapimageor = pixmapimageor.scaled(w, h, Qt.KeepAspectRatio)

        text.setPixmap(pixmapimageor)
        text. show()
    #поверни оригинал изображения на 180 градусов

spisok.clicked.connect(loading)
knopka1.clicked.connect(open)
knopka2.clicked.connect(perevert)
knopka6.clicked.connect(gray)
knopka5.clicked.connect(filte)

window1.show()
app.exec()






















