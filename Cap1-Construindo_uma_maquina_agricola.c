#include <DHT.h>
//inicializando os componentes
int ledverde = 19;     
int ledazul = 18;      
int buttonPin1 = 2;    
int buttonPin2 = 15;   
int dhtPin = 4;        

#define DHTTYPE DHT22  
DHT dht(dhtPin, DHTTYPE);  
//para efeito de execução considerei este valor manualmente
float humidity = 50.0;    

void setup() {
    pinMode(ledverde, OUTPUT);
    pinMode(ledazul, OUTPUT);
    pinMode(buttonPin1, INPUT_PULLUP);  
    pinMode(buttonPin2, INPUT_PULLUP);  
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
    }

    if (buttonState2 == LOW) {  
        digitalWrite(ledazul, HIGH);  
        Serial.println("LED azul está aceso");
    } else {
        digitalWrite(ledazul, LOW);  
    }

    if (isnan(humidity)) {
        // como eu inicializei manualmente, esta condição nunca se aplicará
        Serial.println("Failed to read from DHT sensor!");
    } else {        
        Serial.print("A medição da humidade está em: ");
        Serial.print(humidity);
        Serial.println(" %, desde a última medição");
    }

    delay(2000);  
}
