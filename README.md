# habi_dt_test

Para construir el primer microservicio utlizaremos el framework Flask. No se utilizara un ORM (como sqlalchemy, SQLALchemy u otro por el estilo) para las consultas. Dentro de cada endpoint de la API tendremos un query statement para poder realizar consultas.

Utilizaremos el linter flake8 para ayudarnos a seguir la guia de estilo definida en PEP8

DUDAS:  
tenia la duda en la instruccion número 6 se referia a guardar los filtros en un archivo json, asi que construi una funcion para esto. Puedes abrir el archivo filters.json despues de ejecutar una query, en ese archivo veras los parametros que manda el front

Las unit tests las realice con pytest.
Puedes correrlas abriendo la terminal y con el comando:  
python -m pytest -s -vv tests/test_api.py

o si quieres correr una en especifico como por ejemplo:test_get_resources:  
python -m pytest -s -vv tests/test_api.py::test_get_resources


Revisar visualmente con Postman o en el explorador
puedes intentar con algunas de las siguientes URL o tu puedes crear la tuyo con gusto:

http://127.0.0.1:5000/inmuebles?city=pereira&year=2020&state=pre_venta