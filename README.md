# Taller-3

Guia para instalar MongoDB y Pymongo en Windows 
Para instalar MongoDB y PyMongo, primero debes asegurarte de que tu sistema cumple con los requisitos necesarios. En Windows, puedes descargar el instalador MSI desde la página oficial de MongoDB, ejecutarlo y seguir las instrucciones, asegurándote de habilitar la opción para ejecutarlo como un servicio si quieres que se inicie automáticamente. Luego, puedes verificar la instalación abriendo una terminal y ejecutando mongod --version. Si MongoDB no se ejecuta automáticamente, puedes iniciarlo manualmente con mongod en una terminal y luego abrir otra para ejecutar mongo y acceder a la base de datos. 

Para instalar PyMongo, la biblioteca de Python para conectarse con MongoDB, simplemente ejecuta pip install pymongo en la terminal. Para comprobar que se instaló correctamente, abre Python e importa PyMongo con import pymongo, luego imprime su versión con print(pymongo.__version__). Si todo funciona sin errores, significa que la instalación fue exitosa.
