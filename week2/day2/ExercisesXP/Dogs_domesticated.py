#3

from ExercisesXP import Dog
import random

class PetDog(Dog):
    def __init__(self,name,age,weight,trained = 'False') -> None:
        super().__init__(name,age,weight)
        self.trained = trained

    def train(self):
        print(self.bark())  
        self.trained = 'True'

    def play(self,*args):
        dog_names = ','.join(args)
        print(f'{dog_names} all play together')

    def do_a_trick(self):
        tricks = [
            f"{self.name} does a barrel roll",
            f"{self.name} stands on his back legs",
            f"{self.name} shakes your hand",
            f"{self.name} plays dead"
        ]
        if self.trained:
            print(random.choice(tricks))
        else:
            print('The dog not trained')
pet_dog = PetDog('Foxy',3,10)
pet_dog.train()  
pet_dog.play('Caesar','Banny','Misha') 
pet_dog.do_a_trick()         

