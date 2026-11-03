"""Lecture 4 (Power Diodes): complete study notes with past-question solutions.

Writes ../build/lec04_notes.html; print with:
    node html_to_pdf.js ../build/lec04_notes.html ../notes/Lecture04_Power_Diodes_Notes.pdf
Numbers in the worked answers are computed here.
"""
import os
from math import sqrt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "build", "lec04_notes.html")

# ------------------------------------------------------------------ numbers
def rr(didt_A_per_us, trr_us):
    didt = didt_A_per_us * 1e6
    trr = trr_us * 1e-6
    Qrr = 0.5 * didt * trr ** 2
    Irr = sqrt(2 * Qrr * didt)
    return Qrr, Irr

Q_PAST, I_PAST = rr(20, 5)                    # 2021 Q4c, 2023 Q1c
# variant: given Q_RR and di/dt
V_DIDT, V_Q = 30e6, 1500e-6
V_TRR = sqrt(2 * V_Q / V_DIDT)
V_IRR = sqrt(2 * V_Q * V_DIDT)
# series diodes (Rashid-style example)
VD, IS1, IS2, R = 5000, 30e-3, 35e-3, 100e3
VD1 = VD / 2 + R * (IS2 - IS1) / 2
VD2 = VD - VD1
R2 = 100e3
R1 = (VD / 2) / (IS2 - IS1 + (VD / 2) / R2)


# ------------------------------------------------------------------ figures
def fig_dynamic():
    """Diode turn-on / turn-off: i_D and v_D with t0..t4, t_rr, I_RR, Q_RR."""
    X0, Y_I, Y_V = 70, 120, 300      # i axis zero, v axis zero
    # time breakpoints (px)
    a, b, c, d, e, f, g = 110, 150, 200, 360, 410, 450, 520   # 0 | t0 | t1 | ... t2 start | t2 end | t3 end | t4 end
    IF, IRR = 70, 40
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 420" width="96%" font-family="Arial" font-size="12">',
         '<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#222"/></marker></defs>']
    # axes
    for y, lab in ((Y_I, "i_D"), (Y_V, "v_D")):
        s.append(f'<line x1="{X0}" y1="{y}" x2="610" y2="{y}" stroke="#222" marker-end="url(#ar)"/>')
        s.append(f'<text x="615" y="{y+4}">t</text><text x="{X0-40}" y="{y-60}" font-weight="bold">{lab}</text>')
        s.append(f'<line x1="{X0}" y1="{y+70}" x2="{X0}" y2="{y-85}" stroke="#222" marker-end="url(#ar)"/>')
    # current waveform
    ip = (f"M{X0},{Y_I} L{a},{Y_I} L{b},{Y_I-IF+8} Q{c-25},{Y_I-IF} {c},{Y_I-IF} L{d},{Y_I-IF} "
          f"L{e},{Y_I} L{f},{Y_I+IRR} Q{f+20},{Y_I+6} {g},{Y_I} L600,{Y_I}")
    # Q_RR shaded area (from e to g below axis)
    qrr = f"M{e},{Y_I} L{f},{Y_I+IRR} Q{f+20},{Y_I+6} {g},{Y_I} Z"
    s.append(f'<path d="{qrr}" fill="#c0392b" fill-opacity="0.25"/>')
    s.append(f'<path d="{ip}" fill="none" stroke="#1d6fb8" stroke-width="2.5"/>')
    s.append(f'<text x="{c+40}" y="{Y_I-IF-6}" fill="#1d6fb8">I_F (forward current)</text>')
    s.append(f'<line x1="{f}" y1="{Y_I+IRR}" x2="{f+60}" y2="{Y_I+IRR}" stroke="#999" stroke-dasharray="3,3"/><text x="{f+64}" y="{Y_I+IRR+4}" fill="#c0392b">−I_RR</text>')
    s.append(f'<text x="{e-62}" y="{Y_I+30}" fill="#c0392b" font-size="11">Q_RR area →</text>')
    s.append(f'<text x="{d-30}" y="{Y_I-20}" font-size="11">slope = −di/dt</text>')
    # voltage waveform
    VF, VR, VFP, VRM = 14, 55, 50, 80
    vp = (f"M{X0},{Y_V+VR} L{a},{Y_V+VR} L{a+8},{Y_V-VFP} Q{b},{Y_V-VF-4} {c},{Y_V-VF} L{d},{Y_V-VF} "
          f"L{e},{Y_V-VF+4} L{f},{Y_V-2} L{f+15},{Y_V+VRM} Q{g-20},{Y_V+VR-4} {g},{Y_V+VR} L600,{Y_V+VR}")
    s.append(f'<path d="{vp}" fill="none" stroke="#2e8b57" stroke-width="2.5"/>')
    s.append(f'<text x="{a+12}" y="{Y_V-VFP-4}" fill="#2e8b57" font-size="11">V_FP (forward overshoot)</text>')
    s.append(f'<text x="{c+40}" y="{Y_V-VF-6}" fill="#2e8b57" font-size="11">V_F ≈ 0.7–1.5 V</text>')
    s.append(f'<text x="{f+20}" y="{Y_V+VRM+14}" fill="#2e8b57" font-size="11">V_RM (overshoot)</text>')
    s.append(f'<text x="{X0+4}" y="{Y_V+VR-6}" fill="#2e8b57" font-size="11">−V_R</text>')
    # interval markers
    for xx in (a, b, c, d, e, f, g):
        s.append(f'<line x1="{xx}" y1="40" x2="{xx}" y2="395" stroke="#bbb" stroke-dasharray="2,4"/>')
    for x1, x2, lab in ((a, b, "t0"), (b, c, "t1"), (d, e, "t2"), (e, f, "t3 (t_a)"), (f, g, "t4 (t_b)")):
        s.append(f'<text x="{(x1+x2)/2 - (14 if len(lab)>2 else 6)}" y="408" font-weight="bold">{lab}</text>')
    s.append(f'<line x1="{e}" y1="30" x2="{g}" y2="30" stroke="#c0392b" marker-end="url(#ar)"/><line x1="{g}" y1="30" x2="{e}" y2="30" stroke="#c0392b" marker-end="url(#ar)"/>')
    s.append(f'<text x="{e+18}" y="24" fill="#c0392b" font-weight="bold">t_rr = t3 + t4</text>')
    s.append(f'<text x="{a-30}" y="24" fill="#555" font-size="11">turn-on</text><text x="{d-10}" y="24" fill="#555" font-size="11">turn-off →</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_soft_hard():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 170" width="80%" font-family="Arial" font-size="12">']
    for i, (title, tail) in enumerate((("Soft recovery (t_b large, S > 1)", "Q330,105 400,60"), ("Hard / abrupt recovery (t_b small, S < 1)", "L292,60"))):
        ox = i * 280
        s.append(f'<g transform="translate({ox},0)">')
        s.append('<line x1="20" y1="60" x2="260" y2="60" stroke="#222"/><line x1="30" y1="10" x2="30" y2="150" stroke="#222"/>')
        path = f"M30,25 L100,25 L180,60 L240,130 {tail.replace('330', str(330-280+0)).replace('400', str(400-280)).replace('292', str(292-280+0))}"
        # build cleanly per case
        if i == 0:
            path = "M30,25 L90,25 L150,60 L190,130 Q205,100 250,60"
        else:
            path = "M30,25 L90,25 L150,60 L190,130 L200,60 L215,78 L228,52 L240,60"
        s.append(f'<path d="{path}" fill="none" stroke="#1d6fb8" stroke-width="2.5"/>')
        s.append('<text x="196" y="146" fill="#c0392b" font-size="11">−I_RR</text>')
        s.append('<text x="150" y="80" font-size="11">t_a</text>')
        s.append(f'<text x="{200 if i==0 else 196}" y="{56}" font-size="11">t_b</text>')
        s.append(f'<text x="20" y="166" font-weight="bold" font-size="12">{title}</text>')
        s.append('</g>')
    s.append('</svg>')
    return "\n".join(s)


