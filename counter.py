import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import QTimer, Qt

class CountdownApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("test")
        self.setFixedSize(300, 200)

    
        self.remaining_time = 60

        self.title_label = QLabel("welcome to my app")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        
        self.timer_label = QLabel(self.format_time(self.remaining_time))
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 32px;")

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")

    
        self.timer = QTimer()
        self.timer.setInterval(1000) 
        self.timer.timeout.connect(self.update_timer)

        
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.timer_label)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def format_time(self, seconds):
        m, s = divmod(seconds, 60)
        return f"{m:02d}:{s:02d}"

    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_label.setText(self.format_time(self.remaining_time))
        else:
            self.timer.stop()
            self.timer_label.setText("Time's up!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CountdownApp()
    window.show()
    sys.exit(app.exec())
