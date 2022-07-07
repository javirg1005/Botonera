//#include <Keyboard.h>

int valor = 0;  //variable que almacena la lectura analógica
int posicion;   //posicion del potenciómetro en tanto por ciento
int valor2 = 0;  //variable que almacena la lectura analógica
int posicion2;   //posicion del potenciómetro en tanto por ciento

int valor3 = 0;  //variable que almacena la lectura analógica
int valor4 = 0;  //variable que almacena la lectura analógica

void setup() {
  Serial.begin(9600);
  //Botones
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  //switches
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
  pinMode(16, INPUT);
  pinMode(17, INPUT);

  //  Keyboard.begin();
}

void loop() {

  boton(2);
  boton(3);
  boton(4);
  boton(5);
  boton(6);
  boton(7);
  boton(8);
  boton(9);
  boton(10);
  boton(11);
  boton(12);
  boton(13);
  boton(16);
  boton(17);

  valor = analogRead(A0);          // realizar la lectura analógica
  valor2 = analogRead(A1);          // realizar la lectura analógica
  posicion = map(valor, 0, 1023, 0, 100);  // convertir a porcentaje
  posicion2 = map(valor2, 0, 1023, 0, 100);  // convertir a porcentaje

  //Serial.print("Valor %: ");
  Serial.print(posicion);
  //Serial.print("Valor2 %: ");
  Serial.print(",");
  Serial.println(posicion2);

  delay(70);
}

void boton(int pin) {
  if (digitalRead(pin) == LOW) {
    //Keyboard.write(87); // w
    Serial.print(pin);
    Serial.print(",");
  } else {
    //Keyboard.releaseAll();
    Serial.print('0');
    Serial.print(",");
  }
}
