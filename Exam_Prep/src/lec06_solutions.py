"""Lecture 6 (Power MOSFET and IGBT): previous-year question solutions.

Writes ../build/lec06_solutions.html; print with:
    node html_to_pdf.js ../build/lec06_solutions.html ../notes/Lecture06_MOSFET_IGBT_PrevYear_Solutions.pdf
"""
import os

from lec05_notes import CSS, ARROW

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "build", "lec06_solutions.html")

P_PLUS, N_PLUS, N_MINUS, P_BODY, METAL, OXIDE, POLY = "#f6c4c0", "#f3a6a0", "#fde9c8", "#cfe3f7", "#9a9a9a", "#ffffff", "#b9a3d6"


def rect(x, y, w, h, fill, label="", lx=None, ly=None, size=11, bold=False):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#222" stroke-width="1"/>'
    if label:
        s += f'<text x="{lx if lx is not None else x+6}" y="{ly if ly is not None else y+h/2+4}" font-size="{size}"{" font-weight=\"bold\"" if bold else ""}>{label}</text>'
    return s


def fig_igbt_cell():
    """Full IGBT cell (PT type) cross-section."""
    X, W = 120, 360
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="88%" font-family="Arial" font-size="11">', ARROW]
    s.append(rect(X, 300, W, 30, P_PLUS, "p⁺ substrate (injecting layer)", X + 100, 319, bold=True))
    s.append(rect(X, 275, W, 25, N_PLUS, "n⁺ buffer layer (PT only)", X + 110, 292))
    s.append(rect(X, 100, W, 175, N_MINUS, "n⁻ drift region", X + 140, 200, bold=True))
    # p bodies
    s.append(rect(X, 60, 135, 70, P_BODY))
    s.append(rect(X + W - 135, 60, 135, 70, P_BODY))
    s.append(f'<text x="{X+10}" y="118" font-weight="bold">p body</text><text x="{X+W-60}" y="118" font-weight="bold">p body</text>')
    # n+ emitters
    s.append(rect(X + 55, 60, 60, 22, N_PLUS, "n⁺", X + 78, 75))
    s.append(rect(X + W - 115, 60, 60, 22, N_PLUS, "n⁺", X + W - 92, 75))
    # emitter metal
    s.append(rect(X, 46, 90, 14, METAL))
    s.append(rect(X + W - 90, 46, 90, 14, METAL))
    s.append(f'<line x1="{X+45}" y1="46" x2="{X+45}" y2="24" stroke="#222"/><line x1="{X+W-45}" y1="46" x2="{X+W-45}" y2="24" stroke="#222"/><line x1="{X+45}" y1="24" x2="{X+W-45}" y2="24" stroke="#222"/><text x="{X+W/2-30}" y="18" font-weight="bold">Emitter (E)</text>')
    # gate oxide + poly
    s.append(rect(X + 100, 54, W - 200, 6, OXIDE))
    s.append(rect(X + 105, 38, W - 210, 16, POLY, "Gate (G)", X + W / 2 - 24, 50, bold=True))
    # collector metal
    s.append(rect(X, 330, W, 10, METAL))
    s.append(f'<text x="{X+W/2-36}" y="355" font-weight="bold">Collector (C)</text>')
    # channel marks
    for cx in (X + 122, X + W - 132):
        s.append(f'<rect x="{cx}" y="60" width="10" height="4" fill="#c0392b"/>')
    s.append(f'<text x="{X+W+8}" y="70" fill="#c0392b">← n-channel</text>')
    s.append(f'<text x="{X+W+8}" y="52" font-size="10" fill="#555">← SiO₂ (oxide)</text>')
    # carrier arrows
    s.append(f'<line x1="{X+140}" y1="70" x2="{X+165}" y2="170" stroke="#1d6fb8" stroke-width="2" marker-end="url(#ar)"/><text x="{X+168}" y="150" fill="#1d6fb8">e⁻</text>')
    s.append(f'<line x1="{X+220}" y1="295" x2="{X+220}" y2="140" stroke="#c0392b" stroke-width="2" marker-end="url(#ar)"/><text x="{X+226}" y="240" fill="#c0392b">holes (h⁺) injected</text>')
    # left labels
    s.append(f'<text x="10" y="200" font-size="10" fill="#555">thick, lightly</text><text x="10" y="212" font-size="10" fill="#555">doped: blocks</text><text x="10" y="224" font-size="10" fill="#555">the voltage</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_pt_npt():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="90%" font-family="Arial" font-size="11">', ARROW]
    for i, (title, buffer, drift_h, sub_h, field) in enumerate((
            ("Punch-through (PT)", True, 120, 70, "trap"),
            ("Non-punch-through (NPT)", False, 190, 22, "tri"))):
        ox = 20 + i * 320
        y = 40
        s.append(f'<text x="{ox}" y="20" font-weight="bold" font-size="12">{title}</text>')
        s.append(rect(ox, y, 150, 22, P_BODY, "p body / n⁺ emitter", ox + 6, y + 15))
        y += 22
        s.append(rect(ox, y, 150, drift_h, N_MINUS, "n⁻ drift", ox + 45, y + drift_h / 2 + 4, bold=True))
        y += drift_h
        if buffer:
            s.append(rect(ox, y, 150, 22, N_PLUS, "n⁺ buffer", ox + 45, y + 15))
            y += 22
        s.append(rect(ox, y, 150, sub_h, P_PLUS, "p⁺ collector" + (" (thick substrate)" if i == 0 else " (thin)"), ox + 4, y + sub_h / 2 + 4))
        # field profile
        fx = ox + 170
        top, bot = 62, 62 + drift_h
        s.append(f'<line x1="{fx}" y1="{top}" x2="{fx}" y2="{bot+30}" stroke="#222"/><text x="{fx+4}" y="{top-6}" font-size="10">E-field</text>')
        if field == "trap":
            s.append(f'<polygon points="{fx},{top} {fx+110},{top} {fx+60},{bot} {fx},{bot}" fill="#c0392b" fill-opacity="0.25" stroke="#c0392b"/>')
            s.append(f'<text x="{fx+4}" y="{bot+22}" font-size="10" fill="#c0392b">trapezoidal: field</text><text x="{fx+4}" y="{bot+34}" font-size="10" fill="#c0392b">reaches the buffer</text>')
        else:
            s.append(f'<polygon points="{fx},{top} {fx+110},{top} {fx},{top+drift_h*0.85}" fill="#c0392b" fill-opacity="0.25" stroke="#c0392b"/>')
            s.append(f'<text x="{fx+4}" y="{bot+22}" font-size="10" fill="#c0392b">triangular: field ends</text><text x="{fx+4}" y="{bot+34}" font-size="10" fill="#c0392b">inside the drift region</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_half_cell():
    """Half cell with the parasitic devices marked."""
    X, W = 60, 300
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 330" width="100%" font-family="Arial" font-size="10">', ARROW]
    s.append(rect(X, 270, W, 30, P_PLUS, "p⁺ collector", X + 110, 289, bold=True))
    s.append(rect(X, 250, W, 20, N_PLUS, "n⁺ buffer", X + 120, 264))
    s.append(rect(X, 90, W, 160, N_MINUS, "n⁻ drift", X + 200, 200, bold=True))
    s.append(rect(X, 60, 150, 80, P_BODY))
    s.append('<text x="68" y="132" font-weight="bold">p body</text>')
    s.append(rect(X + 60, 60, 70, 22, N_PLUS, "n⁺ emitter", X + 66, 75))
    s.append(rect(X, 46, 100, 14, METAL))
    s.append(f'<text x="{X+20}" y="40" font-weight="bold">Emitter E</text>')
    s.append(rect(X + 110, 54, 190, 6, OXIDE))
    s.append(rect(X + 115, 38, 185, 16, POLY, "Gate G", X + 190, 50, bold=True))
    s.append(rect(X, 300, W, 8, METAL))
    s.append(f'<text x="{X+120}" y="322" font-weight="bold">Collector C</text>')
    # R_s along p body under n+
    s.append(f'<path d="M{X+130},92 l-8,6 l-8,-6 l-8,6 l-8,-6 l-8,6 l-8,-6 l-8,6 l-8,-6" fill="none" stroke="#e08e0b" stroke-width="2"/>')
    s.append(f'<text x="{X+18}" y="110" fill="#e08e0b" font-weight="bold">R_s (p-body resistance)</text>')
    # labels for parasitic transistors
    s.append(f'<text x="{X+160}" y="160" fill="#c0392b" font-weight="bold">PNP: p⁺ – n⁻ – p body</text>')
    s.append(f'<text x="{X+160}" y="122" fill="#1d6fb8" font-weight="bold">NPN (parasitic): n⁺ – p – n⁻</text>')
    s.append(f'<text x="{X+160}" y="82" fill="#2e8b57" font-weight="bold">MOSFET channel</text>')
    s.append(f'<line x1="{X+157}" y1="80" x2="{X+137}" y2="64" stroke="#2e8b57" marker-end="url(#ar)"/>')
    s.append('</svg>')
    return "\n".join(s)


def fig_equiv():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 330" width="100%" font-family="Arial" font-size="10">', ARROW,
         '<defs><marker id="ab" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 z" fill="#222"/></marker></defs>']
    L = lambda x1, y1, x2, y2, extra="": f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#222" stroke-width="1.6" {extra}/>'
    # Collector terminal
    s.append(L(300, 20, 300, 60)); s.append('<circle cx="300" cy="20" r="3" fill="#222"/><text x="308" y="24" font-weight="bold" font-size="12">C</text>')
    # PNP: bar at x=280, emitter to top (arrow into bar), collector to bottom
    s.append(L(280, 72, 280, 108, 'stroke-width="3"'))
    s.append(L(300, 60, 282, 78, 'marker-end="url(#ab)"'))       # emitter arrow points into the bar (PNP)
    s.append(L(282, 102, 300, 118)); s.append(L(300, 118, 300, 190))
    s.append('<text x="310" y="92" fill="#c0392b" font-weight="bold">Q1 PNP</text>')
    # node B (PNP base)
    s.append(L(280, 90, 150, 90)); s.append('<circle cx="230" cy="90" r="2.5" fill="#222"/>')
    # NPN Q2: bar at x=245, base lead right to node X (300,190); collector up to node B
    s.append(L(245, 172, 245, 208, 'stroke-width="3"'))
    s.append(L(245, 180, 230, 165)); s.append(L(230, 165, 230, 90))
    s.append(L(245, 200, 230, 215, 'marker-end="url(#ab)"'))       # emitter arrow out of bar (NPN)
    s.append(L(230, 215, 230, 270))
    s.append(L(245, 190, 300, 190)); s.append('<circle cx="300" cy="190" r="2.5" fill="#222"/>')
    s.append('<text x="168" y="196" fill="#1d6fb8" font-weight="bold">Q2 NPN</text><text x="160" y="208" fill="#1d6fb8">(parasitic)</text>')
    # R_s from node X to E bus
    pts = [(300, 205)] + [(300 + (7 if k % 2 else -7), 210 + k * 6) for k in range(8)] + [(300, 262)]
    s.append(L(300, 190, 300, 205))
    s.append('<polyline points="' + " ".join(f"{a},{b}" for a, b in pts) + '" fill="none" stroke="#e08e0b" stroke-width="2"/>')
    s.append(L(300, 262, 300, 270)); s.append('<text x="312" y="238" fill="#e08e0b" font-weight="bold">R_s</text>')
    # MOSFET M1 (n-channel): drain stub up to node B, source down to bus
    s.append(L(150, 90, 150, 150)); s.append(L(150, 150, 128, 150))
    s.append(L(128, 145, 128, 215, 'stroke-width="3"'))
    s.append(L(118, 150, 118, 210)); s.append(L(80, 180, 118, 180)); s.append('<text x="64" y="176" font-weight="bold" font-size="12">G</text><circle cx="80" cy="180" r="3" fill="#222"/>')
    s.append(L(128, 210, 150, 210)); s.append(L(150, 210, 150, 270))
    s.append(L(150, 180, 130, 180, 'marker-end="url(#ab)"')); s.append(L(150, 180, 150, 210))
    s.append('<text x="40" y="130" fill="#2e8b57" font-weight="bold">M1 MOSFET</text>')
    # emitter bus
    s.append(L(150, 270, 300, 270)); s.append(L(225, 270, 225, 300)); s.append('<circle cx="225" cy="300" r="3" fill="#222"/><text x="233" y="304" font-weight="bold" font-size="12">E</text>')
    s.append('<text x="20" y="324" fill="#555">Q1 + Q2 = parasitic thyristor (p⁺n⁻pn⁺) → latch-up if V(R_s) &gt; 0.7 V</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_pinchoff():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 260" width="98%" font-family="Arial" font-size="11">', ARROW]
    # cross-section
    X = 20
    s.append(rect(X, 70, 280, 130, P_BODY, "p substrate (body)", X + 90, 180, bold=True))
    s.append(rect(X + 10, 70, 60, 30, N_PLUS, "n⁺ source", X + 12, 90))
    s.append(rect(X + 210, 70, 60, 30, N_PLUS, "n⁺ drain", X + 214, 90))
    s.append(rect(X + 60, 62, 160, 8, OXIDE))
    s.append(rect(X + 65, 44, 150, 18, POLY, "Gate", X + 125, 57, bold=True))
    # tapered channel to pinch-off point
    s.append(f'<polygon points="{X+70},70 {X+70},84 {X+200},71 {X+200},70" fill="#1d6fb8" fill-opacity="0.75"/>')
    s.append(f'<circle cx="{X+200}" cy="71" r="4" fill="none" stroke="#c0392b" stroke-width="2"/>')
    s.append(f'<line x1="{X+205}" y1="115" x2="{X+201}" y2="76" stroke="#c0392b" marker-end="url(#ar)"/><text x="{X+150}" y="128" fill="#c0392b" font-weight="bold">pinch-off point</text>')
    s.append(f'<text x="{X+72}" y="112" fill="#1d6fb8">channel narrows toward drain</text>')
    s.append(f'<text x="{X+60}" y="30">V_GS &gt; V_T</text><text x="{X+200}" y="30">V_DS = V_GS − V_T</text>')
    # characteristics
    O = (370, 220)
    s.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="660" y2="{O[1]}" stroke="#222" marker-end="url(#ar)"/><text x="664" y="{O[1]+4}">V_DS</text>')
    s.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{O[0]}" y2="20" stroke="#222" marker-end="url(#ar)"/><text x="{O[0]+6}" y="26">I_D</text>')
    for k, (xs, Iy) in enumerate(((40, 40), (60, 80), (80, 125), (100, 170))):
        x1, y1 = O[0] + xs, O[1] - Iy
        s.append(f'<path d="M{O[0]},{O[1]} Q{O[0]+xs*0.55},{y1} {x1},{y1} L610,{y1-4}" fill="none" stroke="#1d6fb8" stroke-width="2"/>')
        s.append(f'<text x="614" y="{y1}" fill="#1d6fb8">V_GS{k+1}</text>')
    s.append(f'<path d="M{O[0]},{O[1]} Q{O[0]+70},{O[1]-40} {O[0]+105},{O[1]-185}" fill="none" stroke="#c0392b" stroke-width="2" stroke-dasharray="6,4"/>')
    s.append(f'<text x="{O[0]+118}" y="{O[1]-150}" fill="#c0392b" font-weight="bold">pinch-off locus</text><text x="{O[0]+118}" y="{O[1]-137}" fill="#c0392b">V_DS = V_GS − V_T</text>')
    s.append(f'<text x="{O[0]+8}" y="{O[1]-14}" fill="#555">ohmic</text><text x="{O[0]+150}" y="{O[1]-14}" fill="#555">active (saturation)</text>')
    s.append(f'<text x="{O[0]+100}" y="{O[1]+18}" fill="#555">cut-off: V_GS &lt; V_T, I_D = 0</text>')
    s.append('</svg>')
    return "\n".join(s)


