#!/usr/bin/env python3
"""Writes the pages that answer one question each: boxing rounds, a class or
a team, no connection, a beep instead of a voice, free with no subscription,
music playing, Android, the simplest timer, and a comparison with other apps.

    python3 build_uses.py .

Each page exists in English and Japanese, written here, and in French and
German, translated from the English in uses_fr.py and uses_de.py. It says only what the main pages
already say about the app, arranged around the one use. When a fact changes
on the main pages, change it here too and run this again.
"""
import html
import json
import sys
from pathlib import Path

SITE = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
BASE = "https://simpletabata.com"
UPDATED = {"en": "26 November 2026", "ja": "2026年11月26日", "fr": "26 novembre 2026", "de": "26. November 2026"}
MODIFIED = {"en": "2026-11-26", "ja": "2026-11-26", "fr": "2026-11-26", "de": "2026-11-26"}
LANGS = ("en", "ja", "fr", "de")
NAMES = {"en": "English", "ja": "日本語", "fr": "Français", "de": "Deutsch"}

STYLE = """  :root { --ink:#1c1c1e; --muted:#6b6b70; --rule:#e4e4e7; --bg:#fff; --accent:#c9b817; --card:#f6f6f7; }
  @media (prefers-color-scheme: dark) {
    :root { --ink:#ececef; --muted:#9a9aa0; --rule:#303034; --bg:#131315; --card:#1c1c20; }
  }
  * { box-sizing:border-box; }
  body {
    margin:0; padding:3rem 1.25rem 5rem;
    background:var(--bg); color:var(--ink);
    font:16px/1.75 -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Noto Sans JP", sans-serif;
  }
  main { max-width:44rem; margin:0 auto; }
  .lang { font-size:.875rem; color:var(--muted); margin:0 0 2.5rem; }
  .lang a { display:inline-block; margin-right:.75rem; }
  header { display:flex; gap:1.25rem; align-items:center; margin:0 0 1.5rem; }
  header img { width:64px; height:64px; border-radius:15px; flex:none; }
  h1 { font-size:1.5rem; line-height:1.35; margin:0 0 .25rem; letter-spacing:-.01em; }
  .by { color:var(--muted); font-size:.9rem; margin:0; }
  .lede { font-size:1.1rem; }
  h2 { font-size:1.1rem; margin:2.75rem 0 .6rem; padding-top:1.5rem; border-top:1px solid var(--rule); }
  h3 { font-size:1rem; margin:1.6rem 0 .3rem; }
  ul, ol { padding-left:1.25rem; }
  li { margin:.4rem 0; }
  a { color:inherit; text-decoration-color:var(--accent); text-underline-offset:3px; }
  .get { display:flex; flex-wrap:wrap; gap:.75rem; margin:1.75rem 0 0; }
  .get a {
    display:inline-block; padding:.6rem 1.1rem; border-radius:10px;
    background:var(--ink); color:var(--bg); text-decoration:none; font-weight:600; font-size:.95rem;
  }
  .tablewrap { overflow-x:auto; }
  table { border-collapse:collapse; width:100%; margin:1rem 0; font-size:.92rem; }
  th, td { text-align:left; padding:.55rem .6rem; border-bottom:1px solid var(--rule); vertical-align:top; }
  th { font-weight:600; color:var(--muted); }
  tr > th:first-child { min-width:5.5em; }
  footer { margin-top:4rem; padding-top:1.5rem; border-top:1px solid var(--rule); color:var(--muted); font-size:.85rem; }
  footer a { margin-right:1rem; }"""

UI = {
    "en": dict(
        home="/", app="Tabata &amp; HIIT Interval Timer", app_plain="Tabata & HIIT Interval Timer",
        by="by Takahiro Torii · iPhone, iPad and Android · free",
        ios="Download on the App Store", ios_url="https://apps.apple.com/app/id1166542235",
        play="Get it on Google Play",
        questions="Questions", related="Other uses", get="Get the app",
        about="About the app", timer="Timer in your browser", timer_url="/timer/",
        privacy="Privacy Policy", contact="Contact", updated="Last updated",
        alt="Tabata &amp; HIIT Interval Timer app icon",
    ),
    "ja": dict(
        home="/ja/", app="HIIT &amp; Tabata Timer - タバタタイマー", app_plain="HIIT & Tabata Timer - タバタタイマー",
        by="開発: Takahiro Torii ・ iPhone / iPad / Android ・ 無料",
        ios="App Store でダウンロード", ios_url="https://apps.apple.com/jp/app/id1166542235",
        play="Google Play で入手",
        questions="よくある質問", related="ほかの使い方", get="ダウンロード",
        about="アプリの説明", timer="ブラウザ版タイマー", timer_url="/timer/ja/",
        privacy="プライバシーポリシー", contact="お問い合わせ", updated="最終更新",
        alt="HIIT &amp; Tabata Timer - タバタタイマー のアイコン",
    ),
    "fr": dict(
        home="/fr/", app="Minuteur Sport HIIT &amp; Tabata", app_plain="Minuteur Sport HIIT & Tabata",
        by="par Takahiro Torii · iPhone, iPad et Android · gratuit",
        ios="Télécharger dans l'App Store", ios_url="https://apps.apple.com/fr/app/id1166542235",
        play="Disponible sur Google Play",
        questions="Questions", related="Autres usages", get="Obtenir l'app",
        about="Présentation de l'app", timer="Minuteur dans le navigateur (en anglais)", timer_url="/timer/",
        privacy="Politique de confidentialité", contact="Contact", updated="Dernière mise à jour :",
        alt="Icône de l'app Minuteur Sport HIIT &amp; Tabata",
    ),
    "de": dict(
        home="/de/", app="Intervall-Timer HIIT &amp; Tabata", app_plain="Intervall-Timer HIIT & Tabata",
        by="von Takahiro Torii · iPhone, iPad und Android · kostenlos",
        ios="Laden im App Store", ios_url="https://apps.apple.com/de/app/id1166542235",
        play="Jetzt bei Google Play",
        questions="Fragen", related="Weitere Einsatzzwecke", get="App laden",
        about="Über die App", timer="Timer im Browser (auf Englisch)", timer_url="/timer/",
        privacy="Datenschutzerklärung", contact="Kontakt", updated="Zuletzt aktualisiert:",
        alt="App-Symbol von Intervall-Timer HIIT &amp; Tabata",
    ),
}

