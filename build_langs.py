#!/usr/bin/env python3
"""Generate the fr/de/it/es/nl pages of simpletabata.com from one template.

Run from the site repo root:  python3 build_langs.py <site-dir>
The English and Japanese pages are hand-written; this only patches their
language links and hreflang block.
"""
import html
import json
import re
import sys
from pathlib import Path

SITE = Path(sys.argv[1])
BASE = "https://simpletabata.com"
ALL = [("en", "English", "/"), ("ja", "日本語", "/ja/"), ("fr", "Français", "/fr/"),
       ("de", "Deutsch", "/de/"), ("it", "Italiano", "/it/"), ("es", "Español", "/es/"),
       ("nl", "Nederlands", "/nl/")]

L = {}

L["fr"] = dict(
    name="Minuteur Sport HIIT & Tabata",
    title="Minuteur Sport HIIT & Tabata — un minuteur d'intervalles gratuit et simple pour iPhone et Android",
    metadesc="Minuteur Sport HIIT & Tabata, par Takahiro Torii : un minuteur d'intervalles gratuit pour iPhone et Android. Réglez l'effort, le repos et les séries, puis lancez. Décompte vocal, fonctionne en arrière-plan, par-dessus votre musique. Sans compte ni abonnement.",
    ogdesc="Un minuteur d'intervalles gratuit et simple pour iPhone et Android. Décompte vocal, arrière-plan, sans compte ni abonnement.",
    alt="Icône de l'app Minuteur Sport HIIT & Tabata",
    by="par Takahiro Torii · iPhone, iPad et Android · gratuit",
    lede="Un minuteur d'intervalles tout simple. Réglez le temps d'effort, le temps de repos et le nombre de séries, puis appuyez sur démarrer. Une voix compte les cinq dernières secondes et annonce chaque changement : vous n'avez jamais besoin de regarder l'écran pendant l'entraînement.",
    p2="Il ne fait qu'une chose. Pas de programmes d'entraînement, pas de vidéos, pas de compte, pas d'abonnement. Il est sur l'App Store depuis 2016 ; ailleurs, il s'appelle « Tabata & HIIT Interval Timer », et au Japon",
    appstore="Télécharger dans l'App Store", play="Disponible sur Google Play",
    h_glance="En bref",
    rows=[
        ("Prix", "Gratuit. Sans abonnement, sans achats intégrés, sans compte."),
        ("Publicité", "Une petite bannière en bas de l'écran. Aucune publicité plein écran ni vidéo."),
        ("Plateformes", "iPhone et iPad (iOS 13 ou version ultérieure), Android (8.0 ou version ultérieure)"),
        ("Note", "{r} sur 5 pour {n} notes sur l'App Store en France ; 4,8 pour 10 896 notes au Japon (15 novembre 2026)"),
        ("Réglages", "Préparation, effort, repos, nombre de séries"),
        ("Par défaut", "10 s de préparation, 20 s d'effort, 10 s de repos, 8 séries — le protocole Tabata classique"),
        ("Voix", "Décompte et annonces vocales, en anglais"),
        ("Arrière-plan", "Continue de compter écran éteint ou dans une autre app"),
        ("Musique", "Se superpose à votre musique ou à votre podcast sans les mettre en pause ni baisser le volume"),
        ("Apple Santé", "Facultatif. Enregistre les séances terminées une fois activé ; ne lit rien."),
        ("Développeur", "Takahiro Torii, développeur indépendant au Japon"),
        ("Première sortie", "Octobre 2016"),
    ],
    h_uses="À quoi il sert",
    uses=["Séances Tabata et HIIT, fractionné",
          "Musculation et circuits, comme minuteur de repos entre les séries",
          "Burpees, gainage, mountain climbers, sprints",
          "Étirements, mobilité, renforcement du tronc",
          "Rounds de boxe, corde à sauter, vélo d'appartement"],
    uses_p="Dans les avis écrits sur l'App Store, la raison la plus souvent donnée pour l'avoir choisi est sa simplicité. Environ un tiers des avis le disent, souvent après avoir essayé un minuteur plus chargé en fonctions.",
    h_not="Ce qu'il ne fait pas",
    not_p="Autant le dire clairement, car c'est ce qui détermine si l'app vous convient.",
    nots=["Pas de préréglages enregistrés. L'app garde un seul réglage à la fois.",
          "Pas de séquences personnalisées, ni de modes EMOM ou AMRAP. Chaque série utilise les mêmes temps d'effort et de repos.",
          "Pas d'app Apple Watch ni Wear OS.",
          "Pas de bibliothèque d'exercices, de coaching ni de programmes.",
          "L'interface et la voix sont en anglais uniquement."],
    not_p2="Si vous voulez un minuteur qui se lance en deux touches et se fait oublier, c'est celui-ci. Si vous voulez programmer des séances complexes, cherchez un minuteur d'intervalles plus complet.",
    h_q="Questions",
    faq=[
        ("Est-ce vraiment gratuit ?", "Oui. Toutes les fonctions sont gratuites, sans abonnement, achat intégré ni compte. L'app est financée par une petite bannière publicitaire en bas de l'écran. Il n'y a aucune publicité plein écran ni vidéo."),
        ("Continue-t-il quand l'écran est éteint ?", "Oui. Le décompte et la voix continuent en arrière-plan et écran verrouillé. Sur iPhone (iOS 16.1 ou version ultérieure), le temps restant et un bouton d'arrêt s'affichent sur l'écran verrouillé ; sur Android, le temps restant apparaît dans une notification."),
        ("Puis-je écouter de la musique en même temps ?", "Oui. Ce qui est en cours de lecture continue à son propre volume, et la voix s'y superpose."),
        ("Que peut-on régler ?", "Le temps de préparation, d'effort, de repos et le nombre de séries. Sur iPhone, chaque intervalle peut durer jusqu'à 120 secondes et une séance compter jusqu'à 40 séries. Sur Android, chaque intervalle dure de 5 à 60 secondes et une séance compte de 2 à 20 séries."),
        ("Qu'est-ce que la méthode Tabata ?", "Après un échauffement, on alterne 20 secondes d'effort maximal et 10 secondes de repos, huit fois — quatre minutes au total. Le protocole porte le nom du professeur Izumi Tabata, de l'université Ritsumeikan, dont les travaux ont été publiés en 1996. L'app démarre exactement sur ces valeurs."),
        ("Quelles données l'app collecte-t-elle ?", "Il n'y a pas d'inscription. L'app enregistre l'heure de fin de chaque séance sous un identifiant anonyme et utilise Firebase Analytics, Crashlytics et Google AdMob. Elle n'utilise ni la localisation, ni les contacts, ni l'appareil photo, ni le micro."),
    ],
    privacy_link="Voir la <a href=\"/privacy.html\">politique de confidentialité</a> (en anglais et en japonais).",
    h_get="Obtenir l'app",
    note="Plusieurs apps portent un nom proche. Celle-ci est publiée par Takahiro Torii ; son identifiant App Store est 1166542235 et son paquet Android <code>com.tabatatimer</code>.",
    privacy="Politique de confidentialité", contact="Contact", updated="Dernière mise à jour : 15 novembre 2026",
    rating=("4,8", "61"), store="fr",
)

