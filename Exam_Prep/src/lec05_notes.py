"""Lecture 5 (Power BJT): complete study notes with previous-year solutions.

Writes ../build/lec05_notes.html; print with:
    node html_to_pdf.js ../build/lec05_notes.html ../notes/Lecture05_Power_BJT_Notes.pdf
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "build", "lec05_notes.html")

ARROW = '<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#222"/></marker></defs>'


def fig_structure():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270" width="80%" font-family="Arial" font-size="12">']
    x, w = 150, 220
    layers = [  # y, h, fill, label, doping, thickness
        (40, 30, "#f6c4c0", "n⁺ emitter", "10¹⁹ cm⁻³", "10 µm"),
        (70, 40, "#cfe3f7", "p base", "10¹⁶ cm⁻³", "5–20 µm"),
        (110, 80, "#fde9c8", "n⁻ collector drift region", "10¹⁴ cm⁻³", "50–200 µm"),
        (190, 50, "#f6c4c0", "n⁺ substrate (collector)", "10¹⁹ cm⁻³", "250 µm"),
    ]
    for y, h, col, lab, dop, th in layers:
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}" stroke="#222"/>')
        s.append(f'<text x="{x+10}" y="{y+h/2+4}" font-weight="bold">{lab}</text>')
        s.append(f'<text x="{x+w+12}" y="{y+h/2-2}" font-size="11">{dop}</text><text x="{x+w+12}" y="{y+h/2+12}" font-size="11" fill="#555">{th}</text>')
    # emitter only over part, base contact
    s.append(f'<rect x="{x+20}" y="28" width="60" height="12" fill="#999"/><text x="{x+28}" y="22">Emitter</text>')
    s.append(f'<rect x="{x+140}" y="58" width="60" height="12" fill="#999"/><text x="{x+150}" y="52">Base</text>')
    s.append(f'<rect x="{x}" y="240" width="{w}" height="10" fill="#999"/><text x="{x+70}" y="264">Collector</text>')
    s.append(f'<text x="10" y="150" font-size="11" fill="#c0392b">Drift region:</text><text x="10" y="164" font-size="11" fill="#c0392b">sets blocking voltage;</text><text x="10" y="178" font-size="11" fill="#c0392b">thicker = higher V,</text><text x="10" y="192" font-size="11" fill="#c0392b">but higher R_on</text>')
    s.append('<text x="380" y="20" font-size="11" fill="#555">doping / thickness</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_output():
    O = (70, 270)
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 320" width="92%" font-family="Arial" font-size="11">', ARROW]
    s.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="590" y2="{O[1]}" stroke="#222" marker-end="url(#ar)"/><text x="592" y="{O[1]+16}">v_CE</text>')
    s.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{O[0]}" y2="20" stroke="#222" marker-end="url(#ar)"/><text x="{O[0]-22}" y="18">i_C</text>')
    levels = [45, 95, 145, 195]
    for k, I in enumerate(levels):
        y = O[1] - I
        d = (f"M{O[0]},{O[1]} L{O[0]+18},{O[1]-0.65*I:.0f} Q{O[0]+40},{y+2} {O[0]+80},{y} "
             f"L{450},{y-6}")
        if k < 2:
            d += f" Q{485},{y-10} {500},{y-60}"   # primary breakdown upturn
        s.append(f'<path d="{d}" fill="none" stroke="#1d6fb8" stroke-width="2"/>')
        s.append(f'<text x="{455 if k>=2 else 380}" y="{y-12}" fill="#1d6fb8">I_B{k+1}</text>')
    # I_B = 0 curve (cut-off)
    s.append(f'<path d="M{O[0]},{O[1]-3} L460,{O[1]-6} Q492,{O[1]-8} 505,{O[1]-50}" fill="none" stroke="#1d6fb8" stroke-dasharray="4,3"/>')
    s.append(f'<text x="250" y="{O[1]-10}" fill="#555">I_B = 0: cut-off</text>')
    # region separators
    for xx in (O[0]+18, O[0]+80):
        s.append(f'<line x1="{xx}" y1="{O[1]}" x2="{xx}" y2="50" stroke="#999" stroke-dasharray="2,3"/>')
    s.append(f'<text x="{O[0]-6}" y="{O[1]+28}" fill="#c0392b">hard sat.</text>')
    s.append(f'<text x="{O[0]+40}" y="{O[1]+42}" fill="#c0392b">quasi-saturation</text>')
    s.append(f'<text x="250" y="{O[1]+28}" fill="#c0392b">active region</text>')
    # second breakdown boundary
    s.append('<path d="M330,32 Q390,80 420,140" fill="none" stroke="#c0392b" stroke-width="2" stroke-dasharray="6,4"/>')
    s.append('<text x="250" y="30" fill="#c0392b" font-weight="bold">second breakdown limit</text>')
    s.append('<text x="490" y="160" fill="#c0392b" font-weight="bold">primary</text><text x="490" y="173" fill="#c0392b" font-weight="bold">breakdown</text>')
    s.append(f'<line x1="500" y1="{O[1]}" x2="500" y2="{O[1]+6}" stroke="#222"/><text x="482" y="{O[1]+20}">BV_SUS</text>')
    s.append('<text x="220" y="312" fill="#555">I_B4 &gt; I_B3 &gt; I_B2 &gt; I_B1</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_soa():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 260" width="96%" font-family="Arial" font-size="11">', ARROW]
    # FBSOA (log-log)
    s.append('<text x="40" y="16" font-weight="bold" font-size="12">(a) FBSOA (log-log)</text>')
    s.append('<line x1="50" y1="230" x2="300" y2="230" stroke="#222" marker-end="url(#ar)"/><text x="250" y="250">log v_CE</text>')
    s.append('<line x1="50" y1="230" x2="50" y2="25" stroke="#222" marker-end="url(#ar)"/><text x="10" y="30">log i_C</text>')
    s.append('<path d="M50,50 L140,50 L200,100 L240,170 L240,230 L50,230 Z" fill="#1d6fb8" fill-opacity="0.18" stroke="#1d6fb8" stroke-width="2"/>')
    s.append('<text x="60" y="44">I_CM (max current)</text>')
    s.append('<text x="175" y="70">thermal limit</text><text x="175" y="82">(P_max)</text>')
    s.append('<text x="222" y="130" fill="#c0392b">second</text><text x="222" y="142" fill="#c0392b">breakdown</text>')
    s.append('<text x="230" y="225">BV_CEO</text>')
    s.append('<path d="M140,38 L230,80 L280,170 L280,230" fill="none" stroke="#2e8b57" stroke-dasharray="5,3"/><text x="245" y="58" fill="#2e8b57">pulsed / switching</text><text x="245" y="70" fill="#2e8b57">(expanded)</text>')
    s.append('<text x="90" y="170" fill="#0d3b66">safe area</text>')
    # RBSOA
    ox = 340
    s.append(f'<text x="{ox}" y="16" font-weight="bold" font-size="12">(b) RBSOA (turn-off)</text>')
    s.append(f'<line x1="{ox+10}" y1="230" x2="{ox+290}" y2="230" stroke="#222" marker-end="url(#ar)"/><text x="{ox+260}" y="250">v_CE</text>')
    s.append(f'<line x1="{ox+10}" y1="230" x2="{ox+10}" y2="25" stroke="#222" marker-end="url(#ar)"/><text x="{ox+16}" y="30">i_C</text>')
    s.append(f'<path d="M{ox+10},60 L{ox+150},60 Q{ox+190},70 {ox+200},230" fill="none" stroke="#1d6fb8" stroke-width="2"/>')
    s.append(f'<path d="M{ox+150},60 Q{ox+230},70 {ox+255},230" fill="none" stroke="#2e8b57" stroke-width="2"/>')
    s.append(f'<text x="{ox+20}" y="54">I_CM: limited by current only</text>')
    s.append(f'<line x1="{ox+150}" y1="60" x2="{ox+150}" y2="230" stroke="#999" stroke-dasharray="2,3"/><text x="{ox+135}" y="245">V_CEO</text>')
    s.append(f'<text x="{ox+92}" y="185" fill="#1d6fb8">V_BE(off) = 0 →</text>')
    s.append(f'<text x="{ox+222}" y="110" fill="#2e8b57">reverse</text><text x="{ox+222}" y="122" fill="#2e8b57">V_BE(off)</text>')
    s.append(f'<text x="{ox+20}" y="200" fill="#555">Reverse base bias</text><text x="{ox+20}" y="212" fill="#555">expands the RBSOA</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_switching():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 420" width="94%" font-family="Arial" font-size="11">', ARROW]
    t0, t1, t2, t3, t4, t5 = 90, 120, 170, 360, 410, 460
    # i_B
    yb = 70
    s.append(f'<line x1="60" y1="{yb}" x2="610" y2="{yb}" stroke="#222" marker-end="url(#ar)"/><text x="20" y="{yb-20}" font-weight="bold">i_B</text>')
    s.append(f'<path d="M60,{yb} L{t0},{yb} L{t0+3},{yb-40} L{t3},{yb-40} L{t3+3},{yb+25} L{t4},{yb+25} Q{t4+20},{yb+8} {t5},{yb} L600,{yb}" fill="none" stroke="#2e8b57" stroke-width="2.2"/>')
    s.append(f'<text x="{t0+10}" y="{yb-46}" fill="#2e8b57">I_B1 (forward drive)</text><text x="{t3+8}" y="{yb+40}" fill="#2e8b57">−I_B2 (reverse base current)</text>')
    # i_C
    yc, IC = 210, 90
    s.append(f'<line x1="60" y1="{yc}" x2="610" y2="{yc}" stroke="#222" marker-end="url(#ar)"/><text x="20" y="{yc-60}" font-weight="bold">i_C</text>')
    s.append(f'<path d="M60,{yc} L{t1},{yc} L{t2},{yc-IC} L{t4},{yc-IC} L{t5},{yc} L600,{yc}" fill="none" stroke="#1d6fb8" stroke-width="2.4"/>')
    s.append(f'<line x1="{t1-10}" y1="{yc-0.1*IC}" x2="{t2+10}" y2="{yc-0.1*IC}" stroke="#ccc" stroke-dasharray="2,2"/><line x1="{t1-10}" y1="{yc-0.9*IC}" x2="{t5+10}" y2="{yc-0.9*IC}" stroke="#ccc" stroke-dasharray="2,2"/>')
    s.append(f'<text x="30" y="{yc-0.9*IC+4}" font-size="10">0.9I_CS</text><text x="30" y="{yc-0.1*IC+4}" font-size="10">0.1I_CS</text>')
    s.append(f'<text x="{t2+40}" y="{yc-IC-6}" fill="#1d6fb8">I_CS (saturation current)</text>')
    # v_CE
    yv, V = 350, 80
    s.append(f'<line x1="60" y1="{yv}" x2="610" y2="{yv}" stroke="#222" marker-end="url(#ar)"/><text x="20" y="{yv-60}" font-weight="bold">v_CE</text>')
    s.append(f'<path d="M60,{yv-V} L{t1},{yv-V} L{t2},{yv-6} L{t4},{yv-6} L{t5},{yv-V} L600,{yv-V}" fill="none" stroke="#c0392b" stroke-width="2.2"/>')
    s.append(f'<text x="{t5+20}" y="{yv-V-6}" fill="#c0392b">V_CC</text><text x="{t2+40}" y="{yv-12}" fill="#c0392b">V_CE(sat)</text>')
    for xx in (t0, t1, t2, t3, t4, t5):
        s.append(f'<line x1="{xx}" y1="20" x2="{xx}" y2="{yv+6}" stroke="#bbb" stroke-dasharray="2,4"/>')
    for a, b, lab in ((t0, t1, "t_d"), (t1, t2, "t_r"), (t3, t4, "t_s"), (t4, t5, "t_f")):
        s.append(f'<text x="{(a+b)/2-8}" y="{yv+22}" font-weight="bold">{lab}</text>')
    s.append(f'<line x1="{t0}" y1="{yv+36}" x2="{t2}" y2="{yv+36}" stroke="#0d3b66" marker-end="url(#ar)"/><text x="{t0+20}" y="{yv+54}" fill="#0d3b66" font-weight="bold">t_on</text>')
    s.append(f'<line x1="{t3}" y1="{yv+36}" x2="{t5}" y2="{yv+36}" stroke="#0d3b66" marker-end="url(#ar)"/><text x="{t3+38}" y="{yv+54}" fill="#0d3b66" font-weight="bold">t_off</text>')
    s.append(f'<text x="{t0-30}" y="14" fill="#555">turn-on signal</text><text x="{t3-30}" y="14" fill="#555">turn-off signal</text>')
    s.append(f'<text x="{t2+20}" y="{yc+18}" fill="#555" font-size="10">switching loss = overlap of i_C and v_CE during t_r and t_f</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_basedrive():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 170" width="80%" font-family="Arial" font-size="11">', ARROW]
    y = 95
    s.append(f'<line x1="40" y1="{y}" x2="580" y2="{y}" stroke="#222" marker-end="url(#ar)"/><text x="572" y="{y+16}">t</text><text x="12" y="20" font-weight="bold">i_B</text>')
    s.append(f'<line x1="40" y1="{y+60}" x2="40" y2="15" stroke="#222" marker-end="url(#ar)"/>')
    s.append(f'<path d="M40,{y} L80,{y} L84,{y-65} L110,{y-65} Q130,{y-35} 160,{y-35} L360,{y-35} L420,{y+45} L470,{y+45} Q500,{y+10} 540,{y}" fill="none" stroke="#2e8b57" stroke-width="2.4"/>')
    s.append(f'<text x="88" y="{y-70}" fill="#2e8b57">I_B1: high, fast-rising (fast turn-on)</text>')
    s.append(f'<text x="200" y="{y-42}" fill="#2e8b57">I_B2: lower, holds quasi-saturation (less stored charge)</text>')
    s.append(f'<text x="365" y="{y+10}" fill="#555">controlled slope di_B/dt</text>')
    s.append(f'<text x="420" y="{y+60}" fill="#c0392b">−I_BR: sweeps out stored charge</text>')
    s.append('</svg>')
    return "\n".join(s)


CSS = """
@page { size: A4; margin: 14mm 14mm 16mm 14mm; }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 10pt; line-height: 1.45; color: #1b1b1b; }
h1 { color: #0d3b66; font-size: 20pt; margin: 0 0 2px; }
h2 { color: #fff; background: #0d3b66; font-size: 12.5pt; padding: 5px 10px; border-radius: 4px; margin: 16px 0 6px; break-after: avoid; }
h3 { color: #0d3b66; font-size: 11pt; margin: 10px 0 4px; break-after: avoid; }
.box { background: #f1f6fb; border-left: 4px solid #0d3b66; padding: 6px 12px; margin: 6px 0; break-inside: avoid; }
.key { background: #fff6e5; border-left: 4px solid #e08e0b; padding: 6px 12px; margin: 6px 0; break-inside: avoid; }
.ans { background: #eaf6ee; border: 2px solid #2e8b57; padding: 6px 12px; margin: 6px 0; border-radius: 4px; }
.q { border: 1px solid #c9d3de; border-top: 4px solid #c0392b; border-radius: 6px; padding: 6px 12px; margin: 10px 0; break-inside: avoid; }
.qh { font-weight: bold; color: #c0392b; }
.tag { display: inline-block; background: #c0392b; color: #fff; font-size: 8.5pt; padding: 1px 6px; border-radius: 3px; margin-right: 4px; }
.tag.b { background: #1d6fb8; }
table { border-collapse: collapse; width: 100%; font-size: 9.2pt; margin: 6px 0; break-inside: avoid; }
td, th { border: 1px solid #bbb; padding: 3px 6px; vertical-align: top; } th { background: #e6edf5; text-align: left; }
.fig { text-align: center; margin: 6px 0; break-inside: avoid; }
.cap { font-size: 8.8pt; color: #555; }
.mono { font-family: 'DejaVu Sans Mono', monospace; }
.pb { break-before: page; }
ul, ol { margin: 3px 0 3px 20px; padding: 0; } li { margin: 2px 0; }
.small { font-size: 8.8pt; color: #555; }
.flow { font-family: 'DejaVu Sans Mono', monospace; background: #fdf0ef; padding: 4px 8px; border-radius: 4px; display: inline-block; }
"""


def html():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Lecture 5 Power BJT Notes</title><style>{CSS}</style></head><body>

<h1>Lecture 5: Power BJT</h1>
<div class="small">EEE 339 Power Electronics · Complete study notes with previous-year solutions · Source: <i>class slides/Lecture 05 Power BJT.pdf</i> (Rashid ch. 4)</div>

<div class="key"><b>Exam priority (from the 2019 to 2024 papers):</b>
<ol>
<li><b>Switching characteristics</b> (t_d, t_r, t_s, t_f with waveforms). Asked in 2022 Q4b [6].</li>
<li><b>Second breakdown</b>, and why it occurs in BJTs and thyristors but not MOSFETs. Asked in 2024 Q3b [7].</li>
<li><b>Parallel operation</b>: why BJTs and SCRs cannot be paralleled easily but MOSFETs can. Asked in 2024 Q1d [5].</li>
<li><b>Comparison tables</b> (BJT vs MOSFET vs IGBT, and others). Asked in 2021 Q1a [7], 2022 Q4a [5], 2023 Q6d, 2019 TT-1.</li>
<li>Constructional features (2023 Q6c), modes / quasi-saturation, SOA, base drive.</li>
</ol>
Expected weight in your 60-mark paper: one theory sub-part of 3 to 6 marks in Part A (devices).</div>

<h2>1. Introduction and basics</h2>
<ul>
<li>The BJT was the traditional power switch. IGBTs and MOSFETs have now largely replaced it, but BJTs are still used where <b>cost</b> is the main concern.</li>
<li>It is a <b>current-controlled</b>, <b>bipolar</b> (minority-carrier) device: a base current I_B is needed to keep it on (I_C = βI_B in the active region).</li>
</ul>
<h3>Basics of a power BJT (slide 2)</h3>
<ul>
<li>Larger current and power handling than a small-signal BJT.</li>
<li>Higher voltage blocking in the OFF state; higher current in the ON state.</li>
<li><b>Vertically oriented</b> structure (current flows from top to bottom).</li>
<li>Emitter is very heavily doped compared with the base; even so, the current gain <b>β is low</b> (typically 5 to 20).</li>
<li>Large metal body (TO-3 style case) to dissipate heat.</li>
</ul>

<h2>2. Structure (constructional features)</h2>
<div class="fig">{fig_structure()}<div class="cap">Fig. 1: Vertical n⁺-p-n⁻-n⁺ structure of a power BJT (doping and thickness from the slide figure).</div></div>
<ul>
<li><b>Four layers:</b> n⁺ emitter, p base, <b>n⁻ collector drift region</b>, n⁺ substrate (collector contact).</li>
<li><b>Drift region</b> (lightly doped, thick): it increases the blocking (voltage) capacity. Thicker drift gives a higher breakdown voltage but a higher on-state resistance and causes the quasi-saturation region.</li>
<li><b>Vertical structure:</b> maximises the cross-section area for current, so on-resistance and thermal resistance are low.</li>
<li><b>Interdigitated emitter and base</b> (many narrow emitter fingers) to reduce emitter current crowding.</li>
<li>Low β, so a <b>Darlington</b> connection is often used to raise the gain.</li>
</ul>

<h2>3. Operating modes and output characteristics</h2>
<div class="fig">{fig_output()}<div class="cap">Fig. 2: Output characteristics of a power BJT showing hard saturation, quasi-saturation, active region, cut-off, primary breakdown and the second-breakdown limit.</div></div>
<table>
<tr><th style="width:20%">Mode</th><th style="width:32%">Junction bias</th><th>Notes</th></tr>
<tr><td><b>Cut-off</b></td><td>B-E reverse, C-B reverse</td><td>I_C ≈ 0 (leakage); switch OFF.</td></tr>
<tr><td><b>Active</b></td><td>B-E forward, C-B reverse</td><td>I_C = βI_B; v_CE large, so loss is high. In switching, cross it <b>as fast as possible</b>.</td></tr>
<tr><td><b>Quasi-saturation</b></td><td>B-E forward, C-B (just) forward</td><td>Extra region of <b>vertical</b> power BJTs: the drift region is not yet flooded with carriers, so v_CE is moderate. Less stored charge, so faster turn-off.</td></tr>
<tr><td><b>Hard saturation</b></td><td>B-E forward, C-B forward</td><td>Drift region fully conductivity-modulated; v_CE = V_CE(sat) is lowest (&lt; 0.7 V region per slide). Lowest conduction loss, but most stored charge.</td></tr>
</table>
<p>In switching, the BJT is used only in <b>saturation (ON)</b> and <b>cut-off (OFF)</b>; in both, the power loss v_CE·i_C is low.</p>

<h2>4. Breakdown: primary and second breakdown</h2>
<h3>Primary breakdown</h3>
<ul>
<li>Normal <b>avalanche breakdown of the collector-base junction</b>, with a large current.</li>
<li><b>BV_SUS</b> (sustaining voltage) is the limit: the maximum v_CE the transistor can sustain while carrying collector current.</li>
<li><b>BV_SUS &lt; BV_CEO &lt; BV_CBO</b>. BV_CEO and BV_CBO are the standoff voltages with zero or negative base current.</li>
</ul>
<h3>Second breakdown (secondary breakdown)</h3>
<ul>
<li>A failure mode seen as a <b>sudden (precipitous) drop of v_CE at large currents</b>.</li>
<li><b>Cause:</b> power dissipation is not uniform across the chip but concentrated in small regions. The local temperature rises quickly, and a BJT's resistance <b>falls</b> as temperature rises (negative temperature coefficient). So the hot spot conducts even more current, gets hotter still: <b>thermal runaway</b>.</li>
<li>The <b>hot spots</b> can melt and recrystallise the silicon, destroying the device.</li>
</ul>
<div class="flow">hot spot → lower resistance there → more current → more heat → hotter spot → … → melting</div>
<h3>How to avoid second breakdown (slide)</h3>
<ol>
<li>Keep power dissipation under control.</li>
<li>Use a controlled rate of change of base current during turn-off.</li>
<li>Use protective snubber circuits.</li>
<li>Keep the switching trajectory within the SOA boundaries.</li>
</ol>

<h2>5. Safe operating area (SOA)</h2>
<div class="fig">{fig_soa()}<div class="cap">Fig. 3: (a) Forward-bias SOA with its four boundaries. (b) Reverse-bias SOA at turn-off.</div></div>
<h3>FBSOA (forward-bias SOA, also simply called SOA)</h3>
<ul>
<li>Boundaries: <b>I_CM</b> (maximum current), the <b>thermal limit</b> (maximum power dissipation), the <b>second-breakdown limit</b>, and the maximum voltage <b>BV_CEO</b>.</li>
<li>The area <b>expands</b> for pulsed (switching) operation.</li>
</ul>
<h3>RBSOA (reverse-bias SOA, during turn-off)</h3>
<ul>
<li>Inductive loads give higher peak energy at turn-off than resistive loads, so second breakdown can happen if the RBSOA is exceeded.</li>
<li>A <b>reverse base current expands the RBSOA</b>.</li>
<li>Below V_CEO, the safe area does not depend on the reverse bias V_EB; it is limited only by I_C. Above V_CEO, the collector current must be controlled depending on the reverse-bias voltage.</li>
<li>Temperature derates the SOA.</li>
</ul>
<h3>Improving SOA capability</h3>
<p>SOA is set by peak power handling, which depends on current density and thermal density. Keep both low: a <b>wide base</b> limits current density, and <b>good heat sinking under the collector</b> lets the device withstand high peak power. Spreading power over a large silicon area gives the highest SOA. Failure starts from a hot spot at the weakest point.</p>

<h2>6. Switching characteristics</h2>
<div class="fig">{fig_switching()}<div class="cap">Fig. 4: Switching waveforms of a power BJT (resistive load): base current, collector current and collector-emitter voltage.</div></div>
<table>
<tr><th style="width:18%">Time</th><th>Meaning</th></tr>
<tr><td><b>Delay time t_d</b></td><td>From the base drive until i_C reaches 10%. Time to charge the <b>base-emitter junction capacitance</b> to forward bias. Reduced by a <b>larger base current with a high slope</b>.</td></tr>
<tr><td><b>Rise time t_r</b></td><td>i_C rises from 10% to 90% of I_CS (index "r" = 10 to 90%).</td></tr>
<tr><td><b>Turn-on time</b></td><td><b>t_on = t_d + t_r</b></td></tr>
<tr><td><b>Storage time t_s</b></td><td>After the turn-off signal, the time needed to <b>neutralise the minority carriers stored in the base and collector</b>. i_C stays almost constant. The most important BJT parameter; the main limit on switching speed.</td></tr>
<tr><td><b>Fall time t_f</b></td><td>i_C falls from 90% to 10%: crossing from saturation to cut-off. Reduced by a <b>negative base current</b> and by keeping the device in <b>quasi-saturation</b> (less stored charge).</td></tr>
<tr><td><b>Turn-off time</b></td><td><b>t_off = t_s + t_f</b></td></tr>
</table>
<p><b>Switching losses</b> occur during t_r and t_f, when v_CE and i_C are both large at the same time. Storage time and switching losses are the key issues with power BJTs.</p>

<h3>Base drive optimisation</h3>
<div class="fig">{fig_basedrive()}<div class="cap">Fig. 5: Ideal base-drive current waveform.</div></div>
<ul>
<li><b>I_B1</b>: high forward base current with a fast rise, so the BJT turns on quickly (small t_d and t_r).</li>
<li><b>I_B2</b>: lower holding current that keeps the BJT in <b>quasi-saturation</b>: conduction loss stays low and excess base charge is avoided.</li>
<li><b>−I_BR</b> with a controlled slope: a reverse base current sweeps out the stored charge, reducing t_s and t_f (and expanding the RBSOA).</li>
</ul>

<h2>7. Applications</h2>
<p>SMPS · power amplifiers · DC-to-AC inverters · relays · power control circuits.</p>

<div class="pb"></div>
<h2>8. Previous-year questions with full solutions</h2>

<div class="q"><span class="tag">2022 Q4(b)</span><span class="qh">Q. Explain the switching characteristics of a BJT. [6]</span>
<div class="ans">
<b>Answer.</b> Draw Fig. 4 (i_B, i_C and v_CE on the same time axis) and mark t_d, t_r, t_s, t_f.
<ul>
<li><b>Turn-on:</b> when the base current I_B1 is applied, i_C does not rise at once. During the <b>delay time t_d</b> the base-emitter junction capacitance charges up to forward bias. Then i_C rises from 10% to 90% of I_CS during the <b>rise time t_r</b>, while v_CE falls to V_CE(sat). <b>t_on = t_d + t_r</b>.</li>
<li><b>Turn-off:</b> when the base current is reversed (−I_B2), the excess minority carriers stored in the base and collector must first be removed. During this <b>storage time t_s</b>, i_C stays almost constant. Then i_C falls from 90% to 10% during the <b>fall time t_f</b> while v_CE rises to V_CC. <b>t_off = t_s + t_f</b>.</li>
<li><b>Losses:</b> during t_r and t_f both v_CE and i_C are large, so most switching loss occurs there.</li>
<li><b>Improving switching:</b> a large, fast-rising I_B1 reduces t_d and t_r; holding the device in quasi-saturation (I_B2) reduces stored charge; a negative base current reduces t_s and t_f.</li>
</ul>
</div></div>

<div class="q"><span class="tag">2024 Q3(b)</span><span class="qh">Q. What is secondary breakdown? Explain why secondary breakdown occurs in BJT and thyristors but not in MOSFETs. [7]</span>
<div class="ans">
<b>Secondary breakdown</b> is a destructive failure of a power transistor at high current and voltage, seen as a sudden collapse of v_CE while the current is large. It is caused by <b>localised thermal runaway</b> (hot spots), not by the normal avalanche of the junction (that is primary breakdown). Mark the second-breakdown limit on the output characteristics or SOA (Fig. 2 or 3a).<br><br>
<b>Why in BJTs and thyristors:</b>
<ul>
<li>They are <b>bipolar (minority-carrier) devices</b>. Their on-state resistance has a <b>negative temperature coefficient</b>: as temperature rises, more carriers are generated, so resistance falls.</li>
<li>Current is never perfectly uniform. A slightly hotter region therefore carries <b>more</b> current, which heats it further (<b>current crowding</b> / filamentation).</li>
<li>This positive feedback gives <b>local thermal runaway</b>; the hot spot melts and recrystallises the silicon and the device is destroyed. In thyristors the regenerative (latching) bipolar action makes the current filament worse.</li>
</ul>
<b>Why not in MOSFETs:</b>
<ul>
<li>A MOSFET is a <b>majority-carrier (unipolar)</b> device with no minority-carrier storage.</li>
<li>Its R_DS(on) has a <b>positive temperature coefficient</b>: carrier mobility falls as temperature rises, so resistance rises.</li>
<li>A hotter region therefore carries <b>less</b> current, and current shifts to cooler regions. The current spreads evenly over the chip (self-stabilising), so no hot spot or thermal runaway can form.</li>
</ul>
<span class="flow">BJT: T↑ → R↓ → I↑ → T↑↑ (runaway) &nbsp;&nbsp;|&nbsp;&nbsp; MOSFET: T↑ → R↑ → I↓ → T stable</span>
</div></div>

<div class="q"><span class="tag">2024 Q1(d)</span><span class="qh">Q. Explain why BJT and SCR cannot be operated in parallel, whereas MOSFETs can operate in parallel. [5]</span>
<div class="ans">
When devices are paralleled, they must <b>share the current equally</b>. Whether they do depends on the temperature coefficient of their on-state resistance.
<ul>
<li><b>BJT:</b> negative temperature coefficient (V_CE(sat) falls as temperature rises). The transistor with slightly lower V_CE(sat) takes more current, heats up, and its V_CE(sat) falls further, so it takes even more. This <b>current hogging</b> leads to thermal runaway of one device. Paralleling needs matched devices and <b>emitter ballast resistors</b>.</li>
<li><b>SCR:</b> also a bipolar device with negative temperature coefficient. In addition, SCRs have different on-state voltages and different turn-on times: the first one to latch takes the whole current. Paralleling needs series resistors or inductors and simultaneous, strong gate pulses.</li>
<li><b>MOSFET:</b> R_DS(on) has a <b>positive temperature coefficient</b>. The device carrying more current heats up, its resistance rises and its current falls. Current sharing is <b>automatic</b>, so MOSFETs can be paralleled easily; only matched gate drive (small gate resistors) is needed.</li>
</ul>
</div></div>

<div class="q"><span class="tag">2023 Q6(c)</span><span class="qh">Q. Mention the constructional features of a power BJT. [part of 8]</span>
<div class="ans">
Draw Fig. 1, then list:
<ol>
<li><b>Vertical structure</b> n⁺-p-n⁻-n⁺: the collector is at the bottom, so the current-carrying area is large.</li>
<li>Heavily doped n⁺ emitter (≈10¹⁹ cm⁻³, ≈10 µm), p base (≈10¹⁶, 5–20 µm).</li>
<li><b>Lightly doped n⁻ collector drift region</b> (≈10¹⁴, 50–200 µm): gives the high blocking voltage; causes quasi-saturation.</li>
<li>n⁺ substrate (≈250 µm) forms the collector contact.</li>
<li>Interdigitated base-emitter fingers to avoid emitter current crowding.</li>
<li>Low current gain β (5 to 20); Darlington pairs used for higher gain.</li>
<li>Large metal case / heat-sink mounting to dissipate heat.</li>
</ol>
</div></div>

<div class="q"><span class="tag">2022 Q4(a)</span><span class="qh">Q. Compare between BJT and MOSFET as a switch. [5]</span>
<div class="ans">
<table>
<tr><th>Feature</th><th>Power BJT</th><th>Power MOSFET</th></tr>
<tr><td>Control</td><td>Current-controlled (needs continuous base current)</td><td>Voltage-controlled (almost no gate current)</td></tr>
<tr><td>Input impedance</td><td>Low</td><td>Very high</td></tr>
<tr><td>Drive circuit</td><td>Complex, high drive power</td><td>Simple, very low drive power</td></tr>
<tr><td>Carriers</td><td>Bipolar (minority carriers): storage time</td><td>Unipolar (majority carriers): no storage time</td></tr>
<tr><td>Switching speed</td><td>Slow (up to about 10 kHz)</td><td>Very fast (hundreds of kHz to MHz)</td></tr>
<tr><td>On-state loss</td><td>Low V_CE(sat)</td><td>R_DS(on); high for high-voltage devices</td></tr>
<tr><td>Temperature coefficient</td><td>Negative: thermal runaway</td><td>Positive: stable</td></tr>
<tr><td>Second breakdown</td><td>Yes</td><td>No</td></tr>
<tr><td>Paralleling</td><td>Difficult (current hogging)</td><td>Easy (automatic sharing)</td></tr>
<tr><td>Cost / ratings</td><td>Cheap; medium voltage and current</td><td>Higher cost; best at low voltage</td></tr>
</table>
</div></div>

<div class="q"><span class="tag">2021 Q1(a)</span><span class="qh">Q. Differentiate among power BJT, MOSFET and IGBT in terms of power handling capacity, input impedance, switching speed, on-state resistance and blocking voltage. [7]</span>
<div class="ans">
<table>
<tr><th>Parameter</th><th>Power BJT</th><th>Power MOSFET</th><th>IGBT</th></tr>
<tr><td>Power handling capacity</td><td>Medium</td><td>Low to medium</td><td><b>High</b></td></tr>
<tr><td>Input impedance</td><td><b>Low</b> (current-driven)</td><td><b>Very high</b> (insulated gate)</td><td><b>Very high</b> (MOS gate)</td></tr>
<tr><td>Switching speed</td><td>Slow (≈ up to 10 kHz)</td><td><b>Fastest</b> (≈ 100 kHz to MHz)</td><td>Medium (≈ 20 to 50 kHz)</td></tr>
<tr><td>On-state resistance / drop</td><td>Low (V_CE(sat) ≈ 1–2 V)</td><td><b>High</b> at high voltage (R_DS(on) grows with voltage rating)</td><td><b>Low</b> (conductivity modulation)</td></tr>
<tr><td>Blocking voltage</td><td>Medium (≈ 1–1.5 kV)</td><td>Low to medium (≈ up to 1 kV)</td><td><b>High</b> (≈ up to 6.5 kV)</td></tr>
</table>
<span class="small">The ratings are approximate typical values; the examiner marks the comparison (low/medium/high), not exact numbers. Summary: the IGBT combines the MOSFET's high input impedance with the BJT's low on-state drop.</span>
</div></div>

<div class="q"><span class="tag">2019 TT-1 Q2</span><span class="qh">Q. Tabulate the similarity and dissimilarity between power BJT and IGBT in terms of power handling capacity, switching speed, on-state resistance and blocking voltage. [4]</span>
<div class="ans">
<b>Similarities:</b> both are three-terminal, controllable (turn-on and turn-off), unidirectional switches; both conduct by bipolar action (minority carriers), so both have a low on-state voltage drop; both have a vertical structure with an n⁻ drift region.<br>
<table>
<tr><th>Parameter</th><th>Power BJT</th><th>IGBT</th></tr>
<tr><td>Power handling</td><td>Medium</td><td>High</td></tr>
<tr><td>Switching speed</td><td>Slow (storage time)</td><td>Faster than BJT (tail current limits it)</td></tr>
<tr><td>On-state resistance</td><td>Low</td><td>Low (similar to BJT)</td></tr>
<tr><td>Blocking voltage</td><td>Medium (≈ 1–1.5 kV)</td><td>High (≈ up to 6.5 kV)</td></tr>
<tr><td>Drive</td><td>Current-driven, high drive power</td><td>Voltage-driven, very low drive power</td></tr>
</table>
</div></div>

<div class="q"><span class="tag">2023 Q6(d)</span><span class="qh">Q. Compare the following devices in terms of power capacity and switching speed: BJT, MOSFET, GTO, IGBT, MCT. [4]</span>
<div class="ans">
<table>
<tr><th>Device</th><th>Power capacity</th><th>Switching speed</th></tr>
<tr><td>GTO</td><td><b>Highest</b> (≈ 6 kV, 6 kA)</td><td><b>Slowest</b> (≈ 1 kHz)</td></tr>
<tr><td>IGBT</td><td>High</td><td>Medium-fast (≈ 20–50 kHz)</td></tr>
<tr><td>MCT</td><td>Medium-high</td><td>Medium-fast (≈ 20 kHz)</td></tr>
<tr><td>BJT</td><td>Medium</td><td>Slow-medium (≈ 10 kHz)</td></tr>
<tr><td>MOSFET</td><td><b>Lowest</b></td><td><b>Fastest</b> (≈ 100 kHz – 1 MHz)</td></tr>
</table>
Order of power: <b>GTO &gt; IGBT &gt; MCT &gt; BJT &gt; MOSFET</b>. Order of speed: <b>MOSFET &gt; IGBT ≈ MCT &gt; BJT &gt; GTO</b>.
</div></div>

<h2>9. Practice questions (likely next) with short answers</h2>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. What is quasi-saturation? Why does it occur only in power BJTs?</span>
<div class="ans">A region between the active region and hard saturation where both junctions are (just) forward biased but the lightly doped n⁻ drift region is not yet fully flooded with carriers, so v_CE is moderate. It occurs because power BJTs have the vertical n⁻ drift region; small-signal BJTs do not. Operating there reduces stored charge and speeds up turn-off.</div></div>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Draw and explain the FBSOA and RBSOA of a power BJT.</span>
<div class="ans">Draw Fig. 3. FBSOA: limited by I_CM, the thermal (P_max) line, the second-breakdown line and BV_CEO; it expands for pulsed operation. RBSOA: the turn-off limit; below V_CEO only I_C limits it; above V_CEO it depends on the reverse base bias, which expands it. Inductive turn-off is the critical case.</div></div>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Explain the modes of operation of a power BJT. / Explain primary breakdown and BV_SUS.</span>
<div class="ans">Use the table in Section 3 and Fig. 2. Primary breakdown = avalanche of the C-B junction; BV_SUS is the maximum v_CE with collector current flowing; BV_SUS &lt; BV_CEO &lt; BV_CBO.</div></div>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. How can the base drive improve the switching performance of a BJT? / How can second breakdown be avoided?</span>
<div class="ans">Base drive: I_B1 (high, fast) for fast turn-on; I_B2 to hold quasi-saturation; −I_BR with controlled slope to remove stored charge (Fig. 5). Second breakdown: control power dissipation, control di_B/dt at turn-off, use snubbers, keep the trajectory inside the SOA.</div></div>

<h2>10. One-look revision sheet</h2>
<table>
<tr><th style="width:32%">Item</th><th>Remember</th></tr>
<tr><td>Structure</td><td>n⁺ emitter / p base / <b>n⁻ drift</b> / n⁺ substrate; vertical; drift sets blocking voltage</td></tr>
<tr><td>Modes</td><td>Cut-off · Active · <b>Quasi-saturation</b> · Hard saturation</td></tr>
<tr><td>Breakdown</td><td>Primary = C-B avalanche (BV_SUS &lt; BV_CEO &lt; BV_CBO) · Second = hot spot thermal runaway</td></tr>
<tr><td>Avoid second breakdown</td><td>Limit power · control di_B/dt at turn-off · snubbers · stay in SOA</td></tr>
<tr><td>SOA</td><td>FBSOA: I_CM, thermal, second breakdown, BV_CEO · RBSOA: turn-off, expanded by reverse base bias</td></tr>
<tr><td>Switching</td><td><b>t_on = t_d + t_r · t_off = t_s + t_f</b>; t_s (stored charge) is the main limit</td></tr>
<tr><td>Base drive</td><td>I_B1 high → I_B2 hold (quasi-sat) → −I_BR sweep out</td></tr>
<tr><td>Temperature coefficient</td><td>BJT/SCR negative: runaway, no easy paralleling · MOSFET positive: stable, easy paralleling</td></tr>
<tr><td>Applications</td><td>SMPS, power amplifiers, inverters, relays, power control</td></tr>
</table>
</body></html>"""


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html())
    print("ok")
