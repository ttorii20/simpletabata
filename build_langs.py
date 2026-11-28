#!/usr/bin/env python3
"""Generate the fr/de/it/es/nl/sv/ko/zh-hant pages of simpletabata.com from one template.

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
       ("nl", "Nederlands", "/nl/"), ("sv", "Svenska", "/sv/"), ("ko", "한국어", "/ko/"),
       ("zh-Hant", "繁體中文", "/zh-hant/")]
PATHS = {c: p for c, _, p in ALL}

L = {}

L["fr"] = dict(
    name="Minuteur Sport HIIT & Tabata",
    title="Minuteur Sport HIIT & Tabata — un minuteur d'intervalles gratuit et simple pour iPhone et Android",
    metadesc="Minuteur Sport HIIT & Tabata, par Takahiro Torii : un minuteur d'intervalles gratuit pour iPhone et Android. Réglez l'effort, le repos et les séries, puis lancez. Décompte vocal, fonctionne en arrière-plan, par-dessus votre musique. Sans compte ni abonnement.",
    ogdesc="Un minuteur d'intervalles gratuit et simple pour iPhone et Android. Décompte vocal, arrière-plan, sans compte ni abonnement.",
    alt="Icône de l'app Minuteur Sport HIIT & Tabata",
    by="par Takahiro Torii · iPhone, iPad et Android · gratuit",
    summary="Minuteur Sport HIIT & Tabata est une app de minuteur d'intervalles pour iPhone et iPad (iOS 15 ou version ultérieure) et Android (8.0 ou version ultérieure), créée par Takahiro Torii. Elle est gratuite, avec une seule petite bannière publicitaire : pas d'abonnement, pas d'achats intégrés, pas de compte. Sur iPhone comme sur Android, l'effort se règle de 5 à 300 secondes, la préparation et le repos de 5 à 120 secondes, et le nombre de séries de 2 à 40 ; on peut enregistrer jusqu'à cinq minuteurs, et le signal est une voix féminine ou masculine, ou l'un des trois bips (aigu, doux, sifflet). Dernière mise à jour : 28 novembre 2026, pour la version 1.8.2 sur iPhone et Android.",
    lede="Un minuteur d'intervalles tout simple. Réglez le temps d'effort, le temps de repos et le nombre de séries, puis appuyez sur démarrer. Une voix compte les cinq dernières secondes et annonce chaque changement : vous n'avez jamais besoin de regarder l'écran pendant l'entraînement.",
    p2="Il ne fait qu'une chose. Pas de programmes d'entraînement, pas de vidéos, pas de compte, pas d'abonnement. Il est sur l'App Store depuis 2016 ; ailleurs, il s'appelle « Tabata & HIIT Interval Timer », et au Japon",
    appstore="Télécharger dans l'App Store", play="Disponible sur Google Play",
    h_glance="En bref",
    rows=[
        ("Prix", "Gratuit. Sans abonnement, sans achats intégrés, sans compte."),
        ("Publicité", "Une petite bannière en bas de l'écran. Aucune publicité plein écran ni vidéo."),
        ("Plateformes", "iPhone et iPad (iOS 15 ou version ultérieure), Android (8.0 ou version ultérieure)"),
        ("Note", "{r} sur 5 pour {n} notes sur l'App Store en France ; 4,8 pour 10 924 notes au Japon (23 novembre 2026)"),
        ("Réglages", "Préparation, effort, repos, nombre de séries"),
        ("Par défaut", "10 s de préparation, 20 s d'effort, 10 s de repos, 8 séries — le protocole Tabata classique"),
        ("Son", "Voix (féminine ou masculine) ou bip (trois sortes) ; annonces en anglais."),
        ("Minuteurs", "Jusqu'à cinq minuteurs enregistrés ; on passe de l'un à l'autre en balayant l'écran"),
        ("Arrière-plan", "Continue de compter écran éteint ou dans une autre app"),
        ("Musique", "Se superpose à votre musique ou à votre podcast sans les mettre en pause ni baisser le volume"),
        ("Apple Santé", "Sur iPhone, facultatif. Enregistre les séances terminées une fois activé ; ne lit rien."),
        ("Développeur", "Takahiro Torii, développeur indépendant au Japon"),
        ("Première sortie", "Octobre 2016"),
    ],
    h_uses="À quoi il sert",
    uses=["Séances Tabata et HIIT, fractionné",
          "Musculation et circuits, comme minuteur de repos entre les séries",
          "Burpees, gainage, mountain climbers, sprints",
          "Étirements, mobilité, renforcement du tronc",
          "Rounds de boxe, corde à sauter, vélo d'appartement"],
    uses_more="Certains usages et certaines questions ont leur propre page :",
    uses_p="Dans les avis écrits sur l'App Store, la raison la plus souvent donnée pour l'avoir choisi est sa simplicité. Environ un tiers des avis le disent, souvent après avoir essayé un minuteur plus chargé en fonctions.",
    h_not="Ce qu'il ne fait pas",
    not_p="Autant le dire clairement, car c'est ce qui détermine si l'app vous convient.",
    nots=["Pas plus de cinq minuteurs enregistrés.",
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
        ("Que peut-on régler ?", "Le temps de préparation, d'effort, de repos et le nombre de séries. Sur iPhone comme sur Android, l'effort peut durer jusqu'à 300 secondes (5 minutes), la préparation et le repos jusqu'à 120 secondes, et une séance compter jusqu'à 40 séries."),
        ("Qu'est-ce que la méthode Tabata ?", "Après un échauffement, on alterne 20 secondes d'effort maximal et 10 secondes de repos, huit fois — quatre minutes au total. Le protocole porte le nom du professeur Izumi Tabata, de l'université Ritsumeikan, dont les travaux ont été publiés en 1996. L'app démarre exactement sur ces valeurs."),
        ("Peut-on remplacer la voix par un bip ?", "Oui, sur iPhone comme sur Android. Dans les réglages, « Sound » propose une voix féminine, une voix masculine ou trois sortes de bips ; touchez-en un pour l'écouter. Les bips s'entendent mieux dans une salle ou par-dessus la musique."),
        ("Peut-on enregistrer plusieurs minuteurs ?", "Oui, jusqu'à cinq, sur iPhone comme sur Android. Ajoutez-en un dans « Timers », dans les réglages, puis balayez l'écran principal vers la gauche ou la droite pour en changer."),
        ("Convient-il aux rounds de boxe de 3 minutes ?", "Oui, sur iPhone comme sur Android. Le temps d'effort va jusqu'à 300 secondes, soit 5 minutes, et le repos jusqu'à 120 secondes : 3 minutes de round et 1 minute de repos se règlent directement."),
        ("Quelles données l'app collecte-t-elle ?", "Il n'y a pas d'inscription. L'app enregistre l'heure de fin de chaque séance sous un identifiant anonyme et utilise Firebase Analytics, Crashlytics et Google AdMob. Elle n'utilise ni la localisation, ni les contacts, ni l'appareil photo, ni le micro."),
    ],
    privacy_link="Voir la <a href=\"/privacy.html\">politique de confidentialité</a> (en anglais et en japonais).",
    h_get="Obtenir l'app",
    note="Plusieurs apps portent un nom proche. Celle-ci est publiée par Takahiro Torii ; son identifiant App Store est 1166542235 et son paquet Android <code>com.tabatatimer</code>.",
    privacy="Politique de confidentialité", contact="Contact", updated="Dernière mise à jour : 28 novembre 2026",
    rating=("4,8", "71"), store="fr",
)

L["de"] = dict(
    name="Intervall-Timer HIIT & Tabata",
    title="Intervall-Timer HIIT & Tabata — ein kostenloser, einfacher Intervall-Timer für iPhone und Android",
    metadesc="Intervall-Timer HIIT & Tabata von Takahiro Torii: ein kostenloser Intervall-Timer für iPhone und Android. Belastung, Pause und Sätze einstellen, Start drücken. Sprach-Countdown, läuft im Hintergrund und über Ihrer Musik. Ohne Konto, ohne Abo.",
    ogdesc="Ein kostenloser, einfacher Intervall-Timer für iPhone und Android. Sprach-Countdown, läuft im Hintergrund, ohne Konto und ohne Abo.",
    alt="App-Symbol von Intervall-Timer HIIT & Tabata",
    by="von Takahiro Torii · iPhone, iPad und Android · kostenlos",
    summary="Intervall-Timer HIIT & Tabata ist eine Intervall-Timer-App für iPhone und iPad (iOS 15 oder neuer) und Android (8.0 oder neuer), entwickelt von Takahiro Torii. Sie ist kostenlos und zeigt nur ein kleines Werbebanner: kein Abo, keine In-App-Käufe, kein Konto. Auf dem iPhone wie unter Android lässt sich die Belastungszeit von 5 bis 300 Sekunden einstellen, Vorbereitung und Pause von 5 bis 120 Sekunden und die Anzahl der Sätze von 2 bis 40; bis zu fünf Timer können gespeichert werden, und als Signal gibt es eine weibliche oder männliche Stimme oder einen von drei Signaltönen (scharf, weich, Pfeife). Zuletzt aktualisiert am 28. November 2026, Stand: Version 1.8.2 für iPhone und Android.",
    lede="Ein einfacher Intervall-Timer. Belastungszeit, Pausenzeit und Anzahl der Sätze einstellen, Start drücken. Eine Stimme zählt die letzten fünf Sekunden herunter und sagt jeden Wechsel an – Sie müssen beim Training nie auf den Bildschirm schauen.",
    p2="Er kann genau eine Sache. Keine Trainingspläne, keine Videos, kein Konto, kein Abo. Im App Store gibt es ihn seit 2016; anderswo heißt er „Tabata & HIIT Interval Timer“, in Japan",
    appstore="Laden im App Store", play="Jetzt bei Google Play",
    h_glance="Auf einen Blick",
    rows=[
        ("Preis", "Kostenlos. Kein Abo, keine In-App-Käufe, kein Konto."),
        ("Werbung", "Ein kleines Banner am unteren Bildschirmrand. Keine Vollbild- oder Videowerbung."),
        ("Plattformen", "iPhone und iPad (iOS 15 oder neuer), Android (8.0 oder neuer)"),
        ("Bewertung", "{r} von 5 bei {n} Bewertungen im deutschen App Store; 4,8 bei 10.924 Bewertungen in Japan (23. November 2026)"),
        ("Einstellungen", "Vorbereitung, Belastung, Pause, Anzahl der Sätze"),
        ("Standard", "10 s Vorbereitung, 20 s Belastung, 10 s Pause, 8 Sätze – das klassische Tabata-Protokoll"),
        ("Ton", "Stimme (weiblich oder männlich) oder Signalton (drei Arten); Ansagen auf Englisch."),
        ("Timer", "Bis zu fünf gespeicherte Timer; Wechsel per Wischen"),
        ("Hintergrund", "Zählt weiter, wenn der Bildschirm aus ist oder eine andere App geöffnet ist"),
        ("Musik", "Läuft über Ihrer Musik oder Ihrem Podcast, ohne sie anzuhalten oder leiser zu stellen"),
        ("Apple Health", "Auf dem iPhone, optional. Schreibt beendete Workouts, wenn eingeschaltet; liest nichts."),
        ("Entwickler", "Takahiro Torii, unabhängiger Entwickler in Japan"),
        ("Erstveröffentlichung", "Oktober 2016"),
    ],
    h_uses="Wofür er genutzt wird",
    uses=["Tabata- und HIIT-Einheiten",
          "Krafttraining und Zirkeltraining, als Pausentimer zwischen den Sätzen",
          "Burpees, Planks, Mountain Climbers, Sprints",
          "Dehnen, Mobility und Rumpftraining",
          "Boxrunden, Seilspringen, Heimtrainer und Spinning"],
    uses_more="Einige Einsatzzwecke und Fragen haben eine eigene Seite:",
    uses_p="In den geschriebenen App-Store-Rezensionen wird als Grund für die Wahl am häufigsten genannt, dass er einfach ist. Etwa ein Drittel schreibt das, meist nachdem ein Timer mit mehr Funktionen ausprobiert wurde.",
    h_not="Was er nicht kann",
    not_p="Das sei offen gesagt, denn davon hängt ab, ob die App zu Ihnen passt.",
    nots=["Höchstens fünf gespeicherte Timer.",
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
        ("Was lässt sich einstellen?", "Vorbereitungszeit, Belastungszeit, Pausenzeit und die Anzahl der Sätze. Auf dem iPhone wie unter Android kann die Belastung bis zu 300 Sekunden (5 Minuten) dauern, Vorbereitung und Pause bis zu 120 Sekunden, und ein Workout kann bis zu 40 Sätze haben."),
        ("Was ist Tabata-Training?", "Nach dem Aufwärmen wechseln sich 20 Sekunden maximale Belastung und 10 Sekunden Pause ab, achtmal – insgesamt vier Minuten. Das Protokoll ist nach Professor Izumi Tabata von der Ritsumeikan-Universität benannt, dessen Studie dazu 1996 erschien. Die App startet mit genau diesen Werten."),
        ("Gibt es statt der Stimme auch einen Signalton?", "Ja, auf dem iPhone wie unter Android. Unter „Sound“ in den Einstellungen stehen eine weibliche Stimme, eine männliche Stimme und drei Arten von Signaltönen zur Wahl; antippen, um sie zu hören. Signaltöne sind im Studio oder über Musik leichter zu hören."),
        ("Kann ich mehrere Timer speichern?", "Ja, bis zu fünf, auf dem iPhone wie unter Android. Unter „Timers“ in den Einstellungen einen hinzufügen und auf dem Hauptbildschirm nach links oder rechts wischen, um zu wechseln."),
        ("Eignet er sich für 3-Minuten-Runden beim Boxen?", "Ja, auf dem iPhone wie unter Android. Die Belastungszeit reicht bis 300 Sekunden, also 5 Minuten, die Pause bis 120 Sekunden: 3 Minuten Runde und 1 Minute Pause lassen sich direkt einstellen."),
        ("Welche Daten erfasst die App?", "Es gibt keine Anmeldung. Die App speichert den Zeitpunkt, zu dem ein Workout beendet wurde, unter einer anonymen Kennung und verwendet Firebase Analytics, Crashlytics und Google AdMob. Standort, Kontakte, Kamera und Mikrofon werden nicht verwendet."),
    ],
    privacy_link="Siehe die <a href=\"/privacy.html\">Datenschutzerklärung</a> (auf Englisch und Japanisch).",
    h_get="App laden",
    note="Mehrere Apps heißen ähnlich. Diese hier stammt von Takahiro Torii; die App-Store-ID lautet 1166542235, das Android-Paket <code>com.tabatatimer</code>.",
    privacy="Datenschutzerklärung", contact="Kontakt", updated="Zuletzt aktualisiert: 28. November 2026",
    rating=("4,7", "104"), store="de",
)

L["it"] = dict(
    name="Timer HIIT Tabata Allenamento",
    title="Timer HIIT Tabata Allenamento — un timer a intervalli gratuito e semplice per iPhone e Android",
    metadesc="Timer HIIT Tabata Allenamento di Takahiro Torii: un timer a intervalli gratuito per iPhone e Android. Imposta lavoro, recupero e serie, poi premi start. Conto alla rovescia vocale, funziona in background e sopra la tua musica. Senza account né abbonamento.",
    ogdesc="Un timer a intervalli gratuito e semplice per iPhone e Android. Conto alla rovescia vocale, funziona in background, senza account né abbonamento.",
    alt="Icona dell'app Timer HIIT Tabata Allenamento",
    by="di Takahiro Torii · iPhone, iPad e Android · gratis",
    summary="Timer HIIT Tabata Allenamento è un'app di timer a intervalli per iPhone e iPad (iOS 15 o versioni successive) e Android (8.0 o versioni successive), sviluppata da Takahiro Torii. È gratuita, con un solo piccolo banner pubblicitario: nessun abbonamento, nessun acquisto in-app, nessun account. Su iPhone come su Android il tempo di lavoro si imposta da 5 a 300 secondi, la preparazione e il recupero da 5 a 120 secondi e il numero di serie da 2 a 40; si possono salvare fino a cinque timer, e gli avvisi sono dati da una voce femminile o maschile oppure da uno dei tre segnali acustici (acuto, morbido, fischietto). Ultimo aggiornamento: 28 novembre 2026, per la versione 1.8.2 per iPhone e Android.",
    lede="Un timer a intervalli semplice. Imposta il tempo di lavoro, il tempo di recupero e il numero di serie, poi premi start. Una voce conta gli ultimi cinque secondi e annuncia ogni cambio, così non devi mai guardare lo schermo mentre ti alleni.",
    p2="Fa una cosa sola. Niente programmi di allenamento, niente video, niente account, niente abbonamento. È sull'App Store dal 2016; altrove si chiama «Tabata & HIIT Interval Timer», in Giappone",
    appstore="Scarica su App Store", play="Disponibile su Google Play",
    h_glance="In breve",
    rows=[
        ("Prezzo", "Gratis. Nessun abbonamento, nessun acquisto in-app, nessun account."),
        ("Pubblicità", "Un piccolo banner in fondo allo schermo. Nessuna pubblicità a schermo intero né video."),
        ("Piattaforme", "iPhone e iPad (iOS 15 o versioni successive), Android (8.0 o versioni successive)"),
        ("Valutazione", "{r} su 5 con {n} valutazioni sull'App Store in Italia; 4,8 con 10.924 valutazioni in Giappone (23 novembre 2026)"),
        ("Impostazioni", "Preparazione, lavoro, recupero, numero di serie"),
        ("Predefinito", "10 s di preparazione, 20 s di lavoro, 10 s di recupero, 8 serie — il protocollo Tabata classico"),
        ("Suono", "Voce (femminile o maschile) o segnale acustico (tre tipi); annunci in inglese."),
        ("Timer", "Fino a cinque timer salvati; si cambia scorrendo lo schermo"),
        ("Background", "Continua a contare con lo schermo spento o con un'altra app aperta"),
        ("Musica", "Si sovrappone alla tua musica o al tuo podcast senza metterli in pausa né abbassarne il volume"),
        ("Apple Salute", "Su iPhone, facoltativo. Scrive gli allenamenti completati quando è attivo; non legge nulla."),
        ("Sviluppatore", "Takahiro Torii, sviluppatore indipendente in Giappone"),
        ("Prima pubblicazione", "Ottobre 2016"),
    ],
    h_uses="Per cosa viene usato",
    uses=["Sessioni Tabata e HIIT",
          "Allenamento con i pesi e circuiti, come timer di recupero tra le serie",
          "Burpees, plank, mountain climbers, scatti",
          "Stretching, mobilità e core",
          "Round di boxe, salto con la corda, cyclette e spinning"],
    uses_more="Alcuni usi e alcune domande hanno una pagina dedicata:",
    uses_p="Nelle recensioni scritte sull'App Store, il motivo citato più spesso per averlo scelto è che è semplice. Lo dice circa un terzo delle recensioni, di solito dopo aver provato un timer con più funzioni.",
    h_not="Cosa non fa",
    not_p="Meglio dirlo chiaramente, perché è questo che decide se l'app fa per te.",
    nots=["Non più di cinque timer salvati.",
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
        ("Cosa si può modificare?", "Il tempo di preparazione, di lavoro, di recupero e il numero di serie. Su iPhone come su Android il lavoro può durare fino a 300 secondi (5 minuti), la preparazione e il recupero fino a 120 secondi, e un allenamento può avere fino a 40 serie."),
        ("Che cos'è l'allenamento Tabata?", "Dopo il riscaldamento si alternano 20 secondi di sforzo massimo e 10 secondi di recupero, per otto volte: quattro minuti in tutto. Il protocollo prende il nome dal professor Izumi Tabata dell'Università Ritsumeikan, la cui ricerca è stata pubblicata nel 1996. L'app parte esattamente con questi valori."),
        ("Si può usare un segnale acustico al posto della voce?", "Sì, su iPhone come su Android. In «Sound», nelle impostazioni, si sceglie tra una voce femminile, una voce maschile e tre tipi di segnale acustico; toccane uno per ascoltarlo. I segnali si sentono meglio in palestra o sopra la musica."),
        ("Si possono salvare più timer?", "Sì, fino a cinque, su iPhone come su Android. Aggiungine uno in «Timers», nelle impostazioni, poi scorri a sinistra o a destra sulla schermata principale per cambiare."),
        ("Va bene per i round di boxe da 3 minuti?", "Sì, su iPhone come su Android. Il tempo di lavoro arriva a 300 secondi, cioè 5 minuti, e il recupero a 120 secondi: 3 minuti di round e 1 minuto di recupero si impostano direttamente."),
        ("Quali dati raccoglie l'app?", "Non c'è registrazione. L'app salva l'orario di completamento di ogni allenamento sotto un identificatore anonimo e usa Firebase Analytics, Crashlytics e Google AdMob. Non usa posizione, contatti, fotocamera né microfono."),
    ],
    privacy_link="Vedi l'<a href=\"/privacy.html\">informativa sulla privacy</a> (in inglese e giapponese).",
    h_get="Scarica l'app",
    note="Diverse app hanno un nome simile. Questa è pubblicata da Takahiro Torii; l'ID App Store è 1166542235 e il pacchetto Android è <code>com.tabatatimer</code>.",
    privacy="Informativa sulla privacy", contact="Contatto", updated="Ultimo aggiornamento: 28 novembre 2026",
    rating=("4,7", "19"), store="it",
)

L["es"] = dict(
    name="HIIT Tabata Temporizador",
    title="HIIT Tabata Temporizador — un temporizador de intervalos gratuito y sencillo para iPhone y Android",
    metadesc="HIIT Tabata Temporizador, de Takahiro Torii: un temporizador de intervalos gratuito para iPhone y Android. Ajusta el trabajo, el descanso y las series, y pulsa empezar. Cuenta atrás por voz, funciona en segundo plano y sobre tu música. Sin cuenta ni suscripción.",
    ogdesc="Un temporizador de intervalos gratuito y sencillo para iPhone y Android. Cuenta atrás por voz, funciona en segundo plano, sin cuenta ni suscripción.",
    alt="Icono de la app HIIT Tabata Temporizador",
    by="de Takahiro Torii · iPhone, iPad y Android · gratis",
    summary="HIIT Tabata Temporizador es una app de temporizador de intervalos para iPhone y iPad (iOS 15 o posterior) y Android (8.0 o posterior), creada por Takahiro Torii. Es gratuita, con un solo banner publicitario pequeño: sin suscripción, sin compras dentro de la app y sin cuenta. En iPhone y en Android, el tiempo de trabajo se ajusta de 5 a 300 segundos, la preparación y el descanso de 5 a 120 segundos, y el número de series de 2 a 40; se pueden guardar hasta cinco temporizadores, y los avisos son una voz femenina o masculina, o uno de los tres pitidos (agudo, suave, silbato). Última actualización: 28 de noviembre de 2026, para la versión 1.8.2 de iPhone y Android.",
    lede="Un temporizador de intervalos sencillo. Ajusta el tiempo de trabajo, el tiempo de descanso y el número de series, y pulsa empezar. Una voz cuenta los últimos cinco segundos y anuncia cada cambio, así que nunca tienes que mirar la pantalla mientras entrenas.",
    p2="Hace una sola cosa. No hay planes de entrenamiento, ni vídeos, ni cuenta, ni suscripción. Está en el App Store desde 2016; en otros países se llama «Tabata & HIIT Interval Timer», y en Japón",
    appstore="Descargar en el App Store", play="Disponible en Google Play",
    h_glance="De un vistazo",
    rows=[
        ("Precio", "Gratis. Sin suscripción, sin compras dentro de la app, sin cuenta."),
        ("Publicidad", "Un pequeño banner en la parte inferior de la pantalla. Sin anuncios a pantalla completa ni de vídeo."),
        ("Plataformas", "iPhone y iPad (iOS 15 o posterior), Android (8.0 o posterior)"),
        ("Valoración", "{r} de 5 con {n} valoraciones en el App Store de España; 4,8 con 10.924 valoraciones en Japón (23 de noviembre de 2026)"),
        ("Ajustes", "Preparación, trabajo, descanso, número de series"),
        ("Por defecto", "10 s de preparación, 20 s de trabajo, 10 s de descanso, 8 series: el protocolo Tabata clásico"),
        ("Sonido", "Voz (femenina o masculina) o pitido (tres tipos); avisos en inglés."),
        ("Temporizadores", "Hasta cinco temporizadores guardados; se cambia deslizando la pantalla"),
        ("Segundo plano", "Sigue contando con la pantalla apagada o con otra app abierta"),
        ("Música", "Suena sobre tu música o tu pódcast sin pausarlos ni bajarles el volumen"),
        ("Apple Salud", "En iPhone, opcional. Registra los entrenamientos terminados cuando se activa; no lee nada."),
        ("Desarrollador", "Takahiro Torii, desarrollador independiente en Japón"),
        ("Primera publicación", "Octubre de 2016"),
    ],
    h_uses="Para qué se usa",
    uses=["Sesiones de Tabata y HIIT",
          "Entrenamiento de fuerza y circuitos con pesas, como temporizador de descanso entre series",
          "Burpees, planchas, mountain climbers, sprints",
          "Estiramientos, movilidad y trabajo de core",
          "Asaltos de boxeo, comba, bicicleta estática y spinning"],
    uses_more="Algunos usos y preguntas tienen su propia página:",
    uses_p="En las reseñas escritas del App Store, la razón que más se repite para elegirlo es que es sencillo. Lo dice aproximadamente un tercio de ellas, normalmente después de haber probado un temporizador con más funciones.",
    h_not="Lo que no hace",
    not_p="Conviene decirlo claramente, porque de ello depende que la app sea la adecuada para ti.",
    nots=["No más de cinco temporizadores guardados.",
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
        ("¿Qué se puede cambiar?", "El tiempo de preparación, de trabajo, de descanso y el número de series. En iPhone y en Android, el trabajo puede durar hasta 300 segundos (5 minutos), la preparación y el descanso hasta 120 segundos, y un entrenamiento puede tener hasta 40 series."),
        ("¿Qué es el entrenamiento Tabata?", "Tras un calentamiento, se alternan 20 segundos de esfuerzo máximo con 10 segundos de descanso, ocho veces: cuatro minutos en total. El protocolo lleva el nombre del profesor Izumi Tabata, de la Universidad Ritsumeikan, cuya investigación se publicó en 1996. La app arranca exactamente con estos valores."),
        ("¿Se puede usar un pitido en lugar de la voz?", "Sí, en iPhone y en Android. En «Sound», en los ajustes, se elige entre una voz femenina, una voz masculina y tres tipos de pitido; toca uno para oírlo. Los pitidos se oyen mejor en un gimnasio o por encima de la música."),
        ("¿Se pueden guardar varios temporizadores?", "Sí, hasta cinco, en iPhone y en Android. Añade uno en «Timers», en los ajustes, y desliza a la izquierda o a la derecha en la pantalla principal para cambiar."),
        ("¿Sirve para asaltos de boxeo de 3 minutos?", "Sí, en iPhone y en Android. El tiempo de trabajo llega a 300 segundos, es decir, 5 minutos, y el descanso a 120 segundos: 3 minutos de asalto y 1 minuto de descanso se ajustan directamente."),
        ("¿Qué datos recoge la app?", "No hay registro. La app guarda la hora de finalización de cada entrenamiento bajo un identificador anónimo y usa Firebase Analytics, Crashlytics y Google AdMob. No usa la ubicación, los contactos, la cámara ni el micrófono."),
    ],
    privacy_link="Consulta la <a href=\"/privacy.html\">política de privacidad</a> (en inglés y japonés).",
    h_get="Consigue la app",
    note="Hay varias apps con un nombre parecido. Esta la publica Takahiro Torii; su ID del App Store es 1166542235 y su paquete de Android es <code>com.tabatatimer</code>.",
    privacy="Política de privacidad", contact="Contacto", updated="Última actualización: 28 de noviembre de 2026",
    rating=("4,6", "17"), store="es",
)

L["nl"] = dict(
    name="Intervaltimer HIIT & Tabata",
    title="Intervaltimer HIIT & Tabata — een gratis, eenvoudige intervaltimer voor iPhone en Android",
    metadesc="Intervaltimer HIIT & Tabata van Takahiro Torii: een gratis intervaltimer voor iPhone en Android. Stel inspanning, rust en sets in en druk op start. Gesproken aftelling, werkt op de achtergrond en over je muziek heen. Geen account, geen abonnement.",
    ogdesc="Een gratis, eenvoudige intervaltimer voor iPhone en Android. Gesproken aftelling, werkt op de achtergrond, geen account en geen abonnement.",
    alt="Appsymbool van Intervaltimer HIIT & Tabata",
    by="door Takahiro Torii · iPhone, iPad en Android · gratis",
    summary="Intervaltimer HIIT & Tabata is een intervaltimer-app voor iPhone en iPad (iOS 15 of nieuwer) en Android (8.0 of nieuwer), gemaakt door Takahiro Torii. De app is gratis, met één kleine advertentiebanner: geen abonnement, geen in-app-aankopen, geen account. Op iPhone en Android stel je de inspanningstijd in van 5 tot 300 seconden, de voorbereiding en de rust van 5 tot 120 seconden en het aantal sets van 2 tot 40; je kunt maximaal vijf timers bewaren, en de signalen zijn een vrouwen- of mannenstem of een van de drie pieptonen (scherp, zacht, fluitje). Laatst bijgewerkt op 28 november 2026, voor versie 1.8.2 op iPhone en Android.",
    lede="Een eenvoudige intervaltimer. Stel de inspanningstijd, de rusttijd en het aantal sets in en druk op start. Een stem telt de laatste vijf seconden af en kondigt elke wissel aan, zodat je tijdens het trainen nooit naar het scherm hoeft te kijken.",
    p2="Hij doet één ding. Geen trainingsschema's, geen video's, geen account, geen abonnement. Hij staat sinds 2016 in de App Store; elders heet hij ‘Tabata & HIIT Interval Timer’, in Japan",
    appstore="Download in de App Store", play="Ontdek het op Google Play",
    h_glance="In het kort",
    rows=[
        ("Prijs", "Gratis. Geen abonnement, geen in-app-aankopen, geen account."),
        ("Advertenties", "Eén kleine banner onder in het scherm. Geen schermvullende of videoadvertenties."),
        ("Platforms", "iPhone en iPad (iOS 15 of nieuwer), Android (8.0 of nieuwer)"),
        ("Beoordeling", "{r} van de 5 uit {n} beoordelingen in de Nederlandse App Store; 4,8 uit 10.924 beoordelingen in Japan (23 november 2026)"),
        ("Instellingen", "Voorbereiding, inspanning, rust, aantal sets"),
        ("Standaard", "10 s voorbereiding, 20 s inspanning, 10 s rust, 8 sets — het klassieke Tabata-protocol"),
        ("Geluid", "Stem (vrouw of man) of pieptoon (drie soorten); aanwijzingen in het Engels."),
        ("Timers", "Tot vijf opgeslagen timers; wisselen door te vegen"),
        ("Achtergrond", "Telt door met het scherm uit of met een andere app open"),
        ("Muziek", "Klinkt over je muziek of podcast heen zonder die te pauzeren of zachter te zetten"),
        ("Apple Gezondheid", "Op iPhone, optioneel. Schrijft voltooide workouts weg als je het aanzet; leest niets."),
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
    nots=["Niet meer dan vijf opgeslagen timers.",
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
        ("Wat kan ik aanpassen?", "De voorbereidingstijd, de inspanningstijd, de rusttijd en het aantal sets. Op iPhone en Android kan de inspanning tot 300 seconden (5 minuten) duren, de voorbereiding en de rust tot 120 seconden, en een workout kan tot 40 sets tellen."),
        ("Wat is Tabata-training?", "Na een warming-up wissel je 20 seconden maximale inspanning af met 10 seconden rust, acht keer — vier minuten in totaal. Het protocol is genoemd naar professor Izumi Tabata van de Ritsumeikan-universiteit, wiens onderzoek in 1996 verscheen. De app start met precies deze waarden."),
        ("Kan ik een pieptoon gebruiken in plaats van de stem?", "Ja, op iPhone en Android. Onder ‘Sound’ in de instellingen kies je een vrouwenstem, een mannenstem of een van de drie pieptonen; tik erop om hem te horen. Pieptonen zijn beter te horen in de sportschool of boven de muziek uit."),
        ("Kan ik meerdere timers bewaren?", "Ja, tot vijf, op iPhone en Android. Voeg er een toe onder ‘Timers’ in de instellingen en veeg op het hoofdscherm naar links of rechts om te wisselen."),
        ("Is hij geschikt voor boksrondes van 3 minuten?", "Ja, op iPhone en Android. De inspanningstijd gaat tot 300 seconden, dus 5 minuten, en de rust tot 120 seconden: 3 minuten ronde en 1 minuut rust stel je direct in."),
        ("Welke gegevens verzamelt de app?", "Je hoeft je niet aan te melden. De app bewaart het tijdstip waarop een workout is voltooid onder een anonieme identificatie en gebruikt Firebase Analytics, Crashlytics en Google AdMob. Locatie, contacten, camera en microfoon worden niet gebruikt."),
    ],
    privacy_link="Zie het <a href=\"/privacy.html\">privacybeleid</a> (in het Engels en Japans).",
    h_get="Download de app",
    note="Er zijn meerdere apps met een vergelijkbare naam. Deze is van Takahiro Torii; de App Store-ID is 1166542235 en het Android-pakket is <code>com.tabatatimer</code>.",
    privacy="Privacybeleid", contact="Contact", updated="Laatst bijgewerkt: 28 november 2026",
    rating=("4,8", "17"), store="nl",
)

L["sv"] = dict(
    name="Intervalltimer HIIT & Tabata",
    title="Intervalltimer HIIT & Tabata — en gratis, enkel intervalltimer för iPhone och Android",
    metadesc="Intervalltimer HIIT & Tabata av Takahiro Torii: en gratis intervalltimer för iPhone och Android. Ställ in arbete, vila och antal set och tryck på start. Röstnedräkning, fortsätter i bakgrunden och hörs över din musik. Inget konto, ingen prenumeration.",
    ogdesc="En gratis, enkel intervalltimer för iPhone och Android. Röstnedräkning, fortsätter i bakgrunden, inget konto och ingen prenumeration.",
    alt="Appsymbol för Intervalltimer HIIT & Tabata",
    by="av Takahiro Torii · iPhone, iPad och Android · gratis",
    summary="Intervalltimer HIIT & Tabata är en intervalltimer-app för iPhone och iPad (iOS 15 eller senare) och Android (8.0 eller senare), utvecklad av Takahiro Torii. Den är gratis, med en enda liten annonsbanner: ingen prenumeration, inga köp i appen och inget konto. På iPhone och Android kan arbetstiden ställas in från 5 till 300 sekunder, förberedelse och vila från 5 till 120 sekunder och antalet set från 2 till 40; upp till fem timrar kan sparas, och signalen är en kvinnlig eller manlig röst eller en av tre ljudsignaler (skarp, mjuk, visselpipa). Senast uppdaterad 28 november 2026, för version 1.8.2 på iPhone och Android.",
    lede="En enkel intervalltimer. Ställ in arbetstid, vilotid och antal set och tryck på start. En röst räknar ner de sista fem sekunderna och ropar ut varje byte, så du behöver aldrig titta på skärmen medan du tränar.",
    p2="Den gör en enda sak. Inga träningsprogram, inga videor, inget konto, ingen prenumeration. Den har funnits i App Store sedan 2016; på andra håll heter den ”Tabata & HIIT Interval Timer”, och i Japan",
    appstore="Hämta i App Store", play="Ladda ned på Google Play",
    h_glance="I korthet",
    rows=[
        ("Pris", "Gratis. Ingen prenumeration, inga köp i appen, inget konto."),
        ("Annonser", "En liten banner längst ned på skärmen. Inga helskärms- eller videoannonser."),
        ("Plattformar", "iPhone och iPad (iOS 15 eller senare), Android (8.0 eller senare)"),
        ("Betyg", "{r} av 5 från {n} betyg i App Store i Sverige; 4,8 från 10 924 betyg i Japan (23 november 2026)"),
        ("Inställningar", "Förberedelse, arbete, vila, antal set"),
        ("Standard", "10 s förberedelse, 20 s arbete, 10 s vila, 8 set – det klassiska Tabata-protokollet"),
        ("Ljud", "Röst (kvinna eller man) eller ljudsignal (tre sorter); utropen är på engelska."),
        ("Timrar", "Upp till fem sparade timrar; svep för att byta"),
        ("Bakgrund", "Räknar vidare när skärmen är av eller en annan app är öppen"),
        ("Musik", "Hörs över din musik eller podd utan att pausa den eller sänka volymen"),
        ("Apple Hälsa", "På iPhone, valfritt. Sparar avslutade pass när det är påslaget; läser ingenting."),
        ("Utvecklare", "Takahiro Torii, oberoende utvecklare i Japan"),
        ("Första utgåva", "Oktober 2016"),
    ],
    h_uses="Vad den används till",
    uses=["Tabata- och HIIT-pass",
          "Styrketräning och cirkelträning, som vilotimer mellan seten",
          "Burpees, plankan, mountain climbers, sprinter",
          "Stretch, rörlighet och bålträning",
          "Boxningsronder, hopprep, motionscykel och spinning"],
    uses_p="I de skrivna recensionerna i App Store är det vanligaste skälet till att man valt den att den är enkel. Ungefär en tredjedel skriver det, oftast efter att ha provat en timer med fler funktioner.",
    h_not="Vad den inte gör",
    not_p="Det är lika bra att säga det rakt ut, eftersom det avgör om appen passar dig.",
    nots=["Högst fem sparade timrar.",
          "Inga egna sekvenser, inga EMOM- eller AMRAP-lägen. Varje set har samma arbets- och vilotid.",
          "Ingen app för Apple Watch eller Wear OS.",
          "Inget övningsbibliotek, ingen coachning och inga träningsprogram.",
          "Appens text och röst finns bara på engelska."],
    not_p2="Vill du ha en timer som du startar med två tryck och sedan inte behöver tänka på, så är det den här. Vill du programmera komplicerade pass bör du leta efter en mer omfattande intervalltimer.",
    h_q="Frågor",
    faq=[
        ("Är den verkligen gratis?", "Ja. Alla funktioner är gratis, utan prenumeration, köp i appen eller konto. Appen finansieras av en liten annonsbanner längst ned på skärmen. Det finns inga helskärms- eller videoannonser."),
        ("Fortsätter den när skärmen är av?", "Ja. Nedräkningen och rösten fortsätter i bakgrunden och när skärmen är låst. På iPhone (iOS 16.1 eller senare) visas återstående tid och en stoppknapp på låsskärmen; på Android visas återstående tid i en avisering."),
        ("Kan jag lyssna på musik samtidigt?", "Ja. Det som spelas fortsätter på sin egen volym, och rösten läggs ovanpå."),
        ("Vad kan jag ändra?", "Förberedelsetid, arbetstid, vilotid och antal set. På iPhone och Android kan arbetet vara upp till 300 sekunder (5 minuter), förberedelse och vila upp till 120 sekunder, och ett pass kan ha upp till 40 set."),
        ("Vad är Tabata-träning?", "Efter uppvärmning växlar man mellan 20 sekunders maximal ansträngning och 10 sekunders vila, åtta gånger – fyra minuter sammanlagt. Protokollet är uppkallat efter professor Izumi Tabata vid Ritsumeikan-universitetet, vars forskning publicerades 1996. Appen startar med exakt de här värdena."),
        ("Kan jag få en ljudsignal i stället för rösten?", "Ja, på iPhone och Android. Under ”Sound” i inställningarna kan du välja en kvinnlig röst, en manlig röst eller en av tre ljudsignaler; tryck på en för att höra den. Ljudsignaler hörs bättre i en gymsal eller över musik."),
        ("Kan jag spara flera timrar?", "Ja, upp till fem, på iPhone och Android. Lägg till en under ”Timers” i inställningarna och svep åt vänster eller höger på huvudskärmen för att byta."),
        ("Fungerar den för boxningsronder på 3 minuter?", "Ja, på iPhone och Android. Arbetstiden går upp till 300 sekunder, alltså 5 minuter, och vilan upp till 120 sekunder: ronder på 3 minuter med 1 minuts vila kan ställas in direkt."),
        ("Vilka uppgifter samlar appen in?", "Ingen registrering krävs. Appen sparar tidpunkten då varje pass avslutades under en anonym identifierare och använder Firebase Analytics, Crashlytics och Google AdMob. Den använder inte plats, kontakter, kamera eller mikrofon."),
    ],
    privacy_link="Se <a href=\"/privacy.html\">integritetspolicyn</a> (på engelska och japanska).",
    h_get="Hämta appen",
    note="Flera appar har liknande namn. Den här ges ut av Takahiro Torii; App Store-ID är 1166542235 och Android-paketet är <code>com.tabatatimer</code>.",
    privacy="Integritetspolicy", contact="Kontakt", updated="Senast uppdaterad: 28 november 2026",
    rating=("4,7", "134"), store="se", currency="SEK",
)

# No ratings yet on the App Store in Korea, so the rating row gives Japan's only.
L["ko"] = dict(
    name="인터벌 타이머 - 타바타 HIIT 운동",
    title="인터벌 타이머 - 타바타 HIIT 운동 — iPhone과 Android용 무료 심플 인터벌 타이머",
    metadesc="인터벌 타이머 - 타바타 HIIT 운동(개발: Takahiro Torii). iPhone과 Android용 무료 인터벌 타이머입니다. 운동·휴식 시간과 세트 수를 정하고 시작만 누르면 됩니다. 음성 카운트다운, 백그라운드 동작, 음악과 함께 사용 가능. 계정도 구독도 없습니다.",
    ogdesc="iPhone과 Android용 무료 심플 인터벌 타이머. 음성 카운트다운, 백그라운드 동작, 계정도 구독도 없습니다.",
    alt="인터벌 타이머 - 타바타 HIIT 운동 앱 아이콘",
    by="개발: Takahiro Torii · iPhone, iPad, Android · 무료",
    summary="인터벌 타이머 - 타바타 HIIT 운동은 Takahiro Torii가 개발한 iPhone·iPad(iOS 15 이상) 및 Android(8.0 이상)용 인터벌 타이머 앱입니다. 무료이며 광고는 작은 배너 하나뿐이고, 구독·앱 내 구입·계정이 없습니다. iPhone과 Android 모두 운동 시간을 5~300초, 준비와 휴식 시간을 5~120초, 세트 수를 2~40으로 설정할 수 있고, 타이머를 5개까지 저장할 수 있으며, 신호는 여성 또는 남성 음성이나 세 가지 비프음(샤프, 소프트, 휘슬) 중에서 고를 수 있습니다. 최종 업데이트: 2026년 11월 28일(iPhone·Android 버전 1.8.2 기준).",
    lede="단순한 인터벌 타이머입니다. 운동 시간, 휴식 시간, 세트 수를 정하고 시작을 누르기만 하면 됩니다. 음성이 마지막 5초를 세고 구간이 바뀔 때마다 알려 주기 때문에, 운동 중에 화면을 볼 필요가 없습니다.",
    p2="하는 일은 하나뿐입니다. 운동 프로그램도, 동영상도, 계정도, 구독도 없습니다. 2016년부터 App Store에 올라와 있으며, 다른 나라에서는 ‘Tabata & HIIT Interval Timer’, 일본에서는",
    p2_end="라는 이름으로 제공됩니다.",
    appstore="App Store에서 다운로드", play="Google Play에서 다운로드",
    h_glance="한눈에 보기",
    rows=[
        ("가격", "무료. 구독, 앱 내 구입, 계정이 없습니다."),
        ("광고", "화면 아래의 작은 배너 하나뿐입니다. 전면 광고나 동영상 광고는 없습니다."),
        ("지원 기기", "iPhone 및 iPad(iOS 15 이상), Android(8.0 이상)"),
        ("평점", "일본 App Store에서 5점 만점에 4.8점, 평가 10,924개(2026년 11월 23일 기준)"),
        ("설정 항목", "준비 시간, 운동 시간, 휴식 시간, 세트 수"),
        ("기본값", "준비 10초, 운동 20초, 휴식 10초, 8세트 — 표준 타바타 프로토콜"),
        ("소리", "음성(여성/남성) 또는 비프음(3종류). 음성 안내는 영어입니다."),
        ("타이머", "타이머를 5개까지 저장할 수 있으며, 좌우로 밀어 전환합니다"),
        ("백그라운드", "화면을 끄거나 다른 앱을 열어도 계속 카운트합니다"),
        ("음악", "듣던 음악이나 팟캐스트를 멈추거나 음량을 낮추지 않고 그 위에 겹쳐 재생됩니다"),
        ("Apple 건강", "iPhone에서 선택 사항. 켜면 완료한 운동을 기록하며, 읽어 오는 데이터는 없습니다."),
        ("개발자", "Takahiro Torii(일본의 개인 개발자)"),
        ("첫 출시", "2016년 10월"),
    ],
    h_uses="이렇게들 씁니다",
    uses=["타바타와 HIIT",
          "근력 운동과 서킷 트레이닝(세트 사이 휴식 타이머로)",
          "버피, 플랭크, 마운틴 클라이머, 스프린트",
          "스트레칭, 가동성 운동, 코어 운동",
          "복싱 라운드, 줄넘기, 실내자전거와 스피닝"],
    uses_p="App Store에 작성된 리뷰에서 이 앱을 고른 이유로 가장 많이 꼽히는 것은 단순함입니다. 리뷰의 약 3분의 1이 그렇게 말하며, 대개 기능이 더 많은 타이머를 써 본 뒤의 이야기입니다.",
    h_not="하지 못하는 것",
    not_p="이 앱이 맞는지는 여기서 갈리므로 분명히 적어 둡니다.",
    nots=["저장할 수 있는 타이머는 5개까지입니다.",
          "맞춤 시퀀스, EMOM, AMRAP 모드는 없습니다. 모든 세트가 같은 운동 시간과 휴식 시간을 씁니다.",
          "Apple Watch 및 Wear OS 앱은 없습니다.",
          "운동 라이브러리, 코칭, 운동 프로그램은 없습니다.",
          "앱 화면의 글자와 음성 안내는 영어로만 제공됩니다."],
    not_p2="두 번만 누르면 시작되고 그 뒤로는 신경 쓸 필요 없는 타이머를 원한다면 이 앱이 맞습니다. 복잡한 운동을 짜고 싶다면 기능이 더 많은 인터벌 타이머를 찾아보세요.",
    h_q="자주 묻는 질문",
    faq=[
        ("정말 무료인가요?", "네. 모든 기능이 무료이며 구독, 앱 내 구입, 계정이 없습니다. 화면 아래의 작은 배너 광고 하나로 운영됩니다. 전면 광고나 동영상 광고는 없습니다."),
        ("화면을 꺼도 계속 동작하나요?", "네. 백그라운드에서도, 화면이 잠긴 상태에서도 카운트와 음성은 계속됩니다. iPhone(iOS 16.1 이상)에서는 잠금 화면에 남은 시간과 정지 버튼이 표시되고, Android에서는 알림에 남은 시간이 표시됩니다."),
        ("음악을 들으면서 쓸 수 있나요?", "네. 재생 중인 소리는 원래 음량 그대로 계속 나오고, 음성이 그 위에 얹힙니다."),
        ("무엇을 설정할 수 있나요?", "준비 시간, 운동 시간, 휴식 시간, 세트 수입니다. iPhone과 Android 모두 운동 시간을 최대 300초(5분), 준비와 휴식 시간을 최대 120초, 세트 수를 최대 40세트까지 설정할 수 있습니다."),
        ("타바타 운동이란 무엇인가요?", "준비 운동을 한 뒤 20초 전력 운동과 10초 휴식을 8회 반복하는 방식으로, 모두 4분입니다. 리쓰메이칸대학 다바타 이즈미 교수의 이름에서 유래했으며, 연구는 1996년에 발표되었습니다. 이 앱의 기본값이 바로 이 숫자입니다."),
        ("음성 대신 비프음으로 바꿀 수 있나요?", "네, iPhone과 Android 모두 가능합니다. 설정 화면의 ‘Sound’에서 여성 음성, 남성 음성, 세 가지 비프음 중 하나를 고를 수 있으며, 누르면 바로 들어볼 수 있습니다. 비프음은 체육관이나 음악을 틀어 놓은 곳에서 더 잘 들립니다."),
        ("타이머를 여러 개 저장할 수 있나요?", "네, iPhone과 Android 모두 5개까지 저장할 수 있습니다. 설정 화면의 ‘Timers’에서 추가한 뒤 메인 화면에서 좌우로 밀어 전환하세요."),
        ("복싱 3분 라운드에 쓸 수 있나요?", "네, iPhone과 Android 모두 가능합니다. 운동 시간은 300초(5분)까지, 휴식은 120초까지 설정할 수 있어서 3분 라운드와 1분 휴식을 그대로 설정할 수 있습니다."),
        ("앱은 어떤 데이터를 수집하나요?", "회원 가입은 없습니다. 앱은 각 운동의 완료 시각을 익명 식별자와 함께 저장하며 Firebase Analytics, Crashlytics, Google AdMob을 사용합니다. 위치, 연락처, 카메라, 마이크는 사용하지 않습니다."),
    ],
    privacy_link="자세한 내용은 <a href=\"/privacy.html\">개인정보 처리방침</a>(영어·일본어)을 참고하세요.",
    h_get="앱 받기",
    note="이름이 비슷한 앱이 여럿 있습니다. 이 앱의 개발자는 Takahiro Torii이며, App Store ID는 1166542235, Android 패키지는 <code>com.tabatatimer</code>입니다.",
    privacy="개인정보 처리방침", contact="문의", updated="최종 업데이트: 2026년 11월 28일",
    rating=("", ""), store="kr", currency="KRW",
)

L["zh-Hant"] = dict(
    name="HIIT 間歇計時器 - Tabata 健身",
    title="HIIT 間歇計時器 - Tabata 健身 — 適用於 iPhone 與 Android 的免費簡單間歇計時器",
    metadesc="HIIT 間歇計時器 - Tabata 健身（開發者：Takahiro Torii）：適用於 iPhone 與 Android 的免費間歇計時器。設定運動、休息的秒數與組數，按下開始即可。語音倒數、可在背景執行、可配著音樂使用。不必註冊，沒有訂閱。",
    ogdesc="適用於 iPhone 與 Android 的免費簡單間歇計時器。語音倒數、可在背景執行，不必註冊、沒有訂閱。",
    alt="HIIT 間歇計時器 - Tabata 健身 的 App 圖像",
    by="開發者：Takahiro Torii · iPhone、iPad 與 Android · 免費",
    summary="HIIT 間歇計時器 - Tabata 健身 是 Takahiro Torii 開發的間歇計時器 App，適用於 iPhone、iPad（iOS 15 或以上版本）與 Android（8.0 或以上版本）。App 免費，只有一則小型橫幅廣告；沒有訂閱、沒有 App 內購買，也不必註冊帳號。在 iPhone 與 Android 上，運動時間都可設定為 5 到 300 秒，準備與休息時間為 5 到 120 秒，組數為 2 到 40 組；最多可保存五個計時器，提示音可選女聲、男聲語音或三種嗶聲（尖銳、柔和、哨音）。最後更新：2026 年 11 月 28 日（依據 iPhone 版與 Android 版 1.8.2）。",
    lede="一款簡單的間歇計時器。設定運動時間、休息時間與組數，按下開始即可。語音會倒數最後五秒，並在每次切換時提示，訓練途中完全不必看螢幕。",
    p2="它只做一件事。沒有訓練課表、沒有影片、不必註冊、沒有訂閱。自 2016 年起在 App Store 上架；在其他地區名為「Tabata & HIIT Interval Timer」，在日本則名為",
    p2_end="。",
    appstore="在 App Store 下載", play="在 Google Play 下載",
    h_glance="概覽",
    rows=[
        ("價格", "免費。沒有訂閱、沒有 App 內購買，也不必註冊。"),
        ("廣告", "只有畫面底部一則小型橫幅廣告。沒有全螢幕廣告或影片廣告。"),
        ("支援平台", "iPhone 與 iPad（iOS 15 或以上版本）、Android（8.0 或以上版本）"),
        ("評分", "在台灣 App Store 獲得 {r} 分（滿分 5 分），共 {n} 則評分；在日本為 4.8 分，共 10,924 則評分（2026 年 11 月 23 日）"),
        ("設定項目", "準備時間、運動時間、休息時間、組數"),
        ("預設值", "準備 10 秒、運動 20 秒、休息 10 秒、8 組，也就是標準的 Tabata 訓練法"),
        ("聲音", "可選語音（女聲／男聲）或嗶聲（三種）；語音提示為英語。"),
        ("計時器", "最多可保存五個計時器，左右滑動即可切換"),
        ("背景執行", "關閉螢幕或開啟其他 App 時仍會繼續計時"),
        ("音樂", "會疊在你的音樂或 Podcast 上播放，不會暫停，也不會降低音量"),
        ("Apple 健康", "iPhone 可選用。開啟後會寫入已完成的訓練；不會讀取任何資料。"),
        ("開發者", "Takahiro Torii（日本的獨立開發者）"),
        ("首次發布", "2016 年 10 月"),
    ],
    h_uses="大家都拿它來做什麼",
    uses=["Tabata 與 HIIT 訓練",
          "重量訓練與循環訓練，當作組間休息計時器",
          "波比跳、棒式、登山者、衝刺",
          "伸展、活動度訓練與核心訓練",
          "拳擊回合、跳繩、健身車與飛輪"],
    uses_p="在 App Store 的文字評論中，最常被提到的選擇理由是「簡單」。大約三分之一的評論這麼說，而且多半是在試過功能更多的計時器之後。",
    h_not="它做不到的事",
    not_p="適不適合你，關鍵就在這裡，所以先說清楚。",
    nots=["最多只能保存五個計時器。",
          "沒有自訂序列，也沒有 EMOM 或 AMRAP 模式。每一組都使用相同的運動時間與休息時間。",
          "沒有 Apple Watch 或 Wear OS 版 App。",
          "沒有動作資料庫、教練指導或訓練課表。",
          "App 的介面文字與語音只有英語。"],
    not_p2="如果你想要一個點兩下就能開始、之後不必再費心的計時器，就是這一款。如果你想編排複雜的訓練，請找功能更完整的間歇計時器。",
    h_q="常見問題",
    faq=[
        ("真的免費嗎？", "是的。所有功能都免費，沒有訂閱、沒有 App 內購買，也不必註冊。App 靠畫面底部一則小型橫幅廣告維持營運，沒有全螢幕廣告或影片廣告。"),
        ("關閉螢幕後還會繼續計時嗎？", "會。在背景執行或螢幕鎖定時，倒數與語音都會繼續。在 iPhone（iOS 16.1 或以上版本）上，鎖定畫面會顯示剩餘時間與停止按鈕；在 Android 上，剩餘時間會顯示在通知中。"),
        ("可以同時聽音樂嗎？", "可以。正在播放的內容會維持原本的音量繼續播放，語音則疊在上面。"),
        ("可以調整哪些設定？", "準備時間、運動時間、休息時間與組數。在 iPhone 與 Android 上，運動時間最長 300 秒（5 分鐘），準備與休息時間最長 120 秒，一次訓練最多 40 組。"),
        ("什麼是 Tabata 訓練？", "熱身之後，以 20 秒全力運動、10 秒休息交替進行八次，總共四分鐘。這套訓練法以立命館大學田畑泉教授的名字命名，相關研究發表於 1996 年。App 的預設值正是這組數字。"),
        ("可以把語音換成嗶聲嗎？", "可以，iPhone 與 Android 都可以。在設定畫面的「Sound」中，可選擇女聲、男聲或三種嗶聲之一，點一下即可試聽。在健身房或播放音樂時，嗶聲更容易聽見。"),
        ("可以保存多個計時器嗎？", "可以，iPhone 與 Android 都最多五個。在設定畫面的「Timers」中新增後，於主畫面左右滑動即可切換。"),
        ("適合拳擊的三分鐘回合嗎？", "適合，iPhone 與 Android 都適用。運動時間最長 300 秒（5 分鐘），休息最長 120 秒，因此可以直接設定三分鐘一回合、休息一分鐘。"),
        ("App 會收集哪些資料？", "不需要註冊。App 會以匿名識別碼儲存每次訓練的完成時間，並使用 Firebase Analytics、Crashlytics 與 Google AdMob。不會使用位置、聯絡人、相機或麥克風。"),
    ],
    privacy_link="請參閱<a href=\"/privacy.html\">隱私權政策</a>（英文與日文）。",
    h_get="取得 App",
    note="有好幾款 App 的名稱很相似。這一款由 Takahiro Torii 發行；App Store ID 為 1166542235，Android 套件名稱為 <code>com.tabatatimer</code>。",
    privacy="隱私權政策", contact="聯絡", updated="最後更新：2026 年 11 月 28 日",
    rating=("4.9", "64"), store="tw", currency="TWD", play_hl="zh-TW",
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
    url = f"{BASE}{PATHS[code]}"
    r, n = t["rating"]
    ios = f"https://apps.apple.com/{t['store']}/app/id1166542235"
    play = f"https://play.google.com/store/apps/details?id=com.tabatatimer&hl={t.get('play_hl', code)}"
    rows = "\n".join(
        f"    <tr><th>{e(k)}</th><td>{e(v.format(r=r, n=n))}</td></tr>" for k, v in t["rows"])
    uses = "\n".join(f"    <li>{e(x)}</li>" for x in t["uses"])
    nots = "\n".join(f"    <li>{e(x)}</li>" for x in t["nots"])
    more = ""
    if "uses_more" in t:  # languages that have the use-case pages (build_uses.py)
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        mod = __import__("uses_" + code)
        links = "\n".join(f'    <li><a href="{PATHS[code]}{slug}/">{e(p["short"])}</a></li>' for slug, p in mod.PAGES.items())
        more = f"  <p>{e(t['uses_more'])}</p>\n  <ul>\n{links}\n  </ul>\n"
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
        "operatingSystem": "iOS 15.0 or later, Android 8.0 or later",
        "url": url, "image": f"{BASE}/icon.png",
        "datePublished": "2016-10-20", "softwareVersion": "1.8.2",
        "author": {"@type": "Person", "name": "Takahiro Torii",
                   "url": "https://ttorii20.github.io/", "email": "support@simpletabata.com"},
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": t.get("currency", "EUR")},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8",
                            "bestRating": "5", "ratingCount": "10924"},
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

  <p>{e(t['summary'])}</p>

  <p class="lede">{e(t['lede'])}</p>

  <p>{e(t['p2'])} <span lang="ja">HIIT &amp; Tabata Timer - タバタタイマー</span>{e(t.get('p2_end', '.'))}</p>

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
{more}  <p>{e(t['uses_p'])}</p>

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
    d = SITE / PATHS[code].strip("/")
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page(code, t), encoding="utf-8")

# Patch the two hand-written pages: hreflang block and language links.
for rel in ("index.html", "ja/index.html"):
    f = SITE / rel
    s = f.read_text(encoding="utf-8")
    s = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]+">\n)+', HREFLANG + "\n", s, count=1)
    s = re.sub(r'<p class="lang">.*?</p>', NAV, s, count=1, flags=re.S)
    f.write_text(s, encoding="utf-8")

USE_SLUGS = ("boxing-round-timer", "team-practice-timer", "offline-interval-timer", "interval-timer-with-beeps", "free-interval-timer-no-subscription", "interval-timer-with-music", "tabata-timer-for-android", "simple-interval-timer", "tabata-timer-apps-compared")
urls = [(p, "2026-11-28") for _, _, p in ALL] + [("/timer/", "2026-11-24"), ("/timer/ja/", "2026-11-24")] + [(pre + slug + "/", "2026-11-28") for slug in USE_SLUGS for pre in ("/", "/ja/", "/fr/", "/de/", "/it/", "/es/")] + [("/privacy.html", "2026-11-23")]
(SITE / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{BASE}{p}</loc><lastmod>{d}</lastmod></url>\n" for p, d in urls)
    + "</urlset>\n", encoding="utf-8")
print("built", ", ".join(L))