def diode_v(x, y, up=False):
    """Vertical diode centred at (x, y). Default: anode on top, cathode at bottom."""
    if not up:
        tri = f"{x-10},{y-8} {x+10},{y-8} {x},{y+8}"
        bar = f'<line x1="{x-10}" y1="{y+8}" x2="{x+10}" y2="{y+8}" stroke="#222" stroke-width="2"/>'
    else:
        tri = f"{x-10},{y+8} {x+10},{y+8} {x},{y-8}"
        bar = f'<line x1="{x-10}" y1="{y-8}" x2="{x+10}" y2="{y-8}" stroke="#222" stroke-width="2"/>'
    return (f'<polygon points="{tri}" fill="none" stroke="#222" stroke-width="1.6"/>{bar}'
            f'<line x1="{x}" y1="{y-20}" x2="{x}" y2="{y-8}" stroke="#222"/><line x1="{x}" y1="{y+8}" x2="{x}" y2="{y+20}" stroke="#222"/>')


def res_v(x, y):
    """Vertical resistor centred at (x, y), 40 px tall."""
    pts = [(x, y-20)] + [(x + (8 if k % 2 else -8), y - 16 + k * 5) for k in range(7)] + [(x, y+20)]
    return '<polyline points="' + " ".join(f"{a},{b}" for a, b in pts) + '" fill="none" stroke="#222" stroke-width="1.6"/>'


def ind_v(x, y):
    p = f"M{x},{y-20} " + " ".join(f"q10,5 0,10" for _ in range(4))
    return f'<path d="{p}" fill="none" stroke="#222" stroke-width="1.6"/>'


