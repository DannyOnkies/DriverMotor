# Driver Motor
Solitamente per pilotare un motore elettrico con la scheda [Pyboard](https://store.micropython.org) si usa un IC L203D cioè un integrato n grado di pilotare il motorino. Questo perchè i pin della scheda non sopportano più di 25mA mentre il motorino in mio possesso vuole almeno 100mA.
Utilizzando un transistor è possibile comandare la rotazione del motorino pilotando la sua base.

![Circuito per pilotare direttamente un motorino dalla Pyboard](https://github.com/DannyOnkies/DriverMotor/blob/main/driver_motor_3v3.jpg)
