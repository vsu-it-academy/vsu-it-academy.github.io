int pin_led_red=8; // пин управления красным светодиодом
int pin_led_green=9; // пин управления зеленым светодиодом
int pin_buzzer=11; // пин управления динамиком

void setup() // функция установок, выполняется один раз
{
  pinMode(pin_led_red, OUTPUT); // конфигурация порта на режим управления
  pinMode(pin_led_green, OUTPUT); // конфигурация порта на режим управления
  pinMode(pin_buzzer, OUTPUT); // конфигурация порта на режим управления
  
  digitalWrite(pin_led_red, LOW); // посылаем низкий уровень сигнала, для выключения светодиода
  digitalWrite(pin_led_green, LOW); // посылаем низкий уровень сигнала, для выключения светодиода
  digitalWrite(pin_buzzer, LOW); // посылаем низкий уровень сигнала, для выключения динамика
}

void loop() // функция, которая по завершению снова запускается(аналог while(true))
{
  digitalWrite(pin_led_red, HIGH); // зажигаем красный светодиод
  delay(2000); // ждем 2 секунды
  digitalWrite(pin_led_red, LOW); // выключаем красный светодиод
  digitalWrite(pin_led_green, HIGH); // зажигаем зеленый светодиод
  tone(pin_buzzer,5000); // включаем динамик
  delay(3000); // ждем 3 секнды
  digitalWrite(pin_led_green, LOW); // выключаем зеленый светодиод
  noTone(pin_buzzer); // выключаем динамик
}
