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
  JsonObject& data = jb.createObject();
  
  // Get data
  temps.requestTemperatures();
  // *(5/1023) for voltage, *500 for W/m^2
  float radiation = (float)analogRead(PYRA)*5*500/1023;
  // area * panel efficiency * MPPT efficiency
  float power = 6 * 0.239 * 0.95 * radiation;
  
  // Write data
  for(int i = 0; i < 3; i++) // Temps
  {
    String tempKey = "temp" + String(i);
    data[tempKey] = temps.getTempCByIndex(i);
  }
  data["rad"] = radiation;
  data["pow"] = power;
  data["time"] = millis();

  data.printTo(Serial);
  Serial.println();
}
