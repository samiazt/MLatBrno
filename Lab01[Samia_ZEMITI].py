# Exercie 1.1

# Création de la liste pour stocker les lignes du motif
lines = []

# Ajouter les lignes ascendantes au motif
for i in range(1, 6):
    lines.append('X ' * i)

# Ajouter les lignes descendantes au motif
for i in range(4, 0, -1):
    lines.append('X ' * i)

# Joindre et imprimer le motif complet
print('\n'.join(lines))

# Ecercie 1.2

input_str = "n45as29@#8ss6"
total = 0 

for char in input_str :
    if char.isdigit():
        total +=int(char)
        
print (total)

# Exercice 1.3

def tobinary(number) :
    binary_number = ""
    while number > 0 :
        binary_number = str(number % 2) + binary_number
        number = number // 2
    return binary_number

print (tobinary(156))

# Exercice 1.4 

def fibonacci(upper_threshold: int) -> list:
    if upper_threshold <= 0:
        return [] 
    elif upper_threshold == 1:
        return [0]  
    fibo_list = [0, 1]
    # Calculer le prochain nombre de Fibonacci et vérifier s'il est inférieur au seuil
    next_fibo = fibo_list[-2] + fibo_list[-1]
    while next_fibo < upper_threshold:
        fibo_list.append(next_fibo)
        # Mettre à jour le prochain nombre de Fibonacci pour la prochaine itération
        next_fibo = fibo_list[-2] + fibo_list[-1]
    return fibo_list


# Exercice 1.5

import random

def rock_paper_scissors() -> None:
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()  # lower Makes it case-insensitive
    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It is a tie")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win")
    else:
        print("You lose")

rock_paper_scissors()