# slug -> language -> page. "body" is HTML; "faq" is plain text, used both on
# the page and in the structured data.
PAGES = {
    "boxing-round-timer": {
        "en": dict(
            short="Boxing round timer",
            title="A free boxing round timer for iPhone: three-minute rounds, one-minute rests",
            desc="Set three-minute rounds with a one-minute rest in Tabata & HIIT Interval Timer, a free app by Takahiro Torii. Rounds up to five minutes, up to 40 rounds, a voice or a beep, no subscription.",
            h1="A free boxing round timer: three-minute rounds, one-minute rests",
            lede="Tabata &amp; HIIT Interval Timer times boxing rounds on iPhone and iPad. A round can be up to five minutes and a rest up to two, for 2 to 40 rounds, so three-minute rounds with a one-minute rest can be set directly. It is free, with no subscription and no account.",
            body="""
  <h2>How to set it</h2>
  <ol>
    <li>Open Settings and set the work time to 180 seconds. That is one round.</li>
    <li>Set the rest time to 60 seconds.</li>
    <li>Set the number of sets to the number of rounds, for example 12.</li>
    <li>Press start. The ready time, 10 seconds by default, runs first.</li>
  </ol>
  <p>The phone can go in a pocket or on the floor. The timer keeps running with the screen locked, and on iOS 16.1 or later the remaining time shows on the Lock Screen.</p>

  <h2>Common round settings</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Use</th><th>Work</th><th>Rest</th><th>Sets</th></tr>
    <tr><td>Three-minute rounds</td><td>180 s</td><td>60 s</td><td>3 to 12</td></tr>
    <tr><td>Two-minute rounds</td><td>120 s</td><td>60 s</td><td>3 to 6</td></tr>
    <tr><td>Five-minute rounds, for grappling or MMA</td><td>300 s</td><td>60 s</td><td>3 to 5</td></tr>
    <tr><td>Heavy bag intervals</td><td>30 s</td><td>30 s</td><td>10 to 20</td></tr>
    <tr><td>Skipping</td><td>60 s</td><td>20 s</td><td>10</td></tr>
  </table>
  </div>
  <p>Work time can be 5 to 60 seconds in steps of five, 70 to 120 in steps of ten, or 150, 180, 210, 240, 270 or 300 seconds. Rest and ready time stop at 120 seconds.</p>
  <p>Up to five timers can be saved on iPhone, so sparring rounds, bag work and skipping can each keep their own numbers. Swipe left or right on the main screen to switch.</p>

  <h2>Hearing it in a gym</h2>
  <p>Under Sound in Settings, choose a female voice, a male voice, or one of three beeps: sharp, soft or whistle. A beep carries further than a voice over bags and music. The sound plays at the phone's media volume, so a Bluetooth speaker makes it as loud as the speaker. Music keeps playing underneath at its own volume.</p>

  <h2>What it does not do</h2>
  <ul>
    <li>Every round is the same length, and every rest is the same length. A session with rounds of different lengths needs a fuller interval timer.</li>
    <li>On Android each interval stops at 60 seconds, so three-minute rounds are iPhone and iPad only, for now.</li>
    <li>There is no Apple Watch app.</li>
    <li>The spoken cues are in English. The beeps have no language.</li>
  </ul>""",
            faq=[
                ("Can it time three-minute boxing rounds?", "Yes, on iPhone and iPad. Set the work time to 180 seconds and the rest time to 60 seconds, and set the number of sets to the number of rounds. Work time goes up to 300 seconds, rest up to 120 seconds, and there can be 2 to 40 rounds."),
                ("Is the boxing round timer free?", "Yes. Every feature is free, with no subscription, no in-app purchases and no account. There is one small banner ad at the bottom of the screen and no full-screen or video ads."),
                ("Does it keep timing rounds with the screen locked?", "Yes. It keeps counting and sounding in the background and with the screen locked. On iPhone with iOS 16.1 or later the remaining time and a stop button show on the Lock Screen."),
                ("Can I use it for MMA or grappling rounds?", "Yes. A round can be up to five minutes (300 seconds) with a rest of up to two minutes."),
                ("Does the Android version time three-minute rounds?", "Not yet. On Android each interval is 5 to 60 seconds and a workout is 2 to 20 sets."),
            ],
        ),
        "ja": dict(
            short="ボクシングのラウンドタイマー",
            title="ボクシングの3分ラウンドを計れる無料タイマー（iPhone）｜タバタタイマー",
            desc="HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）で、3分ラウンド・1分休憩をそのまま設定できます。1ラウンド最大5分、最大40ラウンド、音声またはビープ音。無料、サブスクなし。",
            h1="ボクシングの3分ラウンドを計れる無料タイマー",
            lede="HIIT &amp; Tabata Timer - タバタタイマー は、iPhone と iPad でボクシングのラウンドを計れます。1ラウンドは最大5分、休憩は最大2分、ラウンド数は2〜40なので、3分ラウンド・1分休憩をそのまま設定できます。無料で、サブスクリプションもアカウント登録もありません。",
            body="""
  <h2>設定のしかた</h2>
  <ol>
    <li>設定を開き、運動時間を180秒にします。これが1ラウンドです。</li>
    <li>休憩時間を60秒にします。</li>
    <li>セット数をラウンド数にします。たとえば12です。</li>
    <li>スタートを押します。最初に準備時間（初期設定は10秒）が流れます。</li>
  </ol>
  <p>スマートフォンはポケットに入れても床に置いてもかまいません。画面をロックしても動き続け、iOS 16.1 以降ではロック画面に残り時間が出ます。</p>

  <h2>よく使われる設定</h2>
  <div class="tablewrap">
  <table>
    <tr><th>用途</th><th>運動</th><th>休憩</th><th>セット数</th></tr>
    <tr><td>3分ラウンド</td><td>180秒</td><td>60秒</td><td>3〜12</td></tr>
    <tr><td>2分ラウンド</td><td>120秒</td><td>60秒</td><td>3〜6</td></tr>
    <tr><td>5分ラウンド（グラップリング、総合格闘技）</td><td>300秒</td><td>60秒</td><td>3〜5</td></tr>
    <tr><td>サンドバッグのインターバル</td><td>30秒</td><td>30秒</td><td>10〜20</td></tr>
    <tr><td>縄跳び</td><td>60秒</td><td>20秒</td><td>10</td></tr>
  </table>
  </div>
  <p>運動時間は、5〜60秒が5秒刻み、70〜120秒が10秒刻み、その先は150・180・210・240・270・300秒から選べます。休憩時間と準備時間は120秒までです。</p>
  <p>iPhone ではタイマーを5つまで保存できるので、スパーリング用、サンドバッグ用、縄跳び用と別々の秒数を持たせられます。メイン画面を左右にスワイプして切り替えます。</p>

  <h2>ジムで聞こえるようにする</h2>
  <p>設定の「Sound」で、女性の声・男性の声・3種類のビープ音（シャープ、ソフト、ホイッスル）から選べます。ビープ音は、サンドバッグの音や音楽の中でも声より通ります。音はスマートフォンのメディア音量で鳴るので、Bluetooth スピーカーにつなげばスピーカーの音量で鳴ります。流している音楽は止まらず、音量もそのままです。</p>

  <h2>できないこと</h2>
  <ul>
    <li>すべてのラウンドが同じ長さ、すべての休憩が同じ長さです。ラウンドごとに長さを変えたい場合は、多機能なインターバルタイマーが向いています。</li>
    <li>Android 版は各区間が60秒までなので、3分ラウンドは今のところ iPhone と iPad だけです。</li>
    <li>Apple Watch のアプリはありません。</li>
    <li>掛け声は英語です。ビープ音は言語に関係なく使えます。</li>
  </ul>""",
            faq=[
                ("ボクシングの3分ラウンドを計れますか？", "はい、iPhone と iPad で計れます。運動時間を180秒、休憩時間を60秒にして、セット数をラウンド数に合わせます。運動時間は300秒まで、休憩は120秒まで、ラウンド数は2〜40です。"),
                ("無料で使えますか？", "はい。すべての機能が無料で、サブスクリプション・アプリ内課金・アカウント登録はありません。広告は画面下の小さなバナー1つだけで、全画面広告や動画広告は出ません。"),
                ("画面をロックしてもラウンドを計り続けますか？", "はい。バックグラウンドでも画面ロック中でも、カウントと音は続きます。iOS 16.1 以降の iPhone では、ロック画面に残り時間と停止ボタンが出ます。"),
                ("総合格闘技やグラップリングの5分ラウンドにも使えますか？", "はい。1ラウンドは最大5分（300秒）、休憩は最大2分まで設定できます。"),
                ("Android 版で3分ラウンドは計れますか？", "まだ計れません。Android 版は各区間が5〜60秒、セット数は2〜20です。"),
            ],
        ),
    },
    "team-practice-timer": {
        "en": dict(
            short="Timer for a class or a team",
            title="An interval timer for a class or a team practice: loud beeps through a speaker",
            desc="Run circuits, shuttles and stations for a whole group with Tabata & HIIT Interval Timer, a free app by Takahiro Torii. Connect a Bluetooth speaker, choose a whistle beep, and leave the phone on the bench.",
            h1="An interval timer for a class or a team practice",
            lede="Tabata &amp; HIIT Interval Timer can run the clock for a whole group. Connect the phone to a Bluetooth speaker, choose a beep, press start and leave it on the bench: everyone hears when to go and when to stop. It is free, with no subscription and no account.",
            body="""
  <h2>How to set it up for a group</h2>
  <ol>
    <li>Connect the phone or iPad to a Bluetooth speaker.</li>
    <li>In Settings, under Sound, choose a beep. There are three: sharp, soft and whistle. Tap one to hear it through the speaker.</li>
    <li>Turn up the media volume on the phone and then on the speaker.</li>
    <li>Set the work time, the rest time and the number of sets, and press start.</li>
  </ol>
  <p>The sound plays at the phone's media volume, so it is as loud as the speaker it is connected to. The app cannot make a phone louder than its own maximum, which is why a hall or a pitch needs a speaker.</p>

  <h2>Why a beep and not a voice</h2>
  <p>A beep cuts through shouting, bouncing balls and music better than a voice, and it needs no translation. The voices speak English; the beeps work for any group.</p>

  <h2>Settings that suit a group</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Use</th><th>Work</th><th>Rest</th><th>Sets</th></tr>
    <tr><td>Station circuit, rest is the change-over</td><td>30 s</td><td>15 s</td><td>one per station, repeated</td></tr>
    <tr><td>Tabata as a group</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>Shuttle runs or sprints</td><td>20 s</td><td>40 s</td><td>10</td></tr>
    <tr><td>Core circuit</td><td>40 s</td><td>20 s</td><td>6 to 10</td></tr>
    <tr><td>Three-minute drills</td><td>180 s</td><td>60 s</td><td>4 to 6</td></tr>
  </table>
  </div>
  <p>On iPhone, work time goes from 5 to 300 seconds, rest from 5 to 120 seconds, and a session can be 2 to 40 sets. Up to five timers can be saved, so the warm-up, the circuit and the sprints can each keep their own numbers; swipe to switch between them.</p>

  <h2>During the session</h2>
  <ul>
    <li>The timer keeps running with the screen locked, so the phone can stay on the bench.</li>
    <li>Music from the same phone keeps playing at its own volume, with the beep over it.</li>
    <li>It works without an internet connection, in a gym with no signal or on a field.</li>
  </ul>

  <h2>What it does not do</h2>
  <ul>
    <li>Every set uses the same work and rest time. A session with a different length for each station needs a fuller interval timer.</li>
    <li>On Android the cues are a voice only, each interval stops at 60 seconds and a session at 20 sets, for now.</li>
    <li>There is no exercise library, and no list of names or scores.</li>
  </ul>""",
            faq=[
                ("Is it loud enough for a class or a team practice?", "The cues play at the phone's media volume, so they are as loud as the phone or the speaker it is connected to. For a hall or a pitch, connect a Bluetooth speaker and choose a beep under Sound in Settings: a beep cuts through noise better than a voice."),
                ("Can the app make the phone louder?", "No. It already plays at the phone's maximum media volume. To go louder, connect a Bluetooth speaker."),
                ("Does it have a whistle sound?", "Yes, on iPhone and iPad. Under Sound in Settings there are three beeps: sharp, soft and whistle."),
                ("Does it cost anything for a school or a club?", "No. Every feature is free, with no subscription, no in-app purchases and no account. There is one small banner ad at the bottom of the screen and no full-screen or video ads."),
                ("Does it work on a field with no signal?", "Yes. The timer, the voice and the beeps all work without an internet connection."),
            ],
        ),
        "ja": dict(
            short="部活・クラス用のタイマー",
            title="部活やクラスで使えるインターバルタイマー｜スピーカーからホイッスル音｜タバタタイマー",
            desc="HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、サーキットやダッシュの合図を全員に聞かせられます。Bluetooth スピーカーにつないでホイッスル音を選ぶだけ。無料、登録なし。",
            h1="部活やクラスで使えるインターバルタイマー",
            lede="HIIT &amp; Tabata Timer - タバタタイマー は、チーム全員の合図として使えます。スマートフォンを Bluetooth スピーカーにつなぎ、ビープ音を選んでスタートを押したら、ベンチに置いておくだけです。始めと終わりが全員に聞こえます。無料で、サブスクリプションもアカウント登録もありません。",
            body="""
  <h2>大人数で使うときの準備</h2>
  <ol>
    <li>スマートフォンか iPad を Bluetooth スピーカーにつなぎます。</li>
    <li>設定の「Sound」でビープ音を選びます。シャープ、ソフト、ホイッスルの3種類があり、タップするとスピーカーから試聴できます。</li>
    <li>スマートフォンのメディア音量を上げ、次にスピーカーの音量を上げます。</li>
    <li>運動時間・休憩時間・セット数を決めて、スタートを押します。</li>
  </ol>
  <p>音はスマートフォンのメディア音量で鳴るので、大きさはつないだスピーカーしだいです。アプリの側で本体の最大音量より大きくすることはできません。体育館やグラウンドではスピーカーが必要です。</p>

  <h2>声よりビープ音がよい理由</h2>
  <p>ビープ音は、掛け声やボールの音、音楽の中でも声より通ります。掛け声は英語ですが、ビープ音なら誰にでも伝わります。</p>

  <h2>部活で使いやすい設定</h2>
  <div class="tablewrap">
  <table>
    <tr><th>用途</th><th>運動</th><th>休憩</th><th>セット数</th></tr>
    <tr><td>サーキット（休憩の間に移動）</td><td>30秒</td><td>15秒</td><td>種目数 × 周回数</td></tr>
    <tr><td>全員でタバタ式</td><td>20秒</td><td>10秒</td><td>8</td></tr>
    <tr><td>ダッシュ、シャトルラン</td><td>20秒</td><td>40秒</td><td>10</td></tr>
    <tr><td>体幹トレーニング</td><td>40秒</td><td>20秒</td><td>6〜10</td></tr>
    <tr><td>3分間の練習メニュー</td><td>180秒</td><td>60秒</td><td>4〜6</td></tr>
  </table>
  </div>
  <p>iPhone では、運動時間が5〜300秒、休憩時間が5〜120秒、セット数が2〜40です。タイマーは5つまで保存できるので、アップ用、サーキット用、ダッシュ用と分けておけます。スワイプで切り替えます。</p>

  <h2>練習中</h2>
  <ul>
    <li>画面をロックしても動き続けるので、ベンチに置いたままで大丈夫です。</li>
    <li>同じスマートフォンで流している音楽は止まらず、その上にビープ音が重なります。</li>
    <li>インターネットにつながっていなくても動きます。電波の届かない体育館やグラウンドでも使えます。</li>
  </ul>

  <h2>できないこと</h2>
  <ul>
    <li>すべてのセットが同じ運動時間・休憩時間です。種目ごとに秒数を変えたい場合は、多機能なインターバルタイマーが向いています。</li>
    <li>Android 版は今のところ音声のみで、各区間は60秒まで、セット数は20までです。</li>
    <li>種目の解説や、名前・記録をつける機能はありません。</li>
  </ul>""",
            faq=[
                ("部活やクラスで使える音量ですか？", "合図はスマートフォンのメディア音量で鳴るので、音の大きさは本体か、つないだスピーカーしだいです。体育館やグラウンドでは Bluetooth スピーカーにつなぎ、設定の「Sound」でビープ音を選ぶのがおすすめです。ビープ音は声より騒音の中で通ります。"),
                ("アプリで音量をもっと大きくできますか？", "できません。すでにスマートフォンのメディア音量の最大で鳴らしています。それより大きくするには、Bluetooth スピーカーにつないでください。"),
                ("ホイッスルの音はありますか？", "はい、iPhone と iPad にあります。設定の「Sound」で、シャープ、ソフト、ホイッスルの3種類のビープ音から選べます。"),
                ("学校や部活で使うのに料金はかかりますか？", "かかりません。すべての機能が無料で、サブスクリプション・アプリ内課金・アカウント登録はありません。広告は画面下の小さなバナー1つだけで、全画面広告や動画広告は出ません。"),
                ("電波の届かないグラウンドでも使えますか？", "はい。タイマーも音声もビープ音も、インターネットにつながっていなくても動きます。"),
            ],
        ),
    },
    "offline-interval-timer": {
        "en": dict(
            short="Offline interval timer",
            title="An interval timer that works offline: no connection, no account",
            desc="Tabata & HIIT Interval Timer by Takahiro Torii works without an internet connection: the timer, the voice and the beeps all run offline, with no account and no sign-in. Free for iPhone, iPad and Android.",
            h1="An interval timer that works offline",
            lede="Tabata &amp; HIIT Interval Timer works without an internet connection. The timer, the voice and the beeps all run offline, and there is no account to sign in to, so it starts the same way in a basement gym, on a field or in airplane mode. It is free for iPhone, iPad and Android.",
            body="""
  <h2>What works without a connection</h2>
  <ul>
    <li>The timer itself: ready time, work time, rest time and sets.</li>
    <li>The spoken countdown, in a female or a male voice.</li>
    <li>The three beeps on iPhone: sharp, soft and whistle.</li>
    <li>Running in the background and with the screen locked.</li>
  </ul>

  <h2>What a connection is used for</h2>
  <p>Only three things: the small banner ad at the bottom of the screen, anonymous usage statistics, and the workout history. None of them is needed to run a workout.</p>

  <h2>Nothing to sign in to</h2>
  <p>There is no account, no sign-up and no subscription to check, so nothing waits for a server when you press start. The app does not use location, contacts, the camera or the microphone.</p>

  <h2>Where that matters</h2>
  <ul>
    <li>Basement gyms and garages with no signal</li>
    <li>Fields, tracks and trails</li>
    <li>Travelling without a data plan</li>
    <li>Airplane mode, to train without notifications</li>
  </ul>

  <h2>At a glance</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Price</th><td>Free. No subscription, no in-app purchases, no account.</td></tr>
    <tr><th>Platforms</th><td>iPhone and iPad (iOS 15 or later), Android (8.0 or later)</td></tr>
    <tr><th>Ranges on iPhone</th><td>Work 5–300 s, ready and rest 5–120 s, 2–40 sets</td></tr>
    <tr><th>Ranges on Android</th><td>Each interval 5–60 s, 2–20 sets</td></tr>
    <tr><th>Ads</th><td>One small banner. No full-screen or video ads.</td></tr>
  </table>
  </div>""",
            faq=[
                ("Does the interval timer work without an internet connection?", "Yes. The timer, the voice and the beeps all work offline. A connection is used only for the banner ad, anonymous usage statistics and the workout history."),
                ("Does it work in airplane mode?", "Yes. Nothing the timer needs comes from the network, so it counts and sounds the same in airplane mode."),
                ("Do I need an account?", "No. There is no account and no sign-up, on iPhone, iPad or Android."),
                ("Does it keep running with the screen off?", "Yes. It keeps counting and sounding in the background and with the screen locked."),
            ],
        ),
        "ja": dict(
            short="オフラインで使えるタイマー",
            title="オフラインで使えるインターバルタイマー｜通信なし・登録なし｜タバタタイマー",
            desc="HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、インターネットにつながっていなくても使えます。タイマーも音声もビープ音もオフラインで動き、アカウント登録もありません。iPhone・iPad・Android、無料。",
            h1="オフラインで使えるインターバルタイマー",
            lede="HIIT &amp; Tabata Timer - タバタタイマー は、インターネットにつながっていなくても使えます。タイマーも音声もビープ音もオフラインで動き、ログインするアカウントもありません。地下のジムでも、グラウンドでも、機内モードでも、同じように始められます。iPhone・iPad・Android 向けで、無料です。",
            body="""
  <h2>通信なしで動くもの</h2>
  <ul>
    <li>タイマー本体（準備時間・運動時間・休憩時間・セット数）</li>
    <li>女性・男性の音声によるカウントダウン</li>
    <li>iPhone の3種類のビープ音（シャープ、ソフト、ホイッスル）</li>
    <li>バックグラウンドと画面ロック中の動作</li>
  </ul>

  <h2>通信を使うもの</h2>
  <p>画面下の小さなバナー広告、匿名の利用統計、ワークアウト履歴の3つだけです。どれもトレーニングを始めるのには必要ありません。</p>

  <h2>ログインがありません</h2>
  <p>アカウント登録も、確認が必要なサブスクリプションもないので、スタートを押すときにサーバーの応答を待つことがありません。位置情報・連絡先・カメラ・マイクも使いません。</p>

  <h2>こんな場所で役に立ちます</h2>
  <ul>
    <li>電波の届かない地下のジムやガレージ</li>
    <li>グラウンド、陸上トラック、山道</li>
    <li>データ通信なしでの旅行中</li>
    <li>通知を止めて集中したいときの機内モード</li>
  </ul>

  <h2>概要</h2>
  <div class="tablewrap">
  <table>
    <tr><th>価格</th><td>無料。サブスク・アプリ内課金・アカウント登録なし。</td></tr>
    <tr><th>対応機種</th><td>iPhone・iPad（iOS 15 以降）、Android（8.0 以降）</td></tr>
    <tr><th>設定範囲（iPhone）</th><td>運動5〜300秒、準備・休憩5〜120秒、2〜40セット</td></tr>
    <tr><th>設定範囲（Android）</th><td>各区間5〜60秒、2〜20セット</td></tr>
    <tr><th>広告</th><td>小さなバナー1つだけ。全画面広告・動画広告はありません。</td></tr>
  </table>
  </div>""",
            faq=[
                ("インターネットにつながっていなくても使えますか？", "はい。タイマーも音声もビープ音もオフラインで動きます。通信を使うのは、バナー広告、匿名の利用統計、ワークアウト履歴だけです。"),
                ("機内モードでも使えますか？", "はい。タイマーに必要なものは通信を使わないので、機内モードでも同じようにカウントして音が鳴ります。"),
                ("アカウント登録は必要ですか？", "いいえ。iPhone・iPad・Android のどれでも、アカウント登録はありません。"),
                ("画面を消しても動きますか？", "はい。バックグラウンドでも画面ロック中でも、カウントと音は続きます。"),
            ],
        ),
    },
    "interval-timer-with-beeps": {
        "en": dict(
            short="Interval timer with beeps",
            title="An interval timer with beeps or a whistle instead of a voice",
            desc="Tabata & HIIT Interval Timer by Takahiro Torii can sound a beep instead of a voice on iPhone: sharp, soft or whistle. Free, no subscription. Beeps carry across a gym and need no language.",
            h1="An interval timer with beeps or a whistle instead of a voice",
            lede="On iPhone and iPad, Tabata &amp; HIIT Interval Timer can sound a beep instead of a voice. There are three beeps: sharp, soft and whistle. It is free, with no subscription and no account.",
            body="""
  <h2>How to choose a beep</h2>
  <ol>
    <li>Open Settings and tap Sound.</li>
    <li>Tap a sound to hear it. There are five: a female voice, a male voice, and three beeps.</li>
    <li>Leave it on the one you want. The next workout uses it.</li>
  </ol>

  <h2>The five sounds</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Sound</th><th>Suits</th></tr>
    <tr><td>Female voice</td><td>Training alone, when hearing the numbers helps. Spoken in English.</td></tr>
    <tr><td>Male voice</td><td>The same, in a lower voice. Spoken in English.</td></tr>
    <tr><td>Sharp beep</td><td>Loud rooms and music</td></tr>
    <tr><td>Soft beep</td><td>Home, early mornings, shared spaces</td></tr>
    <tr><td>Whistle</td><td>Teams, classes and outdoor sessions</td></tr>
  </table>
  </div>

  <h2>Why choose a beep</h2>
  <ul>
    <li>It carries across a gym and over loud music better than a voice.</li>
    <li>It has no language. The voices speak English only.</li>
    <li>It sits over a podcast or a song without talking across it. Whatever is playing keeps playing at its own volume.</li>
  </ul>

  <h2>What it does not do</h2>
  <ul>
    <li>On Android the cues are a voice only, for now.</li>
    <li>The beep plays at the phone's media volume. For a hall or a field, connect a Bluetooth speaker.</li>
  </ul>
  <p>The <a href="/timer/">timer in your browser</a> on this site also uses beeps, with nothing to install.</p>""",
            faq=[
                ("Can I have a beep instead of a voice?", "Yes, on iPhone and iPad. Under Sound in Settings you can choose a female voice, a male voice, or one of three beeps (sharp, soft, whistle), and tap one to hear it. On Android the cues are a voice only, for now."),
                ("Is there an interval timer with a whistle sound?", "Yes. Tabata & HIIT Interval Timer for iPhone and iPad has a whistle among its three beeps."),
                ("Do the beeps play over music?", "Yes. Whatever is playing keeps playing at its own volume, and the beep plays over it."),
                ("Is it free?", "Yes. Every sound is free, with no subscription, no in-app purchases and no account. There is one small banner ad and no full-screen or video ads."),
            ],
        ),
        "ja": dict(
            short="ビープ音・ホイッスル音のタイマー",
            title="音声の代わりにビープ音やホイッスルで知らせるインターバルタイマー｜タバタタイマー",
            desc="HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、iPhone で音声の代わりにビープ音を選べます。シャープ、ソフト、ホイッスルの3種類。無料、サブスクなし。",
            h1="ビープ音やホイッスルで知らせるインターバルタイマー",
            lede="HIIT &amp; Tabata Timer - タバタタイマー は、iPhone と iPad で、音声の代わりにビープ音で知らせることができます。ビープ音はシャープ、ソフト、ホイッスルの3種類です。無料で、サブスクリプションもアカウント登録もありません。",
            body="""
  <h2>ビープ音の選び方</h2>
  <ol>
    <li>設定を開き、「Sound」をタップします。</li>
    <li>音をタップすると試聴できます。女性の声、男性の声、ビープ音3種類の、合わせて5つです。</li>
    <li>使いたい音を選んだままにします。次のワークアウトからその音で鳴ります。</li>
  </ol>

  <h2>5つの音</h2>
  <div class="tablewrap">
  <table>
    <tr><th>音</th><th>向いている場面</th></tr>
    <tr><td>女性の声</td><td>ひとりでのトレーニング。数字を聞きたいとき。英語です。</td></tr>
    <tr><td>男性の声</td><td>同じく、低めの声で。英語です。</td></tr>
    <tr><td>シャープ</td><td>音の大きい場所、音楽を流しているとき</td></tr>
    <tr><td>ソフト</td><td>自宅、早朝、まわりに人がいる場所</td></tr>
    <tr><td>ホイッスル</td><td>部活、クラス、屋外での練習</td></tr>
  </table>
  </div>

  <h2>ビープ音を選ぶ理由</h2>
  <ul>
    <li>体育館や大きな音楽の中でも、声より聞き取りやすい音です。</li>
    <li>言語に関係ありません。掛け声は英語のみです。</li>
    <li>ポッドキャストや曲に声がかぶりません。再生中の音はそのままの音量で流れ続けます。</li>
  </ul>

  <h2>できないこと</h2>
  <ul>
    <li>Android 版は今のところ音声のみです。</li>
    <li>ビープ音はスマートフォンのメディア音量で鳴ります。体育館やグラウンドでは Bluetooth スピーカーにつないでください。</li>
  </ul>
  <p>このサイトの<a href="/timer/ja/">ブラウザ版タイマー</a>もビープ音で知らせます。インストールは不要です。</p>""",
            faq=[
                ("音声の代わりにビープ音にできますか？", "はい、iPhone と iPad でできます。設定の「Sound」で、女性の声・男性の声・3種類のビープ音（シャープ、ソフト、ホイッスル）から選べ、タップすると試聴できます。Android 版は今のところ音声のみです。"),
                ("ホイッスルの音が鳴るインターバルタイマーはありますか？", "はい。iPhone・iPad 版の HIIT & Tabata Timer - タバタタイマー には、3種類のビープ音の1つとしてホイッスルがあります。"),
                ("音楽を流しながらでもビープ音は鳴りますか？", "はい。再生中の音はそのままの音量で流れ続け、その上にビープ音が重なります。"),
                ("無料ですか？", "はい。どの音も無料で、サブスクリプション・アプリ内課金・アカウント登録はありません。広告は小さなバナー1つだけで、全画面広告や動画広告は出ません。"),
            ],
        ),
    },
    "free-interval-timer-no-subscription": {
        "en": dict(
            short="Free, with no subscription",
            title="A free interval timer with no subscription, no in-app purchases and no account",
            desc="Tabata & HIIT Interval Timer by Takahiro Torii is free on iPhone, iPad and Android: no subscription, no in-app purchases, no account, no trial. One small banner ad, no full-screen or video ads.",
            h1="A free interval timer with no subscription and no account",
            lede="Tabata &amp; HIIT Interval Timer is free, and all of it is free: there is no subscription, no in-app purchase, no trial and no account. It is paid for by one small banner ad at the bottom of the screen. It runs on iPhone, iPad and Android.",
            body="""
  <h2>What "free" means here</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Price</th><td>Free to download and to use</td></tr>
    <tr><th>Subscription</th><td>None</td></tr>
    <tr><th>In-app purchases</th><td>None. Nothing is locked behind a payment.</td></tr>
    <tr><th>Free trial</th><td>None, because there is nothing to pay for afterwards</td></tr>
    <tr><th>Account</th><td>None. No sign-up, no email address, no sign-in.</td></tr>
    <tr><th>Ads</th><td>One small banner at the bottom of the screen. No full-screen ads and no video ads.</td></tr>
  </table>
  </div>

  <h2>About the ad</h2>
  <p>The app is not ad-free. It shows one small banner at the bottom of the screen, and that banner is what pays for it. It never covers the timer, it never plays a video, and nothing appears between pressing start and the workout beginning. There is no paid version without the banner.</p>
  <p>If you want a timer with no ad at all and nothing to install, the <a href="/timer/">timer in your browser</a> on this site has none.</p>

  <h2>What you get without paying</h2>
  <ul>
    <li>Ready time, work time, rest time and the number of sets</li>
    <li>On iPhone: work 5 to 300 seconds, ready and rest 5 to 120 seconds, 2 to 40 sets, and up to five saved timers</li>
    <li>On iPhone: a female voice, a male voice, or one of three beeps (sharp, soft, whistle)</li>
    <li>Running in the background, with the screen locked, and over your music</li>
    <li>A list of finished workouts, and fifteen colour themes on iPhone</li>
    <li>On Android: each interval 5 to 60 seconds, 2 to 20 sets, a voice</li>
  </ul>

  <h2>What it does not do</h2>
  <ul>
    <li>No custom sequences, EMOM or AMRAP modes. Every set uses the same work and rest time.</li>
    <li>No Apple Watch or Wear OS app.</li>
    <li>No exercise library, videos, coaching or workout plans.</li>
  </ul>
  <p>Timers that do these things are often the ones with a subscription. This one stays small, and free.</p>""",
            faq=[
                ("Is there a free interval timer with no subscription?", "Yes. Tabata & HIIT Interval Timer by Takahiro Torii is free on iPhone, iPad and Android, with no subscription, no in-app purchases, no trial and no account. It is paid for by one small banner ad."),
                ("Does it have ads?", "One small banner at the bottom of the screen. There are no full-screen ads and no video ads, and nothing interrupts a workout."),
                ("Can I pay to remove the ad?", "No. There are no in-app purchases of any kind, so there is no paid version without the banner."),
                ("Do I need to sign up?", "No. There is no account, no sign-up and no email address to give."),
                ("Are any features locked?", "No. Every setting, sound and theme is available without paying. Five of the fifteen themes on iPhone are earned by finishing workouts, not bought."),
            ],
        ),
        "ja": dict(
            short="無料・サブスクなしのタイマー",
            title="無料でサブスクなし・登録なしのインターバルタイマー｜広告は小さなバナー1つ｜タバタタイマー",
            desc="HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、iPhone・iPad・Android で無料です。サブスクリプション、アプリ内課金、アカウント登録、お試し期間はありません。広告は小さなバナー1つだけで、全画面広告や動画広告は出ません。",
            h1="無料でサブスクなし・登録なしのインターバルタイマー",
            lede="HIIT &amp; Tabata Timer - タバタタイマー は無料で、すべての機能が無料です。サブスクリプションも、アプリ内課金も、お試し期間も、アカウント登録もありません。費用は、画面下の小さなバナー広告1つでまかなっています。iPhone・iPad・Android で使えます。",
            body="""
  <h2>「無料」の中身</h2>
  <div class="tablewrap">
  <table>
    <tr><th>価格</th><td>ダウンロードも利用も無料</td></tr>
    <tr><th>サブスクリプション</th><td>なし</td></tr>
    <tr><th>アプリ内課金</th><td>なし。課金しないと使えない機能はありません。</td></tr>
    <tr><th>お試し期間</th><td>なし。あとから支払うものがないためです。</td></tr>
    <tr><th>アカウント登録</th><td>なし。登録もメールアドレスの入力もログインもありません。</td></tr>
    <tr><th>広告</th><td>画面下の小さなバナー1つ。全画面広告と動画広告はありません。</td></tr>
  </table>
  </div>

  <h2>広告について</h2>
  <p>広告がまったくないアプリではありません。画面下に小さなバナーが1つ出ます。このバナーがアプリの費用をまかなっています。バナーがタイマーを隠すことはなく、動画が流れることもなく、スタートを押してから運動が始まるまでの間に何かが挟まることもありません。バナーを消す有料版はありません。</p>
  <p>広告がまったくなく、インストールもしたくない場合は、このサイトの<a href="/timer/ja/">ブラウザ版タイマー</a>に広告はありません。</p>

  <h2>無料で使えるもの</h2>
  <ul>
    <li>準備時間・運動時間・休憩時間・セット数の設定</li>
    <li>iPhone: 運動5〜300秒、準備・休憩5〜120秒、2〜40セット、タイマーを5つまで保存</li>
    <li>iPhone: 女性の声、男性の声、3種類のビープ音（シャープ、ソフト、ホイッスル）</li>
    <li>バックグラウンド、画面ロック中、音楽を流しながらの動作</li>
    <li>終えたワークアウトの一覧。iPhone では15種類のカラーテーマ</li>
    <li>Android: 各区間5〜60秒、2〜20セット、音声</li>
  </ul>

  <h2>できないこと</h2>
  <ul>
    <li>区間ごとに長さを変えるメニュー、EMOM、AMRAP のモードはありません。すべてのセットが同じ運動時間・休憩時間です。</li>
    <li>Apple Watch と Wear OS のアプリはありません。</li>
    <li>種目の解説、動画、コーチング、トレーニングプランはありません。</li>
  </ul>
  <p>こうした機能を持つタイマーには、サブスクリプションのものが多くあります。このアプリは小さいまま、無料のままです。</p>""",
            faq=[
                ("無料でサブスクなしのインターバルタイマーはありますか？", "はい。HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、iPhone・iPad・Android で無料です。サブスクリプション、アプリ内課金、お試し期間、アカウント登録はありません。費用は小さなバナー広告1つでまかなっています。"),
                ("広告はありますか？", "画面下に小さなバナーが1つあります。全画面広告と動画広告はなく、ワークアウトの途中で広告に中断されることはありません。"),
                ("お金を払って広告を消せますか？", "できません。アプリ内課金が一切ないので、バナーのない有料版もありません。"),
                ("登録は必要ですか？", "いいえ。アカウント登録もメールアドレスの入力もありません。"),
                ("課金しないと使えない機能はありますか？", "ありません。設定も音もテーマも、支払いなしで使えます。iPhone の15種類のテーマのうち5つは、ワークアウトを終えた回数で開くもので、購入するものではありません。"),
            ],
        ),
    },
    "interval-timer-with-music": {
        "en": dict(
            short="Interval timer with music",
            title="An interval timer that works with music playing, in the background and with the screen locked",
            desc="Tabata & HIIT Interval Timer by Takahiro Torii plays its voice or beep over your music or podcast without pausing or lowering it, and keeps counting in the background and with the screen locked. Free, no subscription.",
            h1="An interval timer that works with your music playing",
            lede="Tabata &amp; HIIT Interval Timer plays over whatever you are listening to. Music or a podcast keeps playing at its own volume, and the timer's voice or beep sounds over it. It keeps counting in the background and with the screen locked. It is free, with no subscription and no account.",
            body="""
  <h2>How to use it with music</h2>
  <ol>
    <li>Start your music or podcast in any app.</li>
    <li>Open the timer, set the work time, the rest time and the number of sets, and press start.</li>
    <li>Go back to the music app or lock the screen. The timer keeps counting and sounding.</li>
  </ol>
  <p>Nothing needs to be switched on for this. The timer does not pause the music, and it does not turn it down while it speaks.</p>

  <h2>What you hear</h2>
  <ul>
    <li>A voice counts the last five seconds of each interval and calls each change.</li>
    <li>On iPhone and iPad a beep can replace the voice: sharp, soft or whistle. A beep sits over a song without talking across it.</li>
    <li>The cues play at the phone's media volume, through the same headphones or speaker as the music.</li>
  </ul>

  <h2>With the screen locked</h2>
  <p>The countdown and the cues continue with the screen off or another app open. On iPhone with iOS 16.1 or later the remaining time and a stop button show on the Lock Screen, so you can check the time without unlocking.</p>

  <h2>If the music is louder than the cue</h2>
  <p>Because the music is not turned down, a quiet voice can be lost under a loud track. Choose the sharp beep under Sound in Settings, or turn the music down a little in the music app.</p>

  <h2>What it does not do</h2>
  <ul>
    <li>It does not play music itself and has no playlists. It works beside whichever music app you use.</li>
    <li>It does not lower the music during a cue.</li>
    <li>On Android the cues are a voice only, each interval stops at 60 seconds and a workout at 20 sets, for now.</li>
  </ul>""",
            faq=[
                ("Which interval timer works in the background with music playing?", "Tabata & HIIT Interval Timer by Takahiro Torii does. Whatever is playing keeps playing at its own volume, the timer's voice or beep plays over it, and the timer keeps counting in the background and with the screen locked."),
                ("Does it pause or lower my music?", "No. It neither pauses the music nor turns it down. The cue plays over it."),
                ("Does it work with Spotify, Apple Music or a podcast app?", "Yes. It plays over audio from any app, because it does not take over the sound from the app that is playing."),
                ("Does it work with headphones?", "Yes. The cues play at the phone's media volume through the same headphones or speaker as the music."),
                ("Is it free?", "Yes. Every feature is free, with no subscription, no in-app purchases and no account. There is one small banner ad and no full-screen or video ads."),
            ],
        ),
        "ja": dict(
            short="音楽を聴きながら使えるタイマー",
            title="音楽を聴きながら使えるインターバルタイマー｜バックグラウンド・画面ロック対応｜タバタタイマー",
            desc="HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、音楽やポッドキャストを止めず、音量も下げずに、その上に音声やビープ音を重ねます。バックグラウンドでも画面ロック中でも動きます。無料、サブスクなし。",
            h1="音楽を聴きながら使えるインターバルタイマー",
            lede="HIIT &amp; Tabata Timer - タバタタイマー は、聴いている音の上に重ねて鳴ります。音楽やポッドキャストはそのままの音量で流れ続け、その上にタイマーの音声かビープ音が鳴ります。バックグラウンドでも画面ロック中でもカウントは続きます。無料で、サブスクリプションもアカウント登録もありません。",
            body="""
  <h2>音楽と一緒に使う手順</h2>
  <ol>
    <li>好きなアプリで音楽やポッドキャストを再生します。</li>
    <li>タイマーを開き、運動時間・休憩時間・セット数を決めて、スタートを押します。</li>
    <li>音楽アプリに戻るか、画面をロックします。タイマーはそのまま動き、音も鳴ります。</li>
  </ol>
  <p>このための設定はありません。タイマーが音楽を止めることはなく、声が出るあいだに音量を下げることもありません。</p>

  <h2>聞こえる音</h2>
  <ul>
    <li>各区間の最後の5秒を声で数え、切り替わりを知らせます。</li>
    <li>iPhone と iPad では、声の代わりにビープ音（シャープ、ソフト、ホイッスル）を選べます。ビープ音なら曲に声がかぶりません。</li>
    <li>合図はスマートフォンのメディア音量で、音楽と同じイヤホンやスピーカーから鳴ります。</li>
  </ul>

  <h2>画面をロックしたまま</h2>
  <p>画面を消しても、ほかのアプリを開いても、カウントと合図は続きます。iOS 16.1 以降の iPhone では、ロック画面に残り時間と停止ボタンが出るので、ロックを解除せずに時間を確かめられます。</p>

  <h2>音楽のほうが大きくて合図が聞こえないとき</h2>
  <p>音楽の音量を下げないので、音の大きい曲では小さな声が埋もれることがあります。設定の「Sound」でシャープのビープ音を選ぶか、音楽アプリの側で少し音量を下げてください。</p>

  <h2>できないこと</h2>
  <ul>
    <li>このアプリ自体は音楽を再生しません。プレイリストもありません。お使いの音楽アプリと並べて使います。</li>
    <li>合図のあいだだけ音楽を小さくする機能はありません。</li>
    <li>Android 版は今のところ音声のみで、各区間は60秒まで、セット数は20までです。</li>
  </ul>""",
            faq=[
                ("音楽を聴きながら使えるインターバルタイマーはありますか？", "はい。HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、再生中の音をそのままの音量で流し続け、その上に音声かビープ音を重ねます。バックグラウンドでも画面ロック中でもカウントは続きます。"),
                ("音楽が止まったり、音量が下がったりしますか？", "いいえ。音楽は止まらず、音量も下がりません。合図がその上に重なります。"),
                ("Spotify や Apple Music、ポッドキャストのアプリと一緒に使えますか？", "はい。再生しているアプリから音を奪わないので、どのアプリの音にも重ねて鳴ります。"),
                ("イヤホンでも使えますか？", "はい。合図はスマートフォンのメディア音量で、音楽と同じイヤホンやスピーカーから鳴ります。"),
                ("無料ですか？", "はい。すべての機能が無料で、サブスクリプション・アプリ内課金・アカウント登録はありません。広告は小さなバナー1つだけで、全画面広告や動画広告は出ません。"),
            ],
        ),
    },
    "tabata-timer-for-android": {
        "en": dict(
            short="Tabata timer for Android",
            title="A free Tabata timer for Android: 20 seconds on, 10 seconds off, no subscription",
            desc="Tabata & HIIT Interval Timer by Takahiro Torii runs on Android 8.0 or later (package com.tabatatimer). It opens on the standard Tabata protocol, counts aloud, keeps running with the screen off and is free with no subscription or account.",
            h1="A free Tabata timer for Android",
            lede="Tabata &amp; HIIT Interval Timer is on Google Play for Android 8.0 or later. It opens on the standard Tabata protocol, 20 seconds of work and 10 seconds of rest for 8 sets, and a voice counts each change. It is free, with no subscription, no in-app purchases and no account.",
            body="""
  <h2>What the Android app does</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Android version</th><td>8.0 or later</td></tr>
    <tr><th>Package</th><td>com.tabatatimer</td></tr>
    <tr><th>Default</th><td>10 s ready, 20 s work, 10 s rest, 8 sets: the standard Tabata protocol</td></tr>
    <tr><th>Ranges</th><td>Ready, work and rest 5 to 60 seconds each; 2 to 20 sets</td></tr>
    <tr><th>Sound</th><td>A voice counts the last five seconds and calls each change. Spoken in English.</td></tr>
    <tr><th>Background</th><td>Keeps counting with the screen off or another app open</td></tr>
    <tr><th>Music</th><td>Plays over music or a podcast without pausing it</td></tr>
    <tr><th>Offline</th><td>Works with no internet connection</td></tr>
    <tr><th>Price</th><td>Free. No subscription, no in-app purchases, no account.</td></tr>
    <tr><th>Ads</th><td>One small banner. No full-screen or video ads.</td></tr>
  </table>
  </div>

  <h2>How to use it</h2>
  <ol>
    <li>Install it from Google Play and open it. The standard Tabata numbers are already set.</li>
    <li>Press start. Ten seconds of ready time run first.</li>
    <li>To change the numbers, open Settings and set the work time, the rest time and the number of sets.</li>
  </ol>

  <h2>How it differs from the iPhone app</h2>
  <p>The Android app is the smaller of the two, for now.</p>
  <div class="tablewrap">
  <table>
    <tr><th></th><th>Android</th><th>iPhone and iPad</th></tr>
    <tr><td>Work time</td><td>5 to 60 s</td><td>5 to 300 s</td></tr>
    <tr><td>Rest and ready time</td><td>5 to 60 s</td><td>5 to 120 s</td></tr>
    <tr><td>Sets</td><td>2 to 20</td><td>2 to 40</td></tr>
    <tr><td>Saved timers</td><td>One setting</td><td>Up to five</td></tr>
    <tr><td>Cues</td><td>A voice</td><td>A female or male voice, or three beeps</td></tr>
  </table>
  </div>

  <h2>What it does not do</h2>
  <ul>
    <li>No intervals longer than 60 seconds, so three-minute rounds cannot be set on Android.</li>
    <li>No beeps, for now. The cues are a voice.</li>
    <li>No Wear OS app.</li>
    <li>No custom sequences, exercise library or workout plans.</li>
  </ul>
  <p>Several Android apps are called "Tabata Timer". This one is by Takahiro Torii and its package is com.tabatatimer.</p>""",
            faq=[
                ("Is there a free Tabata timer for Android with no subscription?", "Yes. Tabata & HIIT Interval Timer by Takahiro Torii (package com.tabatatimer) is free on Google Play for Android 8.0 or later, with no subscription, no in-app purchases and no account. It shows one small banner ad."),
                ("What can I set on Android?", "Ready time, work time and rest time from 5 to 60 seconds each, and 2 to 20 sets. It opens on 10 seconds ready, 20 seconds work, 10 seconds rest and 8 sets, the standard Tabata protocol."),
                ("Does it keep running with the screen off on Android?", "Yes. It keeps counting and speaking with the screen off or another app open."),
                ("Does the Android app have beeps?", "Not yet. On Android the cues are a voice. The iPhone and iPad app has three beeps as well."),
                ("Is the Android app the same as the iPhone app?", "It is the same timer by the same developer, but smaller for now: intervals up to 60 seconds, up to 20 sets, one setting and a voice only. On iPhone work time goes up to 300 seconds, with up to 40 sets, five saved timers and beeps."),
            ],
        ),
        "ja": dict(
            short="Android のタバタタイマー",
            title="Android で使える無料のタバタタイマー｜20秒運動・10秒休憩｜サブスクなし",
            desc="HIIT & Tabata Timer（開発: Takahiro Torii、パッケージ com.tabatatimer）は Android 8.0 以降で使えます。最初からタバタ式の秒数で始まり、声で数え、画面を消しても動きます。無料、サブスク・登録なし。",
            h1="Android で使える無料のタバタタイマー",
            lede="Takahiro Torii のタバタタイマーは、Google Play で Android 8.0 以降向けに公開しています。最初から標準のタバタ式（運動20秒・休憩10秒・8セット）になっていて、切り替わりを声で知らせます。無料で、サブスクリプションも、アプリ内課金も、アカウント登録もありません。",
            body="""
  <h2>Android 版でできること</h2>
  <div class="tablewrap">
  <table>
    <tr><th>対応バージョン</th><td>Android 8.0 以降</td></tr>
    <tr><th>パッケージ名</th><td>com.tabatatimer</td></tr>
    <tr><th>初期設定</th><td>準備10秒、運動20秒、休憩10秒、8セット（標準のタバタ式）</td></tr>
    <tr><th>設定範囲</th><td>準備・運動・休憩がそれぞれ5〜60秒、2〜20セット</td></tr>
    <tr><th>音</th><td>各区間の最後の5秒を声で数え、切り替わりを知らせます。英語です。</td></tr>
    <tr><th>バックグラウンド</th><td>画面を消しても、ほかのアプリを開いても動き続けます</td></tr>
    <tr><th>音楽</th><td>音楽やポッドキャストを止めずに、その上に重ねて鳴ります</td></tr>
    <tr><th>オフライン</th><td>インターネットにつながっていなくても動きます</td></tr>
    <tr><th>価格</th><td>無料。サブスク・アプリ内課金・アカウント登録なし。</td></tr>
    <tr><th>広告</th><td>小さなバナー1つだけ。全画面広告・動画広告はありません。</td></tr>
  </table>
  </div>

  <h2>使い方</h2>
  <ol>
    <li>Google Play から入れて開きます。標準のタバタ式の秒数が最初から入っています。</li>
    <li>スタートを押します。最初に準備時間の10秒が流れます。</li>
    <li>秒数を変えるときは、設定を開いて運動時間・休憩時間・セット数を決めます。</li>
  </ol>

  <h2>iPhone 版との違い</h2>
  <p>今のところ、Android 版のほうが小さなつくりです。</p>
  <div class="tablewrap">
  <table>
    <tr><th></th><th>Android</th><th>iPhone・iPad</th></tr>
    <tr><td>運動時間</td><td>5〜60秒</td><td>5〜300秒</td></tr>
    <tr><td>休憩・準備時間</td><td>5〜60秒</td><td>5〜120秒</td></tr>
    <tr><td>セット数</td><td>2〜20</td><td>2〜40</td></tr>
    <tr><td>保存できるタイマー</td><td>設定は1つ</td><td>5つまで</td></tr>
    <tr><td>合図</td><td>音声</td><td>女性・男性の声、または3種類のビープ音</td></tr>
  </table>
  </div>

  <h2>できないこと</h2>
  <ul>
    <li>60秒を超える区間は設定できません。3分ラウンドは Android では計れません。</li>
    <li>ビープ音は今のところありません。合図は音声です。</li>
    <li>Wear OS のアプリはありません。</li>
    <li>区間ごとに長さを変えるメニュー、種目の解説、トレーニングプランはありません。</li>
  </ul>
  <p>Android には「Tabata Timer」という名前のアプリがいくつもあります。このアプリは開発者が Takahiro Torii、パッケージ名が com.tabatatimer のものです。</p>""",
            faq=[
                ("Android で使える無料のタバタタイマーはありますか？", "はい。Takahiro Torii のタバタタイマー（パッケージ名 com.tabatatimer）は、Google Play で Android 8.0 以降向けに無料で公開しています。サブスクリプション、アプリ内課金、アカウント登録はありません。小さなバナー広告が1つ出ます。"),
                ("Android 版では何を設定できますか？", "準備時間・運動時間・休憩時間がそれぞれ5〜60秒、セット数が2〜20です。最初は準備10秒、運動20秒、休憩10秒、8セットの標準のタバタ式になっています。"),
                ("Android で画面を消しても動きますか？", "はい。画面を消しても、ほかのアプリを開いても、カウントと音声は続きます。"),
                ("Android 版にビープ音はありますか？", "まだありません。Android 版の合図は音声です。iPhone・iPad 版には3種類のビープ音もあります。"),
                ("Android 版は iPhone 版と同じですか？", "同じ開発者による同じタイマーですが、今のところ小さなつくりです。各区間は60秒まで、セット数は20まで、設定は1つ、合図は音声のみです。iPhone 版は運動時間が300秒まで、セット数が40まで、タイマーを5つ保存でき、ビープ音も選べます。"),
            ],
        ),
    },
    "simple-interval-timer": {
        "en": dict(
            short="A simple interval timer",
            title="A simple interval timer for HIIT and for rest between sets: four numbers and a start button",
            desc="Tabata & HIIT Interval Timer by Takahiro Torii is a simple interval timer for iPhone, iPad and Android: ready time, work time, rest time, sets, and start. No plans, no videos, no account. Free, no subscription.",
            h1="A simple interval timer: four numbers and a start button",
            lede="Tabata &amp; HIIT Interval Timer has four numbers: ready time, work time, rest time and the number of sets. Set them, press start, and a voice or a beep tells you when to go and when to stop. There are no workout plans, no videos and no account. It is free for iPhone, iPad and Android, with no subscription.",
            body="""
  <h2>All there is to set</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Setting</th><th>iPhone and iPad</th><th>Android</th></tr>
    <tr><td>Ready time</td><td>5 to 120 s</td><td>5 to 60 s</td></tr>
    <tr><td>Work time</td><td>5 to 300 s</td><td>5 to 60 s</td></tr>
    <tr><td>Rest time</td><td>5 to 120 s</td><td>5 to 60 s</td></tr>
    <tr><td>Sets</td><td>2 to 40</td><td>2 to 20</td></tr>
  </table>
  </div>
  <p>It opens on 10 seconds ready, 20 seconds work, 10 seconds rest and 8 sets, so a Tabata session needs no setting at all: open the app and press start.</p>

  <h2>Settings for common uses</h2>
  <div class="tablewrap">
  <table>
    <tr><th>Use</th><th>Work</th><th>Rest</th><th>Sets</th></tr>
    <tr><td>Tabata</td><td>20 s</td><td>10 s</td><td>8</td></tr>
    <tr><td>HIIT, even split</td><td>30 s</td><td>30 s</td><td>10</td></tr>
    <tr><td>HIIT, longer efforts</td><td>40 s</td><td>20 s</td><td>8 to 12</td></tr>
    <tr><td>Strength circuit with timed sets</td><td>45 s</td><td>15 s</td><td>one per exercise, repeated</td></tr>
    <tr><td>Strength training, timed sets with a full rest (iPhone)</td><td>40 s</td><td>90 s</td><td>3 to 5</td></tr>
    <tr><td>Plank</td><td>60 s</td><td>30 s</td><td>3 to 5</td></tr>
  </table>
  </div>

  <h2>As a rest timer in strength training</h2>
  <p>The app repeats one work time and one rest time, so it suits sets done against the clock: 40 seconds of squats, 90 seconds of rest, again. On iPhone the rest can be up to 120 seconds.</p>
  <p>It does not wait for you. If your sets take a different time each round and you want to start the rest with a tap when you put the bar down, a rest timer built for that will suit you better.</p>

  <h2>Why it stays simple</h2>
  <ul>
    <li>It can be started in two taps, and you do not have to look at it again: the voice counts the last five seconds of every interval.</li>
    <li>It keeps running with the screen locked and plays over your music.</li>
    <li>In the written App Store reviews, the reason people give most often for choosing it is that it is simple.</li>
  </ul>

  <h2>What it does not do</h2>
  <ul>
    <li>No custom sequences, EMOM or AMRAP modes. Every set uses the same work and rest time.</li>
    <li>No more than five saved timers on iPhone, and one setting on Android.</li>
    <li>No exercise library, videos, coaching or workout plans.</li>
    <li>No Apple Watch or Wear OS app.</li>
  </ul>""",
            faq=[
                ("What is the simplest HIIT timer for iPhone?", "Tabata & HIIT Interval Timer by Takahiro Torii is built to be that: ready time, work time, rest time, the number of sets and a start button. It has no workout plans, videos, account or subscription, and it is free."),
                ("Can I use it without setting anything?", "Yes. It opens on 10 seconds ready, 20 seconds work, 10 seconds rest and 8 sets, the standard Tabata protocol. Press start."),
                ("Can I use it as a rest timer between strength sets?", "Yes, for sets done against the clock: it repeats one work time and one rest time, with rest up to 120 seconds on iPhone. It does not wait for a tap at the end of a set, so it does not suit sets of varying length."),
                ("Can I save more than one timer?", "On iPhone, up to five, and you swipe between them. On Android the app holds one setting."),
                ("Is it free?", "Yes. Every feature is free, with no subscription, no in-app purchases and no account. There is one small banner ad and no full-screen or video ads."),
            ],
        ),
        "ja": dict(
            short="シンプルなインターバルタイマー",
            title="筋トレや HIIT のインターバルを計るシンプルなタイマーアプリ｜数字4つとスタートだけ｜タバタタイマー",
            desc="HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、準備時間・運動時間・休憩時間・セット数を決めてスタートを押すだけのシンプルなインターバルタイマーです。iPhone・iPad・Android、無料、サブスク・登録なし。",
            h1="筋トレや HIIT のインターバルを計るシンプルなタイマー",
            lede="HIIT &amp; Tabata Timer - タバタタイマー にある数字は4つだけです。準備時間、運動時間、休憩時間、セット数。決めてスタートを押せば、始めと終わりを声かビープ音で知らせます。トレーニングプランも、動画も、アカウント登録もありません。iPhone・iPad・Android で無料、サブスクリプションもありません。",
            body="""
  <h2>設定はこれだけ</h2>
  <div class="tablewrap">
  <table>
    <tr><th>設定</th><th>iPhone・iPad</th><th>Android</th></tr>
    <tr><td>準備時間</td><td>5〜120秒</td><td>5〜60秒</td></tr>
    <tr><td>運動時間</td><td>5〜300秒</td><td>5〜60秒</td></tr>
    <tr><td>休憩時間</td><td>5〜120秒</td><td>5〜60秒</td></tr>
    <tr><td>セット数</td><td>2〜40</td><td>2〜20</td></tr>
  </table>
  </div>
  <p>最初は準備10秒、運動20秒、休憩10秒、8セットになっています。タバタ式なら何も設定せず、開いてスタートを押すだけです。</p>

  <h2>よく使われる設定</h2>
  <div class="tablewrap">
  <table>
    <tr><th>用途</th><th>運動</th><th>休憩</th><th>セット数</th></tr>
    <tr><td>タバタ式</td><td>20秒</td><td>10秒</td><td>8</td></tr>
    <tr><td>HIIT（同じ長さ）</td><td>30秒</td><td>30秒</td><td>10</td></tr>
    <tr><td>HIIT（運動を長めに）</td><td>40秒</td><td>20秒</td><td>8〜12</td></tr>
    <tr><td>筋トレのサーキット（時間で区切る）</td><td>45秒</td><td>15秒</td><td>種目数 × 周回数</td></tr>
    <tr><td>筋トレ（時間で区切り、しっかり休む。iPhone）</td><td>40秒</td><td>90秒</td><td>3〜5</td></tr>
    <tr><td>プランク</td><td>60秒</td><td>30秒</td><td>3〜5</td></tr>
  </table>
  </div>

  <h2>筋トレのセット間の休憩に使う場合</h2>
  <p>このアプリは、1つの運動時間と1つの休憩時間を繰り返します。時間で区切る筋トレに向いています。たとえば、スクワット40秒、休憩90秒、をそのまま繰り返せます。iPhone では休憩を120秒まで設定できます。</p>
  <p>セットが終わるのを待ってはくれません。セットごとにかかる時間が違い、バーベルを置いたときにタップして休憩を始めたい場合は、そのための休憩タイマーのほうが向いています。</p>

  <h2>シンプルなままにしている理由</h2>
  <ul>
    <li>2タップで始められ、そのあとは画面を見なくて済みます。各区間の最後の5秒を声で数えます。</li>
    <li>画面をロックしても動き続け、音楽の上に重ねて鳴ります。</li>
    <li>App Store に書かれたレビューで、選んだ理由としていちばん多く挙がるのは「シンプル」です。</li>
  </ul>

  <h2>できないこと</h2>
  <ul>
    <li>区間ごとに長さを変えるメニュー、EMOM、AMRAP のモードはありません。すべてのセットが同じ運動時間・休憩時間です。</li>
    <li>保存できるタイマーは iPhone で5つまで、Android は設定1つです。</li>
    <li>種目の解説、動画、コーチング、トレーニングプランはありません。</li>
    <li>Apple Watch と Wear OS のアプリはありません。</li>
  </ul>""",
            faq=[
                ("筋トレのインターバルを計るシンプルなアプリはありますか？", "はい。HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、準備時間・運動時間・休憩時間・セット数を決めてスタートを押すだけのタイマーです。トレーニングプラン、動画、アカウント登録、サブスクリプションはなく、無料です。"),
                ("何も設定せずに使えますか？", "はい。最初から準備10秒、運動20秒、休憩10秒、8セットの標準のタバタ式になっています。スタートを押すだけです。"),
                ("筋トレのセット間の休憩タイマーとして使えますか？", "時間で区切る筋トレなら使えます。1つの運動時間と1つの休憩時間を繰り返し、iPhone では休憩を120秒まで設定できます。セットの終わりにタップして休憩を始める形ではないので、セットごとに長さが変わる場合には向きません。"),
                ("タイマーを複数保存できますか？", "iPhone では5つまで保存でき、スワイプで切り替えます。Android は設定1つです。"),
                ("無料ですか？", "はい。すべての機能が無料で、サブスクリプション・アプリ内課金・アカウント登録はありません。広告は小さなバナー1つだけで、全画面広告や動画広告は出ません。"),
            ],
        ),
    },
    "tabata-timer-apps-compared": {
        "en": dict(
            short="Tabata timer apps compared",
            title="Tabata timer apps compared: which one suits which workout",
            desc="Six Tabata and interval timer apps side by side: Tabata & HIIT Interval Timer, SmartWOD Timer, Seconds, Intervals Pro and two more. What each does, what is free, which run on Apple Watch. Written by the developer of one of them.",
            h1="Tabata timer apps compared: which one suits which workout",
            lede="There is no single best Tabata timer app. A plain timer suits a workout that repeats the same work and rest; a fuller one suits a session built from different intervals. This page puts six of them side by side. It is written by Takahiro Torii, who makes one of the six, Tabata &amp; HIIT Interval Timer, and it says where the others suit better.",
            body="""
  <h2>The short answer</h2>
  <ul>
    <li><strong>The same work and rest repeated, with nothing to set up</strong> (Tabata, 20 seconds on and 10 off, eight times; simple HIIT): Tabata &amp; HIIT Interval Timer, the app this site is about.</li>
    <li><strong>EMOM, AMRAP and For Time</strong>: SmartWOD Timer.</li>
    <li><strong>Intervals of different lengths</strong>, or a warm-up running into the main set: Seconds Interval Timer or Intervals Pro.</li>
    <li><strong>A timer on Apple Watch</strong>: SmartWOD Timer, Seconds Interval Timer and Intervals Pro. The app this site is about has none.</li>
  </ul>

  <h2>Six apps side by side</h2>
  <div class="tablewrap">
  <table>
    <tr><th>App</th><th>What its App Store page says it does</th><th>Paying</th></tr>
    <tr><td>Tabata &amp; HIIT Interval Timer<br>Takahiro Torii</td><td>One ready time, work time and rest time, and a number of sets. A voice or one of three beeps. Up to five saved timers. Runs in the background and on the Lock Screen, over music. No custom sequences.</td><td>Free. One small banner ad. No subscription and no in-app purchases.</td></tr>
    <tr><td>SmartWOD Timer - WOD Clock<br>SmartWOD GmbH</td><td>AMRAP, EMOM, For Time and Tabata timers and a custom timer. Presets, Apple Watch, casting to a TV, a workout log.</td><td>Free to download. Its page lists subscriptions.</td></tr>
    <tr><td>Seconds Interval Timer<br>Runloop Ltd</td><td>Templates for HIIT, Tabata and circuits. Intervals of different lengths, and timers chained into one. Voice, beeps and bells. Runs on Apple Watch by itself.</td><td>Free to download. Seconds Pro is a separate paid app.</td></tr>
    <tr><td>Intervals Pro: HIIT Timer<br>Intervals, LLC</td><td>A name, a duration, an alert and a colour for each interval. Apple Watch workouts without the phone, heart-rate monitors, running pace targets, widgets.</td><td>Free to download.</td></tr>
    <tr><td>Tabata Timer: Interval Timer.<br>Oleksandr Serhiienko</td><td>Work and rest times, sets and cycles. Interval names, voice cues, vibration. Runs in the background.</td><td>Free to download.</td></tr>
    <tr><td>Interval Timer □ HIIT Timer<br>Float Tech, LLC</td><td>Drag to set work, rest and rounds. A voice or a beep. History and statistics.</td><td>Free to download. Its page describes an optional subscription and a one-time lifetime pass.</td></tr>
  </table>
  </div>
  <p>The names, developers and descriptions of the other five apps are taken from their pages on the US App Store on 26 November 2026. What is free inside each of them, and the prices, can change: check the store page before choosing.</p>

  <h2>Where Tabata &amp; HIIT Interval Timer fits</h2>
  <p>It is the narrow one. It opens on 10 seconds ready, 20 seconds work, 10 seconds rest and 8 sets, so a Tabata session starts in two taps with nothing to set. On iPhone, work time goes up to 300 seconds, rest up to 120 seconds and sets up to 40, and five timers can be saved. It is also on Android (8.0 or later), where each interval is 5 to 60 seconds, a workout is 2 to 20 sets, and the cues are a voice.</p>
  <p>Every feature is free. In the written App Store reviews, the reason people give most often for choosing it is that it is simple.</p>

  <h2>Where another app fits better</h2>
  <ul>
    <li>Sets of different lengths in one session, or named intervals: Seconds Interval Timer or Intervals Pro.</li>
    <li>EMOM, AMRAP or For Time workouts: SmartWOD Timer.</li>
    <li>Timing from an Apple Watch: SmartWOD Timer, Seconds Interval Timer or Intervals Pro.</li>
    <li>An exercise library, videos or coaching: none of that is in Tabata &amp; HIIT Interval Timer.</li>
  </ul>""",
            faq=[
                ("What is the best Tabata timer app?", "It depends on the workout. For plain Tabata, 20 seconds of work and 10 seconds of rest eight times, Tabata & HIIT Interval Timer by Takahiro Torii opens on exactly those numbers and starts in two taps; it is free, with no subscription. For EMOM and AMRAP, SmartWOD Timer has those modes. For sessions built from intervals of different lengths, Seconds Interval Timer and Intervals Pro are made for that."),
                ("Which Tabata timer app is free with no subscription?", "Tabata & HIIT Interval Timer by Takahiro Torii: every feature is free, with no subscription, no in-app purchases and no account, and one small banner ad. The other apps on this page are free to download; the App Store pages of SmartWOD Timer and of Float Tech's Interval Timer describe subscriptions."),
                ("Which Tabata timer apps have an Apple Watch app?", "SmartWOD Timer, Seconds Interval Timer and Intervals Pro say on their App Store pages that they run on Apple Watch. Tabata & HIIT Interval Timer has no Apple Watch app."),
                ("Is there a simple Tabata timer for both iPhone and Android?", "Tabata & HIIT Interval Timer by Takahiro Torii is on iPhone and iPad (iOS 15 or later) and on Android (8.0 or later). On Android each interval is 5 to 60 seconds, a workout is 2 to 20 sets, and the cues are a voice."),
                ("Who wrote this comparison?", "Takahiro Torii, the developer of Tabata & HIIT Interval Timer, one of the six apps compared. What it says about the other apps comes from their US App Store pages on 26 November 2026."),
            ],
        ),
        "ja": dict(
            short="タバタタイマーアプリの比較",
            title="タバタタイマーアプリの比較｜どのアプリがどんなトレーニングに向くか",
            desc="タバタ式・インターバルタイマーのアプリ6つを並べて比べました。HIIT & Tabata Timer - タバタタイマー、SmartWOD Timer、Seconds、Intervals Pro ほか。できること、無料の範囲、Apple Watch 対応。6つのうち1つの開発者が書いています。",
            h1="タバタタイマーアプリの比較：どのアプリがどんなトレーニングに向くか",
            lede="いちばん良いタバタタイマーアプリは、1つには決まりません。同じ運動と休憩を繰り返すなら単純なタイマーが、長さの違う区間を組み合わせるなら機能の多いタイマーが向いています。このページでは6つのアプリを並べます。書いているのは、そのうちの1つ HIIT &amp; Tabata Timer - タバタタイマー の開発者 Takahiro Torii です。ほかのアプリのほうが向く場合も、そのまま書いています。",
            body="""
  <h2>先に結論</h2>
  <ul>
    <li><strong>同じ運動と休憩を、設定なしで繰り返したい</strong>（20秒運動・10秒休憩を8回のタバタ式、単純な HIIT）: HIIT &amp; Tabata Timer - タバタタイマー（このサイトのアプリ）</li>
    <li><strong>EMOM、AMRAP、For Time</strong>: SmartWOD Timer</li>
    <li><strong>区間ごとに長さを変えたい</strong>、ウォームアップから本番まで続けて計りたい: Seconds Interval Timer、Intervals Pro</li>
    <li><strong>Apple Watch で計りたい</strong>: SmartWOD Timer、Seconds Interval Timer、Intervals Pro。このサイトのアプリには Apple Watch 版がありません。</li>
  </ul>

  <h2>6つのアプリを並べる</h2>
  <div class="tablewrap">
  <table>
    <tr><th>アプリ</th><th>App Store のページに書かれていること</th><th>料金</th></tr>
    <tr><td>HIIT &amp; Tabata Timer - タバタタイマー<br>Takahiro Torii</td><td>準備時間・運動時間・休憩時間を1つずつと、セット数。声か3種類のビープ音。タイマーを5つまで保存。バックグラウンドとロック画面で動き、音楽に重ねて鳴る。区間ごとに長さを変えるメニューはない。</td><td>無料。小さなバナー広告が1つ。サブスクリプションとアプリ内課金はなし。</td></tr>
    <tr><td>SmartWOD Timer - WOD Clock<br>SmartWOD GmbH</td><td>AMRAP、EMOM、For Time、タバタのタイマーと、自分で組むタイマー。プリセット、Apple Watch、テレビへのキャスト、トレーニングの記録。</td><td>ダウンロードは無料。ページにサブスクリプションの記載あり。</td></tr>
    <tr><td>Seconds Interval Timer<br>Runloop Ltd</td><td>HIIT、タバタ、サーキットのテンプレート。長さの違う区間を組め、複数のタイマーを1つにつなげられる。声、ビープ音、ベル。Apple Watch だけでも動く。</td><td>ダウンロードは無料。Seconds Pro は別の有料アプリ。</td></tr>
    <tr><td>Intervals Pro: HIIT Timer<br>Intervals, LLC</td><td>区間ごとに名前・長さ・音・色を設定。iPhone なしで動く Apple Watch のワークアウト、心拍計、ランニングのペース目標、ウィジェット。</td><td>ダウンロードは無料。</td></tr>
    <tr><td>Tabata Timer: Interval Timer.<br>Oleksandr Serhiienko</td><td>運動時間と休憩時間、セット数とサイクル数。区間の名前、音声、バイブレーション。バックグラウンドで動く。</td><td>ダウンロードは無料。</td></tr>
    <tr><td>Interval Timer □ HIIT Timer<br>Float Tech, LLC</td><td>ドラッグで運動・休憩・ラウンド数を設定。声かビープ音。履歴と統計。</td><td>ダウンロードは無料。ページに、任意のサブスクリプションと買い切りのパスの記載あり。</td></tr>
  </table>
  </div>
  <p>ほかの5つのアプリの名前・開発者・説明は、2026年11月26日に米国の App Store の各ページから取りました。日本の App Store では名前が違うことがあります。アプリの中でどこまで無料か、いくらかは変わるので、選ぶ前にストアのページを確かめてください。</p>

  <h2>HIIT &amp; Tabata Timer - タバタタイマー が向く場合</h2>
  <p>6つのなかで、いちばんできることが少ないアプリです。開くと準備10秒、運動20秒、休憩10秒、8セットになっていて、タバタ式なら何も設定せず2タップで始まります。iPhone では運動時間を300秒まで、休憩を120秒まで、セット数を40まで設定でき、タイマーを5つ保存できます。Android（8.0以降）にもあり、こちらは各区間5〜60秒、2〜20セット、合図は声です。</p>
  <p>すべての機能が無料です。App Store に書かれたレビューで、選んだ理由としていちばん多く挙がるのは「シンプル」です。</p>

  <h2>ほかのアプリのほうが向く場合</h2>
  <ul>
    <li>1回のメニューのなかで区間の長さを変えたい、区間に名前を付けたい: Seconds Interval Timer、Intervals Pro</li>
    <li>EMOM、AMRAP、For Time のワークアウト: SmartWOD Timer</li>
    <li>Apple Watch で計りたい: SmartWOD Timer、Seconds Interval Timer、Intervals Pro</li>
    <li>種目の解説、動画、コーチング: HIIT &amp; Tabata Timer - タバタタイマー にはどれもありません。</li>
  </ul>""",
            faq=[
                ("おすすめのタバタタイマーアプリはどれですか？", "トレーニングの内容で変わります。20秒運動・10秒休憩を8回繰り返す標準のタバタ式なら、HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）が最初からその数字になっていて、2タップで始まります。無料で、サブスクリプションはありません。EMOM や AMRAP なら、そのモードがある SmartWOD Timer。長さの違う区間を組むなら、Seconds Interval Timer か Intervals Pro がそのためのアプリです。"),
                ("無料でサブスクリプションのないタバタタイマーアプリは？", "HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、すべての機能が無料で、サブスクリプション・アプリ内課金・アカウント登録がなく、広告は小さなバナー1つだけです。このページのほかのアプリもダウンロードは無料ですが、SmartWOD Timer と Float Tech の Interval Timer は、App Store のページにサブスクリプションの記載があります。"),
                ("Apple Watch で使えるタバタタイマーアプリは？", "SmartWOD Timer、Seconds Interval Timer、Intervals Pro は、App Store のページに Apple Watch で動くと書かれています。HIIT & Tabata Timer - タバタタイマー に Apple Watch 版はありません。"),
                ("iPhone と Android の両方で使えるシンプルなタバタタイマーは？", "HIIT & Tabata Timer - タバタタイマー（開発: Takahiro Torii）は、iPhone・iPad（iOS 15 以降）と Android（8.0 以降）で使えます。Android では各区間5〜60秒、2〜20セットで、合図は声です。"),
                ("この比較は誰が書いていますか？", "比べた6つのうちの1つ、HIIT & Tabata Timer - タバタタイマー の開発者 Takahiro Torii です。ほかのアプリについての記述は、2026年11月26日に米国の App Store の各ページから取りました。"),
            ],
        ),
    },
}

