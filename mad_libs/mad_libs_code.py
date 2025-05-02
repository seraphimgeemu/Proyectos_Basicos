# En este primer Proyecto Realizaremos el Juego Mad Libs

lista_palabras = ['nombre femenino','numero','adjetivo femenino','adjetivo femenino','hora',
                  'lugar con un articulo','numero','verbo en 3 persona','adverbio',
                  'comida','bebida','sustantivo masculino','adjetivo masculino'
                  ,'numero 2 o mas','sustantivo femenino plural', 'adjetivo femenino plural'
                  ,'sustantivo masculino singular','adjetivo masculino singular']
respuestas = []
for pregunta in lista_palabras:
    respuestas.append(input(f'Ingrese el siguiente dato "{pregunta}": '))

print(f'''
            ! La fiesta de Cumpleaños !
   --Hoy el cumple años de {respuestas[0]}.
   !Cumple {respuestas[1]} años! Ella quiere tener una
   fiesta muy {respuestas[2]} y {respuestas[3]}. La fiesta empieza a las {respuestas[4]} en
   {respuestas[5]}. Vienen {respuestas[6]} invitados. En la fiesta, primero todos {respuestas[7]}
   muy {respuestas[8]}. Despues, comen {respuestas[9]} y beben {respuestas[10]}. Finalmente {respuestas[0]}
   Puede abrir sus regalos. Su mejor amigo le regala un
   {respuestas[11]}, {respuestas[12]}. Su vecino le regala {respuestas[13]} {respuestas[14]} {respuestas[15]}. El mejor regalo
   de todos es un {respuestas[16]} {respuestas[17]}. !Feliz cumpleaños!, {respuestas[0]}
''')
