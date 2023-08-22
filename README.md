### PILOTARE UN MOTORINO DIRETTAMENTE CON I 3,3V DELLA SCHEDA PYBOARD
Solitamente per pilotare un motore elettrico con la scheda [Pyboard](https://store.micropython.org) si usa un [IC L293D](https://www.robotstore.it/Motor-Shield-L293D-4-canali) cioè un integrato in grado di pilotare il motorino [vedi il mio video su Youtube](https://www.youtube.com/watch?v=qONEuLo44G4&t=193s).
Questo perchè i pin della scheda non sopportano più di 25mA mentre il motorino in mio possesso vuole almeno 100mA.
Utilizzando un transistor è possibile comandare la rotazione del motorino pilotando la sua base. Il motorino viene alimentato dal piedino **3v3** che può erogare al max **250 mA** . [Vedi mappa Pyboard](https://micropython.org/resources/pybv11-pinout.jpg) .  
In pratica il transistor **2n2222** viene usato in modalità [interruttore](https://www.vincenzov.net/tutorial/elettronica-di-potenza/transistor.htm) , cioè lavora in *saturazione* o in *interdizione*.
Nel circuito si vede male ma l'emettitore del transistor è collegato al GND della scheda Pyboard.
Più sotto ho inserito un breve codice da inserire per testare il circuito. 

![Circuito per pilotare direttamente un motorino dalla Pyboard](https://github.com/DannyOnkies/DriverMotor/blob/main/driver_motor_3v3.jpg)


### Codice Micropython per testare il circuito

> from pyb import Pin
> 
> ventola = Pin("X1",Pin.OUT)
> 
> led = Pin("X2",Pin.OUT)
> 
> ventola.on()
> 
> led.on()
> 
> pyb.delay(5000)
> 
> ventola.off()
> 
> led.off()
