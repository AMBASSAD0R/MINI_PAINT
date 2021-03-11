import os.path


def error_2(name_file):
    if not os.path.isfile(name_file):
        print("ERROR: name file\n")
