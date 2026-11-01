from models.tipo_insumo import TipoInsumo
from models.marca import Marca
from models.insumo import Insumo
from models.ingrediente import Ingrediente
from models.receta import Receta
import utils.datos_simulados 

class FakeRecetaDAO:    
    def __init__(self):
        self._tabla_recetas: list[Receta] = utils.datos_simulados.generar_recetas()  # type: ignore
        self._tabla_ingredientes: list[Ingrediente] = utils.datos_simulados.generar_ingredientes()

    # =====================================================================
    # 5. METODOS DEL DAO (Simulan de consultas SQL)
    # =====================================================================
    def buscar_por_id(self, num_insumo):
            """Simula un SELECT * FROM receta WHERE num = ?"""
            for receta in self._tabla_recetas:
                if receta.num == num_insumo:
                    return receta
            return False
    
    def buscar_por_nombre(self, nombre_insumo:str):
        for receta in self._tabla_recetas:
            if receta.nombre == nombre_insumo:
                return receta
        return False
        
    def obtener_todos(self):
        """Simula un SELECT * FROM receta"""
        return self._tabla_recetas

    def buscar_ingrediente_por_id(self, num_ingrediente:int):
        """Simula un SELECT * FROM receta WHERE num = ?"""
        for ingrediente in self._tabla_ingredientes:
            if ingrediente.num == num_ingrediente:
                return ingrediente
        return False

    def obtener_todos_ingredientes(self):
        return self._tabla_ingredientes

