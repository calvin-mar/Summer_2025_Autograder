# This code is a prototype for the GUI creation of json using inputted test cases
# Simply run the file, input your test cases and tasks and click make_lab to produce the json file
# This code needs stress testing before use most likely. Currently it definitely breaks if there is an empty function name, function location, or other certain fields
# Calvin Mar

import sys
import ast
import json


from PyQt6.QtCore import QSize, Qt, QRect, pyqtSlot, QThreadPool, QObject, QThread, pyqtSignal, QTimer
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication
import PyQt6.QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QColor, QPalette

# This is the main window. It sets everything up, yay.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize scroll area and other window attributes
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('Lab Creator')

        # This is the test_list, which contains the list of Test objects
        self.test_list = []

        # This is the tests int, which is the number of tests, it is also used to place tests in the correct index within the QVBoxLayout
        self.tests = 0

        # This the tasks int, which is the number of tasks
        self.tasks = 0
        
        # Set up first Box
        self.layout = QVBoxLayout()
        self.header = QHBoxLayout()
        self.make_lab_button = QPushButton("Make Lab")
        self.make_lab_button.setCheckable(True)
        self.lab_name = QLineEdit(self)
        self.lab_name.setPlaceholderText("Enter the name of the lab here...")
        self.make_lab_button.clicked.connect(self.make_lab)
        self.header.addWidget(self.lab_name)
        self.header.addWidget(self.make_lab_button)
        #Add first box to layout
        temp_widget = QWidget()
        temp_widget.setLayout(self.header)
        self.layout.addWidget(temp_widget)

        # Call the add_one_task method 
        self.add_one_task()
        
        ## Add buttons
        self.addTest = QPushButton("Add Test")
        self.addTest.setCheckable(True)
        self.addTask = QPushButton("Add Task")
        self.addTask.setCheckable(True)
        self.addTest.clicked.connect(self.add_one_test)
        self.addTask.clicked.connect(self.add_one_task)
        buttons = QHBoxLayout()
        buttons.addWidget(self.addTask)
        buttons.addWidget(self.addTest)
        buttonWidget = QWidget()
        buttonWidget.setLayout(buttons)
        self.layout.addWidget(buttonWidget)
        
        #######
        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.scroll.setWidget(centralWidget)
        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
      
        self.setCentralWidget(self.scroll)
        self.show()
        
    def make_lab(self):
        '''
        This function is connected to the make_lab button
        It gathers information from all Test Objects and compiles the dictionary from them and writes it to the file
        '''
        print("Making lab_" + str(self.lab_name.text()) + "_testFile.json")
        dictionary = {}
        testSets = {}
        modules = []
        for test in self.test_list:
            num, task, test_dict = test.get_info()
            test_keys = test_dict.keys()
            if("special" in test_keys):
                modules.append(test_dict["special"]["functionLocation"])
            if(task in testSets.keys()):
                testSets[task] += 1
            else:
                testSets[task] = 1
            dictionary[num] = test_dict
        dictionary["modules"] = modules
        
        testSetsList = []
        for i in range(self.tasks):
            testSetsList.append(testSets[str(i+1)])
        dictionary["testSets"] = testSetsList

        filename = "lab_" + str(self.lab_name.text()) + "_testFile.json"
        with open(filename, "w") as f:
            json.dump(dictionary, f, indent=4)

    def add_one_task(self):
        '''
        This function is connected to the add_task button
        Adds one to the task count and adds a test
        '''
        self.tasks += 1
        self.add_one_test()
        
    def add_one_test(self):
        '''
        This function is connected to the add_test button
        Adds one to the test count and creates an instance of the Test class to display
        This function also establishes the necessary connections between delete buttons so that all is properly updated
        '''
        self.tests += 1
        testWidget = Test(self.tests, self.tasks)
        for test in self.test_list:
            test.connections.append(testWidget.del_button.clicked.connect(lambda: test.update_num(testWidget.testNum)))
            testWidget.connections.append(test.del_button.clicked.connect(lambda: testWidget.update_num(test.testNum)))
            
        testWidget.del_button.clicked.connect(lambda: self.delete_test(testWidget.testNum))
        self.layout.insertWidget(self.tests,testWidget)
        self.test_list.append(testWidget)

    def delete_test(self, testNum):
        '''
        This function removes a test from the display window
        This includes disconnecting the test to be removed from all other Test objects
        '''
        self.tests -= 1
        del self.test_list[testNum-1]
        item_to_del = self.layout.takeAt(testNum)
        widget_to_del = item_to_del.widget()
        for connection in widget_to_del.connections:
            QObject.disconnect(connection)
        widget_to_del.deleteLater()
        self.layout.update()

