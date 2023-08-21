## PILOTARE UN MOTORINO DIRETTAMENTE CON I 3,3V DELLA SCHEDA PYBOARD
Solitamente per pilotare un motore elettrico con la scheda [Pyboard](https://store.micropython.org) si usa un IC L293D cioè un integrato in grado di pilotare il motorino. Questo perchè i pin della scheda non sopportano più di 25mA mentre il motorino in mio possesso vuole almeno 100mA.
Utilizzando un transistor è possibile comandare la rotazione del motorino pilotando la sua base. Il motorino viene alimentato dal piedino **3v3** che può erogare al max **250 mA** . 
Nel circuito si vede male ma l'emettitore del transistor è collegato a GND della scheda Pyboard.

![Circuito per pilotare direttamente un motorino dalla Pyboard](https://github.com/DannyOnkies/DriverMotor/blob/main/driver_motor_3v3.jpg)
