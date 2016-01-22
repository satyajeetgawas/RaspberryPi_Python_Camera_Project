import shutil
import os
import datetime
import subprocess
import sys
import usb.core
import usb.backend.libusb1

import RPi.GPIO as GPIO

GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.IN)
class ListUSB:
    def getUSB():
        # find USB devices
        dev = usb.core.find(find_all=True)
        # loop through devices, printing vendor and product ids in decimal and hex
        for cfg in dev:
            print('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
            print('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')

class ListOfFiles(object):
    def getSource(self):
        return 'C:\\Users\\insag3\\Desktop\\DCIM'
    def getDest(self):
        return 'C:\\Users\\insag3\\Desktop\\dest'

class CopyFiles:
    def copyFile(sFolder,source,dest):
        shutil.copy2(source,dest)
        logger.generatelog(sFolder,source,dest)
        os.remove(source)
        return

class CopyDir:
    def copyDir(sFolder,dFolder):
        fileList = os.listdir(sFolder)
        if not os.path.exists(dFolder):
            os.makedirs(dFolder)
            print('Directory '+dFolder+' created')
        log = logger(sFolder)
        for i in fileList:
            source = sFolder+'\\'+i
            dest = dFolder+'\\'+i
            if os.path.isfile(source):
                CopyFiles.copyFile(sFolder,source,dest)
            if os.path.isdir(source):
                CopyDir.copyDir(source,dest)
        return

class logger:
    def __init__(self,sFolder):
        logFile=sFolder+'\\log.txt'
        file = open(logFile,'a')
        ostime=datetime.datetime.now()
        file.write('Copy Procedure Started @ ')
        file.write(ostime.isoformat())
        file.write('\n')
        file.close
        
        
    def generatelog(sFolder,source,dest):
            logFile=sFolder+'\\log.txt'
            size=0.0
            size = size+os.path.getsize(source)
            size = size/1024
            try:
                file = open(logFile,'a')
                try:
                    file.write('----------------------------------------------------------------------------------------------------------------------\n')
                    file.write('File '+source+' moved to '+dest+' Size--'+'%d'%(size)+'KB\n')
                finally:
                    file.close()
            except IOError:
                pass
            
class Main:

    while(1)
        if GPIO.input(19)
            GPIO.output(18,GPIO.HIGH)
            x=ListOfFiles()
            ListUSB.getUSB()
            srcDrive = x.getSource()
            destDrive = x.getDest()
            listOfFiles=os.listdir(srcDrive)
            log = logger(srcDrive)
            for i in listOfFiles:
                source = srcDrive+'\\'+i
                dest   = destDrive+'\\'+i
                if os.path.isfile(source):
                    CopyFiles.copyFile(srcDrive,source,dest)
                if os.path.isdir(source):
                    CopyDir.copyDir(source,dest)
        else:
            GPIO.output(18,GPIO.LOW)

            
            
            
                
    
    

