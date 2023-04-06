def write(curSerial):
    with open("serial", "w") as fh:
        fh.write(str(curSerial))

def read():
    try:
        with open("serial", "r") as fh:
            return fh.read()
    except FileNotFoundError:
        return ""
