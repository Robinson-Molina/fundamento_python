## Las excepciones se producen durante la ejecución del código. Los errores de sintaxis no generan una excepción, pues se detectan durante el análisis del código y no en tiempo de ejecución:
""""
"""" Comentar todo las excepciones """"
# Excepcion ZeroDivisionError: division by zero

def media(*args):
    return sum(args)/len(args)

media()

a=2
assert a%2 ==1

# ValueError
def test (num):
    if(num < 0):
        return num

test(-1)

def retest(num):
    if test(num) > 100:
        print('OK')

retest(-1)

with EXPR as VAR:
    BLOCK

VAR = EXPR
VAR.__enter__()
    try:
        BLOCK
    finally:
        VAR.__exit__()
"""


"""
# tratamiento


def media(*args):
    if len(args) == 0:
        raise TypeError ('media: excepted at least 1 arguments, got 0')
        return sum(args)/len(args)
# assert
a=2
assert a%2 ==1, 'variable a incorrecta'
media()


# ValueError
def test (num):
    if(num < 0):
        raise ValueError ('El nùmero es negativo')
        return num

test(-1)

def retest(num):
    if test(num) > 100:
        raise ValueError ('El nùmero es negativo')
        print('OK')

retest(-1)

with open('ejemplo.txt') as archivo:

    content = archivo.read()

for line in open('ejemplo.txt'):
    pass


"""
# manejar Excepciones
def test (num):
    if(num < 0):
        raise ValueError ('El nùmero es negativo')
        return num

num = -1

try:
    num = test(num)
except:
    num = 0
    #raise ValueError ("El nùmero es negativo")

try:
    pass
except TypeError as e:  

    """Procesamiento para este tipo de excepción"""    
except ValueError as e:
    """Procesamiento para este tipo de excepción"""
except Exception as e:

    """Procesamiento para los demás tipos de excepción"""

def f(num):
    try:
        return test(num)
    except:
        return 0
    finally:
        print("Siempre se ejecuta")

f(-1)

try:
    # establecimiento de conexión con una base de datos
    pass
except:
    # se muestra un mensaje que pide verificar la conexión
    pass
else:
    try:
        # se envía una consulta
        pass
    except:
        # se muestra un mensaje con la consulta
        pass
    else:
        # se recupera el resultado en una variable
        pass
    finally:
        pass
        # se cierra la conexión a la base de dato

with open('ejemplo1.txt') as f1, open('ejemplo2.txt', 'w') as f2:
    for l in f1:
        f2.write(l)

## funciones Asincronas
###########################
async def envio_peticion(servidor, accion):
    """Cuerpo de la función asíncrona"""
    pass

async def recuperar_informacion():
    return await envio_peticion("localhost:8844", "/info")

async def get_cursor(db):
    async with db.transaction():
        return await db.fetch('SELECT * from mi_tabla')

async def read_data(cursor):
    async for row in cursor:
        print(row)
    else:
        print('there is no row')