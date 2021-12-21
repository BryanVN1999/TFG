#include <SoftwareSerial.h>

// PIN INPUTS
const int INPUT_ECG = A0;             // PIN PARA LOS DATOS DEL ECG
const int INPUT_LED_RED = A1;         // PIN PARA LOS DATOS DEL LED ROJO
const int INPUT_LED_INFRARRED = A2;   // PIN PARA LOS DATOS DEL LED INFRARROJO

// PIN OUTPUTS
const int PIN_LED_RED = 6; // PIN DE EXCITACIÓN DEL LED ROJO
const int PIN_LED_INFRARRED = 5; // PIN DE EXCITACIÓN DEL LED INFRARROJO

// VARIABLES
int state; // 0 para el LED Rojo y 1 para el LED Infrarrojo
float valueEcg;
float valueRed;
float valueInfraRed;
float prevValueRed;
float prevValueInfraRed;
float R;
float spo2Total;
float spo2;
float spo2_average;
int spo2_final;


// VARIABLES STADISTIC
const int numMaxReading = 200;
int samples[numMaxReading];
int index = 0;
int canSpo2Final;

float EMA_ALPHA = 0.3;
float EMA_LP = 0;
float EMA_HP = 0;

// FUNCIONES
void CalculoR()
{
  // CALCULO DEL NUMERADOR Y DENOMINADOR DE LA ECUACION DE R
  float dA_R = (valueRed - prevValueRed) / ((valueRed + prevValueRed) / 2);
  float dA_IR = (valueInfraRed - prevValueInfraRed) / ((valueInfraRed + prevValueInfraRed) / 2);
  if (dA_R != 0.0)
  {
    // CALCULO DE R Y SPO2 EN CADA INSTANTE DE TIEMPO
    R = dA_IR / dA_R;
    spo2 = 115 - (30 * R);
    if (R > 0 && R < 1.5)
    {
      // CALCULO DE LA MEDIA DEL SPO2
      spo2Total -= samples[index];
      samples[index] = spo2;
      spo2Total += samples[index];
      spo2_average = spo2Total/numMaxReading;
      // HASTA QUE NO SE HAYA RECORRIDO EL ARRAY UNA VEZ
      // NO SE ACTUALIZA EL VALOR DE SPO2_FINAL
      // QUE SE ENVIARA AL PROGRAMA DE PYTHON
      if(canSpo2Final == 1)
      {
        spo2_final = (int)spo2_average;
      }
      index++;
    }
  }
  if (index == numMaxReading)
  {
    canSpo2Final = 1;
    index = 0;
  }
}

void setup()
{
  // INICIO DE LA COMUNICACIÓN SERIE
  Serial.begin(9600);
  // INSTANCIA DE PINES
  pinMode(PIN_LED_RED, OUTPUT);
  pinMode(PIN_LED_INFRARRED, OUTPUT);
  // INICIALIZAR ARRAYS
  for (int i = 0; i < numMaxReading; i++)
  {
    samples[i] = 0;
  }
  // INITIALIZE VARIABLES
  valueEcg = 0;
  valueRed = 0;
  prevValueRed = 0;
  valueInfraRed = 0;
  prevValueInfraRed = 0;
  R = 0;
  spo2 = 0;
  spo2Total = 0;
  spo2_average = 0;
  spo2_final = 0;
  canSpo2Final = 0;
}

void loop()
{
  Serial.println(String(valueEcg) + "," + String(spo2) + "," + String(spo2_final));
  // --------------------- ELECTROCARDIOGRAM -------------------
  // SE OBTIENE EL VALOR DEL ECG EN UN RANGO DE 5V.
  valueEcg = (EMALowPassFilter(analogRead(INPUT_ECG))/1024.0)*5.0;
  //Serial.print("ECG:");
  //Serial.println(valueEcg);
  // -------------------- PULSIOXIMETRE ----------------------
  // LED ROJO ON, LED IR OFF
  analogWrite(PIN_LED_INFRARRED,0);
  analogWrite(PIN_LED_RED,97);
  delayMicroseconds(400);
  // LED ROJO OFF, LED IR OFF
  prevValueRed = valueRed;
  valueRed = (analogRead(INPUT_LED_RED)/1024.0)*5.0;
  //Serial.print("RED:");
  //Serial.println(valueRed);
  delayMicroseconds(600);
  // LED ROJO OFF, LED IR ON
  analogWrite(PIN_LED_RED,0);
  analogWrite(PIN_LED_INFRARRED, 97);
  delayMicroseconds(400);
  // LED ROJO OFF, LED IR OFF
  prevValueInfraRed = valueInfraRed;
  valueInfraRed = (analogRead(INPUT_LED_INFRARRED)/1024.0)*5.00;
  //Serial.print("IF:");
  //Serial.println(valueInfraRed);
  delayMicroseconds(600);
  CalculoR();
  //Serial.print("SPO2:");
  //Serial.println(spo2);
  //Serial.print("MEDIA_SPO2:");
  //Serial.println(spo2_final);
}



float EMALowPassFilter(int value)
{
  EMA_LP = EMA_ALPHA * value + (1 - EMA_ALPHA) * EMA_LP;
  return EMA_LP;
}
float EMAHighPassFilter(int value)
{
  EMA_LP = EMA_ALPHA * value + (1 - EMA_ALPHA) * EMA_LP;
  EMA_HP = value - EMA_LP;
  return EMA_HP;
}
