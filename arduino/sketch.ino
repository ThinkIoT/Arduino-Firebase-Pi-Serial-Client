/* 
    A sample dummy arduino code to get data from 
    multiple sensors. 

*/


#include <RTClib.h>
#include <lib1.h>
#include "lib2.h"
#include <lib3.h>
#include <Arduino.h>




const int ss =53;
const int pin_scl = 2;      
const int pin_sda = 3;      



#define PIN_GATE_IN 2
#define IRQ_GATE_IN  0
#define PIN_LED_OUT 13
#define PIN_ANALOG_IN A0

//declare function prototype here

//Declare global variables

void setup()
{
    //rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    Serial1.begin(9600);   //set the serial1's Baudrate of sensors

    //  Configure LED pin as output
    pinMode(PIN_LED_OUT, OUTPUT);

    // configure input to interrupt
    pinMode(PIN_GATE_IN, INPUT);


    Serial.setTimeout(1500);    //set the Timeout to 1500ms, longer than the data transmission periodic time of the sensor
    pinMode(ss, OUTPUT);
    digitalWrite(ss, HIGH);

    delay(100);


    Serial.println("power on!");
    Serial.print("Firmware Version = ");
    pinMode(pin44, OUTPUT);

    rtc.begin();
    //rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));

    if (! rtc.isrunning()) {
      Serial.println("RTC is NOT running!");
      rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    }
}

void loop()
{
    //g b g y
     printDateTime();
    
    Serial.print(fn4Sensor2());
    Serial.print(", ");
    Serial.print(fn4Sensor3());
    Serial.print(", ");
    Serial.print(fn4Sensor4());
    Serial.print(", ");
    Serial.print(fn4Sensor5());
    Serial.print("\n");
    
}

void printDateTime()
{
  DateTime now = rtc.now();
  Serial.print(now.day(), DEC);
  Serial.print("/");
  Serial.print(now.month(), DEC);
  Serial.print("/");
  Serial.print(now.year(), DEC);
  Serial.print(", ");
  Serial.print(now.hour(), DEC);
  Serial.print(":");
  Serial.print(now.minute(), DEC);
  Serial.print(":");
  Serial.print(now.second(), DEC);
  Serial.print(", ");
}


//Functions
double fn4Sensor5(//args)
{
    //logic here
    //return val5;
}

int fn4Sensor4(//args)
{
    //code here
    //return val4;
}

int fn4Sensor3(//args)
{
    //code here
    //return val3;
}

int fn4Sensor2(//args)
{
    //code here
    //return val2;
}