class Test(QWidget):
    '''
    This class organizes a single test
    '''
    def __init__(self, tests, tasks):
        super().__init__()
        self.testNum = tests
        self.taskNum = tasks
        self.origin = tests
        self.connections = []

        self.layout = QVBoxLayout()
        # Display Tests and Tasks
        header_line = QHBoxLayout()
        button_set = QHBoxLayout()
        button_set.setSpacing(0)
        task_label = QLabel()
        task_label.setText("<font size = 8><b><u>Task " + str(self.taskNum) + "</u></b></font>")
        button_set.addWidget(task_label)
        
        self.minus_button = QPushButton("-")
        self.minus_button.setFixedSize(20, 20)
        self.plus_button = QPushButton("+")
        self.plus_button.setFixedSize(20,20)

        self.minus_button.clicked.connect(self.minusTask)
        self.plus_button.clicked.connect(self.plusTask)
        
        button_set.addWidget(self.minus_button)
        button_set.addWidget(self.plus_button)
        button_set.addStretch()
        buttonSetWidget = QWidget()
        buttonSetWidget.setLayout(button_set)


        header_line.addWidget(buttonSetWidget)
        header_line.addWidget(QLabel())
        test_label = QLabel()
        test_label.setText("<font size = 8><b><u>Test " + str(self.testNum) + "</u></b></font>")
        header_line.addWidget(test_label)
        header_line.addWidget(QLabel())
        header_line.addWidget(QLabel())
        header_line.addStretch()
        self.headerWidget = QWidget()
        self.headerWidget.setLayout(header_line)
        self.layout.addWidget(self.headerWidget)
        


        # Function Name Line
        name_line = QHBoxLayout()
        name_label = QLabel()
        name_label.setText("Function Name:")
        name_line.addWidget(name_label)
        self.name_text = QLineEdit(self)
        self.name_text.setPlaceholderText("Enter the name of the function here...")
        name_line.addWidget(self.name_text)
        self.del_button = QPushButton("Delete Test")
        name_line.addWidget(self.del_button)
        nameWidget = QWidget()
        nameWidget.setLayout(name_line)
        self.layout.addWidget(nameWidget)

        # Function Inputs Line
        inputs_line = QHBoxLayout()
        inputs_label = QLabel()
        inputs_label.setText("Function Inputs:")
        inputs_line.addWidget(inputs_label)
        self.inputs_text = QLineEdit(self)
        self.inputs_text.setPlaceholderText("Enter the inputs for the function as called by 'input' as a list here...")
        inputs_line.addWidget(self.inputs_text)
        inputsWidget = QWidget()
        inputsWidget.setLayout(inputs_line)
        self.layout.addWidget(inputsWidget)

        # Function Parameters Line
        parameters_line = QHBoxLayout()
        parameters_label = QLabel()
        parameters_label.setText("Function Parameters:")
        parameters_line.addWidget(parameters_label)
        self.parameters_text = QLineEdit(self)
        self.parameters_text.setPlaceholderText("Enter the parameters to be passed to the function as a list here...")
        parameters_line.addWidget(self.parameters_text)
        parametersWidget = QWidget()
        parametersWidget.setLayout(parameters_line)
        self.layout.addWidget(parametersWidget)

        # Toggle Output Line
        toggle_line = QHBoxLayout()
        toggle_label = QLabel()
        toggle_label.setText("Needs external testing function? ")
        toggle_line.addWidget(toggle_label)
        self.toggle_box = QCheckBox("")
        self.toggle_box.stateChanged.connect(self.toggle_comparator)
        toggle_line.addWidget(self.toggle_box)
        toggle_line.addWidget(QLabel())
        toggle_line.addWidget(QLabel())
        toggle_widget = QWidget()
        toggle_widget.setLayout(toggle_line)
        self.layout.addWidget(toggle_widget)

        # Add a line
        line = QHBoxLayout()
        

        # Comparator
        ## The Comparator is a separate class so that it is easily toggleable between a simple output and external testing function
        self.comparator_widget = Comparator(self.toggle_box)
        self.layout.addWidget(self.comparator_widget)
        
        self.setLayout(self.layout)

    def toggle_comparator(self):
        '''
        This function toggles the comparator section, by remoing the old version and creating a new instance
        '''
        self.layout.removeWidget(self.comparator_widget)
        self.comparator_widget.setParent(None)
        
        self.comparator_widget = Comparator(self.toggle_box)
        self.layout.addWidget(self.comparator_widget)
        
        self.setLayout(self.layout)
        self.update()

    def update_num(self, otherNum):
        '''
        This function is called when another test is deleted
        It updates this Test as necessary
        '''
        if(otherNum < self.testNum):
            self.testNum -= 1
            self.remake_header()
            
    def minusTask(self):
        if(self.taskNum > 1):
            self.taskNum -= 1
            self.remake_header()

    def plusTask(self):
        self.taskNum += 1
        self.remake_header()
        
    def remake_header(self):
        self.layout.removeWidget(self.headerWidget)
        self.headerWidget.setParent(None)

        header_line = QHBoxLayout()
        button_set = QHBoxLayout()
        button_set.setSpacing(0)
        task_label = QLabel()
        task_label.setText("<font size = 8><b><u>Task " + str(self.taskNum) + "</u></b></font>")
        button_set.addWidget(task_label)
        
        self.minus_button = QPushButton("-")
        self.minus_button.setFixedSize(20, 20)
        self.plus_button = QPushButton("+")
        self.plus_button.setFixedSize(20,20)

        self.minus_button.clicked.connect(self.minusTask)
        self.plus_button.clicked.connect(self.plusTask)
        
        button_set.addWidget(self.minus_button)
        button_set.addWidget(self.plus_button)
        button_set.addStretch()
        buttonSetWidget = QWidget()
        buttonSetWidget.setLayout(button_set)


        header_line.addWidget(buttonSetWidget)
        header_line.addWidget(QLabel())
        test_label = QLabel()
        test_label.setText("<font size = 8><b><u>Test " + str(self.testNum) + "</u></b></font>")
        header_line.addWidget(test_label)
        header_line.addWidget(QLabel())
        header_line.addWidget(QLabel())
        header_line.addStretch()
        self.headerWidget = QWidget()
        self.headerWidget.setLayout(header_line)
        self.layout.insertWidget(0, self.headerWidget)

        self.setLayout(self.layout)
        self.update()

    def get_info(self):
        '''
        This method returns the test number, task number, and dictionary corresponding to this test
        '''
        dictionary = {}
        dictionary["functionName"] = ast.literal_eval('"' +str(self.name_text.text())+'"')
        
        input_string = str(self.inputs_text.text())
        if input_string == "":
            dictionary["inputs"] = []
        else:
            dictionary["inputs"] = ast.literal_eval(input_string)
            if(type(dictionary["inputs"]) != list):
                dictionary["inputs"] = [dictionary["inputs"]]
                
        parameter_string = str(self.parameters_text.text())
        if parameter_string == "":
            dictionary["parameters"] = []
        else:
            dictionary["parameters"] = ast.literal_eval(parameter_string)
            if(type(dictionary["parameters"]) != list):
                dictionary["parameters"] = [dictionary["parameters"]]
    
        key, value = self.comparator_widget.get_info()
        dictionary[key] = value
        return str(self.testNum),str(self.taskNum), dictionary


