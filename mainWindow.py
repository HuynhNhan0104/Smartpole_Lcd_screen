from PySide6.QtCore import  QUrl ,QTimer, Signal, Slot
from PySide6.QtMultimedia import QMediaPlayer , QAudioOutput, QAudioDevice,QMediaDevices

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor
import sys
import random
import paho.mqtt.client as mqttclient
import json
import streamlink
import time
from cell import Cell
from dashboard import Dashboard, MESSURE
from video import VideoWindow
import threading
# ######## TO DO ############
# use QMQTT instead paho
# MQTT declear

ADAFRUIT_IO_USERNAME = "NhanHuynh"
ADAFRUIT_IO_KEY = ""
BROKER_ADDRESS = "io.adafruit.com"
PORT = 1883

feeds_list = [
    "NhanHuynh/feeds/link"
]
class MainWindow(QWidget):
    def __init__(self,width,height,url) -> None:
        super().__init__()
        self.setFixedSize(width,height)
        
        layout = QVBoxLayout()
        self.dashboard = Dashboard(width,height*0.3)
        layout.addWidget(self.dashboard,stretch=1)
        self.video_window = VideoWindow(width,height*0.7,url)
        layout.addWidget(self.video_window)
        layout.addStretch(1)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        # create mqtt
        self.client = mqttclient.Client("2013961")
        self.client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

        self.client.on_connect = self.on_connected
        self.client.on_subscribe = self.on_subscribed
        self.client.on_message = self.on_messaged
        self.client.connect(BROKER_ADDRESS, 1883)
        self.client.loop_start()
    
    def run(self):
        self.showFullScreen()
        self.video_window.video_player.play()
        print("[App] running success")
        
    
          
    def on_subscribed(self, client, userdata, mid, granted_qos):
        print("subscribed successfully")
        pass

    def on_messaged(self, client, userdata, message):
        topic = message.topic
        data = message.payload.decode("utf-8")
        try:
            # process message here
            print(f"received message on topic {topic}: {data}")
            if topic == "NhanHuynh/feeds/link":
                self.video_window.change_source_signal[str].emit(data)
                # self.change_source(data)
        except Exception as e:
            print(e)
        
    def on_connected(self, client, usedata, flags, rc):
        if rc == 0:
            for feed in feeds_list:
                client.subscribe(feed)
        else:
            print("Connection is failed")
    
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = AirQualityMonitor()
    # ex = Cell("CO2_icon.png","CO2",300, 200,color="#00FF00")
    # ex = MainWindow(1920,1080,"https://www.youtube.com/watch?v=rKn4EQ3-Ns0")
    ex = MainWindow(1920,1080,"https://www.twitch.tv/mrpokke")
    
    ex.showFullScreen()
    ex.video_window.video_player.play()
    ex.dashboard.update_text_cell(MESSURE.CO2,"100")
    ex.dashboard.update_text_cell(MESSURE.NOx,"100")
    ex.dashboard.update_text_cell(MESSURE.SO2,"100")
    ex.dashboard.update_text_cell(MESSURE.CO,"100")
    ex.dashboard.update_text_cell(MESSURE.O3,"100")
    ex.dashboard.update_text_cell(MESSURE.VOC,"100")
    
        
    
    
    
    
    
    # ex.show()

    sys.exit(app.exec())

        