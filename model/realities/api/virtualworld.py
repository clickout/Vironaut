class VirtualWorld:
    def __init__(self, theme, date, energy, biomes):
        self.theme = theme
        self.date = date
        self.energy = energy
        self.biomes = biomes

class Biome:
    def __init__(self, name, description, weather, flora, fauna):
        self.name = name
        self.description = description
        self.weather = weather
        self.flora = flora
        self.fauna = fauna

class Weather:
    def __init__(self, name, description, temperature, humidity, wind_speed):
        self.name = name
        self.description = description
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

class Flora:
    def __init__(self, name, description, growth_rate, oxygen_production, carbon_dioxide_absorption):
        self.name = name
        self.description = description
        self.growth_rate = growth_rate
        self.oxygen_production = oxygen_production
        self.carbon_dioxide_absorption = carbon_dioxide_absorption

class Fauna:
    def __init__(self, name, description, diet, habitat, lifespan):
        self.name = name
        self.description = description
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan