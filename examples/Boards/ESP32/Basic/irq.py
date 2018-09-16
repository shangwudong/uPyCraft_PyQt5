#Hardware Platform: FireBeetle-ESP32
from machine import Pin
value=1
counter=0
def func(v):
  global value,counter
  time.sleep_ms(50)
  value = 0 if value else 1                         #If LED is turn on,it will be shutdown next,otherwise if will turn on next.
  print("IRQ ",counter)

  led = Pin(25, Pin.OUT)                              #create LED object from pin25,Set Pin25 to output
  led.value(0)
  button = Pin(27, Pin.IN)                            #create Button object from pin27,Set Pin27 to input
  button.irq(trigger=Pin.IRQ_RISING, handler=func)    #init irq,set interrupt on rising edge,and callback function is func
  while True:
    pass