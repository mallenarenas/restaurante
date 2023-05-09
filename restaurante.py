#############################################################
from random import choice, shuffle
## Si necesita agregar imports, debe agregarlos aquí arriba ##



### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre: str, platos: list, cocineros: list, repartidores: list):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0

    def __str__(self):
        return f"El Restaurante {self.nombre} ha sido creado. "

    def recibir_pedidos(self, clientes):
        calificaciones = []
        print("")
        print(f"Bienvenido al restaurante {self.nombre}.\n")
        print("Hoy trabajan los cocineros:") 
        for cocinero in self.cocineros:
            print(f"Nombre: {cocinero.nombre} Energía: {cocinero.energia} y Habilidad: {cocinero.habilidad}") 
        print(f"Tambien están los siguientes repartidores:")  
        for repartidor in self.repartidores:
            print(f"Nombre: {repartidor.nombre} Energía: {repartidor.energia} y Tiempo de entrega: {repartidor.tiempo_entrega}")

        print(f"Los clientes para atender son: {', '.join(cliente.nombre for cliente in clientes)}" )
        print("-"*50) 
        for cliente in clientes:
            pedido = []
            print("")
            print(f"Se está atendiendo al/la cliente: {cliente.nombre}\nSus platos preferidos son: {', '.join(plato for plato in cliente.platos_preferidos.keys())}.")
            for plato in cliente.platos_preferidos.values():
                
                while True:
                    i = choice(range(len(self.cocineros)))
                    if self.cocineros[i].energia > 0:
                        print(f"El plato {plato[0]} será elaborado por el/la cocinero/a {self.cocineros[i].nombre}, con energía {self.cocineros[i].energia}")
                        plato_cocinado = self.cocineros[i].cocinar(plato)
                        pedido.append(plato_cocinado)
                        print(f"El plato {plato_cocinado.nombre} se elaboró con calidad {plato_cocinado.calidad}")
                        break
                    else:
                        self.cocineros.remove(self.cocineros[i])
                        
            
            j = choice([0,1])
            if self.repartidores[j].energia > 0:
                print(f"Este pedido será repartido por el/la repartidor/a: {self.repartidores[j].nombre}, con energía: {self.repartidores[j].energia}")
                demora = self.repartidores[j].repartir(pedido)
                print(f"El pedido tendrá una demora de {demora} segundos")
                calificacion_cliente = cliente.recibir_pedido(pedido,demora)
                calificaciones.append(calificacion_cliente)
                print(f"{cliente.nombre} ha calificado el restaurante con nota {calificacion_cliente}\n")
                print("-"*50)
            elif self.repartidores[1-j].energia > 0:
                print(f"Este pedido será repartido por el/la repartidor/a: {self.repartidores[1-j].nombre}, con energía: {self.repartidores[1-j].energia}")
                demora = self.repartidores[1-j].repartir(pedido)
                print(f"El pedido tendrá una demora de {demora} segundos")
                calificacion_cliente = cliente.recibir_pedido(pedido,demora)
                calificaciones.append(calificacion_cliente)
                print(f"{cliente.nombre} ha calificado el restaurante con nota {calificacion_cliente}\n")
                print("-"*50)
            else:
                print(f"No hay repartidores el pedido no puede ser despachado")
                calificacion_cliente = cliente.recibir_pedido([], 0)
                calificaciones.append(calificacion_cliente)
                print(f"{cliente.nombre} ha calificado el restaurante con nota {calificacion_cliente}\n")
                print("-"*50)
                    
        self.calificacion = sum(calificaciones)/len(calificaciones)
                        

            
            

### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
