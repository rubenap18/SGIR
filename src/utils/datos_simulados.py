# src/utils/datos_simulados.py

from models.tipo_insumo import TipoInsumo
from models.marca import Marca
from models.insumo import Insumo
from models.ingrediente import Ingrediente
from models.receta import Receta
from models.platillo import Platillo
from models.menu import Menu

def generar_recetas():
    # =====================================================================
    # 1. CATÁLOGOS BASE (Compartidos)
    # =====================================================================
    tipo_veg = TipoInsumo(clave="VEG", nombre="Vegetal")
    tipo_lac = TipoInsumo(clave="LAC", nombre="Lácteo")
    tipo_car = TipoInsumo(clave="CAR", nombre="Cárnico")
    tipo_aba = TipoInsumo(clave="ABA", nombre="Abarrotes")
    tipo_prep = TipoInsumo(clave="PREP", nombre="Preparación Interna") # Para la salsa
    
    marca_generica = Marca(num=1, nombre="Generica")
    marca_premium = Marca(num=2, nombre="Marca premiun")

    # =====================================================================
    # 2. INSUMOS FISICOS DE ALMACEN (no tienen fk a la receta)
    # =====================================================================
    # Insumos Crudos
    insumo_tomate = Insumo(num=1, nombre="Tomate Roma (Caja 10kg)", stock=20, unidad_medida="kg", tipo_insumo=tipo_veg, marca=marca_generica, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=10.0, umbral=10)
    insumo_ajo = Insumo(num=2, nombre="Ajo Pelado", stock=2, unidad_medida="kg", tipo_insumo=tipo_veg, marca=marca_generica, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=20.0, umbral=1)
    insumo_harina = Insumo(num=3, nombre="Harina de Trigo (Bulto 25kg)", stock=50, unidad_medida="kg", tipo_insumo=tipo_aba, marca=marca_generica, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=16.0, umbral=25)
    insumo_queso = Insumo(num=4, nombre="Queso Mozzarella", stock=15, unidad_medida="kg", tipo_insumo=tipo_lac, marca=marca_premium, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=16.0, umbral=5)
    insumo_peperoni = Insumo(num=5, nombre="Peperoni Rebanado", stock=8, unidad_medida="kg", tipo_insumo=tipo_car, marca=marca_premium, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=14.0, umbral=4)
    insumo_pasta = Insumo(num=6, nombre="Láminas Lasaña", stock=10, unidad_medida="kg", tipo_insumo=tipo_aba, marca=marca_premium,fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=40.0, umbral=7)
    insumo_carne_molida = Insumo(num=7, nombre="Carne Molida Res 80/20", stock=12, unidad_medida="kg", tipo_insumo=tipo_car, marca=marca_generica,fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=30.0, umbral=7)
    
    # Insumo Preparado (es la salsa ya hecha y guardada en refrigeraciion)
    #insumo_salsa_lista = Insumo(num=8, nombre="Salsa de Tomate Base (Litros)", stock=15, unidad_medida="L", tipo_insumo=tipo_prep, marca=marca_generica,fecha_compra=None, fecha_caducidad=None,precio_unitario=0.0, umbral=8)
    # =====================================================================
    # 3. INGREDIENTES LOGICOS DE COCINA (tienen la fk al insumo)
    # =====================================================================
    ing_tomate = Ingrediente(num=1, nombre="Tomate", insumo=insumo_tomate)
    ing_ajo = Ingrediente(num=2, nombre="Ajo", insumo=insumo_ajo)
    ing_harina = Ingrediente(num=3, nombre="Harina", insumo=insumo_harina)
    ing_queso = Ingrediente(num=4, nombre="Queso Mozzarella", insumo=insumo_queso)
    ing_peperoni = Ingrediente(num=5, nombre="Peperoni", insumo=insumo_peperoni)
    ing_pasta = Ingrediente(num=6, nombre="Pasta para Lasaña", insumo=insumo_pasta)
    ing_carne = Ingrediente(num=7, nombre="Carne Molida", insumo=insumo_carne_molida)
    
    # =====================================================================
    # 4. RECETAS (instanciacion y composicion)
    # =====================================================================
    
    # --- RECETA 1: Salsa Base (Ingrediene que actua como Receta) ---
    instrucciones_salsa = {
        1: "Hervir los tomates por 10 minutos.",
        2: "Licuar el tomate junto con el ajo y especias.",
        3: "Sofreír y reducir a fuego lento."
    }
    receta_salsa = Receta(num=1, nombre="Producción: Salsa Base 10L", num_porciones=10, instrucciones=instrucciones_salsa)
    receta_salsa.agregarIngrediente(ingrediente=ing_tomate, cantidad=12.0, unidad_medida="kg")
    receta_salsa.agregarIngrediente(ingrediente=ing_ajo, cantidad=0.200, unidad_medida="kg")

    # El ingrediente que actua como receta (salsa preparada previamente)
    ing_salsa_lista = Ingrediente(num=8, nombre="Salsa Base Pizza", insumo=None, receta=receta_salsa)
    
    # --- RECETA 2: Pizza de Peperoni 
    instrucciones_pizza = {
        1: "Amasar la harina y formar la base.",
        2: "Esparcir la Salsa Base Pizza de manera uniforme.",
        3: "Agregar queso mozzarella y colocar el peperoni.",
        4: "Hornear a 250°C por 12 minutos."
    }
    receta_pizza = Receta(num=2, nombre="Pizza Peperoni Grande", num_porciones=1, instrucciones=instrucciones_pizza)
    receta_pizza.agregarIngrediente(ingrediente=ing_harina, cantidad=0.300, unidad_medida="kg")
    receta_pizza.agregarIngrediente(ingrediente=ing_salsa_lista, cantidad=0.150, unidad_medida="L") # Usa el insumo preparado
    receta_pizza.agregarIngrediente(ingrediente=ing_queso, cantidad=0.250, unidad_medida="kg")
    receta_pizza.agregarIngrediente(ingrediente=ing_peperoni, cantidad=0.100, unidad_medida="kg")
    # --- RECETA 3: Lasaña 
    instrucciones_lasana = {
        1: "Cocer las láminas de pasta.",
        2: "Guisar la carne molida con la salsa base de tomate.",
        3: "Alternar capas de pasta, carne y queso.",
        4: "Gratinar en horno a 200°C por 20 minutos."
    }
    receta_lasana = Receta(num=3, nombre="Lasaña Clásica", num_porciones=1, instrucciones=instrucciones_lasana)
    receta_lasana.agregarIngrediente(ingrediente=ing_pasta, cantidad=0.200, unidad_medida="kg")
    receta_lasana.agregarIngrediente(ingrediente=ing_carne, cantidad=0.350, unidad_medida="kg")
    receta_lasana.agregarIngrediente(ingrediente=ing_salsa_lista, cantidad=0.200, unidad_medida="L") # También usa la salsa
    receta_lasana.agregarIngrediente(ingrediente=ing_queso, cantidad=0.200, unidad_medida="kg")
    # Retornamos el diccionario que fungirá como nuestra "BD" simnulada
    return [receta_lasana,receta_pizza,receta_salsa]

