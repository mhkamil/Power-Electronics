"""Step-by-step solutions: Hart Ex 9-2 (ZVS), 2021 Q6d (ZVS), 2022 Q3d / 2024 Q6c (parallel resonant).

Writes ../build/resonant_solutions.html; print it with:
    node html_to_pdf.js ../build/resonant_solutions.html ../solutions/Resonant_Converter_Solutions.pdf
All numbers are computed here, so the text cannot drift from the arithmetic.
"""
import os
from math import sqrt, pi, asin, cos, sin

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "build", "resonant_solutions.html")


def zvs(Vs, Io, Lr, Cr):
    w0 = 1 / sqrt(Lr * Cr)
    Z0 = sqrt(Lr / Cr)
    t1 = Vs * Cr / Io
    ang = asin(Vs / (Io * Z0))
    t2 = (ang + pi) / w0 + t1
    th = w0 * (t2 - t1)
    t3 = (Lr * Io / Vs) * (1 - cos(th)) + t2
    return dict(w0=w0, Z0=Z0, IoZ0=Io * Z0, t1=t1, ang=ang, t2=t2, th=th, cos=cos(th), k=Lr * Io / Vs, t3=t3)


def zvs_svg(Vs, Io, Lr, Cr, fs, title):
    r = zvs(Vs, Io, Lr, Cr)
    T = 1 / fs
    w0, Z0, t1, t2, t3 = r["w0"], r["Z0"], r["t1"], r["t2"], r["t3"]

    def vC(t):
        if t < t1: return Io * t / Cr
        if t < t2: return max(Vs + Io * Z0 * sin(w0 * (t - t1)), 0.0)
        return 0.0

    def iL(t):
        if t < t1: return Io
        if t < t2: return Io * cos(w0 * (t - t1))
        if t < t3: return (Vs / Lr) * (t - t2) + Io * cos(w0 * (t2 - t1))
        return Io

    W, X0, PW = 640, 60, 540
    X = lambda t: X0 + t / T * PW
    vmax = Vs + Io * Z0
    imin = min(Io * cos(w0 * (t2 - t1)), -0.1 * Io)
    n = 600
    ts = [T * i / n for i in range(n + 1)]
    yv0, hv = 120, 90       # v panel baseline and height for vmax
    yi0, hi = 300, 60       # i panel zero line; Io maps to hi
    vp = " ".join(f"{X(t):.1f},{yv0 - vC(t) / vmax * hv:.1f}" for t in ts)
    ip = " ".join(f"{X(t):.1f},{yi0 - iL(t) / Io * hi:.1f}" for t in ts)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 400" width="100%" font-family="Arial" font-size="11">',
         f'<text x="{X0}" y="14" font-weight="bold" font-size="12">{title}</text>',
         f'<line x1="{X0}" y1="{yv0}" x2="{X0+PW+10}" y2="{yv0}" stroke="#222"/><line x1="{X0}" y1="22" x2="{X0}" y2="{yv0+4}" stroke="#222"/>',
         f'<text x="{X0-50}" y="{yv0-hv+4}">{vmax:.1f} V</text><text x="{X0-50}" y="{yv0 - Vs/vmax*hv + 4}">V_s</text>',
         f'<line x1="{X0}" y1="{yv0 - Vs/vmax*hv}" x2="{X0+PW}" y2="{yv0 - Vs/vmax*hv}" stroke="#ccc" stroke-dasharray="3,3"/>',
         f'<polyline points="{vp}" fill="none" stroke="#c0392b" stroke-width="2"/>',
         f'<text x="{X0+PW-150}" y="34" fill="#c0392b">v_Cr (switch voltage)</text>',
         f'<line x1="{X0}" y1="{yi0}" x2="{X0+PW+10}" y2="{yi0}" stroke="#222"/><line x1="{X0}" y1="{yi0-hi-20}" x2="{X0}" y2="{yi0 - imin/Io*hi + 6}" stroke="#222"/>',
         f'<text x="{X0-40}" y="{yi0-hi+4}">I_o</text><text x="{X0-22}" y="{yi0+4}">0</text>',
         f'<line x1="{X0}" y1="{yi0-hi}" x2="{X0+PW}" y2="{yi0-hi}" stroke="#ccc" stroke-dasharray="3,3"/>',
         f'<polyline points="{ip}" fill="none" stroke="#1d6fb8" stroke-width="2"/>',
         f'<text x="{X0+PW-150}" y="{yi0-hi-24}" fill="#1d6fb8">i_Lr (inductor current)</text>']
    for t, lb in ((t1, "t1"), (t2, "t2"), (t3, "t3"), (T, "T")):
        s.append(f'<line x1="{X(t):.1f}" y1="22" x2="{X(t):.1f}" y2="{yi0 - imin/Io*hi + 6}" stroke="#999" stroke-dasharray="2,3"/>')
        s.append(f'<text x="{X(t)-6:.1f}" y="{yi0 - imin/Io*hi + 22}">{lb}</text>')
    mids = ((0, t1, "Mode 1"), (t1, t2, "Mode 2"), (t2, t3, "Mode 3"), (t3, T, "Mode 4"))
    for a, b, lb in mids:
        if X(b) - X(a) > 34:
            s.append(f'<text x="{(X(a)+X(b))/2-18:.1f}" y="{yi0 - imin/Io*hi + 38}" fill="#555">{lb}</text>')
    s.append('</svg>')
    return "\n".join(s)


