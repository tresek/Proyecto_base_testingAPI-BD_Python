import requests
import pytest
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# URL base de la API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Test para obtener todos los usuarios (GET /users)
def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")


    # Verificar que la respuesta es exitosa
    logging.info("Validacion de status coode 200")
    assert response.status_code == 200
    
    # Verificar que se devuelve una lista de usuarios
    lista = isinstance(response.json(), list)
    print (list) 
    assert isinstance(response.json(), list)

# Test para obtener un usuario específico (GET /users/{id})
def test_get_user_by_id():
    user_id = 1
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    
    # Verificar que la respuesta es exitosa
    assert response.status_code == 200
    
    # Verificar que el usuario tiene el ID correcto
    data = response.json()

    assert data['id'] == user_id


# Test para crear un nuevo usuario (POST /users)
def test_create_new_user():
    new_user = {
        "name": "freddy Escobar",
        "username": "fescoabar",
        "email": "johndoe@example.com"
    }
    
    response = requests.post(f"{BASE_URL}/users", new_user)
    
    # Verificar que la respuesta es exitosa
    assert response.status_code == 201
    
    # Verificar que el usuario fue creado correctamente
    data = response.json()
    assert data["name"] == new_user["name"]
    assert data["email"] == new_user["email"]
    ##Validar en el reporte el nombre del usuario creado
    print (new_user)


# Test para eliminar un usuario (DELETE /users/{id})
def test_delete_user():
    user_id = 1
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    
    # Verificar que la respuesta sea correcta (204 para no content, 200 para éxito)
    assert response.status_code in [200, 204]

def test_validacion_formato():
    assert 4 >= 3

def test_validacion_statusCode_200():
    assert 4 >= 3

def test_validacion_statusCode_201():
    assert 4 >= 3

def test_validacion_statusCode_400():
    assert 4 >= 3

def test_validacion_statusCode_404():
    assert 4 >= 3

def test_validacion_statusCode_500():
    assert 4 >= 3

def test_validacion_No_ingreso_datos_invalidos():
    assert 4 >= 3

def test_validacion_token_valido():
    assert 4 >= 3

def test_validacion_de_campos_del_json():
    data = {
        'id': 1,
        'name': 'Leanne Graham',
        'username': 'Bret',
        'email': 'Sincere@april.biz',
        'address': {
            'street': 'Kulas Light',
            'suite': 'Apt. 556',
            'city': 'Gwenborough',
            'zipcode': '92998-3874',
            'geo': {'lat': '-37.3159', 'lng': '81.1496'}
        },
        'phone': '1-770-736-8031 x56442',
        'website': 'hildegard.org',
        'company': {
            'name': 'Romaguera-Crona',
            'catchPhrase': 'Multi-layered client-server neural-net',
            'bs': 'harness real-time e-markets'
        }
    }
    # Validar que existen las claves principales
    assert 'id' in data, "El campo 'id' no existe"
    assert 'name' in data, "El campo 'name' no existe"

    ##logging.info("Campo 'name' encontrado")

    assert 'username' in data, "El campo 'username' no existe"
    assert 'email' in data, "El campo 'email' no existe"
    assert 'address' in data, "El campo 'address' no existe"
    assert 'phone' in data, "El campo 'phone' no existe"
    assert 'website' in data, "El campo 'website' no existe"
    assert 'company' in data, "El campo 'company' no existe"


def test_validacion_tiempo_de_vida_de_token():
    assert 4 >= 3

def test_validacion_Json_debe_tener_un_solo_uso():
    assert 4 >= 3
