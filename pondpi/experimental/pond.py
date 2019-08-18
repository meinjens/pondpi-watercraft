import time

import pigpio

print('init:')

pi = pigpio.pi()

leftmotor_in1_pin = 24
leftmotor_in2_pin = 25

leftmotor_pwm_pin = 17

pi.set_mode(leftmotor_in1_pin, pigpio.OUTPUT)
pi.set_mode(leftmotor_in2_pin, pigpio.OUTPUT)

print ('start:')

pi.write(leftmotor_in1_pin, 0)
pi.write(leftmotor_in2_pin, 1)

pi.set_PWM_frequency(leftmotor_pwm_pin, 50)
print(pi.get_PWM_frequency(leftmotor_pwm_pin))

pi.set_PWM_range(leftmotor_pwm_pin, 100)

pi.set_PWM_dutycycle(leftmotor_pwm_pin, 0)


print('stop:')

pi.stop()

print ('stopped.')
