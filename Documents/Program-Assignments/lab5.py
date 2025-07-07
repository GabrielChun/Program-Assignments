def cat_greeting(word):
    print(f'The cat says {word}')

cat_greeting('meow')

def generate_superhero_power():
    name = 'Hassan'
    power = 'Time Stop'
    print(f"{name}'s power is {power}")

generate_superhero_power()

def generate_superhero_power1():
    power = 'Time Stop'
    return power

print(generate_superhero_power1())

def generate_superhero_power2(user_name, power):
    return f"{user_name}'s power is {power}"

print(generate_superhero_power2('Meenice510', 'invisibility'))

def cat_greeting_loop():
    for i in range(5):
        print('Meow')

cat_greeting_loop()

def generate_multiple_powers(powers):
    for power in powers:
        print(f"Superpower: {power}")

generate_multiple_powers(['Super Strength', 'Super Speed', 'Invisibility'])