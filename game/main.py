import random#global

def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input("Escoge piedra, papel o tijera: ")
  user_option = user_option.lower()
  if not user_option in options:
    print("Porfavor escoge una opción adecuada.")
    # continue
    return None, None
  computer_option = random.choice(options)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print(computer_option)
    print("¡Empataste con la computadora!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("La computadora escogió", computer_option)
      print("¡Tú ganas!, piedra le gana a tijera.")
      user_wins += 1
    else:
      print("La computadora escogió", computer_option)
      print("¡Tú pierdes!, papel le gana a piedra.")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("La computadora escogió", computer_option)
      print("¡Tú ganas!, papel le gana a piedra.")
      user_wins += 1
    else:
      print("La computadora escogió", computer_option)
      print("¡Tú pierdes!, tijera le gana a papel.")
      computer_wins += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("La computadora escogió", computer_option)
      print("¡Tú ganas!, tijera le gana a papel.")
      user_wins += 1
    else:
      print("La computadora escogió", computer_option)
      print("¡Tú pierdes!, piedra le gana a tijera.") 
      computer_wins += 1
  return user_wins, computer_wins


def check_win(user_wins, computer_wins):
  if computer_wins == 2:
    print("El rotundo ganador es la COMPUTADORA (2 victorias).")
    return True
  elif user_wins == 2:
    print("El rotundo ganador eres TÚ (2 victorias).")
    return True


def run_game():  
  rounds = 1 # Contador de rondas.
  computer_wins = 0 # Contador de wins cpu.
  user_wins = 0 # Contador de wins usuario.
  while True: # Para que las sisguientes instrucciones se ejecuten automáticamente con iniciar el programa se comienza con un ciclo while True:.
# Tarea1: Obtener las opciones del usuario y la computadora.
    print("*" * 10)
    print("ROUND:", rounds)
    print("*" * 10)

    print("Wins de la computadora:", computer_wins)
    print("Wins del usuario:", user_wins)
#Función choose_options: para determinar las opciones del usuario y la computadoral. Al nombrar a la variable con el nombre de dos variables creadas anteriormente separadas con una coma, el valor de la variable son ambas opciones separadas. Retorna el valor de la opción de la computadora y el usuario.
    user_option, computer_option = choose_options()
    
#Función check_rules: incluye toda la lógica del juego piedra papel o tijera. Retorna la cantidad de veces que gana tanto el usuario como la computadora. 
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
  
#Función check_win: se utiliza para detener el juego. Retorna valores booleanos que indican si ganó el usuario o la computadora.
    resultado = check_win(user_wins, computer_wins)
    rounds+= 1
# Se utilizan valores booleanos para detener la ejecución del programa al alcanzar 2 victorias, ya sea por parte del usuario o de la computadora.
    if resultado == True:
      break
    else:
      continue
    

if __name__ == '__main__':
  run_game()