L["de"] = dict(
    name="Intervall-Timer HIIT & Tabata",
    title="Intervall-Timer HIIT & Tabata — ein kostenloser, einfacher Intervall-Timer für iPhone und Android",
    metadesc="Intervall-Timer HIIT & Tabata von Takahiro Torii: ein kostenloser Intervall-Timer für iPhone und Android. Belastung, Pause und Sätze einstellen, Start drücken. Sprach-Countdown, läuft im Hintergrund und über Ihrer Musik. Ohne Konto, ohne Abo.",
    ogdesc="Ein kostenloser, einfacher Intervall-Timer für iPhone und Android. Sprach-Countdown, läuft im Hintergrund, ohne Konto und ohne Abo.",
    alt="App-Symbol von Intervall-Timer HIIT & Tabata",
    by="von Takahiro Torii · iPhone, iPad und Android · kostenlos",
    lede="Ein einfacher Intervall-Timer. Belastungszeit, Pausenzeit und Anzahl der Sätze einstellen, Start drücken. Eine Stimme zählt die letzten fünf Sekunden herunter und sagt jeden Wechsel an – Sie müssen beim Training nie auf den Bildschirm schauen.",
    p2="Er kann genau eine Sache. Keine Trainingspläne, keine Videos, kein Konto, kein Abo. Im App Store gibt es ihn seit 2016; anderswo heißt er „Tabata & HIIT Interval Timer“, in Japan",
    appstore="Laden im App Store", play="Jetzt bei Google Play",
    h_glance="Auf einen Blick",
    rows=[
        ("Preis", "Kostenlos. Kein Abo, keine In-App-Käufe, kein Konto."),
        ("Werbung", "Ein kleines Banner am unteren Bildschirmrand. Keine Vollbild- oder Videowerbung."),
        ("Plattformen", "iPhone und iPad (iOS 13 oder neuer), Android (8.0 oder neuer)"),
        ("Bewertung", "{r} von 5 bei {n} Bewertungen im deutschen App Store; 4,8 bei 10.896 Bewertungen in Japan (15. November 2026)"),
        ("Einstellungen", "Vorbereitung, Belastung, Pause, Anzahl der Sätze"),
        ("Standard", "10 s Vorbereitung, 20 s Belastung, 10 s Pause, 8 Sätze – das klassische Tabata-Protokoll"),
        ("Stimme", "Gesprochener Countdown und Ansagen, auf Englisch"),
        ("Hintergrund", "Zählt weiter, wenn der Bildschirm aus ist oder eine andere App geöffnet ist"),
        ("Musik", "Läuft über Ihrer Musik oder Ihrem Podcast, ohne sie anzuhalten oder leiser zu stellen"),
        ("Apple Health", "Optional. Schreibt beendete Workouts, wenn eingeschaltet; liest nichts."),
        ("Entwickler", "Takahiro Torii, unabhängiger Entwickler in Japan"),
        ("Erstveröffentlichung", "Oktober 2016"),
    ],
    h_uses="Wofür er genutzt wird",
    uses=["Tabata- und HIIT-Einheiten",
          "Krafttraining und Zirkeltraining, als Pausentimer zwischen den Sätzen",
          "Burpees, Planks, Mountain Climbers, Sprints",
          "Dehnen, Mobility und Rumpftraining",
          "Boxrunden, Seilspringen, Heimtrainer und Spinning"],
    uses_p="In den geschriebenen App-Store-Rezensionen wird als Grund für die Wahl am häufigsten genannt, dass er einfach ist. Etwa ein Drittel schreibt das, meist nachdem ein Timer mit mehr Funktionen ausprobiert wurde.",
    h_not="Was er nicht kann",
    not_p="Das sei offen gesagt, denn davon hängt ab, ob die App zu Ihnen passt.",
    nots=["Keine gespeicherten Voreinstellungen. Die App merkt sich immer nur eine Einstellung.",
          "Keine eigenen Abfolgen, kein EMOM oder AMRAP. Jeder Satz hat dieselbe Belastungs- und Pausenzeit.",
          "Keine App für Apple Watch oder Wear OS.",
          "Keine Übungsbibliothek, kein Coaching, keine Trainingspläne.",
          "Oberfläche und Stimme gibt es nur auf Englisch."],
    not_p2="Wenn Sie einen Timer wollen, der mit zwei Tipps läuft und über den Sie nicht mehr nachdenken müssen, ist es dieser. Wenn Sie komplexe Workouts programmieren möchten, suchen Sie nach einem umfangreicheren Intervall-Timer.",
    h_q="Fragen",
    faq=[
        ("Ist er wirklich kostenlos?", "Ja. Alle Funktionen sind kostenlos, ohne Abo, In-App-Kauf oder Konto. Finanziert wird die App durch ein kleines Werbebanner am unteren Bildschirmrand. Es gibt keine Vollbild- oder Videowerbung."),
        ("Läuft er weiter, wenn der Bildschirm aus ist?", "Ja. Countdown und Stimme laufen im Hintergrund und bei gesperrtem Bildschirm weiter. Auf dem iPhone (iOS 16.1 oder neuer) erscheinen die Restzeit und eine Stopp-Taste auf dem Sperrbildschirm; unter Android steht die Restzeit in einer Mitteilung."),
        ("Kann ich gleichzeitig Musik hören?", "Ja. Was gerade läuft, läuft in seiner eigenen Lautstärke weiter, und die Stimme wird darübergelegt."),
        ("Was lässt sich einstellen?", "Vorbereitungszeit, Belastungszeit, Pausenzeit und die Anzahl der Sätze. Auf dem iPhone kann jedes Intervall bis zu 120 Sekunden dauern und ein Workout bis zu 40 Sätze haben. Unter Android dauert jedes Intervall 5 bis 60 Sekunden, ein Workout hat 2 bis 20 Sätze."),
        ("Was ist Tabata-Training?", "Nach dem Aufwärmen wechseln sich 20 Sekunden maximale Belastung und 10 Sekunden Pause ab, achtmal – insgesamt vier Minuten. Das Protokoll ist nach Professor Izumi Tabata von der Ritsumeikan-Universität benannt, dessen Studie dazu 1996 erschien. Die App startet mit genau diesen Werten."),
        ("Welche Daten erfasst die App?", "Es gibt keine Anmeldung. Die App speichert den Zeitpunkt, zu dem ein Workout beendet wurde, unter einer anonymen Kennung und verwendet Firebase Analytics, Crashlytics und Google AdMob. Standort, Kontakte, Kamera und Mikrofon werden nicht verwendet."),
    ],
    privacy_link="Siehe die <a href=\"/privacy.html\">Datenschutzerklärung</a> (auf Englisch und Japanisch).",
    h_get="App laden",
    note="Mehrere Apps heißen ähnlich. Diese hier stammt von Takahiro Torii; die App-Store-ID lautet 1166542235, das Android-Paket <code>com.tabatatimer</code>.",
    privacy="Datenschutzerklärung", contact="Kontakt", updated="Zuletzt aktualisiert: 15. November 2026",
    rating=("4,7", "103"), store="de",
)

