"""Build the lecture-by-lecture guide (HTML for PDF printing) and the topic checklist (HTML).

Usage:  python3 build.py            -> writes ../build/guide.html and ../Topic_Checklist.html
        node print_pdf.js           -> prints ../build/guide.html to ../Lecture_by_Lecture_Study_Guide.pdf
"""
import html
import json
import os

from lectures import LECTURES, EXTERNAL_ZONE, DAYS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
e = html.escape
STARCH = "\u2605"

PART_A = [l for l in LECTURES if l["part"] == "A"]
PART_B = [l for l in LECTURES if l["part"] == "B"]
STAR = {3: "★★★ Must master", 2: "★★ Important", 1: "★ Light"}


def ul(items, cls=""):
    if not items:
        return ""
    return f'<ul class="{cls}">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def ol(items):
    return "<ol>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ol>"


# ----------------------------------------------------------------- PDF guide
def lecture_card(l):
    return f"""
<section class="lec p{l['part']}">
  <div class="lhead">
    <div class="lid">{e(l['id'])}</div>
    <div class="ltitle">{e(l['title'])}
      <div class="lmeta">Part {l['part']} &middot; {STAR[l['stars']]} &middot; {l['hours']:g} h &middot; Day {l['day']} &middot; {e(l['ref'])}</div>
      <div class="lfile">Slide: {e(l['file'])}</div>
    </div>
  </div>
  <div class="grid">
    <div><h4>Topics in this lecture ({len(l['topics'])})</h4>{ul(l['topics'], 'boxes')}</div>
    <div>
      <h4>Do with your own hand</h4>{ul(l['practice'], 'boxes')}
      {'<h4>Past-paper hits</h4>' + ul(l['past']) if l['past'] else ''}
      {'<h4>Formula sheet</h4>' + ul(l['formulas'], 'mono') if l['formulas'] else ''}
    </div>
  </div>
  <h4>How to study it</h4>{ol(l['how'])}
  <h4>Closed-book self-test (answer without looking)</h4>{ul(l['selftest'], 'boxes')}
</section>"""


def part_table(lst):
    rows = "".join(
        f"<tr><td>{e(l['id'])}</td><td>{e(l['title'])}</td><td>{'★' * l['stars']}</td><td>{l['hours']:g} h</td><td>Day {l['day']}</td></tr>"
        for l in lst)
    total = sum(l["hours"] for l in lst)
    return f"<table class='tbl'><tr><th>Lecture</th><th>Title</th><th>Priority</th><th>Time</th><th>When</th></tr>{rows}<tr><td></td><td><b>Total</b></td><td></td><td><b>{total:g} h</b></td><td></td></tr></table>"


def day_plan():
    out = ""
    for d, (title, lecs, end) in DAYS.items():
        items = [l for l in LECTURES if l["day"] == d]
        order = "".join(f"<li><b>{e(l['id'])}</b> {e(l['title'])} ({l['hours']:g} h)</li>" for l in items)
        extra = ""
        if d == 4:
            extra = "<li><b>External zone</b> (section 6), 1.5 h</li><li><b>Full mock exam</b>, 6 questions, real time limit</li><li><b>Formula sheet and waveform redraw</b>, 1.5 h</li>"
        hrs = sum(l["hours"] for l in items)
        out += f"<div class='day'><h3>{e(title)}</h3><p class='small'>Lectures: {e(lecs)} &middot; lecture study time {hrs:g} h</p><ol>{order}{extra}</ol><p><b>Close the day:</b> {e(end)}</p></div>"
    return out


def guide_html():
    a_cards = "".join(lecture_card(l) for l in PART_A)
    b_cards = "".join(lecture_card(l) for l in PART_B)
    ext = "".join(f"<tr><td><b>{e(t)}</b></td><td>{e(d)}</td></tr>" for t, d in EXTERNAL_ZONE)
    n_topics = sum(len(l["topics"]) for l in LECTURES)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Power Electronics: Lecture-by-Lecture Study Guide</title>
