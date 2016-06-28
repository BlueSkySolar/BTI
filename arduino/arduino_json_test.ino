#include <ArduinoJson.h>

StaticJsonBuffer<200> jb;
JsonObject& root = jb.createObject();

void setup(){
  Serial.begin(9600);
  root["sensor"] = "temp";
}

void loop(){
  root["time"] = millis();
  root.printTo(Serial);
  Serial.println();
  delay(1000);
}