EXTRA_CSS = ".two { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; align-items: start; }"


def html():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Lecture 6 Previous-Year Solutions</title><style>{CSS}{EXTRA_CSS}</style></head><body>
<h1>Lecture 6: Power MOSFET and IGBT</h1>
<div class="small">EEE 339 Power Electronics · Previous-year question solutions · Source: <i>class slides/Lecture 06 Power MOSFET and IGBT.pdf</i> (Rashid ch. 4)</div>

<div class="key"><b>Questions from this lecture in the 2021 to 2024 finals:</b>
<table>
<tr><th>Year</th><th>Question</th><th>Marks</th></tr>
<tr><td>2023 Q3(b)</td><td>Draw the cross-section of an IGBT showing the layers; differentiate PT and NPT IGBTs</td><td>≈ 6</td></tr>
<tr><td>2022 Q6(d)</td><td>Briefly describe the half-cell model of an IGBT with appropriate figure</td><td>7</td></tr>
<tr><td>2022 Q6(b)</td><td>Write the advantages of using IGBT as a switch</td><td>4</td></tr>
<tr><td>2021 Q3(d)</td><td>With diagram, explain the pinch-off condition in a power MOSFET</td><td>4</td></tr>
<tr><td>2022 Q4(a), 2021 Q1(a)</td><td>BJT vs MOSFET; BJT vs MOSFET vs IGBT comparison</td><td>5, 7</td></tr>
</table>
The IGBT was asked in 2022 and 2023, so it is the most likely topic from this lecture again.</div>

