from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor
import sys
from cell import Cell

class Dashboard(QWidget):
    def __init__(self, width, height,x = 0,y = 0):
        super().__init__()
        self.setFixedSize(width,height)
        layout1 = QHBoxLayout()
        # print(width)
        self.cell0 = Cell("icon/CO2_icon.png","CO2",width/3, height/2,color="#FF0000")
        self.cell1 = Cell("icon/NO2_icon.png","NO2",width/3, height/2,color="#00FF00")
        self.cell2 = Cell("icon/SO2_icon.png","SO2",width/3, height/2,color="#0000FF")
        layout1.addWidget(self.cell0,stretch=1)
        layout1.addWidget(self.cell1,stretch=1)
        layout1.addWidget(self.cell2,stretch=1)
        layout1.setSpacing(0)
        layout1.setContentsMargins(0,0,0,0)
        
        layout2 = QHBoxLayout()
        self.cell3 = Cell("icon/CO_icon.png","CO",width/3, height/2,color="#66CCFF")
        self.cell4 = Cell("icon/O3_icon.png","O3",width/3, height/2,color="#FFCC00")
        self.cell5 = Cell("icon/VOC_icon.png","VOC",width/3, height/2,color="#CCCCFF")
        layout2.addWidget(self.cell3,stretch=1)
        layout2.addWidget(self.cell4,stretch=1)
        layout2.addWidget(self.cell5,stretch=1)
        layout2.setSpacing(0)
        layout2.setContentsMargins(0,0,0,0)
        
        
        
        layout = QVBoxLayout()
        layout.addLayout(layout1,stretch=1)
        layout.addLayout(layout2,stretch=1)
        layout.addStretch(1)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = AirQualityMonitor()
    # ex = Cell("CO2_icon.png","CO2",300, 200,color="#00FF00")
    ex = Dashboard(1920,200)
    ex.showFullScreen()
    # ex.show()

    sys.exit(app.exec())

        
        