<style>
@page {{ size: A4; margin: 14mm 13mm 14mm 13mm; }}
body {{ font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 9.6pt; color: #1b1b1b; line-height: 1.38; }}
h1 {{ font-size: 21pt; margin: 0 0 4px; color: #0d3b66; }}
h2 {{ font-size: 15pt; color: #0d3b66; border-bottom: 2px solid #0d3b66; padding-bottom: 3px; margin-top: 18px; }}
h3 {{ font-size: 11.5pt; margin: 10px 0 4px; color: #0d3b66; }}
h4 {{ font-size: 9.6pt; margin: 8px 0 3px; color: #333; text-transform: uppercase; letter-spacing: .3px; }}
ul, ol {{ margin: 2px 0 4px 18px; padding: 0; }}
li {{ margin: 1px 0; }}
ul.boxes {{ list-style: none; margin-left: 2px; }}
ul.boxes li::before {{ content: '☐ '; color: #0d3b66; }}
ul.mono li {{ font-family: 'DejaVu Sans Mono', monospace; font-size: 8.6pt; }}
.small {{ font-size: 8.8pt; color: #555; }}
.cover {{ border: 3px solid #0d3b66; padding: 18px; border-radius: 6px; }}
.box {{ background: #f1f6fb; border-left: 4px solid #0d3b66; padding: 8px 12px; margin: 8px 0; }}
.warn {{ background: #fff6e5; border-left: 4px solid #e08e0b; padding: 8px 12px; margin: 8px 0; }}
.tbl {{ border-collapse: collapse; width: 100%; font-size: 8.8pt; margin: 6px 0; }}
.tbl td, .tbl th {{ border: 1px solid #bbb; padding: 3px 5px; vertical-align: top; }}
.tbl th {{ background: #0d3b66; color: #fff; text-align: left; }}
.lec {{ border: 1px solid #c9d3de; border-radius: 6px; padding: 8px 10px; margin: 10px 0; break-inside: auto; }}
.lec.pA {{ border-top: 5px solid #1d6fb8; }}
.lec.pB {{ border-top: 5px solid #c0392b; }}
.lhead {{ display: flex; gap: 10px; align-items: flex-start; break-after: avoid; }}
.lid {{ font-size: 15pt; font-weight: bold; color: #fff; background: #0d3b66; border-radius: 4px; padding: 3px 8px; min-width: 58px; text-align: center; }}
.pB .lid {{ background: #c0392b; }}
.ltitle {{ font-weight: bold; font-size: 11.2pt; }}
.lmeta {{ font-weight: normal; font-size: 8.8pt; color: #444; }}
.lfile {{ font-weight: normal; font-size: 8.2pt; color: #777; }}
.grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
.day {{ border: 1px solid #ccc; border-radius: 6px; padding: 6px 10px; margin: 8px 0; break-inside: avoid; }}
.pb {{ break-before: page; }}
.partbanner {{ padding: 8px 12px; color: #fff; border-radius: 6px; font-size: 13pt; font-weight: bold; }}
.bA {{ background: #1d6fb8; }} .bB {{ background: #c0392b; }}
</style></head><body>

<div class="cover">
<h1>EEE 339 Power Electronics</h1>
<div style="font-size:13pt;font-weight:bold;">Lecture-by-Lecture Study Guide for the Semester Final (Batch 22)</div>
<p class="small">Built from all 35 lectures in <i>class slides/</i>, the 2021 to 2024 finals, the Batch 19/20 term tests, your batch's Assessments #5 to #7, the syllabus and the course outcomes. {len(LECTURES)} lecture units, {n_topics} topics.</p>
<div class="box"><b>Exam format:</b> 60 marks. Part A (30) and Part B (30). Each part has 4 questions: Q1 and Q2 are compulsory, then answer Q3 <i>or</i> Q4. You write 3 questions per part, about 10 marks each, 6 questions in total.</div>
<div class="box"><b>Target: 80 to 90% (48 to 54 marks).</b> Six questions of about 10 marks. Each lost question costs about 10 marks. So the plan is: (1) every ★★★ lecture fully mastered, which covers all of the compulsory questions we can predict; (2) every ★★ lecture learned well enough for the optional choice; (3) one session on the external zone so a surprise sub-part is still worth partial marks.</div>
</div>

<h2>1. How the paper is set, and why this plan works</h2>
<ul>
<li><b>About 60% comes from the teacher's slides and notes, about 20% from previous papers, about 20% is the external examiner's choice.</b></li>
<li>In the <b>2024 paper (Batch 21, same teacher, same slides)</b>, 7 numericals were slide examples copied with the same numbers: Rashid Ex 3.4 (L19), Rashid Ex 10.4 (L22), Hart Ex 3-5 (L17), Hart Ex 4-1 (L18), Hart Ex 6-6 (L13), and both AC-controller class examples (L31_32). About 91% of the paper's marks came from the slides.</li>
<li>The external examiner's part repeated older papers (the parallel resonant converter came word for word from 2022) or took textbook items next to the slides (for example the SCR gate-pulse-width numerical).</li>
<li><b>Inverters got only 5 marks in 2024</b>, but your batch had two inverter assessments (#5 and #6). Expect a full inverter question in Part B.</li>
<li>Topics asked in <b>all four</b> years: SCR two-transistor model, cycloconverter, device comparison, full-wave rectifiers, 3-phase rectifiers, buck / buck-boost numericals.</li>
</ul>

<h2>2. Part A and Part B: how the lectures are divided</h2>
<p>This split follows the 2024 paper (the same teacher). In 2024, Part A held devices and Rashid-style rectifier questions; Part B held Hart DC-DC and rectifier examples, resonant, inverters, AC-AC, cycloconverter and solar. The boundary is not strict, so <b>L09 (linear regulator vs SMPS), L17 and L18 (Hart rectifier examples) can appear in either part.</b> Prepare everything; use the split to plan and to balance your time.</p>
<div class="partbanner bA">PART A (30 marks): Power Devices + Rectifiers</div>
{part_table(PART_A)}
<div class="partbanner bB">PART B (30 marks): DC-DC, Resonant, Inverters, AC-AC, Cycloconverter, Solar</div>
{part_table(PART_B)}

<h2>3. How to study each lecture: the 5-step method</h2>
<ol>
<li><b>Skim (5 min).</b> Read the lecture's topic list in this guide, then flip through the slide once.</li>
<li><b>Redraw (15 to 20 min).</b> Close the slide. Draw every circuit and waveform yourself. Waveforms must be drawn "with proper alignment" (stacked on the same ωt axis). Many marks depend on this.</li>
<li><b>Derive (15 to 20 min).</b> Write each derivation from start to boxed result without looking. If you get stuck, look once, then start again from the top.</li>
<li><b>Solve (20 to 30 min).</b> Solve every "Do with your own hand" item with the book closed. Compare every number with this guide.</li>
<li><b>Recall (5 min).</b> Answer the self-test questions out loud or on paper. Tick the boxes only when you can do it without help. Copy formulas onto your one-page formula sheet.</li>
</ol>
<div class="warn"><b>Rules for 4 days:</b> Do not read passively. Writing beats reading. Study in 50-minute blocks with 10-minute breaks. Use the checklist file (Topic_Checklist.html) to tick off every topic. Sleep at least 6 hours each night; memory consolidates during sleep.</div>

<h2>4. Four-day timetable</h2>
{day_plan()}

<div class="pb"></div>
<h2>5. Lecture-by-lecture guide</h2>
<div class="partbanner bA">PART A: Power Devices (L01 to L08) and Rectifiers (L16 to L22)</div>
{a_cards}
<div class="pb"></div>
<div class="partbanner bB">PART B: DC-DC (L09 to L15), Resonant (L23 to L24), Inverters (L25 to L30), AC-AC and Cycloconverter (L31 to L34), Solar (L35)</div>
{b_cards}

<div class="pb"></div>
<h2>6. External-examiner zone (not in the slides, but asked before)</h2>
<p>Give these one session on Day 4. Even partial knowledge here can save 3 to 5 marks.</p>
<table class="tbl"><tr><th style="width:34%">Topic</th><th>What to know</th></tr>{ext}</table>

<h2>7. In the exam hall</h2>
<ol>
<li>Read the whole paper first (3 minutes). Choose the optional question in each part by asking which one has more numericals you have practised.</li>
<li>Time: about 2 minutes per mark. A 10-mark question gets about 20 minutes. Keep 10 minutes at the end to review.</li>
<li>Start each part with your strongest compulsory question.</li>
<li>Derivations: circuit, then equivalent circuits, then aligned waveforms, then equations, then boxed result.</li>
<li>Numericals: formula, substitution, answer with unit, boxed. Partial marks depend on the formula line.</li>
<li>Compare / differentiate: always a table of at least 5 rows.</li>
<li>Surprise question: write the governing equation and draw the circuit anyway. Never leave a sub-part blank.</li>
</ol>
<p class="small">Numbers in this guide were checked against the solutions printed in the slides where available; the parallel resonant answer is our own calculation (the topic is not in the slides).</p>
</body></html>"""


# ----------------------------------------------------------------- checklist
def checklist_html():
    data = []
    for l in LECTURES:
        items = []
        for kind, lst in (("topic", l["topics"]), ("practice", l["practice"]), ("selftest", l["selftest"])):
            for i, text in enumerate(lst):
                items.append({"id": f"{l['id']}-{kind[0]}{i}", "kind": kind, "text": text})
        data.append({k: l[k] for k in ("id", "title", "part", "stars", "hours", "day", "file", "ref")} | {"past": l["past"], "formulas": l["formulas"], "items": items})
    ext = [{"id": f"EXT-{i}", "kind": "topic", "text": t, "note": d} for i, (t, d) in enumerate(EXTERNAL_ZONE)]
    days = {str(k): v for k, v in DAYS.items()}
    payload = json.dumps({"lectures": data, "external": ext, "days": days}, ensure_ascii=False)
    return CHECKLIST_TEMPLATE.replace("__DATA__", payload)


CHECKLIST_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Power Electronics Final: Topic Checklist</title>
<style>
:root { --a:#1d6fb8; --b:#c0392b; --ink:#1b1b1b; --muted:#666; --bg:#f6f8fb; --card:#fff; --line:#dde3ea; --ok:#2e8b57; }
@media (prefers-color-scheme: dark) { :root { --ink:#e8e8e8; --muted:#a8a8a8; --bg:#14171c; --card:#1d222a; --line:#2f3743; } }
* { box-sizing: border-box; }
body { margin:0; font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; background:var(--bg); color:var(--ink); }
header { position: sticky; top:0; z-index:5; background:var(--card); border-bottom:1px solid var(--line); padding:10px 14px; }
h1 { font-size:18px; margin:0 0 6px; }
.bars { display:grid; grid-template-columns: repeat(3, 1fr); gap:8px; }
.bar { font-size:12px; }
.track { height:10px; background:var(--line); border-radius:6px; overflow:hidden; margin-top:3px; }
.fill { height:100%; width:0; background:var(--ok); transition: width .25s; }
.fill.a { background:var(--a); } .fill.b { background:var(--b); }
.controls { display:flex; flex-wrap:wrap; gap:6px; margin-top:8px; }
.controls button, .controls select { font: inherit; font-size:13px; padding:5px 10px; border-radius:6px; border:1px solid var(--line); background:var(--card); color:var(--ink); cursor:pointer; }
.controls button.on { background:var(--ink); color:var(--card); }
main { max-width: 980px; margin: 0 auto; padding: 12px; }
.part { margin:16px 0 6px; padding:8px 12px; color:#fff; border-radius:8px; font-weight:600; }
.part.A { background:var(--a); } .part.B { background:var(--b); } .part.X { background:#6b4fa0; }
details.lec { background:var(--card); border:1px solid var(--line); border-radius:8px; margin:8px 0; }
details.lec[open] { box-shadow: 0 1px 6px rgba(0,0,0,.06); }
summary { list-style:none; cursor:pointer; padding:10px 12px; display:flex; gap:10px; align-items:center; }
summary::-webkit-details-marker { display:none; }
.tag { font-weight:700; color:#fff; border-radius:5px; padding:2px 7px; font-size:13px; min-width:58px; text-align:center; }
.tag.A { background:var(--a); } .tag.B { background:var(--b); } .tag.X { background:#6b4fa0; }
.st { flex:1; }
.st .t { font-weight:600; font-size:14.5px; }
.st .m { font-size:12px; color:var(--muted); }
.pct { font-size:12px; font-weight:700; min-width:44px; text-align:right; }
.mini { width:70px; height:6px; background:var(--line); border-radius:4px; overflow:hidden; }
.mini > div { height:100%; background:var(--ok); width:0; }
.done .t { text-decoration: line-through; color: var(--muted); }
.body { padding: 0 14px 12px 14px; }
.grp { font-size:11.5px; text-transform:uppercase; letter-spacing:.4px; color:var(--muted); margin:10px 0 4px; font-weight:700; }
label.item { display:flex; gap:8px; align-items:flex-start; padding:4px 2px; border-bottom:1px dashed var(--line); font-size:14px; cursor:pointer; }
label.item input { margin-top:3px; transform: scale(1.15); }
label.item.checked span { color: var(--muted); text-decoration: line-through; }
.note { font-size:12.5px; color:var(--muted); margin:2px 0 0 26px; }
.past li, .form li { font-size:13px; margin:2px 0; }
.form li { font-family: ui-monospace, Consolas, monospace; font-size:12.5px; }
.hide { display:none !important; }
.daynote { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:8px 12px; font-size:13.5px; margin:8px 0; }
footer { text-align:center; color:var(--muted); font-size:12px; padding:20px; }
@media print { header { position: static; } details.lec { break-inside: avoid; } .controls { display:none; } }
@media (max-width: 640px) { .bars { grid-template-columns: 1fr; } .mini { display:none; } }
</style></head>
<body>
<header>
  <h1>EEE 339 Power Electronics &middot; Semester Final Topic Checklist</h1>
  <div class="bars">
    <div class="bar">Overall <b id="pAll">0%</b> <span id="cAll"></span><div class="track"><div class="fill" id="fAll"></div></div></div>
    <div class="bar">Part A <b id="pA">0%</b> <span id="cA"></span><div class="track"><div class="fill a" id="fA"></div></div></div>
    <div class="bar">Part B <b id="pB">0%</b> <span id="cB"></span><div class="track"><div class="fill b" id="fB"></div></div></div>
  </div>
  <div class="controls">
    <button data-f="all" class="on">All</button>
    <button data-f="A">Part A</button>
    <button data-f="B">Part B</button>
    <button data-f="X">External zone</button>
    <select id="day"><option value="">Any day</option><option value="1">Day 1</option><option value="2">Day 2</option><option value="3">Day 3</option><option value="4">Day 4</option></select>
    <select id="star"><option value="0">Any priority</option><option value="3">&#9733;&#9733;&#9733; only</option><option value="2">&#9733;&#9733; and up</option></select>
    <button id="todo">Hide finished</button>
    <button id="expand">Expand all</button>
    <button id="reset" title="Clear every tick">Reset</button>
  </div>
</header>
<main id="main"></main>
<footer>Ticks are saved in this browser (localStorage). Open the same file in the same browser to continue.</footer>
<script>
const DATA = __DATA__;
const KEY = 'pe-final-checklist-v1';
let state = {};
try { state = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { state = {}; }
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} };
const stars = n => '★'.repeat(n);
const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const groupName = {topic:'Topics in this lecture', practice:'Do with your own hand (derive / solve)', selftest:'Closed-book self-test'};

function lecBlock(l, part) {
  const groups = ['topic','practice','selftest'].map(k => {
    const its = l.items.filter(i => i.kind === k);
    if (!its.length) return '';
    return `<div class="grp">${groupName[k]}</div>` + its.map(i =>
      `<label class="item" data-id="${i.id}"><input type="checkbox" data-id="${i.id}"><span>${esc(i.text)}${i.note ? `<div class="note">${esc(i.note)}</div>` : ''}</span></label>`).join('');
  }).join('');
  const past = l.past && l.past.length ? `<div class="grp">Past-paper hits</div><ul class="past">${l.past.map(p => `<li>${esc(p)}</li>`).join('')}</ul>` : '';
  const form = l.formulas && l.formulas.length ? `<div class="grp">Formula sheet</div><ul class="form">${l.formulas.map(p => `<li>${esc(p)}</li>`).join('')}</ul>` : '';
  const meta = part === 'X' ? 'Not in slides. Asked in earlier papers.' :
    `Part ${l.part} &middot; ${stars(l.stars)} &middot; ${l.hours} h &middot; Day ${l.day} &middot; ${esc(l.ref)}`;
  return `<details class="lec" data-part="${part}" data-day="${l.day || ''}" data-stars="${l.stars || 0}" data-lec="${l.id}">
    <summary><span class="tag ${part}">${esc(l.id)}</span><span class="st"><div class="t">${esc(l.title)}</div><div class="m">${meta}</div></span>
    <span class="mini"><div></div></span><span class="pct">0%</span></summary>
    <div class="body">${l.file ? `<div class="m" style="font-size:12px;color:var(--muted)">Slide: ${esc(l.file)}</div>` : ''}${groups}${past}${form}</div></details>`;
}

function render() {
  const A = DATA.lectures.filter(l => l.part === 'A'), B = DATA.lectures.filter(l => l.part === 'B');
  let h = '';
  h += `<div class="daynote"><b>4-day plan.</b> ` + Object.entries(DATA.days).map(([d, v]) => `<div><b>${esc(v[0])}</b>: ${esc(v[1])}. <i>${esc(v[2])}</i></div>`).join('') + `</div>`;
  h += `<div class="part A">PART A (30 marks): Power Devices + Rectifiers</div>` + A.map(l => lecBlock(l, 'A')).join('');
  h += `<div class="part B">PART B (30 marks): DC-DC, Resonant, Inverters, AC-AC, Cycloconverter, Solar</div>` + B.map(l => lecBlock(l, 'B')).join('');
  h += `<div class="part X">External-examiner zone (Day 4)</div>` + lecBlock({id:'EXT', title:'Topics not in the slides that were asked before', items: DATA.external}, 'X');
  document.getElementById('main').innerHTML = h;
  document.querySelectorAll('input[type=checkbox]').forEach(cb => {
    cb.checked = !!state[cb.dataset.id];
    cb.closest('label').classList.toggle('checked', cb.checked);
    cb.addEventListener('change', () => {
      if (cb.checked) state[cb.dataset.id] = 1; else delete state[cb.dataset.id];
      cb.closest('label').classList.toggle('checked', cb.checked);
      save(); update();
    });
  });
  update();
}

function pct(n, d) { return d ? Math.round(100 * n / d) : 0; }
function update() {
  const tot = {all:[0,0], A:[0,0], B:[0,0]};
  document.querySelectorAll('details.lec').forEach(d => {
    const boxes = d.querySelectorAll('input[type=checkbox]');
    const done = [...boxes].filter(b => b.checked).length;
    const p = pct(done, boxes.length);
    d.querySelector('.pct').textContent = p + '%';
    d.querySelector('.mini > div').style.width = p + '%';
    d.querySelector('.st').classList.toggle('done', p === 100);
    d.dataset.complete = p === 100 ? '1' : '0';
    tot.all[0] += done; tot.all[1] += boxes.length;
    const part = d.dataset.part;
    if (tot[part]) { tot[part][0] += done; tot[part][1] += boxes.length; }
  });
  for (const k of ['All','A','B']) {
    const t = tot[k === 'All' ? 'all' : k];
    const p = pct(t[0], t[1]);
    document.getElementById('p' + k).textContent = p + '%';
    document.getElementById('c' + k).textContent = `(${t[0]}/${t[1]})`;
    document.getElementById('f' + k).style.width = p + '%';
  }
  applyFilter();
}

let filt = 'all', hideDone = false;
function applyFilter() {
  const day = document.getElementById('day').value, st = +document.getElementById('star').value;
  document.querySelectorAll('details.lec').forEach(d => {
    let show = filt === 'all' || d.dataset.part === filt;
    if (day && d.dataset.day !== day) show = false;
    if (st && +d.dataset.stars < st) show = false;
    if (hideDone && d.dataset.complete === '1') show = false;
    d.classList.toggle('hide', !show);
  });
  document.querySelectorAll('.part').forEach(p => {
    const cls = p.classList.contains('A') ? 'A' : p.classList.contains('B') ? 'B' : 'X';
    p.classList.toggle('hide', filt !== 'all' && filt !== cls);
  });
}
document.querySelectorAll('.controls button[data-f]').forEach(b => b.addEventListener('click', () => {
  document.querySelectorAll('.controls button[data-f]').forEach(x => x.classList.remove('on'));
  b.classList.add('on'); filt = b.dataset.f; applyFilter();
}));
document.getElementById('day').addEventListener('change', applyFilter);
document.getElementById('star').addEventListener('change', applyFilter);
document.getElementById('todo').addEventListener('click', e => { hideDone = !hideDone; e.target.classList.toggle('on', hideDone); applyFilter(); });
document.getElementById('expand').addEventListener('click', e => {
  const open = e.target.textContent === 'Expand all';
  document.querySelectorAll('details.lec').forEach(d => d.open = open);
  e.target.textContent = open ? 'Collapse all' : 'Expand all';
});
document.getElementById('reset').addEventListener('click', () => {
  if (confirm('Clear every tick?')) { state = {}; save(); render(); }
});
render();
</script>
</body></html>
"""

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "build"), exist_ok=True)
    with open(os.path.join(OUT, "build", "guide.html"), "w", encoding="utf-8") as f:
        f.write(guide_html())
    with open(os.path.join(OUT, "Topic_Checklist.html"), "w", encoding="utf-8") as f:
        f.write(checklist_html())
    n = sum(len(l["topics"]) + len(l["practice"]) + len(l["selftest"]) for l in LECTURES) + len(EXTERNAL_ZONE)
    print(f"lectures={len(LECTURES)} checklist_items={n}")
