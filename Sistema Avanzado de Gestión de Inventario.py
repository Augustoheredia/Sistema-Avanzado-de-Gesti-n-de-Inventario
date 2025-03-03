#Establecemos la clase de producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id

    def establecer_id(self, id):
        self.id = id

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

#Establemos la clase de inventario
import json

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}  # Diccionario para almacenar productos (id: Producto)
        self.archivo = archivo
        self.cargar_inventario()

    def agregar_producto(self, producto):
        self.productos[producto.obtener_id()] = producto
        self.guardar_inventario()

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            self.guardar_inventario()
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.obtener_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("Inventario vacío.")

    def guardar_inventario(self):
        with open(self.archivo, 'w') as archivo:
            productos_serializados = {id: producto.__dict__ for id, producto in self.productos.items()}
            json.dump(productos_serializados, archivo, indent=4)

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as archivo:
                productos_serializados = json.load(archivo)
                self.productos = {id: Producto(**datos) for id, datos in productos_serializados.items()}
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Creando uno nuevo.")
            self.guardar_inventario()
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. El archivo podría estar corrupto.")

#Establecemos el interfaz de usuario
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()