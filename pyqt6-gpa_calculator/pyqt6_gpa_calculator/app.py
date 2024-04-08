import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        self.UiComponents()
    
    def UiComponents(self):

            self.layout = QVBoxLayout()

            self.widget = QWidget()
            self.widget.setLayout(self.layout)

            self.title_label = QLabel("GPA Calculator")
            self.layout.addWidget(self.title_label)


            self.gpa1_spinbox = QSpinBox()
            self.gpa2_spinbox = QSpinBox()
            self.gpa3_spinbox = QSpinBox()
            self.gpa4_spinbox = QSpinBox()
            self.gpa5_spinbox = QSpinBox()
            self.gpa6_spinbox = QSpinBox()
            self.gpa7_spinbox = QSpinBox()
            self.gpa8_spinbox = QSpinBox()
            
            self.layout.addWidget(self.gpa1_spinbox)
            self.layout.addWidget(self.gpa2_spinbox)
            self.layout.addWidget(self.gpa3_spinbox)
            self.layout.addWidget(self.gpa4_spinbox)
            self.layout.addWidget(self.gpa5_spinbox)
            self.layout.addWidget(self.gpa6_spinbox)
            self.layout.addWidget(self.gpa7_spinbox)
            self.layout.addWidget(self.gpa8_spinbox)

            self.gpa_label = QLabel("GPA")
            self.layout.addWidget(self.gpa_label)

            # Set the central widget of the Window. Widget will expand
            # to take up all the space in the window by default.
            self.setCentralWidget(self.widget)
            self.calculate_btn = QPushButton(text = "Calculate")
            self.layout.addWidget(self.calculate_btn)
            self.calculate_btn.pressed.connect(self.calculate_gpa)


    def calculate_gpa(self):
                
        self.gpa_label.setText(str((int(self.gpa1_spinbox.value()) + int(self.gpa2_spinbox.value()) + int(self.gpa3_spinbox.value()) + int(self.gpa4_spinbox.value()) + int(self.gpa5_spinbox.value()) + int(self.gpa6_spinbox.value()) + int(self.gpa7_spinbox.value()) + int(self.gpa8_spinbox.value()))/8)) 





app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

