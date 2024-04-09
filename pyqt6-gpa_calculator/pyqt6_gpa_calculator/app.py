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
    QFormLayout,
    QDouble
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

            self.layout.addRow("Grade 1:", QDoubleSpinBox)



            # Set the central widget of the Window. Widget will expand
            # to take up all the space in the window by default.
            self.setCentralWidget(self.widget)
            #self.calculate_btn = QPushButton(text = "Calculate")
            #self.layout.addWidget(self.calculate_btn)
            #self.calculate_btn.pressed.connect(self.calculate_gpa)


    #def calculate_gpa(self):
                
        #self.gpa_label.setText(str((int(self.gpa1_spinbox.value()) + int(self.gpa2_spinbox.value()) + int(self.gpa3_spinbox.value()) + int(self.gpa4_spinbox.value()) + int(self.gpa5_spinbox.value()) + int(self.gpa6_spinbox.value()) + int(self.gpa7_spinbox.value()) + int(self.gpa8_spinbox.value()))/8)) 





app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()