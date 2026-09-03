### IMPORTANT: LINE FOR QT DESIGNER: WRITE THAT IN TERMINAL TO OPEN: pyside6-designer
import sys
import os
from PySide6.QtCore import Slot, Signal, QSize, Qt
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (QDialog,
                               QWidget, 
                               QApplication, 
                               QFileDialog, 
                               QHBoxLayout, 
                               QVBoxLayout,
                               QLabel, 
                               QPushButton, 
                               QLayout, 
                               QTextEdit)
class Browser(QDialog):
    path= Signal(str)
    def __init__(self, parent= None):
        super().__init__(parent)
        self.__browser= QPushButton("browser")
        self.__save= QPushButton("save")
        self.__canva= QLabel()
        self.__layout_office= QHBoxLayout()
        self.__main_layout= QHBoxLayout()
        self.textbox = QTextEdit()
        self.textbox.setFixedHeight(50)
        self.__layout_office.addWidget(self.__browser)
        self.__layout_office.addWidget(self.__save)
        self.__layout_office.addWidget(self.textbox)
        self.__main_layout.addLayout(self.__layout_office)
        self.setLayout(self.__main_layout)
        self.__browser.clicked.connect(self.getFileName)
        self.__save.clicked.connect(self.save_file)


    @property
    def browser(self):
        return self.__browser

    @property
    def save(self):
        return self.__save

    

    @Slot()
    def getFileName(self):
        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls);; Image File (*.png *.jpg)'
        response = QFileDialog.getOpenFileName(
            self,
            'Select a file',
            os.getcwd(),
            filter=file_filter,
            selectedFilter= 'Image File (*.png *.jpg)'
        )
        self.textbox.setText(str(response))
        self.__path_text= response[0]
        self.path.emit(self.__path_text)


    @Slot()
    def save_file(self):

        path, _ = QFileDialog.getSaveFileName(
        self,
        "Save Image",
        os.getcwd(),
        "Image File (*.jpg)"
        )
        if path:
            my_content = "This is the text that will be saved to the hard drive."

            with open(path, "w", encoding="utf-8") as file:
                file.write(my_content)
        

class ShowImage(QWidget):
    def __init__(self,parent= None):
        super().__init__(parent)
        self.__image= QImage()
        self.__label= QLabel()
        self.__label.setFixedSize(QSize(400,400))
        self._layout= QHBoxLayout()
        self.setLayout(self._layout)

    @Slot(str)
    def recieve_path(self, path):
        self.__path= path 
        self.show_image()

    def show_image(self):
        self.__image.load(self.__path)
        pixmap= QPixmap(self.__image)
        pixmap= pixmap.scaled(self.__label.size(), aspectMode= Qt.KeepAspectRatio)
        self.__label.setPixmap(pixmap)
        self._layout.addWidget(self.__label)


class MainWindow(QWidget):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.__browser= Browser()
        self.__picture= ShowImage()
        self._layout= QVBoxLayout()
        self.__browser.path.connect(self.__picture.recieve_path)


        self._layout.addWidget(self.__browser)
        self._layout.addWidget(self.__picture)


        self.setLayout(self._layout)
        self.resize(QSize(700,700))


def main():
    app= QApplication(sys.argv)
    test= MainWindow()
    test.show()

    sys.exit((app.exec_()))
    


if __name__== "__main__":
    main()

        
