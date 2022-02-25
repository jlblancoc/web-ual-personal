Title: Google Drive File Stream: Cómo cambiar permanentemente la letra de la unidad
Date: 2018-06-18 10:00

La nueva aplicación [Google File Stream](https://support.google.com/a/answer/7491144?hl=es)
sustituyó este año a _Google Drive Desktop_ para los usuarios _G Suite_ (empresas) de _Google Drive_.

Drive File Stream hace que todos los archivos de Drive aparezcan como si fueran
una nueva unidad de disco de red, así que podemos explorar, abrir, editar, etc.
todos los documentos de forma (casi) totalmente transparente, como si estuvieran
en nuestro propio ordenador.

Un problema importante con el uso de esta unidad es que, por alguna razón,
la letra usada por la unidad _"Mi Unidad"_ de _Google File Stream_ **cambia
cada vez que arrancas el PC**.

Estos son los pasos para arreglarlo y **asignar una letra de forma permanente**
a dicha unidad de disco.

## Cómo cambiar la letra de la unidad Google File Stream

Antes de nada, si tu equipo usa alguna aplicación de "congelado", asegúrate de
descongelarlo antes de las siguientes operaciones.

### Paso 1: Cerrar la aplicación Google File Stream.

Para eso pulsamos este botón del menú de la aplicación, entrando por el icono del
espacio de notificaciones:

![Quit Drive FS]({static}/imgs/2018-01/1_gsuite_quit.png)

### Paso 2: Abrir el editor del registro

Pulsar tecla de Windows para abrir menú inicio; escribir `regedit` para
encontrar el editor del registro y ejecutarlo. Os pedirá permisos de
administración, que hay que aceptar.

### Paso 3: Crear una entrada en el registro

En el árbol de la izquierda, busca y selecciona la entrada:

	HKEY_LOCAL_MACHINE
	 |
	 |-> SOFTWARE
	     |
		 | -> Google
		      |
			  | -> DriveFS

En el espacio de la derecha, pulsa el botón derecho y crea una nueva entrada
de tipo cadena de texto (`REG_SZ`) con **nombre** `DefaultMountPoint` y **valor**
el de la letra que se desea, por ejemplo, yo uso `Y:`.

Deberías ver algo parecido a:

![DriveFS regedit]({static}/imgs/2018-06/gdrive_regedit.png)

### Paso 4: todo listo, ¡a probarlo!

Abre el menú inicio y escribe _Drive file stream_ para ejecutarlo de nuevo.
