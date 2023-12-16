import random

class Humanoids:
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

class Humans(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.choose_attribute_bonus()

    def choose_attribute_bonus(self):
        attribute_options = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        print("You are a Human! You can add +2 to one of the following attributes:")
        for i, attribute in enumerate(attribute_options, 1):
            print(f"{i}. {attribute}")

        choice = int(input("Enter the number corresponding to your choice: "))
        setattr(self, attribute_options[choice - 1], getattr(self, attribute_options[choice - 1]) + 2)

class Elves(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.resistance_to_sleep = 100
        self.dexterity += 2
        self.charisma += 2

class Dwarves(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.resistance_to_magic = 20
        self.strength += 2
        self.constitution += 2
        self.charisma -= 2

def characterCreation():
    race = input("Choose your race (Human/Elf/Dwarf): ").capitalize()
    height = random.randint(36, 84)  # Height in inches (3ft - 7ft)
    weight = random.randint(60, 300)  # Weight in pounds (60lbs - 300lbs)
    hair_color = random.choice(['white', 'silver', 'gray', 'black', 'brown', 'green', 'blue', 'yellow', 'pink', 'red', 'blonde'])
    eye_color = random.choice(['white', 'black', 'red', 'green', 'blue', 'brown', 'purple', 'amber'])

    if race == "Human":
        character = Humans(height, weight, hair_color, eye_color, 0, 0, 0, 0, 0, 0)
    elif race == "Elf":
        character = Elves(height, weight, hair_color, eye_color, 0, 0, 0, 0, 0, 0)
    elif race == "Dwarf":
        character = Dwarves(height, weight, hair_color, eye_color, 0, 0, 0, 0, 0, 0)
    else:
        print("Invalid race choice. Please choose Human, Elf, or Dwarf.")
        return

    print(f"\nYour character details:\n"
          f"Race: {race}\n"
          f"Height: {height} inches\n"
          f"Weight: {weight} lbs\n"
          f"Hair Color: {hair_color}\n"
          f"Eye Color: {eye_color}\n"
          f"Strength: {character.strength}\n"
          f"Dexterity: {character.dexterity}\n"
          f"Constitution: {character.constitution}\n"
          f"Intelligence: {character.intelligence}\n"
          f"Wisdom: {character.wisdom}\n"
          f"Charisma: {character.charisma}\n")

if __name__ == "__main__":
    def main():
        characterCreation()

    main()
