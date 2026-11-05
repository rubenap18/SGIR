from models.venta import Venta
from models.menu import Menu
from models.menu import DetalleMenu
from models.venta import Consumo
from models.platillo import Platillo

class VentasServicio:
    def __init__(self, venta_dao,platillo_dao):
        self._insumo_dao = venta_dao
        self._receta_dao = platillo_dao

    def realizar_venta(self):
        pass

    def obtener_venta(self):
        pass

    def calcular_monto_total_venta(self, venta:Venta, menu:Menu):
        monto_total = 0
        for consumo in venta.detalles:
            monto_total += self.calcular_importe_consumo(consumo.platillo.num,menu,consumo.cantidad_platillos)

        return monto_total

    def calcular_importe_consumo(self, num_platillo:int, menu:Menu ,cantidad_platillos:int):
        '''calcula el importe de un platillo'''
        if cantidad_platillos == 0: return 0
        if cantidad_platillos < 0: return  0

        precio_platillo = 0
        for detalle_menu in menu.detalles:
            if num_platillo == detalle_menu.platillo.num:
                precio_platillo = detalle_menu.precio
        # validando que el platillo exista, si es 0, entonces nunca se encontró el platillo.
        if precio_platillo == 0: return 0

        # el importe es igual a el precio del platillo por la cantidad de ellos que se consumieron
        return precio_platillo * cantidad_platillos

    