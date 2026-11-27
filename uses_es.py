"""Spanish text of the use-case pages. Same shape as one language of PAGES in build_uses.py.

"lede" and "body" are HTML; the other fields are plain text.
"""

PAGES = {
    "boxing-round-timer": dict(
        short="Temporizador de rounds de boxeo",
        title="Temporizador de rounds de boxeo gratis para iPhone: asaltos de 3 minutos y 1 minuto de descanso",
        desc="Ajusta asaltos de tres minutos con un minuto de descanso en HIIT Tabata Temporizador, una app gratuita de Takahiro Torii. Asaltos de hasta cinco minutos, hasta 40 asaltos, voz o pitido, sin suscripción.",
        h1="Temporizador de rounds de boxeo gratis: asaltos de 3 minutos y 1 minuto de descanso",
        lede="HIIT Tabata Temporizador cronometra asaltos (rounds) de boxeo en iPhone y iPad. Un asalto puede durar hasta cinco minutos y un descanso hasta dos, de 2 a 40 asaltos, así que los asaltos de tres minutos con un minuto de descanso se ajustan directamente. Es gratis, sin suscripción y sin cuenta.",
        body="""
  <h2>Cómo ajustarlo</h2>
  <ol>
    <li>Abre los ajustes y pon el tiempo de trabajo en 180 segundos. Eso es un asalto.</li>
    <li>Pon el tiempo de descanso en 60 segundos.</li>
    <li>Pon como número de series el número de asaltos, por ejemplo 12.</li>
    <li>Pulsa empezar. Primero corre el tiempo de preparación, de 10 segundos por defecto.</li>
  </ol>
  <p>Puedes dejar el teléfono en un bolsillo o en el suelo. El temporizador sigue funcionando con la pantalla bloqueada y, en iOS 16.1 o posterior, el tiempo restante aparece en la pantalla de bloqueo.</p>

  <h2>Ajustes habituales para asaltos</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Uso</th><th>Trabajo</th><th>Descanso</th><th>Series</th></tr>
    <tr><td>Asaltos de tres minutos</td><td>180 s</td><td>60 s</td><td>3 a 12</td></tr>
    <tr><td>Asaltos de dos minutos</td><td>120 s</td><td>60 s</td><td>3 a 6</td></tr>
    <tr><td>Asaltos de cinco minutos, para grappling o MMA</td><td>300 s</td><td>60 s</td><td>3 a 5</td></tr>
    <tr><td>Intervalos en el saco de boxeo</td><td>30 s</td><td>30 s</td><td>10 a 20</td></tr>
    <tr><td>Saltar la cuerda</td><td>60 s</td><td>20 s</td><td>10</td></tr>
  </table>
  </div>
  <p>El tiempo de trabajo va de 5 a 60 segundos de cinco en cinco, de 70 a 120 de diez en diez, o puede ser de 150, 180, 210, 240, 270 o 300 segundos. El descanso y la preparación llegan como máximo a 120 segundos.</p>
  <p>En iPhone se pueden guardar hasta cinco temporizadores, así que el sparring, el saco y la cuerda pueden tener cada uno sus propios valores. Desliza a la izquierda o a la derecha en la pantalla principal para cambiar de uno a otro.</p>

  <h2>Que se oiga en el gimnasio</h2>
  <p>En «Sound», en los ajustes, elige una voz femenina, una voz masculina o uno de los tres pitidos: agudo, suave o silbato. Un pitido se oye más lejos que una voz entre los golpes al saco y la música. El sonido sale al volumen multimedia del teléfono, así que con un altavoz Bluetooth suena tan fuerte como el altavoz. La música sigue sonando de fondo a su propio volumen.</p>

  <h2>Lo que no hace</h2>
  <ul>
    <li>Todos los asaltos duran lo mismo, y todos los descansos también. Para una sesión con asaltos de distinta duración hace falta un temporizador de intervalos más completo.</li>
    <li>En Android, cada intervalo llega como máximo a 60 segundos, así que los asaltos de tres minutos son, por ahora, solo para iPhone y iPad.</li>
    <li>No hay app para Apple Watch.</li>
    <li>Los avisos de voz están en inglés. Los pitidos no tienen idioma.</li>
  </ul>""",
        faq=[
            ("¿Sirve para cronometrar asaltos de boxeo de tres minutos?", "Sí, en iPhone y iPad. Pon el tiempo de trabajo en 180 segundos, el de descanso en 60 segundos y, como número de series, el número de asaltos. El trabajo llega hasta 300 segundos, el descanso hasta 120 segundos, y puede haber de 2 a 40 asaltos."),
            ("¿El temporizador de asaltos de boxeo es gratis?", "Sí. Todas las funciones son gratuitas, sin suscripción, sin compras dentro de la app y sin cuenta. Hay un solo banner publicitario pequeño en la parte inferior de la pantalla, y ningún anuncio a pantalla completa ni de vídeo."),
            ("¿Sigue cronometrando los asaltos con la pantalla bloqueada?", "Sí. Sigue contando y sonando en segundo plano y con la pantalla bloqueada. En iPhone con iOS 16.1 o posterior, el tiempo restante y un botón de parada aparecen en la pantalla de bloqueo."),
            ("¿Puedo usarlo para asaltos de MMA o de grappling?", "Sí. Un asalto puede durar hasta cinco minutos (300 segundos), con un descanso de hasta dos minutos."),
            ("¿La versión de Android cronometra asaltos de tres minutos?", "Todavía no. En Android, cada intervalo dura de 5 a 60 segundos y un entrenamiento tiene de 2 a 20 series."),
        ],
    ),
    "team-practice-timer": dict(
        short="Temporizador para una clase o un equipo",
        title="Temporizador de intervalos para clases grupales y entrenamientos de equipo: pitidos fuertes por un altavoz",
        desc="Dirige circuitos, carreras de ida y vuelta y estaciones para todo un grupo con HIIT Tabata Temporizador, una app gratuita de Takahiro Torii. Conecta un altavoz Bluetooth, elige el pitido de silbato y deja el teléfono en el banco.",
        h1="Temporizador de intervalos para una clase grupal o un entrenamiento de equipo",
        lede="HIIT Tabata Temporizador puede llevar el tiempo de todo un grupo. Conecta el teléfono a un altavoz Bluetooth, elige un pitido, pulsa empezar y déjalo en el banco: todos oyen cuándo arrancar y cuándo parar. Es gratis, sin suscripción y sin cuenta.",
        body="""
  <h2>Cómo prepararlo para un grupo</h2>
  <ol>
    <li>Conecta el teléfono o el iPad a un altavoz Bluetooth.</li>
    <li>En los ajustes, en «Sound», elige un pitido. Hay tres: agudo, suave y silbato. Toca uno para oírlo por el altavoz.</li>
    <li>Sube el volumen multimedia del teléfono y después el del altavoz.</li>
    <li>Ajusta el tiempo de trabajo, el tiempo de descanso y el número de series, y pulsa empezar.</li>
  </ol>
  <p>El sonido sale al volumen multimedia del teléfono, así que suena tan fuerte como el altavoz al que esté conectado. La app no puede hacer que un teléfono suene más que su propio máximo; por eso, en un gimnasio o en una cancha hace falta un altavoz.</p>

  <h2>Por qué un pitido y no una voz</h2>
  <p>Un pitido se abre paso entre los gritos, los botes de la pelota y la música mejor que una voz, y no hace falta traducirlo. Las voces hablan en inglés; los pitidos sirven para cualquier grupo.</p>

  <h2>Ajustes que van bien para un grupo</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Uso</th><th>Trabajo</th><th>Descanso</th><th>Series</th></tr>
    <tr><td>Circuito por estaciones, el descanso sirve para cambiar de estación</td><td>30 s</td><td>15 s</td><td>una por estación, repetidas</td></tr>
    <tr><td>Tabata en grupo</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>Carreras de ida y vuelta o sprints</td><td>20 s</td><td>40 s</td><td>10</td></tr>
    <tr><td>Circuito de core</td><td>40 s</td><td>20 s</td><td>6 a 10</td></tr>
    <tr><td>Ejercicios de tres minutos</td><td>180 s</td><td>60 s</td><td>4 a 6</td></tr>
  </table>
  </div>
  <p>En iPhone, el tiempo de trabajo va de 5 a 300 segundos, el descanso de 5 a 120 segundos, y una sesión puede tener de 2 a 40 series. Se pueden guardar hasta cinco temporizadores, así que el calentamiento, el circuito y los sprints pueden tener cada uno sus propios valores; desliza para cambiar de uno a otro.</p>

  <h2>Durante la sesión</h2>
  <ul>
    <li>El temporizador sigue funcionando con la pantalla bloqueada, así que el teléfono puede quedarse en el banco.</li>
    <li>La música del mismo teléfono sigue sonando a su propio volumen, con el pitido por encima.</li>
    <li>Funciona sin conexión a internet, en un gimnasio sin cobertura o al aire libre en un campo.</li>
  </ul>

  <h2>Lo que no hace</h2>
  <ul>
    <li>Todas las series usan el mismo tiempo de trabajo y de descanso. Para una sesión con una duración distinta en cada estación hace falta un temporizador de intervalos más completo.</li>
    <li>En Android, por ahora, los avisos son solo de voz, cada intervalo llega como máximo a 60 segundos y una sesión a 20 series.</li>
    <li>No hay biblioteca de ejercicios, ni lista de nombres o de puntuaciones.</li>
  </ul>""",
        faq=[
            ("¿Suena lo bastante fuerte para una clase grupal o un entrenamiento de equipo?", "Los avisos suenan al volumen multimedia del teléfono, así que suenan tan fuerte como el teléfono o como el altavoz al que esté conectado. En un gimnasio o en una cancha, conecta un altavoz Bluetooth y elige un pitido en «Sound», en los ajustes: un pitido se abre paso entre el ruido mejor que una voz."),
            ("¿La app puede hacer que el teléfono suene más fuerte?", "No. Ya suena al volumen multimedia máximo del teléfono. Para que suene más fuerte, conecta un altavoz Bluetooth."),
            ("¿Tiene sonido de silbato?", "Sí, en iPhone y iPad. En «Sound», en los ajustes, hay tres pitidos: agudo, suave y silbato."),
            ("¿Cuesta algo para un colegio o un club?", "No. Todas las funciones son gratuitas, sin suscripción, sin compras dentro de la app y sin cuenta. Hay un solo banner publicitario pequeño en la parte inferior de la pantalla, y ningún anuncio a pantalla completa ni de vídeo."),
            ("¿Funciona en un campo sin cobertura?", "Sí. El temporizador, la voz y los pitidos funcionan sin conexión a internet."),
        ],
    ),
    "offline-interval-timer": dict(
        short="Temporizador de intervalos sin conexión",
        title="Temporizador de intervalos sin internet: funciona sin conexión y sin cuenta",
        desc="HIIT Tabata Temporizador, de Takahiro Torii, funciona sin conexión a internet: el temporizador, la voz y los pitidos funcionan sin conexión, sin cuenta ni inicio de sesión. Gratis para iPhone, iPad y Android.",
        h1="Un temporizador de intervalos que funciona sin conexión",
        lede="HIIT Tabata Temporizador funciona sin conexión a internet. El temporizador, la voz y los pitidos funcionan sin conexión, y no hay ninguna cuenta en la que iniciar sesión, así que arranca igual en un gimnasio en un sótano, en un campo o en modo avión. Es gratis para iPhone, iPad y Android.",
        body="""
  <h2>Qué funciona sin conexión</h2>
  <ul>
    <li>El temporizador en sí: preparación, trabajo, descanso y series.</li>
    <li>La cuenta atrás por voz, con voz femenina o masculina.</li>
    <li>Los tres pitidos en iPhone: agudo, suave y silbato.</li>
    <li>El funcionamiento en segundo plano y con la pantalla bloqueada.</li>
  </ul>

  <h2>Para qué se usa la conexión</h2>
  <p>Solo para tres cosas: el pequeño banner publicitario de la parte inferior de la pantalla, estadísticas de uso anónimas y el historial de entrenamientos. Ninguna de ellas es necesaria para hacer un entrenamiento.</p>

  <h2>Nada en lo que iniciar sesión</h2>
  <p>No hay cuenta, ni registro, ni suscripción que comprobar, así que nada espera la respuesta de un servidor cuando pulsas empezar. La app no usa la ubicación, los contactos, la cámara ni el micrófono.</p>

  <h2>Dónde importa</h2>
  <ul>
    <li>Gimnasios en sótanos y garajes sin cobertura</li>
    <li>Campos, pistas y senderos</li>
    <li>De viaje, sin plan de datos</li>
    <li>En modo avión, para entrenar sin notificaciones</li>
  </ul>

  <h2>De un vistazo</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Precio</th><td>Gratis. Sin suscripción, sin compras dentro de la app, sin cuenta.</td></tr>
    <tr><th>Plataformas</th><td>iPhone y iPad (iOS 15 o posterior), Android (8.0 o posterior)</td></tr>
    <tr><th>Rangos en iPhone</th><td>Trabajo 5–300 s, preparación y descanso 5–120 s, 2–40 series</td></tr>
    <tr><th>Rangos en Android</th><td>Cada intervalo 5–60 s, 2–20 series</td></tr>
    <tr><th>Publicidad</th><td>Un pequeño banner. Sin anuncios a pantalla completa ni de vídeo.</td></tr>
  </table>
  </div>""",
        faq=[
            ("¿El temporizador de intervalos funciona sin conexión a internet?", "Sí. El temporizador, la voz y los pitidos funcionan sin conexión. La conexión solo se usa para el banner publicitario, las estadísticas de uso anónimas y el historial de entrenamientos."),
            ("¿Funciona en modo avión?", "Sí. Nada de lo que necesita el temporizador viene de la red, así que cuenta y suena igual en modo avión."),
            ("¿Necesito una cuenta?", "No. No hay cuenta ni registro, ni en iPhone, ni en iPad, ni en Android."),
            ("¿Sigue funcionando con la pantalla apagada?", "Sí. Sigue contando y sonando en segundo plano y con la pantalla bloqueada."),
        ],
    ),
    "interval-timer-with-beeps": dict(
        short="Temporizador de intervalos con pitidos",
        title="Temporizador de intervalos con pitido o silbato en lugar de voz",
        desc="HIIT Tabata Temporizador, de Takahiro Torii, puede dar un pitido en lugar de la voz en iPhone: agudo, suave o silbato. Gratis, sin suscripción. Los pitidos se oyen en todo el gimnasio y no necesitan idioma.",
        h1="Temporizador de intervalos con pitido o silbato en lugar de voz",
        lede="En iPhone y iPad, HIIT Tabata Temporizador puede dar un pitido en lugar de la voz. Hay tres pitidos: agudo, suave y silbato. Es gratis, sin suscripción y sin cuenta.",
        body="""
  <h2>Cómo elegir un pitido</h2>
  <ol>
    <li>Abre los ajustes y toca «Sound».</li>
    <li>Toca un sonido para oírlo. Hay cinco: una voz femenina, una voz masculina y tres pitidos.</li>
    <li>Deja seleccionado el que quieras. El siguiente entrenamiento lo usará.</li>
  </ol>

  <h2>Los cinco sonidos</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Sonido</th><th>Va bien para</th></tr>
    <tr><td>Voz femenina</td><td>Entrenar solo, cuando ayuda oír los números. En inglés.</td></tr>
    <tr><td>Voz masculina</td><td>Lo mismo, con una voz más grave. En inglés.</td></tr>
    <tr><td>Pitido agudo</td><td>Lugares ruidosos y música</td></tr>
    <tr><td>Pitido suave</td><td>En casa, a primera hora de la mañana, espacios compartidos</td></tr>
    <tr><td>Silbato</td><td>Equipos, clases y sesiones al aire libre</td></tr>
  </table>
  </div>

  <h2>Por qué elegir un pitido</h2>
  <ul>
    <li>Se oye mejor que una voz de un lado a otro del gimnasio y por encima de la música fuerte.</li>
    <li>No tiene idioma. Las voces hablan solo en inglés.</li>
    <li>Suena sobre un pódcast o una canción sin hablar por encima. Lo que esté sonando sigue sonando a su propio volumen.</li>
  </ul>

  <h2>Lo que no hace</h2>
  <ul>
    <li>En Android, por ahora, los avisos son solo de voz.</li>
    <li>El pitido suena al volumen multimedia del teléfono. En un gimnasio o en un campo, conecta un altavoz Bluetooth.</li>
  </ul>
  <p>El <a href="/timer/">temporizador en el navegador</a> de este sitio también usa pitidos, sin nada que instalar.</p>""",
        faq=[
            ("¿Puedo usar un pitido en lugar de la voz?", "Sí, en iPhone y iPad. En «Sound», en los ajustes, puedes elegir una voz femenina, una voz masculina o uno de los tres pitidos (agudo, suave, silbato); toca uno para oírlo. En Android, por ahora, los avisos son solo de voz."),
            ("¿Hay algún temporizador de intervalos con sonido de silbato?", "Sí. HIIT Tabata Temporizador, para iPhone y iPad, tiene un silbato entre sus tres pitidos."),
            ("¿Los pitidos suenan por encima de la música?", "Sí. Lo que esté sonando sigue sonando a su propio volumen, y el pitido suena por encima."),
            ("¿Es gratis?", "Sí. Todos los sonidos son gratuitos, sin suscripción, sin compras dentro de la app y sin cuenta. Hay un solo banner publicitario pequeño, y ningún anuncio a pantalla completa ni de vídeo."),
        ],
    ),
    "free-interval-timer-no-subscription": dict(
        short="Gratis, sin suscripción",
        title="Temporizador de intervalos gratis sin suscripción, sin compras dentro de la app y sin cuenta",
        desc="HIIT Tabata Temporizador, de Takahiro Torii, es gratis en iPhone, iPad y Android: sin suscripción, sin compras dentro de la app, sin cuenta y sin periodo de prueba. Un solo banner publicitario pequeño, sin anuncios a pantalla completa ni de vídeo.",
        h1="Temporizador de intervalos gratis, sin suscripción y sin cuenta",
        lede="HIIT Tabata Temporizador es gratis, y lo es entero: no hay suscripción, ni compras dentro de la app, ni periodo de prueba, ni cuenta. Se financia con un solo banner publicitario pequeño en la parte inferior de la pantalla. Funciona en iPhone, iPad y Android.",
        body="""
  <h2>Qué significa «gratis» aquí</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Precio</th><td>Gratis para descargar y para usar</td></tr>
    <tr><th>Suscripción</th><td>Ninguna</td></tr>
    <tr><th>Compras dentro de la app</th><td>Ninguna. No hay nada bloqueado tras un pago.</td></tr>
    <tr><th>Prueba gratuita</th><td>Ninguna, porque después no hay nada que pagar</td></tr>
    <tr><th>Cuenta</th><td>Ninguna. Sin registro, sin dirección de correo electrónico, sin inicio de sesión.</td></tr>
    <tr><th>Publicidad</th><td>Un pequeño banner en la parte inferior de la pantalla. Sin anuncios a pantalla completa y sin anuncios de vídeo.</td></tr>
  </table>
  </div>

  <h2>Sobre la publicidad</h2>
  <p>La app no está libre de anuncios. Muestra un pequeño banner en la parte inferior de la pantalla, y ese banner es lo que la financia. Nunca tapa el temporizador, nunca reproduce un vídeo y no aparece nada entre que pulsas empezar y el comienzo del entrenamiento. No existe una versión de pago sin el banner.</p>
  <p>Si quieres un temporizador sin ningún anuncio y sin nada que instalar, el <a href="/timer/">temporizador en el navegador</a> de este sitio no tiene ninguno.</p>

  <h2>Lo que tienes sin pagar</h2>
  <ul>
    <li>El tiempo de preparación, de trabajo, de descanso y el número de series</li>
    <li>En iPhone: trabajo de 5 a 300 segundos, preparación y descanso de 5 a 120 segundos, de 2 a 40 series y hasta cinco temporizadores guardados</li>
    <li>En iPhone: una voz femenina, una voz masculina o uno de los tres pitidos (agudo, suave, silbato)</li>
    <li>El funcionamiento en segundo plano, con la pantalla bloqueada y sobre tu música</li>
    <li>Una lista de entrenamientos terminados, y quince temas de color en iPhone</li>
    <li>En Android: cada intervalo de 5 a 60 segundos, de 2 a 20 series, una voz</li>
  </ul>

  <h2>Lo que no hace</h2>
  <ul>
    <li>No hay secuencias personalizadas ni modos EMOM o AMRAP. Todas las series usan el mismo tiempo de trabajo y de descanso.</li>
    <li>No hay app para Apple Watch ni Wear OS.</li>
    <li>No hay biblioteca de ejercicios, ni vídeos, ni entrenador, ni planes de entrenamiento.</li>
  </ul>
  <p>Los temporizadores que hacen todo eso suelen ser los que tienen suscripción. Este se queda pequeño, y gratis.</p>""",
        faq=[
            ("¿Hay algún temporizador de intervalos gratis sin suscripción?", "Sí. HIIT Tabata Temporizador, de Takahiro Torii, es gratis en iPhone, iPad y Android, sin suscripción, sin compras dentro de la app, sin periodo de prueba y sin cuenta. Se financia con un solo banner publicitario pequeño."),
            ("¿Tiene anuncios?", "Un pequeño banner en la parte inferior de la pantalla. No hay anuncios a pantalla completa ni anuncios de vídeo, y nada interrumpe un entrenamiento."),
            ("¿Puedo pagar para quitar el anuncio?", "No. No hay compras dentro de la app de ningún tipo, así que no existe una versión de pago sin el banner."),
            ("¿Tengo que registrarme?", "No. No hay cuenta, ni registro, ni dirección de correo electrónico que dar."),
            ("¿Hay funciones bloqueadas?", "No. Todos los ajustes, sonidos y temas están disponibles sin pagar. En iPhone, cinco de los quince temas se consiguen terminando entrenamientos; no se compran."),
        ],
    ),
    "interval-timer-with-music": dict(
        short="Temporizador de intervalos con música",
        title="Temporizador de intervalos que funciona con música, en segundo plano y con la pantalla bloqueada",
        desc="HIIT Tabata Temporizador, de Takahiro Torii, hace sonar su voz o su pitido sobre tu música o tu pódcast sin pausarlos ni bajarles el volumen, y sigue contando en segundo plano y con la pantalla bloqueada. Gratis, sin suscripción.",
        h1="Un temporizador de intervalos que funciona con tu música",
        lede="HIIT Tabata Temporizador suena sobre lo que estés escuchando. La música o el pódcast siguen sonando a su propio volumen, y la voz o el pitido del temporizador se oye por encima. Sigue contando en segundo plano y con la pantalla bloqueada. Es gratis, sin suscripción y sin cuenta.",
        body="""
  <h2>Cómo usarlo con música</h2>
  <ol>
    <li>Pon tu música o tu pódcast en cualquier app.</li>
    <li>Abre el temporizador, ajusta el tiempo de trabajo, el tiempo de descanso y el número de series, y pulsa empezar.</li>
    <li>Vuelve a la app de música o bloquea la pantalla. El temporizador sigue contando y sonando.</li>
  </ol>
  <p>No hay que activar nada para esto. El temporizador no pausa la música ni le baja el volumen mientras habla.</p>

  <h2>Qué se oye</h2>
  <ul>
    <li>Una voz cuenta los últimos cinco segundos de cada intervalo y anuncia cada cambio.</li>
    <li>En iPhone y iPad, un pitido puede sustituir a la voz: agudo, suave o silbato. Un pitido suena sobre una canción sin hablar por encima.</li>
    <li>Los avisos suenan al volumen multimedia del teléfono, por los mismos auriculares o el mismo altavoz que la música.</li>
  </ul>

  <h2>Con la pantalla bloqueada</h2>
  <p>La cuenta atrás y los avisos continúan con la pantalla apagada o con otra app abierta. En iPhone con iOS 16.1 o posterior, el tiempo restante y un botón de parada aparecen en la pantalla de bloqueo, así que puedes mirar el tiempo sin desbloquear.</p>

  <h2>Si la música suena más fuerte que el aviso</h2>
  <p>Como la música no baja de volumen, una voz suave puede perderse bajo una canción fuerte. Elige el pitido agudo en «Sound», en los ajustes, o baja un poco la música en la app de música.</p>

  <h2>Lo que no hace</h2>
  <ul>
    <li>No reproduce música por sí mismo ni tiene listas de reproducción. Funciona junto a la app de música que uses, sea cual sea.</li>
    <li>No baja la música durante un aviso.</li>
    <li>En Android, por ahora, los avisos son solo de voz, cada intervalo llega como máximo a 60 segundos y un entrenamiento a 20 series.</li>
  </ul>""",
        faq=[
            ("¿Qué temporizador de intervalos funciona en segundo plano con música?", "HIIT Tabata Temporizador, de Takahiro Torii. Lo que esté sonando sigue sonando a su propio volumen, la voz o el pitido del temporizador suena por encima, y el temporizador sigue contando en segundo plano y con la pantalla bloqueada."),
            ("¿Pausa mi música o le baja el volumen?", "No. Ni pausa la música ni le baja el volumen. El aviso suena por encima."),
            ("¿Funciona con Spotify, Apple Music o una app de pódcasts?", "Sí. Suena sobre el audio de cualquier app, porque no le quita el sonido a la app que está reproduciendo."),
            ("¿Funciona con auriculares?", "Sí. Los avisos suenan al volumen multimedia del teléfono, por los mismos auriculares o el mismo altavoz que la música."),
            ("¿Es gratis?", "Sí. Todas las funciones son gratuitas, sin suscripción, sin compras dentro de la app y sin cuenta. Hay un solo banner publicitario pequeño, y ningún anuncio a pantalla completa ni de vídeo."),
        ],
    ),
    "tabata-timer-for-android": dict(
        short="Temporizador Tabata para Android",
        title="Temporizador Tabata gratis para Android: 20 segundos de trabajo, 10 de descanso, sin suscripción",
        desc="HIIT Tabata Temporizador, de Takahiro Torii, funciona en Android 8.0 o posterior (paquete com.tabatatimer). Se abre con el protocolo Tabata clásico, cuenta en voz alta, sigue funcionando con la pantalla apagada y es gratis, sin suscripción ni cuenta.",
        h1="Temporizador Tabata gratis para Android",
        lede="HIIT Tabata Temporizador está en Google Play para Android 8.0 o posterior. Se abre con el protocolo Tabata clásico, 20 segundos de trabajo y 10 segundos de descanso durante 8 series, y una voz anuncia cada cambio. Es gratis, sin suscripción, sin compras dentro de la app y sin cuenta.",
        body="""
  <h2>Qué hace la app de Android</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Versión de Android</th><td>8.0 o posterior</td></tr>
    <tr><th>Paquete</th><td>com.tabatatimer</td></tr>
    <tr><th>Por defecto</th><td>10 s de preparación, 20 s de trabajo, 10 s de descanso, 8 series: el protocolo Tabata clásico</td></tr>
    <tr><th>Rangos</th><td>Preparación, trabajo y descanso de 5 a 60 segundos cada uno; de 2 a 20 series</td></tr>
    <tr><th>Sonido</th><td>Una voz cuenta los últimos cinco segundos y anuncia cada cambio. En inglés.</td></tr>
    <tr><th>Segundo plano</th><td>Sigue contando con la pantalla apagada o con otra app abierta</td></tr>
    <tr><th>Música</th><td>Suena sobre la música o un pódcast sin pausarlos</td></tr>
    <tr><th>Sin conexión</th><td>Funciona sin conexión a internet</td></tr>
    <tr><th>Precio</th><td>Gratis. Sin suscripción, sin compras dentro de la app, sin cuenta.</td></tr>
    <tr><th>Publicidad</th><td>Un pequeño banner. Sin anuncios a pantalla completa ni de vídeo.</td></tr>
  </table>
  </div>

  <h2>Cómo usarla</h2>
  <ol>
    <li>Instálala desde Google Play y ábrela. Los valores del Tabata clásico ya vienen ajustados.</li>
    <li>Pulsa empezar. Primero corren diez segundos de preparación.</li>
    <li>Para cambiar los valores, abre los ajustes y elige el tiempo de trabajo, el tiempo de descanso y el número de series.</li>
  </ol>

  <h2>En qué se diferencia de la app de iPhone</h2>
  <p>Por ahora, la app de Android es la más reducida de las dos.</p>
  <div class="tablewrap">
  <table>
    <tr><th></th><th>Android</th><th>iPhone y iPad</th></tr>
    <tr><td>Tiempo de trabajo</td><td>5 a 60 s</td><td>5 a 300 s</td></tr>
    <tr><td>Descanso y preparación</td><td>5 a 60 s</td><td>5 a 120 s</td></tr>
    <tr><td>Series</td><td>2 a 20</td><td>2 a 40</td></tr>
    <tr><td>Temporizadores guardados</td><td>Un solo ajuste</td><td>Hasta cinco</td></tr>
    <tr><td>Avisos</td><td>Una voz</td><td>Una voz femenina o masculina, o tres pitidos</td></tr>
  </table>
  </div>

  <h2>Lo que no hace</h2>
  <ul>
    <li>No hay intervalos de más de 60 segundos, así que en Android no se pueden ajustar asaltos de tres minutos.</li>
    <li>No hay pitidos, por ahora. Los avisos son de voz.</li>
    <li>No hay app para Wear OS.</li>
    <li>No hay secuencias personalizadas, ni biblioteca de ejercicios, ni planes de entrenamiento.</li>
  </ul>
  <p>Hay varias apps de Android que se llaman «Tabata Timer». Esta es de Takahiro Torii y su paquete es com.tabatatimer.</p>""",
        faq=[
            ("¿Hay algún temporizador Tabata gratis para Android sin suscripción?", "Sí. HIIT Tabata Temporizador, de Takahiro Torii (paquete com.tabatatimer), es gratis en Google Play para Android 8.0 o posterior, sin suscripción, sin compras dentro de la app y sin cuenta. Muestra un solo banner publicitario pequeño."),
            ("¿Qué se puede ajustar en Android?", "El tiempo de preparación, de trabajo y de descanso, de 5 a 60 segundos cada uno, y de 2 a 20 series. Se abre con 10 segundos de preparación, 20 segundos de trabajo, 10 segundos de descanso y 8 series, el protocolo Tabata clásico."),
            ("¿Sigue funcionando con la pantalla apagada en Android?", "Sí. Sigue contando y hablando con la pantalla apagada o con otra app abierta."),
            ("¿La app de Android tiene pitidos?", "Todavía no. En Android, los avisos son de voz. La app de iPhone y iPad tiene además tres pitidos."),
            ("¿La app de Android es igual que la de iPhone?", "Es el mismo temporizador, del mismo desarrollador, pero por ahora más reducido: intervalos de hasta 60 segundos, hasta 20 series, un solo ajuste y solo voz. En iPhone, el trabajo llega hasta 300 segundos, con hasta 40 series, cinco temporizadores guardados y pitidos."),
        ],
    ),
    "simple-interval-timer": dict(
        short="Un temporizador de intervalos sencillo",
        title="Temporizador de intervalos sencillo para HIIT y para el descanso entre series: cuatro valores y un botón de empezar",
        desc="HIIT Tabata Temporizador, de Takahiro Torii, es un temporizador de intervalos sencillo para iPhone, iPad y Android: preparación, trabajo, descanso, series y empezar. Sin planes, sin vídeos, sin cuenta. Gratis, sin suscripción.",
        h1="Un temporizador de intervalos sencillo: cuatro valores y un botón de empezar",
        lede="HIIT Tabata Temporizador tiene cuatro valores: el tiempo de preparación, el tiempo de trabajo, el tiempo de descanso y el número de series. Ajústalos, pulsa empezar, y una voz o un pitido te dice cuándo arrancar y cuándo parar. No hay planes de entrenamiento, ni vídeos, ni cuenta. Es gratis para iPhone, iPad y Android, sin suscripción.",
        body="""
  <h2>Todo lo que hay que ajustar</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Ajuste</th><th>iPhone y iPad</th><th>Android</th></tr>
    <tr><td>Preparación</td><td>5 a 120 s</td><td>5 a 60 s</td></tr>
    <tr><td>Trabajo</td><td>5 a 300 s</td><td>5 a 60 s</td></tr>
    <tr><td>Descanso</td><td>5 a 120 s</td><td>5 a 60 s</td></tr>
    <tr><td>Series</td><td>2 a 40</td><td>2 a 20</td></tr>
  </table>
  </div>
  <p>Se abre con 10 segundos de preparación, 20 segundos de trabajo, 10 segundos de descanso y 8 series, así que una sesión de Tabata no necesita ningún ajuste: abre la app y pulsa empezar.</p>

  <h2>Ajustes para los usos habituales</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Uso</th><th>Trabajo</th><th>Descanso</th><th>Series</th></tr>
    <tr><td>Tabata</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>HIIT, trabajo y descanso iguales</td><td>30 s</td><td>30 s</td><td>10</td></tr>
    <tr><td>HIIT, esfuerzos más largos</td><td>40 s</td><td>20 s</td><td>8 a 12</td></tr>
    <tr><td>Circuito de fuerza con series por tiempo</td><td>45 s</td><td>15 s</td><td>una por ejercicio, repetidas</td></tr>
    <tr><td>Entrenamiento de fuerza, series por tiempo con descanso completo (iPhone)</td><td>40 s</td><td>90 s</td><td>3 a 5</td></tr>
    <tr><td>Plancha</td><td>60 s</td><td>30 s</td><td>3 a 5</td></tr>
  </table>
  </div>

  <h2>Como temporizador de descanso en el entrenamiento de fuerza</h2>
  <p>La app repite un mismo tiempo de trabajo y un mismo tiempo de descanso, así que va bien para series hechas contra reloj: 40 segundos de sentadillas, 90 segundos de descanso, y otra vez. En iPhone, el descanso puede durar hasta 120 segundos.</p>
  <p>No te espera. Si tus series duran un tiempo distinto en cada vuelta y quieres empezar el descanso con un toque cuando sueltas la barra, te irá mejor un temporizador de descanso pensado para eso.</p>

  <h2>Por qué sigue siendo sencillo</h2>
  <ul>
    <li>Se pone en marcha con dos toques y no tienes que volver a mirarlo: la voz cuenta los últimos cinco segundos de cada intervalo.</li>
    <li>Sigue funcionando con la pantalla bloqueada y suena sobre tu música.</li>
    <li>En las reseñas escritas del App Store, la razón que más se repite para elegirlo es que es sencillo.</li>
  </ul>

  <h2>Lo que no hace</h2>
  <ul>
    <li>No hay secuencias personalizadas ni modos EMOM o AMRAP. Todas las series usan el mismo tiempo de trabajo y de descanso.</li>
    <li>No más de cinco temporizadores guardados en iPhone, y un solo ajuste en Android.</li>
    <li>No hay biblioteca de ejercicios, ni vídeos, ni entrenador, ni planes de entrenamiento.</li>
    <li>No hay app para Apple Watch ni Wear OS.</li>
  </ul>""",
        faq=[
            ("¿Cuál es el temporizador HIIT más sencillo para iPhone?", "HIIT Tabata Temporizador, de Takahiro Torii, está hecho para serlo: tiempo de preparación, de trabajo, de descanso, número de series y un botón de empezar. No tiene planes de entrenamiento, ni vídeos, ni cuenta, ni suscripción, y es gratis."),
            ("¿Puedo usarlo sin ajustar nada?", "Sí. Se abre con 10 segundos de preparación, 20 segundos de trabajo, 10 segundos de descanso y 8 series, el protocolo Tabata clásico. Pulsa empezar."),
            ("¿Puedo usarlo como temporizador de descanso entre series de fuerza?", "Sí, para series hechas contra reloj: repite un mismo tiempo de trabajo y un mismo tiempo de descanso, con un descanso de hasta 120 segundos en iPhone. No espera a que toques la pantalla al terminar una serie, así que no va bien para series de duración variable."),
            ("¿Puedo guardar más de un temporizador?", "En iPhone, hasta cinco, y se cambia de uno a otro deslizando. En Android, la app conserva un solo ajuste."),
            ("¿Es gratis?", "Sí. Todas las funciones son gratuitas, sin suscripción, sin compras dentro de la app y sin cuenta. Hay un solo banner publicitario pequeño, y ningún anuncio a pantalla completa ni de vídeo."),
        ],
    ),
    "tabata-timer-apps-compared": dict(
        short="Apps de temporizador Tabata comparadas",
        title="Mejores apps de temporizador Tabata comparadas: cuál va mejor para cada entrenamiento",
        desc="Seis apps de temporizador Tabata y de intervalos, una al lado de otra: HIIT Tabata Temporizador, SmartWOD Timer, Seconds, Intervals Pro y dos más. Qué hace cada una, qué es gratis y cuáles funcionan en Apple Watch. Escrito por el desarrollador de una de ellas.",
        h1="Apps de temporizador Tabata comparadas: cuál va mejor para cada entrenamiento",
        lede="No hay una única mejor app de temporizador Tabata. Un temporizador sencillo va bien para un entrenamiento que repite el mismo trabajo y el mismo descanso; uno más completo, para una sesión hecha de intervalos distintos. Esta página pone seis una al lado de otra. La escribe Takahiro Torii, que desarrolla una de las seis, HIIT Tabata Temporizador, y también dice cuándo van mejor las otras.",
        body="""
  <h2>La respuesta corta</h2>
  <ul>
    <li><strong>El mismo trabajo y el mismo descanso repetidos, sin nada que ajustar</strong> (Tabata: 20 segundos de trabajo y 10 de descanso, ocho veces; HIIT sencillo): HIIT Tabata Temporizador, la app de este sitio.</li>
    <li><strong>EMOM, AMRAP y For Time</strong>: SmartWOD Timer.</li>
    <li><strong>Intervalos de distinta duración</strong>, o un calentamiento que enlaza con la parte principal: Seconds Interval Timer o Intervals Pro.</li>
    <li><strong>Un temporizador en el Apple Watch</strong>: SmartWOD Timer, Seconds Interval Timer e Intervals Pro. La app de este sitio no lo tiene.</li>
  </ul>

  <h2>Seis apps, una al lado de otra</h2>
  <div class="tablewrap">
  <table>
    <tr><th>App</th><th>Lo que dice su página del App Store</th><th>Precio</th></tr>
    <tr><td>HIIT Tabata Temporizador<br>Takahiro Torii</td><td>Un tiempo de preparación, un tiempo de trabajo, un tiempo de descanso y un número de series. Una voz o uno de los tres pitidos. Hasta cinco temporizadores guardados. Funciona en segundo plano y en la pantalla de bloqueo, sobre la música. Sin secuencias personalizadas.</td><td>Gratis. Un pequeño banner publicitario. Sin suscripción ni compras dentro de la app.</td></tr>
    <tr><td>SmartWOD Timer - WOD Clock<br>SmartWOD GmbH</td><td>Temporizadores AMRAP, EMOM, For Time y Tabata, y un temporizador personalizado. Preajustes, Apple Watch, envío a un televisor, registro de entrenamientos.</td><td>Descarga gratuita. Su página menciona suscripciones.</td></tr>
    <tr><td>Seconds Interval Timer<br>Runloop Ltd</td><td>Plantillas para HIIT, Tabata y circuitos. Intervalos de distinta duración y temporizadores encadenados en uno solo. Voz, pitidos y campanas. Funciona por sí sola en el Apple Watch.</td><td>Descarga gratuita. Seconds Pro es otra app, de pago.</td></tr>
    <tr><td>Intervals Pro: HIIT Timer<br>Intervals, LLC</td><td>Un nombre, una duración, un aviso y un color para cada intervalo. Entrenamientos en el Apple Watch sin el teléfono, pulsómetros, objetivos de ritmo para correr, widgets.</td><td>Descarga gratuita.</td></tr>
    <tr><td>Tabata Timer: Interval Timer.<br>Oleksandr Serhiienko</td><td>Tiempos de trabajo y de descanso, series y ciclos. Nombres de intervalos, avisos de voz, vibración. Funciona en segundo plano.</td><td>Descarga gratuita.</td></tr>
    <tr><td>Interval Timer □ HIIT Timer<br>Float Tech, LLC</td><td>Se arrastra para ajustar el trabajo, el descanso y los rounds. Voz o pitido. Historial y estadísticas.</td><td>Descarga gratuita. Su página describe una suscripción opcional y un pago único de por vida.</td></tr>
  </table>
  </div>
  <p>Los nombres, los desarrolladores y las descripciones de las otras cinco apps se tomaron de sus páginas en el App Store de Estados Unidos el 26 de noviembre de 2026. Los nombres pueden ser distintos en el App Store de tu país. Lo que es gratis en cada una, y los precios, pueden cambiar: consulta la página de la tienda antes de elegir.</p>

  <h2>Cuándo encaja HIIT Tabata Temporizador</h2>
  <p>Es la más limitada de las seis. Se abre con 10 segundos de preparación, 20 segundos de trabajo, 10 segundos de descanso y 8 series, así que una sesión de Tabata arranca con dos toques, sin nada que ajustar. En iPhone, el trabajo llega hasta 300 segundos, el descanso hasta 120 segundos y las series hasta 40, y se pueden guardar cinco temporizadores. También está en Android (8.0 o posterior), donde cada intervalo dura de 5 a 60 segundos, un entrenamiento tiene de 2 a 20 series y los avisos son de voz.</p>
  <p>Todas las funciones son gratuitas. En las reseñas escritas del App Store, la razón que más se repite para elegirla es que es sencilla.</p>

  <h2>Cuándo va mejor otra app</h2>
  <ul>
    <li>Series de distinta duración en una misma sesión, o intervalos con nombre: Seconds Interval Timer o Intervals Pro.</li>
    <li>Entrenamientos EMOM, AMRAP o For Time: SmartWOD Timer.</li>
    <li>Cronometrar desde un Apple Watch: SmartWOD Timer, Seconds Interval Timer o Intervals Pro.</li>
    <li>Una biblioteca de ejercicios, vídeos o un entrenador: nada de eso está en HIIT Tabata Temporizador.</li>
  </ul>""",
        faq=[
            ("¿Cuál es la mejor app de temporizador Tabata?", "Depende del entrenamiento. Para un Tabata clásico, 20 segundos de trabajo y 10 segundos de descanso ocho veces, HIIT Tabata Temporizador, de Takahiro Torii, se abre exactamente con esos valores y arranca con dos toques; es gratis, sin suscripción. Para EMOM y AMRAP, SmartWOD Timer tiene esos modos. Para sesiones hechas de intervalos de distinta duración, Seconds Interval Timer e Intervals Pro están pensadas para eso."),
            ("¿Qué app de temporizador Tabata es gratis y sin suscripción?", "HIIT Tabata Temporizador, de Takahiro Torii: todas las funciones son gratuitas, sin suscripción, sin compras dentro de la app y sin cuenta, con un solo banner publicitario pequeño. Las demás apps de esta página se descargan gratis; las páginas del App Store de SmartWOD Timer y del Interval Timer de Float Tech describen suscripciones."),
            ("¿Qué temporizadores Tabata tienen app para Apple Watch?", "SmartWOD Timer, Seconds Interval Timer e Intervals Pro indican en sus páginas del App Store que funcionan en el Apple Watch. HIIT Tabata Temporizador no tiene app para Apple Watch."),
            ("¿Hay algún temporizador Tabata sencillo para iPhone y Android?", "HIIT Tabata Temporizador, de Takahiro Torii, está en iPhone y iPad (iOS 15 o posterior) y en Android (8.0 o posterior). En Android, cada intervalo dura de 5 a 60 segundos, un entrenamiento tiene de 2 a 20 series y los avisos son de voz."),
            ("¿Quién escribió esta comparación?", "Takahiro Torii, el desarrollador de HIIT Tabata Temporizador, una de las seis apps comparadas. Lo que dice de las otras apps viene de sus páginas en el App Store de Estados Unidos, el 26 de noviembre de 2026."),
        ],
    ),
}