def fig_series_parallel():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 260" width="88%" font-family="Arial" font-size="12">']
    # series: cathode at top (reverse blocking with + at top)
    s.append('<text x="20" y="18" font-weight="bold" font-size="11">(a) Series: shunt R for voltage sharing</text>')
    x, xr = 110, 190
    s.append(f'<line x1="{x}" y1="40" x2="{xr}" y2="40" stroke="#222"/><line x1="{x}" y1="130" x2="{xr}" y2="130" stroke="#222"/><line x1="{x}" y1="220" x2="{xr}" y2="220" stroke="#222"/>')
    for yc, n in ((85, 1), (175, 2)):
        s.append(f'<line x1="{x}" y1="{yc-45}" x2="{x}" y2="{yc-20}" stroke="#222"/><line x1="{x}" y1="{yc+20}" x2="{x}" y2="{yc+45}" stroke="#222"/>')
        s.append(diode_v(x, yc, up=True))
        s.append(f'<line x1="{xr}" y1="{yc-45}" x2="{xr}" y2="{yc-20}" stroke="#222"/><line x1="{xr}" y1="{yc+20}" x2="{xr}" y2="{yc+45}" stroke="#222"/>')
        s.append(res_v(xr, yc))
        s.append(f'<text x="{x-40}" y="{yc+4}">D{n}</text><text x="{xr+14}" y="{yc+4}">R{n}</text>')
        s.append(f'<text x="{x+14}" y="{yc-24}" font-size="10" fill="#555">I_s{n}</text>')
    s.append('<text x="60" y="44">+</text><text x="60" y="224">−</text><text x="30" y="134">V_D</text>')
    s.append('<text x="20" y="248" font-size="11" fill="#555">I_s1 + V_D1/R1 = I_s2 + V_D2/R2,  V_D1 + V_D2 = V_D</text>')
    # parallel
    s.append('<text x="340" y="18" font-weight="bold" font-size="11">(b) Parallel: series R or L for current sharing</text>')
    s.append('<line x1="380" y1="40" x2="540" y2="40" stroke="#222"/><line x1="380" y1="220" x2="540" y2="220" stroke="#222"/>')
    for xx, n in ((410, 1), (510, 2)):
        s.append(f'<line x1="{xx}" y1="40" x2="{xx}" y2="65" stroke="#222"/>')
        s.append(diode_v(xx, 85))
        s.append(f'<line x1="{xx}" y1="105" x2="{xx}" y2="135" stroke="#222"/>')
        s.append(res_v(xx, 155))
        s.append(f'<line x1="{xx}" y1="175" x2="{xx}" y2="220" stroke="#222"/>')
        s.append(f'<text x="{xx+14}" y="89">D{n}</text><text x="{xx+14}" y="159">R{n} or L{n}</text>')
    s.append('<text x="440" y="34">I_D</text><text x="340" y="248" font-size="11" fill="#555">Equal R (or equal lead L) forces equal current</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_freewheel():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 210" width="78%" font-family="Arial" font-size="12">']
    # source
    s.append('<circle cx="60" cy="110" r="22" fill="none" stroke="#222" stroke-width="1.6"/><text x="52" y="106">+</text><text x="53" y="124">−</text><text x="18" y="150">V_s</text>')
    s.append('<line x1="60" y1="88" x2="60" y2="40" stroke="#222"/><line x1="60" y1="40" x2="150" y2="40" stroke="#222"/>')
    # switch
    s.append('<circle cx="150" cy="40" r="3" fill="#222"/><line x1="150" y1="40" x2="190" y2="24" stroke="#222" stroke-width="2"/><circle cx="195" cy="40" r="3" fill="#222"/><text x="150" y="16">S (transistor)</text>')
    s.append('<line x1="195" y1="40" x2="420" y2="40" stroke="#222"/>')
    # diode from ground up to node at x=270 (cathode at top)
    s.append('<line x1="270" y1="40" x2="270" y2="90" stroke="#222"/>')
    s.append(diode_v(270, 110, up=True))
    s.append('<line x1="270" y1="130" x2="270" y2="180" stroke="#222"/><text x="286" y="114">D_FW</text>')
    # load L + R
    s.append('<line x1="420" y1="40" x2="420" y2="60" stroke="#222"/>')
    s.append(ind_v(420, 80))
    s.append('<line x1="420" y1="100" x2="420" y2="115" stroke="#222"/>')
    s.append(res_v(420, 135))
    s.append('<line x1="420" y1="155" x2="420" y2="180" stroke="#222"/><text x="436" y="84">L</text><text x="436" y="139">R</text><text x="460" y="112" fill="#555">load</text>')
    s.append('<line x1="60" y1="132" x2="60" y2="180" stroke="#222"/><line x1="60" y1="180" x2="420" y2="180" stroke="#222"/>')
    s.append('<path d="M300,60 C360,70 380,150 300,165" fill="none" stroke="#c0392b" stroke-width="1.6" stroke-dasharray="5,3"/><text x="330" y="200" fill="#c0392b" font-size="11">i_L freewheels through D_FW when S turns off</text>')
    s.append('</svg>')
    return "\n".join(s)