L["it"] = dict(
    name="Timer HIIT Tabata Allenamento",
    title="Timer HIIT Tabata Allenamento — un timer a intervalli gratuito e semplice per iPhone e Android",
    metadesc="Timer HIIT Tabata Allenamento di Takahiro Torii: un timer a intervalli gratuito per iPhone e Android. Imposta lavoro, recupero e serie, poi premi start. Conto alla rovescia vocale, funziona in background e sopra la tua musica. Senza account né abbonamento.",
    ogdesc="Un timer a intervalli gratuito e semplice per iPhone e Android. Conto alla rovescia vocale, funziona in background, senza account né abbonamento.",
    alt="Icona dell'app Timer HIIT Tabata Allenamento",
    by="di Takahiro Torii · iPhone, iPad e Android · gratis",
    lede="Un timer a intervalli semplice. Imposta il tempo di lavoro, il tempo di recupero e il numero di serie, poi premi start. Una voce conta gli ultimi cinque secondi e annuncia ogni cambio, così non devi mai guardare lo schermo mentre ti alleni.",
    p2="Fa una cosa sola. Niente programmi di allenamento, niente video, niente account, niente abbonamento. È sull'App Store dal 2016; altrove si chiama «Tabata & HIIT Interval Timer», in Giappone",
    appstore="Scarica su App Store", play="Disponibile su Google Play",
    h_glance="In breve",
    rows=[
        ("Prezzo", "Gratis. Nessun abbonamento, nessun acquisto in-app, nessun account."),
        ("Pubblicità", "Un piccolo banner in fondo allo schermo. Nessuna pubblicità a schermo intero né video."),
        ("Piattaforme", "iPhone e iPad (iOS 13 o versioni successive), Android (8.0 o versioni successive)"),
        ("Valutazione", "{r} su 5 con {n} valutazioni sull'App Store in Italia; 4,8 con 10.896 valutazioni in Giappone (15 novembre 2026)"),
        ("Impostazioni", "Preparazione, lavoro, recupero, numero di serie"),
        ("Predefinito", "10 s di preparazione, 20 s di lavoro, 10 s di recupero, 8 serie — il protocollo Tabata classico"),
        ("Voce", "Conto alla rovescia e annunci vocali, in inglese"),
        ("Background", "Continua a contare con lo schermo spento o con un'altra app aperta"),
        ("Musica", "Si sovrappone alla tua musica o al tuo podcast senza metterli in pausa né abbassarne il volume"),
        ("Apple Salute", "Facoltativo. Scrive gli allenamenti completati quando è attivo; non legge nulla."),
        ("Sviluppatore", "Takahiro Torii, sviluppatore indipendente in Giappone"),
        ("Prima pubblicazione", "Ottobre 2016"),
    ],
    h_uses="Per cosa viene usato",
    uses=["Sessioni Tabata e HIIT",
          "Allenamento con i pesi e circuiti, come timer di recupero tra le serie",
          "Burpees, plank, mountain climbers, scatti",
          "Stretching, mobilità e core",
          "Round di boxe, salto con la corda, cyclette e spinning"],
    uses_p="Nelle recensioni scritte sull'App Store, il motivo citato più spesso per averlo scelto è che è semplice. Lo dice circa un terzo delle recensioni, di solito dopo aver provato un timer con più funzioni.",
    h_not="Cosa non fa",
    not_p="Meglio dirlo chiaramente, perché è questo che decide se l'app fa per te.",
    nots=["Nessun preset salvato. L'app conserva una sola impostazione alla volta.",
          "Nessuna sequenza personalizzata, né modalità EMOM o AMRAP. Ogni serie usa gli stessi tempi di lavoro e di recupero.",
          "Nessuna app per Apple Watch o Wear OS.",
          "Nessuna libreria di esercizi, coaching o programmi di allenamento.",
          "L'interfaccia e la voce sono solo in inglese."],
    not_p2="Se vuoi un timer che parte con due tocchi e a cui non devi più pensare, è questo. Se vuoi programmare allenamenti complessi, cerca un timer a intervalli più completo.",
    h_q="Domande",
    faq=[
        ("È davvero gratis?", "Sì. Tutte le funzioni sono gratuite, senza abbonamento, acquisti in-app o account. L'app si finanzia con un piccolo banner pubblicitario in fondo allo schermo. Non ci sono pubblicità a schermo intero né video."),
        ("Continua a funzionare con lo schermo spento?", "Sì. Il conto alla rovescia e la voce continuano in background e con lo schermo bloccato. Su iPhone (iOS 16.1 o versioni successive) il tempo rimanente e un pulsante di stop compaiono nella schermata di blocco; su Android il tempo rimanente compare in una notifica."),
        ("Posso ascoltare musica nel frattempo?", "Sì. Quello che è in riproduzione continua al proprio volume, e la voce vi si sovrappone."),
        ("Cosa si può modificare?", "Il tempo di preparazione, di lavoro, di recupero e il numero di serie. Su iPhone ogni intervallo può durare fino a 120 secondi e un allenamento può avere fino a 40 serie. Su Android ogni intervallo dura da 5 a 60 secondi e un allenamento ha da 2 a 20 serie."),
        ("Che cos'è l'allenamento Tabata?", "Dopo il riscaldamento si alternano 20 secondi di sforzo massimo e 10 secondi di recupero, per otto volte: quattro minuti in tutto. Il protocollo prende il nome dal professor Izumi Tabata dell'Università Ritsumeikan, la cui ricerca è stata pubblicata nel 1996. L'app parte esattamente con questi valori."),
        ("Quali dati raccoglie l'app?", "Non c'è registrazione. L'app salva l'orario di completamento di ogni allenamento sotto un identificatore anonimo e usa Firebase Analytics, Crashlytics e Google AdMob. Non usa posizione, contatti, fotocamera né microfono."),
    ],
    privacy_link="Vedi l'<a href=\"/privacy.html\">informativa sulla privacy</a> (in inglese e giapponese).",
    h_get="Scarica l'app",
    note="Diverse app hanno un nome simile. Questa è pubblicata da Takahiro Torii; l'ID App Store è 1166542235 e il pacchetto Android è <code>com.tabatatimer</code>.",
    privacy="Informativa sulla privacy", contact="Contatto", updated="Ultimo aggiornamento: 15 novembre 2026",
    rating=("4,7", "19"), store="it",
)

