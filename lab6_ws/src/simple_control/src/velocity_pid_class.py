#!/usr/bin/env python

class PID:
  # TODO FOR CHECKPOINT 0
  # On node initialization
  def __init__(self, p=0.0, i=0.0, d=0.0):
    self.kp = p
    self.ki = i
    self.kd = d
    self.integral = 0
    self.prev_error = 0
    self.output = 0

   # TODO FOR CHECKPOINT 0
  def pid_loop(self, error, dt):
    self.integral += error * dt
    derivative = (error - self.prev_error) / dt
    self.output = self.kp * error + self.ki * self.integral + self.kd * derivative
    self.prev_error = error

    return self.output