#include <SoftwareSerial.h>

SoftwareSerial arduinoBT(10,11);

void setup()
{
  Serial.begin(9600);
  arduinoBT.begin(38400);
  Serial.println("LISTO!")
}
void loop()
{
  
}