<h2>Q1 · 2023 Q3(b): IGBT cross-section; PT vs NPT IGBT</h2>
<div class="q" style="border-top-color:#0d3b66"><span class="qh" style="color:#0d3b66">Q. Draw the cross-section of an IGBT showing the layers. Differentiate between punch-through and non-punch-through IGBTs.</span></div>
<h3>(a) Cross-section</h3>
<div class="fig">{fig_igbt_cell()}<div class="cap">Fig. 1: Cross-section of one IGBT cell (punch-through type). The NPT type has no n⁺ buffer layer.</div></div>
<p><b>Layers from collector to emitter:</b></p>
<ol>
<li><b>p⁺ substrate (collector):</b> the injecting layer. It injects holes into the drift region when the device is on. This is what makes the IGBT different from a MOSFET (a MOSFET has n⁺ here).</li>
<li><b>n⁺ buffer layer</b> (PT only): stops the depletion region from reaching the p⁺ layer.</li>
<li><b>n⁻ drift region:</b> thick and lightly doped; it supports the blocking voltage.</li>
<li><b>p body:</b> the channel is formed in this layer under the gate.</li>
<li><b>n⁺ emitter</b> regions inside the p body, contacted by the emitter metal (the metal also shorts n⁺ to the p body).</li>
<li><b>Gate:</b> polysilicon over a thin <b>SiO₂</b> layer, so the gate is insulated (very high input impedance).</li>
</ol>
<p><b>Operation in one line:</b> V_GE &gt; V_th creates an n-channel in the p body, like a MOSFET. Electrons flow from the n⁺ emitter through the channel into the drift region; the p⁺ layer then injects holes. The drift region is flooded with carriers (<b>conductivity modulation</b>), so the on-state drop is low.</p>

