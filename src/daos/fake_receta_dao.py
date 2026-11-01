# Importación de los modelos (Asegúrense de que las rutas coincidan con su proyecto)
from models.tipo_insumo import TipoInsumo
from models.marca import Marca
from models.insumo import Insumo
from models.ingrediente import Ingrediente
from models.receta import Receta
import utils.datos_simulados 

class FakeRecetaDAO:    
    def __init__(self):
        self._tabla_recetas = utils.datos_simulados.generar_datos()
    # =====================================================================
    # 5. METODOS DEL DAO (Simulan de consultas SQL)
    # =====================================================================
    def buscar_por_id(self, num_receta):
        """Simula un SELECT * FROM recetas WHERE num = ? JOIN ..."""
        return self._tabla_recetas.get(num_receta, None)

    def obtener_todas(self):
        """Simula un SELECT * FROM recetas JOIN ..."""
        return list(self._tabla_recetas.values())