L["es"] = dict(
    name="HIIT Tabata Temporizador",
    title="HIIT Tabata Temporizador — un temporizador de intervalos gratuito y sencillo para iPhone y Android",
    metadesc="HIIT Tabata Temporizador, de Takahiro Torii: un temporizador de intervalos gratuito para iPhone y Android. Ajusta el trabajo, el descanso y las series, y pulsa empezar. Cuenta atrás por voz, funciona en segundo plano y sobre tu música. Sin cuenta ni suscripción.",
    ogdesc="Un temporizador de intervalos gratuito y sencillo para iPhone y Android. Cuenta atrás por voz, funciona en segundo plano, sin cuenta ni suscripción.",
    alt="Icono de la app HIIT Tabata Temporizador",
    by="de Takahiro Torii · iPhone, iPad y Android · gratis",
    lede="Un temporizador de intervalos sencillo. Ajusta el tiempo de trabajo, el tiempo de descanso y el número de series, y pulsa empezar. Una voz cuenta los últimos cinco segundos y anuncia cada cambio, así que nunca tienes que mirar la pantalla mientras entrenas.",
    p2="Hace una sola cosa. No hay planes de entrenamiento, ni vídeos, ni cuenta, ni suscripción. Está en el App Store desde 2016; en otros países se llama «Tabata & HIIT Interval Timer», y en Japón",
    appstore="Descargar en el App Store", play="Disponible en Google Play",
    h_glance="De un vistazo",
    rows=[
        ("Precio", "Gratis. Sin suscripción, sin compras dentro de la app, sin cuenta."),
        ("Publicidad", "Un pequeño banner en la parte inferior de la pantalla. Sin anuncios a pantalla completa ni de vídeo."),
        ("Plataformas", "iPhone y iPad (iOS 13 o posterior), Android (8.0 o posterior)"),
        ("Valoración", "{r} de 5 con {n} valoraciones en el App Store de España; 4,8 con 10.896 valoraciones en Japón (15 de noviembre de 2026)"),
        ("Ajustes", "Preparación, trabajo, descanso, número de series"),
        ("Por defecto", "10 s de preparación, 20 s de trabajo, 10 s de descanso, 8 series: el protocolo Tabata clásico"),
        ("Voz", "Cuenta atrás y avisos por voz, en inglés"),
        ("Segundo plano", "Sigue contando con la pantalla apagada o con otra app abierta"),
        ("Música", "Suena sobre tu música o tu pódcast sin pausarlos ni bajarles el volumen"),
        ("Apple Salud", "Opcional. Registra los entrenamientos terminados cuando se activa; no lee nada."),
        ("Desarrollador", "Takahiro Torii, desarrollador independiente en Japón"),
        ("Primera publicación", "Octubre de 2016"),
    ],
    h_uses="Para qué se usa",
    uses=["Sesiones de Tabata y HIIT",
          "Entrenamiento de fuerza y circuitos con pesas, como temporizador de descanso entre series",
          "Burpees, planchas, mountain climbers, sprints",
          "Estiramientos, movilidad y trabajo de core",
          "Asaltos de boxeo, comba, bicicleta estática y spinning"],
    uses_p="En las reseñas escritas del App Store, la razón que más se repite para elegirlo es que es sencillo. Lo dice aproximadamente un tercio de ellas, normalmente después de haber probado un temporizador con más funciones.",
    h_not="Lo que no hace",
    not_p="Conviene decirlo claramente, porque de ello depende que la app sea la adecuada para ti.",
    nots=["No guarda ajustes predefinidos. La app conserva un solo ajuste a la vez.",
          "No hay secuencias personalizadas ni modos EMOM o AMRAP. Todas las series usan el mismo tiempo de trabajo y de descanso.",
          "No hay app para Apple Watch ni Wear OS.",
          "No hay biblioteca de ejercicios, entrenador ni planes de entrenamiento.",
          "La interfaz y la voz están solo en inglés."],
    not_p2="Si quieres un temporizador que arranca con dos toques y del que te puedes olvidar, es este. Si quieres programar entrenamientos complejos, busca un temporizador de intervalos más completo.",
    h_q="Preguntas",
    faq=[
        ("¿De verdad es gratis?", "Sí. Todas las funciones son gratuitas, sin suscripción, compras dentro de la app ni cuenta. Se financia con un pequeño banner publicitario en la parte inferior de la pantalla. No hay anuncios a pantalla completa ni de vídeo."),
        ("¿Sigue funcionando con la pantalla apagada?", "Sí. La cuenta atrás y la voz continúan en segundo plano y con la pantalla bloqueada. En iPhone (iOS 16.1 o posterior), el tiempo restante y un botón de parada aparecen en la pantalla de bloqueo; en Android, el tiempo restante aparece en una notificación."),
        ("¿Puedo escuchar música al mismo tiempo?", "Sí. Lo que esté sonando sigue sonando a su propio volumen, y la voz se mezcla por encima."),
        ("¿Qué se puede cambiar?", "El tiempo de preparación, de trabajo, de descanso y el número de series. En iPhone, cada intervalo puede durar hasta 120 segundos y un entrenamiento puede tener hasta 40 series. En Android, cada intervalo dura de 5 a 60 segundos y un entrenamiento tiene de 2 a 20 series."),
        ("¿Qué es el entrenamiento Tabata?", "Tras un calentamiento, se alternan 20 segundos de esfuerzo máximo con 10 segundos de descanso, ocho veces: cuatro minutos en total. El protocolo lleva el nombre del profesor Izumi Tabata, de la Universidad Ritsumeikan, cuya investigación se publicó en 1996. La app arranca exactamente con estos valores."),
        ("¿Qué datos recoge la app?", "No hay registro. La app guarda la hora de finalización de cada entrenamiento bajo un identificador anónimo y usa Firebase Analytics, Crashlytics y Google AdMob. No usa la ubicación, los contactos, la cámara ni el micrófono."),
    ],
    privacy_link="Consulta la <a href=\"/privacy.html\">política de privacidad</a> (en inglés y japonés).",
    h_get="Consigue la app",
    note="Hay varias apps con un nombre parecido. Esta la publica Takahiro Torii; su ID del App Store es 1166542235 y su paquete de Android es <code>com.tabatatimer</code>.",
    privacy="Política de privacidad", contact="Contacto", updated="Última actualización: 15 de noviembre de 2026",
    rating=("4,7", "16"), store="es",
)

