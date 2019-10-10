#importar libreria
import sqlite3

def borrar_tablas(db):
    """Recibe una conexión a una db en sqlite3. Elimina las tablas si existen."""

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS clientes")
    cursor.execute("DROP TABLE IF EXISTS productos")
    cursor.execute("DROP TABLE IF EXISTS colaboradores")
    cursor.execute("DROP TABLE IF EXISTS pedidos")
    cursor.execute("DROP TABLE IF EXISTS detalle_pedidos")
    cursor.execute("DROP TABLE IF EXISTS preferencias")
    cursor.execute("DROP TABLE IF EXISTS localizaciones")

    #Confirmar cambios
    db.commit()
    #Cerrar conexión
    cursor.close()

def crear_tabla_cliente(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla clientes"""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla clientes
    cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
        email TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        documento_identidad TEXT NULL,
        nombres TEXT NULL,
        apellido_paterno TEXT NULL,
        apellido_materno TEXT NULL,
        genero TEXT NULL,
        fecha_nacimiento DATETIME NULL,
        fecha_creacion DATETIME,
        estado TEXT NOT NULL,
        preferencias TEXT NULL)""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()


def crear_tabla_productos(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla productos"""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla productos
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
        codigo VARCHAR(8) PRIMARY KEY,
        nombre VARCHAR(250) NOT NULL,
        descripcion VARCHAR(1000) NOT NULL,
        precio_normal NUMERIC(8,2) NOT NULL,
        precio_venta NUMERIC(8,2) NULL,
        estado CHAR(1) NOT NULL,
        descuento NUMERIC(4,3) NOT NULL)""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def crear_tabla_pedidos(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla pedidos"""
    #Cursor
    cursor = db.cursor()

    #Creacion de tabla pedidos
    cursor.execute("""CREATE TABLE IF NOT EXISTS pedidos(
        codigo CHAR(8) PRIMARY KEY,
        codigo_cliente VARCHAR(50) NOT NULL,
        codigo_colaborador VARCHAR(50),
        estado CHAR(1) NOT NULL,
        fecha_creacion DATETIME DEFAULT (datetime(current_timestamp)),
        fecha_entrega DATETIME,
        direccion_entrega VARCHAR(150) NOT NULL,
        tarifa VARCHAR(150),
        codigo_zona VARCHAR(8) NOT NULL,        
        FOREIGN KEY(codigo_cliente) REFERENCES clientes(email),
        FOREIGN KEY(codigo_colaborador) REFERENCES colaboradores(email));""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def crear_tabla_detalle_pedidos(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla detalle_pedidos"""
    #Cursor
    cursor = db.cursor()

    #Creacion de tabla pedidos
    cursor.execute("""CREATE TABLE IF NOT EXISTS detalle_pedidos(
        codigo_pedido VARCHAR(8),
        codigo_producto VARCHAR(8),
        cantidad INTEGER NOT NULL,
        subtotal NUMERIC(10,2),
        PRIMARY KEY(codigo_pedido, codigo_producto),
        FOREIGN KEY(codigo_pedido) REFERENCES pedidos(codigo),
        FOREIGN KEY(codigo_producto) REFERENCES productos(codigo))""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def crear_tabla_colaboradores(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla colaboradores"""
    #Cursor
    cursor = db.cursor()

    #Creacion de tabla colaboradores
    cursor.execute("""CREATE TABLE IF NOT EXISTS colaboradores(
        email VARCHAR(50) PRIMARY KEY,
        password VARCHAR(12) NOT NULL,
        documento_identidad VARCHAR(8) NOT NULL,
        nombres VARCHAR(50) NOT NULL,
        apellido_paterno VARCHAR(50) NOT NULL,
        apellido_materno VARCHAR(50) NOT NULL,
        genero CHAR(1) NOT NULL,
        fecha_nacimiento DATETIME NOT NULL,
        fecha_creacion DATETIME NOT NULL,
        estado CHAR(1) NOT NULL,
        reputacion NUMERIC(2,1) NOT NULL,
        cobertura VARCHAR(20) NOT NULL)""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def crear_tabla_preferencias(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla preferencias"""
    #Cursor
    cursor = db.cursor()

    #Creacion de tabla preferencias
    cursor.execute("""CREATE TABLE IF NOT EXISTS preferencias(
        codigo VARCHAR(8) PRIMARY KEY,
        nombre VARCHAR(20) NOT NULL)""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def crear_tabla_localizaciones(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla localizaciones"""
    #Cursor
    cursor = db.cursor()

    #Creacion de tabla localizaciones
    cursor.execute("""CREATE TABLE IF NOT EXISTS localizaciones(
        codigo_zona VARCHAR(8) PRIMARY KEY,
        distrito VARCHAR(50) NOT NULL,
        provincia VARCHAR(50) NOT NULL,
        departamento VARCHAR(50) NOT NULL)""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def insertar_datos_clientes(db):
    """Recibe una conexión a una db en sqlite3. Inserta datos a la tabla clientes"""
    #Cursor
    cursor = db.cursor()

    #Insertar datos a la tabla clientes
    cursor.execute("""INSERT INTO clientes(email, password, documento_identidad, nombres, apellido_paterno, apellido_materno,
        genero, fecha_nacimiento, fecha_creacion, estado)
        VALUES ('alicia.gaguilar@gmail.com','demo123','75230816','Alicia','Garcia','Aguilar','F','2018-12-05', '2019-05-13', 'V'),
        ('luis.medina.delgado@hotmail.com','demo123','53707830','Luis','Medina','Delgago','M','2018-11-19', '2019-08-23', 'V'),
        ('carmen.puertas120@gmail.com','demo123',NULL,NULL,NULL,NULL,NULL,NULL,'2018-12-20', 'P')""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()


def insertar_datos_productos(db):
    """Recibe una conexión a una db en sqlite3. Inserta datos a la tabla productos"""
    #Cursor
    cursor = db.cursor()

    #Insertar datos a la tabla productos
    cursor.execute("""INSERT INTO productos (codigo, nombre, descripcion, precio_normal, estado, descuento)
    VALUES ('PROD0001','GoPro Hero 7 4K UHD - Black',
    'Estabilización Superfluido de video:  Consigue estabilización sin tener que usar instrumentos.
    La HERO7 Black prevé tus movimientos y los corrige,  lo que evita vibraciones de la cámara y
    ofrece un contenido increíblemente nítido. Resistente y sumergible: Comparte experiencias que no
    puedes capturar con tu teléfono. La HERO7 Black es resistente y sumergible sin carcasa
    hasta 10 m, y está lista para todo tipo de aventura. Control por voz: Permanece en el momento.
    Controla tu HERO7 Black sin tener que usar las manos mediante
    comandos de voz como "GoPro toma una foto" y "GoPro graba video". Video en 4K y 60 fps, y fotos de 12 MP:
    La HERO7 Black captura videos en 4K y 60 fps increíbles, así como fotos de 12 MP tan fantásticas como los
    propios momentos. Video en cámara lenta de 8 fps: La alta velocidad de fotogramas para videos, de 1080p a
    240 fps, te permite ralentizar hasta 8 fps para crear momentos épicos, interesantes o divertidos en todo
    su esplendor.', 1199.00, 'D', 0.5),
     ('PROD0002', 'Play Station 4 Slim - Negro - 1 TB',
    'Consola más fina y ligera con un estilizado nuevo diseño que encierra una potente PlayStation®4 en su interior.
    30% más delgada y un 16% más ligera que su antecesora. Pero que no te engañe su compacto diseño, su interior
    alberga un disco duro de 1TB de capacidad.Disfruta del HDR también en tu consola favorita.
    Las imágenes son más realistas, impactantes, vívidas. Es como si vieras a través de una ventana,
    lo más parecido a lo que un ojo humano es capaz de ver en el mundo real.
    Lo disfrutarás al máximo no sólo en los juegos sino también en todas las aplicaciones de cine, tele y mucho más
    a las que puedes acceder. Mejoras e innovaciones para el juego como los modos Remote Play y el Share Play.
    El modo Remote Play te permite jugar a tus juegos en otros dispositivos mediante WiFi, como por ejemplo, en tu
    PS Vita.', 1099.00, 'D', 0.1),
     ('PROD0003', 'Xiaomi Redmi Note 6 Pro / 4GB 64GB Versión Global - Negro',
    'Celular Desbloqueado Ranura para SIM: Dual SIM, Dual Standby  Tipo de SIM: Dual Nano SIM, Micro SIM  TIpo: Phablet
    Procesador: Qualcomm Snapdragon 636  Núcleos: 1.8GHz, Octa Core  Memoria expandible: con micro SD hasta 256GB
    GPU: Adreno 509  RAM: 4GB RAM  ROM: 64GB Wireless Connectivity: 3G,4G,A-GPS,Bluetooth,GPS,GSM,LTE,WiFi
    TDD B40 2300MHz Resolución FHD: 2280 x 1080 Tamaño: 6.26 pulgadas Tipo: IPS CAMARA
    Trasera: 12.0MP + 5.0MP  Frontal: 20.0MP + 2.0MP Música: AAC,AMR,FLAC,MP3,MP4  Video: H.263,H.264,H.265,MPEG4
    3G,4G,Alarm,Bluetooth,Browser,Calculator,Calendar,Camera,Fingerprint recognition,GPS,Hall Sensor,Proximity Sensing
    Bluetooth 5.0 Google Play Store: Si I/O Interface: 1 x Nano SIM Card Slot,3.5mm Audio Out Port,Micophone,Micro USB
    Slot,Nano SIM / Micro SD Slot,Speaker  Sensores: Accelerometer,Ambient Light Sensor,E-Compass,Gyroscope,Hall Sensor,
    Infrared Radiation,Proximity', 799.00,'D',0.0),
     ('PROD0004','Disco Duro Externo Toshiba Canvio Basics, 1 Tb, Usb 3.0, 2.5, Negro.',
    'Traemos para ti el Disco Duro Externo, con el cual podrás almacenar y llevar consigo tu información importante
    mientras viajas usando la unidad de disco duro externa USB 3.0 de 1TB. Con una capacidad de 1TB, puede usarse
    para almacenamiento adicional o para realizar copias de seguridad de sus vídeos, fotos, música, documentos y
     otros archivos.',179.00, 'D', 0.0),
     ('PROD0005','Nintendo Switch Neón',
    'Su pantalla multitáctil capacitiva de 6.2 pulgadas (15.75 cm) con una resolución de 1280 x 720 te da toda la
    comodidad que necesitas para jugar mientras viajas, vas al trabajo o la universidad y en cualquier momento del
    día. Además, su batería te brinda aproximadamente hasta 6 horas de autonomía (varía de acuerdo al juego) para
    ue disfrutes de tus juegos favoritos.   Juega cómodamente    Coloca la consola Nintendo Switch en su base y
    juega en alta definición en la comodidad de tu hogar. Además, tus juegos favoritos cobrarán vida gracias a
    los controles por movimiento fáciles de usar y a la sofisticada función de vibración HD incluida en cada
    control Joy?Con. ¡Puedes jugar con tus amigos o en familia!Nuevas formas de jugar Utiliza dos de los innovadores
    controles Joy‑Con para jugar frente a frente o conéctate a internet para una competencia de 4 contra 4.
    Disfrutas de muchas horas del mejor entretenimiento junto a tus amigos. ¡Cuantos más sean, mucho mejor! ',
    1199.00, 'D', 0.2),
    ('PROD0006', 'Roku Premiere 4K HDR Streaming Potente - Negro',
    'Experimenta el mejor streaming gracias al procesador veloz de cuatro núcleos y recepción inalámbrica
    802.11 (compatible con b/g/n). Roku Premiere te permite ver tus programas favoritos rápidamente, con
    navegación receptiva y sin obstáculos y por canales que se inician con rapidez. Roku Premiere brinda una
    magnífica calidad de imagen a tu TV 4K UHD o 1080p HD que te sumerge en la acción con imágenes nítidas y
    tan reales que parece que están a punto de saltar de la pantalla. Experimenta el apremio visual de reproducir
    por streaming 4K Ultra HD con un TV 4K y contenido compatible. El canal Spotlight 4K de Roku ayuda a encontrar
    contenido 4K. Consulta con el socio de canal sobre los requisitos de ancho de banda. Una interfaz intuitiva
    permite que accedas fácilmente a todos tus canales favoritos (pagados o gratuitos) desde la pantalla de tu hogar.
    Por último, Roku Premiere viene con un control remoto fácil de usar.',162.00,'D',0.1),
    ('PROD0007','Drone DJI Tello',
    'La tecnología los últimos años ha experimentado uno de los saltos más evidentes y acelerados respecto a todo
    los acumulados hasta el día de hoy, se encarga de resolver los problemas más modernos y de satisfacer las
    necesidades y deseos de cada consumidor en particular. Asimismo, es capaz de reducir la distancia entre
    las personas, mejorar, automatizar y acelerar procesos, generar entretenimiento y momentos sin igual,
    sin duda, una de las tecnologías que más destacan y llaman la atención de todos en estos últimos años son
    los drones, aparatos voladores que pueden ser controlados en forma remota, además, logran ser usados en
    infinidad de tareas que el humano desee. Disfruta de este drone que te permite grabar videos con una resolución
    de 720p y hacer fotos de hasta 5 Megapixeles, también te permite utilizar las gafas inmersivas de realidad virtual
    Dji Goggles para sentirte igual que si estuvieras dentro del dron convirtiendo la navegación en una experiencia única.',
     369.00, 'D', 0.1),
    ('PROD0008','Samsung Galaxy S10 128GB 8GB Ram - Negro',
    'Smartphone Samsung Galaxy S10
    Samsung está innovando en el mundo de las tecnologías de internet y el marketing digital. Es por eso que en esta
    oportunidad te traemos un teléfono ideal para ti, uno de los más esperados en el mundo, el cual cuenta con múltiples
    funciones que te ayudarán a mantenerte activo en la actualidad al ser un celular con características de gama alta.
    Entre las que destacan: su cámara triple, pantalla de 6.1 pulgadas, lector de huellas, batería de 3400 mAh, entre
    otras características. El sistema operativo de este teléfono es Android 9.0 Pie. Su procesador es Snapdragon 855,
    sumando así una unidad de procesamiento neutral de 8 núcleos, lo que hace que este dispositivo mejore su trabajo de
    inteligencia artificial.Por otra parte, este dispositivo cuenta con soporte para WiFi 6, un nuevo método de conexión
    inalámbrica que mejora la velocidad en dispositivos móviles y es capaz de alcanzar una velocidad máxima de 5 Gbps.',
    3199.00, 'D', 0.0),
    ('PROD0009','Lentes De Sol Ray Ban Aviador RB3025 019/Z2 Pink Espejado - Sanllo Global',
    'Estos productos de alta calidad de la marca RayBan están elaborados por Luxottica con los mejores materiales para
    garantizar su duración, además de una excelente funcionalidad. Sin duda, debes adquirirlo y disfrutar de todos sus
    beneficios y ventajas. Quedarás gratamente sorprendido. Adquiere ahora en Linio al mejor precio y en la puerta de tu casa.
    Lentes de Sol RayBan son de calidad A1 con proteccion UV400  viene nuevo en caja ¿Qué estás esperando? No te quedes atrás y
    adquiere un producto de gran diseño, calidad y garantía, gracias a Linio que trae para ti lo mejor de su amplia línea de productos.
    Adquiere este magnífico producto a través de la plataforma web de Linio, a un precio increíble, si deseas otros modelos, puedes
    revisar nuestro catalogo online y hacer su pedido.', 199.00,'D', 0.0),
    ('PROD0010','Trotadora Eléctrica Monark T-306',
    'Con esta Trotadora Eléctrica podrás disfrutar en la comodidad de tu hogar, de los grandes beneficios que ofrece el ejercicio a tu cuerpo
    y salud.Esta Trotadora Eléctrica Monark T-306 cuenta con una serie de características que hacen de esta el complemento perfecto para tu
    entrenamiento corporal. Posee un computador, que refleja información de pantalla, donde puedes visualizar: velocidad, distancia, tiempo,
     calorías, ritmo cardíaco y programas; elementos de gran relevancia para cualquier persona que realiza ejercicio, puesto que de esta manera
     puedes trazarte metas de entrenamiento, así como también conocer claramente los resultados alcanzados.En cuanto al diseño de la máquina,
     el mismo es ergonómico, ya que está ideado pensando en la comodidad del usuario, como es el caso de la inclinación, la cual es de tipo ajustable,
     dependiendo de los gustos de quien hace uso de la máquina. El peso máximo es de 100 kg. ',2699.00,'D',0.1);""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def insertar_datos_pedidos(db):
    """Recibe una conexión a una db en sqlite3. Inserta datos a la tabla pedidos"""
    #Cursor
    cursor = db.cursor()

    #Insertar datos a la tabla clientes
    cursor.execute("""INSERT INTO pedidos(codigo, codigo_cliente, estado, direccion_entrega, codigo_zona)
        VALUES ('Pedido0001', 'alicia.gaguilar@gmail.com','N','Av. Salaverry 2020, Jesus María', '15088')""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def insertar_datos_detalle_pedidos(db):
    """Recibe una conexión a una db en sqlite3. Inserta datos a la tabla detalle pedidos"""
    #Cursor
    cursor = db.cursor()

    #Insertar datos a la tabla detalle pedidos
    cursor.execute("""INSERT INTO detalle_pedidos(codigo_pedido, codigo_producto, cantidad)
        VALUES ('Pedido0001', 'PROD0005', 1), ('Pedido0001', 'PROD0002', 2)""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def insertar_datos_colaboradores(db):
    """Recibe una conexión a una db en sqlite3. Inserta datos a la tabla colaboradores"""
    #Cursor
    cursor = db.cursor()

    #Insertar datos a la tabla colaboradores
    cursor.execute("""INSERT INTO colaboradores(email, password, documento_identidad, nombres, apellido_paterno, apellido_materno,
        genero, fecha_nacimiento, fecha_creacion, estado, reputacion, cobertura)
        VALUES ('alicia.gaguilar@gmail.com','demo123','75230816','Oscar','Rivas','Delgado','M','1999-05-04', '2019-05-13', 'V', 5, 'Lima')""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

def insertar_datos_localizaciones(db):
    """Recibe una conexión a una db en sqlite3. Inserta datos a la tabla localizaciones"""
    #Cursor
    cursor = db.cursor()

    #Insertar datos a la tabla localizaciones
    cursor.execute("""INSERT INTO localizaciones(codigo_zona, distrito, provincia, departamento)
        VALUES ('1', 'Lima', 'Lima', 'Lima'), ('2', 'Ancón', 'Lima', 'Lima'), ('3', 'Ate', 'Lima', 'Lima'),
        ('4', 'Barranco', 'Lima', 'Lima'), ('5', 'Breña', 'Lima', 'Lima'), ('6', 'Carabayllo', 'Lima', 'Lima'),
        ('7', 'Chaclacayo', 'Lima', 'Lima'), ('8', 'Chorrillos', 'Lima', 'Lima'), ('9', 'Cienieguilla', 'Lima', 'Lima'),
        ('10', 'Comas', 'Lima', 'Lima'), ('11', 'El Agustino', 'Lima', 'Lima'), ('12', 'Independencia', 'Lima', 'Lima'),
        ('13', 'Jesus María', 'Lima', 'Lima'), ('14', 'La Molina', 'Lima', 'Lima'), ('15', 'La Victoria', 'Lima', 'Lima'),
        ('16', 'Lince', 'Lima', 'Lima'), ('17', 'Los Olivos', 'Lima', 'Lima'), ('18', 'Lurigancho', 'Lima', 'Lima'),
        ('19', 'Lurín', 'Lima', 'Lima'), ('20', 'Magdalena del Mar', 'Lima', 'Lima'), ('21', 'Miraflores', 'Lima', 'Lima'),
        ('22', 'Pachacámac', 'Lima', 'Lima'), ('23', 'Pucusana', 'Lima', 'Lima'), ('24', 'Pueblo Libre', 'Lima', 'Lima'),
        ('25', 'Puente Piedra', 'Lima', 'Lima'), ('26', 'Punta Hermosa', 'Lima', 'Lima'), ('27', 'Punta Negra', 'Lima', 'Lima'),
        ('28', 'Rímac', 'Lima', 'Lima'), ('29', 'San Bartolo', 'Lima', 'Lima'), ('30', 'San Borja', 'Lima', 'Lima'),
        ('31', 'San Isidro', 'Lima', 'Lima'), ('32', 'San Juan de Lurigancho', 'Lima', 'Lima'), ('33', 'San Juan de Miraflores', 'Lima', 'Lima'),
        ('34', 'San Luis', 'Lima', 'Lima'), ('35', 'San Martín de Porres', 'Lima', 'Lima'), ('36', 'San Miguel', 'Lima', 'Lima'),
        ('37', 'Santa Anita', 'Lima', 'Lima'), ('38', 'Santa María del Mar', 'Lima', 'Lima'), ('39', 'Santa Rosa', 'Lima', 'Lima'),
        ('40', 'Santiago de Surco', 'Lima', 'Lima'), ('41', 'Surquillo', 'Lima', 'Lima'), ('42', 'Villa El Salvador', 'Lima', 'Lima'),
        ('43', 'Villa María del Triunfo', 'Lima', 'Lima');""")

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()



#Apertura de db
db = sqlite3.connect("linioexp_parcial_lab3.db")
borrar_tablas(db)
crear_tabla_cliente(db)
crear_tabla_productos(db)
crear_tabla_colaboradores(db)
crear_tabla_detalle_pedidos(db)
crear_tabla_localizaciones(db)
crear_tabla_preferencias(db)
crear_tabla_pedidos(db)
insertar_datos_clientes(db)
insertar_datos_productos(db)
insertar_datos_colaboradores(db)
insertar_datos_pedidos(db)
insertar_datos_detalle_pedidos(db)
insertar_datos_localizaciones(db)
