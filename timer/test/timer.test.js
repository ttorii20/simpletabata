// Tests for the browser timer. Run from the repository root:
//
//     node --test timer/test/timer.test.js
//
// No dependencies. The pages are self-contained, so the timing logic lives in
// an inline <script> in each of them, between the comments `timer-core:begin`
// and `timer-core:end`. These tests read that text out of the HTML and
// evaluate it, so what is tested is exactly what the browser runs.

'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const PAGES = {
  en: path.join(__dirname, '..', 'index.html'),
  ja: path.join(__dirname, '..', 'ja', 'index.html'),
};

function read(file) {
  return fs.readFileSync(file, 'utf8');
}

// The last <script> in the page that is not JSON-LD.
function inlineScript(html) {
  const found = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
  assert.equal(found.length, 1, 'expected exactly one inline script');
  return found[0][1];
}

function loadCore(html) {
  const script = inlineScript(html);
  const begin = script.indexOf('/* timer-core:begin');
  const end = script.indexOf('/* timer-core:end */');
  assert.ok(begin >= 0 && end > begin, 'timer-core markers not found');
  const source = script.slice(begin, end);
  return new Function(
    source +
      '\nreturn { RANGES, KEYS, clampValue, normalize, parseQuery, toQuery, totalMs, stateAt, cueFor, clock };'
  )();
}

const html = { en: read(PAGES.en), ja: read(PAGES.ja) };
const core = loadCore(html.en);
const TABATA = { ready: 10, work: 20, rest: 10, sets: 8 };
const at = (seconds, s = TABATA) => core.stateAt(s, seconds * 1000);

test('both pages carry the same script, byte for byte', () => {
  assert.equal(inlineScript(html.ja), inlineScript(html.en));
});

test('defaults are the Tabata protocol', () => {
  assert.deepEqual(core.normalize(null), TABATA);
  assert.deepEqual(core.normalize({}), TABATA);
});

test('total has no rest after the last set: 10 + 8*20 + 7*10 = 240 s', () => {
  assert.equal(core.totalMs(TABATA), 240000);
  assert.equal(core.totalMs({ ready: 5, work: 5, rest: 5, sets: 2 }), 20000);
  assert.equal(core.totalMs({ ready: 120, work: 300, rest: 120, sets: 40 }), (120 + 300 * 40 + 120 * 39) * 1000);
});

test('start: ready, set 1, full time on the clock', () => {
  assert.deepEqual(at(0), {
    phase: 'ready', set: 1, sets: 8, step: 0,
    secondsLeft: 10, totalSecondsLeft: 240, finished: false,
  });
});

test('seconds left counts down by ceiling, so it never shows 0 mid-phase', () => {
  assert.equal(core.stateAt(TABATA, 1).secondsLeft, 10);
  assert.equal(core.stateAt(TABATA, 999).secondsLeft, 10);
  assert.equal(core.stateAt(TABATA, 1000).secondsLeft, 9);
  assert.equal(core.stateAt(TABATA, 9999).secondsLeft, 1);
  assert.equal(core.stateAt(TABATA, 9999).phase, 'ready');
});

test('phase boundaries in the first set', () => {
  // ready 0-10, work 10-30, rest 30-40, work 40-60 ...
  assert.equal(core.stateAt(TABATA, 9999).phase, 'ready');
  assert.deepEqual(at(10), {
    phase: 'work', set: 1, sets: 8, step: 1,
    secondsLeft: 20, totalSecondsLeft: 230, finished: false,
  });
  assert.equal(core.stateAt(TABATA, 29999).phase, 'work');
  assert.equal(core.stateAt(TABATA, 29999).secondsLeft, 1);
  assert.deepEqual(at(30), {
    phase: 'rest', set: 1, sets: 8, step: 2,
    secondsLeft: 10, totalSecondsLeft: 210, finished: false,
  });
  assert.equal(core.stateAt(TABATA, 39999).phase, 'rest');
  assert.deepEqual(at(40), {
    phase: 'work', set: 2, sets: 8, step: 3,
    secondsLeft: 20, totalSecondsLeft: 200, finished: false,
  });
});