<h3>(b) PT vs NPT IGBT</h3>
<div class="fig">{fig_pt_npt()}<div class="cap">Fig. 2: Layer stacks and electric-field shapes of PT and NPT IGBTs in the blocking state.</div></div>
<table>
<tr><th style="width:24%">Feature</th><th>Punch-through (PT)</th><th>Non-punch-through (NPT)</th></tr>
<tr><td>n⁺ buffer layer</td><td><b>Yes</b>, between p⁺ and n⁻</td><td><b>No</b></td></tr>
<tr><td>Field in blocking state</td><td>Depletion "punches through" the drift region to the buffer (trapezoidal field)</td><td>Depletion ends inside the drift region (triangular field)</td></tr>
<tr><td>Drift region</td><td>Thinner</td><td>Thicker</td></tr>
<tr><td>p⁺ collector</td><td>Thick, heavily doped substrate (epitaxial wafer)</td><td>Thin, lightly doped layer on the back of the wafer</td></tr>
<tr><td>On-state drop V_CE(sat)</td><td>Lower</td><td>Slightly higher</td></tr>
<tr><td>Turn-off / tail current</td><td>Faster (with lifetime control); switching losses rise with temperature</td><td>Longer tail but losses nearly independent of temperature</td></tr>
<tr><td>Reverse blocking</td><td>Very low (asymmetric)</td><td>Can block reverse voltage (symmetric)</td></tr>
<tr><td>Temperature coefficient of V_CE(sat)</td><td>Negative at normal currents: harder to parallel</td><td><b>Positive</b>: easy to parallel</td></tr>
<tr><td>Ruggedness</td><td>Lower short-circuit capability</td><td>More rugged (better short-circuit capability)</td></tr>
</table>

