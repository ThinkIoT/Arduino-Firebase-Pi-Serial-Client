import serial
import re
import time
from auth import FirebaseAuth

class FirebaseClient:
    def __init__(self, data):
        fa = FirebaseAuth()
        fa.initialisedb()
        self.root = fa.createdb(data)

    def setRoot(self):
        self.root.set({
        'SensorA': 00,
        'SensorB': 00,
        'SensorC': 00,

        'SensorD': 00,
        'SoilStats': 'No Soil',

        'Status' : 'Live'

    })


    def validateData(self, datalist):
        if len(datalist) == 4:
            updateData(datalist)
        else:
            print((datalist))
            self.root.update({
                'Status': 'Error in Writing'
            })
    def updateData(self, datalist):
        try:
            self.root.update({
                    'SensorA': float(DataList[0]),
                    'SensorB': float(DataList[1]),
                    'SensorC': float(DataList[2]),
                    
                    'SensorD': float(DataList[3])
                })
            print("Data Updated")
        except IOError:
            print('Error! Something went wrong.')
            time.sleep(20)

class ArduinoClient:

    port = 'COM4'
    baudrate = 9600
    timeout = 0.1

    def __init__(self, port=port, baudrate=baudrate, timeout=timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

    def sendIt(self, datalist):
        FirebaseClient.validateData(datalist)
    
    
    def filterData(self, datalist):
        pattern = re.compile("^\s+|\s*,\s*|\s+$")
        datastring = datalist[0]
        datalist = [x for x in pattern.split(datastring) if x]
        sendIt(datalist)
        
    def startSerial(self):
        try:
            self.arduino = serial.Serial(self.port, self.baudrate, self.timeout)
            return True
        except:
            return False
        else:
            return False

    def readData(self):
        start = 0
        st = []
        
        while True:
            data = self.arduino.readline()[:-2]
            if data:
                if start <= 2:
                    start += 1
                    pass
            else:
                st.append(data.decode('ASCII'))
                filterData(st)
                st = []
