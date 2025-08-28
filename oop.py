class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self._health = 100  # Protected attribute
        self.__secret_identity = "Unknown"  # Private attribute
    
    def fight(self):
        return (f" {self.name} uses {self.power}!")
    
    def get_health(self):
        return self._health

# Inheritance classes
class FlyingHero(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed
    
    def fight(self):  # Polymorphism - override parent method
        return (f" {self.name} flies and uses {self.power} at {self.speed}")
# Add this before line 23:
class MagicHero(Superhero):
    def __init__(self, name, power, spell):
        super().__init__(name, power)
        self.spell = spell
    
    def fight(self):
        return f"🪄 {self.name} casts {self.spell} with {self.power}!"

# Test the class:
heroes = [
    FlyingHero("Superman", "Super Strength", 1000),
    MagicHero("Doctor Strange", "Magic", "Time Loop"),  # Add this
    Superhero("Batman", "Intelligence")
]

print("🦸 SUPERHERO BATTLE!")
for hero in heroes:
    print(hero.fight())  # Polymorphism in action!
    print(f"   Health: {hero.get_health()}")
    