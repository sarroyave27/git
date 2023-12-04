diccionario = ['casa', 'pescado', 'calamar', 'monigote', 'codigopiton']

tablero, palabra, letras_erroneas = inicializar_juego(diccionario) # paso 1
while len(letras_erroneas) < len(simbolos): # pasos 7 y 8
    mostrar_escenario(len(letras_erroneas)) # paso 2
    mostrar_tablero(tablero, letras_erroneas) # paso 3
    letra = pedir_letra(tablero, letras_erroneas) # paso 4
    procesar_letra(letra, palabra, tablero, letras_erroneas) #paso 5

else:
    print(f'¡Lo siento! ¡Has perdido! La palabra a adivinar era {palabra}.')
    mostrar_escenario(len(letras_erroneas)) #paso 7

mostrar_tablero(tablero, letras_erroneas)