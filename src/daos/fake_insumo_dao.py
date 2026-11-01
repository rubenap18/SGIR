# dao falso pruebas
from models.insumo import Insumo
from models.ingrediente import Ingrediente
from models.marca import Marca
from models.tipo_insumo import TipoInsumo
import utils.datos_simulados

class FakeInsumoDAO:
    def __init__(self):
        self._tabla_insumos: list[Insumo] = utils.datos_simulados.generar_insumos()

    def buscar_por_id(self, num_insumo):
        """Simula un SELECT * FROM insumos WHERE num = ?"""
        for insumo in self._tabla_insumos:
            if insumo.num == num_insumo:
                return insumo
        return False

    def buscar_por_nombre(self, nombre_insumo:str):
        for insumo in self._tabla_insumos:
            if insumo.nombre == nombre_insumo:
                return insumo
        return False
        
    def obtener_todos(self):
        """Simula un SELECT * FROM insumos"""
        return self._tabla_insumos

    def actualizar_stock(self, num_insumo:int, stock_actualizado:float):
        """Simula un UPDATE insumos SET stock = ? WHERE num = ?"""
        for insumo in self._tabla_insumos:
            if insumo.num == num_insumo:
                insumo.stock = stock_actualizado