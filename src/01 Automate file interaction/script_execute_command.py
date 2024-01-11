''' Executing terminal commands using subprocess library '''
import subprocess
import sys

if __name__ == '__main__':
    # Check the Python installation path
    print("Python executable path:\n", sys.executable)

    # Run the task
    subprocess.check_call(['python', '.\\src\\01 Automate file interaction\\file_ops.py'])
