import sys
import pytest
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore
from python_plotter import MainWindow


@pytest.fixture
def gui(qtbot):
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        
    window = MainWindow()
    qtbot.addWidget(window)
    qtbot.wait_for_window_shown(window)
    yield window
    window.close()
    

def test_plot_linear_function(gui, qtbot):
    # Test plot output for a simple linear function
    qtbot.keyClicks(gui.function_input, '2*x + 1')
    qtbot.keyClicks(gui.xmin_input, '-5')
    qtbot.keyClicks(gui.xmax_input, '5')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()
    

def test_input_validation_invalid_function(gui, qtbot):
    # Test invalid function input
    qtbot.keyClicks(gui.function_input, '5x**z')
    qtbot.keyClicks(gui.xmin_input, '0')
    qtbot.keyClicks(gui.xmax_input, '1')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == 'Error: Invalid Function'
    assert not gui.canvas.figure.gca().has_data()
    

def test_input_validation_non_numeric_xmin_xmax(gui, qtbot):
    # Test invalid xmin and xmax inputs
    qtbot.keyClicks(gui.function_input, 'x^2')
    qtbot.keyClicks(gui.xmin_input, 'a')
    qtbot.keyClicks(gui.xmax_input, 'b')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == 'Error: xmin and xmax must be numbers'
    assert not gui.canvas.figure.gca().has_data()
    

def test_plot_validation_xmin_is_greater(gui, qtbot):
    # Test invalid xmin and xmax inputs that is xmin is greater
    qtbot.keyClicks(gui.function_input, 'x^2')
    qtbot.keyClicks(gui.xmin_input, '20')
    qtbot.keyClicks(gui.xmax_input, '-12')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == 'Error: xmin is greater or equal to xmax'
    assert not gui.canvas.figure.gca().has_data()
    

def test_decimal_input_values(gui, qtbot):
    # Test plot output for input values with decimal places
    qtbot.keyClicks(gui.function_input, '2^x')
    qtbot.keyClicks(gui.xmin_input, '-1.5')
    qtbot.keyClicks(gui.xmax_input, '1.5')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()
    

def test_large_input_values(gui, qtbot):
    # Test plot output for a large range of input values
    qtbot.keyClicks(gui.function_input, 'x^3 + 4*x^2 + 3*x + 2')
    qtbot.keyClicks(gui.xmin_input, '-100000')
    qtbot.keyClicks(gui.xmax_input, '100000')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()
    

def test_zero_division(gui, qtbot):
    # Test invalid function that contains division on zero
    qtbot.keyClicks(gui.function_input, 'x + 21 ^ x / 0')
    qtbot.keyClicks(gui.xmin_input, '21')
    qtbot.keyClicks(gui.xmax_input, '39')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == 'Error: Zero Division Exists'
    assert not gui.canvas.figure.gca().has_data()
    
def test_complex_function(gui, qtbot):
    # Test complex function
    qtbot.keyClicks(gui.function_input, '(x ^ 3 / 10 ^ x) + 49 * x - x ^ 2 + (x ^ (1/2))')
    qtbot.keyClicks(gui.xmin_input, '-1395')
    qtbot.keyClicks(gui.xmax_input, '9321')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()


def test_mix_of_invalids(gui, qtbot):
    # Test mix of invalid input xmin and xmax and invalid function
    qtbot.keyClicks(gui.function_input, 'x+23/dmcxzlqls.fg')
    qtbot.keyClicks(gui.xmin_input, 'abcdj1i3k499293949l')
    qtbot.keyClicks(gui.xmax_input, 'yoamzl12945i3edfjjdsf')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == 'Error: xmin and xmax must be numbers'
    assert not gui.canvas.figure.gca().has_data()
    
def test_toy_function1(gui, qtbot):
    qtbot.keyClicks(gui.function_input, 'x^-10/(x*21^2)')
    qtbot.keyClicks(gui.xmin_input, '-2139490')
    qtbot.keyClicks(gui.xmax_input, '2339911')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()
    
def test_toy_function2(gui, qtbot):
    qtbot.keyClicks(gui.function_input, '(x/19)^(2*x)')
    qtbot.keyClicks(gui.xmin_input, '-5')
    qtbot.keyClicks(gui.xmax_input, '92129')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()
    
def test_toy_function3(gui, qtbot):
    qtbot.keyClicks(gui.function_input, '102')
    qtbot.keyClicks(gui.xmin_input, '-9129049')
    qtbot.keyClicks(gui.xmax_input, '3993955869921')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()
    
def test_toy_function4(gui, qtbot):
    qtbot.keyClicks(gui.function_input, 'x^9/((1/x)^-2)')
    qtbot.keyClicks(gui.xmin_input, '93')
    qtbot.keyClicks(gui.xmax_input, '552')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()
    
def test_toy_function5(gui, qtbot):
    qtbot.keyClicks(gui.function_input, '5/(9-(x^3))')
    qtbot.keyClicks(gui.xmin_input, '93')
    qtbot.keyClicks(gui.xmax_input, '552')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()
    
def test_toy_function5(gui, qtbot):
    qtbot.keyClicks(gui.function_input, '(29 - (x - 4)^2)^(1/2) - 3')
    qtbot.keyClicks(gui.xmin_input, '-10')
    qtbot.keyClicks(gui.xmax_input, '10')
    qtbot.mouseClick(gui.plot_button, QtCore.Qt.LeftButton)
    assert gui.statusBar().currentMessage() == ''
    assert gui.canvas.figure.gca().has_data()