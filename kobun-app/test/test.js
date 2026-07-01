// Smoke tests for the built pages. Run: npm i jsdom && node test/test.js
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');

const DIST = path.join(__dirname, '..', 'dist');
const run = f => new JSDOM(fs.readFileSync(path.join(DIST, f), 'utf8'),
  { runScripts: 'dangerously', pretendToBeVisual: true, url: 'file:///' + f });

let pass = 0, fail = 0;
const ok = (name, cond) => { (cond ? pass++ : fail++); console.log((cond ? 'PASS ' : 'FAIL ') + name); };

// ---- dictionary (index.html) ----
{
  const d = run('index.html'), doc = d.window.document;
  ok('index: 330 cards', doc.querySelectorAll('.card').length === 330);
  ok('index: subtitle shows total', /330/.test(doc.querySelector('#subtitle').textContent));
  ok('index: every card has a note preview', doc.querySelectorAll('.noteprev').length === 330);
  ok('index: all tags in one meta row (no themerow)', doc.querySelectorAll('.themerow').length === 0);
  ok('index: meanings are citation form (w7 みゆ has 見られる)',
     [...doc.querySelectorAll('#w7 .means li')].some(li => li.textContent === '見られる'));
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
  ok('quiz fwd: reveal lists citation-form meanings', doc.querySelectorAll('#reveal ol.means li').length >= 1);
  // reverse: numbered meaning prompt + all cloze examples + 訳 underlined, scrollable
  w.eval("$('#quit').click();mode='rev';start(pool());idx=deck.findIndex(x=>x.no===7);show();");
  ok('quiz rev: scrollable example list', !!doc.querySelector('#qbody .qexlist'));
  ok('quiz rev: all examples shown', doc.querySelectorAll('#qbody .qex2').length >= 5);
  ok('quiz rev: translation underlined, classical not', 
     doc.querySelector('#qbody').innerHTML.includes('<u class="mk">') &&
     !doc.querySelector('#qbody .qexko').innerHTML.includes('<u'));
  ok('quiz rev: meaning numbers map to examples', [...doc.querySelectorAll('#qbody .qexn')].every(n => /\d|・/.test(n.textContent)));
}

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
