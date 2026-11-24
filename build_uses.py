#!/usr/bin/env python3
"""Writes the pages that answer one question each: boxing rounds, a class or
a team, no connection, a beep instead of a voice.

    python3 build_uses.py .

Each page exists in English and Japanese and says only what the main pages
already say about the app, arranged around the one use. When a fact changes
on the main pages, change it here too and run this again.
"""
import html
import json
import sys
from pathlib import Path

SITE = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
BASE = "https://simpletabata.com"
UPDATED = {"en": "24 November 2026", "ja": "2026年11月24日"}

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
  .lang a { margin-right:.75rem; }
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
        other_lang=("日本語", "ja"), alt="Tabata &amp; HIIT Interval Timer app icon",
    ),
    "ja": dict(
        home="/ja/", app="HIIT &amp; Tabata Timer - タバタタイマー", app_plain="HIIT & Tabata Timer - タバタタイマー",
        by="開発: Takahiro Torii ・ iPhone / iPad / Android ・ 無料",
        ios="App Store でダウンロード", ios_url="https://apps.apple.com/jp/app/id1166542235",
        play="Google Play で入手",
        questions="よくある質問", related="ほかの使い方", get="ダウンロード",
        about="アプリの説明", timer="ブラウザ版タイマー", timer_url="/timer/ja/",
        privacy="プライバシーポリシー", contact="お問い合わせ", updated="最終更新",
        other_lang=("English", "en"), alt="HIIT &amp; Tabata Timer - タバタタイマー のアイコン",
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
}

SLUGS = list(PAGES)


def path(lang, slug):
    return ("/ja/" if lang == "ja" else "/") + slug + "/"


def page(lang, slug):
    p, u = PAGES[slug][lang], UI[lang]
    e = html.escape
    ld = [
        {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
        {"@context": "https://schema.org", "@type": "WebPage", "inLanguage": lang,
         "name": p["h1"], "url": BASE + path(lang, slug),
         "dateModified": "2026-11-24",
         "author": {"@type": "Person", "name": "Takahiro Torii"},
         "about": {"@type": "SoftwareApplication", "name": u["app_plain"],
                   "applicationCategory": "HealthApplication",
                   "operatingSystem": "iOS 15.0 or later, Android 8.0 or later",
                   "url": BASE + u["home"],
                   "offers": {"@type": "Offer", "price": "0", "priceCurrency": "JPY" if lang == "ja" else "USD"},
                   "sameAs": ["https://apps.apple.com/app/id1166542235",
                              "https://play.google.com/store/apps/details?id=com.tabatatimer"]}},
    ]
    scripts = "\n".join('<script type="application/ld+json">\n' + json.dumps(x, ensure_ascii=False, indent=2) + "\n</script>" for x in ld)
    faq = "\n".join(f"  <h3>{e(q)}</h3>\n  <p>{e(a)}</p>\n" for q, a in p["faq"])
    related = "\n".join(f'    <li><a href="{path(lang, s)}">{e(PAGES[s][lang]["short"])}</a></li>' for s in SLUGS if s != slug)
    ol_name, ol_code = u["other_lang"]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['desc'])}">
<link rel="canonical" href="{BASE}{path(lang, slug)}">
<link rel="alternate" hreflang="en" href="{BASE}{path('en', slug)}">
<link rel="alternate" hreflang="ja" href="{BASE}{path('ja', slug)}">
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
  <p class="lang"><a href="{u['home']}">{u['app']}</a><a href="{path(ol_code, slug)}" lang="{ol_code}">{ol_name}</a></p>

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
    for lang in ("en", "ja"):
        d = SITE / path(lang, slug).strip("/")
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(lang, slug), encoding="utf-8")
print("built", ", ".join(SLUGS))
