#/usr/bin/env python

from tkinter import *
import sys
from subprocess import *


#====================================================================================================================
#                                               BUILD INFORMATION LIST
#====================================================================================================================

deviceDetails = ['[ro.ml.wearable.serialno]', '[ro.build.version]', '[ro.ml.build.version.release]', '[ro.boot.serialno]', '[ro.build.flavor]']


def checkPythonVersion():
    version=sys.version_info
    if version[0] != 3 and version[1] != 4:
        print("Update the Python to verion 3.4 or above")


#=====================================================================================================================
#                     FUNCTION  CONVERTS MLDB LOGS INTO DICTIONARY WHEN LOGS ARE FROM A FILE
#=====================================================================================================================
def deviceInfoFromLogs(args):
    dItem = {}
    f = open("output.txt", 'r' )
    for line in f:
        x=(line.rstrip('\n').split(':'))
        dItem[x[0]]=x[1]

    for key, value in dItem.items():
        if key == args:
            dItem[key].strip('[').strip(']')
            return dItem[key].strip(' [').strip(']')


#=====================================================================================================================
#                     FUNCTION  CONVERTS MLDB SHELL OUTPUT INTO DICTIONARY 
#====================================================================================================================
CMD = "mldb shell getprop"
#output = subprocess.check_output(CMD, shell=True)
p = Popen(["mldb", "shell", "getprop"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)

dItem={}
def deviceGetProp(args):
    #dItem = {}
    #f = open("output.txt", 'r' )
    for line in p.stdout:
        line=line.decode()
        x=line.split(':')
        dItem[x[0]]=x[1]
    
        

    for key, value in dItem.items():
        if key == args:
            return dItem[key].strip(' [').strip(']\n')

#=====================================================================================================================
#                                           SET THE GUI WINDOW
#=====================================================================================================================

window = Tk()
window.geometry("500x220")
window.title("                         MagicLeapDeviceInfoGUI                                    ")
wearable_Serial_Number_Value= StringVar(window)
build_Version_Value = StringVar(window)
build_Release_Value = StringVar(window)
boot_Serial_Number_Value = StringVar(window)
build_Flavor_Value = StringVar(window)

#=====================================================================================================================
#                                           EXTRACT BUILD INFORMATION
#=====================================================================================================================


def wearableSerialNumber():
    wearable_Serial_Number_Value.set(deviceGetProp(deviceDetails[0]))


def buildVersion():
    build_Version_Value.set(deviceGetProp(deviceDetails[1]))

def buildRelease():
    build_Release_Value.set(deviceGetProp(deviceDetails[2]))

def bootSerialNumber():
    boot_Serial_Number_Value.set(deviceGetProp(deviceDetails[3]))

def buildFlavor():
    build_Flavor_Value.set(deviceGetProp(deviceDetails[4]))

def main():
    checkPythonVersion()



  








    B1 = Button(window, text = "WEARABLE SERIAL NUMBER" ,command = wearableSerialNumber).place(x = 15,y = 20)
    textbox = Entry(window, textvariable = wearable_Serial_Number_Value).place(x=250,y=20)

    B2 = Button(window, text = "BUILD NUMBER",command = buildVersion).place(x =15,y = 60)
    textbox = Entry(window, textvariable = build_Version_Value).place(x=250,y=60)

    B3 = Button(window, text = "BUILD RELEASE",command = buildRelease).place(x = 15,y = 100)
    textbox = Entry(window, textvariable = build_Release_Value).place(x=250,y=100)


    B4 = Button(window, text = "DEVICE ID",command = bootSerialNumber).place(x = 15,y = 140)
    textbox = Entry(window, textvariable = boot_Serial_Number_Value).place(x=250,y=140)

    B5 = Button(window, text = "BUILD FLAVOR",command = buildFlavor).place(x = 15,y = 180)
    textbox = Entry(window, textvariable = build_Flavor_Value).place(x=250,y=180)

    window.mainloop()
if __name__ == '__main__':
	main()



