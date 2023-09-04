
class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print(f'moves along')

    def get_make_model(self):
        print(f"\nI'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')
# my_car.get_make_model()
# my_car.moves()

# inhertance


class Aeroplane(Vehicle):

    def __init__(self, make, model, faa_Id):
        super().__init__(make, model)
        self.faa_Id = faa_Id

    def moves(self):
        print("Flies along")

    def get_make_model(self):
        print(f"\nI'm a {self.make} {self.model} with faa_Id: {self.faa_Id}.")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along")


class GolfCart(Vehicle):
    pass


cessna = Aeroplane('Cessna', 'Skyhawk', 'FA766-FLY')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

# cessna.get_make_model()
# cessna.moves()

# mack.get_make_model()
# mack.moves()

# golfwagon.get_make_model()
# golfwagon.moves()

# for v in (my_car, cessna, mack, golfwagon):
#   v.get_make_model()
#   v.moves()

###
######
# EXCEPTIONS

class JustNotCoolError(Exception):
    pass

x = 9
try:
    raise JustNotCoolError("I'm a custom error")
    # if not isinstance(x, int):
    #     raise TypeError('Only integers are allowed')
except NameError:
    print("X is not defined")
except ZeroDivisionError:
    print('Do not divide by zero')
except Exception as error:
    print(error)
else:
    print(f"{x} is here")
finally:
    print("I'll always print regardless")
