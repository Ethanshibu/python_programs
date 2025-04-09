import os


def current_dir():
    cwd = os.getcwd()
    print(cwd)


def file_path(fname):
    path = os.path.abspath(fname)
    print(path)

    
current_dir()
fname = "samplescriptingbysimplilearn.py"
file_path(fname)