SLUGS = list(PAGES)

# French and German are translations of the English text above.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import uses_de  # noqa: E402
import uses_fr  # noqa: E402

for _lang, _mod in (("fr", uses_fr), ("de", uses_de)):
    assert list(_mod.PAGES) == SLUGS, _lang
    for _slug in SLUGS:
        assert len(_mod.PAGES[_slug]["faq"]) == len(PAGES[_slug]["en"]["faq"]), (_lang, _slug)
        PAGES[_slug][_lang] = _mod.PAGES[_slug]


def path(lang, slug):
    return ("/" if lang == "en" else f"/{lang}/") + slug + "/"


def page(lang, slug):
    p, u = PAGES[slug][lang], UI[lang]
    e = html.escape
    ld = [
        {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
        {"@context": "https://schema.org", "@type": "WebPage", "inLanguage": lang,
         "name": p["h1"], "url": BASE + path(lang, slug),
         "dateModified": MODIFIED[lang],
         "author": {"@type": "Person", "name": "Takahiro Torii"},
         "about": {"@type": "SoftwareApplication", "name": u["app_plain"],
                   "applicationCategory": "HealthApplication",
                   "operatingSystem": "iOS 15.0 or later, Android 8.0 or later",
                   "url": BASE + u["home"],
                   "offers": {"@type": "Offer", "price": "0", "priceCurrency": {"ja": "JPY", "fr": "EUR", "de": "EUR"}.get(lang, "USD")},
                   "sameAs": ["https://apps.apple.com/app/id1166542235",
                              "https://play.google.com/store/apps/details?id=com.tabatatimer"]}},
    ]
    scripts = "\n".join('<script type="application/ld+json">\n' + json.dumps(x, ensure_ascii=False, indent=2) + "\n</script>" for x in ld)
    faq = "\n".join(f"  <h3>{e(q)}</h3>\n  <p>{e(a)}</p>\n" for q, a in p["faq"])
    related = "\n".join(f'    <li><a href="{path(lang, s)}">{e(PAGES[s][lang]["short"])}</a></li>' for s in SLUGS if s != slug)
    hreflang = "\n".join(f'<link rel="alternate" hreflang="{c}" href="{BASE}{path(c, slug)}">' for c in LANGS)
    others = "".join(f'<a href="{path(c, slug)}" lang="{c}">{NAMES[c]}</a>' for c in LANGS if c != lang)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['desc'])}">
