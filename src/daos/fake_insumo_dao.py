# dao falso pruebas
from models.insumo import Insumo
from models.ingrediente import Ingrediente
from models.marca import Marca
from models.tipo_insumo import TipoInsumo

class FakeInsumoDAO:
    def __init__(self):
    # simulando una tabla mysl usando un diccionario 
    # Instancias de catalogos base (Marca y TipoInsumo)
        marca_a = Marca(num=1, nombre="Marca A")
        marca_b = Marca(num=2, nombre="Marca B")
        tipo_veg = TipoInsumo(clave="VEG", nombre="Vegetal")
        tipo_carne = TipoInsumo(clave="CAR", nombre="Carnes")

        # instancias de Insumo (objeto de almacen independiente)
        insumo_tomate = Insumo(
            num=1,
            nombre="Tomate Verde",
            fecha_compra="2026-10-01",
            fecha_caducidad="2026-11-15",
            precio_unitario=25.0,  # aprox por kg
            umbral=5,              
            stock=5,
            unidad_medida="kg",
            tipo_insumo=tipo_veg,
            marca=marca_a
        )

        insumo_ribeye = Insumo(
            num=2,
            nombre="Carne Ribeye",
            fecha_compra="2026-10-20",
            fecha_caducidad="2026-11-05",
            precio_unitario=380.00, # aprox por kg
            umbral=2,               # Alerta si hay menos de 2 kg
            stock=5,
            unidad_medida="kg",
            tipo_insumo=tipo_carne,
            marca=marca_b
        )

        # Diccionario simulando la tabla de insumos
        self._tabla_insumos = {
            1: insumo_tomate,
            2: insumo_ribeye
        }

    def buscar_por_id(self, num_insumo):
        """Simula un SELECT * FROM insumos WHERE num = ?"""
        return self._tabla_insumos.get(num_insumo, None)

    def buscar_por_nombre(self, nombre_insumo):
        for insumo in self._tabla_insumos.values():
            if insumo.nombre == nombre_insumo:
                return insumo

    def obtener_todos(self):
        """Simula un SELECT * FROM insumos"""
        return list(self._tabla_insumos.values())

    def actualizar_stock(self, insumo_actualizado):
        """Simula un UPDATE insumos SET stock = ? WHERE num = ?"""
        if insumo_actualizado.num in self._tabla_insumos:
            self._tabla_insumos[insumo_actualizado.num] = insumo_actualizado
            print(f"[BD SIMULADA] Stock de {insumo_actualizado.nombre} actualizado a {insumo_actualizado.stock}")