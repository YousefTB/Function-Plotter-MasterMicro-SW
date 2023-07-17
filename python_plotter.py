import sys
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



#=====================================================================================
#MainWindow Class is used to make an object of QMainWindow to create full GUI Window #
#Customized based on the required task                                               #
#Instance of this class creates MainWindow object that used to build the GUI         #
#=====================================================================================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.setWindowTitle("Python Plotter")
        self.resize(800, 600)

        # Create widgets
        self.function_label = QLabel('Enter function:')
        self.function_input = QLineEdit()
        self.xmin_label = QLabel('Enter minimum value of x:')
        self.xmin_input = QLineEdit()
        self.xmax_label = QLabel('Enter maximum value of x:')
        self.xmax_input = QLineEdit()
        self.plot_button = QPushButton('Plot')
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Set layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.create_layout())
        self.setCentralWidget(self.central_widget)

        # Connect button signal to slot
        self.plot_button.clicked.connect(self.plot)

    def create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.xmin_label)
        layout.addWidget(self.xmin_input)
        layout.addWidget(self.xmax_label)
        layout.addWidget(self.xmax_input)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.canvas)
        return layout

    def plot(self):
        # Get user input
        function = self.function_input.text()
        xmin = self.xmin_input.text()
        xmax = self.xmax_input.text()

        # Validate input
        try:
            xmin = float(xmin)
            xmax = float(xmax)
        except ValueError:
            self.canvas.figure.clear()
            self.canvas.draw()
            self.statusBar().showMessage('Error: xmin and xmax must be numbers')
            return
        
        if xmin >= xmax:
            self.canvas.figure.clear()
            self.canvas.draw()
            self.statusBar().showMessage('Error: xmin is greater or equal to xmax')
            return
        
        
        # Create x values
        n_points = round(abs(xmin) + xmax + 1)
        if n_points > 100000:
            n_points = 100000
        
        x = np.linspace(xmin, xmax, n_points)
        
        # add 0 point to x to enhance the output shape
        if xmin < 0:
            x = np.append(x,0)
            x = np.sort(x)

        # Evaluate function
        try:
            y = eval(function.replace('^', '**')) # X variable is defined in line 68 to be evaluated
        except:
            self.canvas.figure.clear()
            self.canvas.draw()
            self.statusBar().showMessage('Error: Invalid Function')
            return
        

        # Normalize all np.inf values to np.nan if exist
        try:
            y[y == np.inf] = np.nan
        except:
            pass
        
        # Avoid empty result of dividing on zero
        try:
            if len(y) == len(y[np.isnan(y)]):
                self.canvas.figure.clear()
                self.canvas.draw()
                self.statusBar().showMessage('Error: Zero Division Exists')
                return
        except:
            pass

        # Clear figure and plot
        self.canvas.figure.clear()
        self.statusBar().showMessage("")
        ax = self.figure.add_subplot(111)
        
        # Handling the constant functions
        try:
            ax.plot(x, y)
        except:
            y = np.full(x.shape, y)
            ax.plot(x, y)
            
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_title('Plot of ' + function)
        self.canvas.draw()


if __name__ == '__main__':
    # Making sure there is no instance (Since using spyder)
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())