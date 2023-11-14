

def translate(angle:float) -> int:
    if 0<= angle <= 180:
        pwm_out = int((500 + (2000) * (angle / 180))*65535/20000)
    elif angle > 180:
        pwm_out = 8192
    else:
        pwm_out = 1638
    return pwm_out