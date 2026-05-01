# -*- coding: utf-8 -*-
"""
Actividad Asincrónica: POO en Python con Herencia, Composición, Encapsulamiento
"""

import datetime

# ------------------------------------------------------------
# Clase Motor (Composición)
# ------------------------------------------------------------
class Motor:
    def __init__(self, tipo, potencia):
        self._tipo = tipo
        self._potencia = potencia
        self._encendido = False

    # Propiedades y setters
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        if isinstance(value, str) and value.strip():
            self._tipo = value
        else:
            raise ValueError("El tipo del motor debe ser un texto válido")

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._potencia = value
        else:
            raise ValueError("La potencia debe ser un número positivo")

    # Métodos de comportamiento
    def encender_motor(self):
        if not self._encendido:
            self._encendido = True
            print(f"🔧 Motor {self._tipo} de {self._potencia} HP encendido.")
        else:
            print("⚠️ El motor ya estaba encendido.")

    def detener_motor(self):
        if self._encendido:
            self._encendido = False
            print(f"🔧 Motor {self._tipo} apagado.")
        else:
            print("⚠️ El motor ya estaba apagado.")

    def __str__(self):
        return f"Motor(tipo={self._tipo}, potencia={self._potencia} HP)"


# ------------------------------------------------------------
# Superclase Vehiculo
# ------------------------------------------------------------
class Vehiculo:
    def __init__(self, marca, modelo, anio, motor):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._motor = motor   # Composición: un vehículo TIENE un motor
        self._encendido = False

    # Propiedades y setters
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        if isinstance(value, str) and value.strip():
            self._marca = value
        else:
            raise ValueError("La marca debe ser un texto válido")

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        if isinstance(value, str) and value.strip():
            self._modelo = value
        else:
            raise ValueError("El modelo debe ser un texto válido")

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        if isinstance(value, int) and 1886 <= value <= datetime.datetime.now().year + 1:
            self._anio = value
        else:
            raise ValueError("Año inválido")

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value):
        if isinstance(value, Motor):
            self._motor = value
        else:
            raise TypeError("El motor debe ser un objeto de la clase Motor")

    # Métodos de comportamiento
    def encender(self):
        if not self._encendido:
            self._encendido = True
            self._motor.encender_motor()
            print(f"🚗 {self._marca} {self._modelo} encendido.")
        else:
            print("⚠️ El vehículo ya estaba encendido.")

    def apagar(self):
        if self._encendido:
            self._encendido = False
            self._motor.detener_motor()
            print(f"🚗 {self._marca} {self._modelo} apagado.")
        else:
            print("⚠️ El vehículo ya estaba apagado.")

    def __str__(self):
        return f"{self.__class__.__name__}: {self._marca} {self._modelo} ({self._anio}) | {self._motor}"


# ------------------------------------------------------------
# Clase Automovil (Hereda de Vehiculo)
# ------------------------------------------------------------
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, numero_puertas):
        super().__init__(marca, modelo, anio, motor)
        self._numero_puertas = numero_puertas

    @property
    def numero_puertas(self):
        return self._numero_puertas

    @numero_puertas.setter
    def numero_puertas(self, value):
        if isinstance(value, int) and value >= 2:
            self._numero_puertas = value
        else:
            raise ValueError("El número de puertas debe ser al menos 2")

    # Métodos de comportamiento específicos
    def abrir_maletero(self):
        print(f"🔓 Maletero del {self.marca} {self.modelo} abierto.")

    def tocar_claxon(self):
        print(f"📢 ¡Piiiiiiii! (Claxon del {self.marca} {self.modelo})")

    def __str__(self):
        return super().__str__() + f" | Puertas: {self._numero_puertas}"


# ------------------------------------------------------------
# Clase Motocicleta (Hereda de Vehiculo)
# ------------------------------------------------------------
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, cilindraje):
        super().__init__(marca, modelo, anio, motor)
        self._cilindraje = cilindraje

    @property
    def cilindraje(self):
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, value):
        if isinstance(value, (int, float)) and value >= 50:
            self._cilindraje = value
        else:
            raise ValueError("El cilindraje debe ser >= 50 cc")

    # Métodos de comportamiento específicos
    def hacer_caballito(self):
        print(f"🏍️ ¡{self.marca} {self.modelo} haciendo caballito! (Habilidad riesgosa)")

    def usar_patada_arranque(self):
        print(f"🦵 Aplicando patada de arranque en la {self.marca} {self.modelo}.")

    def __str__(self):
        return super().__str__() + f" | Cilindraje: {self._cilindraje} cc"


# ------------------------------------------------------------
# Clase Principal (ejecución del programa)
# ------------------------------------------------------------
def main():
    print("=" * 60)
    print("SISTEMA DE VEHÍCULOS - POO con Herencia y Composición")
    print(f"Fecha y hora: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Crear motores
    motor1 = Motor("Gasolina", 120)
    motor2 = Motor("Eléctrico", 80)
    motor3 = Motor("Gasolina", 45)
    motor4 = Motor("Diesel", 150)

    # Crear 2 automóviles
    auto1 = Automovil("Toyota", "Corolla", 2022, motor1, 4)
    auto2 = Automovil("Tesla", "Model 3", 2023, motor2, 4)

    # Crear 2 motocicletas
    moto1 = Motocicleta("Honda", "Wave", 2021, motor3, 110)
    moto2 = Motocicleta("Yamaha", "MT-07", 2024, motor4, 689)

    # Mostrar estado inicial con __str__
    print("\n--- VEHÍCULOS CREADOS ---")
    print(auto1)
    print(auto2)
    print(moto1)
    print(moto2)

    # Ejecutar métodos de comportamiento
    print("\n--- DEMOSTRACIÓN DE COMPORTAMIENTOS ---")
    
    print("\n[Automóvil 1]")
    auto1.encender()
    auto1.tocar_claxon()
    auto1.abrir_maletero()
    auto1.apagar()
    
    print("\n[Automóvil 2]")
    auto2.encender()
    auto2.tocar_claxon()
    auto2.apagar()
    
    print("\n[Motocicleta 1]")
    moto1.encender()
    moto1.hacer_caballito()
    moto1.usar_patada_arranque()
    moto1.apagar()
    
    print("\n[Motocicleta 2]")
    moto2.encender()
    moto2.hacer_caballito()
    moto2.apagar()

    print("\n--- MOSTRANDO OBJETOS NUEVAMENTE CON __str__ ---")
    print(auto1)
    print(auto2)
    print(moto1)
    print(moto2)

    print("\n✅ Ejecución completada exitosamente.")


if __name__ == "__main__":
    main()
