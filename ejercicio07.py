class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.set_titular(titular)
        self._cantidad = cantidad

    def set_titular(self, titular):
        if isinstance(titular, Persona):
            self._titular = titular
        else:
            raise ValueError("El titular debe ser una instancia de la clase Persona.")

    def get_titular(self):
        return self._titular

    def get_cantidad(self):
        return self._cantidad

    def mostrar(self):
        print(f"Titular: {self.get_titular().get_nombre()}, Cantidad: {self.get_cantidad()}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self._cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser positiva.")


class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres.")

    def get_nombre(self):
        return self._nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un entero positivo.")

    def get_edad(self):
        return self._edad

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 8:  # Asumiendo un DNI de 8 caracteres
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de 8 caracteres.")

    def get_dni(self):
        return self._dni

    def mostrar(self):
        print(
            "Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, DNI: {self.get_dni()}"
        )

    def es_mayor_de_edad(self):
        return self.get_edad() >= 18


# Utilizacion de las entidades
if __name__ == "__main__":
    try:
        persona1 = Persona("Mauro", 45, "28937942")
        cuenta1 = Cuenta(persona1, 1000.0)

        cuenta1.mostrar()

        cuenta1.ingresar(500000.0)
        cuenta1.mostrar()

        cuenta1.retirar(200000.0)
        cuenta1.mostrar()

        cuenta1.ingresar(-100000.0)

        cuenta2 = Cuenta("Ana", 2000.0)
    except ValueError as e:
        print(e)