test('the last set is work only, then done; there is no eighth rest', () => {
  // Set 8 works from 220 s to 240 s.
  assert.equal(at(219.999).phase, 'rest');
  assert.equal(at(219.999).set, 7);
  assert.deepEqual(at(220), {
    phase: 'work', set: 8, sets: 8, step: 15,
    secondsLeft: 20, totalSecondsLeft: 20, finished: false,
  });
  assert.equal(at(239.999).phase, 'work');
  assert.equal(at(239.999).secondsLeft, 1);
  assert.deepEqual(at(240), {
    phase: 'done', set: 8, sets: 8, step: 16,
    secondsLeft: 0, totalSecondsLeft: 0, finished: true,
  });
});

test('every second of a workout: phases in order, clocks consistent', () => {
  for (const s of [TABATA, { ready: 5, work: 5, rest: 5, sets: 2 }, { ready: 7, work: 45, rest: 15, sets: 5 }]) {
    const total = core.totalMs(s) / 1000;
    let previous = null;
    let rests = 0;
    let works = 0;
    for (let sec = 0; sec < total; sec++) {
      const st = at(sec, s);
      assert.equal(st.finished, false);
      assert.equal(st.totalSecondsLeft, total - sec);
      assert.ok(st.secondsLeft >= 1 && st.secondsLeft <= st.totalSecondsLeft);
      assert.ok(st.set >= 1 && st.set <= s.sets);
      if (previous) {
        if (st.step === previous.step) {
          assert.equal(st.secondsLeft, previous.secondsLeft - 1);
        } else {
          assert.equal(st.step, previous.step + 1);
          assert.equal(previous.secondsLeft, 1);
          assert.equal(st.secondsLeft, s[st.phase]);
        }
      }
      if (!previous || st.step !== previous.step) {
        if (st.phase === 'work') works++;
        if (st.phase === 'rest') rests++;
      }
      previous = st;
    }
    assert.equal(previous.phase, 'work');
    assert.equal(works, s.sets);
    assert.equal(rests, s.sets - 1);
  }
});

test('large jumps and odd inputs still give a right answer', () => {
  // A tab asleep for a minute and a half lands mid-workout, correctly.
  assert.deepEqual(at(95.4), {
    phase: 'rest', set: 3, sets: 8, step: 6,
    secondsLeft: 5, totalSecondsLeft: 145, finished: false,
  });
  // Far past the end, a day later, is simply done.
  for (const ms of [240001, 86400000, Number.MAX_SAFE_INTEGER, Infinity]) {
    const st = core.stateAt(TABATA, ms);
    assert.equal(st.finished, true);
    assert.equal(st.phase, 'done');
    assert.equal(st.totalSecondsLeft, 0);
  }
  // A clock that went backwards, or nonsense, is the start.
  for (const ms of [-1, -100000, NaN, undefined, null]) {
    assert.deepEqual(core.stateAt(TABATA, ms), at(0));
  }
});

test('cues: ticks on 3, 2, 1, a tone per phase change, one finish', () => {
  const cue = (a, b) => core.cueFor(core.stateAt(TABATA, a), core.stateAt(TABATA, b));
  assert.equal(cue(0, 100), null);
  assert.equal(cue(5900, 6000), null);       // shows 4
  assert.equal(cue(6900, 7000), 'tick');     // shows 3
  assert.equal(cue(7000, 7100), null);       // still 3
  assert.equal(cue(7900, 8000), 'tick');     // 2
  assert.equal(cue(8900, 9000), 'tick');     // 1
  assert.equal(cue(9900, 10000), 'work');
  assert.equal(cue(29900, 30000), 'rest');
  assert.equal(cue(239900, 240000), 'finish');
  assert.equal(cue(240000, 240100), null);   // only once
});

test('cues after a long gap: the newest phase only, never a backlog', () => {
  const cue = (a, b) => core.cueFor(core.stateAt(TABATA, a), core.stateAt(TABATA, b));
  assert.equal(cue(2000, 95400), 'rest');
  assert.equal(cue(2000, 75000), 'work');
  assert.equal(cue(2000, 999999), 'finish');
  // Same phase, landing inside the last three seconds: a single tick.
  assert.equal(cue(11000, 28500), 'tick');
});

test('a whole run sampled every 100 ms plays each cue the right number of times', () => {
  const counts = { tick: 0, ready: 0, work: 0, rest: 0, finish: 0 };
  let previous = core.stateAt(TABATA, 0);
  for (let ms = 100; ms <= 241000; ms += 100) {
    const now = core.stateAt(TABATA, ms);
    const cue = core.cueFor(previous, now);
    if (cue) counts[cue]++;
    previous = now;
  }
  // 1 ready + 8 work + 7 rest = 16 phases, three ticks each.
  assert.deepEqual(counts, { tick: 48, ready: 0, work: 8, rest: 7, finish: 1 });
});

