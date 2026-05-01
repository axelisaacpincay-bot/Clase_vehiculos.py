# Clase_vehiculos.py
# Sistema de Vehículos - POO en Python

## 📌 Descripción
Sistema orientado a objetos que implementa:
- **Encapsulamiento** con @property y @setter
- **Herencia** (Vehiculo → Automovil, Motocicleta)
- **Composición** (Vehiculo tiene un Motor)
- **Métodos de comportamiento**
- **Sobrescritura** de `__str__()`

### Motor
- Atributos: tipo, potencia
- Métodos: encender_motor(), detener_motor()

### Vehiculo (Superclase)
- Atributos: marca, modelo, año, motor
- Métodos: encender(), apagar()

### Automovil (Hereda de Vehiculo)
- Atributo adicional: numero_puertas
- Métodos: abrir_maletero(), tocar_claxon()

### Motocicleta (Hereda de Vehiculo)
- Atributo adicional: cilindraje
- Métodos: hacer_caballito(), usar_patada_arranque()
