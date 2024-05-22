from PySide6.QtCore import  QUrl ,QTimer, Signal, Slot
from PySide6.QtMultimedia import QMediaPlayer , QAudioOutput, QAudioDevice,QMediaDevices
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel,QSizePolicy, QVBoxLayout, QFrame,QMainWindow
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor

import sys
import vlc
import streamlink

class VideoWindow(QWidget):
    change_source_signal = Signal(str)
    
    def __init__(self,width=1000, height=1000, url=None) -> None:
        super().__init__()
        self.setFixedSize(width,height)
        layout = QVBoxLayout()
        self.change_source_signal.connect(self.change_source)
        
        # url = "https://www.youtube.com/watch?v=rKn4EQ3-Ns0"
        # url=
        stream = streamlink.streams(url)
        url = stream['best'].to_url()
        # url = stream['best'].to_manifest_url()
        self.video_player = QMediaPlayer()
        self.video_player.setSource(QUrl(url))
        
        
        # Video frame
        self.videoWidget   = QVideoWidget()
        self.video_player.setVideoOutput(self.videoWidget)
        
        #audio output
        self.audio_output  = QAudioOutput()
        self.video_player.setAudioOutput(self.audio_output)
        device = QAudioDevice(QMediaDevices.defaultAudioOutput())
        self.audio_output.setDevice(device)
        self.audio_output.setVolume(1)
        
        
        # addlayout
        layout.addWidget(self.videoWidget)
        self.setLayout(layout)
        
    @Slot(str)    
    def change_source(self, new_url):
        # new_url = "https://www.youtube.com/watch?v=rKn4EQ3-Ns0"
        # print(f"POSITION{self.video_window.video_player.position()}")
        self.video_player.stop()
        stream = streamlink.streams(new_url)
        # for key, value in stream.items():
        #     print(f"Type:{key} ")
        #     # print(f"\t {value}")
        #     print(f"\t {value.to_url()}")
        #     print(f'\t {value.to_manifest_url()}')
        url = stream['480p'].to_url()
        # url = stream['best'].to_manifest_url()
        self.video_player.setSource(QUrl(url))
        self.video_player.play() 
    



if __name__ == "__main__":

    app = QApplication(sys.argv)

    player = VideoWindow(url="https://www.youtube.com/watch?v=rKn4EQ3-Ns0")
    player.show()
    player.video_player.play()
    
    
    
    

    


    sys.exit(app.exec_())