#include <OneWire.h>
#include <DallasTemperature.h>

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
  Serial.begin(115200);
  temps.begin();
}

void loop()
{
  // Turn on 'on' LED
  digitalWrite(SETUP, LOW);
  digitalWrite(ON, HIGH);
  
  // Calculate values
  temps.requestTemperatures();
  // *(5/1023) for voltage, *5 for W/m^2
  float radiation = (float)analogRead(PYRA)*5*500/1023;
  
  // Write values to serial
  Serial.print(millis()); // System time
  Serial.print(",");
  for(int i = 0; i < 3; i++) // Temps
  {
    Serial.print(temps.getTempCByIndex(i));
    if(i != 3)
      Serial.print(",");
  }
  Serial.println(radiation); // Radiation
  
  delay(200); // Necessary; outputs gibberish otherwise
}
