class InventarioServicio:
    def __init__(self, insumo_dao):
        self.insumo_dao = insumo_dao

    def evaluar_stock(self, nombre_insumo):
        #logica
        insumo = self.insumo_dao.buscar_por_nombre('Tomate Verde')
        if (insumo.stock - insumo.umbral) <= 1 :
            if (insumo.stock - insumo.umbral) == 0:
                return 'Limite de Stock. Se necesita reabastecer.' 
            return 'Bajo Stock'
        if (insumo.stock - insumo.umbral) > 1:
                    return 'En Stock'
    
