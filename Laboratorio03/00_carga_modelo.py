# INSERTAR DATOS A LA TABLA CLIENTE
cursor.execute("""
INSERT INTO clientes(email, password, documento_identidad, nombres, apellido_paterno, apellido_materno, 
genero, fecha_nacimiento, fecha_creacion, estado)
VALUES ('alicia.gaguilar@gmail.com','demo123','75230816','Alicia','Garcia','Aguilar','F','2018-12-05', '2019-05-13', 'V'),
('luis.medina.delgado@hotmail.com','demo123','53707830','Luis','Medina','Delgago','M','2018-11-19', '2019-08-23', 'V'),
('carmen.puertas120@gmail.com','demo123',NULL,NULL,NULL,NULL,NULL,NULL,'2018-12-20', 'P')
""")

# INSERTAR DATOS A LA TABLA PRODUCTOS
cursor.execute("""
INSERT INTO productos (codigo, nombre, descripcion, precio_normal, estado, descuento)
VALUES 
('PROD0001','GoPro Hero 7 4K UHD - Black',
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

con.commit()    # CONFIRMAR CAMBIOS

cursor.close()  # CERRAR CONECCION AL SQLITE3
