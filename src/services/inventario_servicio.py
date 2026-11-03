from models.receta import Receta

class InventarioServicio:
    def __init__(self, insumo_dao,receta_dao):
        self._insumo_dao = insumo_dao
        self._receta_dao = receta_dao

    def evaluar_stock_insumo(self, numero_insumo:int):
        '''logica para evaluar el stock de un insumo, considerando que:
            1. si la diferencia entre el stock y el umbral es menor a 1, entonces es bajo stock.
            2. si la diferencia entre el stock y el umbral es 0, entonces es necesario reabastecer.
            3. si la diferencia entre el stock y el umbral es mayor a 1, entonces hay stock suficiente.
        '''
        insumo = self._insumo_dao.buscar_por_id(numero_insumo)

        if (insumo.stock - insumo.umbral) > 1:
            return 'En Stock'  
        if(insumo.stock < insumo.umbral):
            return 'Muy bajo stock. Es necesario reabastecer.'
        if (insumo.stock - insumo.umbral) <= 1 :
            if (insumo.stock - insumo.umbral) == 0:
                return 'Limite de Umbral. Se necesita reabastecer.' 
            return 'Bajo Stock'

    def abastecer_insumo(self, num_insumo:int, cantidad:int):
        ''' en este caso se descuenta la cantidad de stock al insumo especificado.
            En general, los insumos usan como unidades de medida standard el KG.
        '''
        # validando que la cantidad sea mayor a 0
        if cantidad <= 0:
            return 'Cantidad invalida. Debe ser mayor a 0.'
        
        insumo = self._insumo_dao.buscar_por_id(num_insumo)
        # validando que el insumo exista en la BD.
        if insumo == False:
            return 'No existe dicho insumo.'

        stock_actualizado = insumo.stock + cantidad
        self._insumo_dao.actualizar_stock(num_insumo,stock_actualizado) 

    def _usar_insumo(self, num_insumo:int, cantidad:int):
        ''' en este caso se descuenta la cantidad de stock al insumo especificado.
            En general, los insumos usan como unidades de medida standard el KG y L o g y ml.
        '''
        # validando que la cantidad sea mayor a 0
        if cantidad <= 0:
            return 'Cantidad invalida. Debe ser mayor a 0.'
        
        insumo = self._insumo_dao.buscar_por_id(num_insumo)
        # validando que el insumo exista en la BD.
        if insumo == False:
            return 'No existe dicho Insumo.'

        stock_actualizado = insumo.stock - cantidad
        #validando que halla stock disponible para descontar
        if stock_actualizado < 0:
            return 'Stock insuficiente en el almacen.'
        self._insumo_dao.actualizar_stock(num_insumo,stock_actualizado) 

    def preparar_receta(self, numero_receta:int):
        '''
        1. Recibir los ingredientes de una receta
        2. Perdir al Dao los insumos de los ingredientes
        3. Descontar a cada insumo la cantidad utilizada para la receta
        '''
        receta:Receta = self._receta_dao.buscar_por_id(numero_receta)
        '''
        Por cada Ingrediente_Receta de la lista_ingredientes de la receta, 
        se descuenta la cantidad de ese ingrediente que se usa en la receta, 
        el cual tiene relacionado al insumo. 
        Es decir, se descuenta del Insumo, no del Ingrediente.
        '''
        for ingrediente_receta in receta.lista_ingredientes:
            cantidad_a_usar = ingrediente_receta.cantidad
            self._usar_insumo(num_insumo=ingrediente_receta.ingrediente.insumo.num, cantidad=cantidad_a_usar)

    def get_insumo(self, num_insumo:int):
        return self._insumo_dao.buscar_por_id(num_insumo)

    def get_receta(self, num_receta:int):
        return self._receta_dao.buscar_por_id(num_receta)

    def get_ingrediente(self, num_ingrediente:int):
        return self._receta_dao.buscar_ingrediente_por_id(num_ingrediente)

    def get_todos_los_insumos(self):
        return self._insumo_dao.obtener_todos()