def us(x): return f"{x*1e6:.3f} µs"


SUP = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")


def sci(x, d=3):
    """4.613e6 -> 4.613 × 10⁶"""
    from math import floor, log10
    e = floor(log10(abs(x)))
    return f"{x / 10**e:.{d}f} × 10{str(e).translate(SUP)}"


def ex92():
    Vs, Io, Lr, Cr, Vo = 20, 5, 1e-6, 0.047e-6, 10
    r = zvs(Vs, Io, Lr, Cr)
    fs = (1 - Vo / Vs) / (r["t3"] - r["t1"] / 2)
    vpk = Vs + r["IoZ0"]
    return r, fs, vpk


def q6d():
    Vs, Io, Lr, Cr = 5, 3, 1e-6, 0.01e-6
    r = zvs(Vs, Io, Lr, Cr)
    Vo500 = Vs * (1 - 500e3 * (r["t3"] - r["t1"] / 2))
    fs25 = (1 - 2.5 / Vs) / (r["t3"] - r["t1"] / 2)
    return r, Vo500, fs25


def parallel():
    Vs, Lr, Cr, RL, fs = 100, 8e-6, 0.32e-6, 10, 120e3
    w0 = 1 / sqrt(Lr * Cr)
    ws = 2 * pi * fs
    x = ws / w0
    Re = pi ** 2 * RL / 8
    XL, XC = ws * Lr, 1 / (ws * Cr)
    a, b = 1 - x ** 2, ws * Lr / Re
    H = 1 / sqrt(a ** 2 + b ** 2)
    V1 = 4 * Vs / pi
    Vc = H * V1
    Vo = 2 * Vc / pi
    Q = RL / (w0 * Lr)
    return dict(w0=w0, f0=w0 / (2 * pi), ws=ws, x=x, Re=Re, XL=XL, XC=XC, a=a, b=b, H=H, V1=V1, Vc=Vc, Vo=Vo, Q=Q)


def html():
    r1, fs1, vpk1 = ex92()
    r2, vo2, fs2 = q6d()
    p = parallel()
    svg1 = zvs_svg(20, 5, 1e-6, 0.047e-6, fs1, f"Ex 9-2 waveforms at f_s = {fs1/1e3:.0f} kHz (one period)")
    svg2 = zvs_svg(5, 3, 1e-6, 0.01e-6, 500e3, "2021 Q6d waveforms at f_s = 500 kHz (one period)")
    pc = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 170" width="90%" font-family="Arial" font-size="12">