<div class="pb"></div>
<h2>Q2 · 2022 Q6(d): Half-cell model of an IGBT [7]</h2>
<div class="q" style="border-top-color:#0d3b66"><span class="qh" style="color:#0d3b66">Q. Briefly describe the half-cell model of an IGBT with appropriate figure.</span></div>
<div class="two">
<div class="fig">{fig_half_cell()}<div class="cap">Fig. 3a: Half cell with the parasitic devices.</div></div>
<div class="fig">{fig_equiv()}<div class="cap">Fig. 3b: Equivalent circuit of the half cell.</div></div>
</div>
<p>An IGBT chip is made of thousands of identical cells. Because each cell is symmetric, <b>half a cell</b> is enough to model the device. The half cell contains:</p>
<ol>
<li><b>MOSFET M1</b>: n⁺ emitter, p body (channel) and n⁻ drift, controlled by the insulated gate.</li>
<li><b>PNP transistor Q1</b>: p⁺ collector (emitter of Q1), n⁻ drift (base of Q1), p body (collector of Q1). This is the main bipolar path.</li>
<li><b>Parasitic NPN transistor Q2</b>: n⁺ emitter, p body (base), n⁻ drift (collector).</li>
<li><b>R_s</b>: the lateral resistance of the p body under the n⁺ emitter, between the base of Q2 and the emitter contact.</li>
</ol>
<p><b>Normal operation:</b></p>
<ul>
<li>A gate voltage above V_th creates the channel. The MOSFET's electron current flows into the n⁻ drift, which is the <b>base current of the PNP</b>.</li>
<li>The PNP turns on and the p⁺ layer injects holes: conductivity modulation gives a low V_CE(sat).</li>
<li>So the IGBT behaves like a <b>MOSFET driving a PNP transistor</b> (the slide calls it a Darlington of an IGFET and a BJT): I_C = I_MOS + β_PNP·I_MOS = (1 + β_PNP)·I_MOS.</li>
<li>The holes collected by the p body flow to the emitter contact through R_s.</li>
</ul>
<p><b>Latch-up:</b></p>
<ul>
<li>If the hole current is too large, the drop across R_s exceeds about 0.7 V and forward-biases the n⁺–p junction, so the <b>parasitic NPN turns on</b>.</li>
<li>Q1 and Q2 then form a <b>parasitic thyristor</b> (p⁺n⁻pn⁺) that latches on, and the gate <b>loses control</b>; the device can be destroyed.</li>
<li><b>Prevention:</b> keep R_s small (heavy p⁺ doping under the emitter, short n⁺ regions), short the n⁺ and p body with the emitter metal, and limit the current.</li>
</ul>

