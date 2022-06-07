# Values
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:

# TURN UP THE TEMPERATURE
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
  
# f_to_c(100):
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# USE THE FORCE

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print(train_force)

print(f"The GE train supplies {train_force} Newtons of force.")

def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)

print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# DO THE WORK

#Define a final function called get_work that takes in mass, acceleration, and distance.
#Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance. Return the result.

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")


