import os, sys, requests, socket
from regex import D

class NotString(Exception):
    def __init__(self):
        
        raise Exception("Following argument is not a string")

class NotNumber(Exception):
    def __init__(self):
        
        raise Exception("Following argument is not a number")

class NotFunction(Exception):
    def __init__(self):


        raise Exception("Following argument is not a function")

def echo(msg: str):
        
    if type(msg) != str:
        raise NotString()
    else:
        print(msg)

def add(num1, num2):
    if type(num1) == int or type(num2) == int or type(num1) == float == type(num2) == float:
        print(num1 + num2)
        return num1 + num2
    else:
        raise NotNumber()

def sub(num1, num2):
    if type(num1) == int or type(num2) == int or type(num1) == float == type(num2) == float:
        print(num1 - num2)
        return num1 - num2
    else:
        raise NotNumber()

def mult(num1, num2):
    if type(num1) == int or type(num2) == int or type(num1) == float == type(num2) == float:
        print(num1 * num2)
        return num1 * num2
    else:
        raise NotNumber()

def div(num1, num2):
    #check if num1 is number and num2 is number
    if type(num1) == int or type(num2) == int or type(num1) == float == type(num2) == float:
        
        print(num1 / num2)
        return num1 / num2
    else:
        raise NotNumber()

def user_input(msg):
    if type(msg) == None:
        return input()
    if type(msg) != str:
        raise NotString()
    else:
        return input(msg)
        
def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def get_ip():
    return requests.get('https://api.ipify.org').text

def get_windows_os_version():
    return os.getenv('OS')

def get_response_code(url):
    return requests.get(url).status_code

def dir_exists(path) -> bool:
    if os.path.isdir(path):
        return True
    else:
        return False
    
def file_exists(path) -> bool:
    if os.path.isfile(path):
        return True
    else:
        return False

def pybatch_version():
    print("PyBatch Center: Version 0.1")

def help():
    print("""
    PyBatch Center: Version 0.1
    ---------------------------------
    Available commands:

    echo <message>
    add <number1> <number2>
    sub <number1> <number2>
    mult <number1> <number2>
    div <number1> <number2>
    user_input <message>
    get_local_ip
    get_ip
    get_windows_os_version
    get_response_code <url>
    dir_exists <path>
    file_exists <path>
    version
    help
    """)








#make command line arguments even with math floats
def main():
    #print(sys.argv)
    if len(sys.argv) == 1:
        print("No arguments")
    else:
        if sys.argv[1] == "echo":
            echo(sys.argv[2])
        elif sys.argv[1] == "add":
            add(float(sys.argv[2]), float(sys.argv[3]))
        elif sys.argv[1] == "sub":
            sub(float(sys.argv[2]), float(sys.argv[3]))
        elif sys.argv[1] == "mult":
            mult(float(sys.argv[2]), float(sys.argv[3]))
        elif sys.argv[1] == "div":
            div(float(sys.argv[2]), float(sys.argv[3]))
        elif sys.argv[1] == "user_input":
            user_input(sys.argv[2])
        elif sys.argv[1] == "get_local_ip":
            print(get_local_ip())
        elif sys.argv[1] == "get_ip":
            print(get_ip())
        elif sys.argv[1] == "get_windows_os_version":
            print(get_windows_os_version())
        elif sys.argv[1] == "get_response_code":
            print(get_response_code(sys.argv[2]))
        elif sys.argv[1] == "dir_exists":
            print(dir_exists(sys.argv[2]))
        elif sys.argv[1] == "file_exists":
            print(file_exists(sys.argv[2]))
        elif sys.argv[1] == "version":
            pybatch_version()
        elif sys.argv[1] == "help":
            help()

        else:
            print("Invalid argument")
if __name__ == "__main__":
    main()