class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # goes through the setter below

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
print(t.celsius, t.fahrenheit)
t.celsius = 100
print(t.fahrenheit)
try:
    t.celsius = -300
except ValueError as error:
    print("Refused:", error)
