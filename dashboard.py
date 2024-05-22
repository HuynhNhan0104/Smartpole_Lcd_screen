from PySide6.QtCore import  QUrl ,QTimer, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor
import sys
import random
from cell import Cell
import requests
import json
class MESSURE(enumerate):
    CO2 = 0
    NOx = 1
    SO2 = 2
    CO = 3
    O3 = 4
    VOC = 5
    PM1_0 = 6
    PM2_5 = 7
    PM4 = 8
    PM10 = 9
class Dashboard(QWidget):
    def __init__(self, width, height,x = 0,y = 0):
        super().__init__()
        self.setFixedSize(width,height)
        layout1 = QHBoxLayout()
        
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(10000)
        # print(width)
        self.cell0 = Cell("icon/CO2_icon.png","CO2 ppm",width/3, height/2,color="#FF6666")
        self.cell1 = Cell("icon/NOx_icon.png","NO2 ppm",width/3, height/2,color="#66FF66")
        self.cell2 = Cell("icon/PM1_icon.png","PM1 μg/m³",width/3, height/2,color="#33CCFF")
        layout1.addWidget(self.cell0,stretch=1)
        layout1.addWidget(self.cell1,stretch=1)
        layout1.addWidget(self.cell2,stretch=1)
        layout1.setSpacing(0)
        layout1.setContentsMargins(0,0,0,0)
        
        layout2 = QHBoxLayout()
        self.cell3 = Cell("icon/PM2.5_icon.png","PM2.5 μg/m³",width/3, height/2,color="#3366FF")
        self.cell4 = Cell("icon/PM10_icon.png","PM10 μg/m³",width/3, height/2,color="#FFCC00")
        self.cell5 = Cell("icon/VOC_icon.png","VOC μg/m³",width/3, height/2,color="#CCCCFF")
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
    
    
    def update_text_cell(self,cell_id, new_text):
        if cell_id == MESSURE.CO2 :
            self.cell0.update_text(new_text)
        if cell_id == MESSURE.NOx :
            self.cell1.update_text(new_text)
            
        if cell_id == MESSURE.PM1_0 :
            self.cell2.update_text(new_text)
            
        if cell_id == MESSURE.PM2_5 :
            self.cell3.update_text(new_text)
            
        if cell_id == MESSURE.PM10 :
            self.cell4.update_text(new_text)
            
        if cell_id == MESSURE.VOC :
            self.cell5.update_text(new_text)
        
    def update_data(self):
        # print("Starting update air")
        api_url = "https://ezdata2.m5stack.com/api/v2/4827E2E30938/dataMacByKey/raw"
        response = requests.get(api_url)
        if response.status_code == 200:
            content= json.loads(response.content)
            # print(json.dumps(content, indent=4))
            data = content.get("data")
            value_str = data.get("value").replace("\\", "")
            value = json.loads(value_str)
            co2 = value["scd40"]["co2"]
            nox = 0 if value["sen55"]["nox"] is None else value["sen55"]["nox"]
            pm1 = value["sen55"]["pm1.0"]
            pm25 = value["sen55"]["pm2.5"]
            pm10 = value["sen55"]["pm10.0"]
            voc = value["sen55"]["voc"]
            self.update_text_cell(MESSURE.CO2,f"{co2:.2f} ppm")
            self.update_text_cell(MESSURE.PM1_0,f"{pm1:.2f} μg/m³")
            self.update_text_cell(MESSURE.NOx,f"{nox:.2f} ppm")
            self.update_text_cell(MESSURE.PM2_5,f"{pm25:.2f} μg/m³")
            self.update_text_cell(MESSURE.PM10,f"{pm10:.2f} μg/m³")
            self.update_text_cell(MESSURE.VOC,f"{voc:.2f} μg/m³") 

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = AirQualityMonitor()
    # ex = Cell("CO2_icon.png","CO2",300, 200,color="#00FF00")
    ex = Dashboard(1920,200)
    ex.showFullScreen()
    # ex.show()

    sys.exit(app.exec())

        
        