<link rel="canonical" href="{BASE}{path(lang, slug)}">
{hreflang}
<link rel="alternate" hreflang="x-default" href="{BASE}{path('en', slug)}">
<link rel="icon" href="/icon.png">
<meta name="apple-itunes-app" content="app-id=1166542235">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(p['h1'])}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:url" content="{BASE}{path(lang, slug)}">
<meta property="og:image" content="{BASE}/icon.png">
{scripts}
<style>
{STYLE}
</style>
</head>
<body>
<main>
  <p class="lang"><a href="{u['home']}">{u['app']}</a>{others}</p>

  <header>
    <img src="/icon.png" alt="{u['alt']}" width="64" height="64">
    <div>
      <h1>{e(p['h1'])}</h1>
      <p class="by">{u['app']} · {u['by']}</p>
    </div>
  </header>

  <p class="lede">{p['lede']}</p>

  <div class="get">
    <a href="{u['ios_url']}">{u['ios']}</a>
    <a href="https://play.google.com/store/apps/details?id=com.tabatatimer">{u['play']}</a>
  </div>
{p['body']}

  <h2>{u['questions']}</h2>

{faq}
  <h2>{u['related']}</h2>
  <ul>
{related}
    <li><a href="{u['home']}">{u['about']}</a></li>
  </ul>

  <h2>{u['get']}</h2>
  <div class="get">
    <a href="{u['ios_url']}">{u['ios']}</a>
    <a href="https://play.google.com/store/apps/details?id=com.tabatatimer">{u['play']}</a>
  </div>

  <footer>
    <a href="{u['home']}">{u['app']}</a>
    <a href="{u['timer_url']}">{u['timer']}</a>
    <a href="/privacy.html">{u['privacy']}</a>
    <a href="mailto:support@simpletabata.com">{u['contact']}: support@simpletabata.com</a>
    <span>{u['updated']} {UPDATED[lang]}</span>
  </footer>
</main>
</body>
</html>
"""


for slug in SLUGS:
    for lang in LANGS:
        d = SITE / path(lang, slug).strip("/")
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(lang, slug), encoding="utf-8")
print("built", ", ".join(SLUGS))
