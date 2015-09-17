import os
targ_file = ''
import importlib
import time
from threading import Thread
def getTarg(file):
    for x in file:
        if x == '.':
            file.replace(".", "\.")
    global targ_file
    targ_file = str(file)
    print(targ_file)
    print(file)
    imported = importlib.import_module(targ_file + '.py', package=None)
    

def backgroundRun():
    try:
        with open(targ_file + '.py', "r") as myfile:
            data=myfile.read().replace('\n','')
        myfile.close()
        targ_file.__main__()
        print('try')
        while True:
            with open(targ_file + '.py', "r") as myfile:
                data1=myfile.read().replace('\n','')
            myfile.close()
            if data1 != data:
                with open(targ_file + '.py', "r") as myfile:
                    data2 = myfile.read().replace('\n','')
                    while data2 != data1:
                        data1 = data2
                myfile.close()
                data=data1
                os.system('cls' if os.name == 'nt' else 'clear')
                importlib.reload(main)
                targ_file.__main__()
#    except:
#        print(targ_file)
#        backgroundRun()
            
            
backgroundRunThread = Thread(target=backgroundRun, args=())


if __name__ != '__main__':
    print("start")
    backgroundRunThread.start()
