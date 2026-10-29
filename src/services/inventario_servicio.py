class InventarioServicio:
    def __init__(self, insumo_dao):
        self.insumo_dao = insumo_dao

    def evaluar_stock(self, nombre_insumo):
        '''logica para evaluar el stock de un insumo, considerando que:
            1. si la diferencia entre el stock y el umbral es menor a 1, entonces es bajo stock.
            2. si la diferencia entre el stock y el umbral es 0, entonces es necesario reabastecer.
            3. si la diferencia entre el stock y el umbral es mayor a 1, entonces hay stock suficiente.
        '''
        insumo = self.insumo_dao.buscar_por_nombre(nombre_insumo)
        if (insumo.stock - insumo.umbral) <= 1 :
            if (insumo.stock - insumo.umbral) == 0:
                return 'Limite de Stock. Se necesita reabastecer.' 
            return 'Bajo Stock'
        if (insumo.stock - insumo.umbral) > 1:
                    return 'En Stock'
    
