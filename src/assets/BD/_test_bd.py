import sqlite3
import pytest
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Fixture para crear la base de datos de pruebas
@pytest.fixture
def conexion_db():
    conn = sqlite3.connect(':memory:')  # Crear base de datos en memoria
    cursor = conn.cursor()

    # Crear la tabla Clientes
    cursor.execute('''
    CREATE TABLE Clientes (
        ClienteID INTEGER PRIMARY KEY,
        SaldoVol DECIMAL,
        Periodo TEXT
    )
    ''')

    # Insertar datos de prueba
    clientes_data = [
        (1, 100.0, '2023-01'),
        (2, -50.0, '2023-02'),
        (3, 200.0, '2023-03')
    ]
    cursor.executemany('INSERT INTO Clientes (ClienteID, SaldoVol, Periodo) VALUES (?, ?, ?)', clientes_data)
    conn.commit()

    # Devolver la conexión para las pruebas
    yield conn  

    # Cerrar la conexión al finalizar la prueba
    conn.close()

# Test para validar clientes con SaldoVol positivo
def test_clientes_saldo_positivo(conexion_db):
    cursor = conexion_db.cursor()
    cursor.execute("SELECT ClienteID FROM Clientes WHERE SaldoVol > 0")
    resultados = cursor.fetchall()

    # Validamos que sólo hay dos clientes con saldo positivo
    assert len(resultados) == 2
    assert resultados[0][0] == 1
    assert resultados[1][0] == 3

# Test para validar que un cliente no tiene saldo negativo
def test_clientes_saldo_negativo(conexion_db):
    cursor = conexion_db.cursor()
    cursor.execute("SELECT ClienteID FROM Clientes WHERE SaldoVol < 0")
    resultado = cursor.fetchone()

    # Validamos que sólo el cliente 2 tiene saldo negativo
    assert resultado[0] == 2

# Test para validar el periodo correcto
def test_clientes_periodo(conexion_db):
    cursor = conexion_db.cursor()
    cursor.execute("SELECT Periodo FROM Clientes WHERE ClienteID = 1")
    resultado = cursor.fetchone()

    # Validamos que el cliente 1 tiene el periodo '2023-01'
    assert resultado[0] == '2023-01'

def test_caso_negativo(conexion_db):
    logging.info("Este es un mensaje de información donde se quiere ver un caso erroneo")
    assert 3 == 4
    logging.error("Este es un mensaje de error.")
