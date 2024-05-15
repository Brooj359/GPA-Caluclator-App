"""
This code is done by Jason Brooks. This is a calculator app that calculates GPA based on 8 classes with the guidelines following the Century High School grading guidelines.
Uses PyQt6.
"""


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

            #entire layout is horizontal
            self.container_layout = QHBoxLayout()

            self.container.setLayout(self.container_layout)
            
            #adds input column(right)
            self.user_input_column = QWidget()
            self.user_input_column_layout = QVBoxLayout()
            self.user_input_column.setLayout(self.user_input_column_layout)
            self.container_layout.addWidget(self.user_input_column)

            #adds output column(right)
            self.user_output_column = QWidget()
            self.user_output_column_layout = QVBoxLayout()
            self.user_output_column.setLayout(self.user_output_column_layout)
            self.container_layout.addWidget(self.user_output_column)

            #adds all 9 rows for the right column
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

            #labels for the aide checkboxes
            self.ap_aide_labels = QLabel("                                AP   Aide")
            self.user_input_row0_layout.addWidget(self.ap_aide_labels)


            #Next 8 sections of code contain everything needed for each of the grade inputs. Includes label, double spin box, and checkboxes for aide and ap classes.
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

            #sets maximum value of double spin boxes
            self.g1_dspinbox.setMaximum(int(4))
            self.g2_dspinbox.setMaximum(int(4))
            self.g3_dspinbox.setMaximum(int(4))
            self.g4_dspinbox.setMaximum(int(4))
            self.g5_dspinbox.setMaximum(int(4))
            self.g6_dspinbox.setMaximum(int(4))
            self.g7_dspinbox.setMaximum(int(4))
            self.g8_dspinbox.setMaximum(int(4))

            #sets the amount that each is step increases by for double spin boxes
            self.g1_dspinbox.setSingleStep(.1)
            self.g2_dspinbox.setSingleStep(.1)
            self.g3_dspinbox.setSingleStep(.1)
            self.g4_dspinbox.setSingleStep(.1)
            self.g5_dspinbox.setSingleStep(.1)
            self.g6_dspinbox.setSingleStep(.1)
            self.g7_dspinbox.setSingleStep(.1)
            self.g8_dspinbox.setSingleStep(.1)

            #The following code is the entire output column(right column)

            #next 4 sections of code adds horizontal boxes for each row
            self.user_output_row1 = QWidget()
            self.user_output_row1_layout = QHBoxLayout()
            self.user_output_row1.setLayout(self.user_output_row1_layout)
            self.user_output_column_layout.addWidget(self.user_output_row1)

            self.user_output_row2 = QWidget()
            self.user_output_row2_layout = QHBoxLayout()
            self.user_output_row2.setLayout(self.user_output_row2_layout)
            self.user_output_column_layout.addWidget(self.user_output_row2)

            self.user_output_row3 = QWidget()
            self.user_output_row3_layout = QHBoxLayout()
            self.user_output_row3.setLayout(self.user_output_row3_layout)
            self.user_output_column_layout.addWidget(self.user_output_row3)
            
            self.user_output_row4 = QWidget()
            self.user_output_row4_layout = QHBoxLayout()
            self.user_output_row4.setLayout(self.user_output_row4_layout)
            self.user_output_column_layout.addWidget(self.user_output_row4)

            
            #next four sections of code adds content to each horizontal row
            self.title_label = QLabel("GPA CALCULATOR")
            self.title_label.setFont(QFont("Helvetica",30))
            self.user_output_row1_layout.addWidget(self.title_label)

            self.calculate_button = QPushButton("Calculate")
            self.calculate_button.setFont(QFont("Helvetica",20))
            self.user_output_row2_layout.addWidget(self.calculate_button)
            self.calculate_button.pressed.connect(self.calculate)

            self.gpa_label = QLabel("GPA")
            self.gpa_label.setFont(QFont("Helvetica",20))
            self.user_output_row3_layout.addWidget(self.gpa_label)
            self.gpa_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.grade_label = QLabel(" ")
            self.grade_label.setFont(QFont("Helvetica",30))
            self.user_output_row4_layout.addWidget(self.grade_label)
            self.grade_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setCentralWidget(self.container)
    """
    This function is the calculate function, though it does more, which is activated by pressing the button. It sets the double spin box values as seperate values, accounts 
    for AP and Aide classes, sets the number for the gpa label and sets the letter grade for the grade label.
    """
    def calculate(self):

        #Sets double spin box values to different values that can be manipulated elsewhere
        self.fixed_value1 = self.g1_dspinbox.value()
        self.fixed_value2 = self.g2_dspinbox.value()
        self.fixed_value3 = self.g3_dspinbox.value()
        self.fixed_value4 = self.g4_dspinbox.value()
        self.fixed_value5 = self.g5_dspinbox.value()
        self.fixed_value6 = self.g6_dspinbox.value()
        self.fixed_value7 = self.g7_dspinbox.value()
        self.fixed_value8 = self.g8_dspinbox.value()

        #Checks if a class is AP and adds 1 to its value
        if self.g1_isap.isChecked() == True:
            self.fixed_value1 += 1
        if self.g2_isap.isChecked() == True:
            self.fixed_value2 += 1
        if self.g3_isap.isChecked() == True:
            self.fixed_value3 += 1
        if self.g4_isap.isChecked() == True:
            self.fixed_value4 += 1
        if self.g5_isap.isChecked() == True:
            self.fixed_value5 += 1
        if self.g6_isap.isChecked() == True:
            self.fixed_value6 += 1
        if self.g7_isap.isChecked() == True:
            self.fixed_value7 += 1
        if self.g8_isap.isChecked() == True:
            self.fixed_value8 += 1

        #if a class is an aide class, it is not counted when calculating gpa, so 1 is subtracted from this for every aide class
        self.number_of_classes = 8

        #checks if each grade is Aide, can have mutiple aide classes
        if self.g1_isaide.isChecked() == True:
            self.fixed_value1 = 0
            self.number_of_classes -= 1
        if self.g2_isaide.isChecked() == True:
            self.fixed_value2 = 0
            self.number_of_classes -= 1
        if self.g3_isaide.isChecked() == True:
            self.fixed_value3 = 0
            self.number_of_classes -= 1
        if self.g4_isaide.isChecked() == True:
            self.fixed_value4 = 0
            self.number_of_classes -= 1
        if self.g5_isaide.isChecked() == True:
            self.fixed_value5 = 0
            self.number_of_classes -= 1
        if self.g6_isaide.isChecked() == True:
            self.fixed_value6 = 0
            self.number_of_classes -= 1
        if self.g7_isaide.isChecked() == True:
            self.fixed_value7 = 0
            self.number_of_classes -= 1
        if self.g8_isaide.isChecked() == True:
            self.fixed_value8 = 0
            self.number_of_classes -= 1
        if self.number_of_classes == 0:
            self.number_of_classes = 1

        #Equation to calculate GPA
        self.gpa = round(((self.fixed_value1) + (self.fixed_value2) + (self.fixed_value3) + (self.fixed_value4) + (self.fixed_value5) + (self.fixed_value6) + (self.fixed_value7) + (self.fixed_value8))/self.number_of_classes,2)
        self.gpa_label.setText(str(self.gpa))

        #Determines what letter grade based on GPA
        if self.gpa > 3.2:
            self.grade_label.setText("A")
        if 3.2 > self.gpa > 2.4:
            self.grade_label.setText("B")
        if 2.4 > self.gpa > 1.6:
            self.grade_label.setText("C")
        if 1.6 > self.gpa > .8:
            self.grade_label.setText("D")
        if self.gpa < .8:
            self.grade_label.setText("F")

    
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()