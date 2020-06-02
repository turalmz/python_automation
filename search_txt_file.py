import os


def iter_dir(name):
    for file in os.listdir(name):
        try :
            iter_dir(os.path.join(name, file))
            print(os.path.join(name, file))
        except:
            if file.endswith(".txt"):
                print(os.path.join(name, file))


iter_dir(".")