def generar_insumos():
    # =====================================================================
    # 1. CATÁLOGOS BASE (Compartidos)
    # =====================================================================
    tipo_veg = TipoInsumo(clave="VEG", nombre="Vegetal")
    tipo_lac = TipoInsumo(clave="LAC", nombre="Lácteo")
    tipo_car = TipoInsumo(clave="CAR", nombre="Cárnico")
    tipo_aba = TipoInsumo(clave="ABA", nombre="Abarrotes")
    tipo_prep = TipoInsumo(clave="PREP", nombre="Preparación Interna") # Para la salsa
    
    marca_generica = Marca(num=1, nombre="Generica")
    marca_premium = Marca(num=2, nombre="Marca premiun")
    
    # =====================================================================
    # 2. INSUMOS FISICOS DE ALMACEN (no tienen fk a la receta)
    # =====================================================================
    # Insumos Crudos
    insumo_tomate = Insumo(num=1, nombre="Tomate Roma (Caja 10kg)", stock=20, unidad_medida="kg", tipo_insumo=tipo_veg, marca=marca_generica, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=10.0, umbral=10)
    insumo_ajo = Insumo(num=2, nombre="Ajo Pelado", stock=2, unidad_medida="kg", tipo_insumo=tipo_veg, marca=marca_generica, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=20.0, umbral=1)
    insumo_harina = Insumo(num=3, nombre="Harina de Trigo (Bulto 25kg)", stock=50, unidad_medida="kg", tipo_insumo=tipo_aba, marca=marca_generica, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=16.0, umbral=25)
    insumo_queso = Insumo(num=4, nombre="Queso Mozzarella", stock=15, unidad_medida="kg", tipo_insumo=tipo_lac, marca=marca_premium, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=16.0, umbral=5)
    insumo_peperoni = Insumo(num=5, nombre="Peperoni Rebanado", stock=8, unidad_medida="kg", tipo_insumo=tipo_car, marca=marca_premium, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=14.0, umbral=4)
    insumo_pasta = Insumo(num=6, nombre="Láminas Lasaña", stock=10, unidad_medida="kg", tipo_insumo=tipo_aba, marca=marca_premium,fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=40.0, umbral=7)
    insumo_carne_molida = Insumo(num=7, nombre="Carne Molida Res 80/20", stock=12, unidad_medida="kg", tipo_insumo=tipo_car, marca=marca_generica,fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=30.0, umbral=7)

    lista_insumos = []
    lista_insumos.append(insumo_tomate)
    lista_insumos.append(insumo_ajo)
    lista_insumos.append(insumo_harina)
    lista_insumos.append(insumo_queso)
    lista_insumos.append(insumo_peperoni)
    lista_insumos.append(insumo_pasta)
    lista_insumos.append(insumo_carne_molida)

    return lista_insumos

