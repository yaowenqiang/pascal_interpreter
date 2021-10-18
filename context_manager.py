import sys

from contextlib import contextmanager
from contextlib import redirect_stdout


@contextmanager

def print_writer(file_path):
    original_stdout = sys.stdout
    with open(file_path, "w") as f:
        sys.stdout = f
        yield
        sys.stdout = original_stdout

def context_redirect_stdout():
    with open("this.txt", "w") as file:
        with redirect_stdout(file):
            import this

    with open("this.txt") as file:
        print(file.read())

with print_writer("myfile.txt"):
    print("Printing straight to the file!")
    for i in range(5):
        print(i)
print("and regular print still works")