class Comparator(QWidget):
    '''
    This comparator class has two init states depending on the state of the QCheckBox
    '''
    def __init__(self, box):
        super().__init__()
        self.box = box
        if(self.box.isChecked()):
            self.specialInit()
        else:
            self.regularInit()
            
    def specialInit(self):
        '''
        This function provides the parameter boxes for external function testing
        '''
        comparator_layout = QVBoxLayout()

        # Function Location Line
        location_line = QHBoxLayout()
        location_label = QLabel()
        location_label.setText("External Function Module Name:")
        location_line.addWidget(location_label)
        self.location_text = QLineEdit(self)
        self.location_text.setPlaceholderText("Enter the name of the external module for the function here...")
        location_line.addWidget(self.location_text)
        locationWidget = QWidget()
        locationWidget.setLayout(location_line)
        comparator_layout.addWidget(locationWidget)

        # Function Name Line
        name_line = QHBoxLayout()
        name_label = QLabel()
        name_label.setText("External Function Name:")
        name_line.addWidget(name_label)
        self.name_text = QLineEdit(self)
        self.name_text.setPlaceholderText("Enter the name of the external function here...")
        name_line.addWidget(self.name_text)
        nameWidget = QWidget()
        nameWidget.setLayout(name_line)
        comparator_layout.addWidget(nameWidget)

        # Function Parameters Line
        parameters_line = QHBoxLayout()
        parameters_label = QLabel()
        parameters_label.setText("Function Parameters:")
        parameters_line.addWidget(parameters_label)
        self.parameters_text = QLineEdit(self)
        self.parameters_text.setPlaceholderText("Enter the parameters to be passed to the external function as a list here...")
        parameters_line.addWidget(self.parameters_text)
        parametersWidget = QWidget()
        parametersWidget.setLayout(parameters_line)
        comparator_layout.addWidget(parametersWidget)

        self.setLayout(comparator_layout)
        
    def regularInit(self):
        '''
        This function provides the input box for only comparatory ouput testing
        '''
        wrapper_layout = QVBoxLayout()
        output_line = QHBoxLayout()
        output_label = QLabel()
        output_label.setText("Expected Outpus:")
        output_line.addWidget(output_label)
        self.output_text = QLineEdit(self)
        self.output_text.setPlaceholderText("Enter the expected Output here...")
        output_line.addWidget(self.output_text)
        wrapper_widget = QWidget()
        wrapper_widget.setLayout(output_line)
        wrapper_layout.addWidget(wrapper_widget)
        self.setLayout(wrapper_layout)
        
    def get_info(self):
        '''
        This function returns the key, value pair for the comparator section
        '''
        if(self.box.isChecked()):
            dictionary = {}
            dictionary["functionLocation"] = ast.literal_eval('"' + str(self.location_text.text()) + '"')
            dictionary["functionName"] = ast.literal_eval('"' + str(self.name_text.text()) + '"')

            
            parameter_string = str(self.parameters_text.text())
            if parameter_string == "":
                dictionary["parameters"] = []
            else:
                dictionary["parameters"] = ast.literal_eval(parameter_string)
                if(type(dictionary["parameters"]) != list):
                    dictionary["parameters"] = [dictionary["parameters"]]
            return "special", dictionary
            
        else:
            return "output", ast.literal_eval(str(self.output_text.text()))
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
