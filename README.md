# pynnn
Python wrapper for the n³ terminal manager (query mode)
Allows you to select files using the n³ terminal interface
and access the file path in python as a pathlib.Path object.

Usage is as follows:
```python
from pynnn import PyNNN

nnn = PyNNN()
selected_file_path: Path = nnn()
```