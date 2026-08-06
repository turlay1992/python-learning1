from src.classes.inheritance.child_lancelet import Lancelet


class Clownfish(Lancelet):
    support: str = 'Sceleton'
    """docstring for Clownfish."""
    
    def __init__(self, name: str, feeding_type: str, water_type: str):
        super().__init__(name)
        self.feeding_type: str = feeding_type
        self.water_typy: str = water_type
        self.hidden: bool = False
    
    def hide(self, place: str) -> None:
        self.hidden = True
        print(f'{self.name.capitalize()} hides in ' 
              f'the {place} being in the '
              f'{self.water_typy} water')
        
    def reveal(self) -> None:
        self.hidden = False
        self.move('forward')
        
    def eat(self, subject):
        print(f"{self.name.capitalize()} eats {subject} "
              f"since it is {self.feeding_type}")
        
        
if __name__ == "__main__":
    print(Clownfish.describe())
    # Output: Clownfish has multi-cell organization and lives in water. It has skeleton for support.
    clownfish = Clownfish(
        name="Amphiprion",
        feeding_type="omnivorous",
        water_type="salt"
    )
    clownfish.move("left")
    # Output: Moves to the left with muscles
    clownfish.eat("zooplankton")
    # Output: Amphiprion eats zooplankton since it is omnivorous
    clownfish.hide("anemone")
    # Output: Amphiprion hides in the anemone being in the salt water
    clownfish.reveal()
    # Output: Moves to the forward with muscles
    print(f"Clownfish is {'resting' if clownfish.hidden else 'swimming'}")
    # Output: Clownfish is swimming