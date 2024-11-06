#include <DHT.h>

// inicializando os componentes
int ledverde = 19;
int ledazul = 18;
int buttonPin1 = 2;
int buttonPin2 = 15;
int dhtPin = 4;
int photoresistorPin = 34;
int relayPin = 5;  // Pino para o relay

#define DHTTYPE DHT22
DHT dht(dhtPin, DHTTYPE);


// Colocando um valor aleatório para humidade//
float humidity = 32.0;
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
        Serial.print("Botão de coleta de Potássio pressionado ");
        Serial.print(buttonPressCount);
        Serial.println(" vezes.");
        

        ////////////////////////////////////////////////////////////////////////////////////////
        // Aqui foi criada a regra para saber se é hora de irrigar                            //
        // Considerar se o botão foi pressionado 3 vezes e se o nível de luz é maior do que 2 //
        ////////////////////////////////////////////////////////////////////////////////////////


        // Verifica se o botão foi pressionado 3 vezes
        if (buttonPressCount >= 3) {
            // Ler o valor do fotoresistor e converter para porcentagem de nível de luz
            int lightLevelRaw = analogRead(photoresistorPin);
            float lightLevelPercentage = map(lightLevelRaw, 0, 4095, 0, 100);
            float lightLevelOutOf14 = lightLevelPercentage * 14 / 100;

            // Verifica se o nível de luz é superior a 2
                        if (lightLevelOutOf14 > 2) {
                Serial.println("Está na hora de irrigar. Processo de irrigação ativado!");
                digitalWrite(relayPin, HIGH);  // Liga o relay
            } else {
                Serial.println("Ainda não é hora de irrigar.");
            }
        }
    }

    digitalWrite(ledazul, buttonState2 == LOW ? HIGH : LOW);
    if (buttonState2 == LOW) {
        Serial.println("LED azul está aceso");
        Serial.println("Nutriente Potássio coletado!");
    }

    // Ler o valor do fotoresistor e converter para porcentagem de nível de luz
    int lightLevelRaw = analogRead(photoresistorPin);
    float lightLevelPercentage = map(lightLevelRaw, 0, 4095, 0, 100);
    float lightLevelOutOf14 = lightLevelPercentage * 14 / 100;

    // Exibir o nível de luz em uma escala de 0 a 14
    Serial.print("Nível de luz (no caso, pH) em uma escala de 0 a 14: ");
    Serial.println(lightLevelOutOf14);

    if (isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
    } else {
        Serial.print("A medição da humidade está em: ");
        Serial.print(humidity);
        Serial.println(" %, desde a última medição");
    }

    lastButtonState2 = buttonState2;
    delay(2000);
}
