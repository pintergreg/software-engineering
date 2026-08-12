class Observable:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, data):
        print(f"{self.name} received data: {data}")


class TemperatureSensor(Observable):
    def __init__(self):
        super().__init__()

    def change_temperature(self, temperature):
        print(f"Temperature changed to: {temperature}")
        self.notify(temperature)


class DisplayUnit(Subscriber):
    def update(self, temperature):
        print(f"{self.name} updated with temperature: {temperature}")


# Create a temperature sensor instance
sensor = TemperatureSensor()

# Create display unit instances
display1 = DisplayUnit("Display 1")
display2 = DisplayUnit("Display 2")

# Subscribe display units to the sensor
sensor.subscribe(display1)
sensor.subscribe(display2)

# Simulate temperature changes
sensor.change_temperature(25)
sensor.change_temperature(30)