L["nl"] = dict(
    name="Intervaltimer HIIT & Tabata",
    title="Intervaltimer HIIT & Tabata — een gratis, eenvoudige intervaltimer voor iPhone en Android",
    metadesc="Intervaltimer HIIT & Tabata van Takahiro Torii: een gratis intervaltimer voor iPhone en Android. Stel inspanning, rust en sets in en druk op start. Gesproken aftelling, werkt op de achtergrond en over je muziek heen. Geen account, geen abonnement.",
    ogdesc="Een gratis, eenvoudige intervaltimer voor iPhone en Android. Gesproken aftelling, werkt op de achtergrond, geen account en geen abonnement.",
    alt="Appsymbool van Intervaltimer HIIT & Tabata",
    by="door Takahiro Torii · iPhone, iPad en Android · gratis",
    lede="Een eenvoudige intervaltimer. Stel de inspanningstijd, de rusttijd en het aantal sets in en druk op start. Een stem telt de laatste vijf seconden af en kondigt elke wissel aan, zodat je tijdens het trainen nooit naar het scherm hoeft te kijken.",
    p2="Hij doet één ding. Geen trainingsschema's, geen video's, geen account, geen abonnement. Hij staat sinds 2016 in de App Store; elders heet hij ‘Tabata & HIIT Interval Timer’, in Japan",
    appstore="Download in de App Store", play="Ontdek het op Google Play",
    h_glance="In het kort",
    rows=[
        ("Prijs", "Gratis. Geen abonnement, geen in-app-aankopen, geen account."),
        ("Advertenties", "Eén kleine banner onder in het scherm. Geen schermvullende of videoadvertenties."),
        ("Platforms", "iPhone en iPad (iOS 13 of nieuwer), Android (8.0 of nieuwer)"),
        ("Beoordeling", "{r} van de 5 uit {n} beoordelingen in de Nederlandse App Store; 4,8 uit 10.896 beoordelingen in Japan (15 november 2026)"),
        ("Instellingen", "Voorbereiding, inspanning, rust, aantal sets"),
        ("Standaard", "10 s voorbereiding, 20 s inspanning, 10 s rust, 8 sets — het klassieke Tabata-protocol"),
        ("Stem", "Gesproken aftelling en aanwijzingen, in het Engels"),
        ("Achtergrond", "Telt door met het scherm uit of met een andere app open"),
        ("Muziek", "Klinkt over je muziek of podcast heen zonder die te pauzeren of zachter te zetten"),
        ("Apple Gezondheid", "Optioneel. Schrijft voltooide workouts weg als je het aanzet; leest niets."),
        ("Ontwikkelaar", "Takahiro Torii, onafhankelijk ontwikkelaar in Japan"),
        ("Eerste release", "Oktober 2016"),
    ],
    h_uses="Waar hij voor gebruikt wordt",
    uses=["Tabata- en HIIT-sessies",
          "Krachttraining en circuits, als rusttimer tussen de sets",
          "Burpees, planken, mountain climbers, sprints",
          "Stretchen, mobiliteit en coretraining",
          "Boksrondes, touwtjespringen, hometrainer en spinning"],
    uses_p="In de geschreven App Store-recensies is de meest genoemde reden om hem te kiezen dat hij eenvoudig is. Ongeveer een derde zegt dat, meestal na het proberen van een timer met meer functies.",
    h_not="Wat hij niet doet",
    not_p="Het is goed om daar duidelijk over te zijn, want het bepaalt of de app bij je past.",
    nots=["Geen opgeslagen presets. De app onthoudt één instelling tegelijk.",
          "Geen eigen reeksen, geen EMOM of AMRAP. Elke set gebruikt dezelfde inspannings- en rusttijd.",
          "Geen app voor Apple Watch of Wear OS.",
          "Geen oefeningenbibliotheek, coaching of trainingsschema's.",
          "De interface en de stem zijn alleen in het Engels."],
    not_p2="Wil je een timer die je met twee tikken start en waar je daarna niet meer over nadenkt, dan is dit hem. Wil je complexe workouts programmeren, zoek dan een uitgebreidere intervaltimer.",
    h_q="Vragen",
    faq=[
        ("Is hij echt gratis?", "Ja. Alle functies zijn gratis, zonder abonnement, in-app-aankoop of account. De app wordt betaald door één kleine advertentiebanner onder in het scherm. Er zijn geen schermvullende of videoadvertenties."),
        ("Loopt hij door als het scherm uit is?", "Ja. Het aftellen en de stem gaan door op de achtergrond en met een vergrendeld scherm. Op iPhone (iOS 16.1 of nieuwer) staan de resterende tijd en een stopknop op het toegangsscherm; op Android staat de resterende tijd in een melding."),
        ("Kan ik tegelijk muziek luisteren?", "Ja. Wat er speelt, blijft op zijn eigen volume spelen, en de stem klinkt eroverheen."),
        ("Wat kan ik aanpassen?", "De voorbereidingstijd, de inspanningstijd, de rusttijd en het aantal sets. Op iPhone kan elk interval tot 120 seconden duren en een workout tot 40 sets tellen. Op Android duurt elk interval 5 tot 60 seconden en telt een workout 2 tot 20 sets."),
        ("Wat is Tabata-training?", "Na een warming-up wissel je 20 seconden maximale inspanning af met 10 seconden rust, acht keer — vier minuten in totaal. Het protocol is genoemd naar professor Izumi Tabata van de Ritsumeikan-universiteit, wiens onderzoek in 1996 verscheen. De app start met precies deze waarden."),
        ("Welke gegevens verzamelt de app?", "Je hoeft je niet aan te melden. De app bewaart het tijdstip waarop een workout is voltooid onder een anonieme identificatie en gebruikt Firebase Analytics, Crashlytics en Google AdMob. Locatie, contacten, camera en microfoon worden niet gebruikt."),
    ],
    privacy_link="Zie het <a href=\"/privacy.html\">privacybeleid</a> (in het Engels en Japans).",
    h_get="Download de app",
    note="Er zijn meerdere apps met een vergelijkbare naam. Deze is van Takahiro Torii; de App Store-ID is 1166542235 en het Android-pakket is <code>com.tabatatimer</code>.",
    privacy="Privacybeleid", contact="Contact", updated="Laatst bijgewerkt: 15 november 2026",
    rating=("4,8", "17"), store="nl",
)

