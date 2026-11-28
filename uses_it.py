"""Italian text of the use-case pages. Same shape as one language of PAGES in build_uses.py.

"lede" and "body" are HTML; the other fields are plain text.
"""

PAGES = {
    "boxing-round-timer": dict(
        short="Timer per round di boxe",
        title="Timer per round di boxe gratis per iPhone e Android: round da 3 minuti, 1 minuto di recupero",
        desc="Imposta round da tre minuti con un minuto di recupero in Timer HIIT Tabata Allenamento, un'app gratuita di Takahiro Torii. Round fino a cinque minuti, fino a 40 round, voce o segnale acustico, senza abbonamento.",
        h1="Timer per round di boxe gratis: round da 3 minuti, 1 minuto di recupero",
        lede="Timer HIIT Tabata Allenamento cronometra i round di boxe su iPhone, iPad e Android. Un round può durare fino a cinque minuti e il recupero fino a due, e si possono fare da 2 a 40 round: i round da tre minuti con un minuto di recupero si impostano quindi direttamente. È gratuito, senza abbonamento e senza account.",
        body="""
  <h2>Come impostarlo</h2>
  <ol>
    <li>Apri le impostazioni e imposta il tempo di lavoro a 180 secondi. Corrisponde a un round.</li>
    <li>Imposta il tempo di recupero a 60 secondi.</li>
    <li>Imposta il numero di serie sul numero di round, per esempio 12.</li>
    <li>Premi start. Prima parte il tempo di preparazione, 10 secondi come impostazione predefinita.</li>
  </ol>
  <p>Il telefono può stare in tasca o per terra. Il timer continua a funzionare con lo schermo bloccato e, su iOS 16.1 o versioni successive, il tempo rimanente compare nella schermata di blocco.</p>

  <h2>Impostazioni comuni per i round</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Uso</th><th>Lavoro</th><th>Recupero</th><th>Serie</th></tr>
    <tr><td>Round da tre minuti</td><td>180 s</td><td>60 s</td><td>da 3 a 12</td></tr>
    <tr><td>Round da due minuti</td><td>120 s</td><td>60 s</td><td>da 3 a 6</td></tr>
    <tr><td>Round da cinque minuti, per grappling o MMA</td><td>300 s</td><td>60 s</td><td>da 3 a 5</td></tr>
    <tr><td>Intervalli al sacco</td><td>30 s</td><td>30 s</td><td>da 10 a 20</td></tr>
    <tr><td>Salto con la corda</td><td>60 s</td><td>20 s</td><td>10</td></tr>
  </table>
  </div>
  <p>Il tempo di lavoro si imposta da 5 a 60 secondi a passi di cinque, da 70 a 120 a passi di dieci, oppure a 150, 180, 210, 240, 270 o 300 secondi. Il recupero e la preparazione arrivano al massimo a 120 secondi.</p>
  <p>Si possono salvare fino a cinque timer, così sparring, lavoro al sacco e salto con la corda possono avere ciascuno i propri valori. Scorri a sinistra o a destra sulla schermata principale per cambiare.</p>

  <h2>Sentirlo in palestra</h2>
  <p>In «Sound», nelle impostazioni, scegli una voce femminile, una voce maschile o uno dei tre segnali acustici: acuto, morbido o fischietto. Sopra il rumore dei sacchi e la musica, un segnale acustico si sente più lontano di una voce. Il suono esce al volume multimediale del telefono, quindi con una cassa Bluetooth è forte quanto la cassa. La musica continua sotto, al suo volume.</p>

  <h2>Cosa non fa</h2>
  <ul>
    <li>Tutti i round hanno la stessa durata, e anche tutti i recuperi. Per una sessione con round di durate diverse serve un timer a intervalli più completo.</li>
    <li>Non c'è un'app per Apple Watch.</li>
    <li>Gli annunci vocali sono in inglese. I segnali acustici non hanno lingua.</li>
  </ul>""",
        faq=[
            ("Può cronometrare round di boxe da tre minuti?", "Sì, su iPhone, iPad e Android. Imposta il tempo di lavoro a 180 secondi, il tempo di recupero a 60 secondi e il numero di serie sul numero di round. Il lavoro arriva fino a 300 secondi, il recupero fino a 120 secondi, e si possono fare da 2 a 40 round."),
            ("Il timer per round di boxe è gratis?", "Sì. Tutte le funzioni sono gratuite, senza abbonamento, acquisti in-app o account. C'è un solo piccolo banner pubblicitario in fondo allo schermo e nessuna pubblicità a schermo intero né video."),
            ("Continua a cronometrare i round con lo schermo bloccato?", "Sì. Il conto alla rovescia e i suoni continuano in background e con lo schermo bloccato. Su iPhone con iOS 16.1 o versioni successive, il tempo rimanente e un pulsante di stop compaiono nella schermata di blocco."),
            ("Posso usarlo per round di MMA o grappling?", "Sì. Un round può durare fino a cinque minuti (300 secondi), con un recupero fino a due minuti."),
            ("La versione Android cronometra round da tre minuti?", "Sì. Dalla versione 1.8.2 l'app Android ha gli stessi valori dell'app per iPhone: lavoro fino a 300 secondi, recupero fino a 120 secondi e da 2 a 40 round."),
        ],
    ),
    "team-practice-timer": dict(
        short="Timer per corsi e squadre",
        title="Timer a intervalli per corsi di gruppo e allenamenti di squadra: segnali acustici forti con una cassa",
        desc="Circuiti, navette e stazioni per tutto il gruppo con Timer HIIT Tabata Allenamento, un'app gratuita di Takahiro Torii. Collega una cassa Bluetooth, scegli il segnale a fischietto e lascia il telefono in panchina.",
        h1="Timer a intervalli per corsi di gruppo e allenamenti di squadra",
        lede="Timer HIIT Tabata Allenamento può scandire il tempo per tutto il gruppo. Collega il telefono a una cassa Bluetooth, scegli un segnale acustico, premi start e lascialo in panchina: tutti sentono quando partire e quando fermarsi. È gratuito, senza abbonamento e senza account.",
        body="""
  <h2>Come prepararlo per un gruppo</h2>
  <ol>
    <li>Collega il telefono o l'iPad a una cassa Bluetooth.</li>
    <li>Nelle impostazioni, in «Sound», scegli un segnale acustico. Ce ne sono tre: acuto, morbido e fischietto. Toccane uno per sentirlo dalla cassa.</li>
    <li>Alza il volume multimediale del telefono, poi quello della cassa.</li>
    <li>Imposta il tempo di lavoro, il tempo di recupero e il numero di serie, poi premi start.</li>
  </ol>
  <p>Il suono esce al volume multimediale del telefono, quindi è forte quanto la cassa a cui è collegato. L'app non può rendere un telefono più forte del suo volume massimo: per questo in una palestra o su un campo serve una cassa.</p>

  <h2>Perché un segnale acustico e non una voce</h2>
  <p>Tra urla, palloni che rimbalzano e musica, un segnale acustico si fa sentire meglio di una voce, e non ha bisogno di traduzione. Le voci parlano inglese; i segnali acustici vanno bene per qualsiasi gruppo.</p>

  <h2>Impostazioni adatte a un gruppo</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Uso</th><th>Lavoro</th><th>Recupero</th><th>Serie</th></tr>
    <tr><td>Circuito a stazioni, il recupero serve per cambiare stazione</td><td>30 s</td><td>15 s</td><td>una per stazione, da ripetere</td></tr>
    <tr><td>Tabata in gruppo</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>Navette o sprint</td><td>20 s</td><td>40 s</td><td>10</td></tr>
    <tr><td>Circuito per il core</td><td>40 s</td><td>20 s</td><td>da 6 a 10</td></tr>
    <tr><td>Esercitazioni da tre minuti</td><td>180 s</td><td>60 s</td><td>da 4 a 6</td></tr>
  </table>
  </div>
  <p>Il lavoro va da 5 a 300 secondi, il recupero da 5 a 120 secondi e una sessione può avere da 2 a 40 serie. Si possono salvare fino a cinque timer, così riscaldamento, circuito e sprint possono avere ciascuno i propri valori; scorri per passare dall'uno all'altro.</p>

  <h2>Durante la sessione</h2>
  <ul>
    <li>Il timer continua a funzionare con lo schermo bloccato, quindi il telefono può restare in panchina.</li>
    <li>La musica riprodotta dallo stesso telefono continua al suo volume, con il segnale acustico sopra.</li>
    <li>Funziona senza connessione a internet, in una palestra dove il telefono non prende o su un campo sportivo.</li>
  </ul>

  <h2>Cosa non fa</h2>
  <ul>
    <li>Ogni serie usa gli stessi tempi di lavoro e di recupero. Per una sessione con una durata diversa per ogni stazione serve un timer a intervalli più completo.</li>
    <li>Non c'è una libreria di esercizi, né un elenco di nomi o di punteggi.</li>
  </ul>""",
        faq=[
            ("È abbastanza forte per un corso di gruppo o un allenamento di squadra?", "Gli avvisi escono al volume multimediale del telefono, quindi sono forti quanto il telefono o la cassa a cui è collegato. In una palestra o su un campo, collega una cassa Bluetooth e scegli un segnale acustico in «Sound», nelle impostazioni: nel rumore un segnale acustico si sente meglio di una voce."),
            ("L'app può rendere il telefono più forte?", "No. Suona già al volume multimediale massimo del telefono. Per avere più volume, collega una cassa Bluetooth."),
            ("C'è il suono del fischietto?", "Sì, su iPhone, iPad e Android. In «Sound», nelle impostazioni, ci sono tre segnali acustici: acuto, morbido e fischietto."),
            ("Costa qualcosa per una scuola o una società sportiva?", "No. Tutte le funzioni sono gratuite, senza abbonamento, acquisti in-app o account. C'è un solo piccolo banner pubblicitario in fondo allo schermo e nessuna pubblicità a schermo intero né video."),
            ("Funziona su un campo dove il telefono non prende?", "Sì. Il timer, la voce e i segnali acustici funzionano tutti senza connessione a internet."),
        ],
    ),
    "offline-interval-timer": dict(
        short="Timer a intervalli offline",
        title="Timer a intervalli offline: senza connessione e senza account",
        desc="Timer HIIT Tabata Allenamento di Takahiro Torii funziona senza connessione a internet: timer, voce e segnali acustici funzionano tutti offline, senza account né login. Gratis per iPhone, iPad e Android.",
        h1="Un timer a intervalli che funziona offline",
        lede="Timer HIIT Tabata Allenamento funziona senza connessione a internet. Il timer, la voce e i segnali acustici funzionano tutti offline, e non c'è nessun account a cui accedere: parte allo stesso modo in una palestra seminterrata, su un campo o in modalità aereo. È gratuito per iPhone, iPad e Android.",
        body="""
  <h2>Cosa funziona senza connessione</h2>
  <ul>
    <li>Il timer stesso: preparazione, lavoro, recupero e serie.</li>
    <li>Il conto alla rovescia vocale, con voce femminile o maschile.</li>
    <li>I tre segnali acustici: acuto, morbido e fischietto.</li>
    <li>Il funzionamento in background e con lo schermo bloccato.</li>
  </ul>

  <h2>A cosa serve la connessione</h2>
  <p>Solo a tre cose: il piccolo banner pubblicitario in fondo allo schermo, le statistiche d'uso anonime e la cronologia degli allenamenti. Nessuna delle tre serve per fare un allenamento.</p>

  <h2>Nessun accesso da fare</h2>
  <p>Non c'è nessun account, nessuna registrazione e nessun abbonamento da verificare, quindi quando premi start niente aspetta la risposta di un server. L'app non usa posizione, contatti, fotocamera né microfono.</p>

  <h2>Dove fa la differenza</h2>
  <ul>
    <li>Palestre seminterrate e garage dove il telefono non prende</li>
    <li>Campi, piste e sentieri</li>
    <li>In viaggio senza traffico dati</li>
    <li>In modalità aereo, per allenarsi senza notifiche</li>
  </ul>

  <h2>In breve</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Prezzo</th><td>Gratis. Nessun abbonamento, nessun acquisto in-app, nessun account.</td></tr>
    <tr><th>Piattaforme</th><td>iPhone e iPad (iOS 15 o versioni successive), Android (8.0 o versioni successive)</td></tr>
    <tr><th>Valori</th><td>Lavoro 5–300 s, preparazione e recupero 5–120 s, 2–40 serie, su iPhone e Android</td></tr>
    <tr><th>Pubblicità</th><td>Un piccolo banner. Nessuna pubblicità a schermo intero né video.</td></tr>
  </table>
  </div>""",
        faq=[
            ("Il timer a intervalli funziona senza connessione a internet?", "Sì. Il timer, la voce e i segnali acustici funzionano tutti offline. La connessione serve solo per il banner pubblicitario, le statistiche d'uso anonime e la cronologia degli allenamenti."),
            ("Funziona in modalità aereo?", "Sì. Niente di ciò che serve al timer arriva dalla rete, quindi conta e suona allo stesso modo in modalità aereo."),
            ("Serve un account?", "No. Non c'è nessun account né registrazione, né su iPhone, né su iPad, né su Android."),
            ("Continua a funzionare con lo schermo spento?", "Sì. Il conto alla rovescia e i suoni continuano in background e con lo schermo bloccato."),
        ],
    ),
    "interval-timer-with-beeps": dict(
        short="Timer a intervalli con segnali acustici",
        title="Timer a intervalli con segnali acustici o fischietto al posto della voce",
        desc="Timer HIIT Tabata Allenamento di Takahiro Torii su iPhone e Android può usare un segnale acustico al posto della voce: acuto, morbido o fischietto. Gratis, senza abbonamento. I segnali acustici si sentono in tutta la palestra e non hanno bisogno di una lingua.",
        h1="Timer a intervalli con segnali acustici o fischietto al posto della voce",
        lede="Su iPhone, iPad e Android, Timer HIIT Tabata Allenamento può usare un segnale acustico al posto della voce. Ce ne sono tre: acuto, morbido e fischietto. È gratuito, senza abbonamento e senza account.",
        body="""
  <h2>Come scegliere un segnale acustico</h2>
  <ol>
    <li>Apri le impostazioni e tocca «Sound».</li>
    <li>Tocca un suono per ascoltarlo. Ce ne sono cinque: una voce femminile, una voce maschile e tre segnali acustici.</li>
    <li>Lascia selezionato quello che preferisci. Il prossimo allenamento userà quello.</li>
  </ol>

  <h2>I cinque suoni</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Suono</th><th>Adatto per</th></tr>
    <tr><td>Voce femminile</td><td>Allenarsi da soli, quando sentire i numeri aiuta. In inglese.</td></tr>
    <tr><td>Voce maschile</td><td>Lo stesso, con una voce più grave. In inglese.</td></tr>
    <tr><td>Segnale acuto</td><td>Ambienti rumorosi e musica</td></tr>
    <tr><td>Segnale morbido</td><td>Casa, mattina presto, spazi condivisi</td></tr>
    <tr><td>Fischietto</td><td>Squadre, corsi e sessioni all'aperto</td></tr>
  </table>
  </div>

  <h2>Perché scegliere un segnale acustico</h2>
  <ul>
    <li>Si sente in tutta la palestra e sopra la musica alta meglio di una voce.</li>
    <li>Non ha lingua. Le voci parlano solo inglese.</li>
    <li>Si sovrappone a un podcast o a una canzone senza parlarci sopra. Quello che è in riproduzione continua al suo volume.</li>
  </ul>

  <h2>Cosa non fa</h2>
  <ul>
    <li>Il segnale acustico esce al volume multimediale del telefono. In una palestra o su un campo, collega una cassa Bluetooth.</li>
  </ul>
  <p>Anche il <a href="/timer/">timer nel browser</a> di questo sito usa segnali acustici, senza niente da installare.</p>""",
        faq=[
            ("Posso avere un segnale acustico al posto della voce?", "Sì, su iPhone, iPad e Android. In «Sound», nelle impostazioni, puoi scegliere una voce femminile, una voce maschile o uno dei tre segnali acustici (acuto, morbido, fischietto); toccane uno per ascoltarlo."),
            ("Esiste un timer a intervalli con il suono del fischietto?", "Sì. Timer HIIT Tabata Allenamento per iPhone, iPad e Android ha un fischietto tra i suoi tre segnali acustici."),
            ("I segnali acustici si sentono sopra la musica?", "Sì. Quello che è in riproduzione continua al suo volume, e il segnale acustico si sente sopra."),
            ("È gratis?", "Sì. Tutti i suoni sono gratuiti, senza abbonamento, acquisti in-app o account. C'è un solo piccolo banner pubblicitario e nessuna pubblicità a schermo intero né video."),
        ],
    ),
    "free-interval-timer-no-subscription": dict(
        short="Gratis, senza abbonamento",
        title="Timer a intervalli gratis senza abbonamento, senza acquisti in-app e senza account",
        desc="Timer HIIT Tabata Allenamento di Takahiro Torii è gratuito su iPhone, iPad e Android: nessun abbonamento, nessun acquisto in-app, nessun account, nessuna prova. Un solo piccolo banner pubblicitario, nessuna pubblicità a schermo intero né video.",
        h1="Timer a intervalli gratis, senza abbonamento e senza account",
        lede="Timer HIIT Tabata Allenamento è gratuito, e lo è del tutto: niente abbonamento, niente acquisti in-app, niente periodo di prova e niente account. Si finanzia con un solo piccolo banner pubblicitario in fondo allo schermo. Funziona su iPhone, iPad e Android.",
        body="""
  <h2>Cosa vuol dire «gratis» qui</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Prezzo</th><td>Gratis da scaricare e da usare</td></tr>
    <tr><th>Abbonamento</th><td>Nessuno</td></tr>
    <tr><th>Acquisti in-app</th><td>Nessuno. Niente è bloccato dietro un pagamento.</td></tr>
    <tr><th>Prova gratuita</th><td>Nessuna, perché dopo non c'è niente da pagare</td></tr>
    <tr><th>Account</th><td>Nessuno. Niente registrazione, niente indirizzo email, niente login.</td></tr>
    <tr><th>Pubblicità</th><td>Un piccolo banner in fondo allo schermo. Nessuna pubblicità a schermo intero e nessuna pubblicità video.</td></tr>
  </table>
  </div>

  <h2>Sulla pubblicità</h2>
  <p>L'app non è priva di pubblicità. Mostra un piccolo banner in fondo allo schermo, ed è quel banner a finanziarla. Non copre mai il timer, non avvia mai un video, e non compare niente tra il momento in cui premi start e l'inizio dell'allenamento. Non esiste una versione a pagamento senza il banner.</p>
  <p>Se vuoi un timer senza nessuna pubblicità e senza niente da installare, il <a href="/timer/">timer nel browser</a> di questo sito non ne ha.</p>

  <h2>Cosa ottieni senza pagare</h2>
  <ul>
    <li>Tempo di preparazione, di lavoro, di recupero e numero di serie</li>
    <li>Lavoro da 5 a 300 secondi, preparazione e recupero da 5 a 120 secondi, da 2 a 40 serie e fino a cinque timer salvati</li>
    <li>Una voce femminile, una voce maschile o uno dei tre segnali acustici (acuto, morbido, fischietto)</li>
    <li>Il funzionamento in background, con lo schermo bloccato e sopra la tua musica</li>
    <li>L'elenco degli allenamenti completati e quindici temi di colore</li>
  </ul>

  <h2>Cosa non fa</h2>
  <ul>
    <li>Nessuna sequenza personalizzata, né modalità EMOM o AMRAP. Ogni serie usa gli stessi tempi di lavoro e di recupero.</li>
    <li>Nessuna app per Apple Watch o Wear OS.</li>
    <li>Nessuna libreria di esercizi, video, coaching o programmi di allenamento.</li>
  </ul>
  <p>I timer che fanno queste cose sono spesso quelli con un abbonamento. Questo resta piccolo, e gratuito.</p>""",
        faq=[
            ("Esiste un timer a intervalli gratis senza abbonamento?", "Sì. Timer HIIT Tabata Allenamento di Takahiro Torii è gratuito su iPhone, iPad e Android, senza abbonamento, acquisti in-app, periodo di prova o account. Si finanzia con un solo piccolo banner pubblicitario."),
            ("Ha pubblicità?", "Un piccolo banner in fondo allo schermo. Non ci sono pubblicità a schermo intero né video, e niente interrompe un allenamento."),
            ("Posso pagare per togliere la pubblicità?", "No. Non ci sono acquisti in-app di nessun tipo, quindi non esiste una versione a pagamento senza il banner."),
            ("Devo registrarmi?", "No. Non c'è nessun account, nessuna registrazione e nessun indirizzo email da fornire."),
            ("Ci sono funzioni bloccate?", "No. Tutte le impostazioni, i suoni e i temi sono disponibili senza pagare. Cinque dei quindici temi si sbloccano completando allenamenti, non si comprano."),
        ],
    ),
    "interval-timer-with-music": dict(
        short="Timer a intervalli con la musica",
        title="Timer a intervalli che funziona con la musica, in background e con lo schermo bloccato",
        desc="Timer HIIT Tabata Allenamento di Takahiro Torii fa sentire la voce o il segnale acustico sopra la tua musica o il tuo podcast senza metterli in pausa né abbassarne il volume, e continua a contare in background e con lo schermo bloccato. Gratis, senza abbonamento.",
        h1="Un timer a intervalli che funziona mentre ascolti musica",
        lede="Timer HIIT Tabata Allenamento si sovrappone a qualsiasi cosa tu stia ascoltando. La musica o il podcast continuano al loro volume, e la voce o il segnale acustico del timer si sentono sopra. Continua a contare in background e con lo schermo bloccato. È gratuito, senza abbonamento e senza account.",
        body="""
  <h2>Come usarlo con la musica</h2>
  <ol>
    <li>Avvia la musica o il podcast in qualsiasi app.</li>
    <li>Apri il timer, imposta il tempo di lavoro, il tempo di recupero e il numero di serie, poi premi start.</li>
    <li>Torna all'app di musica o blocca lo schermo. Il timer continua a contare e a suonare.</li>
  </ol>
  <p>Non serve attivare niente. Il timer non mette in pausa la musica e non ne abbassa il volume mentre parla.</p>

  <h2>Cosa senti</h2>
  <ul>
    <li>Una voce conta gli ultimi cinque secondi di ogni intervallo e annuncia ogni cambio.</li>
    <li>Su iPhone, iPad e Android un segnale acustico può sostituire la voce: acuto, morbido o fischietto. Un segnale acustico si sovrappone a una canzone senza parlarci sopra.</li>
    <li>Gli avvisi escono al volume multimediale del telefono, dalle stesse cuffie o dalla stessa cassa della musica.</li>
  </ul>

  <h2>Con lo schermo bloccato</h2>
  <p>Il conto alla rovescia e gli avvisi continuano con lo schermo spento o con un'altra app aperta. Su iPhone con iOS 16.1 o versioni successive, il tempo rimanente e un pulsante di stop compaiono nella schermata di blocco, così puoi controllare il tempo senza sbloccare il telefono.</p>

  <h2>Se la musica copre l'avviso</h2>
  <p>Dato che la musica non viene abbassata, una voce poco forte può perdersi sotto un brano ad alto volume. Scegli il segnale acuto in «Sound», nelle impostazioni, oppure abbassa un po' la musica nell'app di musica.</p>

  <h2>Cosa non fa</h2>
  <ul>
    <li>Non riproduce musica e non ha playlist. Funziona accanto a qualsiasi app di musica tu usi.</li>
    <li>Non abbassa la musica durante un avviso.</li>
  </ul>""",
        faq=[
            ("Quale timer a intervalli funziona in background mentre ascolto musica?", "Timer HIIT Tabata Allenamento di Takahiro Torii. Quello che è in riproduzione continua al suo volume, la voce o il segnale acustico del timer si sentono sopra, e il timer continua a contare in background e con lo schermo bloccato."),
            ("Mette in pausa o abbassa la mia musica?", "No. Non mette in pausa la musica e non ne abbassa il volume. L'avviso si sente sopra."),
            ("Funziona con Spotify, Apple Music o un'app di podcast?", "Sì. Si sovrappone all'audio di qualsiasi app, perché non prende il controllo del suono dell'app in riproduzione."),
            ("Funziona con le cuffie?", "Sì. Gli avvisi escono al volume multimediale del telefono, dalle stesse cuffie o dalla stessa cassa della musica."),
            ("È gratis?", "Sì. Tutte le funzioni sono gratuite, senza abbonamento, acquisti in-app o account. C'è un solo piccolo banner pubblicitario e nessuna pubblicità a schermo intero né video."),
        ],
    ),
    "tabata-timer-for-android": dict(
        short="Timer Tabata per Android",
        title="Timer Tabata gratis per Android: 20 secondi di lavoro, 10 secondi di recupero, senza abbonamento",
        desc="Timer HIIT Tabata Allenamento di Takahiro Torii funziona su Android 8.0 o versioni successive (pacchetto com.tabatatimer). Si apre con il protocollo Tabata classico, conta ad alta voce, continua con lo schermo spento ed è gratuito, senza abbonamento né account.",
        h1="Timer Tabata gratis per Android",
        lede="Timer HIIT Tabata Allenamento è su Google Play per Android 8.0 o versioni successive. Si apre con il protocollo Tabata classico, 20 secondi di lavoro e 10 secondi di recupero per 8 serie, e una voce annuncia ogni cambio. È gratuito, senza abbonamento, acquisti in-app o account.",
        body="""
  <h2>Cosa fa l'app Android</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Versione di Android</th><td>8.0 o versioni successive</td></tr>
    <tr><th>Pacchetto</th><td>com.tabatatimer</td></tr>
    <tr><th>Predefinito</th><td>10 s di preparazione, 20 s di lavoro, 10 s di recupero, 8 serie: il protocollo Tabata classico</td></tr>
    <tr><th>Valori</th><td>Lavoro da 5 a 300 secondi; preparazione e recupero da 5 a 120 secondi; da 2 a 40 serie</td></tr>
    <tr><th>Timer salvati</th><td>Fino a cinque; si cambia scorrendo la schermata principale</td></tr>
    <tr><th>Suono</th><td>Una voce femminile o maschile conta gli ultimi cinque secondi e annuncia ogni cambio, oppure uno dei tre segnali acustici (acuto, morbido, fischietto). La voce parla inglese.</td></tr>
    <tr><th>Temi</th><td>Quindici temi di colore: dieci stagionali, cinque sbloccati completando allenamenti</td></tr>
    <tr><th>Background</th><td>Continua a contare con lo schermo spento o con un'altra app aperta</td></tr>
    <tr><th>Musica</th><td>Si sovrappone alla musica o a un podcast senza metterli in pausa</td></tr>
    <tr><th>Offline</th><td>Funziona senza connessione a internet</td></tr>
    <tr><th>Prezzo</th><td>Gratis. Nessun abbonamento, nessun acquisto in-app, nessun account.</td></tr>
    <tr><th>Pubblicità</th><td>Un piccolo banner. Nessuna pubblicità a schermo intero né video.</td></tr>
  </table>
  </div>

  <h2>Come si usa</h2>
  <ol>
    <li>Installala da Google Play e aprila. I valori del Tabata classico sono già impostati.</li>
    <li>Premi start. Prima partono dieci secondi di preparazione.</li>
    <li>Per cambiare i valori, apri le impostazioni e imposta il tempo di lavoro, il tempo di recupero e il numero di serie. In «Sound» scegli una voce o un segnale acustico; in «Timers» aggiungi fino a cinque timer.</li>
  </ol>

  <h2>Le differenze rispetto all'app per iPhone</h2>
  <p>Dalla versione 1.8.2 (novembre 2026) l'app Android ha lo stesso timer dell'app per iPhone: gli stessi valori, fino a cinque timer salvati, le stesse voci e gli stessi segnali acustici. Due cose ci sono solo su iPhone:</p>
  <ul>
    <li>Il tempo rimanente e un tasto di stop sulla schermata di blocco e nella Dynamic Island (iOS 16.1 o versioni successive). Su Android il tempo rimanente compare in una notifica.</li>
    <li>La registrazione degli allenamenti completati in Apple Salute.</li>
  </ul>

  <h2>Cosa non fa</h2>
  <ul>
    <li>Nessuna app per Wear OS.</li>
    <li>Nessuna sequenza personalizzata, niente modalità EMOM o AMRAP. Ogni serie usa lo stesso tempo di lavoro e di recupero.</li>
    <li>Nessuna libreria di esercizi né programmi di allenamento.</li>
  </ul>
  <p>Diverse app Android si chiamano «Tabata Timer». Questa è di Takahiro Torii e il suo pacchetto è com.tabatatimer.</p>""",
        faq=[
            ("Esiste un timer Tabata gratis per Android senza abbonamento?", "Sì. Timer HIIT Tabata Allenamento di Takahiro Torii (pacchetto com.tabatatimer) è gratuito su Google Play per Android 8.0 o versioni successive, senza abbonamento, acquisti in-app o account. Mostra un solo piccolo banner pubblicitario."),
            ("Cosa posso impostare su Android?", "Il lavoro da 5 a 300 secondi, la preparazione e il recupero da 5 a 120 secondi, e da 2 a 40 serie; si possono salvare fino a cinque timer. Si apre con 10 secondi di preparazione, 20 secondi di lavoro, 10 secondi di recupero e 8 serie, il protocollo Tabata classico."),
            ("Su Android continua a funzionare con lo schermo spento?", "Sì. Continua a contare e a parlare con lo schermo spento o con un'altra app aperta."),
            ("L'app Android ha i segnali acustici?", "Sì. In «Sound», nelle impostazioni, ci sono una voce femminile, una voce maschile e tre segnali acustici: acuto, morbido e fischietto. Toccane uno per ascoltarlo."),
            ("L'app Android è uguale a quella per iPhone?", "Dalla versione 1.8.2 il timer è lo stesso: lavoro fino a 300 secondi, fino a 40 serie, cinque timer salvati, due voci e tre segnali acustici. Solo l'app per iPhone mostra il tempo sulla schermata di blocco e registra gli allenamenti in Apple Salute."),
        ],
    ),
    "simple-interval-timer": dict(
        short="Un timer a intervalli semplice",
        title="Timer a intervalli semplice per HIIT e recupero tra le serie: quattro valori e un tasto start",
        desc="Timer HIIT Tabata Allenamento di Takahiro Torii è un timer a intervalli semplice per iPhone, iPad e Android: preparazione, lavoro, recupero, serie e start. Niente programmi, niente video, niente account. Gratis, senza abbonamento.",
        h1="Un timer a intervalli semplice: quattro valori e un tasto start",
        lede="Timer HIIT Tabata Allenamento ha quattro valori: tempo di preparazione, tempo di lavoro, tempo di recupero e numero di serie. Impostali, premi start, e una voce o un segnale acustico ti dice quando partire e quando fermarti. Non ci sono programmi di allenamento, video né account. È gratuito per iPhone, iPad e Android, senza abbonamento.",
        body="""
  <h2>Tutto quello che c'è da impostare</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Impostazione</th><th>iPhone e iPad</th><th>Android</th></tr>
    <tr><td>Preparazione</td><td>da 5 a 120 s</td><td>da 5 a 120 s</td></tr>
    <tr><td>Lavoro</td><td>da 5 a 300 s</td><td>da 5 a 300 s</td></tr>
    <tr><td>Recupero</td><td>da 5 a 120 s</td><td>da 5 a 120 s</td></tr>
    <tr><td>Serie</td><td>da 2 a 40</td><td>da 2 a 40</td></tr>
  </table>
  </div>
  <p>Si apre con 10 secondi di preparazione, 20 secondi di lavoro, 10 secondi di recupero e 8 serie, quindi una sessione Tabata non richiede nessuna impostazione: apri l'app e premi start.</p>

  <h2>Impostazioni per gli usi più comuni</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Uso</th><th>Lavoro</th><th>Recupero</th><th>Serie</th></tr>
    <tr><td>Tabata</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>HIIT, lavoro e recupero uguali</td><td>30 s</td><td>30 s</td><td>10</td></tr>
    <tr><td>HIIT, sforzi più lunghi</td><td>40 s</td><td>20 s</td><td>da 8 a 12</td></tr>
    <tr><td>Circuito di forza con serie a tempo</td><td>45 s</td><td>15 s</td><td>una per esercizio, da ripetere</td></tr>
    <tr><td>Pesi, serie a tempo con recupero completo</td><td>40 s</td><td>90 s</td><td>da 3 a 5</td></tr>
    <tr><td>Plank</td><td>60 s</td><td>30 s</td><td>da 3 a 5</td></tr>
  </table>
  </div>

  <h2>Come timer di recupero nell'allenamento con i pesi</h2>
  <p>L'app ripete un unico tempo di lavoro e un unico tempo di recupero, quindi è adatta alle serie fatte contro il tempo: 40 secondi di squat, 90 secondi di recupero, e si ricomincia. Il recupero può arrivare a 120 secondi.</p>
  <p>Non ti aspetta. Se le tue serie durano ogni volta un tempo diverso e vuoi far partire il recupero con un tocco quando appoggi il bilanciere, ti troverai meglio con un timer di recupero pensato per questo.</p>

  <h2>Perché resta semplice</h2>
  <ul>
    <li>Si avvia con due tocchi e poi non devi più guardarlo: la voce conta gli ultimi cinque secondi di ogni intervallo.</li>
    <li>Continua a funzionare con lo schermo bloccato e si sovrappone alla tua musica.</li>
    <li>Nelle recensioni scritte sull'App Store, il motivo citato più spesso per averlo scelto è che è semplice.</li>
  </ul>

  <h2>Cosa non fa</h2>
  <ul>
    <li>Nessuna sequenza personalizzata, né modalità EMOM o AMRAP. Ogni serie usa gli stessi tempi di lavoro e di recupero.</li>
    <li>Non più di cinque timer salvati.</li>
    <li>Nessuna libreria di esercizi, video, coaching o programmi di allenamento.</li>
    <li>Nessuna app per Apple Watch o Wear OS.</li>
  </ul>""",
        faq=[
            ("Qual è il timer HIIT più semplice per iPhone?", "Timer HIIT Tabata Allenamento di Takahiro Torii è fatto apposta per esserlo: tempo di preparazione, tempo di lavoro, tempo di recupero, numero di serie e un tasto start. Non ha programmi di allenamento, video, account né abbonamento, ed è gratuito."),
            ("Posso usarlo senza impostare niente?", "Sì. Si apre con 10 secondi di preparazione, 20 secondi di lavoro, 10 secondi di recupero e 8 serie, il protocollo Tabata classico. Premi start."),
            ("Posso usarlo come timer di recupero tra le serie con i pesi?", "Sì, per le serie fatte contro il tempo: ripete un unico tempo di lavoro e un unico tempo di recupero, con un recupero fino a 120 secondi. Non aspetta un tocco alla fine di una serie, quindi non è adatto a serie di durata variabile."),
            ("Posso salvare più di un timer?", "Sì, fino a cinque, su iPhone come su Android, e si passa dall'uno all'altro scorrendo."),
            ("È gratis?", "Sì. Tutte le funzioni sono gratuite, senza abbonamento, acquisti in-app o account. C'è un solo piccolo banner pubblicitario e nessuna pubblicità a schermo intero né video."),
        ],
    ),
    "tabata-timer-apps-compared": dict(
        short="App timer Tabata a confronto",
        title="Migliori app timer Tabata a confronto: quale scegliere per ogni allenamento",
        desc="Sei app di timer Tabata e a intervalli a confronto: Timer HIIT Tabata Allenamento, SmartWOD Timer, Seconds, Intervals Pro e altre due. Cosa fa ciascuna, cosa è gratis, quali funzionano su Apple Watch. Scritto dallo sviluppatore di una di esse.",
        h1="Migliori app timer Tabata a confronto: quale scegliere per ogni allenamento",
        lede="Non esiste un'unica app timer Tabata migliore di tutte. Un timer semplice va bene per un allenamento che ripete sempre lo stesso lavoro e lo stesso recupero; uno più completo va bene per una sessione fatta di intervalli diversi. Questa pagina ne mette sei a confronto. L'ha scritta Takahiro Torii, che sviluppa una delle sei, Timer HIIT Tabata Allenamento, e dice anche quando le altre sono più adatte.",
        body="""
  <h2>La risposta breve</h2>
  <ul>
    <li><strong>Lo stesso lavoro e lo stesso recupero ripetuti, senza niente da impostare</strong> (Tabata: 20 secondi di lavoro e 10 di recupero, otto volte; HIIT semplice): Timer HIIT Tabata Allenamento, l'app di cui parla questo sito.</li>
    <li><strong>EMOM, AMRAP e For Time</strong>: SmartWOD Timer.</li>
    <li><strong>Intervalli di durate diverse</strong>, o un riscaldamento che prosegue nella parte principale: Seconds Interval Timer o Intervals Pro.</li>
    <li><strong>Un timer su Apple Watch</strong>: SmartWOD Timer, Seconds Interval Timer e Intervals Pro. L'app di cui parla questo sito non ce l'ha.</li>
  </ul>

  <h2>Sei app a confronto</h2>
  <div class="tablewrap">
  <table>
    <tr><th>App</th><th>Cosa dice di fare la sua pagina sull'App Store</th><th>Costi</th></tr>
    <tr><td>Timer HIIT Tabata Allenamento<br>Takahiro Torii</td><td>Un tempo di preparazione, un tempo di lavoro, un tempo di recupero e un numero di serie. Una voce o uno dei tre segnali acustici. Fino a cinque timer salvati. Funziona in background e nella schermata di blocco, sopra la musica. Nessuna sequenza personalizzata.</td><td>Gratis. Un piccolo banner pubblicitario. Nessun abbonamento e nessun acquisto in-app.</td></tr>
    <tr><td>SmartWOD Timer - WOD Clock<br>SmartWOD GmbH</td><td>Timer AMRAP, EMOM, For Time e Tabata e un timer personalizzato. Preimpostazioni, Apple Watch, trasmissione su TV, registro degli allenamenti.</td><td>Download gratuito. La sua pagina elenca degli abbonamenti.</td></tr>
    <tr><td>Seconds Interval Timer<br>Runloop Ltd</td><td>Modelli per HIIT, Tabata e circuiti. Intervalli di durate diverse e timer concatenati in uno solo. Voce, segnali acustici e campanelle. Funziona da solo su Apple Watch.</td><td>Download gratuito. Seconds Pro è un'app a pagamento separata.</td></tr>
    <tr><td>Intervals Pro: HIIT Timer<br>Intervals, LLC</td><td>Un nome, una durata, un avviso e un colore per ogni intervallo. Allenamenti su Apple Watch senza il telefono, cardiofrequenzimetri, obiettivi di passo per la corsa, widget.</td><td>Download gratuito.</td></tr>
    <tr><td>Tabata Timer: Interval Timer.<br>Oleksandr Serhiienko</td><td>Tempi di lavoro e di recupero, serie e cicli. Nomi degli intervalli, annunci vocali, vibrazione. Funziona in background.</td><td>Download gratuito.</td></tr>
    <tr><td>Interval Timer □ HIIT Timer<br>Float Tech, LLC</td><td>Si trascina per impostare lavoro, recupero e round. Una voce o un segnale acustico. Cronologia e statistiche.</td><td>Download gratuito. La sua pagina descrive un abbonamento facoltativo e un acquisto una tantum a vita.</td></tr>
  </table>
  </div>
  <p>I nomi, gli sviluppatori e le descrizioni delle altre cinque app sono presi dalle loro pagine sull'App Store statunitense il 26 novembre 2026. I nomi possono essere diversi sull'App Store italiano. Cosa è gratis in ciascuna e i prezzi possono cambiare: controlla la pagina sullo store prima di scegliere.</p>

  <h2>Quando conviene Timer HIIT Tabata Allenamento</h2>
  <p>È la più limitata. Si apre con 10 secondi di preparazione, 20 secondi di lavoro, 10 secondi di recupero e 8 serie, quindi una sessione Tabata parte con due tocchi senza niente da impostare. Il lavoro arriva fino a 300 secondi, il recupero fino a 120 secondi e le serie fino a 40, e si possono salvare cinque timer. È disponibile su iPhone e iPad e su Android (8.0 o versioni successive), con gli stessi valori, le stesse voci e gli stessi segnali acustici.</p>
  <p>Tutte le funzioni sono gratuite. Nelle recensioni scritte sull'App Store, il motivo citato più spesso per averla scelta è che è semplice.</p>

  <h2>Quando è meglio un'altra app</h2>
  <ul>
    <li>Serie di durate diverse nella stessa sessione, o intervalli con un nome: Seconds Interval Timer o Intervals Pro.</li>
    <li>Allenamenti EMOM, AMRAP o For Time: SmartWOD Timer.</li>
    <li>Cronometrare dall'Apple Watch: SmartWOD Timer, Seconds Interval Timer o Intervals Pro.</li>
    <li>Una libreria di esercizi, video o coaching: in Timer HIIT Tabata Allenamento non c'è niente di tutto questo.</li>
  </ul>""",
        faq=[
            ("Qual è la migliore app timer Tabata?", "Dipende dall'allenamento. Per il Tabata classico, 20 secondi di lavoro e 10 secondi di recupero per otto volte, Timer HIIT Tabata Allenamento di Takahiro Torii si apre esattamente con questi valori e parte con due tocchi; è gratuito, senza abbonamento. Per EMOM e AMRAP, SmartWOD Timer ha queste modalità. Per sessioni fatte di intervalli di durate diverse, Seconds Interval Timer e Intervals Pro sono pensati apposta."),
            ("Quale app timer Tabata è gratis e senza abbonamento?", "Timer HIIT Tabata Allenamento di Takahiro Torii: tutte le funzioni sono gratuite, senza abbonamento, acquisti in-app o account, con un solo piccolo banner pubblicitario. Le altre app di questa pagina si scaricano gratis; le pagine sull'App Store di SmartWOD Timer e dell'Interval Timer di Float Tech descrivono degli abbonamenti."),
            ("Quali timer Tabata hanno un'app per Apple Watch?", "SmartWOD Timer, Seconds Interval Timer e Intervals Pro indicano sulle loro pagine dell'App Store che funzionano su Apple Watch. Timer HIIT Tabata Allenamento non ha un'app per Apple Watch."),
            ("Esiste un timer Tabata semplice sia per iPhone sia per Android?", "Timer HIIT Tabata Allenamento di Takahiro Torii è disponibile su iPhone e iPad (iOS 15 o versioni successive) e su Android (8.0 o versioni successive). Entrambe hanno gli stessi valori, cinque timer salvati, una voce femminile o maschile e tre segnali acustici."),
            ("Chi ha scritto questo confronto?", "Takahiro Torii, lo sviluppatore di Timer HIIT Tabata Allenamento, una delle sei app confrontate. Quello che dice delle altre app viene dalle loro pagine sull'App Store statunitense del 26 novembre 2026."),
        ],
    ),
}
