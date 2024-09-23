import pytest
import cx_Oracle
from assets.BD.config import ORACLE_DB

@pytest.fixture(scope='module')
def oracle_connection():
    """Establece una conexión a la base de datos Oracle antes de las pruebas."""
    dsn = "10.220.2.214:1521/TEST.sura.cl"
    try:
        # Establecer la conexión a la base de datos Oracle
        connection = cx_Oracle.connect(
        ORACLE_DB['username'],
        ORACLE_DB['password'],
        dsn=dsn 

        )
        print("Conexión establecida correctamente.")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        pytest.fail(f"Error al conectar a la base de datos: {error.message}")
    
    yield connection
    connection.close()

@pytest.fixture(scope='function')
def cursor(oracle_connection):
    """Proporciona un cursor para ejecutar consultas."""
    cursor = oracle_connection.cursor()
    yield cursor
    cursor.close()

'''def test_query_aaa_clientes(cursor):
    try:
         # Cambia al esquema correcto
        cursor.execute("ALTER SESSION SET CURRENT_SCHEMA = NEWAFP")
        cursor.execute("SELECT * FROM AAA_CLIENTES ac")
        rows = cursor.fetchall()
        
        assert len(rows) > 0, "No se encontraron registros en AAA_CLIENTES"
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        pytest.fail(f"Error al ejecutar la consulta: {error.message}")
'''
def test_query_aaa_clientes(cursor):
    """Consulta la tabla AAA_CLIENTES en el esquema NEWAFP, mostrando solo 10 registros."""
    try:
        # Cambiar el esquema
        cursor.execute("ALTER SESSION SET CURRENT_SCHEMA = NEWAFP")
        
        # Ejecutar la consulta limitando los resultados a 10
        cursor.execute("SELECT * FROM AAA_CLIENTES FETCH FIRST 10 ROWS ONLY")
        rows = cursor.fetchall()
        
        # Verificar que haya registros
        assert len(rows) > 0, "No se encontraron registros en AAA_CLIENTES"
        
        # Mostrar los 10 primeros clientes
        for row in rows:
            print(row)
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        pytest.fail(f"Error al ejecutar la consulta: {error.message}")

def test_validar_segmento_APTop_Saldo():
    print ("Se debe validar que si el segmento AP Top el Saldo >= 650 MM$, entonces coresponde a AP Top.")

def test_validar_segmento_Alto_Patrimonio():
    print ("Se debe validar que si el segmento Alto Patrimonio el Saldo >= 100 MM$, entonces corresponde a Alto Patrimonio.")

def test_validar_segmento_Primer_Alto():
    print ("Se debe validar que si el segmento Primer Alto el Saldo >= 55 MM$, entonces coresponde a Primer Alto.")

def test_validar_segmento_Primer_Clasico():
    print ("Se debe validar que si el segmento Prime Clasico el Saldo >= 20 MM$ o Flujo >= $500,000  entonces coresponde a Primer Clasico.")

def test_validar_segmento_Alto_Valor():
    print ("Se debe validar que si el segmento Alto Valor el Saldo >= $5.000.000 o Renta >= $1,700,000 o Flujo >= $100,000  entonces corresponde a Alto Valor.")

def test_validar_segmento_Rentas_Medias():
    print ("Se debe validar que si el segmento Rentas Medias el Saldo >= $100.000 o Renta >= $700,000 o Flujo >= $0  entonces corresponde a Rentas Medias.")

def test_validar_segmento_Clasico_Resto():
    print ("Se debe validar que si el segmento Clásico Resto corresponde a los clientes vigentes que no están en los otros segmentos.")

def test_validar_segmento_Debe_subir():
    print ("Se debe validar que si el cliente tiene tres cotizaciones y la renta en las tres es mayor debe subir de segmento")

def test_validar_segmento_Debe_bajar():
    print ("Se debe validar que si el cliente tiene tres cotizaciones y la renta en las tres es menor a la actual, debe bajar de segmento")

def test_validar_Que_ingrese_al_segmento():
    print ("Se debe validar que si el cliente ingrese al segmento si cumple con la condicion de AUM Vol (Ahorro Voluntario) definida por el segmento de forma inmediata.")

def test_validar_Que_cliente_baje_por_condiciones_de_Saldo():
    print ("Se debe validar que si el cliente baje de segmento si deja de cumplir con las condiciones de Saldo Vol (Saldo Voluntario) definida por 3 meses consecutivos")

def test_validar_Que_segmento_debe_ser_paramertrico():
    print ("Se debe validar que el nombre del segmento debe ser parametrico.")

def test_validar_Que_cortes_de_saldo_Renta_y_Flujo_deben_ser_paramertrico():
    print ("Se debe validar que los cortes de saldo, Renta y Flujo VOl. Deben ser parametricos.")

def test_validar_Primer_cliente_debe_ser_AP_Top():
    print ("Se debe validar que un cliente nuevo al primer segmento que debe ingresar es al de AP Top ")

def test_validar_No_debe_existir_un_cliente_fallecido():
    print ("Se debe validar que los cliente Fallecidos deben ser Excluidos")

def test_validar_No_debe_existir_un_cliente_Pensionado_nocotizante_y_sin_producto():
    print ("Se debe validar que los cliente Pensionados no cotizantes y sin productos voluntarios. deben ser Excluidos")

def test_validar_clientes_excluidos():  
    print ("Se debe validar que los cliente con productos vigentes, que no presenten Renta, Flujo Vol, Saldo Vol o Saldo Obligatorio (AUM APO) en el último mes.. deben ser Excluidos")


def test_validar_cliente_nuevo_asignarle_segmento():
    print ("Se debe validar que un cliente nuevo es posible asignarle segmento miestras cumpla con saldo vol > 0 y los tres periodos consecutivos.")