# ------------------------------------------------------------------ page
def html():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Lecture 4 Power Diodes Notes</title>
<style>
@page {{ size: A4; margin: 14mm 14mm 16mm 14mm; }}
body {{ font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 10pt; line-height: 1.45; color: #1b1b1b; }}
h1 {{ color: #0d3b66; font-size: 20pt; margin: 0 0 2px; }}
h2 {{ color: #fff; background: #0d3b66; font-size: 12.5pt; padding: 5px 10px; border-radius: 4px; margin: 16px 0 6px; break-after: avoid; }}
h3 {{ color: #0d3b66; font-size: 11pt; margin: 10px 0 4px; break-after: avoid; }}
.box {{ background: #f1f6fb; border-left: 4px solid #0d3b66; padding: 6px 12px; margin: 6px 0; break-inside: avoid; }}
.key {{ background: #fff6e5; border-left: 4px solid #e08e0b; padding: 6px 12px; margin: 6px 0; break-inside: avoid; }}
.ans {{ background: #eaf6ee; border: 2px solid #2e8b57; padding: 6px 12px; margin: 6px 0; border-radius: 4px; break-inside: avoid; }}
.q {{ break-inside: avoid; border: 1px solid #c9d3de; border-top: 4px solid #c0392b; border-radius: 6px; padding: 6px 12px; margin: 10px 0; }}
.qh {{ font-weight: bold; color: #c0392b; }}
.tag {{ display: inline-block; background: #c0392b; color: #fff; font-size: 8.5pt; padding: 1px 6px; border-radius: 3px; margin-right: 4px; }}
.tag.g {{ background: #2e8b57; }} .tag.b {{ background: #1d6fb8; }}
table {{ border-collapse: collapse; width: 100%; font-size: 9.3pt; margin: 6px 0; break-inside: avoid; }}
td, th {{ border: 1px solid #bbb; padding: 3px 6px; vertical-align: top; }} th {{ background: #e6edf5; text-align: left; }}
.fig {{ text-align: center; margin: 6px 0; break-inside: avoid; }}
.cap {{ font-size: 8.8pt; color: #555; }}
.mono {{ font-family: 'DejaVu Sans Mono', monospace; }}
.pb {{ break-before: page; }}
ul, ol {{ margin: 3px 0 3px 20px; padding: 0; }} li {{ margin: 2px 0; }}
.small {{ font-size: 8.8pt; color: #555; }}
</style></head><body>

<h1>Lecture 4: Power Diodes</h1>
<div class="small">EEE 339 Power Electronics · Complete study notes with previous-year solutions · Source: <i>class slides/Lecture 04 Power Diodes.pdf</i> (Rashid ch. 2)</div>

<div class="key"><b>Exam priority (from the 2020 to 2024 papers):</b>
<ol>
<li><b>Reverse recovery</b>: definition, waveform, significance. Asked in TT-1 2020, 2021 Q2a, 2023 Q1b.</li>
<li><b>Reverse recovery numerical</b> (di/dt = 20 A/µs, t_rr = 5 µs). Asked in <b>2021 Q4c and 2023 Q1c with the same numbers</b>.</li>
<li>Diode types (general-purpose / fast-recovery / Schottky / SiC), soft vs hard recovery.</li>
<li>Series and parallel diodes; freewheeling diode (2022 Q1a short note).</li>
</ol>
Expected weight in your 60-mark paper: one 3 to 6 mark sub-part in Part A.</div>

<h2>1. Dynamic (switching) characteristics</h2>
<p>When a diode switches, its current and voltage do not change instantly. The slide divides the transition into intervals:</p>
<div class="fig">{fig_dynamic()}<div class="cap">Fig. 1: Diode turn-on (t0, t1) and turn-off (t2, t3, t4). Shaded area = reverse recovery charge Q_RR.</div></div>
<table>
<tr><th style="width:12%">Interval</th><th>What happens</th></tr>
<tr><td><b>t0</b> (turn-on)</td><td>Source goes from negative to positive. Stored charge in the depletion region is removed; the current starts to rise. The diode voltage shows a <b>peak (forward overshoot V_FP)</b> because carrier injection is not yet complete and the N-region resistance is high.</td></tr>
<tr><td><b>t1</b></td><td>Carrier injection completes and the voltage falls to the forward drop V_F. t0 and t1 are tens to hundreds of ns in power diodes. End of t1 = turn-on complete.</td></tr>
<tr><td><b>t2</b> (turn-off starts)</td><td>Source goes from positive to negative. The <b>minority carriers</b> (electrons in P, holes in N) must be removed before the potential barrier forms, so the diode <b>keeps conducting</b>. The current falls at the rate di/dt; the voltage falls slightly as R_ON falls.</td></tr>
<tr><td><b>t3</b> (= t_a)</td><td>The current goes <b>negative</b> and reaches its negative peak <b>−I_RR</b>. At this point the stored minority carriers have been swept out and the diode starts to become reverse-biased.</td></tr>
<tr><td><b>t4</b> (= t_b)</td><td>The current returns to zero as the depletion region recharges. The diode voltage shows a <b>reverse overshoot</b> because of the circuit's parasitic (stray) inductance.</td></tr>
<tr><td><b>t_rr</b></td><td><b>Reverse recovery time t_rr = t3 + t4</b> (t_a + t_b). The area under the time axis in the current waveform is the <b>reverse recovery charge Q_RR</b>.</td></tr>
</table>

<h2>2. Reverse recovery (most important topic)</h2>
<h3>Definitions</h3>
<ul>
<li><b>Reverse recovery time (t_rr):</b> the time from the instant the forward current crosses zero until the reverse current has decayed to about 25% of its peak I_RR (practically, back to zero); t_rr = t_a + t_b.</li>
<li><b>Peak reverse recovery current (I_RR):</b> the maximum reverse current that flows during recovery, at the end of t_a.</li>
<li><b>Reverse recovery charge (Q_RR):</b> the charge carried by the reverse current during recovery, equal to the area of the reverse-current triangle (shaded in Fig. 1).</li>
<li><b>t_a:</b> time to remove stored charge from the depletion region. <b>t_b:</b> time to remove stored charge from the bulk semiconductor.</li>
<li><b>Softness factor S = t_b / t_a.</b></li>
</ul>

<h3>Formulas (and where they come from)</h3>
<div class="box">
Approximate the reverse current as a triangle with height I_RR and base t_rr:
<div class="mono">&nbsp;&nbsp;Q_RR ≈ ½ · I_RR · t_rr ……(1)</div>
The current falls at a constant rate di/dt during t_a:
<div class="mono">&nbsp;&nbsp;I_RR = t_a · (di/dt) ……(2)</div>
For an abrupt recovery (t_b small), t_a ≈ t_rr, so I_RR ≈ t_rr · (di/dt). Substituting into (1):
<div class="mono">&nbsp;&nbsp;Q_RR = ½ · (di/dt) · t_rr² ……(3)</div>
Rearranging (3) and combining with (2):
<div class="mono">&nbsp;&nbsp;t_rr = √(2 Q_RR / (di/dt)) ……(4)&nbsp;&nbsp;&nbsp;&nbsp;I_RR = √(2 Q_RR · (di/dt)) ……(5)</div>
<b>Remember:</b> t_rr and I_RR depend on the stored charge Q_RR and on di/dt (which the circuit sets). Q_RR grows with the forward current I_F.
</div>

<h3>Significance (importance) of t_rr</h3>
<ol>
<li><b>Sets the maximum switching frequency.</b> Reverse recovery must finish before the diode is forward-biased again. The lower t_rr, the faster the diode can be switched (fast / ultrafast diodes).</li>
<li><b>Switching losses.</b> During t_rr the diode carries reverse current while voltage builds up across it, so energy is lost each cycle. Loss rises with frequency.</li>
<li><b>Stress on the other switch.</b> I_RR adds to the current of the transistor that turns on, increasing its peak current and turn-on loss.</li>
<li><b>Overvoltage and EMI.</b> A fast fall of reverse current through stray inductance gives v = L·di/dt spikes, overvoltage and electromagnetic interference.</li>
<li><b>Choice of diode.</b> Rectifiers at line frequency can use general-purpose diodes; choppers and inverters need fast-recovery or Schottky diodes.</li>
</ol>

<h3>Soft vs hard recovery</h3>
<div class="fig">{fig_soft_hard()}<div class="cap">Fig. 2: Shape of the current after −I_RR.</div></div>
<table>
<tr><th></th><th>Soft recovery</th><th>Hard (abrupt) recovery</th></tr>
<tr><td>Current fall after I_RR</td><td>Slow</td><td>Fast (snappy)</td></tr>
<tr><td>Softness S = t_b/t_a</td><td>Large (S ≈ 1 or more)</td><td>Small (S &lt; 1)</td></tr>
<tr><td>Voltage spike L·di/dt</td><td>Low</td><td>High, causes oscillation and EMI</td></tr>
<tr><td>Preferred?</td><td><b>Yes</b> (the slide: "a slow current fall is more attractive")</td><td>No</td></tr>
</table>

<h2>3. Types of diodes</h2>
<h3>Common types (slide 6)</h3>
<table>
<tr><th style="width:20%">Type</th><th>Key points</th></tr>
<tr><td>Small-signal diode</td><td>Low voltage, low current; low-power rectifiers, limiters, amplifiers, waveshaping. Designer must know V_F, breakdown voltage, I_RR and t_rr.</td></tr>
<tr><td>Power rectifier diode</td><td>High forward current and high reverse breakdown voltage; rectifiers, inverters, power supplies. Thermal resistance matters; usually needs a heat sink.</td></tr>
<tr><td>Zener diode</td><td>Voltage regulation; operates in reverse breakdown; the Zener current clamps the voltage.</td></tr>
<tr><td>Schottky diode</td><td>Thin metal film on the semiconductor gives a rectifying contact. V_F ≈ 0.3 V; low-voltage applications.</td></tr>
</table>

<h3>Power diode categories (by recovery): learn this table</h3>
<table>
<tr><th></th><th>General-purpose (standard)</th><th>Fast-recovery</th><th>Schottky</th></tr>
<tr><td>t_rr</td><td>High, typically <b>25 µs</b></td><td>Low, <b>&lt; 5 µs</b></td><td>Almost none (only junction capacitance)</td></tr>
<tr><td>Voltage rating</td><td>50 V to about <b>5 kV</b></td><td>50 V to about <b>3 kV</b></td><td>Low (about 100 V); V_F ≈ 0.3 V</td></tr>
<tr><td>Current rating</td><td>&lt; 1 A to several thousand A</td><td>&lt; 1 A to hundreds of A</td><td>Low to medium</td></tr>
<tr><td>Carriers</td><td>Minority + majority (PN)</td><td>Minority + majority (PN, lifetime-controlled)</td><td><b>Majority carriers only</b>: no excess minority carriers to recombine</td></tr>
<tr><td>Use</td><td>Low-speed: line-frequency rectifiers</td><td>DC-DC and DC-AC converters</td><td>High-frequency, low-voltage supplies</td></tr>
</table>
<p><b>Why Schottky recovers so fast:</b> conduction is by majority carriers only, so there is no stored minority charge. The small recovered charge comes from the junction capacitance only, so it is <b>largely independent of the reverse di/dt</b>.</p>

<h3>Silicon carbide (SiC) diodes</h3>
<ul>
<li>SiC outperforms Si and GaAs. SiC Schottky diodes have <b>no reverse recovery time</b>, ultrafast switching, and switching that is <b>not affected by temperature</b>.</li>
<li>Benefits: lowest switching losses (low Q_RR), surge-current stable and rugged, lower cooling cost, higher frequency and power density, low device capacitance, less EMI.</li>
<li>Uses: power supplies, solar inverters, transport, welding, air conditioners.</li>
<li>A Schottky diode is made by joining doped n-type semiconductor with a metal such as gold, silver or platinum.</li>
</ul>

<h2>4. Series and parallel connection</h2>
<div class="fig">{fig_series_parallel()}<div class="cap">Fig. 3: (a) Series diodes with voltage-sharing resistors. (b) Parallel diodes with current-sharing resistors (or equal inductances).</div></div>
<h3>Series-connected diodes (for high voltage, e.g. HVDC)</h3>
<ul>
<li><b>Why:</b> one diode cannot block the required voltage.</li>
<li><b>Problem:</b> diodes of the same type have different v-i curves (production tolerance). In reverse blocking they all carry the <b>same leakage current</b>, so their <b>blocking voltages can be very different</b>; one diode may break down.</li>
<li><b>Solution:</b> connect a <b>resistor across each diode</b> to force equal voltage sharing. The leakage currents of the diodes then differ, but each diode-plus-resistor pair carries the same total current. (Capacitors are added across each diode to share voltage during transients.)</li>
<li>Equations: I_s1 + V_D1/R1 = I_s2 + V_D2/R2 and V_D1 + V_D2 = V_D.</li>
</ul>
<h3>Parallel-connected diodes (for high current)</h3>
<ul>
<li><b>Why:</b> one diode cannot carry the required current.</li>
<li><b>Problem:</b> current divides according to the forward voltage drops; the diode with the lowest V_F hogs the current.</li>
<li><b>Solution:</b> equal series <b>inductances</b> (e.g. in the leads) or <b>current-sharing resistors</b> (the resistors waste power, so they may not be practical). Choosing diodes of the same type with equal V_F also helps.</li>
<li>In parallel, every diode sees the <b>same reverse voltage</b>.</li>
</ul>

<h2>5. Applications of diodes</h2>
<ul>
<li><b>Rectifiers</b> (AC to DC) and <b>voltage multipliers</b>.</li>
<li><b>Freewheeling diode:</b> gives the inductor current a path when the transistor turns off.</li>
</ul>
<div class="fig">{fig_freewheel()}<div class="cap">Fig. 4: Freewheeling diode D_FW across an inductive load.</div></div>
<p>Without D_FW, turning the switch off would force the inductor current to zero instantly. That gives a huge v = L·di/dt across the switch, which would destroy it. With D_FW, the inductor voltage reverses and forward-biases the diode, so the current continues smoothly through D_FW and the switch is protected.</p>

<div class="pb"></div>
<h2>6. Previous-year questions with full solutions</h2>

<div class="q"><span class="tag">TT-1 2020</span><span class="qh">Q. Explain the reverse recovery time of a diode with diagram. [4]</span>
<div class="ans">
<b>Answer.</b> Draw Fig. 1 (current part is enough, label I_F, −I_RR, t_a, t_b, t_rr, Q_RR).<br>
When a conducting diode is suddenly reverse-biased, the current does not stop at zero. The stored minority carriers in the junction and bulk must first be removed, so the current falls at the rate di/dt, passes through zero and flows in the reverse direction.
<ul>
<li>During <b>t_a</b> the charge in the depletion region is removed and the reverse current rises to its peak <b>I_RR</b>.</li>
<li>During <b>t_b</b> the charge in the bulk semiconductor is removed and the reverse current decays to zero.</li>
<li><b>t_rr = t_a + t_b</b> is the reverse recovery time; the area of the reverse current is the reverse recovery charge <b>Q_RR ≈ ½ I_RR t_rr</b>.</li>
</ul>
The diode can block reverse voltage only after t_rr has ended.
</div></div>

<div class="q"><span class="tag">2021 Q2(a)</span><span class="qh">Q. Discuss the significance of reverse recovery time of a diode. [5]</span>
<div class="ans">
<b>Answer.</b> Start with a one-line definition plus the current sketch (Fig. 1), then give the points:
<ol>
<li><b>Maximum switching frequency:</b> recovery must be over before the diode is forward-biased again, so t_rr limits how fast the diode can switch. Low t_rr means fast/ultrafast diodes.</li>
<li><b>Switching loss:</b> reverse current flows while reverse voltage builds up, so energy is lost every cycle; the loss is proportional to switching frequency.</li>
<li><b>Extra stress on the complementary switch:</b> the I_RR adds to the transistor current at turn-on (higher peak current, higher loss).</li>
<li><b>Voltage spikes and EMI:</b> the rapid fall of reverse current through stray inductance gives L·di/dt overvoltage and noise. Soft-recovery diodes reduce this.</li>
<li><b>Diode selection:</b> line-frequency rectifiers use general-purpose diodes (t_rr ≈ 25 µs); choppers and inverters need fast-recovery (&lt; 5 µs) or Schottky diodes.</li>
</ol>
</div></div>

<div class="q"><span class="tag">2023 Q1(b)</span><span class="qh">Q. Define reverse recovery current and reverse recovery time for diode switching. What is the importance of these parameters? [6]</span>
<div class="ans">
<b>Answer.</b>
<ul>
<li><b>Reverse recovery time t_rr:</b> the time between the instant the forward current falls to zero and the instant the reverse current decays back to (almost) zero; t_rr = t_a + t_b.</li>
<li><b>Reverse recovery current I_RR:</b> the peak reverse current that flows during recovery, at the end of t_a; I_RR = t_a·(di/dt) ≈ √(2Q_RR·di/dt).</li>
</ul>
Draw Fig. 1 (current waveform) with t_a, t_b, t_rr, I_RR and Q_RR marked.<br>
<b>Importance:</b>
<ol>
<li>t_rr fixes the highest usable switching frequency.</li>
<li>I_RR and t_rr together set the reverse recovery loss (∝ Q_RR · V_R · f).</li>
<li>I_RR flows through the switch that turns on, increasing its peak current and stress.</li>
<li>The fall of I_RR through stray inductance causes overvoltage and EMI, which is why soft recovery is preferred.</li>
<li>They decide which diode type to use (general-purpose, fast-recovery or Schottky).</li>
</ol>
</div></div>

<div class="q"><span class="tag">2021 Q4(c) [4]</span><span class="tag">2023 Q1(c) [6]</span><span class="qh">Q. The manufacturer of a selected diode gives the rate of fall of the diode current di/dt = 20 A/µs, and its reverse recovery time t_rr = 5 µs. What value of peak reverse current (and storage charge) do you expect?</span>
<div class="ans">
<b>Given:</b> di/dt = 20 A/µs = 20 × 10⁶ A/s, t_rr = 5 µs = 5 × 10⁻⁶ s.<br>
<b>Step 1: stored charge.</b> Q_RR = ½ (di/dt) t_rr² = ½ × 20 × 10⁶ × (5 × 10⁻⁶)² = ½ × 20 × 10⁶ × 25 × 10⁻¹² = <b>{Q_PAST*1e6:.0f} µC</b><br>
<b>Step 2: peak reverse current.</b> I_RR = √(2 Q_RR (di/dt)) = √(2 × {Q_PAST*1e6:.0f} × 10⁻⁶ × 20 × 10⁶) = √{2*Q_PAST*20e6:.0f} = <b>{I_PAST:.0f} A</b><br>
<b>Check:</b> I_RR = t_rr × di/dt = 5 µs × 20 A/µs = 100 A ✓<br>
<div style="margin-top:4px;font-size:11pt"><b>Answer: I_RR = {I_PAST:.0f} A, Q_RR = {Q_PAST*1e6:.0f} µC</b></div>
<span class="small">Assumption to write in the exam: abrupt recovery (t_b small), so t_a ≈ t_rr.</span>
</div></div>

<div class="q"><span class="tag">2022 Q1(a)(ii)</span><span class="qh">Q. Write a short note on: Freewheeling diode. [about 4]</span>
<div class="ans">
<b>Answer.</b> A freewheeling (flywheel) diode is connected across an inductive load (anti-parallel to the load), as in Fig. 4.
<ul>
<li><b>Purpose:</b> when the switch (or the rectifier diode/SCR) turns off, the inductor current cannot stop instantly. The freewheeling diode gives it a closed path, so the current continues smoothly.</li>
<li><b>Protects the switch:</b> without it, the inductor would create a very large L·di/dt voltage across the switch and destroy it.</li>
<li><b>In rectifiers</b> (e.g. half-wave with RL load): it stops the output voltage going negative, so V_o increases (V_o = V_m/π), the load current becomes smoother (continuous for large L), and the input power factor improves. The rectifier diode no longer conducts in the negative half cycle.</li>
<li>Used in choppers (DC-DC converters), rectifiers with inductive loads, relay and motor drives.</li>
</ul>
</div></div>

<h2>7. Practice questions (likely next) with short answers</h2>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. A diode has Q_RR = 1500 µC and di/dt = 30 A/µs. Find t_rr and I_RR.</span>
<div class="ans">t_rr = √(2Q_RR/(di/dt)) = √(2 × 1500 × 10⁻⁶ / 30 × 10⁶) = <b>{V_TRR*1e6:.0f} µs</b>; I_RR = √(2Q_RR·di/dt) = √(2 × 1500 × 10⁻⁶ × 30 × 10⁶) = <b>{V_IRR:.0f} A</b> (check: 10 µs × 30 A/µs = 300 A ✓)</div></div>

<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Two diodes are connected in series to block V_D = 5 kV. Leakage currents I_s1 = 30 mA, I_s2 = 35 mA. (a) Find each diode voltage if R1 = R2 = 100 kΩ. (b) Find R1 for equal sharing if R2 = 100 kΩ.</span>
<div class="ans">
(a) I_s1 + V_D1/R = I_s2 + V_D2/R with V_D2 = V_D − V_D1 ⇒ V_D1 = V_D/2 + R(I_s2 − I_s1)/2 = 2500 + 100 kΩ × 5 mA / 2 = <b>{VD1:.0f} V</b>, V_D2 = <b>{VD2:.0f} V</b>.<br>
(b) V_D1 = V_D2 = 2500 V: I_s1 + 2500/R1 = I_s2 + 2500/R2 ⇒ 2500/R1 = 35 mA − 30 mA + 25 mA = 30 mA ⇒ <b>R1 = {R1/1e3:.2f} kΩ</b>.<br>
<span class="small">This textbook example (Rashid) is not on your slides, but the slide explains the method, so an examiner can ask it.</span>
</div></div>

<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Compare general-purpose, fast-recovery and Schottky diodes. / Why does a Schottky diode have almost no reverse recovery?</span>
<div class="ans">Use the table in Section 3. Schottky: majority-carrier device, so no stored minority charge; only junction capacitance gives a small recovered charge, independent of di/dt; low V_F (≈ 0.3 V) but low reverse voltage rating.</div></div>

<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. What are soft and hard recovery? Which is preferred and why?</span>
<div class="ans">Soft recovery: slow fall of reverse current (large t_b, S = t_b/t_a large). Hard recovery: fast, snappy fall. Soft is preferred because the voltage induced in stray inductances (L·di/dt) is lower, so less overvoltage, oscillation and EMI.</div></div>

<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Why are resistors connected across series diodes and resistors/inductors in series with parallel diodes?</span>
<div class="ans">Series: diodes of the same type have different leakage characteristics, so with the same leakage current their reverse voltages differ; shunt resistors force equal voltage sharing. Parallel: current divides according to V_F, so the diode with the lowest V_F carries most current; equal series resistors or lead inductances force equal current sharing.</div></div>

<h2>8. One-look revision sheet</h2>
<table>
<tr><th style="width:38%">Item</th><th>Remember</th></tr>
<tr><td>Turn-on intervals</td><td>t0: current rises, forward overshoot V_FP; t1: falls to V_F</td></tr>
<tr><td>Turn-off intervals</td><td>t2: still conducting, current falls; t3 (t_a): reverse current to −I_RR; t4 (t_b): back to 0, reverse overshoot from stray L</td></tr>
<tr><td>t_rr, softness</td><td>t_rr = t_a + t_b = t3 + t4; S = t_b/t_a</td></tr>
<tr><td>Formulas</td><td class="mono">Q_RR = ½ I_RR t_rr · I_RR = t_a di/dt · t_rr = √(2Q_RR/(di/dt)) · I_RR = √(2Q_RR di/dt)</td></tr>
<tr><td>Classic numerical</td><td>20 A/µs, 5 µs gives <b>I_RR = 100 A, Q_RR = 250 µC</b></td></tr>
<tr><td>Diode types</td><td>General-purpose 25 µs, up to 5 kV · Fast-recovery &lt; 5 µs, up to 3 kV · Schottky: majority carriers, V_F ≈ 0.3 V, low voltage</td></tr>
<tr><td>SiC Schottky</td><td>No t_rr, ultrafast, temperature-independent switching, low loss, less EMI</td></tr>
<tr><td>Series / parallel</td><td>Series: shunt R (voltage sharing) · Parallel: series R or equal L (current sharing)</td></tr>
<tr><td>Freewheeling diode</td><td>Path for inductor current at switch-off; prevents L·di/dt spike; in rectifiers keeps v_o ≥ 0</td></tr>
</table>
<p class="small">Numbers in the solutions are computed by Exam_Prep/src/lec04_notes.py.</p>
</body></html>"""


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html())
    print(f"Q_RR={Q_PAST*1e6:.1f}uC I_RR={I_PAST:.1f}A | variant trr={V_TRR*1e6:.2f}us Irr={V_IRR:.1f}A | series VD1={VD1:.0f} VD2={VD2:.0f} R1={R1/1e3:.2f}k")
