class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type if pet_type in self.PET_TYPES else Exception()
        self.owner = owner
        Pet.all.append(self)
        
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, type):
        if type in self.PET_TYPES:
            self._pet_type = type
        else:
            raise Exception()

class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [p for p in Pet.all if self == p.owner]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception()

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda p: p.name)