<h2>Q3 · 2022 Q6(b): Advantages of IGBT as a switch [4]</h2>
<div class="ans">
<ol>
<li><b>Voltage-controlled</b> insulated (MOS) gate: very high input impedance, negligible gate current, simple and cheap drive circuit.</li>
<li><b>Low on-state voltage drop</b> (like a BJT) because of conductivity modulation, so low conduction loss, much lower than a high-voltage MOSFET.</li>
<li><b>High voltage and current ratings</b> (up to several kV and kA) with high current density, so a smaller chip.</li>
<li><b>Faster switching than a BJT</b>; good for PWM inverters and drives (about 20–50 kHz).</li>
<li>Turned on and off by the gate: <b>no commutation circuit</b> needed (unlike an SCR).</li>
<li>Wide safe operating area; less prone to second breakdown than a BJT.</li>
<li>NPT IGBTs have a positive temperature coefficient, so they are <b>easy to parallel</b>.</li>
</ol>
<span class="small">If the question also asks for disadvantages (slide): slower turn-off than a BJT or MOSFET because of the <b>tail current</b>; faster turn-off is possible only with a higher V_CE(sat); latch-up risk.</span>
</div>

<div class="pb"></div>
<h2>Q4 · 2021 Q3(d): Pinch-off condition in a power MOSFET [4]</h2>
<div class="q" style="border-top-color:#0d3b66"><span class="qh" style="color:#0d3b66">Q. With diagram, explain the pinch-off condition in a power MOSFET.</span></div>
<div class="fig">{fig_pinchoff()}<div class="cap">Fig. 4: Left: channel pinch-off at the drain end. Right: output characteristics; the pinch-off locus separates the ohmic and active regions.</div></div>
<ol>
<li><b>Channel formation:</b> for an n-channel enhancement MOSFET, a gate-source voltage V_GS above the threshold V_T induces an n-type inversion channel between source and drain.</li>
<li><b>Ohmic region:</b> for a small V_DS the channel has the same depth along its length and behaves like a resistor (R_DS(on)); I_D rises almost linearly with V_DS.</li>
<li><b>Channel narrowing:</b> as V_DS increases, the gate-to-channel voltage at the drain end, V_GD = V_GS − V_DS, decreases, so the channel becomes thinner near the drain.</li>
<li><b>Pinch-off:</b> when V_GD = V_T, that is
<div class="mono" style="margin:4px 0 4px 20px"><b>V_DS = V_GS − V_T</b></div>
the channel depth at the drain end becomes zero. This is the <b>pinch-off condition</b>.</li>
<li><b>Beyond pinch-off</b> (V_DS &gt; V_GS − V_T): the extra voltage is dropped across the small depletion region near the drain; the current stops increasing and stays at I_D ≈ K(V_GS − V_T)². The MOSFET is in the <b>active (saturation) region</b>, where I_D is controlled by V_GS only.</li>
<li>The locus of pinch-off points, <b>I_D = K·V_DS²</b>, is the boundary between the ohmic and active regions (dashed line in Fig. 4).</li>
</ol>
<p class="small">For switching, a power MOSFET is used in the ohmic region (ON) and cut-off (OFF); the active region is crossed only during transitions.</p>

