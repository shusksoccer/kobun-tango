// Smoke tests for the built pages. Run: npm i jsdom && node test/test.js
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');

const DIST = path.join(__dirname, '..', 'dist');
const run = f => new JSDOM(fs.readFileSync(path.join(DIST, f), 'utf8'),
  { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://kobun.test/' + f });

let pass = 0, fail = 0;
const ok = (name, cond) => { (cond ? pass++ : fail++); console.log((cond ? 'PASS ' : 'FAIL ') + name); };

// ---- dictionary (index.html) ----
{
  const d = run('index.html'), doc = d.window.document;
  ok('index: 330 cards', doc.querySelectorAll('.card').length === 330);
  ok('index: subtitle shows total', /330/.test(doc.querySelector('#subtitle').textContent));
  ok('index: every card has a note preview', doc.querySelectorAll('.noteprev').length === 330);
  ok('index: all tags in one meta row (no themerow)', doc.querySelectorAll('.themerow').length === 0);
  const w7len = d.window.eval('DB.words.find(x=>x.no===7).meanings.length');
  ok('index: one checkable row per meaning (w7)',
     doc.querySelectorAll('#w7 .mlist .mrow').length === w7len);
  ok('index: meaning text is citation form (w7 みゆ has 見られる)',
     [...doc.querySelectorAll('#w7 .mtext')].some(s => s.textContent.includes('見られる')));
  ok('index: example answer keeps example form (見られ)',
     [...doc.querySelectorAll('#w7 .ex .exmask')].some(span => span.textContent === '見られ'));
  // popup
  d.window.eval('openNote(1)');
  ok('index: note popup opens', !doc.querySelector('#noteModal').hidden);
  ok('index: popup shows kanji', /驚く/.test(doc.querySelector('#noteTitle').textContent));
  d.window.eval('closeNote()');
  // example panel toggle independent of popup
  doc.querySelector('#w1 .disc[data-t="ex"]').click();
  ok('index: example panel toggles', doc.querySelector('#w1 .panel[data-p="ex"]').classList.contains('open'));
  // per-sense known checks
  const chk = doc.querySelector('#w7 .mlist .mchk');
  chk.click();
  ok('index: sense check toggles on',
     chk.getAttribute('aria-pressed') === 'true' && chk.closest('.mrow').classList.contains('on'));
  ok('index: sense check persists to localStorage (7:1)',
     JSON.parse(d.window.localStorage.getItem('koten_known') || '[]').includes('7:1'));
  ok('index: master shows partial when some (not all) senses known',
     doc.querySelector('#w7 .known').classList.contains('partial'));
  doc.querySelector('#w7 .known').click();
  ok('index: master toggle marks all senses known',
     doc.querySelectorAll('#w7 .mrow.on').length === w7len &&
     doc.querySelector('#w7 .known').getAttribute('aria-pressed') === 'true' &&
     doc.querySelector('#w7').classList.contains('learned'));
  doc.querySelector('#w7 .known').click();
  ok('index: master toggle clears all senses',
     doc.querySelectorAll('#w7 .mrow.on').length === 0 &&
     !doc.querySelector('#w7').classList.contains('learned'));
  // sense check writes a date (SRS-lite)
  doc.querySelector('#w7 .mlist .mchk').click();
  ok('index: sense check records date in koten_known_at',
     !!JSON.parse(d.window.localStorage.getItem('koten_known_at') || '{}')['7:1']);
  // kana-normalized search: modern kana finds historical-kana headword
  d.window.eval("state.q='おかし';render()");
  ok('index: search normalizes historical kana (おかし → をかし)',
     !!doc.querySelector('#w15') && !doc.querySelector('#w1'));
  d.window.eval("state.q='';render()");
  // conjugation badge and source era
  ok('index: conjugation badge (w1 おどろく = カ行四段)',
     (doc.querySelector('#w1 .kat') || {}).textContent === 'カ行四段');
  ok('index: adjective conjugation (w15 をかし = シク活用)',
     (doc.querySelector('#w15 .kat') || {}).textContent === 'シク活用');
  ok('index: source shows era (源氏物語（平安中期）)',
     [...doc.querySelectorAll('#w1 .src')].some(s => s.textContent.includes('源氏物語（平安中期）')));
  // report modal
  doc.querySelector('#report').click();
  ok('index: report modal opens with band/theme bars',
     !doc.querySelector('#repModal').hidden &&
     doc.querySelectorAll('#repBody .rep').length >= 10 &&
     /330/.test(doc.querySelector('#repBody .repline').textContent));
  d.window.eval('closeReport()');
  // legacy word-level data (a bare number) migrates to all senses of that word
  const dm = new JSDOM(fs.readFileSync(path.join(DIST, 'index.html'), 'utf8'),
    { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://kobun.test/index.html',
      beforeParse(win) { try { win.localStorage.setItem('koten_known', JSON.stringify([1])); } catch (e) {} } });
  const migrated = dm.window.eval('[...known]');
  ok('index: legacy word-level known migrates to per-sense',
     migrated.includes('1:1') && migrated.includes('1:2') &&
     dm.window.document.querySelector('#w1 .known').getAttribute('aria-pressed') === 'true');
}

// ---- quiz (quiz.html) ----
{
  const q = run('quiz.html'), w = q.window, doc = w.document;
  ok('quiz: pool = 330', doc.querySelector('#pcount').textContent === '330');
  // forward: full sentence + underlined target + tap hint
  w.eval("mode='fwd';$('#num').value='0';$('#order').value='no';start(pool());idx=deck.findIndex(x=>x.no===1);show();");
  ok('quiz fwd: classical sentence underlined (.mk)', doc.querySelector('.qcard .qko').innerHTML.includes('<u class="mk">'));
  ok('quiz fwd: hint hidden until tapped', doc.querySelector('#qhint').style.display === 'none');
  w.eval('revealAns()');
  ok('quiz fwd: reveal lists per-sense checkable meanings', doc.querySelectorAll('#reveal .mlist .mrow').length >= 1);
  w.eval("known.clear();localStorage.removeItem('koten_known');idx=deck.findIndex(x=>x.no===1);show();revealAns();");
  doc.querySelector('#reveal .mlist .mchk').click();
  ok('quiz fwd: checking a sense in reveal persists to localStorage',
     JSON.parse(w.localStorage.getItem('koten_known') || '[]').some(k => /^1:/.test(k)));
  w.eval("known.clear();localStorage.removeItem('koten_known');idx=deck.findIndex(x=>x.no===1);show();revealAns();$('#knowBtn').click();");
  ok('quiz fwd: 覚えた marks a sense of the tested word (not the whole word as a bare number)',
     JSON.parse(w.localStorage.getItem('koten_known') || '[]').some(k => /^1:\d+$/.test(k)));
  // reverse: numbered meaning prompt + all cloze examples + 訳 underlined, scrollable
  w.eval("$('#quit').click();mode='rev';start(pool());idx=deck.findIndex(x=>x.no===7);show();");
  ok('quiz rev: scrollable example list', !!doc.querySelector('#qbody .qexlist'));
  ok('quiz rev: all examples shown', doc.querySelectorAll('#qbody .qex2').length >= 5);
  ok('quiz rev: translation underlined, classical not', 
     doc.querySelector('#qbody').innerHTML.includes('<u class="mk">') &&
     !doc.querySelector('#qbody .qexko').innerHTML.includes('<u'));
  ok('quiz rev: meaning numbers map to examples', [...doc.querySelectorAll('#qbody .qexn')].every(n => /\d|・/.test(n.textContent)));
  // SRS-lite: あいまい persists, 覚えた clears weak + records date
  w.eval("localStorage.removeItem('koten_weak');weakSet.clear();mode='fwd';start(pool());idx=deck.findIndex(x=>x.no===2);show();revealAns();$('#againBtn').click();");
  ok('quiz: あいまい persists word to koten_weak',
     JSON.parse(w.localStorage.getItem('koten_weak') || '[]').includes(2));
  w.eval("idx=deck.findIndex(x=>x.no===2);show();revealAns();$('#knowBtn').click();");
  ok('quiz: 覚えた removes from koten_weak and records date',
     !JSON.parse(w.localStorage.getItem('koten_weak') || '[]').includes(2) &&
     Object.keys(JSON.parse(w.localStorage.getItem('koten_known_at') || '{}')).some(k => /^2:/.test(k)));
}

// ---- quiz multiple choice (四択) ----
{
  const q = run('quiz.html'), w = q.window, doc = w.document;
  w.eval("localStorage.clear();known.clear();weakSet.clear();mode='mc';$('#num').value='0';$('#order').value='no';start(pool());idx=deck.findIndex(x=>x.no===1);show();");
  const btns = [...doc.querySelectorAll('.mcbtn')];
  const w1meanings = w.eval('DB.words.find(x=>x.no===1).meanings');
  ok('quiz mc: 4 choices with exactly one correct',
     btns.length === 4 && btns.filter(b => b.dataset.ok === '1').length === 1);
  const okBtn = btns.find(b => b.dataset.ok === '1');
  ok('quiz mc: correct choice text is one of the word\'s meanings',
     w1meanings.some(m => okBtn.textContent.includes(m)));
  ok('quiz mc: distractors do not duplicate own meanings',
     btns.filter(b => b.dataset.ok !== '1').every(b => !w1meanings.some(m => b.textContent.includes(m))));
  // hint (blanked translation) hidden until tapped, same as fwd mode
  ok('quiz mc: hint hidden until tapped and contains blank',
     doc.querySelector('#qhint').style.display === 'none' &&
     doc.querySelector('#qhint').innerHTML.includes('blank'));
  // answering reveals checklist + 覚えた/あいまい buttons (no auto-recording)
  btns.find(b => b.dataset.ok !== '1').click();
  ok('quiz mc: answer reveals checklist and 覚えた/あいまい buttons',
     !!doc.querySelector('#reveal .mlist') &&
     !!doc.querySelector('#againBtn') && !!doc.querySelector('#knowBtn') &&
     !JSON.parse(w.localStorage.getItem('koten_weak') || '[]').includes(1));
  doc.querySelector('#againBtn').click();
  ok('quiz mc: あいまい persists weak',
     JSON.parse(w.localStorage.getItem('koten_weak') || '[]').includes(1));
  // 覚えた → known recorded, weak cleared
  w.eval("idx=deck.findIndex(x=>x.no===1);show();");
  doc.querySelector('.mcbtn[data-ok="1"]').click();
  doc.querySelector('#knowBtn').click();
  ok('quiz mc: 覚えた records known and clears weak',
     !JSON.parse(w.localStorage.getItem('koten_weak') || '[]').includes(1) &&
     Object.keys(JSON.parse(w.localStorage.getItem('koten_known_at') || '{}')).some(k => /^1:/.test(k)));
  // distractor difficulty: for 24 うし (形容詞・マイナス) distractors come from same-pos words
  w.eval("idx=deck.findIndex(x=>x.no===24);show();");
  const dist24 = [...doc.querySelectorAll('.mcbtn')].filter(b => b.dataset.ok !== '1')
    .map(b => b.textContent.slice(1));
  const posCount = dist24.filter(t =>
    w.eval(`(DB.words.find(x=>x.no!==24&&x.meanings.includes(${JSON.stringify(t)}))||{}).pos`) === '形容詞').length;
  ok('quiz mc: distractors match part of speech (≥2 of 3 adjectives for うし)', posCount >= 2);
}

// ---- PWA artifacts ----
{
  const mf = JSON.parse(fs.readFileSync(path.join(DIST, 'manifest.webmanifest'), 'utf8'));
  ok('pwa: manifest valid with icons', mf.name === '古文単語帳' && mf.icons.length >= 2);
  const sw = fs.readFileSync(path.join(DIST, 'sw.js'), 'utf8');
  ok('pwa: sw.js has versioned cache + core routes', /koten-\d+/.test(sw) && sw.includes("'./quiz'"));
  const html = fs.readFileSync(path.join(DIST, 'index.html'), 'utf8');
  ok('pwa: pages link manifest and register sw',
     html.includes('manifest.webmanifest') && html.includes('serviceWorker') &&
     ['icon-192.png', 'icon-512.png', 'apple-touch-icon.png'].every(f => fs.existsSync(path.join(DIST, f))));
}

// ---- quiz scope filter (すべて / 未習のみ) ----
{
  const q = run('quiz.html'), w = q.window, doc = w.document;
  ok('quiz: scope=すべて shows 330', doc.querySelector('#pcount').textContent === '330');
  w.eval("const w1=DB.words[0];for(let i=1;i<=totalSenses(w1);i++)addKnown(sk(1,i));saveKnown();$('#scope').value='unknown';updateCount();");
  ok('quiz: scope=未習のみ excludes fully-known words',
     doc.querySelector('#pcount').textContent === '329' && w.eval('pool().every(x=>x.no!==1)'));
  // partially known word stays in 未習のみ
  w.eval("delKnown(sk(2,1));addKnown(sk(2,1));delKnown(sk(2,2));saveKnown();updateCount();");
  ok('quiz: partially-known word remains in 未習のみ', w.eval('pool().some(x=>x.no===2)'));
}

// ---- quiz review queue (weak + expired known) ----
{
  const qr = new JSDOM(fs.readFileSync(path.join(DIST, 'quiz.html'), 'utf8'),
    { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://kobun.test/quiz.html',
      beforeParse(win) {
        win.localStorage.setItem('koten_known', JSON.stringify(['5:1']));
        win.localStorage.setItem('koten_known_at', JSON.stringify({ '5:1': Date.now() - 40 * 24 * 3600 * 1000 }));
        win.localStorage.setItem('koten_weak', JSON.stringify([9]));
      } });
  const rnos = qr.window.eval('reviewWords().map(w=>w.no)');
  ok('quiz: review queue = あいまい + 30日期限切れの既習',
     rnos.includes(5) && rnos.includes(9) && rnos.length === 2 &&
     !qr.window.document.querySelector('#reviewBox').hidden);
  qr.window.document.querySelector('#reviewStart').click();
  ok('quiz: 復習キューで始めるが復習デッキを組む', qr.window.eval('deck.length') === 2);
}

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
