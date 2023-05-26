import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title Test")

        # Set (V)ertical Layout
        self.setLayout(qtw.QVBoxLayout())

        #Create label
        my_label = qtw.QLabel("TESTING LABEL")
        
        #Change font size label
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)

        self.show()


app = qtw.QApplication([])
main_window = MainWindow()

app.exec_()
