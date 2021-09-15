# Install X-dist to execute the tests in parallel using Pytest - pip inatsll pytest-xdist
# This executor is created for question number 4
import os

os.chdir("C:\\Users\Raj\PycharmProjects\PythonFramework\\test_Exam")
os.system("pytest -s -n=2")