# external_library_error_example.py

import pandas as pd

# This will throw a FileNotFoundError because the file does not exist.
df = pd.read_csv("non_existent_file.csv")  # FileNotFoundError: [Errno 2] No such file or directory