test('URL parameters are read and clamped to the ranges', () => {
  assert.deepEqual(core.parseQuery('?ready=10&work=20&rest=10&sets=8'), TABATA);
  assert.deepEqual(core.parseQuery('?ready=15&work=180&rest=60&sets=12'), { ready: 15, work: 180, rest: 60, sets: 12 });
  // Too small and too large.
  assert.deepEqual(core.parseQuery('?ready=0&work=1&rest=-5&sets=1'), { ready: 5, work: 5, rest: 5, sets: 2 });
  assert.deepEqual(core.parseQuery('?ready=999&work=301&rest=121&sets=41'), { ready: 120, work: 300, rest: 120, sets: 40 });
  // The edges themselves pass through.
  assert.deepEqual(core.parseQuery('?ready=5&work=5&rest=5&sets=2'), { ready: 5, work: 5, rest: 5, sets: 2 });
  assert.deepEqual(core.parseQuery('?ready=120&work=300&rest=120&sets=40'), { ready: 120, work: 300, rest: 120, sets: 40 });
});

test('missing or broken URL parameters fall back to the defaults', () => {
  assert.equal(core.parseQuery(''), null);
  assert.equal(core.parseQuery('?utm_source=x'), null);
  assert.deepEqual(core.parseQuery('?work=45'), { ready: 10, work: 45, rest: 10, sets: 8 });
  assert.deepEqual(core.parseQuery('?work=abc&sets='), TABATA);
  assert.deepEqual(core.parseQuery('?work=Infinity&rest=1e9&sets=NaN'), { ready: 10, work: 20, rest: 120, sets: 8 });
  assert.deepEqual(core.parseQuery('?work=29.6&sets=7.4'), { ready: 10, work: 30, rest: 10, sets: 7 });
  assert.deepEqual(core.parseQuery('?work=<script>&sets=%00'), TABATA);
});

test('settings round-trip through the address', () => {
  assert.equal(core.toQuery(TABATA), '?ready=10&work=20&rest=10&sets=8');
  const s = { ready: 15, work: 180, rest: 60, sets: 12 };
  assert.deepEqual(core.parseQuery(core.toQuery(s)), s);
});

test('clock formats seconds as m:ss', () => {
  assert.equal(core.clock(240), '4:00');
  assert.equal(core.clock(9), '0:09');
  assert.equal(core.clock(61), '1:01');
  assert.equal(core.clock(0), '0:00');
  assert.equal(core.clock(16800), '280:00');
});

test('pages are self-contained: nothing is loaded from another host', () => {
  for (const [name, page] of Object.entries(html)) {
    // Anything the browser would fetch on load.
    const loaded = [...page.matchAll(/<(?:script|img|iframe|source|audio|video|embed|object)\b[^>]*\b(?:src|data)="([^"]+)"/g)].map((m) => m[1]);
    const sheets = [...page.matchAll(/<link\b[^>]*rel="(?:stylesheet|preload|preconnect|dns-prefetch|modulepreload)"[^>]*>/g)];
    assert.deepEqual(loaded, [], name + ': unexpected embedded resource');
    assert.deepEqual(sheets, [], name + ': unexpected linked resource');
    assert.ok(!/@import|url\(|fetch\(|XMLHttpRequest|sendBeacon|WebSocket|document\.cookie/.test(page), name + ': unexpected network or cookie use');
  }
});

test('structured data is valid JSON and says only what the page says', () => {
  const expected = { en: 'https://simpletabata.com/timer/', ja: 'https://simpletabata.com/timer/ja/' };
  for (const [name, page] of Object.entries(html)) {
    const block = page.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
    assert.ok(block, name + ': JSON-LD missing');
    const data = JSON.parse(block[1]);
    assert.equal(data['@type'], 'WebApplication');
    assert.equal(data.url, expected[name]);
    assert.equal(data.operatingSystem, 'Any (web browser)');
    assert.equal(data.offers.price, '0');
    assert.equal(data.author.name, 'Takahiro Torii');
    assert.equal(data.aggregateRating, undefined);
    assert.equal(data.review, undefined);
    assert.ok(page.includes('<link rel="canonical" href="' + expected[name] + '">'));
    assert.ok(page.includes('Takahiro Torii</a>'));
  }
});
