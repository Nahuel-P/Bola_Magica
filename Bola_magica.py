import random

respuestas=["En mi opinión, sí", "Es cierto", "Es decididamente así", "Probablemente","Buen pronóstico", "Todo apunta a que sí",
            "Sí","Sí - definitivamente", "Debes confiar en ello", "Respuesta vaga, vuelve a intentarlo","Pregunta en otro momento", 
            "Será mejor que no te lo diga ahora", "No puedo predecirlo ahora", "Concéntrate y vuelve a preguntar", "Puede ser",
            "No cuentes con ello","Mi respuesta es no","Mis fuentes me dicen que no","Las perspectivas no son buenas", "Muy dudoso"]
entrada_o_salida=input("Presiona ENTER para agitar la bola magica. Escribe SALIR para salir: ")

while(entrada_o_salida.lower()!="salir"):
    if entrada_o_salida=="":
        pregunta=input("Cual es tu pregunta? \n")
        print(random.choice(respuestas))
        entrada_o_salida=input("Presiona ENTER para agitar la bola magica. Escribe SALIR para salir: ")
    elif not(entrada_o_salida.lower()=="salir" or entrada_o_salida==""):
        print("No ingresaste algo valido")
        entrada_o_salida=input("Presiona ENTER para agitar la bola magica. Escribe SALIR para salir: ")
print("Adios!")