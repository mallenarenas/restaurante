##############################################################
from random import seed, randint, sample
from personas import Repartidor, Cocinero, Cliente
from restaurante import Restaurante
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 4 ###

def crear_repartidores():
    repartidores = []
    nombres = sample(NOMBRES,2)
    for nombre in nombres:
        repartidores.append(Repartidor(nombre, randint(20, 30)))
    return repartidores

def crear_cocineros():
    cocineros = []
    nombres = sample(NOMBRES,5)
    for nombre in nombres:
        cocineros.append(Cocinero(nombre, randint(1, 10)))
    return cocineros

def crear_clientes():
    clientes = []
    nombres = sample(NOMBRES,5)
    for nombre in nombres:
        platos_preferidos_keys = sample(sorted(INFO_PLATOS.keys()), randint(1,5))
        platos_preferidos = dict()
        for plato in platos_preferidos_keys:
            platos_preferidos[plato] = INFO_PLATOS[plato]
        clientes.append(Cliente(nombre, platos_preferidos))
    return clientes
    

def crear_restaurante():
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    return(Restaurante("Mama Mía", INFO_PLATOS, cocineros, repartidores))


### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Amaia", "Cristian", "Maggie", "Pablo", "Catalina", "Juan", "Sergio"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("With Love") 
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
