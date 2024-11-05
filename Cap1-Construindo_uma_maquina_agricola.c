#include <DHT.h>

// inicializando os componentes
int ledverde = 19;
int ledazul = 18;
int buttonPin1 = 2;
int buttonPin2 = 15;
int dhtPin = 4;
int photoresistorPin = 34;  // define the pin for the photoresistor

#define DHTTYPE DHT22
DHT dht(dhtPin, DHTTYPE);

float humidity = 50.0;

void setup() {
    pinMode(ledverde, OUTPUT);
    pinMode(ledazul, OUTPUT);
    pinMode(buttonPin1, INPUT_PULLUP);
    pinMode(buttonPin2, INPUT_PULLUP);
    pinMode(photoresistorPin, INPUT); // setup the photoresistor pin
    Serial.begin(9600);
    Serial.println("todos os leds estao apagados, inicializando!");
    dht.begin();
}

void loop() {
    int buttonState1 = digitalRead(buttonPin1);
    int buttonState2 = digitalRead(buttonPin2);

    if (buttonState1 == LOW) {
        digitalWrite(ledverde, HIGH);
        Serial.println("LED verde está aceso");
    } else {
        digitalWrite(ledverde, LOW);
        Serial.println("LED verde está apagado");
    }

    if (buttonState2 == LOW) {
        digitalWrite(ledazul, HIGH);
        Serial.println("LED azul está aceso");
    } else {
        digitalWrite(ledazul, LOW);
        Serial.println("LED azul está apagado");
    }

    if (isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
    } else {
        Serial.print("A medição da humidade está em: ");
        Serial.print(humidity);
        Serial.println(" %, desde a última medição");
    }

    // Ler o valor do fotoresistor e converter para porcentagem de nível de luz
    int lightLevelRaw = analogRead(photoresistorPin);
    float lightLevelPercentage = map(lightLevelRaw, 0, 4095, 0, 100); // Formula para converter em percentual

    Serial.print("Nível de luz (Fotoresistor) em bruto: ");
    Serial.print(lightLevelRaw);
    Serial.print(" | Nível de luz em porcentagem: ");
    Serial.print(lightLevelPercentage);
    Serial.println("%");

    delay(2000);
}
