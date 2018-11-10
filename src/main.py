from script import FirebaseClient 
from script import ArduinoClient 

def main():
    fc = FirebaseClient('data')
    fc.setRoot()
    ac = ArduinoClient('COM4', 9600, 0.1)
    if ac.startSerial():
        ac.readData()
    else:
        print("Error in Serial Connecction!!!")

if __name__ == "__main__":
    main()
