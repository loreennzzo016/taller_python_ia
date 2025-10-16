import random

colores = ['rojo', 'azul', 'verde', 'amarillo']
secuencia = []

for ronda in range(1, 6):
    secuencia.append(random.choice(colores))
    print('Secuencia:', ' '.join(secuencia))
    respuesta = input('Repítela: ').split()
    if respuesta != secuencia:
        print('¡Perdiste!')
        break
else:
    print('¡Ganaste todas las rondas!')
