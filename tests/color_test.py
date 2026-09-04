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


class HSL(QWidget):
    def __init__(self, parent= None):
        super().__init__(parent)
        
