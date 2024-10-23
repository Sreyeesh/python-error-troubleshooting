# Python Troubleshooting Toolkit

Welcome to the **Python Troubleshooting Toolkit**! This project is designed to help you practice and enhance your debugging skills in Python by identifying and fixing intentional bugs in various functions.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Running the Toolkit](#running-the-toolkit)
4. [How to Use](#how-to-use)
5. [Features](#features)
6. [Contributing](#contributing)

## Project Overview

The Python Troubleshooting Toolkit consists of several functions with intentional bugs. Your task is to run the toolkit, identify the bugs, and fix them. This hands-on practice will help you understand error messages and improve your debugging skills.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

## Running the Toolkit

1. **Open your Terminal**:  
   Make sure you're in the project directory.

2. **Run the Toolkit**:  
   Execute the following command:
   ```bash
   python troubleshooting_toolkit.py
   ```

## How to Use

1. **Understand the Functions**:  
   Review each function in the toolkit. Each function contains intentional bugs that you need to identify and fix.

2. **Identify Bugs**:  
   Run the script and observe the output. Each function is tested with specific cases that may raise errors.

3. **Fix the Bugs**:  
   Modify the code directly in `troubleshooting_toolkit.py` to handle the errors gracefully. You can implement error handling or correct the logic.

4. **Test Your Fixes**:  
   Rerun the toolkit after making changes to see if your fixes work. Check the output for any remaining errors.

5. **Review the Log**:  
   Any errors encountered during execution will be logged in `troubleshooting.log`. Review this file to analyze the errors.

## Features

- **sum_list**: Intentionally fails with a `TypeError` when summing a list containing non-integer types.
- **divide_numbers**: Raises a `ZeroDivisionError` when attempting to divide by zero.
- **get_value**: Raises a `KeyError` if a specified key is not found in a dictionary.
- **factorial**: Fails with infinite recursion for negative input values.
- **is_palindrome**: Checks if a string is a palindrome but should ignore case differences.

## Contributing

Feel free to modify the functions, add new test cases, or enhance the toolkit in any way! Contributions are welcome. If you have suggestions or improvements, consider creating a pull request.

---

Happy debugging! Enjoy the learning experience with the Python Troubleshooting Toolkit.

