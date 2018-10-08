#program to use a DHT22 sensor to operate two fans AC fans via relays based upon sensor feedback of enviornmental conditions
#code also includes a cutoff switch for when it's tool cold or something's on fire
#cuz it's too fucking hot in that room and we want to try something cool
#pin and interupt setup from: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/pins.html
#DHT sensor setup from: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/dht.html

#DHT22 sensor setup
import dht
import machine
d = dht.DHT22 (machine.Pin(4))
import time

#fan control variables and pin setup
fan = machine.Pin(0, machine.Pin.OUT)
stick_fan = machine.Pin(2, machine.Pin.OUT)

#iterupt setup for cutoff switch
i=0
def cutoff(i):
    i+=1
interupt_pin = Pin(4, Pin.IN)
interupt_pin.irq(trigger=Pin.IRQ_FALLING, handler=cutoff)


while i%2==0:
    #put some code hereto read the sensor every 2 seconds (the maximum read frequency of a DHT22) and have the fans turn on and off in response.
    #something like read value after interval, take average of temprature and humidity readings, if average is over 76 fan and stick_fan turn on
    #may also want to add provisions for digital feedback of readings. more to come on that i guess
   if(d.temprature+d.humidity/100>72):
        fan.high()
        stick_fan.high()
   else:
        fan.low()
        stick_fan.low()


