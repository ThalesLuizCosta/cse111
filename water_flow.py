# Import necessary libraries
import math
import pytest
from pytest import approx

# Define constants
WATER_DENSITY = 998.2 # kg/m3
GRAVITY = 9.80665 # m/s2

# Define program functions

def water_column_height(tower_height, tank_height):
  # Calculate the height of the water column in the elevated tank
  # The total height is the sum of the tower height and the tank height
  total_height = tower_height + tank_height
  return total_height

def pressure_gain_water_height(total_height):
  # Calculate the pressure gain caused by Earth's gravity
  # pulling the water in the tank's column
  # using the formula P = rho * g * h
  # where P is the pressure, rho is the water density, g is the acceleration of gravity
  # and h is the height of the water column
  pressure = WATER_DENSITY * GRAVITY * total_height
  return pressure

def pipe_friction_loss(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
  pressure_loss = friction_factor * pipe_length / pipe_diameter * 0.5 * WATER_DENSITY * fluid_velocity ** 2
  return pressure_loss

# Define test functions

def test_water_column_height():
  # Test the water_column_height function with some example values
  assert water_column_height(10, 5) == approx(15, abs=0.001)
  assert water_column_height(20, 10) == approx(30, abs=0.001)
  assert water_column_height(5, 2) == approx(7, abs=0.001)

def test_pressure_gain_water_height():
  # Test the pressure_gain_water_height function with some example values
  assert pressure_gain_water_height(15) == approx(147.1, abs=0.1)
  assert pressure_gain_water_height(30) == approx(294.3, abs=0.1)
  assert pressure_gain_water_height(7) == approx(68.6, abs=0.1)

def test_pipe_friction_loss():
  # Test the pipe_friction_loss function with some example values
  assert pipe_friction_loss(0.1, 100, 0.02, 2) == approx(-39.7, abs=0.1)
  assert pipe_friction_loss(0.05, 50, 0.04, 1) == approx(-31.8, abs=0.1)
  assert pipe_friction_loss(0.01, 10, 0.08, 0.5) == approx(-9.9, abs=0.1)

# Call the main function that is part of pytest so that the
# computer runs the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
