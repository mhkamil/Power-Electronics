"""Lectures 7-8 (SCR, SCR commutation): previous-year question solutions.

Writes ../build/lec07_08_solutions.html; print with:
    node html_to_pdf.js ../build/lec07_08_solutions.html ../notes/Lecture07_08_SCR_PrevYear_Solutions.pdf
"""
import os
from math import sin, pi, sqrt, exp, log, radians

from lec05_notes import CSS, ARROW
from lec04_notes import diode_v, res_v

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "build", "lec07_08_solutions.html")

# ------------------------------------------------------------------ numbers (gate pulse, slide Example 14-1 = 2024 Q1c)
IH, TD, VRMS, L, R, ALPHA = 0.5, 1.5e-6, 120, 10e-3, 10, radians(30)
VM = sqrt(2) * VRMS
V1 = VM * sin(ALPHA)
DIDT = V1 / L
T1 = IH / DIDT
TG = T1 + TD
T1_EXACT = -(L / R) * log(1 - IH * R / V1)
TG_EXACT = T1_EXACT + TD

AB = '<defs><marker id="ab" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 z" fill="#222"/></marker></defs>'


def L_(x1, y1, x2, y2, extra=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#222" stroke-width="1.6" {extra}/>'


def rect(x, y, w, h, fill, label="", size=12, bold=True):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#222"/>'
    if label:
        s += f'<text x="{x+w/2-5}" y="{y+h/2+5}" font-size="{size}"{" font-weight=\"bold\"" if bold else ""}>{label}</text>'
    return s


def scr_v(x, y):
    """Vertical SCR: anode on top, cathode at bottom, gate lead to the right of the cathode."""
    return diode_v(x, y) + L_(x + 4, y + 8, x + 18, y + 20)


# ------------------------------------------------------------------ figures
def fig_two_transistor():
    P, N = "#f6c4c0", "#cfe3f7"
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="96%" font-family="Arial" font-size="11">', AB]
    # (a) structure split into two transistors
    s.append('<text x="10" y="16" font-weight="bold">(a) PNPN split into Q1 (PNP) and Q2 (NPN)</text>')
    x1, x2, h = 40, 150, 40
    for i, (lab, col) in enumerate((("p", P), ("n", N), ("p", P))):
        s.append(rect(x1, 50 + i * h, 60, h, col, lab))
    for i, (lab, col) in enumerate((("n", N), ("p", P), ("n", N))):
        s.append(rect(x2, 90 + i * h, 60, h, col, lab))
    s.append(f'<line x1="{x1+60}" y1="110" x2="{x2}" y2="110" stroke="#c0392b" stroke-dasharray="3,3"/><line x1="{x1+60}" y1="150" x2="{x2}" y2="150" stroke="#c0392b" stroke-dasharray="3,3"/>')
    s.append(f'<text x="{x1+64}" y="106" font-size="9" fill="#c0392b">shared</text><text x="{x1+64}" y="146" font-size="9" fill="#c0392b">shared</text>')
    s.append(L_(x1 + 30, 50, x1 + 30, 30) + f'<text x="{x1+36}" y="34" font-weight="bold">A</text>')
    s.append(L_(x2 + 30, 210, x2 + 30, 236) + f'<text x="{x2+36}" y="234" font-weight="bold">K</text>')
    s.append(L_(x2 + 60, 150, x2 + 90, 150) + f'<text x="{x2+92}" y="154" font-weight="bold">G</text>')
    s.append(f'<text x="{x1}" y="190" fill="#c0392b" font-weight="bold">Q1 (PNP)</text><text x="{x2}" y="256" fill="#1d6fb8" font-weight="bold">Q2 (NPN)</text>')
    s.append('<text x="10" y="280" font-size="10" fill="#555">J1 = top p-n, J2 = middle n-p, J3 = bottom p-n junction</text>')
    # (b) equivalent circuit
    ox = 330
    s.append(f'<text x="{ox}" y="16" font-weight="bold">(b) Equivalent circuit</text>')
    # Q1 PNP: bar at ox+110, leads on the left (x = ox+92)
    s.append(L_(ox + 110, 82, ox + 110, 118, 'stroke-width="3"'))
    s.append(L_(ox + 92, 66, ox + 108, 86, 'marker-end="url(#ab)"'))      # emitter arrow into bar (PNP)
    s.append(L_(ox + 92, 66, ox + 92, 30) + f'<circle cx="{ox+92}" cy="30" r="3" fill="#222"/><text x="{ox+98}" y="32" font-weight="bold">A</text><text x="{ox+98}" y="54" fill="#555">I_A</text>')
    s.append(L_(ox + 110, 112, ox + 92, 130) + L_(ox + 92, 130, ox + 92, 200))
    s.append(f'<text x="{ox+30}" y="164" fill="#c0392b">I_C1 = I_B2</text>')
    s.append(f'<text x="{ox+118}" y="94" fill="#c0392b" font-weight="bold">Q1 PNP (α₁)</text>')
    # Q1 base to the right
    s.append(L_(ox + 110, 100, ox + 190, 100))
    # Q2 NPN: bar at ox+170, base lead to the left at y=200
    s.append(L_(ox + 170, 182, ox + 170, 218, 'stroke-width="3"'))
    s.append(L_(ox + 92, 200, ox + 170, 200))
    s.append(L_(ox + 170, 190, ox + 190, 172) + L_(ox + 190, 172, ox + 190, 100))
    s.append(f'<text x="{ox+196}" y="140" fill="#1d6fb8">I_C2 = I_B1</text>')
    s.append(L_(ox + 170, 210, ox + 190, 228, 'marker-end="url(#ab)"'))   # emitter arrow out of bar (NPN)
    s.append(L_(ox + 190, 228, ox + 190, 272) + f'<circle cx="{ox+190}" cy="272" r="3" fill="#222"/><text x="{ox+198}" y="276" font-weight="bold">K</text><text x="{ox+198}" y="254" fill="#555">I_K = I_A + I_G</text>')
    s.append(f'<text x="{ox+200}" y="204" fill="#1d6fb8" font-weight="bold">Q2 NPN (α₂)</text>')
    # gate
    s.append(L_(ox + 20, 200, ox + 92, 200) + f'<circle cx="{ox+20}" cy="200" r="3" fill="#222"/><text x="{ox+4}" y="196" font-weight="bold">G</text><text x="{ox+34}" y="216" fill="#555">I_G →</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_iv():
    O = (300, 170)
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="90%" font-family="Arial" font-size="11">', ARROW]
    s.append(f'<line x1="20" y1="{O[1]}" x2="620" y2="{O[1]}" stroke="#222" marker-end="url(#ar)"/><text x="596" y="{O[1]+18}">V_AK</text>')
    s.append(f'<line x1="{O[0]}" y1="290" x2="{O[0]}" y2="15" stroke="#222" marker-end="url(#ar)"/><text x="{O[0]+6}" y="20">I_A</text>')
    # on-state line
    s.append(f'<path d="M{O[0]+4},{O[1]-12} L{O[0]+22},25" fill="none" stroke="#1d6fb8" stroke-width="2.4"/>')
    s.append(f'<text x="{O[0]+26}" y="34" fill="#1d6fb8">on-state (V_T ≈ 1 V)</text>')
    # forward blocking curves for I_G = 0, IG1, IG2, IG3
    for vbo, lab in ((560, "I_G = 0"), (480, "I_G1"), (420, "I_G2"), (370, "I_G3")):
        s.append(f'<path d="M{O[0]},{O[1]} Q{(O[0]+vbo)/2},{O[1]-6} {vbo},{O[1]-16} Q{vbo+6},{O[1]-40} {vbo-30},{O[1]-48} L{O[0]+12},{O[1]-56}" fill="none" stroke="#2e8b57" stroke-width="1.6" stroke-dasharray="{"0" if lab=="I_G = 0" else "5,3"}"/>')
        s.append(f'<text x="{vbo-14}" y="{O[1]+16}" font-size="10">{"V_BO" if lab=="I_G = 0" else ""}</text><text x="{vbo-16}" y="{O[1]-60 if lab!="I_G = 0" else O[1]-24}" font-size="10" fill="#2e8b57">{lab}</text>')
    s.append(f'<text x="{O[0]+60}" y="{O[1]+34}" fill="#2e8b57">I_G3 &gt; I_G2 &gt; I_G1: more I_G, lower breakover</text>')
    s.append(f'<text x="{O[0]+70}" y="{O[1]-80}" fill="#2e8b57" font-size="10">forward blocking (J2 reverse biased)</text>')
    # I_L, I_H
    for yy, lab in ((O[1]-75, "I_L (latching)"), (O[1]-58, "I_H (holding)")):
        s.append(f'<line x1="{O[0]-2}" y1="{yy}" x2="{O[0]+60}" y2="{yy}" stroke="#c0392b" stroke-dasharray="3,3"/><text x="{O[0]-92}" y="{yy+4}" fill="#c0392b" font-size="10">{lab}</text>')
    # reverse characteristic
    s.append(f'<path d="M{O[0]},{O[1]} L90,{O[1]+8} Q70,{O[1]+12} 60,280" fill="none" stroke="#1d6fb8" stroke-width="2"/>')
    s.append(f'<text x="120" y="{O[1]+28}" fill="#1d6fb8" font-size="10">reverse blocking (J1, J3 reverse biased)</text><text x="28" y="{O[1]+70}" fill="#1d6fb8" font-size="10">reverse</text><text x="28" y="{O[1]+82}" fill="#1d6fb8" font-size="10">breakdown</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_transient():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 220" width="78%" font-family="Arial" font-size="11">', ARROW]
    P, N = "#f6c4c0", "#cfe3f7"
    x = 60
    for i, (lab, col) in enumerate((("p", P), ("n", N), ("p", P), ("n", N))):
        s.append(rect(x, 30 + i * 40, 70, 40, col, lab))
    s.append(L_(x + 35, 30, x + 35, 12) + f'<text x="{x+42}" y="18" font-weight="bold">A</text>')
    s.append(L_(x + 35, 190, x + 35, 208) + f'<text x="{x+42}" y="206" font-weight="bold">K</text>')
    for k, yy in enumerate((70, 110, 150)):
        cx = x + 120
        s.append(L_(x + 70, yy, cx, yy) + f'<line x1="{cx}" y1="{yy-10}" x2="{cx}" y2="{yy+10}" stroke="#222" stroke-width="2"/><line x1="{cx+8}" y1="{yy-10}" x2="{cx+8}" y2="{yy+10}" stroke="#222" stroke-width="2"/>')
        s.append(f'<text x="{cx+14}" y="{yy+4}" font-weight="{"bold" if k==1 else "normal"}" fill="{"#c0392b" if k==1 else "#222"}">C_j{k+1} (J{k+1})</text>')
    s.append('<text x="300" y="60" font-weight="bold">In forward blocking, J2 is reverse biased:</text>')
    s.append('<text x="300" y="80">a fast-rising V_AK charges C_j2 with</text>')
    s.append('<text x="300" y="104" font-weight="bold" fill="#c0392b">i_j2 = C_j2·(dV_j2/dt) + V_j2·(dC_j2/dt)</text>')
    s.append('<text x="300" y="128">i_j2 flows like a gate current → leakage</text>')
    s.append('<text x="300" y="146">I_CBO1, I_CBO2 rise → α₁ + α₂ → 1</text>')
    s.append('<text x="300" y="164">→ false turn-on (dv/dt turn-on)</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_dynamic_on():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 230" width="72%" font-family="Arial" font-size="11">', ARROW]
    t0, td, tr = 80, 140, 220
    # i_T
    y = 100
    s.append(f'<line x1="60" y1="{y}" x2="540" y2="{y}" stroke="#222" marker-end="url(#ar)"/><text x="20" y="14" font-weight="bold">i_T</text>')
    s.append(f'<path d="M60,{y} L{td},{y} L{td},{y-8} Q{(td+tr)/2},{y-50} {tr},{y-72} Q{tr+30},{y-80} 520,{y-80}" fill="none" stroke="#1d6fb8" stroke-width="2.4"/>')
    for v, lab in ((0.1, "0.1 I_T"), (0.9, "0.9 I_T")):
        s.append(f'<line x1="60" y1="{y-80*v}" x2="{tr+20}" y2="{y-80*v}" stroke="#ccc" stroke-dasharray="2,2"/><text x="6" y="{y-80*v+4}" font-size="10">{lab}</text>')
    # i_G
    y2 = 190
    s.append(f'<line x1="60" y1="{y2}" x2="540" y2="{y2}" stroke="#222" marker-end="url(#ar)"/><text x="20" y="140" font-weight="bold">i_G</text>')
    s.append(f'<path d="M60,{y2} L{t0},{y2} Q{t0+10},{y2-40} {t0+60},{y2-48} L360,{y2-48} L360,{y2} L520,{y2}" fill="none" stroke="#2e8b57" stroke-width="2.2"/>')
    s.append(f'<text x="{t0+64}" y="{y2-54}" fill="#2e8b57">gate pulse, width t_G</text>')
    s.append(f'<line x1="{t0}" y1="{y2-60}" x2="360" y2="{y2-60}" stroke="#2e8b57" stroke-dasharray="2,2"/>')
    for xx in (t0, td, tr):
        s.append(f'<line x1="{xx}" y1="20" x2="{xx}" y2="{y2+6}" stroke="#bbb" stroke-dasharray="2,4"/>')
    s.append(f'<text x="{(t0+td)/2-6}" y="{y2+20}" font-weight="bold">t_d</text><text x="{(td+tr)/2-6}" y="{y2+20}" font-weight="bold">t_r</text>')
    s.append(f'<line x1="{t0}" y1="{y2+30}" x2="{tr}" y2="{y2+30}" stroke="#0d3b66" marker-end="url(#ar)"/><text x="{tr+8}" y="{y2+34}" fill="#0d3b66" font-weight="bold">t_on = t_d + t_r</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_turnoff():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="80%" font-family="Arial" font-size="11">', ARROW]
    t1, t2, t3, t4, t5 = 160, 190, 240, 330, 380
    y = 80
    s.append(f'<line x1="40" y1="{y}" x2="580" y2="{y}" stroke="#222" marker-end="url(#ar)"/><text x="10" y="30" font-weight="bold">i_A</text>')
    s.append(f'<path d="M40,{y-45} L110,{y-45} L{t1},{y} L{t2},{y+30} Q{t2+20},{y+6} {t3},{y} L560,{y}" fill="none" stroke="#1d6fb8" stroke-width="2.4"/>')
    s.append(f'<text x="{t2+4}" y="{y+42}" fill="#1d6fb8" font-size="10">−I_RR</text>')
    y2 = 190
    s.append(f'<line x1="40" y1="{y2}" x2="580" y2="{y2}" stroke="#222" marker-end="url(#ar)"/><text x="10" y="150" font-weight="bold">v_AK</text>')
    s.append(f'<path d="M40,{y2-4} L{t2},{y2-4} L{t2+6},{y2+50} Q{t2+30},{y2+34} {t3},{y2+36} L{t5},{y2+36} L{t5},{y2-40} L560,{y2-40}" fill="none" stroke="#c0392b" stroke-width="2.2"/>')
    s.append(f'<text x="{t3+10}" y="{y2+52}" fill="#c0392b" font-size="10">reverse voltage applied by the circuit</text><text x="{t5+8}" y="{y2-46}" fill="#c0392b" font-size="10">forward voltage reapplied</text>')
    for xx, lab in ((t1, "t1"), (t3, "t3"), (t4, "t4"), (t5, "")):
        s.append(f'<line x1="{xx}" y1="20" x2="{xx}" y2="{y2+60}" stroke="#bbb" stroke-dasharray="2,4"/><text x="{xx-6}" y="16">{lab}</text>')
    yb = 288
    for a, b, lab, col in ((t1, t3, "t_rr", "#1d6fb8"), (t3, t4, "t_gr", "#2e8b57")):
        s.append(f'<line x1="{a}" y1="{yb-14}" x2="{b}" y2="{yb-14}" stroke="{col}" marker-end="url(#ar)"/><text x="{(a+b)/2-10}" y="{yb-18}" fill="{col}" font-weight="bold">{lab}</text>')
    s.append(f'<line x1="{t1}" y1="{yb}" x2="{t4}" y2="{yb}" stroke="#0d3b66" marker-end="url(#ar)"/><text x="{t4+6}" y="{yb+4}" fill="#0d3b66" font-weight="bold">t_q = t_rr + t_gr</text>')
    s.append(f'<text x="{t5+12}" y="106" fill="#555" font-size="10">t_c (circuit turn-off time):</text><text x="{t5+12}" y="119" fill="#555" font-size="10">from t1 until forward voltage</text><text x="{t5+12}" y="132" fill="#555" font-size="10">is reapplied; must be &gt; t_q</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_natural():
    a_deg = 45
    X0, W, Y = 50, 520, 0
    sx = W / 400.0
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="88%" font-family="Arial" font-size="11">', ARROW]
    panels = (("v_s", 60, "#555"), ("i_T", 160, "#1d6fb8"), ("v_AK", 250, "#c0392b"))
    for lab, y0, col in panels:
        s.append(f'<line x1="{X0}" y1="{y0}" x2="{X0+W+20}" y2="{y0}" stroke="#222" marker-end="url(#ar)"/><text x="10" y="{y0-20}" font-weight="bold" fill="{col}">{lab}</text>')

    def pts(f, y0, amp):
        return " ".join(f"{X0 + d*sx:.1f},{y0 - f(d)*amp:.1f}" for d in range(0, 401, 2))
    s.append(f'<polyline points="{pts(lambda d: sin(radians(d)), 60, 40)}" fill="none" stroke="#555" stroke-width="2"/>')
    on = lambda d: (a_deg <= d % 360 <= 180)
    s.append(f'<polyline points="{pts(lambda d: sin(radians(d)) if on(d) else 0, 160, 50)}" fill="none" stroke="#1d6fb8" stroke-width="2.4"/>')
    s.append(f'<polyline points="{pts(lambda d: 0 if on(d) else sin(radians(d)), 250, 40)}" fill="none" stroke="#c0392b" stroke-width="2.4"/>')
    for d, lab in ((a_deg, "α (gate pulse)"), (180, "π: natural current zero"), (360, "2π")):
        s.append(f'<line x1="{X0+d*sx:.1f}" y1="20" x2="{X0+d*sx:.1f}" y2="290" stroke="#bbb" stroke-dasharray="2,4"/><text x="{X0+d*sx+3:.1f}" y="18" font-size="10">{lab}</text>')
    s.append(f'<text x="{X0+190*sx:.1f}" y="290" fill="#c0392b" font-size="10">supply reverse-biases the SCR → it turns off</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_classc_circuit():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 290" width="100%" font-family="Arial" font-size="11">', ARROW]
    # source
    s.append('<circle cx="50" cy="150" r="18" fill="none" stroke="#222" stroke-width="1.6"/><text x="45" y="146">+</text><text x="46" y="162">−</text><text x="14" y="190" font-weight="bold">V_s</text>')
    s.append(L_(50, 132, 50, 40) + L_(50, 40, 330, 40) + L_(50, 168, 50, 260) + L_(50, 260, 330, 260))
    for x, rl, tl in ((170, "R₁ (load)", "T₁ (main)"), (330, "R₂", "T₂ (aux)")):
        s.append(L_(x, 40, x, 60) + res_v(x, 80) + L_(x, 100, x, 160) + scr_v(x, 180) + L_(x, 200, x, 260))
        s.append(f'<text x="{x+14}" y="84">{rl}</text><text x="{x+24}" y="184">{tl}</text>')
    # capacitor between anodes at y=125
    s.append(L_(170, 125, 245, 125) + L_(255, 125, 330, 125))
    s.append('<line x1="245" y1="110" x2="245" y2="140" stroke="#222" stroke-width="2.4"/><line x1="255" y1="110" x2="255" y2="140" stroke="#222" stroke-width="2.4"/>')
    s.append('<text x="243" y="104" font-weight="bold">C</text><circle cx="170" cy="125" r="2.5" fill="#222"/><circle cx="330" cy="125" r="2.5" fill="#222"/>')
    s.append('<text x="150" y="122" font-size="10">a</text><text x="336" y="122" font-size="10">b</text>')
    s.append('<text x="60" y="284" fill="#555" font-size="10">T₁ fired → C charges (b +); T₂ fired → C puts −V_s across T₁ → T₁ off</text>')
    s.append('</svg>')
    return "\n".join(s)


def fig_classc_waves():
    """T1 fired at 0, T2 at T/2, T1 again at T. R1 = R2, tau = RC, T = 10 tau. Vs = 1."""
    T, tau = 10.0, 1.0
    X0, W = 70, 330
    X = lambda t: X0 + t / (1.25 * T) * W
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 360" width="100%" font-family="Arial" font-size="10">', ARROW]

    def va(t):   # T1 anode (= v_T1)
        t = t % T
        return 0.0 if t < T / 2 else 1 - 2 * exp(-(t - T / 2) / tau)

    def vb(t):   # T2 anode (= v_T2)
        t = t % T
        return 1 - 2 * exp(-t / tau) if t < T / 2 else 0.0

    def iT1(t):
        t = t % T
        return 1 + 2 * exp(-t / tau) if t < T / 2 else 0.0
    ts = [1.25 * T * k / 500 for k in range(501)]
    # gate pulses
    yg = 40
    s.append(f'<line x1="{X0}" y1="{yg}" x2="{X0+W+10}" y2="{yg}" stroke="#222" marker-end="url(#ar)"/><text x="6" y="{yg-4}" font-weight="bold">gates</text>')
    for t, lab in ((0, "T₁"), (T / 2, "T₂"), (T, "T₁")):
        s.append(f'<rect x="{X(t):.1f}" y="{yg-16}" width="5" height="16" fill="#2e8b57"/><text x="{X(t)+7:.1f}" y="{yg-6}" fill="#2e8b57">{lab}</text>')
    for lab, f, y0, amp, col in (("v_T1", va, 125, 32, "#c0392b"), ("v_T2", vb, 215, 32, "#1d6fb8"), ("i_T1", iT1, 330, 14, "#0d3b66")):
        s.append(f'<line x1="{X0}" y1="{y0}" x2="{X0+W+10}" y2="{y0}" stroke="#222" marker-end="url(#ar)"/><text x="6" y="{y0-4}" font-weight="bold" fill="{col}">{lab}</text>')
        pts = " ".join(f"{X(t):.1f},{y0 - f(t)*amp:.1f}" for t in ts)
        s.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2"/>')
    s.append(f'<text x="{X0-34}" y="{125-32+4}">+V_s</text><text x="{X0-34}" y="{125+32+4}">−V_s</text>')
    s.append(f'<text x="{X0-34}" y="{330-14+4}" font-size="9">V_s/R₁</text><text x="{X(0)+40:.1f}" y="{330-30}" font-size="9" fill="#0d3b66">+2V_s/R₂ spike (C charging)</text>')
    # t_c on v_T1
    tc = tau * log(2)
    s.append(f'<line x1="{X(T/2):.1f}" y1="{125+44}" x2="{X(T/2+tc):.1f}" y2="{125+44}" stroke="#c0392b" marker-end="url(#ar)"/><text x="{X(T/2+tc)+4:.1f}" y="{125+48}" fill="#c0392b" font-weight="bold">t_c = 0.693 R₁C</text>')
    s.append(f'<text x="{X(T/2)-80:.1f}" y="{125+20}" fill="#c0392b">T₁ reverse-biased</text>')
    s.append('</svg>')
    return "\n".join(s)


EXTRA_CSS = ".two { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; align-items: start; } .der { font-family: 'DejaVu Sans Mono', monospace; background:#f4f4f4; padding: 6px 10px; border-radius: 4px; line-height: 1.7; }"


def html():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Lectures 7-8 Previous-Year Solutions</title><style>{CSS}{EXTRA_CSS}</style></head><body>
<h1>Lectures 7–8: SCR and SCR Commutation</h1>
<div class="small">EEE 339 Power Electronics · Previous-year question solutions · Source: <i>class slides/Lecture 07 SCR.pdf</i> and <i>Lecture 08 SCR Commutation.pdf</i> (Rashid ch. 9)</div>

<div class="key"><b>Questions from these lectures (finals 2021 to 2024, term tests 2019 to 2020):</b>
<table>
<tr><th>Asked in</th><th>Question</th><th>Marks</th><th>Solved in</th></tr>
<tr><td><b>2021 Q2(b), 2022 Q4(c), 2023 Q2(a), 2024 Q1(a)</b></td><td>Two-transistor model: turn-on condition / anode current / characteristics</td><td>6 to 8</td><td>Q1</td></tr>
<tr><td>2020 TT-1 Q2</td><td>I-V curve; holding and latching current</td><td>5</td><td>Q2</td></tr>
<tr><td>2021 TT-1 Q1</td><td>Five turn-on processes; effect of dv/dt with diagram</td><td>5</td><td>Q3</td></tr>
<tr><td>2022 Q4(d)</td><td>Methods of SCR turn-on and turn-off</td><td>8</td><td>Q4</td></tr>
<tr><td>2024 Q1(b)</td><td>Natural vs forced commutation, one device example each</td><td>6</td><td>Q5</td></tr>
<tr><td>2021 Q3(c)</td><td>Any one forced commutation circuit, with diagram and waveforms</td><td>6</td><td>Q6</td></tr>
<tr><td>2024 Q1(c)</td><td>Minimum gate pulse width (slide Example 14-1, word for word)</td><td>7</td><td>Q7</td></tr>
<tr><td>2024 Q1(d), 2024 Q3(b)</td><td>Why SCRs cannot be paralleled; second breakdown in thyristors</td><td>5, 7</td><td>Lecture 5 notes</td></tr>
</table>
The two-transistor model was asked in <b>all four</b> finals. Learn Q1 first.</div>

<h2>Q1 · Two-transistor model of a thyristor</h2>
<div class="q" style="border-top-color:#0d3b66"><span class="qh" style="color:#0d3b66">2021 Q2(b) [8] · 2023 Q2(a) [7]: Draw the two-transistor model of a thyristor and explain the turn-on condition with equations from this model.<br>
2022 Q4(c) [6]: Using the two-transistor model explain the anode current in a thyristor. · 2024 Q1(a) [7]: With a two-transistor model explain the characteristics of an SCR.</span></div>
<div class="fig">{fig_two_transistor()}<div class="cap">Fig. 1: (a) The PNPN structure viewed as two interconnected transistors. (b) Equivalent circuit.</div></div>
<p><b>Model.</b> The regenerative (latching) action of a thyristor can be shown by splitting its PNPN structure into two complementary transistors: a PNP transistor <b>Q1</b> (p-n-p from the anode side) and an NPN transistor <b>Q2</b> (n-p-n from the cathode side). The middle n and p layers are shared: the <b>collector of each transistor drives the base of the other</b>, which is positive feedback.</p>
<p><b>Derivation.</b> For any transistor, I_C = αI_E + I_CBO, where α is the common-base current gain and I_CBO the collector-base leakage current.</p>
<div class="der">
For Q1 (emitter current = I_A):&nbsp;&nbsp;&nbsp;&nbsp;I_C1 = α₁I_A + I_CBO1 ……(1)<br>
For Q2 (emitter current = I_K):&nbsp;&nbsp;&nbsp;&nbsp;I_C2 = α₂I_K + I_CBO2 ……(2)<br>
Anode current (KCL at Q1):&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I_A = I_C1 + I_C2 ……(3)<br>
Cathode current:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I_K = I_A + I_G ……(4)<br>
Put (1), (2), (4) into (3):&nbsp;&nbsp;I_A = α₁I_A + I_CBO1 + α₂(I_A + I_G) + I_CBO2<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I_A(1 − α₁ − α₂) = α₂I_G + I_CBO1 + I_CBO2<br>
<b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I_A = (α₂I_G + I_CBO1 + I_CBO2) / [1 − (α₁ + α₂)] ……(5)</b>
</div>
<p><b>Turn-on condition (explaining equation 5).</b></p>
<ul>
<li>α₁ and α₂ are not constant: they are small at low emitter current and <b>increase as the current increases</b>.</li>
<li><b>Off state (forward blocking):</b> with I_G = 0 the currents are only leakage, so α₁ + α₂ is much less than 1 and I_A ≈ (I_CBO1 + I_CBO2), a tiny leakage current.</li>
<li><b>Gate current applied:</b> I_G increases I_K, so α₂ rises; I_C2 rises, and since I_C2 is the base current of Q1, I_C1 rises; I_C1 is the base current of Q2, so I_C2 rises further. This is <b>regenerative</b> (positive feedback).</li>
<li>As the currents grow, <b>α₁ + α₂ → 1</b>, the denominator of (5) → 0, so I_A → ∞ in theory. In practice I_A is limited only by the external circuit: <b>the thyristor has turned on (latched)</b>.</li>
<li>Once I_A is above the latching current I_L, the loop sustains itself and the <b>gate signal can be removed</b>. The SCR stays on until I_A falls below the holding current I_H.</li>
<li>Anything that raises α or the leakage currents (high temperature, high V_AK near V_BO, a large dv/dt, light) can also make α₁ + α₂ reach 1, which is why these are the other turn-on methods.</li>
</ul>
<p><b>For 2024 Q1(a) ("explain the characteristics"):</b> add Fig. 2 and link each region to the model: forward blocking (α₁ + α₂ &lt; 1, only leakage); breakover at V_BO (avalanche leakage raises α₁ + α₂ to 1); a larger I_G reaches α₁ + α₂ = 1 at a lower voltage, so V_BO falls; on-state (latched, about 1 V drop); I_L and I_H; reverse blocking (J1 and J3 reverse-biased).</p>

<div class="pb"></div>
<h2>Q2 · 2020 TT-1: I-V curve; holding and latching current [5]</h2>
<div class="fig">{fig_iv()}<div class="cap">Fig. 2: SCR I-V characteristics with the effect of gate current.</div></div>
<ul>
<li><b>Forward blocking:</b> anode positive; J1 and J3 forward-biased, J2 reverse-biased; only a small leakage (off-state) current flows.</li>
<li><b>Forward breakover V_BO:</b> if V_AK is raised far enough, J2 breaks down by avalanche; all three junctions conduct and the SCR switches to the <b>on-state</b> with only about 1 V drop. In practice V_AK is kept below V_BO and the SCR is turned on by gate current; more gate current means a lower breakover voltage.</li>
<li><b>Reverse blocking:</b> cathode positive; J1 and J3 reverse-biased (like two series diodes); only reverse leakage I_R flows, until reverse breakdown.</li>
</ul>
<div class="ans">
<b>Latching current I_L:</b> the minimum anode current required to keep the thyristor in the on-state <b>immediately after it has been turned on and the gate signal has been removed</b>.<br>
<b>Holding current I_H:</b> the minimum anode current required to <b>maintain</b> the thyristor in the on-state. If I_A falls below I_H, a depletion region forms around J2 and the SCR returns to the blocking state. It is of the order of milliamperes.<br>
<b>I_L &gt; I_H.</b>
</div>

<h2>Q3 · 2021 TT-1: Five turn-on processes; effect of dv/dt [5]</h2>
<div class="ans">
<b>Five ways to turn on a thyristor (slide):</b>
<ol>
<li><b>Thermal:</b> high temperature raises electron-hole pairs and leakage, so α₁ + α₂ rises toward 1. May cause thermal runaway; normally avoided.</li>
<li><b>Light:</b> light striking the junctions creates electron-hole pairs (light-activated SCRs, LASCR).</li>
<li><b>High voltage:</b> V_AK &gt; V_BO; leakage starts regenerative turn-on. Can be destructive; avoided.</li>
<li><b>dv/dt:</b> a fast-rising V_AK charges the junction capacitance (below).</li>
<li><b>Gate current:</b> a positive gate-cathode voltage injects gate current; the <b>normal, practical method</b>. More gate current means a lower forward blocking voltage.</li>
</ol>
</div>
<div class="fig">{fig_transient()}<div class="cap">Fig. 3: Thyristor transient model: junction capacitances C_j1, C_j2, C_j3.</div></div>
<p><b>Effect of dv/dt:</b> in forward blocking, J2 is reverse-biased and behaves like a capacitor C_j2. A rapidly rising anode voltage drives a charging current <b>i_j2 = C_j2·dV_j2/dt (+ V_j2·dC_j2/dt)</b> through it. This current acts like a gate current: it increases the leakage currents I_CBO1 and I_CBO2, so α₁ + α₂ can reach 1 and the SCR turns on <b>without a gate signal</b> (false triggering). A large charging current can also damage the device. Protection: an <b>RC snubber</b> across the SCR limits dv/dt; manufacturers specify the maximum allowable dv/dt.</p>

<div class="pb"></div>
<h2>Q4 · 2022 Q4(d): Methods of SCR turn-on and turn-off [8]</h2>
<h3>Turn-on methods</h3>
<p>List and explain the five methods from Q3 (thermal, light, high voltage, dv/dt, gate current), stating that <b>gate triggering</b> is the practical method and the others are mostly unwanted. Add the dynamic turn-on picture:</p>
<div class="fig">{fig_dynamic_on()}<div class="cap">Fig. 4: Dynamic turn-on: after the gate pulse, the anode current needs the delay time t_d and rise time t_r.</div></div>
<p>Gate-pulse rules (slide): remove the gate signal once the SCR is on (to save gate loss); do not apply a gate signal while the SCR is reverse-biased; the gate pulse must last longer than the time the anode current needs to reach the holding (latching) value, and in practice longer than t_on.</p>
<h3>Turn-off methods (commutation)</h3>
<p>The gate cannot turn an SCR off. Turn-off (<b>commutation</b>) needs two conditions: (1) the anode current must be reduced below the holding current I_H, and (2) a reverse voltage must be applied for a sufficient time so that the excess carriers are removed and the SCR regains forward blocking.</p>
<div class="fig">{fig_turnoff()}<div class="cap">Fig. 5: Turn-off characteristics: t_q = t_rr + t_gr; the circuit must give t_c &gt; t_q.</div></div>
<ul>
<li><b>t_rr</b> (t1 to t3): reverse recovery current removes carriers from the outer junctions J1, J3.</li>
<li><b>t_gr</b> (t3 to t4): carriers at J2 disappear by recombination while reverse voltage is held. <b>t_q = t_rr + t_gr</b> (10 to 100 µs).</li>
<li>The commutation circuit must give a <b>circuit turn-off time t_c &gt; t_q</b>, or commutation fails.</li>
</ul>
<table>
<tr><th style="width:24%">Method</th><th>How the current is forced to zero</th></tr>
<tr><td><b>Natural</b> (line, class F)</td><td>The AC supply itself: current passes through a natural zero at the end of the positive half cycle and the supply then reverse-biases the SCR.</td></tr>
<tr><td>Class A (self / resonant / load)</td><td>Load is an underdamped RLC circuit; the current oscillates to zero and the charged capacitor reverse-biases the SCR. Good above 1000 Hz.</td></tr>
<tr><td>Class B (self, resonant LC across SCR)</td><td>An LC circuit across the SCR (not in series with load) rings and turns the SCR off periodically; used in choppers.</td></tr>
<tr><td>Class C (complementary)</td><td>A second SCR in parallel; firing it puts a charged capacitor's reverse voltage across the main SCR. See Q6.</td></tr>
<tr><td>Class D (auxiliary / impulse)</td><td>An auxiliary SCR switches a pre-charged capacitor across the main SCR; diode D and L reverse the capacitor polarity.</td></tr>
<tr><td>Class E (external pulse)</td><td>A pulse transformer injects a reverse voltage pulse (lasting at least t_q) across the SCR.</td></tr>
</table>
<p class="small">Device grades (slide): converter-grade SCRs have t_q ≈ 50 to 100 µs (rectifiers, cycloconverters, AC regulators); inverter-grade SCRs have t_q ≈ 3 to 50 µs (choppers, inverters) and cost more.</p>

<h2>Q5 · 2024 Q1(b): Natural vs forced commutation [6]</h2>
<div class="q" style="border-top-color:#0d3b66"><span class="qh" style="color:#0d3b66">Q. Explain how natural commutation and forced commutation occur, giving one static power semiconductor device example for each.</span></div>
<p><b>Natural commutation</b> (line / source / class F): the commutation voltage comes from the <b>AC supply itself</b>. At the end of every positive half cycle the anode current passes through a <b>natural current zero</b>, and immediately afterwards the supply applies a <b>reverse voltage</b> across the SCR. Both turn-off conditions are met, so the SCR turns off by itself.</p>
<p><b>Example:</b> an <b>SCR (thyristor)</b> in a single-phase phase-controlled rectifier. Natural commutation is also used in AC voltage controllers (SCR or TRIAC), cycloconverters and line-commutated inverters.</p>
<div class="fig">{fig_natural()}<div class="cap">Fig. 6: Natural commutation of an SCR (resistive load): the current ends at π and the supply then reverse-biases the SCR.</div></div>
<p><b>Forced commutation:</b> in <b>DC circuits</b> there is no natural current zero. An external <b>commutation circuit of L and C</b> forces the anode current to zero and applies a reverse voltage across the SCR (Classes A to E).</p>
<p><b>Example:</b> an <b>SCR in a DC chopper</b> (DC-DC converter) or in a forced-commutated inverter.</p>
<table>
<tr><th></th><th>Natural commutation</th><th>Forced commutation</th></tr>
<tr><td>Supply</td><td>AC</td><td>DC</td></tr>
<tr><td>Source of commutation voltage</td><td>The supply itself</td><td>External L-C commutation circuit</td></tr>
<tr><td>Extra components</td><td>None</td><td>Inductors, capacitors, auxiliary SCRs</td></tr>
<tr><td>Cost / losses</td><td>Low</td><td>Higher</td></tr>
<tr><td>Also called</td><td>Line, source, class F</td><td>Classes A, B, C, D, E</td></tr>
<tr><td>Device example</td><td>SCR in a controlled rectifier</td><td>SCR in a DC chopper</td></tr>
</table>

<div class="pb"></div>
<h2>Q6 · 2021 Q3(c): One forced commutation circuit [6]</h2>
<div class="q" style="border-top-color:#0d3b66"><span class="qh" style="color:#0d3b66">Q. Briefly describe any one kind of thyristor forced commutation circuit with necessary diagram and waveforms.</span></div>
<p><b>Chosen: Class C (complementary) commutation.</b> The main SCR T₁ is in series with the load R₁; an auxiliary (complementary) SCR T₂ with R₂ is connected in parallel with it, and a capacitor C joins the two anodes.</p>
<div class="two">
<div class="fig">{fig_classc_circuit()}<div class="cap">Fig. 7a: Class C commutation circuit.</div></div>
<div class="fig">{fig_classc_waves()}<div class="cap">Fig. 7b: Waveforms (R₁ = R₂, steady state).</div></div>
</div>
<ol>
<li><b>T₁ fired:</b> load current V_s/R₁ flows through R₁ and T₁. At the same time C charges through R₂ and T₁ until plate b is at +V_s (a at 0). i_T1 has an extra decaying capacitor-charging spike.</li>
<li><b>T₂ fired (to turn T₁ off):</b> point b drops to 0. Because a capacitor's voltage cannot change instantly, point a jumps to <b>−V_s</b>: the charged capacitor puts a <b>reverse voltage across T₁</b>, its current falls to zero and it turns off.</li>
<li>C now charges through R₁ (and T₂) in the opposite direction: v_T1 = V_s(1 − 2e^(−t/R₁C)). T₁ stays reverse-biased until v_T1 crosses zero, which gives the <b>circuit turn-off time</b><br>
<div class="mono" style="margin-left:20px"><b>t_c = R₁C·ln 2 = 0.693 R₁C</b> (must be &gt; t_q of T₁)</div></li>
<li><b>T₁ fired again:</b> a drops to 0, b jumps to −V_s, so T₂ is reverse-biased and turns off. The cycle repeats; each SCR turns the other off.</li>
</ol>
<p><b>Features (slide):</b> also called complementary commutation; the SCR turns off by the reverse voltage of a charged capacitor; very reliable; useful even below 1000 Hz; used in single-phase inverters with centre-tapped transformers.</p>

<h2>Q7 · 2024 Q1(c): Minimum gate pulse width [7]</h2>
<div class="q" style="border-top-color:#0d3b66"><span class="qh" style="color:#0d3b66">Q. The holding current of the thyristors in a single-phase full converter is I_H = 500 mA and the delay time is t_d = 1.5 µs. The converter is supplied from a 120 V, 60 Hz supply and has a load of L = 10 mH and R = 10 Ω. The converter is operated with a delay angle α = 30°. Determine the minimum value of gate pulse width t_G.</span><br><span class="small">This is <b>Example 14-1 on your Lecture 8 slides</b>, word for word.</span></div>
<div class="ans">
<b>Step 1: supply voltage at the firing instant.</b> V_m = √2 × 120 = {VM:.1f} V; at ωt = α = 30°:<br>
&nbsp;&nbsp;V₁ = V_m sin α = {VM:.1f} × sin 30° = <b>{V1:.2f} V</b><br>
<b>Step 2: initial rate of rise of anode current.</b> Just after triggering the inductor limits the current (R·i is still small):<br>
&nbsp;&nbsp;di/dt = V₁/L = {V1:.2f} / (10 × 10⁻³) = <b>{DIDT:.0f} A/s</b><br>
<b>Step 3: time for the current to reach the holding value.</b> Taking di/dt as constant for this short time:<br>
&nbsp;&nbsp;t₁ = I_H / (di/dt) = 0.5 / {DIDT:.0f} = <b>{T1*1e6:.2f} µs</b><br>
<b>Step 4: minimum gate pulse width.</b> The gate must stay on during the delay time plus this rise time:<br>
&nbsp;&nbsp;t_G = t₁ + t_d = {T1*1e6:.2f} + 1.5 = <b>{TG*1e6:.2f} µs</b>
<div style="margin-top:4px;font-size:11pt"><b>Answer: t_G(min) ≈ {TG*1e6:.2f} µs</b> (this is the slide's answer)</div>
<span class="small">Check with the exact RL current i(t) = (V₁/R)(1 − e^(−tR/L)): t₁ = −(L/R)ln(1 − I_H R/V₁) = {T1_EXACT*1e6:.2f} µs, so t_G = {TG_EXACT*1e6:.2f} µs. Both are accepted; write the slide method and mention the assumption "di/dt constant". In practice t_G is made longer than t_on.</span>
</div>

<h2>Q8 · Related questions answered in your Lecture 5 notes</h2>
<ul>
<li><b>2024 Q1(d):</b> why SCRs (and BJTs) cannot be paralleled easily: negative temperature coefficient, unequal on-state drops and turn-on times, so one device hogs the current. Needs series R/L and simultaneous strong gate pulses.</li>
<li><b>2024 Q3(b):</b> secondary breakdown occurs in thyristors because they are bipolar devices with negative temperature coefficient and regenerative action: current filaments form hot spots.</li>
</ul>

<h2>Likely new questions (short answers)</h2>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Explain the dynamic turn-on and turn-off characteristics of an SCR.</span>
<div class="ans">Turn-on (Fig. 4): t_on = t_d + t_r (t_d: anode current rises to 0.1 I_T; t_r: 0.1 to 0.9 I_T). Turn-off (Fig. 5): t_q = t_rr + t_gr; the circuit turn-off time t_c must exceed t_q.</div></div>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Distinguish converter-grade and inverter-grade SCRs. / Compare thyristors and transistors.</span>
<div class="ans">Converter grade: slow, t_q ≈ 50 to 100 µs, cheaper; rectifiers, cycloconverters, AC regulators. Inverter grade: fast, t_q ≈ 3 to 50 µs, costlier; choppers, inverters. Thyristors vs transistors (slide): thyristors have lower conduction loss and higher power capability; transistors switch faster with lower switching loss.</div></div>
<div class="q"><span class="tag b">Predicted</span><span class="qh">Q. Describe Class A / Class B / Class D / Class E commutation.</span>
<div class="ans">Use the one-line descriptions in the Q4 table. Class A: underdamped RLC load gives a natural current zero (high frequency). Class B: LC across the SCR, periodic on/off (choppers). Class D: auxiliary SCR switches a charged capacitor; the diode prevents reverse discharge. Class E: pulse transformer applies an external reverse pulse at least t_q long.</div></div>
</body></html>"""


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html())
    print(f"V1={V1:.2f} didt={DIDT:.0f} t1={T1*1e6:.2f}us tG={TG*1e6:.2f}us | exact t1={T1_EXACT*1e6:.2f} tG={TG_EXACT*1e6:.2f}")
