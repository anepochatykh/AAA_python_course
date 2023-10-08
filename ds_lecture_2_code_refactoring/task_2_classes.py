# solution
class Celsius:
    def __init__(self, temperature):
        self._temp = temperature

    @property
    def temperature(self):
        if self._temp < -273:
            raise ValueError('Absolutelly freezing here')
        return self._temp


# advanced solution
class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temp

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temp = value

if __name__ == "__main__":
    c1 = Celsius(-300)
    print(c1.temperature)

    c1.temperature = -100
    print(c1.temperature)

    # c2 = Celsius(-300)
    # print(c2.temperature)


