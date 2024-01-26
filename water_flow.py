import math
import pytest
from pytest import approx

WATER_DENSITY = 998.2 # kg/m3
GRAVITY = 9.80665 # m/s2

def water_column_height(tower_height, tank_height):
  total_height = tower_height + tank_height
  return total_height

def pressure_gain_water_height(total_height):
  pressure = WATER_DENSITY * GRAVITY * total_height
  return pressure

def pipe_friction_loss(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
  pressure_loss = friction_factor * pipe_length / pipe_diameter * 0.5 * WATER_DENSITY * fluid_velocity ** 2
  return pressure_loss

def test_water_column_height():
  assert water_column_height(10, 5) == approx(15, abs=0.001)
  assert water_column_height(20, 10) == approx(30, abs=0.001)
  assert water_column_height(5, 2) == approx(7, abs=0.001)

def test_pressure_gain_water_height():
  assert pressure_gain_water_height(15) == approx(147.1, abs=0.1)
  assert pressure_gain_water_height(30) == approx(294.3, abs=0.1)
  assert pressure_gain_water_height(7) == approx(68.6, abs=0.1)

def test_pipe_friction_loss():
  assert pipe_friction_loss(0.1, 100, 0.02, 2) == approx(-39.7, abs=0.1)
  assert pipe_friction_loss(0.05, 50, 0.04, 1) == approx(-31.8, abs=0.1)
  assert pipe_friction_loss(0.01, 10, 0.08, 0.5) == approx(-9.9, abs=0.1)

pytest.main(["-v", "--tb=line", "-rN", __file__])
