from machine import Pin, PWM

servo = PWM(Pin(0))
servo.freq(50)

#duty_max = 
#duty_min = 
angle = 180
pwm_out = int((500 + (2000) * (angle / 180))*65535/20000)
print(pwm_out)