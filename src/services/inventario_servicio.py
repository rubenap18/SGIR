from models.receta import Receta



class InventarioServicio:
    def __init__(self, insumo_dao,receta_dao):
        self.__insumo_dao = insumo_dao
        self.__receta_dao = receta_dao

    def evaluar_stock_insumo(self, nombre_insumo:str):
        '''logica para evaluar el stock de un insumo, considerando que:
            1. si la diferencia entre el stock y el umbral es menor a 1, entonces es bajo stock.
            2. si la diferencia entre el stock y el umbral es 0, entonces es necesario reabastecer.
            3. si la diferencia entre el stock y el umbral es mayor a 1, entonces hay stock suficiente.
        '''
        insumo = self.__insumo_dao.buscar_por_nombre(nombre_insumo)
        if (insumo.stock - insumo.umbral) <= 1 :
            if (insumo.stock - insumo.umbral) == 0:
                return 'Limite de Stock. Se necesita reabastecer.' 
            return 'Bajo Stock'
        if (insumo.stock - insumo.umbral) > 1:
                    return 'En Stock'  

    def actualizar_inventario(self, num_insumo:int, cantidad:int):
        ''' en este caso se descuenta la cantidad de stock al insumo especificado.
            En general, los insumos usan como unidades de medida standard el KG.
        '''
        insumo = self.__insumo_dao.buscar_por_id(num_insumo)
        insumo.stock = insumo.stock - cantidad
        self.__insumo_dao.actualizar_stock(insumo) 

    def preparar_receta(self, numero_receta:int):
        '''
        1. Recibir los ingredientes de una receta
        2. Perdir al Dao los insumos de los ingredientes
        3. Descontar a cada insumo la cantidad utilizada para la receta
        '''

        receta:Receta = self.__receta_dao.bucar_por_id(numero_receta)
        for ingrediente in receta.lista_ingredientes:
            print(ingrediente.nombre)

