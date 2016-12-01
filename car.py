#Class Car, that creates car object with a drive & is_saloon method.
#By hms91

class Car(object):
## Initialize class variables and Check and assign doors according to car arg passed
  def __init__(self, name = "General", model = "GM" , *car_type):
    
    self.speed = 0
    self.num_of_doors = 4 if not(name =='Porshe' or name == 'Koenigsegg') else 2
    self.num_of_wheels = 8 if 'trailer' in car_type else 4
    self.name = name
    self.model = model
    self.car_type = car_type

## Check whether the car is of type saloon or trailer
  def is_saloon(self):
    if self.car_type is not 'trailer':
      self.car_type == 'saloon'
      return True
    return False

## Check the moving speed and return the speed
  def drive(self, moving_speed):
    if moving_speed == 3:
      self.speed = 1000
    elif moving_speed == 7:
      self.speed = 77
      
    return self
