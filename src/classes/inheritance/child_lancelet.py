from src.classes.inheritance.base_amoeba import Amoeba


class Lancelet(Amoeba):
    organisation: str = "multi-cell"
    support: str = "notochord"
    
    @classmethod
    def describe(cls):
        description = super().describe()
        return description + f' It has {cls.support} for support.'
    
    @staticmethod
    def move(direction: str):
        print(f'Moves to the {direction} with muscles')
        
    def eat(self, subject: str):
        print(f'{self.name.capitalize()} filter water'
              f' to eat {subject}')
    
    
    
if __name__ == "__main__":
    print(Lancelet.describe())
    # Output: Lancelet has multi-cell organization and lives in water
    
    lancelet = Lancelet('Amphioxus')
    lancelet.move('right')
     # Output: Moves to the right with muscles
    lancelet.eat('organic particles')
     # Output: Amphioxus filters water to eat organic particles
     