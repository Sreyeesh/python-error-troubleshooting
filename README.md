

# Python Error Troubleshooting

This repository contains Python code examples that demonstrate common Python errors and their solutions. Each script showcases how to trigger an error and provides explanations for fixing them. This project is intended to help learners understand error messages and improve their debugging skills.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed. You can download it from the official [Python website](https://www.python.org/downloads/).
- **pandas**: Required for running `external_library_error_example.py`. You can install it using pip:
  ```bash
  pip install pandas
  ```

### Running the Examples Locally

1. Clone the repository and navigate to the `code` directory.
2. Install any dependencies (if required).
3. Run each script individually using Python.

## Code Examples

Each script demonstrates a different Python error and how to fix it.

- **index_error_example.py**: Demonstrates an `IndexError` when trying to access a list index that is out of range.
- **syntax_error_example.py**: Demonstrates a `SyntaxError` due to a missing colon in a loop.
- **type_error_example.py**: Demonstrates a `TypeError` when trying to concatenate a string and an integer.
- **value_error_example.py**: Demonstrates a `ValueError` when trying to convert an invalid string to an integer.
- **zero_division_error_example.py**: Demonstrates a `ZeroDivisionError` when dividing by zero, and how to debug it using print statements.
- **pdb_debugging_example.py**: Demonstrates how to use the Python debugger (`pdb`) to inspect and step through the code.
- **external_library_error_example.py**: Demonstrates a `FileNotFoundError` using the `pandas` library when attempting to read a non-existent file.
  
### Troubleshooting Exercises

In addition to error demonstrations, this repository includes troubleshooting exercises designed to improve your debugging skills. Each exercise presents a coding problem with intentional bugs. 

- **exercise_1_sum_list.py**: Identifies and fixes bugs related to summing a list that may contain non-integer types.
- **exercise_2_divide_numbers.py**: Handles division by zero and demonstrates proper error management.
- **exercise_3_get_value.py**: Correctly retrieves values from a dictionary, managing cases where keys may not exist.
- **exercise_4_factorial.py**: Computes the factorial of a number while handling negative input gracefully.
- **exercise_5_is_palindrome.py**: Checks if a string is a palindrome, ignoring case differences.

## Example Fixes

For each script, fixes are applied in the comments to help learners understand how to correct the errors. Be sure to review the code and try fixing the errors yourself before viewing the solutions.

