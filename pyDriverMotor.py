from pyb import Pin

ventola = Pin("X1",Pin.OUT)
led = Pin("X2",Pin.OUT)

ventola.on()
led.on()

pyb.delay(5000)

ventola.off()
led.off()