<circle cx="60" cy="90" r="24" fill="none" stroke="#222" stroke-width="1.6"/><path d="M44,90 q8,-14 16,0 t16,0" fill="none" stroke="#222"/>
<text x="6" y="140">v₁ = (4V_s/π) sin ω_s t</text>
<line x1="60" y1="66" x2="60" y2="30" stroke="#222"/><line x1="60" y1="30" x2="170" y2="30" stroke="#222"/>
<path d="M170,30 q8,-12 16,0 q8,-12 16,0 q8,-12 16,0 q8,-12 16,0" fill="none" stroke="#222" stroke-width="1.6"/><text x="176" y="14">L_r (jX_L)</text>
<line x1="234" y1="30" x2="420" y2="30" stroke="#222"/>
<line x1="300" y1="30" x2="300" y2="80" stroke="#222"/><line x1="284" y1="80" x2="316" y2="80" stroke="#222" stroke-width="2"/><line x1="284" y1="90" x2="316" y2="90" stroke="#222" stroke-width="2"/><line x1="300" y1="90" x2="300" y2="150" stroke="#222"/><text x="248" y="88">C_r</text>
<text x="322" y="78">v_C</text>
<line x1="420" y1="30" x2="420" y2="62" stroke="#222"/><rect x="410" y="62" width="20" height="50" fill="none" stroke="#222" stroke-width="1.6"/><line x1="420" y1="112" x2="420" y2="150" stroke="#222"/>
<text x="436" y="84">R_e = π²R_L/8</text><text x="436" y="100">(rectifier + L_o C_o + R_L)</text>
<line x1="60" y1="114" x2="60" y2="150" stroke="#222"/><line x1="60" y1="150" x2="420" y2="150" stroke="#222"/>
</svg>"""

    def zvs_steps(r, Vs, Io, Lr_t, Cr_t):
        return f"""
