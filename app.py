import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap
from cell import Cell
from window import Window
class AirQualityMonitor(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_values)
        self.timer.start(1000)  # Cập nhật mỗi giây

    def initUI(self):
        self.layout = QVBoxLayout()

        # Tạo layout cho từng thông số
        self.temperature_layout = QHBoxLayout()
        self.humidity_layout = QHBoxLayout()
        self.co2_layout = QHBoxLayout()

        # Hình ảnh cho nhiệt độ
        self.temperature_image = QLabel(self)
        self.temperature_image.setPixmap(QPixmap('temperature.png').scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        self.temperature_label = QLabel('Nhiệt độ: -- °C', self)
        self.temperature_layout.addWidget(self.temperature_image)
        self.temperature_layout.addWidget(self.temperature_label)

        # Hình ảnh cho độ ẩm
        self.humidity_image = QLabel(self)
        self.humidity_image.setPixmap(QPixmap('humidity.png').scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        self.humidity_label = QLabel('Độ ẩm: -- %', self)
        self.humidity_layout.addWidget(self.humidity_image)
        self.humidity_layout.addWidget(self.humidity_label)

        # Hình ảnh cho CO2
        self.co2_image = QLabel(self)
        self.co2_image.setPixmap(QPixmap('co2.png').scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        self.co2_label = QLabel('CO2: -- ppm', self)
        self.co2_layout.addWidget(self.co2_image)
        self.co2_layout.addWidget(self.co2_label)

        # Thêm các layout vào layout chính
        self.layout.addLayout(self.temperature_layout)
        self.layout.addLayout(self.humidity_layout)
        self.layout.addLayout(self.co2_layout)

        self.setLayout(self.layout)
        self.setWindowTitle('Quan Trắc Không Khí')
        self.setGeometry(100, 100, 400, 200)

    def update_values(self):
        temperature = random.uniform(20.0, 30.0)  # Giá trị nhiệt độ giả lập
        humidity = random.uniform(40.0, 60.0)     # Giá trị độ ẩm giả lập
        co2 = random.uniform(300, 500)            # Giá trị CO2 giả lập

        self.temperature_label.setText(f'Nhiệt độ: {temperature:.2f} °C')
        self.humidity_label.setText(f'Độ ẩm: {humidity:.2f} %')
        self.co2_label.setText(f'CO2: {co2:.2f} ppm')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = AirQualityMonitor()
    ex = Cell("CO2_icon.png","CO2",300, 200,color="#00FF00")
    # ex = Window()
    ex.show()

    sys.exit(app.exec())
