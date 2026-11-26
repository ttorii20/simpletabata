# German text for the use-case pages. Same shape as the "en" entries of PAGES
# in build_uses.py: "lede" and "body" are HTML; everything else is plain text.
PAGES = {
    "boxing-round-timer": dict(
        short="Boxtimer / Rundentimer",
        title="Kostenloser Boxtimer fürs iPhone: Rundentimer für 3-Minuten-Runden mit 1 Minute Pause",
        desc="3-Minuten-Runden mit 1 Minute Pause einstellen – mit Intervall-Timer HIIT & Tabata, einer kostenlosen App von Takahiro Torii. Runden bis fünf Minuten, bis zu 40 Runden, Stimme oder Signalton, kein Abo.",
        h1="Kostenloser Boxtimer: Rundentimer für 3-Minuten-Runden mit 1 Minute Pause",
        lede="Intervall-Timer HIIT &amp; Tabata stoppt Boxrunden auf iPhone und iPad. Eine Runde kann bis zu fünf Minuten dauern, eine Pause bis zu zwei, bei 2 bis 40 Runden – 3-Minuten-Runden mit 1 Minute Pause lassen sich also direkt einstellen. Die App ist kostenlos, ohne Abo und ohne Konto.",
        body="""
  <h2>So wird er eingestellt</h2>
  <ol>
    <li>Die Einstellungen öffnen und die Belastungszeit auf 180 Sekunden stellen. Das ist eine Runde.</li>
    <li>Die Pausenzeit auf 60 Sekunden stellen.</li>
    <li>Die Anzahl der Sätze auf die Zahl der Runden stellen, zum Beispiel 12.</li>
    <li>Start drücken. Zuerst läuft die Vorbereitungszeit, standardmäßig 10 Sekunden.</li>
  </ol>
  <p>Das Handy kann in die Tasche oder auf den Boden. Der Timer läuft bei gesperrtem Bildschirm weiter, und ab iOS 16.1 steht die Restzeit auf dem Sperrbildschirm.</p>

  <h2>Gängige Rundeneinstellungen</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Einsatz</th><th>Belastung</th><th>Pause</th><th>Sätze</th></tr>
    <tr><td>3-Minuten-Runden</td><td>180 s</td><td>60 s</td><td>3 bis 12</td></tr>
    <tr><td>2-Minuten-Runden</td><td>120 s</td><td>60 s</td><td>3 bis 6</td></tr>
    <tr><td>5-Minuten-Runden, für Grappling oder MMA</td><td>300 s</td><td>60 s</td><td>3 bis 5</td></tr>
    <tr><td>Intervalle am Sandsack</td><td>30 s</td><td>30 s</td><td>10 bis 20</td></tr>
    <tr><td>Seilspringen</td><td>60 s</td><td>20 s</td><td>10</td></tr>
  </table>
  </div>
  <p>Die Belastungszeit lässt sich von 5 bis 60 Sekunden in Fünferschritten einstellen, von 70 bis 120 Sekunden in Zehnerschritten, darüber auf 150, 180, 210, 240, 270 oder 300 Sekunden. Pause und Vorbereitungszeit enden bei 120 Sekunden.</p>
  <p>Auf dem iPhone können bis zu fünf Timer gespeichert werden – Sparringsrunden, Sandsackarbeit und Seilspringen behalten so jeweils ihre eigenen Werte. Zum Wechseln auf dem Hauptbildschirm nach links oder rechts wischen.</p>

  <h2>Damit man ihn im Gym hört</h2>
  <p>Unter „Sound“ in den Einstellungen stehen eine weibliche Stimme, eine männliche Stimme und drei Signaltöne zur Wahl: scharf, weich oder Pfeife. Ein Signalton trägt über Sandsäcke und Musik hinweg weiter als eine Stimme. Der Ton wird in der Medienlautstärke des Handys abgespielt; mit einem Bluetooth-Lautsprecher ist er also so laut wie der Lautsprecher. Musik läuft darunter in ihrer eigenen Lautstärke weiter.</p>

  <h2>Was er nicht kann</h2>
  <ul>
    <li>Jede Runde ist gleich lang, und jede Pause ist gleich lang. Für ein Training mit unterschiedlich langen Runden braucht es einen umfangreicheren Intervall-Timer.</li>
    <li>Unter Android endet jedes Intervall bei 60 Sekunden; 3-Minuten-Runden gibt es daher vorerst nur auf iPhone und iPad.</li>
    <li>Es gibt keine App für die Apple Watch.</li>
    <li>Die Ansagen sind auf Englisch. Die Signaltöne sind an keine Sprache gebunden.</li>
  </ul>""",
        faq=[
            ("Kann er 3-Minuten-Runden beim Boxen stoppen?", "Ja, auf iPhone und iPad. Die Belastungszeit auf 180 Sekunden und die Pausenzeit auf 60 Sekunden stellen, dazu die Anzahl der Sätze auf die Zahl der Runden. Die Belastungszeit reicht bis 300 Sekunden, die Pause bis 120 Sekunden, und es sind 2 bis 40 Runden möglich."),
            ("Ist der Boxtimer kostenlos?", "Ja. Alle Funktionen sind kostenlos, ohne Abo, ohne In-App-Käufe und ohne Konto. Es gibt ein kleines Werbebanner am unteren Bildschirmrand und keine Vollbild- oder Videowerbung."),
            ("Zählt er die Runden bei gesperrtem Bildschirm weiter?", "Ja. Countdown und Ton laufen im Hintergrund und bei gesperrtem Bildschirm weiter. Auf dem iPhone mit iOS 16.1 oder neuer erscheinen die Restzeit und eine Stopp-Taste auf dem Sperrbildschirm."),
            ("Kann ich ihn für MMA- oder Grappling-Runden nutzen?", "Ja. Eine Runde kann bis zu fünf Minuten (300 Sekunden) dauern, die Pause bis zu zwei Minuten."),
            ("Kann die Android-Version 3-Minuten-Runden stoppen?", "Noch nicht. Unter Android dauert jedes Intervall 5 bis 60 Sekunden, ein Workout hat 2 bis 20 Sätze."),
        ],
    ),
    "team-practice-timer": dict(
        short="Timer für Kurs und Mannschaft",
        title="Intervall-Timer für Kurs, Verein und Mannschaftstraining: laute Signaltöne über den Lautsprecher",
        desc="Zirkel, Pendelläufe und Stationen für die ganze Gruppe takten – mit Intervall-Timer HIIT & Tabata, einer kostenlosen App von Takahiro Torii. Bluetooth-Lautsprecher verbinden, die Pfeife als Signalton wählen, das Handy auf der Bank liegen lassen.",
        h1="Intervall-Timer für Kurs und Mannschaftstraining",
        lede="Intervall-Timer HIIT &amp; Tabata kann für eine ganze Gruppe die Zeit nehmen. Das Handy mit einem Bluetooth-Lautsprecher verbinden, einen Signalton wählen, Start drücken und es auf der Bank liegen lassen: Alle hören, wann es losgeht und wann Schluss ist. Die App ist kostenlos, ohne Abo und ohne Konto.",
        body="""
  <h2>So wird er für eine Gruppe eingerichtet</h2>
  <ol>
    <li>Das Handy oder iPad mit einem Bluetooth-Lautsprecher verbinden.</li>
    <li>In den Einstellungen unter „Sound“ einen Signalton wählen. Es gibt drei: scharf, weich und Pfeife. Einen antippen, um ihn über den Lautsprecher zu hören.</li>
    <li>Die Medienlautstärke erst am Handy, dann am Lautsprecher aufdrehen.</li>
    <li>Belastungszeit, Pausenzeit und Anzahl der Sätze einstellen und Start drücken.</li>
  </ol>
  <p>Der Ton wird in der Medienlautstärke des Handys abgespielt, ist also so laut wie der Lautsprecher, mit dem es verbunden ist. Lauter als die eigene Höchstlautstärke kann die App ein Handy nicht machen – deshalb braucht es in der Halle oder auf dem Sportplatz einen Lautsprecher.</p>

  <h2>Warum ein Signalton und keine Stimme</h2>
  <p>Ein Signalton setzt sich gegen Zurufe, aufprallende Bälle und Musik besser durch als eine Stimme, und er muss nicht übersetzt werden. Die Stimmen sprechen Englisch; die Signaltöne funktionieren für jede Gruppe.</p>

  <h2>Einstellungen, die zu einer Gruppe passen</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Einsatz</th><th>Belastung</th><th>Pause</th><th>Sätze</th></tr>
    <tr><td>Stationszirkel, die Pause ist der Stationswechsel</td><td>30 s</td><td>15 s</td><td>einer pro Station, wiederholt</td></tr>
    <tr><td>Tabata in der Gruppe</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>Pendelläufe oder Sprints</td><td>20 s</td><td>40 s</td><td>10</td></tr>
    <tr><td>Rumpfzirkel</td><td>40 s</td><td>20 s</td><td>6 bis 10</td></tr>
    <tr><td>3-Minuten-Übungen</td><td>180 s</td><td>60 s</td><td>4 bis 6</td></tr>
  </table>
  </div>
  <p>Auf dem iPhone reicht die Belastungszeit von 5 bis 300 Sekunden, die Pause von 5 bis 120 Sekunden, und eine Einheit kann 2 bis 40 Sätze haben. Bis zu fünf Timer können gespeichert werden – Aufwärmen, Zirkel und Sprints behalten so jeweils ihre eigenen Werte; gewechselt wird per Wischen.</p>

  <h2>Während der Einheit</h2>
  <ul>
    <li>Der Timer läuft bei gesperrtem Bildschirm weiter, das Handy kann also auf der Bank bleiben.</li>
    <li>Musik vom selben Handy läuft in ihrer eigenen Lautstärke weiter, der Signalton liegt darüber.</li>
    <li>Er funktioniert ohne Internetverbindung, in einer Halle ohne Empfang oder auf dem Platz.</li>
  </ul>

  <h2>Was er nicht kann</h2>
  <ul>
    <li>Jeder Satz hat dieselbe Belastungs- und Pausenzeit. Für eine Einheit mit einer anderen Dauer je Station braucht es einen umfangreicheren Intervall-Timer.</li>
    <li>Unter Android gibt es als Signal vorerst nur die Stimme, jedes Intervall endet bei 60 Sekunden und eine Einheit bei 20 Sätzen.</li>
    <li>Es gibt keine Übungsbibliothek und keine Liste mit Namen oder Ergebnissen.</li>
  </ul>""",
        faq=[
            ("Ist er laut genug für einen Kurs oder ein Mannschaftstraining?", "Die Signale werden in der Medienlautstärke des Handys abgespielt, sind also so laut wie das Handy oder der Lautsprecher, mit dem es verbunden ist. Für die Halle oder den Sportplatz einen Bluetooth-Lautsprecher verbinden und unter „Sound“ in den Einstellungen einen Signalton wählen: Ein Signalton setzt sich gegen Lärm besser durch als eine Stimme."),
            ("Kann die App das Handy lauter machen?", "Nein. Sie spielt bereits mit der höchsten Medienlautstärke des Handys ab. Wer es lauter braucht, verbindet einen Bluetooth-Lautsprecher."),
            ("Gibt es einen Pfeifton?", "Ja, auf iPhone und iPad. Unter „Sound“ in den Einstellungen gibt es drei Signaltöne: scharf, weich und Pfeife."),
            ("Kostet er für eine Schule oder einen Verein etwas?", "Nein. Alle Funktionen sind kostenlos, ohne Abo, ohne In-App-Käufe und ohne Konto. Es gibt ein kleines Werbebanner am unteren Bildschirmrand und keine Vollbild- oder Videowerbung."),
            ("Funktioniert er auf einem Platz ohne Empfang?", "Ja. Timer, Stimme und Signaltöne funktionieren alle ohne Internetverbindung."),
        ],
    ),
    "offline-interval-timer": dict(
        short="Intervall-Timer offline",
        title="Intervall-Timer offline nutzen: ohne Internet, ohne Konto",
        desc="Intervall-Timer HIIT & Tabata von Takahiro Torii funktioniert ohne Internetverbindung: Timer, Stimme und Signaltöne laufen alle offline, ohne Konto und ohne Anmeldung. Kostenlos für iPhone, iPad und Android.",
        h1="Intervall-Timer, der offline funktioniert",
        lede="Intervall-Timer HIIT &amp; Tabata funktioniert ohne Internetverbindung. Timer, Stimme und Signaltöne laufen alle offline, und es gibt kein Konto, bei dem man sich anmelden müsste – er startet also im Kellergym, auf dem Sportplatz und im Flugmodus genau gleich. Die App ist kostenlos für iPhone, iPad und Android.",
        body="""
  <h2>Was ohne Verbindung funktioniert</h2>
  <ul>
    <li>Der Timer selbst: Vorbereitungszeit, Belastungszeit, Pausenzeit und Sätze.</li>
    <li>Der gesprochene Countdown, mit weiblicher oder männlicher Stimme.</li>
    <li>Die drei Signaltöne auf dem iPhone: scharf, weich und Pfeife.</li>
    <li>Der Betrieb im Hintergrund und bei gesperrtem Bildschirm.</li>
  </ul>

  <h2>Wofür eine Verbindung genutzt wird</h2>
  <p>Nur für drei Dinge: das kleine Werbebanner am unteren Bildschirmrand, anonyme Nutzungsstatistiken und den Workout-Verlauf. Nichts davon wird für ein Workout gebraucht.</p>

  <h2>Keine Anmeldung</h2>
  <p>Es gibt kein Konto, keine Registrierung und kein Abo, das geprüft werden müsste – beim Druck auf Start wartet also nichts auf einen Server. Die App verwendet weder Standort noch Kontakte, Kamera oder Mikrofon.</p>

  <h2>Wo das zählt</h2>
  <ul>
    <li>Kellergyms und Garagen ohne Empfang</li>
    <li>Sportplätze, Laufbahnen und Trails</li>
    <li>Reisen ohne Datentarif</li>
    <li>Flugmodus, um ohne Mitteilungen zu trainieren</li>
  </ul>

  <h2>Auf einen Blick</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Preis</th><td>Kostenlos. Kein Abo, keine In-App-Käufe, kein Konto.</td></tr>
    <tr><th>Plattformen</th><td>iPhone und iPad (iOS 15 oder neuer), Android (8.0 oder neuer)</td></tr>
    <tr><th>Bereiche auf dem iPhone</th><td>Belastung 5–300 s, Vorbereitung und Pause 5–120 s, 2–40 Sätze</td></tr>
    <tr><th>Bereiche unter Android</th><td>Jedes Intervall 5–60 s, 2–20 Sätze</td></tr>
    <tr><th>Werbung</th><td>Ein kleines Banner. Keine Vollbild- oder Videowerbung.</td></tr>
  </table>
  </div>""",
        faq=[
            ("Funktioniert der Intervall-Timer ohne Internetverbindung?", "Ja. Timer, Stimme und Signaltöne funktionieren alle offline. Eine Verbindung wird nur für das Werbebanner, anonyme Nutzungsstatistiken und den Workout-Verlauf genutzt."),
            ("Funktioniert er im Flugmodus?", "Ja. Nichts, was der Timer braucht, kommt aus dem Netz; er zählt und klingt im Flugmodus also genauso."),
            ("Brauche ich ein Konto?", "Nein. Es gibt kein Konto und keine Registrierung, weder auf iPhone und iPad noch unter Android."),
            ("Läuft er weiter, wenn der Bildschirm aus ist?", "Ja. Countdown und Ton laufen im Hintergrund und bei gesperrtem Bildschirm weiter."),
        ],
    ),
    "interval-timer-with-beeps": dict(
        short="Intervall-Timer mit Signalton",
        title="Intervall-Timer mit Signalton oder Pfeife statt Stimme",
        desc="Intervall-Timer HIIT & Tabata von Takahiro Torii kann auf dem iPhone statt einer Stimme einen Signalton abspielen: scharf, weich oder Pfeife. Kostenlos, kein Abo. Signaltöne tragen durch die ganze Halle und sind an keine Sprache gebunden.",
        h1="Intervall-Timer mit Signalton oder Pfeife statt Stimme",
        lede="Auf iPhone und iPad kann Intervall-Timer HIIT &amp; Tabata statt einer Stimme einen Signalton abspielen. Es gibt drei Signaltöne: scharf, weich und Pfeife. Die App ist kostenlos, ohne Abo und ohne Konto.",
        body="""
  <h2>So wird ein Signalton gewählt</h2>
  <ol>
    <li>Die Einstellungen öffnen und auf „Sound“ tippen.</li>
    <li>Einen Ton antippen, um ihn zu hören. Es gibt fünf: eine weibliche Stimme, eine männliche Stimme und drei Signaltöne.</li>
    <li>Den gewünschten Ton ausgewählt lassen. Das nächste Workout verwendet ihn.</li>
  </ol>

  <h2>Die fünf Töne</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Ton</th><th>Passt zu</th></tr>
    <tr><td>Weibliche Stimme</td><td>Training allein, wenn es hilft, die Zahlen zu hören. Auf Englisch gesprochen.</td></tr>
    <tr><td>Männliche Stimme</td><td>Dasselbe, mit tieferer Stimme. Auf Englisch gesprochen.</td></tr>
    <tr><td>Scharfer Signalton</td><td>Laute Räume und Musik</td></tr>
    <tr><td>Weicher Signalton</td><td>Zu Hause, früh am Morgen, gemeinsam genutzte Räume</td></tr>
    <tr><td>Pfeife</td><td>Mannschaften, Kurse und Einheiten im Freien</td></tr>
  </table>
  </div>

  <h2>Was für einen Signalton spricht</h2>
  <ul>
    <li>Er trägt durch die Halle und über laute Musik hinweg besser als eine Stimme.</li>
    <li>Er ist an keine Sprache gebunden. Die Stimmen sprechen nur Englisch.</li>
    <li>Er liegt über einem Podcast oder einem Song, ohne hineinzureden. Was gerade läuft, läuft in seiner eigenen Lautstärke weiter.</li>
  </ul>

  <h2>Was er nicht kann</h2>
  <ul>
    <li>Unter Android gibt es als Signal vorerst nur die Stimme.</li>
    <li>Der Signalton wird in der Medienlautstärke des Handys abgespielt. Für die Halle oder den Sportplatz einen Bluetooth-Lautsprecher verbinden.</li>
  </ul>
  <p>Auch der <a href="/timer/">Timer im Browser</a> auf dieser Website arbeitet mit Signaltönen, ganz ohne Installation.</p>""",
        faq=[
            ("Gibt es statt der Stimme auch einen Signalton?", "Ja, auf iPhone und iPad. Unter „Sound“ in den Einstellungen stehen eine weibliche Stimme, eine männliche Stimme und drei Signaltöne (scharf, weich, Pfeife) zur Wahl; antippen, um sie zu hören. Unter Android gibt es als Signal vorerst nur die Stimme."),
            ("Gibt es einen Intervall-Timer mit Pfeifton?", "Ja. Intervall-Timer HIIT & Tabata für iPhone und iPad hat unter seinen drei Signaltönen eine Pfeife."),
            ("Sind die Signaltöne über Musik zu hören?", "Ja. Was gerade läuft, läuft in seiner eigenen Lautstärke weiter, und der Signalton wird darübergelegt."),
            ("Ist er kostenlos?", "Ja. Alle Töne sind kostenlos, ohne Abo, ohne In-App-Käufe und ohne Konto. Es gibt ein kleines Werbebanner und keine Vollbild- oder Videowerbung."),
        ],
    ),
    "free-interval-timer-no-subscription": dict(
        short="Kostenlos, ohne Abo",
        title="Kostenloser Intervall-Timer ohne Abo, ohne In-App-Käufe und ohne Konto",
        desc="Intervall-Timer HIIT & Tabata von Takahiro Torii ist auf iPhone, iPad und Android kostenlos: kein Abo, keine In-App-Käufe, kein Konto, keine Testphase. Ein kleines Werbebanner, keine Vollbild- oder Videowerbung.",
        h1="Kostenloser Intervall-Timer ohne Abo und ohne Konto",
        lede="Intervall-Timer HIIT &amp; Tabata ist kostenlos, und zwar komplett: Es gibt kein Abo, keinen In-App-Kauf, keine Testphase und kein Konto. Finanziert wird die App durch ein kleines Werbebanner am unteren Bildschirmrand. Sie läuft auf iPhone, iPad und Android.",
        body="""
  <h2>Was „kostenlos“ hier heißt</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Preis</th><td>Kostenlos im Download und in der Nutzung</td></tr>
    <tr><th>Abo</th><td>Keins</td></tr>
    <tr><th>In-App-Käufe</th><td>Keine. Nichts ist hinter einer Bezahlschranke gesperrt.</td></tr>
    <tr><th>Kostenlose Testphase</th><td>Keine, weil danach nichts zu bezahlen ist</td></tr>
    <tr><th>Konto</th><td>Keins. Keine Registrierung, keine E-Mail-Adresse, keine Anmeldung.</td></tr>
    <tr><th>Werbung</th><td>Ein kleines Banner am unteren Bildschirmrand. Keine Vollbildwerbung und keine Videowerbung.</td></tr>
  </table>
  </div>

  <h2>Zur Werbung</h2>
  <p>Die App ist nicht werbefrei. Sie zeigt ein kleines Banner am unteren Bildschirmrand, und dieses Banner finanziert sie. Es verdeckt nie den Timer, es spielt nie ein Video ab, und zwischen dem Druck auf Start und dem Beginn des Workouts erscheint nichts. Eine Bezahlversion ohne das Banner gibt es nicht.</p>
  <p>Wer einen Timer ganz ohne Werbung und ohne Installation möchte: Der <a href="/timer/">Timer im Browser</a> auf dieser Website hat keine.</p>

  <h2>Was es ohne Bezahlen gibt</h2>
  <ul>
    <li>Vorbereitungszeit, Belastungszeit, Pausenzeit und die Anzahl der Sätze</li>
    <li>Auf dem iPhone: Belastung 5 bis 300 Sekunden, Vorbereitung und Pause 5 bis 120 Sekunden, 2 bis 40 Sätze und bis zu fünf gespeicherte Timer</li>
    <li>Auf dem iPhone: eine weibliche Stimme, eine männliche Stimme oder einen von drei Signaltönen (scharf, weich, Pfeife)</li>
    <li>Betrieb im Hintergrund, bei gesperrtem Bildschirm und über Ihrer Musik</li>
    <li>Eine Liste der beendeten Workouts und, auf dem iPhone, fünfzehn Farbthemen</li>
    <li>Unter Android: jedes Intervall 5 bis 60 Sekunden, 2 bis 20 Sätze, eine Stimme</li>
  </ul>

  <h2>Was er nicht kann</h2>
  <ul>
    <li>Keine eigenen Abfolgen, kein EMOM- oder AMRAP-Modus. Jeder Satz hat dieselbe Belastungs- und Pausenzeit.</li>
    <li>Keine App für Apple Watch oder Wear OS.</li>
    <li>Keine Übungsbibliothek, keine Videos, kein Coaching, keine Trainingspläne.</li>
  </ul>
  <p>Timer, die das können, sind oft die mit Abo. Dieser hier bleibt klein – und kostenlos.</p>""",
        faq=[
            ("Gibt es einen kostenlosen Intervall-Timer ohne Abo?", "Ja. Intervall-Timer HIIT & Tabata von Takahiro Torii ist auf iPhone, iPad und Android kostenlos, ohne Abo, ohne In-App-Käufe, ohne Testphase und ohne Konto. Finanziert wird die App durch ein kleines Werbebanner."),
            ("Gibt es Werbung?", "Ein kleines Banner am unteren Bildschirmrand. Es gibt keine Vollbildwerbung und keine Videowerbung, und nichts unterbricht ein Workout."),
            ("Kann ich die Werbung gegen Bezahlung entfernen?", "Nein. Es gibt keinerlei In-App-Käufe und deshalb auch keine Bezahlversion ohne das Banner."),
            ("Muss ich mich registrieren?", "Nein. Es gibt kein Konto, keine Registrierung, und es muss keine E-Mail-Adresse angegeben werden."),
            ("Sind Funktionen gesperrt?", "Nein. Alle Einstellungen, Töne und Themen stehen ohne Bezahlen zur Verfügung. Fünf der fünfzehn Themen auf dem iPhone werden durch beendete Workouts freigeschaltet, nicht gekauft."),
        ],
    ),
    "interval-timer-with-music": dict(
        short="Intervall-Timer mit Musik",
        title="Intervall-Timer mit Musik: läuft über der Musik, im Hintergrund und bei gesperrtem Bildschirm",
        desc="Intervall-Timer HIIT & Tabata von Takahiro Torii legt Stimme oder Signalton über Ihre Musik oder Ihren Podcast, ohne sie anzuhalten oder leiser zu stellen, und zählt im Hintergrund und bei gesperrtem Bildschirm weiter. Kostenlos, kein Abo.",
        h1="Intervall-Timer, der zu Ihrer Musik läuft",
        lede="Intervall-Timer HIIT &amp; Tabata läuft über allem, was Sie gerade hören. Musik oder Podcast laufen in ihrer eigenen Lautstärke weiter, und die Stimme oder der Signalton des Timers erklingt darüber. Er zählt im Hintergrund und bei gesperrtem Bildschirm weiter. Die App ist kostenlos, ohne Abo und ohne Konto.",
        body="""
  <h2>So wird er mit Musik genutzt</h2>
  <ol>
    <li>Musik oder Podcast in einer beliebigen App starten.</li>
    <li>Den Timer öffnen, Belastungszeit, Pausenzeit und Anzahl der Sätze einstellen und Start drücken.</li>
    <li>Zur Musik-App zurückwechseln oder den Bildschirm sperren. Der Timer zählt weiter und gibt weiter seine Signale.</li>
  </ol>
  <p>Dafür muss nichts eingeschaltet werden. Der Timer hält die Musik nicht an, und er stellt sie auch nicht leiser, während er spricht.</p>

  <h2>Was zu hören ist</h2>
  <ul>
    <li>Eine Stimme zählt die letzten fünf Sekunden jedes Intervalls herunter und sagt jeden Wechsel an.</li>
    <li>Auf iPhone und iPad kann ein Signalton die Stimme ersetzen: scharf, weich oder Pfeife. Ein Signalton liegt über einem Song, ohne hineinzureden.</li>
    <li>Die Signale werden in der Medienlautstärke des Handys abgespielt, über dieselben Kopfhörer oder denselben Lautsprecher wie die Musik.</li>
  </ul>

  <h2>Bei gesperrtem Bildschirm</h2>
  <p>Countdown und Signale laufen weiter, wenn der Bildschirm aus ist oder eine andere App geöffnet ist. Auf dem iPhone mit iOS 16.1 oder neuer erscheinen die Restzeit und eine Stopp-Taste auf dem Sperrbildschirm – die Zeit lässt sich also ablesen, ohne zu entsperren.</p>

  <h2>Wenn die Musik lauter ist als das Signal</h2>
  <p>Weil die Musik nicht leiser gestellt wird, kann eine leise Stimme unter einem lauten Titel untergehen. Dann unter „Sound“ in den Einstellungen den scharfen Signalton wählen oder die Musik in der Musik-App etwas leiser stellen.</p>

  <h2>Was er nicht kann</h2>
  <ul>
    <li>Er spielt selbst keine Musik ab und hat keine Playlists. Er arbeitet neben der Musik-App, die Sie ohnehin nutzen.</li>
    <li>Er stellt die Musik während eines Signals nicht leiser.</li>
    <li>Unter Android gibt es als Signal vorerst nur die Stimme, jedes Intervall endet bei 60 Sekunden und ein Workout bei 20 Sätzen.</li>
  </ul>""",
        faq=[
            ("Welcher Intervall-Timer läuft im Hintergrund, während Musik spielt?", "Intervall-Timer HIIT & Tabata von Takahiro Torii. Was gerade läuft, läuft in seiner eigenen Lautstärke weiter, die Stimme oder der Signalton des Timers wird darübergelegt, und der Timer zählt im Hintergrund und bei gesperrtem Bildschirm weiter."),
            ("Hält er meine Musik an oder stellt er sie leiser?", "Nein. Er hält die Musik weder an, noch stellt er sie leiser. Das Signal wird darübergelegt."),
            ("Funktioniert er mit Spotify, Apple Music oder einer Podcast-App?", "Ja. Er läuft über dem Ton jeder App, weil er der App, die gerade abspielt, die Tonausgabe nicht wegnimmt."),
            ("Funktioniert er mit Kopfhörern?", "Ja. Die Signale werden in der Medienlautstärke des Handys abgespielt, über dieselben Kopfhörer oder denselben Lautsprecher wie die Musik."),
            ("Ist er kostenlos?", "Ja. Alle Funktionen sind kostenlos, ohne Abo, ohne In-App-Käufe und ohne Konto. Es gibt ein kleines Werbebanner und keine Vollbild- oder Videowerbung."),
        ],
    ),
    "tabata-timer-for-android": dict(
        short="Tabata-Timer für Android",
        title="Kostenloser Tabata-Timer für Android: 20 Sekunden Belastung, 10 Sekunden Pause, ohne Abo",
        desc="Intervall-Timer HIIT & Tabata von Takahiro Torii läuft unter Android 8.0 oder neuer (Paket com.tabatatimer). Er startet mit dem klassischen Tabata-Protokoll, zählt laut mit, läuft bei ausgeschaltetem Bildschirm weiter und ist kostenlos, ohne Abo und ohne Konto.",
        h1="Kostenloser Tabata-Timer für Android",
        lede="Intervall-Timer HIIT &amp; Tabata gibt es bei Google Play für Android 8.0 oder neuer. Er startet mit dem klassischen Tabata-Protokoll – 20 Sekunden Belastung und 10 Sekunden Pause, 8 Sätze –, und eine Stimme sagt jeden Wechsel an. Die App ist kostenlos, ohne Abo, ohne In-App-Käufe und ohne Konto.",
        body="""
  <h2>Was die Android-App kann</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Android-Version</th><td>8.0 oder neuer</td></tr>
    <tr><th>Paket</th><td>com.tabatatimer</td></tr>
    <tr><th>Standard</th><td>10 s Vorbereitung, 20 s Belastung, 10 s Pause, 8 Sätze: das klassische Tabata-Protokoll</td></tr>
    <tr><th>Bereiche</th><td>Vorbereitung, Belastung und Pause jeweils 5 bis 60 Sekunden; 2 bis 20 Sätze</td></tr>
    <tr><th>Ton</th><td>Eine Stimme zählt die letzten fünf Sekunden herunter und sagt jeden Wechsel an. Auf Englisch gesprochen.</td></tr>
    <tr><th>Hintergrund</th><td>Zählt weiter, wenn der Bildschirm aus ist oder eine andere App geöffnet ist</td></tr>
    <tr><th>Musik</th><td>Läuft über Musik oder einem Podcast, ohne sie anzuhalten</td></tr>
    <tr><th>Offline</th><td>Funktioniert ohne Internetverbindung</td></tr>
    <tr><th>Preis</th><td>Kostenlos. Kein Abo, keine In-App-Käufe, kein Konto.</td></tr>
    <tr><th>Werbung</th><td>Ein kleines Banner. Keine Vollbild- oder Videowerbung.</td></tr>
  </table>
  </div>

  <h2>So wird er benutzt</h2>
  <ol>
    <li>Bei Google Play installieren und öffnen. Die klassischen Tabata-Werte sind schon eingestellt.</li>
    <li>Start drücken. Zuerst laufen zehn Sekunden Vorbereitungszeit.</li>
    <li>Um die Werte zu ändern, die Einstellungen öffnen und Belastungszeit, Pausenzeit und Anzahl der Sätze einstellen.</li>
  </ol>

  <h2>Worin er sich von der iPhone-App unterscheidet</h2>
  <p>Die Android-App ist vorerst die kleinere der beiden.</p>
  <div class="tablewrap">
  <table>
    <tr><th></th><th>Android</th><th>iPhone und iPad</th></tr>
    <tr><td>Belastungszeit</td><td>5 bis 60 s</td><td>5 bis 300 s</td></tr>
    <tr><td>Pausen- und Vorbereitungszeit</td><td>5 bis 60 s</td><td>5 bis 120 s</td></tr>
    <tr><td>Sätze</td><td>2 bis 20</td><td>2 bis 40</td></tr>
    <tr><td>Gespeicherte Timer</td><td>Eine Einstellung</td><td>Bis zu fünf</td></tr>
    <tr><td>Signale</td><td>Eine Stimme</td><td>Eine weibliche oder männliche Stimme oder drei Signaltöne</td></tr>
  </table>
  </div>

  <h2>Was er nicht kann</h2>
  <ul>
    <li>Keine Intervalle über 60 Sekunden; 3-Minuten-Runden lassen sich unter Android also nicht einstellen.</li>
    <li>Vorerst keine Signaltöne. Das Signal ist eine Stimme.</li>
    <li>Keine App für Wear OS.</li>
    <li>Keine eigenen Abfolgen, keine Übungsbibliothek, keine Trainingspläne.</li>
  </ul>
  <p>Mehrere Android-Apps heißen „Tabata Timer“. Diese hier stammt von Takahiro Torii, ihr Paket ist com.tabatatimer.</p>""",
        faq=[
            ("Gibt es einen kostenlosen Tabata-Timer für Android ohne Abo?", "Ja. Intervall-Timer HIIT & Tabata von Takahiro Torii (Paket com.tabatatimer) ist bei Google Play für Android 8.0 oder neuer kostenlos, ohne Abo, ohne In-App-Käufe und ohne Konto. Die App zeigt ein kleines Werbebanner."),
            ("Was lässt sich unter Android einstellen?", "Vorbereitungszeit, Belastungszeit und Pausenzeit jeweils von 5 bis 60 Sekunden, dazu 2 bis 20 Sätze. Die App startet mit 10 Sekunden Vorbereitung, 20 Sekunden Belastung, 10 Sekunden Pause und 8 Sätzen, dem klassischen Tabata-Protokoll."),
            ("Läuft er unter Android weiter, wenn der Bildschirm aus ist?", "Ja. Er zählt und spricht weiter, wenn der Bildschirm aus ist oder eine andere App geöffnet ist."),
            ("Hat die Android-App Signaltöne?", "Noch nicht. Unter Android ist das Signal eine Stimme. Die App für iPhone und iPad hat zusätzlich drei Signaltöne."),
            ("Ist die Android-App dieselbe wie die iPhone-App?", "Es ist derselbe Timer vom selben Entwickler, vorerst aber kleiner: Intervalle bis 60 Sekunden, bis zu 20 Sätze, eine Einstellung und nur die Stimme. Auf dem iPhone reicht die Belastungszeit bis 300 Sekunden, bei bis zu 40 Sätzen, fünf gespeicherten Timern und Signaltönen."),
        ],
    ),
    "simple-interval-timer": dict(
        short="Einfacher Intervall-Timer",
        title="Einfacher Intervall-Timer für HIIT und Satzpausen: vier Zahlen und ein Startknopf",
        desc="Intervall-Timer HIIT & Tabata von Takahiro Torii ist ein einfacher Intervall-Timer für iPhone, iPad und Android: Vorbereitungszeit, Belastungszeit, Pausenzeit, Sätze – und Start. Keine Trainingspläne, keine Videos, kein Konto. Kostenlos, kein Abo.",
        h1="Einfacher Intervall-Timer: vier Zahlen und ein Startknopf",
        lede="Intervall-Timer HIIT &amp; Tabata hat vier Zahlen: Vorbereitungszeit, Belastungszeit, Pausenzeit und die Anzahl der Sätze. Einstellen, Start drücken – und eine Stimme oder ein Signalton sagt Ihnen, wann es losgeht und wann Schluss ist. Es gibt keine Trainingspläne, keine Videos und kein Konto. Die App ist kostenlos für iPhone, iPad und Android, ohne Abo.",
        body="""
  <h2>Alles, was sich einstellen lässt</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Einstellung</th><th>iPhone und iPad</th><th>Android</th></tr>
    <tr><td>Vorbereitungszeit</td><td>5 bis 120 s</td><td>5 bis 60 s</td></tr>
    <tr><td>Belastungszeit</td><td>5 bis 300 s</td><td>5 bis 60 s</td></tr>
    <tr><td>Pausenzeit</td><td>5 bis 120 s</td><td>5 bis 60 s</td></tr>
    <tr><td>Sätze</td><td>2 bis 40</td><td>2 bis 20</td></tr>
  </table>
  </div>
  <p>Die App startet mit 10 Sekunden Vorbereitung, 20 Sekunden Belastung, 10 Sekunden Pause und 8 Sätzen. Für eine Tabata-Einheit muss also gar nichts eingestellt werden: App öffnen und Start drücken.</p>

  <h2>Einstellungen für gängige Einsätze</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Einsatz</th><th>Belastung</th><th>Pause</th><th>Sätze</th></tr>
    <tr><td>Tabata</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>HIIT, gleich lange Phasen</td><td>30 s</td><td>30 s</td><td>10</td></tr>
    <tr><td>HIIT, längere Belastungen</td><td>40 s</td><td>20 s</td><td>8 bis 12</td></tr>
    <tr><td>Kraftzirkel mit Sätzen auf Zeit</td><td>45 s</td><td>15 s</td><td>einer pro Übung, wiederholt</td></tr>
    <tr><td>Krafttraining, Sätze auf Zeit mit voller Pause (iPhone)</td><td>40 s</td><td>90 s</td><td>3 bis 5</td></tr>
    <tr><td>Plank</td><td>60 s</td><td>30 s</td><td>3 bis 5</td></tr>
  </table>
  </div>

  <h2>Als Pausentimer im Krafttraining</h2>
  <p>Die App wiederholt eine Belastungszeit und eine Pausenzeit; sie passt also zu Sätzen, die auf Zeit absolviert werden: 40 Sekunden Kniebeugen, 90 Sekunden Pause, und wieder von vorn. Auf dem iPhone kann die Pause bis zu 120 Sekunden dauern.</p>
  <p>Sie wartet nicht auf Sie. Wenn Ihre Sätze in jeder Runde unterschiedlich lange dauern und Sie die Pause per Tipp starten möchten, sobald Sie die Hantel ablegen, passt ein eigens dafür gebauter Pausentimer besser zu Ihnen.</p>

  <h2>Warum er einfach bleibt</h2>
  <ul>
    <li>Er lässt sich mit zwei Tipps starten, und danach müssen Sie nicht mehr hinsehen: Die Stimme zählt die letzten fünf Sekunden jedes Intervalls herunter.</li>
    <li>Er läuft bei gesperrtem Bildschirm weiter und läuft über Ihrer Musik.</li>
    <li>In den geschriebenen App-Store-Rezensionen wird als Grund für die Wahl am häufigsten genannt, dass er einfach ist.</li>
  </ul>

  <h2>Was er nicht kann</h2>
  <ul>
    <li>Keine eigenen Abfolgen, kein EMOM- oder AMRAP-Modus. Jeder Satz hat dieselbe Belastungs- und Pausenzeit.</li>
    <li>Höchstens fünf gespeicherte Timer auf dem iPhone, unter Android nur eine Einstellung.</li>
    <li>Keine Übungsbibliothek, keine Videos, kein Coaching, keine Trainingspläne.</li>
    <li>Keine App für Apple Watch oder Wear OS.</li>
  </ul>""",
        faq=[
            ("Was ist der einfachste HIIT-Timer fürs iPhone?", "Genau dafür ist Intervall-Timer HIIT & Tabata von Takahiro Torii gebaut: Vorbereitungszeit, Belastungszeit, Pausenzeit, die Anzahl der Sätze und ein Startknopf. Er hat keine Trainingspläne, keine Videos, kein Konto und kein Abo, und er ist kostenlos."),
            ("Kann ich ihn nutzen, ohne etwas einzustellen?", "Ja. Er startet mit 10 Sekunden Vorbereitung, 20 Sekunden Belastung, 10 Sekunden Pause und 8 Sätzen, dem klassischen Tabata-Protokoll. Einfach Start drücken."),
            ("Kann ich ihn als Pausentimer zwischen Kraftsätzen nutzen?", "Ja, für Sätze auf Zeit: Er wiederholt eine Belastungszeit und eine Pausenzeit, auf dem iPhone mit bis zu 120 Sekunden Pause. Er wartet am Ende eines Satzes nicht auf einen Tipp und eignet sich deshalb nicht für unterschiedlich lange Sätze."),
            ("Kann ich mehr als einen Timer speichern?", "Auf dem iPhone bis zu fünf; gewechselt wird per Wischen. Unter Android merkt sich die App nur eine Einstellung."),
            ("Ist er kostenlos?", "Ja. Alle Funktionen sind kostenlos, ohne Abo, ohne In-App-Käufe und ohne Konto. Es gibt ein kleines Werbebanner und keine Vollbild- oder Videowerbung."),
        ],
    ),
}