<h2>Q5 · 2022 Q4(a) and 2021 Q1(a): Comparisons</h2>
<p>These are answered in full in your <b>Lecture 5 notes</b> (pages 8 to 9): BJT vs MOSFET (10-row table) and BJT vs MOSFET vs IGBT (power handling, input impedance, switching speed, on-state resistance, blocking voltage). Short version to remember:</p>
<table>
<tr><th>Parameter</th><th>BJT</th><th>MOSFET</th><th>IGBT</th></tr>
<tr><td>Control / input impedance</td><td>Current / low</td><td>Voltage / very high</td><td>Voltage / very high</td></tr>
<tr><td>Speed</td><td>Slow</td><td>Fastest</td><td>Medium</td></tr>
<tr><td>On-state drop</td><td>Low</td><td>High at high voltage</td><td>Low</td></tr>
<tr><td>Power / voltage</td><td>Medium</td><td>Low-medium</td><td>High</td></tr>
<tr><td>Second breakdown</td><td>Yes</td><td>No</td><td>Less prone</td></tr>
</table>

<h2>Likely new questions from this lecture (short answers)</h2>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Write the features and disadvantages of a power MOSFET.</span>
<div class="ans"><b>Features (slide):</b> low input current; voltage-controlled; high switching speed; no second breakdown; high input impedance; unipolar; no commutation circuit needed; small size; small holding power.<br>
<b>Disadvantages (slide):</b> high on-state voltage, so high conduction loss compared with a BJT; easily damaged by static electricity, so it needs careful handling; asymmetric blocking: blocks high forward voltage but not high reverse voltage.</div></div>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Why is a vertical (VDMOS) structure used for power MOSFETs?</span>
<div class="ans">In a lateral MOSFET both the current and the breakdown voltage depend on the channel dimensions, so it is inefficient. In the vertical, double-diffused MOSFET the source is on top and the drain at the bottom, so current flows vertically. The <b>voltage rating depends on the doping and thickness of the n⁻ layer</b>, while the <b>current rating depends on the channel width</b>. The device can therefore handle high voltage and high current without becoming large. "Double-diffused" refers to the p and n⁺ wells made by two diffusions.</div></div>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Why was the IGBT developed? / Explain the turn-off of a power MOSFET.</span>
<div class="ans"><b>Why IGBT:</b> a BJT needs a large base current (even as a Darlington); a MOSFET needs almost no gate current but has a high on-state drop at high current. The IGBT combines the MOSFET's insulated gate with the BJT's low on-state drop.<br>
<b>MOSFET turn-off (slide):</b> t5: v_GS falls, C_GS discharges and C_GD charges; i_D and v_DS unchanged. t6: v_DS rises to V_CC while v_GS stays constant (Miller plateau); then the diode turns on and i_D starts to fall. t7: v_GS falls to V_T and i_D falls to zero (cut-off). t6 and t7 have both i_D and v_DS present, so they cause the switching loss.</div></div>
</body></html>"""


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html())
    print("ok")
