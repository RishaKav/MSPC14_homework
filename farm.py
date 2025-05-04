from abc import ABC, abstractmethod
from collections import defaultdict

# Animal Base Class (Abstract)
class Animal(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self):
        print(f"{self._name} is being fed!")

    def get_name(self):
        return self._name

    def get_species(self):
        return self.__class__.__name__


class Cow(Animal):
    def make_sound(self):
        print(f"{self._name} says Moo!")

    def produce(self):
        return "Milk"


class Chicken(Animal):
    def make_sound(self):
        print(f"{self._name} says Cluck!")

    def produce(self):
        return "Egg"


class Sheep(Animal):
    def make_sound(self):
        print(f"{self._name} says Baa!")

    def produce(self):
        return "Wool"


# FarmStructure Class
class FarmStructure:
    def __init__(self, name: str, structure_type: str):
        self._name = name
        self._type = structure_type

    def describe(self):
        return f"{self._name} ({self._type})"


# Farm Class
class Farm:
    def __init__(self, name="The Belval Farm"):
        self._name = name
        self._animals = []
        self._structures = []

    def add_animal(self, animal: Animal):
        self._animals.append(animal)

    def add_structure(self, structure: FarmStructure):
        self._structures.append(structure)

    def show_population(self):
        print(f"Welcome to {self._name}!\nFarm Population:")
        species_count = defaultdict(int)
        for animal in self._animals:
            species_count[animal.get_species()] += 1
        for species, count in species_count.items():
            print(f"- {species}: {count}")

    def list_structures(self):
        print("Structures:")
        for structure in self._structures:
            print(structure.describe())

    def daily_routine(self):
        print("----- Morning Routine ------")
        products = set()
        for animal in self._animals:
            animal.feed()
            animal.make_sound()
            if hasattr(animal, 'produce'):
                products.add(animal.produce())
        print(f"Collected products: {', '.join(products)}")


# Demo Setup with Desired Output

if __name__ == "__main__":
    # Create farm
    my_farm = Farm()

    # Add animals
    my_farm.add_animal(Cow("Bessie", 5))
    my_farm.add_animal(Cow("Daisy", 4))
    my_farm.add_animal(Chicken("Clucker", 2))
    my_farm.add_animal(Chicken("Pecky", 1))
    my_farm.add_animal(Chicken("Fluffy", 1))
    my_farm.add_animal(Sheep("Wooly", 3))
    my_farm.add_animal(Sheep("Cotton", 3))
    my_farm.add_animal(Sheep("Fleece", 2))
    my_farm.add_animal(Sheep("Sheary", 2))
    my_farm.add_animal(Sheep("Lana", 4))

    # Add structures
    my_farm.add_structure(FarmStructure("Red Barn", "Barn"))
    my_farm.add_structure(FarmStructure("Hen Palace", "Coop"))

    # Show results
    my_farm.show_population()
    print()
    my_farm.list_structures()
    print()
    my_farm.daily_routine()
