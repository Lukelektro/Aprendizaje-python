from random import randint

# Genera un numero del 1-10
random_number = randint(1, 10)

guesses_left = 3
# el while cumple la funcion de loop, en texto diría: si guesses_left es mayor a 0, imprime en pantalla  un input que 
# tome un valor entero, si este valor es igual al numero aleatorio generado, imprime en pantalla que ganaste, si no es así
# imprime que perdiste, en el if hay un "break" que significa que romperá el loop en el cual esta el codigo y el guesses_left
# es el que resta los intentos dados en la variable de arriba.
while guesses_left > 0:
  guess = int(input("Your guess: "))
  if guess == random_number:
    print ("You win!")
    break
  guesses_left -= 1
else:
  print ("You lose.")



 # otra manera de hacer loops es con el for, abajo explicado
print ("Counting...")

for i in range(20):
  print (i)

# la primera vez que usé esta forma de loopear hize una manera ineficiente del codigo, pero funcional
# lo hize de la siguiente manera:
hobbies = []

for i in range(3):
 hob1 = input("Cual es tu primer hobbie?: ")
 hobbies.append(hob1)
 hob2 = input("Cual es tu segundo hobbie: ")
 hobbies.append(hob2)
 hob3 = input("Cual es tu tercer hobbie?: ")
 hobbies.append(hob3)

print (hobbies)

# es una manera ineficiente de utilizarlo y está mal hecho, ya que repitirá un total de 9 variables, y yo solo buscaba
# 3 variables, pero es una manera funcional asi que igualmente la anotaré, el siguiente codigo es el que tuve que usar:
hobbies = []

for num in range(3):
  hobby =  input("Tell me one of your favorite hobbies: ")
  hobbies.append(hobby)

print (hobbies)

# igualmente este codigo a simple vista genera una impresion que no cambia, por lo cual si quieres escribir distintos
# mensajes no sirve, asi que bueno yo igual usaria el primero, pero no da para el caso de un loop.

thing = "spam!"

for c in thing:
  print (c)

word = "eggs!"

for a in word:
  print (a)

# usos del loop: operaciones en una lista.
numbers  = [7, 9, 12, 54, 99]

print ("This list contains: ")

for num in numbers:
  print (num)

for num in numbers:
  print (num ** 2)  