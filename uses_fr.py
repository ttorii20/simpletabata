"""French text of the use-case pages. Same shape as one language of PAGES in build_uses.py.

"lede" and "body" are HTML; the other fields are plain text.
"""

PAGES = {
    "boxing-round-timer": dict(
        short="Minuteur de rounds de boxe",
        title="Minuteur de rounds de boxe gratuit pour iPhone : rounds de 3 minutes, 1 minute de repos",
        desc="Réglez des rounds de trois minutes avec une minute de repos dans Minuteur Sport HIIT & Tabata, une app gratuite de Takahiro Torii. Rounds jusqu'à cinq minutes, jusqu'à 40 rounds, voix ou bip, sans abonnement.",
        h1="Minuteur de rounds de boxe gratuit : rounds de 3 minutes, 1 minute de repos",
        lede="Minuteur Sport HIIT &amp; Tabata chronomètre les rounds de boxe sur iPhone et iPad. Un round peut durer jusqu'à cinq minutes et un repos jusqu'à deux, pour 2 à 40 rounds : des rounds de trois minutes avec une minute de repos se règlent donc directement. L'app est gratuite, sans abonnement et sans compte.",
        body="""
  <h2>Comment le régler</h2>
  <ol>
    <li>Ouvrez les réglages et mettez le temps d'effort sur 180 secondes. C'est un round.</li>
    <li>Mettez le temps de repos sur 60 secondes.</li>
    <li>Mettez le nombre de séries sur le nombre de rounds, par exemple 12.</li>
    <li>Appuyez sur démarrer. Le temps de préparation, 10 secondes par défaut, passe en premier.</li>
  </ol>
  <p>Le téléphone peut rester dans une poche ou par terre. Le minuteur continue écran verrouillé et, sous iOS 16.1 ou version ultérieure, le temps restant s'affiche sur l'écran verrouillé.</p>

  <h2>Réglages courants pour les rounds</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Usage</th><th>Effort</th><th>Repos</th><th>Séries</th></tr>
    <tr><td>Rounds de trois minutes</td><td>180 s</td><td>60 s</td><td>3 à 12</td></tr>
    <tr><td>Rounds de deux minutes</td><td>120 s</td><td>60 s</td><td>3 à 6</td></tr>
    <tr><td>Rounds de cinq minutes, pour le grappling ou le MMA</td><td>300 s</td><td>60 s</td><td>3 à 5</td></tr>
    <tr><td>Intervalles au sac de frappe</td><td>30 s</td><td>30 s</td><td>10 à 20</td></tr>
    <tr><td>Corde à sauter</td><td>60 s</td><td>20 s</td><td>10</td></tr>
  </table>
  </div>
  <p>Le temps d'effort se règle de 5 à 60 secondes par pas de cinq, de 70 à 120 par pas de dix, ou sur 150, 180, 210, 240, 270 ou 300 secondes. Le repos et la préparation s'arrêtent à 120 secondes.</p>
  <p>Sur iPhone, on peut enregistrer jusqu'à cinq minuteurs : le sparring, le sac et la corde à sauter gardent ainsi chacun leurs propres valeurs. Balayez l'écran principal vers la gauche ou la droite pour passer de l'un à l'autre.</p>

  <h2>L'entendre dans une salle</h2>
  <p>Dans les réglages, « Sound » propose une voix féminine, une voix masculine ou l'un des trois bips : aigu, doux ou sifflet. Un bip porte plus loin qu'une voix par-dessus le bruit des sacs et la musique. Le son est joué au volume multimédia du téléphone : relié à une enceinte Bluetooth, il est aussi fort que l'enceinte. La musique continue en dessous, à son propre volume.</p>

  <h2>Ce qu'il ne fait pas</h2>
  <ul>
    <li>Tous les rounds ont la même durée, et tous les repos aussi. Pour une séance avec des rounds de durées différentes, il faut un minuteur d'intervalles plus complet.</li>
    <li>Sur Android, chaque intervalle s'arrête à 60 secondes : les rounds de trois minutes sont donc réservés à l'iPhone et à l'iPad, pour l'instant.</li>
    <li>Il n'y a pas d'app Apple Watch.</li>
    <li>Les annonces vocales sont en anglais. Les bips, eux, n'ont pas de langue.</li>
  </ul>""",
        faq=[
            ("Peut-il chronométrer des rounds de boxe de trois minutes ?", "Oui, sur iPhone et iPad. Mettez le temps d'effort sur 180 secondes, le temps de repos sur 60 secondes, et le nombre de séries sur le nombre de rounds. L'effort va jusqu'à 300 secondes, le repos jusqu'à 120 secondes, et l'on peut faire de 2 à 40 rounds."),
            ("Le minuteur de rounds de boxe est-il gratuit ?", "Oui. Toutes les fonctions sont gratuites, sans abonnement, sans achats intégrés et sans compte. Il y a une seule petite bannière publicitaire en bas de l'écran, et aucune publicité plein écran ni vidéo."),
            ("Continue-t-il de chronométrer les rounds écran verrouillé ?", "Oui. Le décompte et le son continuent en arrière-plan et écran verrouillé. Sur iPhone, sous iOS 16.1 ou version ultérieure, le temps restant et un bouton d'arrêt s'affichent sur l'écran verrouillé."),
            ("Puis-je l'utiliser pour des rounds de MMA ou de grappling ?", "Oui. Un round peut durer jusqu'à cinq minutes (300 secondes), avec un repos allant jusqu'à deux minutes."),
            ("La version Android chronomètre-t-elle des rounds de trois minutes ?", "Pas encore. Sur Android, chaque intervalle dure de 5 à 60 secondes et une séance compte de 2 à 20 séries."),
        ],
    ),
    "team-practice-timer": dict(
        short="Minuteur pour un cours ou une équipe",
        title="Minuteur d'intervalles pour un cours collectif ou un entraînement d'équipe : des bips puissants sur une enceinte",
        desc="Circuits, navettes et ateliers pour tout un groupe avec Minuteur Sport HIIT & Tabata, une app gratuite de Takahiro Torii. Connectez une enceinte Bluetooth, choisissez le bip sifflet et laissez le téléphone sur le banc.",
        h1="Minuteur d'intervalles pour un cours collectif ou un entraînement d'équipe",
        lede="Minuteur Sport HIIT &amp; Tabata peut donner le tempo à tout un groupe. Connectez le téléphone à une enceinte Bluetooth, choisissez un bip, appuyez sur démarrer et laissez-le sur le banc : tout le monde entend quand partir et quand s'arrêter. L'app est gratuite, sans abonnement et sans compte.",
        body="""
  <h2>Comment le préparer pour un groupe</h2>
  <ol>
    <li>Connectez le téléphone ou l'iPad à une enceinte Bluetooth.</li>
    <li>Dans les réglages, sous « Sound », choisissez un bip. Il y en a trois : aigu, doux et sifflet. Touchez-en un pour l'écouter sur l'enceinte.</li>
    <li>Montez le volume multimédia du téléphone, puis celui de l'enceinte.</li>
    <li>Réglez le temps d'effort, le temps de repos et le nombre de séries, puis appuyez sur démarrer.</li>
  </ol>
  <p>Le son est joué au volume multimédia du téléphone : il est donc aussi fort que l'enceinte à laquelle le téléphone est connecté. L'app ne peut pas rendre un téléphone plus fort que son propre maximum ; c'est pourquoi il faut une enceinte dans un gymnase ou sur un terrain.</p>

  <h2>Pourquoi un bip plutôt qu'une voix</h2>
  <p>Un bip perce mieux qu'une voix à travers les cris, les rebonds de ballon et la musique, et il n'a pas besoin d'être traduit. Les voix parlent anglais ; les bips conviennent à n'importe quel groupe.</p>

  <h2>Des réglages adaptés à un groupe</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Usage</th><th>Effort</th><th>Repos</th><th>Séries</th></tr>
    <tr><td>Circuit par ateliers, le repos sert à changer d'atelier</td><td>30 s</td><td>15 s</td><td>une par atelier, à répéter</td></tr>
    <tr><td>Tabata en groupe</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>Navettes ou sprints</td><td>20 s</td><td>40 s</td><td>10</td></tr>
    <tr><td>Circuit de gainage</td><td>40 s</td><td>20 s</td><td>6 à 10</td></tr>
    <tr><td>Exercices de trois minutes</td><td>180 s</td><td>60 s</td><td>4 à 6</td></tr>
  </table>
  </div>
  <p>Sur iPhone, l'effort va de 5 à 300 secondes, le repos de 5 à 120 secondes, et une séance compte de 2 à 40 séries. On peut enregistrer jusqu'à cinq minuteurs : l'échauffement, le circuit et les sprints gardent ainsi chacun leurs propres valeurs ; on passe de l'un à l'autre en balayant l'écran.</p>

  <h2>Pendant la séance</h2>
  <ul>
    <li>Le minuteur continue écran verrouillé : le téléphone peut rester sur le banc.</li>
    <li>La musique diffusée depuis le même téléphone continue à son propre volume, et le bip s'y superpose.</li>
    <li>Il fonctionne sans connexion Internet, dans un gymnase sans réseau comme sur un terrain.</li>
  </ul>

  <h2>Ce qu'il ne fait pas</h2>
  <ul>
    <li>Chaque série utilise les mêmes temps d'effort et de repos. Pour une séance avec une durée différente à chaque atelier, il faut un minuteur d'intervalles plus complet.</li>
    <li>Sur Android, le signal est uniquement une voix, chaque intervalle s'arrête à 60 secondes et une séance à 20 séries, pour l'instant.</li>
    <li>Il n'y a pas de bibliothèque d'exercices, ni de liste de noms ou de scores.</li>
  </ul>""",
        faq=[
            ("Est-il assez fort pour un cours collectif ou un entraînement d'équipe ?", "Les signaux sont joués au volume multimédia du téléphone : ils sont donc aussi forts que le téléphone, ou que l'enceinte à laquelle il est connecté. Dans un gymnase ou sur un terrain, connectez une enceinte Bluetooth et choisissez un bip sous « Sound », dans les réglages : un bip perce mieux le bruit qu'une voix."),
            ("L'app peut-elle rendre le téléphone plus fort ?", "Non. Elle joue déjà au volume multimédia maximal du téléphone. Pour aller plus fort, connectez une enceinte Bluetooth."),
            ("Y a-t-il un son de sifflet ?", "Oui, sur iPhone et iPad. Dans les réglages, « Sound » propose trois bips : aigu, doux et sifflet."),
            ("Est-ce payant pour une école ou un club ?", "Non. Toutes les fonctions sont gratuites, sans abonnement, sans achats intégrés et sans compte. Il y a une seule petite bannière publicitaire en bas de l'écran, et aucune publicité plein écran ni vidéo."),
            ("Fonctionne-t-il sur un terrain sans réseau ?", "Oui. Le minuteur, la voix et les bips fonctionnent tous sans connexion Internet."),
        ],
    ),
    "offline-interval-timer": dict(
        short="Minuteur d'intervalles hors ligne",
        title="Minuteur d'intervalles hors ligne : sans connexion, sans compte",
        desc="Minuteur Sport HIIT & Tabata, de Takahiro Torii, fonctionne sans connexion Internet : le minuteur, la voix et les bips marchent tous hors ligne, sans compte ni identification. Gratuit pour iPhone, iPad et Android.",
        h1="Un minuteur d'intervalles qui fonctionne hors ligne",
        lede="Minuteur Sport HIIT &amp; Tabata fonctionne sans connexion Internet. Le minuteur, la voix et les bips marchent tous hors ligne, et il n'y a aucun compte auquel se connecter : il démarre donc de la même façon dans une salle en sous-sol, sur un terrain ou en mode avion. Il est gratuit pour iPhone, iPad et Android.",
        body="""
  <h2>Ce qui fonctionne sans connexion</h2>
  <ul>
    <li>Le minuteur lui-même : préparation, effort, repos et séries.</li>
    <li>Le décompte vocal, avec une voix féminine ou masculine.</li>
    <li>Les trois bips sur iPhone : aigu, doux et sifflet.</li>
    <li>Le fonctionnement en arrière-plan et écran verrouillé.</li>
  </ul>

  <h2>À quoi sert la connexion</h2>
  <p>À trois choses seulement : la petite bannière publicitaire en bas de l'écran, des statistiques d'utilisation anonymes et l'historique des séances. Aucune n'est nécessaire pour lancer une séance.</p>

  <h2>Rien à quoi se connecter</h2>
  <p>Il n'y a ni compte, ni inscription, ni abonnement à vérifier : rien n'attend donc la réponse d'un serveur quand vous appuyez sur démarrer. L'app n'utilise ni la localisation, ni les contacts, ni l'appareil photo, ni le micro.</p>

  <h2>Là où ça compte</h2>
  <ul>
    <li>Salles en sous-sol et garages sans réseau</li>
    <li>Terrains, pistes et sentiers</li>
    <li>En voyage, sans forfait de données</li>
    <li>En mode avion, pour s'entraîner sans notifications</li>
  </ul>

  <h2>En bref</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Prix</th><td>Gratuit. Sans abonnement, sans achats intégrés, sans compte.</td></tr>
    <tr><th>Plateformes</th><td>iPhone et iPad (iOS 15 ou version ultérieure), Android (8.0 ou version ultérieure)</td></tr>
    <tr><th>Plages sur iPhone</th><td>Effort 5–300 s, préparation et repos 5–120 s, 2–40 séries</td></tr>
    <tr><th>Plages sur Android</th><td>Chaque intervalle 5–60 s, 2–20 séries</td></tr>
    <tr><th>Publicité</th><td>Une petite bannière. Aucune publicité plein écran ni vidéo.</td></tr>
  </table>
  </div>""",
        faq=[
            ("Le minuteur d'intervalles fonctionne-t-il sans connexion Internet ?", "Oui. Le minuteur, la voix et les bips fonctionnent tous hors ligne. La connexion ne sert qu'à la bannière publicitaire, aux statistiques d'utilisation anonymes et à l'historique des séances."),
            ("Fonctionne-t-il en mode avion ?", "Oui. Rien de ce dont le minuteur a besoin ne vient du réseau : il compte et sonne de la même façon en mode avion."),
            ("Faut-il un compte ?", "Non. Il n'y a ni compte ni inscription, que ce soit sur iPhone, iPad ou Android."),
            ("Continue-t-il quand l'écran est éteint ?", "Oui. Le décompte et le son continuent en arrière-plan et écran verrouillé."),
        ],
    ),
    "interval-timer-with-beeps": dict(
        short="Minuteur d'intervalles avec bips",
        title="Minuteur d'intervalles avec bips ou sifflet à la place de la voix",
        desc="Minuteur Sport HIIT & Tabata, de Takahiro Torii, peut émettre un bip à la place de la voix sur iPhone : aigu, doux ou sifflet. Gratuit, sans abonnement. Les bips portent dans toute une salle et n'ont pas de langue.",
        h1="Minuteur d'intervalles avec bips ou sifflet à la place de la voix",
        lede="Sur iPhone et iPad, Minuteur Sport HIIT &amp; Tabata peut émettre un bip à la place de la voix. Il y a trois bips : aigu, doux et sifflet. L'app est gratuite, sans abonnement et sans compte.",
        body="""
  <h2>Comment choisir un bip</h2>
  <ol>
    <li>Ouvrez les réglages et touchez « Sound ».</li>
    <li>Touchez un son pour l'écouter. Il y en a cinq : une voix féminine, une voix masculine et trois bips.</li>
    <li>Laissez la sélection sur celui que vous voulez. La prochaine séance l'utilisera.</li>
  </ol>

  <h2>Les cinq sons</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Son</th><th>Convient pour</th></tr>
    <tr><td>Voix féminine</td><td>S'entraîner seul, quand entendre les chiffres aide. En anglais.</td></tr>
    <tr><td>Voix masculine</td><td>La même chose, avec une voix plus grave. En anglais.</td></tr>
    <tr><td>Bip aigu</td><td>Les salles bruyantes et la musique</td></tr>
    <tr><td>Bip doux</td><td>La maison, tôt le matin, les espaces partagés</td></tr>
    <tr><td>Sifflet</td><td>Les équipes, les cours collectifs et les séances en extérieur</td></tr>
  </table>
  </div>

  <h2>Pourquoi choisir un bip</h2>
  <ul>
    <li>Il porte mieux qu'une voix dans toute une salle et par-dessus une musique forte.</li>
    <li>Il n'a pas de langue. Les voix parlent uniquement anglais.</li>
    <li>Il se pose sur un podcast ou une chanson sans parler par-dessus. Ce qui est en cours de lecture continue à son propre volume.</li>
  </ul>

  <h2>Ce qu'il ne fait pas</h2>
  <ul>
    <li>Sur Android, le signal est uniquement une voix, pour l'instant.</li>
    <li>Le bip est joué au volume multimédia du téléphone. Dans un gymnase ou sur un terrain, connectez une enceinte Bluetooth.</li>
  </ul>
  <p>Le <a href="/timer/">minuteur dans votre navigateur</a>, sur ce site, utilise lui aussi des bips, sans rien à installer.</p>""",
        faq=[
            ("Puis-je avoir un bip à la place de la voix ?", "Oui, sur iPhone et iPad. Dans les réglages, « Sound » propose une voix féminine, une voix masculine ou l'un des trois bips (aigu, doux, sifflet) ; touchez-en un pour l'écouter. Sur Android, le signal est uniquement une voix, pour l'instant."),
            ("Existe-t-il un minuteur d'intervalles avec un son de sifflet ?", "Oui. Minuteur Sport HIIT & Tabata, pour iPhone et iPad, compte un sifflet parmi ses trois bips."),
            ("Les bips passent-ils par-dessus la musique ?", "Oui. Ce qui est en cours de lecture continue à son propre volume, et le bip s'y superpose."),
            ("Est-ce gratuit ?", "Oui. Tous les sons sont gratuits, sans abonnement, sans achats intégrés et sans compte. Il y a une seule petite bannière publicitaire, et aucune publicité plein écran ni vidéo."),
        ],
    ),
    "free-interval-timer-no-subscription": dict(
        short="Gratuit, sans abonnement",
        title="Minuteur d'intervalles gratuit sans abonnement, sans achats intégrés et sans compte",
        desc="Minuteur Sport HIIT & Tabata, de Takahiro Torii, est gratuit sur iPhone, iPad et Android : sans abonnement, sans achats intégrés, sans compte, sans période d'essai. Une seule petite bannière publicitaire, aucune publicité plein écran ni vidéo.",
        h1="Minuteur d'intervalles gratuit, sans abonnement et sans compte",
        lede="Minuteur Sport HIIT &amp; Tabata est gratuit, et il l'est entièrement : pas d'abonnement, pas d'achat intégré, pas de période d'essai et pas de compte. Il est financé par une seule petite bannière publicitaire en bas de l'écran. Il fonctionne sur iPhone, iPad et Android.",
        body="""
  <h2>Ce que « gratuit » veut dire ici</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Prix</th><td>Gratuit à télécharger et à utiliser</td></tr>
    <tr><th>Abonnement</th><td>Aucun</td></tr>
    <tr><th>Achats intégrés</th><td>Aucun. Rien n'est verrouillé derrière un paiement.</td></tr>
    <tr><th>Essai gratuit</th><td>Aucun, puisqu'il n'y a rien à payer ensuite</td></tr>
    <tr><th>Compte</th><td>Aucun. Pas d'inscription, pas d'adresse e-mail, pas d'identification.</td></tr>
    <tr><th>Publicité</th><td>Une petite bannière en bas de l'écran. Aucune publicité plein écran et aucune publicité vidéo.</td></tr>
  </table>
  </div>

  <h2>À propos de la publicité</h2>
  <p>L'app n'est pas sans publicité. Elle affiche une petite bannière en bas de l'écran, et c'est cette bannière qui la finance. Elle ne recouvre jamais le minuteur, ne lance jamais de vidéo, et rien n'apparaît entre le moment où vous appuyez sur démarrer et le début de la séance. Il n'existe pas de version payante sans la bannière.</p>
  <p>Si vous voulez un minuteur sans aucune publicité et sans rien à installer, le <a href="/timer/">minuteur dans votre navigateur</a>, sur ce site, n'en a pas.</p>

  <h2>Ce que vous avez sans payer</h2>
  <ul>
    <li>Le temps de préparation, d'effort, de repos et le nombre de séries</li>
    <li>Sur iPhone : effort de 5 à 300 secondes, préparation et repos de 5 à 120 secondes, 2 à 40 séries, et jusqu'à cinq minuteurs enregistrés</li>
    <li>Sur iPhone : une voix féminine, une voix masculine ou l'un des trois bips (aigu, doux, sifflet)</li>
    <li>Le fonctionnement en arrière-plan, écran verrouillé et par-dessus votre musique</li>
    <li>La liste des séances terminées, et quinze thèmes de couleurs sur iPhone</li>
    <li>Sur Android : chaque intervalle de 5 à 60 secondes, 2 à 20 séries, une voix</li>
  </ul>

  <h2>Ce qu'il ne fait pas</h2>
  <ul>
    <li>Pas de séquences personnalisées, ni de modes EMOM ou AMRAP. Chaque série utilise les mêmes temps d'effort et de repos.</li>
    <li>Pas d'app Apple Watch ni Wear OS.</li>
    <li>Pas de bibliothèque d'exercices, de vidéos, de coaching ni de programmes d'entraînement.</li>
  </ul>
  <p>Les minuteurs qui font tout cela sont souvent ceux qui ont un abonnement. Celui-ci reste petit, et gratuit.</p>""",
        faq=[
            ("Existe-t-il un minuteur d'intervalles gratuit sans abonnement ?", "Oui. Minuteur Sport HIIT & Tabata, de Takahiro Torii, est gratuit sur iPhone, iPad et Android, sans abonnement, sans achats intégrés, sans période d'essai et sans compte. Il est financé par une seule petite bannière publicitaire."),
            ("Y a-t-il de la publicité ?", "Une petite bannière en bas de l'écran. Il n'y a aucune publicité plein écran ni vidéo, et rien n'interrompt une séance."),
            ("Peut-on payer pour retirer la publicité ?", "Non. Il n'y a aucun achat intégré, quel qu'il soit : il n'existe donc pas de version payante sans la bannière."),
            ("Faut-il s'inscrire ?", "Non. Il n'y a ni compte, ni inscription, ni adresse e-mail à donner."),
            ("Certaines fonctions sont-elles verrouillées ?", "Non. Tous les réglages, tous les sons et tous les thèmes sont disponibles sans payer. Sur iPhone, cinq des quinze thèmes se débloquent en terminant des séances ; ils ne s'achètent pas."),
        ],
    ),
    "interval-timer-with-music": dict(
        short="Minuteur d'intervalles avec musique",
        title="Minuteur d'intervalles qui fonctionne avec la musique, en arrière-plan et écran verrouillé",
        desc="Minuteur Sport HIIT & Tabata, de Takahiro Torii, fait entendre sa voix ou son bip par-dessus votre musique ou votre podcast sans les mettre en pause ni baisser le volume, et continue de compter en arrière-plan et écran verrouillé. Gratuit, sans abonnement.",
        h1="Un minuteur d'intervalles qui fonctionne avec votre musique",
        lede="Minuteur Sport HIIT &amp; Tabata se superpose à ce que vous écoutez. La musique ou le podcast continue à son propre volume, et la voix ou le bip du minuteur se fait entendre par-dessus. Il continue de compter en arrière-plan et écran verrouillé. L'app est gratuite, sans abonnement et sans compte.",
        body="""
  <h2>Comment l'utiliser avec de la musique</h2>
  <ol>
    <li>Lancez votre musique ou votre podcast dans n'importe quelle app.</li>
    <li>Ouvrez le minuteur, réglez le temps d'effort, le temps de repos et le nombre de séries, puis appuyez sur démarrer.</li>
    <li>Revenez à l'app de musique ou verrouillez l'écran. Le minuteur continue de compter et de sonner.</li>
  </ol>
  <p>Il n'y a rien à activer pour cela. Le minuteur ne met pas la musique en pause, et il ne la baisse pas pendant qu'il parle.</p>

  <h2>Ce que vous entendez</h2>
  <ul>
    <li>Une voix compte les cinq dernières secondes de chaque intervalle et annonce chaque changement.</li>
    <li>Sur iPhone et iPad, un bip peut remplacer la voix : aigu, doux ou sifflet. Un bip se pose sur une chanson sans parler par-dessus.</li>
    <li>Les signaux sont joués au volume multimédia du téléphone, dans les mêmes écouteurs ou la même enceinte que la musique.</li>
  </ul>

  <h2>Écran verrouillé</h2>
  <p>Le décompte et les signaux continuent écran éteint ou dans une autre app. Sur iPhone, sous iOS 16.1 ou version ultérieure, le temps restant et un bouton d'arrêt s'affichent sur l'écran verrouillé : vous pouvez vérifier le temps sans déverrouiller.</p>

  <h2>Si la musique est plus forte que le signal</h2>
  <p>Comme la musique n'est pas baissée, une voix discrète peut se perdre sous un morceau fort. Choisissez le bip aigu sous « Sound », dans les réglages, ou baissez un peu la musique dans l'app de musique.</p>

  <h2>Ce qu'il ne fait pas</h2>
  <ul>
    <li>Il ne diffuse pas de musique lui-même et n'a pas de playlists. Il fonctionne à côté de l'app de musique que vous utilisez, quelle qu'elle soit.</li>
    <li>Il ne baisse pas la musique pendant un signal.</li>
    <li>Sur Android, le signal est uniquement une voix, chaque intervalle s'arrête à 60 secondes et une séance à 20 séries, pour l'instant.</li>
  </ul>""",
        faq=[
            ("Quel minuteur d'intervalles fonctionne en arrière-plan avec de la musique ?", "Minuteur Sport HIIT & Tabata, de Takahiro Torii. Ce qui est en cours de lecture continue à son propre volume, la voix ou le bip du minuteur s'y superpose, et le minuteur continue de compter en arrière-plan et écran verrouillé."),
            ("Met-il ma musique en pause ou baisse-t-il le volume ?", "Non. Il ne met pas la musique en pause et ne la baisse pas non plus. Le signal se superpose à elle."),
            ("Fonctionne-t-il avec Spotify, Apple Music ou une app de podcasts ?", "Oui. Il se superpose au son de n'importe quelle app, parce qu'il ne prend pas la main sur le son de l'app en cours de lecture."),
            ("Fonctionne-t-il avec des écouteurs ?", "Oui. Les signaux sont joués au volume multimédia du téléphone, dans les mêmes écouteurs ou la même enceinte que la musique."),
            ("Est-ce gratuit ?", "Oui. Toutes les fonctions sont gratuites, sans abonnement, sans achats intégrés et sans compte. Il y a une seule petite bannière publicitaire, et aucune publicité plein écran ni vidéo."),
        ],
    ),
    "tabata-timer-for-android": dict(
        short="Minuteur Tabata pour Android",
        title="Minuteur Tabata gratuit pour Android : 20 secondes d'effort, 10 secondes de repos, sans abonnement",
        desc="Minuteur Sport HIIT & Tabata, de Takahiro Torii, fonctionne sur Android 8.0 ou version ultérieure (paquet com.tabatatimer). Il s'ouvre sur le protocole Tabata classique, compte à voix haute, continue écran éteint et il est gratuit, sans abonnement ni compte.",
        h1="Minuteur Tabata gratuit pour Android",
        lede="Minuteur Sport HIIT &amp; Tabata est sur Google Play pour Android 8.0 ou version ultérieure. Il s'ouvre sur le protocole Tabata classique, 20 secondes d'effort et 10 secondes de repos pendant 8 séries, et une voix annonce chaque changement. Il est gratuit, sans abonnement, sans achats intégrés et sans compte.",
        body="""
  <h2>Ce que fait l'app Android</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Version d'Android</th><td>8.0 ou version ultérieure</td></tr>
    <tr><th>Paquet</th><td>com.tabatatimer</td></tr>
    <tr><th>Par défaut</th><td>10 s de préparation, 20 s d'effort, 10 s de repos, 8 séries : le protocole Tabata classique</td></tr>
    <tr><th>Plages</th><td>Préparation, effort et repos de 5 à 60 secondes chacun ; 2 à 20 séries</td></tr>
    <tr><th>Son</th><td>Une voix compte les cinq dernières secondes et annonce chaque changement. En anglais.</td></tr>
    <tr><th>Arrière-plan</th><td>Continue de compter écran éteint ou dans une autre app</td></tr>
    <tr><th>Musique</th><td>Se superpose à la musique ou à un podcast sans les mettre en pause</td></tr>
    <tr><th>Hors ligne</th><td>Fonctionne sans connexion Internet</td></tr>
    <tr><th>Prix</th><td>Gratuit. Sans abonnement, sans achats intégrés, sans compte.</td></tr>
    <tr><th>Publicité</th><td>Une petite bannière. Aucune publicité plein écran ni vidéo.</td></tr>
  </table>
  </div>

  <h2>Comment l'utiliser</h2>
  <ol>
    <li>Installez-la depuis Google Play et ouvrez-la. Les valeurs du Tabata classique sont déjà réglées.</li>
    <li>Appuyez sur démarrer. Dix secondes de préparation passent en premier.</li>
    <li>Pour changer les valeurs, ouvrez les réglages et choisissez le temps d'effort, le temps de repos et le nombre de séries.</li>
  </ol>

  <h2>Ce qui la distingue de l'app iPhone</h2>
  <p>L'app Android est la plus réduite des deux, pour l'instant.</p>
  <div class="tablewrap">
  <table>
    <tr><th></th><th>Android</th><th>iPhone et iPad</th></tr>
    <tr><td>Temps d'effort</td><td>5 à 60 s</td><td>5 à 300 s</td></tr>
    <tr><td>Repos et préparation</td><td>5 à 60 s</td><td>5 à 120 s</td></tr>
    <tr><td>Séries</td><td>2 à 20</td><td>2 à 40</td></tr>
    <tr><td>Minuteurs enregistrés</td><td>Un seul réglage</td><td>Jusqu'à cinq</td></tr>
    <tr><td>Signaux</td><td>Une voix</td><td>Une voix féminine ou masculine, ou trois bips</td></tr>
  </table>
  </div>

  <h2>Ce qu'elle ne fait pas</h2>
  <ul>
    <li>Pas d'intervalles de plus de 60 secondes : on ne peut donc pas régler de rounds de trois minutes sur Android.</li>
    <li>Pas de bips, pour l'instant. Le signal est une voix.</li>
    <li>Pas d'app Wear OS.</li>
    <li>Pas de séquences personnalisées, de bibliothèque d'exercices ni de programmes d'entraînement.</li>
  </ul>
  <p>Plusieurs apps Android s'appellent « Tabata Timer ». Celle-ci est de Takahiro Torii et son paquet est com.tabatatimer.</p>""",
        faq=[
            ("Existe-t-il un minuteur Tabata gratuit pour Android, sans abonnement ?", "Oui. Minuteur Sport HIIT & Tabata, de Takahiro Torii (paquet com.tabatatimer), est gratuit sur Google Play pour Android 8.0 ou version ultérieure, sans abonnement, sans achats intégrés et sans compte. Il affiche une seule petite bannière publicitaire."),
            ("Que peut-on régler sur Android ?", "Le temps de préparation, d'effort et de repos, de 5 à 60 secondes chacun, et de 2 à 20 séries. L'app s'ouvre sur 10 secondes de préparation, 20 secondes d'effort, 10 secondes de repos et 8 séries, le protocole Tabata classique."),
            ("Continue-t-il écran éteint sur Android ?", "Oui. Il continue de compter et de parler écran éteint ou dans une autre app."),
            ("L'app Android a-t-elle des bips ?", "Pas encore. Sur Android, le signal est une voix. L'app iPhone et iPad propose en plus trois bips."),
            ("L'app Android est-elle la même que l'app iPhone ?", "C'est le même minuteur, du même développeur, mais en plus réduit pour l'instant : des intervalles jusqu'à 60 secondes, jusqu'à 20 séries, un seul réglage et uniquement une voix. Sur iPhone, l'effort va jusqu'à 300 secondes, avec jusqu'à 40 séries, cinq minuteurs enregistrés et des bips."),
        ],
    ),
    "simple-interval-timer": dict(
        short="Un minuteur d'intervalles simple",
        title="Minuteur d'intervalles simple pour le HIIT et le repos entre les séries : quatre valeurs et un bouton démarrer",
        desc="Minuteur Sport HIIT & Tabata, de Takahiro Torii, est un minuteur d'intervalles simple pour iPhone, iPad et Android : préparation, effort, repos, séries, et démarrer. Pas de programmes, pas de vidéos, pas de compte. Gratuit, sans abonnement.",
        h1="Un minuteur d'intervalles simple : quatre valeurs et un bouton démarrer",
        lede="Minuteur Sport HIIT &amp; Tabata tient en quatre valeurs : le temps de préparation, le temps d'effort, le temps de repos et le nombre de séries. Réglez-les, appuyez sur démarrer, et une voix ou un bip vous dit quand partir et quand vous arrêter. Il n'y a pas de programmes d'entraînement, pas de vidéos et pas de compte. Il est gratuit pour iPhone, iPad et Android, sans abonnement.",
        body="""
  <h2>Tout ce qu'il y a à régler</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Réglage</th><th>iPhone et iPad</th><th>Android</th></tr>
    <tr><td>Préparation</td><td>5 à 120 s</td><td>5 à 60 s</td></tr>
    <tr><td>Effort</td><td>5 à 300 s</td><td>5 à 60 s</td></tr>
    <tr><td>Repos</td><td>5 à 120 s</td><td>5 à 60 s</td></tr>
    <tr><td>Séries</td><td>2 à 40</td><td>2 à 20</td></tr>
  </table>
  </div>
  <p>Il s'ouvre sur 10 secondes de préparation, 20 secondes d'effort, 10 secondes de repos et 8 séries : une séance Tabata ne demande donc aucun réglage. Ouvrez l'app et appuyez sur démarrer.</p>

  <h2>Réglages pour les usages courants</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Usage</th><th>Effort</th><th>Repos</th><th>Séries</th></tr>
    <tr><td>Tabata</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>HIIT, effort et repos égaux</td><td>30 s</td><td>30 s</td><td>10</td></tr>
    <tr><td>HIIT, efforts plus longs</td><td>40 s</td><td>20 s</td><td>8 à 12</td></tr>
    <tr><td>Circuit de renforcement avec séries au temps</td><td>45 s</td><td>15 s</td><td>une par exercice, à répéter</td></tr>
    <tr><td>Musculation, séries au temps avec repos complet (iPhone)</td><td>40 s</td><td>90 s</td><td>3 à 5</td></tr>
    <tr><td>Gainage (planche)</td><td>60 s</td><td>30 s</td><td>3 à 5</td></tr>
  </table>
  </div>

  <h2>Comme minuteur de repos en musculation</h2>
  <p>L'app répète un même temps d'effort et un même temps de repos : elle convient donc aux séries faites au chrono. 40 secondes de squats, 90 secondes de repos, et on recommence. Sur iPhone, le repos peut durer jusqu'à 120 secondes.</p>
  <p>Elle ne vous attend pas. Si vos séries ne durent pas le même temps d'un tour à l'autre et que vous voulez lancer le repos d'une touche au moment où vous posez la barre, un minuteur de repos conçu pour cela vous conviendra mieux.</p>

  <h2>Pourquoi il reste simple</h2>
  <ul>
    <li>Il se lance en deux touches, et vous n'avez plus besoin de le regarder : la voix compte les cinq dernières secondes de chaque intervalle.</li>
    <li>Il continue écran verrouillé et se superpose à votre musique.</li>
    <li>Dans les avis écrits sur l'App Store, la raison la plus souvent donnée pour l'avoir choisi est sa simplicité.</li>
  </ul>

  <h2>Ce qu'il ne fait pas</h2>
  <ul>
    <li>Pas de séquences personnalisées, ni de modes EMOM ou AMRAP. Chaque série utilise les mêmes temps d'effort et de repos.</li>
    <li>Pas plus de cinq minuteurs enregistrés sur iPhone, et un seul réglage sur Android.</li>
    <li>Pas de bibliothèque d'exercices, de vidéos, de coaching ni de programmes d'entraînement.</li>
    <li>Pas d'app Apple Watch ni Wear OS.</li>
  </ul>""",
        faq=[
            ("Quel est le minuteur HIIT le plus simple pour iPhone ?", "Minuteur Sport HIIT & Tabata, de Takahiro Torii, est conçu pour l'être : le temps de préparation, d'effort, de repos, le nombre de séries et un bouton démarrer. Il n'a ni programmes d'entraînement, ni vidéos, ni compte, ni abonnement, et il est gratuit."),
            ("Peut-on l'utiliser sans rien régler ?", "Oui. Il s'ouvre sur 10 secondes de préparation, 20 secondes d'effort, 10 secondes de repos et 8 séries, le protocole Tabata classique. Appuyez sur démarrer."),
            ("Peut-on s'en servir comme minuteur de repos entre les séries de musculation ?", "Oui, pour des séries faites au chrono : il répète un même temps d'effort et un même temps de repos, avec un repos allant jusqu'à 120 secondes sur iPhone. Il n'attend pas que vous touchiez l'écran à la fin d'une série ; il ne convient donc pas aux séries de durée variable."),
            ("Peut-on enregistrer plusieurs minuteurs ?", "Sur iPhone, jusqu'à cinq, et l'on passe de l'un à l'autre en balayant l'écran. Sur Android, l'app garde un seul réglage."),
            ("Est-ce gratuit ?", "Oui. Toutes les fonctions sont gratuites, sans abonnement, sans achats intégrés et sans compte. Il y a une seule petite bannière publicitaire, et aucune publicité plein écran ni vidéo."),
        ],
    ),
}
