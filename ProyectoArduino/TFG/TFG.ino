void setup()
{
  Serial.begin(9600);
}
int i = 0;
void loop()
{
  Serial.println("CONTADOR: " + String(i));
  i++;
  delay(100);
}
