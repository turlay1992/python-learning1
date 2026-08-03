class Amoeba(object):
    """docstring for Amoeba."""
    organisation: str = 'single-cell'
    habitation: str = 'water'
    
    def __init__(self, name: str):
        super(Amoeba, self).__init__()
        self.name: str = name
    
    @classmethod
    def describe(cls):
        return (f'{cls.__name__} has {cls.organisation} organisation'
                f' and lives in {cls.habitation}.')
    
    @staticmethod
    def move(direction: str):
        print(f'Moves to the {direction} with pseudopodia')
        
    def eat(self, subject: str):
        print(f'{self.name.capitalize()} grows pseudopodia'
              f' to eat {subject}')
        
        
if __name__ == "__main__":
    print(Amoeba.describe())
    # Output: Amoeba has single-cell organization and lives in water
    amoeba = Amoeba('proteus')
    amoeba.move('left')
     # Output: Moves to the left with pseudopodia
    amoeba.eat('bacteria')
     # Output: Proteus grows pseudopodia to eat bacteria
    