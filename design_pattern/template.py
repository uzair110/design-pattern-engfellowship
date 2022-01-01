from typing import overload

#Facade: Structural Design Pattern

class StartIgnition: #subsystem1

    def operation():
        return "Starting Ignition..."


class ChangeGear: #subsystem2

    def operation():
        return "Changing to first gear..."


class PressAccelerator: #subsystem3

    def operation():
        return "Pressing Accelerator..."
    
class Stop:
    def operation():
        return "Stop the car by applying brakes..."


class MoveCar:
    
    def DoWork():
        print()
        print(StartIgnition.operation())
        print(ChangeGear.operation())
        print(PressAccelerator.operation())
        print("Car is now moving....")
        print(Stop.operation())


if __name__ == "__main__":
    firstCar = MoveCar
    firstCar.DoWork()
    print()

 