<ol class="steps">
<li><b>Resonant constants.</b><br>
ω₀ = 1/√(L_rC_r) = 1/√({Lr_t} × {Cr_t}) = <b>{sci(r['w0'])} rad/s</b><br>
Z₀ = √(L_r/C_r) = √({Lr_t} / {Cr_t}) = <b>{r['Z0']:.3f} Ω</b></li>
<li><b>Check the ZVS condition</b> (the capacitor voltage must swing back to zero): I_oZ₀ = {Io} × {r['Z0']:.3f} = {r['IoZ0']:.2f} V &gt; V_s = {Vs} V ✓</li>
<li><b>Mode 1 (0 → t₁): switch opens, C_r charges linearly with I_o until v_C = V_s.</b><br>
t₁ = V_sC_r/I_o = {Vs} × {Cr_t} / {Io} = <b>{us(r['t1'])}</b></li>
<li><b>Mode 2 (t₁ → t₂): L_r–C_r resonance, v_C = V_s + I_oZ₀ sin ω₀(t − t₁). t₂ is when v_C returns to zero.</b><br>
sin ω₀(t₂ − t₁) = −V_s/(I_oZ₀) = −{Vs/r['IoZ0']:.4f}. The angle must be in the 3rd quadrant (after the peak), so<br>
ω₀(t₂ − t₁) = π + sin⁻¹({Vs/r['IoZ0']:.4f}) = π + {r['ang']:.4f} = <b>{r['th']:.4f} rad</b><br>
t₂ = {r['th']:.4f} / ({sci(r['w0'])}) + t₁ = {us(r['th']/r['w0'])} + {us(r['t1'])} = <b>{us(r['t2'])}</b></li>
<li><b>Mode 3 (t₂ → t₃): the diode across the switch conducts, so the switch can be turned on at zero voltage.</b> i_L rises linearly from I_o cos ω₀(t₂−t₁) back to I_o:<br>
t₃ = (L_rI_o/V_s)[1 − cos ω₀(t₂ − t₁)] + t₂ = {us(r['k'])} × [1 − ({r['cos']:.4f})] + {us(r['t2'])} = <b>{us(r['t3'])}</b></li>
<li><b>Mode 4 (t₃ → T): switch on, i_L = I_o, v_C = 0.</b> Output voltage (average of v_x):<br>
<span class="eq">V_o = V_s[1 − f_s(t₃ − t₁/2)]</span>, with t₃ − t₁/2 = {us(r['t3'] - r['t1']/2)}</li>
</ol>"""

    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Resonant Converter Solutions</title>
<style>
@page {{ size: A4; margin: 14mm 14mm 16mm 14mm; }}
body {{ font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 10pt; line-height: 1.45; color: #1b1b1b; }}
h1 {{ color: #0d3b66; font-size: 19pt; margin: 0 0 4px; }}
h2 {{ color: #fff; background: #0d3b66; font-size: 13pt; padding: 5px 10px; border-radius: 4px; margin-top: 18px; }}
h3 {{ color: #0d3b66; font-size: 11pt; margin: 12px 0 4px; }}
.given {{ background: #f1f6fb; border-left: 4px solid #0d3b66; padding: 6px 12px; margin: 6px 0; }}
.ans {{ background: #eaf6ee; border: 2px solid #2e8b57; padding: 6px 12px; margin: 8px 0; border-radius: 4px; }}
.warn {{ background: #fff6e5; border-left: 4px solid #e08e0b; padding: 6px 12px; margin: 8px 0; }}
ol.steps li {{ margin: 6px 0; }}
.eq {{ font-family: 'DejaVu Sans Mono', monospace; background: #f4f4f4; padding: 1px 5px; }}
table {{ border-collapse: collapse; margin: 6px 0; font-size: 9.5pt; }}
td, th {{ border: 1px solid #bbb; padding: 3px 8px; }} th {{ background: #e6edf5; }}
.pb {{ break-before: page; }} .keep, .ans, .given {{ break-inside: avoid; }} h2, h3 {{ break-after: avoid; }} h2.nb {{ break-before: auto; }}
.fig {{ text-align: center; margin: 8px 0; break-inside: avoid; }}
.small {{ font-size: 8.8pt; color: #555; }}
</style></head><body>
<h1>Resonant Converters: Solved Problems</h1>
<div class="small">EEE 339 Power Electronics · Lectures 23–24 (Hart ch. 9) · Hart Ex 9-2, 2021 Final Q6(d), 2022 Final Q3(d) (= 2024 Final Q6(c))</div>

<div class="given"><b>ZVS equations used (Hart 9.3, the same set printed in the 2021 paper):</b><br>
ω₀ = 1/√(L_rC_r), Z₀ = √(L_r/C_r) · t₁ = V_sC_r/I_o · t₂ = (1/ω₀)[sin⁻¹(V_s/(I_oZ₀)) + π] + t₁ · t₃ = (L_rI_o/V_s){{1 − cos[ω₀(t₂ − t₁)]}} + t₂ · <b>V_o = V_s[1 − f_s(t₃ − t₁/2)]</b> · V_C,peak = V_s + I_oZ₀<br>
Condition for ZVS: I_oZ₀ &gt; V_s. Note that V_o <b>falls</b> as f_s rises.</div>

<h2>Problem 1 · Hart Example 9-2 (ZVS resonant switch converter, Lecture 24)</h2>
<div class="given"><b>Given:</b> V_s = 20 V, L_r = 1 µH, C_r = 0.047 µF, I_o = 5 A.<br>
(a) Find the switching frequency for V_o = 10 V. (b) Find the peak voltage across D_s when it is reverse-biased.</div>
{zvs_steps(r1, 20, 5, "1 µH", "0.047 µF")}
<h3>(a) Switching frequency</h3>
<p>10 = 20[1 − f_s × {us(r1['t3'] - r1['t1']/2)}] ⇒ f_s = (1 − 10/20) / {us(r1['t3'] - r1['t1']/2)} = 0.5 / {(r1['t3'] - r1['t1']/2)*1e6:.4f} µs</p>
<p>Check: T = 1/f_s = {us(1/fs1)} &gt; t₃ = {us(r1['t3'])} ✓ (all four modes fit in one period).</p>
<div class="ans"><b>(a) f_s ≈ {fs1/1e3:.0f} kHz</b></div>
<h3>(b) Peak reverse voltage across D_s</h3>
<p>D_s is reverse-biased while C_r is charged, so its peak reverse voltage equals the peak capacitor voltage (at ω₀(t − t₁) = π/2 in Mode 2):</p>
<p>V_Ds,peak = V_C,peak = V_s + I_oZ₀ = 20 + 5 × {r1['Z0']:.2f} = {vpk1:.2f} V</p>
<div class="ans"><b>(b) V_Ds,peak ≈ {vpk1:.1f} V</b></div>
<div class="warn"><b>Note:</b> the slide (Hart's printed solution) writes “20 + (5)(4.61) = 33 V”. That is an arithmetic slip: 20 + 23.05 = <b>43.1 V</b>. Use 43.1 V.</div>
<div class="fig">{svg1}</div>

<h2 class="nb">Problem 2 · 2021 Final Q6(d) (ZVS resonant converter, 6 marks)</h2>
<div class="given"><b>Given:</b> V_s = 5 V, I_o = 3 A, L_r = 1 µH, C_r = 0.01 µF.<br>
(i) Find the output voltage when f_s = 500 kHz. (ii) Find the switching frequency for V_o = 2.5 V.<br>
<span class="small">The ZVS equations were printed on the question paper.</span></div>
{zvs_steps(r2, 5, 3, "1 µH", "0.01 µF")}
<h3>(i) Output voltage at f_s = 500 kHz</h3>
<p>Check: T = 1/500 kHz = 2.000 µs &gt; t₃ = {us(r2['t3'])} ✓</p>
<p>V_o = 5[1 − (500 × 10³)({(r2['t3'] - r2['t1']/2)*1e6:.4f} × 10⁻⁶)] = 5[1 − {500e3*(r2['t3'] - r2['t1']/2):.4f}] = {vo2:.3f} V</p>
<div class="ans"><b>(i) V_o ≈ {vo2:.2f} V</b></div>
<h3>(ii) Switching frequency for V_o = 2.5 V</h3>
<p>t₁, t₂, t₃ depend only on V_s, I_o, L_r and C_r, not on f_s, so they stay the same.</p>
<p>2.5 = 5[1 − f_s × {us(r2['t3'] - r2['t1']/2)}] ⇒ f_s = 0.5 / {(r2['t3'] - r2['t1']/2)*1e6:.4f} µs = {fs2/1e3:.1f} kHz</p>
<p>Check: T = {us(1/fs2)} &gt; t₃ ✓. Lower f_s gives higher V_o, which is consistent with ZVS behaviour.</p>
<div class="ans"><b>(ii) f_s ≈ {fs2/1e3:.0f} kHz</b></div>
<div class="fig">{svg2}</div>

<div class="pb"></div>
<h2>Problem 3 · 2022 Final Q3(d) (also 2024 Final Q6(c), word for word)</h2>
<div class="given"><b>Given:</b> parallel resonant DC-DC converter, V_s = 100 V, L_r = 8 µH, C_r = 0.32 µF, R_L = 10 Ω, f_s = 120 kHz. Output filter L_o, C_o give ripple-free output current and voltage. <b>Find V_o.</b></div>
<div class="warn">This topic is <b>not in your slides</b> (it is Hart §9.6). It was asked in 2022 and 2024 with the same numbers, so it is worth learning this method.</div>
<h3>Idea (first-harmonic method)</h3>
<p>The switches apply a ±V_s square wave to the series L_r and parallel C_r tank. The tank filters it, so only the fundamental matters. The output rectifier, with L_o, C_o and R_L, acts as an equivalent resistor R_e in parallel with C_r. V_o is the average of the rectified capacitor voltage.</p>
<div class="fig">{pc}</div>
<ol class="steps">
<li><b>Fundamental of the input square wave:</b> V₁ = 4V_s/π = 4 × 100/π = <b>{p['V1']:.2f} V</b> (peak)</li>
<li><b>Equivalent load resistor</b> (the rectifier with an L-filter draws a square-wave current): R_e = π²R_L/8 = π² × 10/8 = <b>{p['Re']:.2f} Ω</b></li>
<li><b>Frequencies:</b> ω₀ = 1/√(L_rC_r) = 1/√(8 µH × 0.32 µF) = <b>{p['w0']:.0f} rad/s</b> (f₀ = {p['f0']/1e3:.1f} kHz)<br>
ω_s = 2π × 120 kHz = <b>{p['ws']:.0f} rad/s</b>, so ω_s/ω₀ = <b>{p['x']:.3f}</b></li>
<li><b>Reactances at f_s:</b> X_L = ω_sL_r = <b>{p['XL']:.3f} Ω</b>, X_C = 1/(ω_sC_r) = <b>{p['XC']:.3f} Ω</b></li>
<li><b>Voltage transfer from source to capacitor:</b><br>
H = Z_p/(jX_L + Z_p) with Z_p = R_e ∥ (−jX_C). Dividing through gives<br>
<span class="eq">H = 1 / [1 − ω_s²L_rC_r + jω_sL_r/R_e]</span><br>
1 − (ω_s/ω₀)² = 1 − {p['x']:.3f}² = {p['a']:.4f}; ω_sL_r/R_e = {p['XL']:.3f}/{p['Re']:.2f} = {p['b']:.4f}<br>
|H| = 1/√(({p['a']:.4f})² + ({p['b']:.4f})²) = 1/√({p['a']**2:.4f} + {p['b']**2:.4f}) = <b>{p['H']:.4f}</b></li>
<li><b>Capacitor voltage (peak):</b> V_C1 = |H| × V₁ = {p['H']:.4f} × {p['V1']:.2f} = <b>{p['Vc']:.1f} V</b></li>
<li><b>Output voltage</b> (the full-wave rectifier with the L_o filter averages |v_C|): V_o = (2/π)V_C1 = 0.6366 × {p['Vc']:.1f}</li>
</ol>
<div class="ans"><b>V_o ≈ {p['Vo']:.0f} V</b> (V_o/V_s ≈ {p['Vo']/100:.2f}; the parallel resonant converter can step the voltage <i>up</i>)</div>
<p><b>One-line formula version:</b> V_o = (8/π²)|H|V_s = 0.8106 × {p['H']:.4f} × 100 = {p['Vo']:.1f} V.</p>
<p><b>Graph check (if the paper gives Hart's V_o/V_s curves):</b> read the curve for Q = R_L/(ω₀L_r) = {p['Q']:.1f} at ω_s/ω₀ = {p['x']:.2f}. It gives V_o/V_s ≈ 1.2, so V_o ≈ 120 V, which agrees.</p>

<div class="keep"><h2>What to write in the exam (marks checklist)</h2>
<table>
<tr><th>Step</th><th>Why it earns marks</th></tr>
<tr><td>Circuit sketch with L_r, C_r, switch/diode, output filter</td><td>Shows you know the topology (1 mark)</td></tr>
<tr><td>ω₀ and Z₀ calculated, ZVS/ZCS condition checked</td><td>Method marks even if the arithmetic slips later</td></tr>
<tr><td>t₁, t₂, t₃ with the quadrant explained for t₂</td><td>t₂ is where most students lose marks</td></tr>
<tr><td>T &gt; t₃ check</td><td>Shows the answer is physically valid</td></tr>
<tr><td>Boxed answer with unit</td><td>Final-answer mark</td></tr>
</table></div>
<p class="small">All numbers were computed by script (Exam_Prep/src/resonant_solutions.py). The Problem 1 values agree with the slide solution (t₁ = 0.188 µs, t₂ = 1.10 µs, t₃ = 1.47 µs, f_s = 363 kHz).</p>
</body></html>"""


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html())
    r1, fs1, v1 = ex92(); r2, vo2, fs2 = q6d(); p = parallel()
    print(f"Ex9-2: t1={r1['t1']*1e6:.3f} t2={r1['t2']*1e6:.3f} t3={r1['t3']*1e6:.3f} fs={fs1/1e3:.1f}kHz Vpk={v1:.2f}")
    print(f"Q6d: t1={r2['t1']*1e6:.4f} t2={r2['t2']*1e6:.4f} t3={r2['t3']*1e6:.4f} Vo={vo2:.3f} fs={fs2/1e3:.1f}kHz")
    print(f"Parallel: Re={p['Re']:.3f} x={p['x']:.4f} H={p['H']:.4f} Vc={p['Vc']:.2f} Vo={p['Vo']:.2f} Q={p['Q']:.2f}")
