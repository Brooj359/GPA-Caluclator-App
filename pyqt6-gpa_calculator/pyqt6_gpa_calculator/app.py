import sys
from PyQt6.QtGui import QFont
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
    QDoubleSpinBox,
    QHBoxLayout,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        self.UiComponents()
    
    def UiComponents(self):
            self.container = QWidget()
            self.container_layout = QHBoxLayout()

            self.container.setLayout(self.container_layout)

            self.user_input_column = QWidget()
            self.user_input_column_layout = QVBoxLayout()
            self.user_input_column.setLayout(self.user_input_column_layout)
            self.container_layout.addWidget(self.user_input_column)


            self.user_output_column = QWidget()
            self.user_output_column_layout = QVBoxLayout()
            self.user_output_column.setLayout(self.user_output_column_layout)
            self.container_layout.addWidget(self.user_output_column)


            self.user_input_row0 = QWidget()
            self.user_input_row0_layout = QHBoxLayout()
            self.user_input_row0.setLayout(self.user_input_row0_layout)
            self.user_input_column_layout.addWidget(self.user_input_row0)

            self.user_input_row1 = QWidget()
            self.user_input_row1_layout = QHBoxLayout()
            self.user_input_row1.setLayout(self.user_input_row1_layout)
            self.user_input_column_layout.addWidget(self.user_input_row1)
            
            self.user_input_row2 = QWidget()
            self.user_input_row2_layout = QHBoxLayout()
            self.user_input_row2.setLayout(self.user_input_row2_layout)
            self.user_input_column_layout.addWidget(self.user_input_row2)

            self.user_input_row3 = QWidget()
            self.user_input_row3_layout = QHBoxLayout()
            self.user_input_row3.setLayout(self.user_input_row3_layout)
            self.user_input_column_layout.addWidget(self.user_input_row3)
            
            self.user_input_row4 = QWidget()
            self.user_input_row4_layout = QHBoxLayout()
            self.user_input_row4.setLayout(self.user_input_row4_layout)
            self.user_input_column_layout.addWidget(self.user_input_row4)

            self.user_input_row5 = QWidget()
            self.user_input_row5_layout = QHBoxLayout()
            self.user_input_row5.setLayout(self.user_input_row5_layout)
            self.user_input_column_layout.addWidget(self.user_input_row5)

            self.user_input_row6 = QWidget()
            self.user_input_row6_layout = QHBoxLayout()
            self.user_input_row6.setLayout(self.user_input_row6_layout)
            self.user_input_column_layout.addWidget(self.user_input_row6)

            self.user_input_row7 = QWidget()
            self.user_input_row7_layout = QHBoxLayout()
            self.user_input_row7.setLayout(self.user_input_row7_layout)
            self.user_input_column_layout.addWidget(self.user_input_row7)

            self.user_input_row8 = QWidget()
            self.user_input_row8_layout = QHBoxLayout()
            self.user_input_row8.setLayout(self.user_input_row8_layout)
            self.user_input_column_layout.addWidget(self.user_input_row8)


            self.ap_aide_labels = QLabel("                                AP   Aide")
            self.user_input_row0_layout.addWidget(self.ap_aide_labels)


            self.g1_label = QLabel("Grade 1:")
            self.g1_dspinbox = QDoubleSpinBox()
            self.g1_isap = QCheckBox()
            self.g1_isaide = QCheckBox()
            self.user_input_row1_layout.addWidget(self.g1_label)
            self.user_input_row1_layout.addWidget(self.g1_dspinbox)
            self.user_input_row1_layout.addWidget(self.g1_isap)
            self.user_input_row1_layout.addWidget(self.g1_isaide)


            self.g2_label = QLabel("Grade 2:")
            self.g2_dspinbox = QDoubleSpinBox()
            self.g2_isap = QCheckBox()
            self.g2_isaide = QCheckBox()
            self.user_input_row2_layout.addWidget(self.g2_label)
            self.user_input_row2_layout.addWidget(self.g2_dspinbox)
            self.user_input_row2_layout.addWidget(self.g2_isap)
            self.user_input_row2_layout.addWidget(self.g2_isaide)
            

            self.g3_label = QLabel("Grade 3:")
            self.g3_dspinbox = QDoubleSpinBox()
            self.g3_isap = QCheckBox()
            self.g3_isaide = QCheckBox()
            self.user_input_row3_layout.addWidget(self.g3_label)
            self.user_input_row3_layout.addWidget(self.g3_dspinbox)
            self.user_input_row3_layout.addWidget(self.g3_isap)
            self.user_input_row3_layout.addWidget(self.g3_isaide)


            self.g4_label = QLabel("Grade 4:")
            self.g4_dspinbox = QDoubleSpinBox()
            self.g4_isap = QCheckBox()
            self.g4_isaide = QCheckBox()
            self.user_input_row4_layout.addWidget(self.g4_label)
            self.user_input_row4_layout.addWidget(self.g4_dspinbox)
            self.user_input_row4_layout.addWidget(self.g4_isap)
            self.user_input_row4_layout.addWidget(self.g4_isaide)



            self.g5_label = QLabel("Grade 5:")
            self.g5_dspinbox = QDoubleSpinBox()
            self.g5_isap = QCheckBox()
            self.g5_isaide = QCheckBox()
            self.user_input_row5_layout.addWidget(self.g5_label)
            self.user_input_row5_layout.addWidget(self.g5_dspinbox)
            self.user_input_row5_layout.addWidget(self.g5_isap)
            self.user_input_row5_layout.addWidget(self.g5_isaide)


            self.g6_label = QLabel("Grade 6:")
            self.g6_dspinbox = QDoubleSpinBox()
            self.g6_isap = QCheckBox()
            self.g6_isaide = QCheckBox()
            self.user_input_row6_layout.addWidget(self.g6_label)
            self.user_input_row6_layout.addWidget(self.g6_dspinbox)
            self.user_input_row6_layout.addWidget(self.g6_isap)
            self.user_input_row6_layout.addWidget(self.g6_isaide)


            self.g7_label = QLabel("Grade 7:")
            self.g7_dspinbox = QDoubleSpinBox()
            self.g7_isap = QCheckBox()
            self.g7_isaide = QCheckBox()
            self.user_input_row7_layout.addWidget(self.g7_label)
            self.user_input_row7_layout.addWidget(self.g7_dspinbox)
            self.user_input_row7_layout.addWidget(self.g7_isap)
            self.user_input_row7_layout.addWidget(self.g7_isaide)


            self.g8_label = QLabel("Grade 8:")
            self.g8_dspinbox = QDoubleSpinBox()
            self.g8_isap = QCheckBox()
            self.g8_isaide = QCheckBox()
            self.user_input_row8_layout.addWidget(self.g8_label)
            self.user_input_row8_layout.addWidget(self.g8_dspinbox)
            self.user_input_row8_layout.addWidget(self.g8_isap)
            self.user_input_row8_layout.addWidget(self.g8_isaide)




            self.user_output_row1 = QWidget()
            self.user_output_row1_layout = QHBoxLayout()
            self.user_output_row1.setLayout(self.user_output_row1_layout)
            self.user_output_column_layout.addWidget(self.user_output_row1)

            self.user_output_row2 = QWidget()
            self.user_output_row2_layout = QHBoxLayout()
            self.user_output_row2.setLayout(self.user_output_row2_layout)
            self.user_output_column_layout.addWidget(self.user_output_row2)

            
            
            self.title_label = QLabel("GPA CALCULATOR")
            self.title_label.setFont(QFont("Helvetica",30))
            self.user_output_row1_layout.addWidget(self.title_label)

            self.calculate_button = QPushButton("Calculate")
            self.calculate_button.setFont(QFont("Helvetica",20))
            self.user_output_row2_layout.addWidget(self.calculate_button)
            self.calculate_button.pressed.connect(self.calculate)

    def calculate(self):
        (self.g1_dspinbox.value()) + (self.g2_dspinbox.value()) + (self.g3_dspinbox.value()) + (self.g4_dspinbox.value()) + (self.g5_dspinbox.value()) + (self.g6_dspinbox.value()) + (self.g7_dspinbox.value()) + (self.g8_dspinbox.value()) 
        



            self.g1_dspinbox.setMaximum(int(4))
            # self.g2_dspinbox.setMaximum(int(4))
            # self.g3_dspinbox.setMaximum(int(4))
            # self.g4_dspinbox.setMaximum(int(4))
            # self.g5_dspinbox.setMaximum(int(4))
            # self.g6_dspinbox.setMaximum(int(4))
            # self.g7_dspinbox.setMaximum(int(4))
            # self.g8_dspinbox.setMaximum(int(4))

            self.g1_dspinbox.setSingleStep(.1)




            # Set the central widget of the Window. Widget will expand
            # to take up all the space in the window by default.
            self.setCentralWidget(self.container)
            #self.calculate_btn = QPushButton(text = "Calculate")
            #self.layout.addWidget(self.calculate_btn)
            #self.calculate_btn.pressed.connect(self.calculate_gpa)


    #def calculate_gpa(self):
                
        #self.gpa_label.setText(str((int(self.gpa1_spinbox.value()) + int(self.gpa2_spinbox.value()) + int(self.gpa3_spinbox.value()) + int(self.gpa4_spinbox.value()) + int(self.gpa5_spinbox.value()) + int(self.gpa6_spinbox.value()) + int(self.gpa7_spinbox.value()) + int(self.gpa8_spinbox.value()))/8)) 



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
