# IT244 Unit 8 Assignment: Working With Python System Interfaces

Outcomes addressed in this assignment:

### Unit Outcome:

Demonstrate the various system interface tasks.

### Course Outcome:

**IT244-3**: Examine Python versions, available system interfaces, built-in tools, and user-defined modules.

### Purpose

In this assignment, you will explore the sys, os, and subprocess modules in Python. You will execute a variety of basic functions in these modules that interface with the operating system. While the functions in these modules can be used in a program, for this assignment, you will take the opportunity to execute these commands directly in the Python shell.

## Assignment Requirements

Using the Python shell, execute the following functions. You will take screenshots at key points to show the successful execution. These will be placed in a single Word document. Recommended screenshot points are listed within the assigned functions, but you may add screenshots if necessary, to show the successful completion of the assignment. (Hint: Under Windows, some of these functions will accept a single backslash in a file path, while others require double backslash between folders.)

## Assignment Instructions

1. In the Python shell, first import the `sys`, `os`, and `subprocess` modules.

	- `Refer to the following Python documentation for more on importing modules`:  Python Software Foundation. [The import system](https://docs.python.org/3/reference/import.html).

2. Execute `os.getlogin()`

	- *Refer to Python Software Foundation*. [Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html#module-os).

3. Execute `os.get_exec_path()`

	- *Refer to Python Software Foundation*. [Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html#module-os).  

4. Take a screenshot.

5. Execute `sys.path`

	- *Refer to Python Software Foundation*. S[ystem-specific parameters and functions](https://docs.python.org/3/library/sys.html#module-sys)

6. Execute `sys.byteorder`

	- *Refer to Python Software Foundation*. [System-specific parameters and functions](https://docs.python.org/3/library/sys.html#module-sys).

7. Take a screenshot.

8. Execute `os.listdir` on your C: drive

	- *Refer to Python Software Foundation*. [Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html#module-os).  

9. Use `os.mkdir` to make a new folder on your C: drive named `tempPython`

	- *Refer to Python Software Foundation*. [Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html#module-os).   

10. Take a screenshot.

11. Use `subprocess.Popen` to execute the Windows dir command and have its output placed in a text file named `pythonOut.txt` 
	- *Hint*: The argument for `Popen` in this case will be `('C:\\windows\\system32\\cmd.exe "/c dir C:\\ >> C:\\pythonOut.txt"')`

	- *Refer to Python Software Foundation*. [Subprocess management](https://docs.python.org/3/library/subprocess.html).    

12. Open `pythonOut.txt` in Notepad and position that window next to the Python shell window where both can be seen.

13. Take a screenshot.

14. Use `subprocess.Popen` to open Windows `calc.exe` utility

	- *Refer to Python Software Foundation*. [Subprocess management](https://docs.python.org/3/library/subprocess.html).

15. Take a screenshot.

### Directions for Submitting Your Assignment

Submit a single document containing all screenshots named `IT244_YourLastName_Unit8.docx`. 