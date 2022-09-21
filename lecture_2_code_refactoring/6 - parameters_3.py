def print_pet_names(owner, **pets):
    print(f"Owner Name: {owner}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")


if __name__ == '__main__':
    # print_pet_names(owner="Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
    print_pet_names(dog="Brock", owner="Jonathan", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
