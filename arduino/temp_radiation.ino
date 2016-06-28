#include <OneWire.h>
#include <DallasTemperature.h>
#include <ArduinoJson.h>

const int TEMP = 2, PYRA = A0; // Input pins
const int ON = 3, SETUP = 4; // Output pins

OneWire oneWire(TEMP);
DallasTemperature temps(&oneWire);

void setup()
{
  // Set up pins
  pinMode(ON, OUTPUT);
  pinMode(SETUP, OUTPUT);
  pinMode(PYRA, INPUT);
  
  // Turn on setup LED
  digitalWrite(ON, LOW);
  digitalWrite(SETUP, HIGH);  
  
  // Begin serial output and temp probes
  Serial.begin(9600);
  temps.begin();
}

void loop()
{
  // Turn on 'on' LED
  digitalWrite(SETUP, LOW);
  digitalWrite(ON, HIGH);
  
  // Init json objects
  StaticJsonBuffer<200> jb;
  JsonObject& tempData = jb.createObject();
  JsonObject& radData = jb.createObject();
  
  // Temperatures
  temps.requestTemperatures();
  JsonArray& temp = tempData.createNestedArray("temp");
  for(int i = 0; i < 3; i++) // Temps
  {
    temp.add(temps.getTempCByIndex(i), 6);
  }
  tempData["time"] = millis();
  tempData["sensor"] = "temp";
  tempData.printTo(Serial);
  Serial.println();
  
  // Radiation
  // *(5/1023) for voltage, *5 for W/m^2
  float radiation = (float)analogRead(PYRA)*5*500/1023;
  radData["rad"] = radiation;
  radData["time"] = millis();
  radData["sensor"] = "rad";
  radData.printTo(Serial);
  Serial.println();
}