def generar_ingredientes():
    # =====================================================================
    # 1. CATÁLOGOS BASE (Compartidos)
    # =====================================================================
    tipo_veg = TipoInsumo(clave="VEG", nombre="Vegetal")
    tipo_lac = TipoInsumo(clave="LAC", nombre="Lácteo")
    tipo_car = TipoInsumo(clave="CAR", nombre="Cárnico")
    tipo_aba = TipoInsumo(clave="ABA", nombre="Abarrotes")
    tipo_prep = TipoInsumo(clave="PREP", nombre="Preparación Interna") # Para la salsa
    
    marca_generica = Marca(num=1, nombre="Generica")
    marca_premium = Marca(num=2, nombre="Marca premiun")

    # =====================================================================
    # 2. INSUMOS FISICOS DE ALMACEN (no tienen fk a la receta)
    # =====================================================================
    # Insumos Crudos
    insumo_tomate = Insumo(num=1, nombre="Tomate Roma (Caja 10kg)", stock=20, unidad_medida="kg", tipo_insumo=tipo_veg, marca=marca_generica, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=10.0, umbral=10)
    insumo_ajo = Insumo(num=2, nombre="Ajo Pelado", stock=2, unidad_medida="kg", tipo_insumo=tipo_veg, marca=marca_generica, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=20.0, umbral=1)
    insumo_harina = Insumo(num=3, nombre="Harina de Trigo (Bulto 25kg)", stock=50, unidad_medida="kg", tipo_insumo=tipo_aba, marca=marca_generica, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=16.0, umbral=25)
    insumo_queso = Insumo(num=4, nombre="Queso Mozzarella", stock=15, unidad_medida="kg", tipo_insumo=tipo_lac, marca=marca_premium, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=16.0, umbral=5)
    insumo_peperoni = Insumo(num=5, nombre="Peperoni Rebanado", stock=8, unidad_medida="kg", tipo_insumo=tipo_car, marca=marca_premium, fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=14.0, umbral=4)
    insumo_pasta = Insumo(num=6, nombre="Láminas Lasaña", stock=10, unidad_medida="kg", tipo_insumo=tipo_aba, marca=marca_premium,fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=40.0, umbral=7)
    insumo_carne_molida = Insumo(num=7, nombre="Carne Molida Res 80/20", stock=12, unidad_medida="kg", tipo_insumo=tipo_car, marca=marca_generica,fecha_compra='2026-10-30', fecha_caducidad='2026-11-29',precio_unitario=30.0, umbral=7)
    
    # Insumo Preparado (es la salsa ya hecha y guardada en refrigeraciion)
    #insumo_salsa_lista = Insumo(num=8, nombre="Salsa de Tomate Base (Litros)", stock=15, unidad_medida="L", tipo_insumo=tipo_prep, marca=marca_generica,fecha_compra=None, fecha_caducidad=None,precio_unitario=0.0, umbral=8)
    # =====================================================================
    # 3. INGREDIENTES LOGICOS DE COCINA (tienen la fk al insumo)
    # =====================================================================
    
    ing_tomate = Ingrediente(num=1, nombre="Tomate", insumo=insumo_tomate)
    ing_ajo = Ingrediente(num=2, nombre="Ajo", insumo=insumo_ajo)
    ing_harina = Ingrediente(num=3, nombre="Harina", insumo=insumo_harina)
    ing_queso = Ingrediente(num=4, nombre="Queso Mozzarella", insumo=insumo_queso)
    ing_peperoni = Ingrediente(num=5, nombre="Peperoni", insumo=insumo_peperoni)
    ing_pasta = Ingrediente(num=6, nombre="Pasta para Lasaña", insumo=insumo_pasta)
    ing_carne = Ingrediente(num=7, nombre="Carne Molida", insumo=insumo_carne_molida)

    # --- RECETA 1: Salsa Base (Ingrediene que actua como Receta) ---
    instrucciones_salsa = {
        1: "Hervir los tomates por 10 minutos.",
        2: "Licuar el tomate junto con el ajo y especias.",
        3: "Sofreír y reducir a fuego lento."
    }
    receta_salsa = Receta(num=1, nombre="Producción: Salsa Base 10L", num_porciones=10, instrucciones=instrucciones_salsa)
    receta_salsa.agregarIngrediente(ingrediente=ing_tomate, cantidad=12.0, unidad_medida="kg")
    receta_salsa.agregarIngrediente(ingrediente=ing_ajo, cantidad=0.200, unidad_medida="kg")

    # El ingrediente que actua como receta (salsa preparada previamente)
    ing_salsa_lista = Ingrediente(num=8, nombre="Salsa Base Pizza", insumo=None, receta=receta_salsa)

    return [ing_tomate,ing_ajo,ing_harina,ing_queso,ing_peperoni,ing_pasta,ing_carne,ing_salsa_lista]