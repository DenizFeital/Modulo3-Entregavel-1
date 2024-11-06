#include <DHT.h>

// inicializando os componentes
int ledverde = 19;
int ledazul = 18;
int buttonPin1 = 2;
int buttonPin2 = 15;
int dhtPin = 4;
int photoresistorPin = 34;
int relayPin = 17;  // Defina o pino para o relé

#define DHTTYPE DHT22
DHT dht(dhtPin, DHTTYPE);

float humidity = 50.0;
int buttonPressCount = 0; // Contador de pressionamentos do botão
bool lastButtonState2 = HIGH; // Último estado do botão 2

void setup() {
    pinMode(ledverde, OUTPUT);
    pinMode(ledazul, OUTPUT);
    pinMode(buttonPin1, INPUT_PULLUP);
    pinMode(buttonPin2, INPUT_PULLUP);
    pinMode(photoresistorPin, INPUT);
    pinMode(relayPin, OUTPUT);   // Configura o pino do relé como saída
    digitalWrite(relayPin, LOW); // Garante que o relé começa desligado
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
        Serial.println("Nutriente Fósforo coletado!");
    } else {
        digitalWrite(ledverde, LOW);
    }

    if (buttonState2 == LOW && lastButtonState2 == HIGH) {
        buttonPressCount++; // Incrementa o contador de pressionamentos
        Serial.print("Button 2 pressionado ");
        Serial.print(buttonPressCount);
        Serial.println(" vezes.");
        
        if (buttonPressCount >= 3) {
            Serial.println("Contagem atingiu 10! Ligando o relé.");
            digitalWrite(relayPin, HIGH);  // Liga o relé quando a contagem atinge 3
        }

        digitalWrite(ledazul, HIGH);
        Serial.println("LED azul está aceso");
        Serial.println("Nutriente Potássio coletado!");
    } else {
        digitalWrite(ledazul, LOW);
    }
    
    lastButtonState2 = buttonState2; // Atualiza o estado anterior do botão

    if (isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
    } else {
        Serial.print("A medição da humidade está em: ");
        Serial.print(humidity);
        Serial.println(" %, desde a última medição");
    }

    // Ler o valor do fotoresistor e converter para porcentagem de nível de luz
    int lightLevelRaw = analogRead(photoresistorPin);
    float lightLevelPercentage = map(lightLevelRaw, 0, 4095, 0, 100);

    // Converter o nível de luz para uma escala de 0 a 14,
    // considerando os dados analógicos coletados, fazendo uma relação com o pH
    // que varia de 0 a 14
    float lightLevelOutOf14 = lightLevelPercentage * 14 / 100;
    Serial.print("Nível de luz (no caso, pH) em uma escala de 0 a 14: ");
    Serial.println(lightLevelOutOf14);

    delay(3000);
}
