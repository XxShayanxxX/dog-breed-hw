class Dog:
    def __init__(self, breed, size, lifespan):
        self.breed = breed
        self.size = size
        self.lifespan = lifespan


dog1 = Dog("Labrador Retriever", "Large", 12)
dog2 = Dog("Husky", "Medium-Large", 14)


print("Dog 1 Breed:", dog1.breed)
print("Dog 1 Size:", dog1.size)
print("Dog 1 Lifespan:", dog1.lifespan, "years")

print("Dog 2 Breed:", dog2.breed)
print("Dog 2 Size:", dog2.size)
print("Dog 2 Lifespan:", dog2.lifespan, "years")