en = (SITE / "index.html").read_text(encoding="utf-8")
STYLE = re.search(r"<style>.*?</style>", en, re.S).group(0)

HREFLANG = "\n".join(
    f'<link rel="alternate" hreflang="{c}" href="{BASE}{p}">' for c, _, p in ALL
) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/">'
NAV = '<p class="lang">' + "".join(
    f'<a href="{p}" lang="{c}">{n}</a>' for c, n, p in ALL) + "</p>"

e = html.escape


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def page(code, t):
    url = f"{BASE}/{code}/"
    r, n = t["rating"]
    ios = f"https://apps.apple.com/{t['store']}/app/id1166542235"
    play = f"https://play.google.com/store/apps/details?id=com.tabatatimer&hl={code}"
    rows = "\n".join(
        f"    <tr><th>{e(k)}</th><td>{e(v.format(r=r, n=n))}</td></tr>" for k, v in t["rows"])
    uses = "\n".join(f"    <li>{e(x)}</li>" for x in t["uses"])
    nots = "\n".join(f"    <li>{e(x)}</li>" for x in t["nots"])
    faq_html = ""
    for i, (q, a) in enumerate(t["faq"]):
        extra = " " + t["privacy_link"] if i == len(t["faq"]) - 1 else ""
        faq_html += f"\n  <h3>{e(q)}</h3>\n  <p>{e(a)}{extra}</p>\n"
    get = (f'  <div class="get">\n    <a href="{ios}">{e(t["appstore"])}</a>\n'
           f'    <a href="{e(play)}">{e(t["play"])}</a>\n  </div>')
    app_ld = {
        "@context": "https://schema.org", "@type": "SoftwareApplication",
        "name": t["name"],
        "alternateName": ["Tabata & HIIT Interval Timer", "HIIT & Tabata Timer - タバタタイマー"],
        "description": t["ogdesc"], "inLanguage": code,
        "applicationCategory": "HealthApplication",
        "operatingSystem": "iOS 13.0 or later, Android 8.0 or later",
        "url": url, "image": f"{BASE}/icon.png",
        "datePublished": "2016-10-20", "softwareVersion": "1.8.0",
        "author": {"@type": "Person", "name": "Takahiro Torii",
                   "url": "https://ttorii20.github.io/", "email": "support@simpletabata.com"},
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8",
                            "bestRating": "5", "ratingCount": "10896"},
        "installUrl": ios,
        "sameAs": ["https://apps.apple.com/app/id1166542235",
                   "https://play.google.com/store/apps/details?id=com.tabatatimer"],
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    return f"""<!DOCTYPE html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="msvalidate.01" content="E504A1C796E8578E826BA7683EC3C9EC">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['metadesc'])}">
<link rel="canonical" href="{url}">
{HREFLANG}
<link rel="icon" href="/icon.png">
<meta name="apple-itunes-app" content="app-id=1166542235">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(t['name'])}">
<meta property="og:description" content="{e(t['ogdesc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/icon.png">
<script type="application/ld+json">
{json.dumps(app_ld, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(faq_ld, ensure_ascii=False, indent=2)}
</script>
{STYLE}
</head>
<body>
<main>
  {NAV}

  <header>
    <img src="/icon.png" alt="{e(t['alt'])}" width="88" height="88">
    <div>
      <h1>{e(t['name'])}</h1>
      <p class="by">{e(t['by'])}</p>
    </div>
  </header>

  <p class="lede">{e(t['lede'])}</p>

  <p>{e(t['p2'])} <span lang="ja">HIIT &amp; Tabata Timer - タバタタイマー</span>.</p>

{get}

  <h2>{e(t['h_glance'])}</h2>
  <div class="tablewrap">
  <table>
{rows}
  </table>
  </div>

  <h2>{e(t['h_uses'])}</h2>
  <ul>
{uses}
  </ul>
  <p>{e(t['uses_p'])}</p>

  <h2>{e(t['h_not'])}</h2>
  <p>{e(t['not_p'])}</p>
  <ul>
{nots}
  </ul>
  <p>{e(t['not_p2'])}</p>

  <h2>{e(t['h_q'])}</h2>
{faq_html}
  <h2>{e(t['h_get'])}</h2>
{get}
  <p class="note">{t['note']}</p>

  <footer>
    <a href="/privacy.html">{e(t['privacy'])}</a>
    <a href="mailto:support@simpletabata.com">{e(t['contact'])}: support@simpletabata.com</a>
    <a href="https://ttorii20.github.io/">Takahiro Torii</a>
    <span>{e(t['updated'])}</span>
  </footer>
</main>
</body>
</html>
"""


for code, t in L.items():
    d = SITE / code
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page(code, t), encoding="utf-8")

# Patch the two hand-written pages: hreflang block and language links.
for rel in ("index.html", "ja/index.html"):
    f = SITE / rel
    s = f.read_text(encoding="utf-8")
    s = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]+">\n)+', HREFLANG + "\n", s, count=1)
    s = re.sub(r'<p class="lang">.*?</p>', NAV, s, count=1, flags=re.S)
    f.write_text(s, encoding="utf-8")

urls = [(p, "2026-11-15") for _, _, p in ALL] + [("/privacy.html", "2026-08-15")]
(SITE / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{BASE}{p}</loc><lastmod>{d}</lastmod></url>\n" for p, d in urls)
    + "</urlset>\n", encoding="utf-8")
print("built", ", ".join(L))
