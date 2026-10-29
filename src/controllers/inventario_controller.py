class InventarioController():
    def __init__(self, inventario_service):
        super().__init__()
        self.service = inventario_service

    def evaluar_inventario_insumo(self, nombre_insumo:str):
        return self.service.evaluar_stock(nombre_insumo)

