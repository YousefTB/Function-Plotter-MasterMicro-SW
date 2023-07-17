# Function-Plotter-MasterMicro-SW
**This repo contains the Master Micro's Software Engineering Task as part of Summer Internship**

## Table of Content
You can use the table of the content to surf the documentation of the task

- [Introduction](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/tree/main#introduction)
- [Proposed Work](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/tree/main#proposed-work)
- [Functionality](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/tree/main#functionality)
- [Constraints](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/tree/main#constraints)
- [Examples](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/tree/main#examples)

## Introduction
This repo includes the Task required by **Master Micro** that is creating `Function Plotter` desktop application using Python with PySide2 package based on `Qt Framework` , so This repo is considered as the Deliverables of the Task

## Proposed Work
1- This program is implemented using `Python 3.11.3` with `Anaconda Platform` in `Spyder IDE` and with the use of `Qt Framework` as mentioned in the task.
> 8. You must use Pyside2 and Matplotlib.

2- All specification of the program maybe clear inside the code such as `Size of the Window`,`Window Title` and Used Widgets and how it is organized
> 5. The GUI should be simple and beautiful (well organized).

3- The code contains comments for important sections and all ambiguous lines are avoided as much a possible to deliver a clean code, with adding ***docstring*** for the `MainWindow Class` that creates the GUI to explain the use of it.
> 11. Your code should be well organized and well documented.

4- The testing code is made in `main_test.py` that contains multiple automated testcases to test the GUI functionality and features and validating inputs using `pytest` and `pytest-qt` as required in the task.
> 10. Create automated tests for your program using pytest and pytest-qt. Perform end-to-end testing for some of the program main features. Include the testing codes in your repository.

5- With the use of `matplotlib` library to plot the function specified by the user and embedding it into the GUI with `PySide2`

![](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/ae8fdc4f-0a61-43d2-8bc3-1ca7ee6e1161)

*Figure 1: Matplotlib plotting of a function*
> 9. The Matplotlib figure must be embedded in the Pyside2 application.


***End of [Proposed Work](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/tree/main#proposed-work) Section***

## Functionality
The application consists of Input text to enter the function by user. **Note that** the only supported operands `+-/*^` only and with parenthesis as required in the task document, with an Input texts for the user to enter the Minimum and Maximum value of `x` to evaluate and plot with applying some constraints.

![image](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/c454897d-ba4b-4ff6-9f21-1fcf527ab882)

*Figure 2: Input texts to enter the specified function, minimum and maximum values of x*

The `Plot` button whenever clicked the program takes the inputs entered into text slots and apply validations to make sure nothing is wrong, then plotting the function with the range of specified values of x variable

![image](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/caa8ac01-a16e-4b2b-adce-c50b49de839a)

*Figure 3: `Plot` button to plot the function*

***End of [Functionality](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/tree/main#functionality) Section***

## Constraints
There are some constraints on the inputs, such as **Other operands than `+-*/^` and parenthesis will not be allowed**, non-numeric values for x variable and the minimum value cannot be greater than or equal (since it is function plotter rather than point) to the maximum value.

Additionaly, any other variables than x in the function/equation are considered invalid input since the relation of plot is between x and y. also, Completely division by zero is not allowed, for functions like $`\frac{5x^2 - x}{3^2 - 9}`$ is prevented.

All these constraints are handled with ***Showing an error message in the menubar*** for the user

![image](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/86d4e3e8-a54e-428e-9cb8-4b53364e241e)

*Figure 4: Invalid function that have warned in the menu bar*

***End of [Constraints](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/tree/main#constraints) Section***

## Examples

This section contains multiple examples and `snapshots` of the results as required with working and wrong examples.
> 2. In your repository, include a readme file and snapshots of working and wrong examples.

### Example 1

![image](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/fb1a30f5-def9-4a1d-8cf3-3d6e62ccb290)

*Figure 5: Example 1 with the function $`5x^3 + 2x`$ with range of values between -10 and 10 inclusive*

### Example 2

![image](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/1475ece2-48aa-4568-b677-a4d31256cd90)

*Figure 6: Example 2 with the function $`\frac{x + 21 ^ x}{0}`$ with range of value between 21 and 39 inclusive*

### Example 3

![image](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/e80672aa-3cb3-4305-b1ca-3ec9746df4c1)

*Figure 7: Example 3 with invalid function type*

### Example 4

![image](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/154a8700-1483-4743-a3ec-1242f60c1198)

*Figure 8: Example 4 with invalid type of inputs for x values*

### Example 5

![image](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/46a8402d-4403-41d2-869c-8f080df922d0)

*Figure 9: Example 5 with Complex function and high range of values for x*

### Example 6

![image](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/assets/95775013/bd40d05f-b3a8-472e-9114-3be56c3ff45f)

*Figure 10: Example 6 with the function $`\frac{9}{3x}`$ with float range of values between -82.5 and 100*


Note that there are more multiple testcases in `main_test.py`

***End of [Examples](https://github.com/YousefTB/Function-Plotter-MasterMicro-SW/tree/main#examples) Section***

# **End of the File**
