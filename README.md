<img width="920" height="173" alt="image" src="https://github.com/user-attachments/assets/a6b9b508-890c-43da-9a95-fee50a4abd2f" />
<img width="920" height="406" alt="image" src="https://github.com/user-attachments/assets/08a9282e-20eb-4e2f-aec7-680a04749e41" />
<img width="919" height="250" alt="image" src="https://github.com/user-attachments/assets/93bff7d7-860d-4e12-8b0c-f5e5390b005a" />
<img width="920" height="570" alt="image" src="https://github.com/user-attachments/assets/1ae88976-5576-4b71-8ac6-df4ecf1a91f7" />
<img width="920" height="492" alt="image" src="https://github.com/user-attachments/assets/551a57ba-9b9c-4a08-b362-14faf0491fba" />
<img width="528" height="136" alt="image" src="https://github.com/user-attachments/assets/73e5f6b6-0cf2-400e-ba71-a01cf977e682" />
<img width="920" height="355" alt="image" src="https://github.com/user-attachments/assets/d58624cf-df5c-45da-bc7c-cae1055c4fdf" />
<img width="920" height="355" alt="image" src="https://github.com/user-attachments/assets/8667769d-982a-49c0-8b95-173d720c1591" />
<img width="920" height="231" alt="image" src="https://github.com/user-attachments/assets/65b7a62a-81e9-4ea5-a3e9-f4d0a6d83967" />
<img width="920" height="617" alt="image" src="https://github.com/user-attachments/assets/d1e8cee1-ca53-4313-8dcf-08db96ade346" />
<img width="920" height="506" alt="image" src="https://github.com/user-attachments/assets/b9b27d09-d4d4-4e40-ad0e-753423d47a71" />
<img width="920" height="267" alt="image" src="https://github.com/user-attachments/assets/e12ea07c-647f-445c-a463-ba24fda1c595" />

Sistema de Gestión de Inventario - Taller TDD
Este proyecto implementa un sistema simplificado de gestión de inventario en memoria utilizando la metodología TDD (Test-Driven Development). El objetivo es asegurar la calidad del software mediante el ciclo de desarrollo orientado a pruebas.

🚀 Metodología Aplicada: Ciclo TDD
Para cada funcionalidad, se respetaron rigurosamente las tres fases del TDD:

Fase Red (Rojo): Escritura de una prueba unitaria que falla inicialmente, ya que la funcionalidad aún no existe. Esto define el comportamiento esperado.

Fase Green (Verde): Implementación del código mínimo necesario para que la prueba pase exitosamente en la terminal.

Fase Refactor (Refactorización): Optimización y limpieza del código para hacerlo más eficiente y profesional, garantizando que todas las pruebas sigan pasando.

🛠️ Funcionalidades Desarrolladas
A continuación se describen los módulos implementados en el Punto 2 de la actividad:

1. Registrar Producto
Descripción: Permite crear una nueva entrada en el diccionario de memoria.

TDD: Se inició con una prueba de inserción fallida. Tras pasar a verde, se refactorizó para asegurar que la estructura del objeto sea consistente.

2. Consultar Producto
Descripción: Retorna los datos detallados de un producto específico buscando por su nombre (clave).

TDD: La fase roja identificó la falta del método de búsqueda. En la fase verde se logró recuperar el dato y en el refactor se mejoró la gestión de la información retornada.

3. Actualizar Stock
Descripción: Modifica el atributo de cantidad de un producto existente.

TDD: Se probó la actualización de valores numéricos. Tras lograr que la prueba pasara, se optimizó la lógica de asignación para mantener la integridad del diccionario.

4. Listar Inventario
Descripción: Devuelve una colección con todos los objetos almacenados en el sistema.

TDD: Se validó que el tamaño de la lista devuelta coincidiera con los registros insertados. El refactor se centró en presentar los datos de forma limpia (formato lista).

📋 Requisitos e Instalación
Para ejecutar las pruebas de este proyecto, se requiere:

Python 3.x

Pytest (Framework de pruebas)

Bash
# Instalación de pytest
pip install pytest

# Ejecución de las pruebas
pytest test_inventario.py
🧠 Reflexión Final
El uso de TDD en este taller permitió identificar errores de lógica antes de que el código fuera complejo, facilitando un diseño limpio y funcional orientado al cumplimiento de requisitos técnicos.

Autores: Kerin Royo / Bryam Serge
Ficha: 3067863 - ADSO
