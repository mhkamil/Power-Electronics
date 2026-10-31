# EEE 339 Power Electronics: Semester Final Strategy (Batch 22)

**Exam:** 60 marks. Part A is 30 marks and Part B is 30 marks.
**Format per part:** 4 questions. Q1 and Q2 are compulsory, and you answer one of Q3 or Q4. You write **3 questions per part**, so each question is about **10 marks**, and you write 6 questions in total.
**Time left:** 4 days.

Sources analysed: the 2021, 2022, 2023 and **2024 (Batch 21, same instructor and slides)** finals, the Batch 19/20 term tests, Assessments #5–#7 (your own batch, from the Problem Solving Class files), the syllabus, the CLOs, and all 35 lectures.

---

## 0. The main finding

Almost every numerical in the **Batch 21 (2024)** paper is a **worked example that is printed in your slides**, with the same numbers and the same sub-parts.

| 2024 question | Exact source in your slides |
|---|---|
| 1(c) Gate pulse width (I_H = 500 mA, t_d = 1.5 µs, L = 10 mH, R = 10 Ω, α = 30°) | **NOT in slides.** Rashid thyristor-chapter textbook example; the theory is in L07 |
| 2(a) Single-phase bridge, highly inductive load: HF and PF | **Rashid Example 3.4, Lecture 19** |
| 2(b) Derive V_dc(α) for 3-phase full converter, with waveforms | **Rashid 10.4, Lecture 22** |
| 3(c) 3-phase full converter: 208 V, R = 10 Ω, 50% of max | **Rashid Example 10.4, Lecture 22**, verbatim |
| 4(b) Half-wave RL-source: R = 2 Ω, L = 20 mH, V_dc = 100 V | **Hart Example 3-5, Lecture 17**, verbatim |
| 4(c) Bridge with RL: V_m = 100 V, R = 10 Ω, L = 10 mH | **Hart Example 4-1, Lecture 18**, verbatim |
| 5(b) Buck-boost: 24 V, D = 0.4, R = 5 Ω, L = 20 µH, C = 80 µF | **Hart Example 6-6, Lecture 13**, verbatim |
| 5(d) 1-φ AC voltage controller, α = 90°, 120 V | **Handwritten class-note example, Lecture 31_32**, verbatim |
| 6(a) 3-φ bidirectional AC controller, α = 60° waveforms | **Class notes, Lecture 31_32** (the α = 60° grid drawing) |
| 6(c) Parallel resonant DC-DC (V_s = 100 V, L_r = 8 µH, C_r = 0.32 µF) | **NOT in slides.** Copied word-for-word from the **2022 paper Q3(d)** |
| Theory: two-transistor model, commutation, secondary breakdown, SEPIC vs buck-boost, Ćuk advantage, cycloconverter, solar PV | Slides L05, L07, L08, L14, L15, L33, L35, plus many repeats from 2021–2023 |

About **91% of the 2024 question pool came from the slides** (only the parallel resonant converter and the gate-pulse-width numerical did not). Roughly **20–25%** also repeated earlier papers (cycloconverter, two-transistor model, commutation, SEPIC, solar PV, parallel resonant). This fits the 60/20/20 model you described.

**What this means for you:**
1. Treat every worked example in the slides as a likely exam question. Learn each one fully (circuit, waveform, formula, final number).
2. The 2024 paper has already used some examples. The remaining examples are the most likely new numericals (see §4).
3. Your batch's Assessments #5, #6 and #7 (inverters and the AC controller) show what the instructor considers important in the topics taught last.

---

## 1. Previous four finals

### 1.1 Topic frequency (finals 2021–2024 and term tests)

| Topic | 2021 | 2022 | 2023 | 2024 | Hits | In slides? |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| SCR two-transistor model / turn-on | ✔ | ✔ | ✔ | ✔ | **4/4** | L07 |
| Cycloconverter (principle and uses) | ✔ | ✔ | ✔ | ✔ | **4/4** | L33 |
| Diode reverse recovery (t_rr, I_RR, Q_RR numerical) | ✔ | TT | ✔ | – | 3 | L04 |
| Device comparison (BJT/MOSFET/IGBT/GTO/MCT) | ✔ | ✔ | ✔ | ✔ (parallel op.) | **4/4** | L02–06 |
| SCR turn-on/turn-off, commutation classes | ✔ | ✔ | – | ✔ | 3 | L08 |
| Half-wave RL / RL-source / freewheeling (Hart ch3) | – | ✔ | ✔ | ✔ | 3 | L17 |
| Full-wave bridge (uncontrolled / controlled), PF, HF | ✔ | ✔ | ✔ | ✔ | **4/4** | L18–20 |
| 3-phase rectifier / converter | ✔ | TT | ✔ | ✔✔ | **4/4** | L21–22 |
| Boost converter (derive + waveforms) | ✔ | TT | ✔ | – | 3 | L11–12 |
| Buck / buck-boost numerical | ✔ | ✔ | ✔ | ✔ | **4/4** | L09–13 |
| SEPIC / Ćuk advantages, comparison | ✔ | – | ✔ | ✔✔ | 3 | L14–15 |
| Linear regulator vs SMPS | – | – | ✔ | ✔ | 2 | L09 |
| Resonant converter (ZVS/ZCS/parallel) | ✔ | ✔ | – | ✔ | 3 | L23–24 (parallel: **not** in slides) |
| Square-wave inverter (full-bridge RL, THD) | ✔ | ✔ | ✔ | – | 3 | L25–26 |
| Amplitude/harmonic control, PWM inverter | ✔ | ✔ | ✔ | – | 3 | **Partly**: quasi-square in Assessment #5; PWM **not** in slides |
| Multilevel inverter | ✔ | – | ✔ | ✔ | 3 | L29 |
| AC voltage controller | – | ✔ | – | ✔✔ | 2 | L31–32 |
| DC motor / induction motor drive | ✔ | ✔ | TT | – | 3 | **Not in slides** |
| Solar PV standalone system | ✔ | – | ✔ | ✔ | 3 | L35 |
| Power computation, non-sinusoidal (THD, DF, crest factor) | ✔ | ✔ | ✔ | – | 3 + every TT-1 | Only partly (L18, inverter notes) |

### 1.2 Batch 21 (2024) structure and how it maps to your 60-mark format

The 2024 paper had 3 questions per part (answer 2), each worth 25 marks. Mark distribution of the question pool (150 marks):

| Area | Marks in pool | Share |
|---|:-:|:-:|
| **Rectifiers (1-φ and 3-φ, controlled and uncontrolled)** | 57 | **38%** |
| Power devices (SCR, BJT, MOSFET, commutation) | 32 | 21% |
| DC-DC converters | 24 | 16% |
| AC voltage controller + cycloconverter | 21 | 14% |
| Resonant converter | 6 | 4% |
| Multilevel inverter | 5 | 3% |
| Solar PV | 5 | 3% |

**Part A (2024)** covered devices (SCR, BJT), rectifiers (1-φ and 3-φ converter) and DC-DC vs SMPS. This is the first half of the course.
**Part B (2024)** covered Hart rectifier examples, DC-DC (SEPIC, Ćuk, buck-boost), AC controller, cycloconverter, multilevel inverter, resonant converter and solar PV. This is the second half plus leftovers.

Inverters received only 5 marks in 2024. In your batch, inverters got two assessments (#5 quasi-square full-bridge, #6 three-phase 120° mode). **Expect inverters to be weighted much more heavily for Batch 22.** This is the biggest change from the 2024 paper.

**Likely Batch 22 split** (an estimate, so prepare everything):
- **Part A (30):** Devices (L02–08), DC-DC converters (L09–15), rectifiers (L16–22)
- **Part B (30):** Rectifier leftovers, resonant (L23–24), inverters (L25–29), AC-AC and cycloconverter (L31–33), solar PV (L35)

With 4 questions per part, each about 10 marks (for example 3 + 3 + 4 or 4 + 6), expect **one theory/derivation plus one numerical per question.**

---

## 2. Priority list

### TIER 1: Must master (highest probability, about 70% of marks)

| # | Topic | What exactly to be able to do | Slide |
|---|---|---|---|
| 1 | **SCR** | I-V curve; latching vs holding current; **two-transistor model with I_A = (α₂I_G + I_CBO1 + I_CBO2)/(1 − (α₁+α₂))**; turn-on methods (gate, dv/dt, thermal, light, forward voltage); **gate pulse width numerical** | L07 |
| 2 | **SCR commutation** | Natural vs forced commutation (one device example each: SCR in AC rectifier vs SCR chopper); Class A–E with a one-line description and a sketch of one (Class C is the easiest) | L08 |
| 3 | **Device comparison** | Table: BJT / MOSFET / IGBT / SCR / GTO by power, speed, drive, R_on, blocking; **why MOSFETs parallel easily** (positive temperature coefficient of R_DS(on)), while BJTs and SCRs don't (negative temperature coefficient leads to current hogging and thermal runaway); **secondary breakdown** in BJT (hot spots), absent in MOSFET | L02–L06 |
| 4 | **Diode reverse recovery** | Sketch t_rr, I_RR; **Q_RR = ½·I_RR·t_rr, I_RR = t_rr·(di/dt)** (assuming t_s ≈ t_rr). Example: di/dt = 20 A/µs, t_rr = 5 µs gives I_RR = 100 A, Q_RR = 250 µC | L04 |
| 5 | **Single-phase full-wave rectifier, highly inductive load (Ex 3.4)** | Square-wave i_s gives **I_s1 = 0.90I_a, HF = 48.34%, DF = 1, PF = 0.90** | L19 |
| 6 | **Single-phase full converter (Ex 10.1)** | V_dc = 2V_m cos α / π; HF = 48.34%, DF = cos α, PF = 0.9 cos α. At α = 60°: V_dc = 54.02 V, PF = 0.45 | L20 |
| 7 | **Controlled bridge, R load (Hart 4-6)** | V_o = (V_m/π)(1 + cos α). With 120 V, 20 Ω, α = 40°: V_o = 95.4 V, I_o = 4.77 A, P ≈ 673 W. Asked in **2022 and 2023** | L20 |
| 8 | **Three-phase full converter (Ex 10.4) and its derivation** | **V_dc = (3√3 V_m/π) cos α = 1.35 V_LL cos α**; waveforms of v_an, v_bn, v_cn, gate pulses T1–T6 (60° apart), output and line current. Ex 10.4: α = 60°, V_dc = 140.45 V, I_dc = 14.05 A, I_rms = 15.93 A, I_A = 4.68 A, I_R = 9.2 A, η = 77.8%, TUF = 0.421, PF = 0.542 | L22 |
| 9 | **Hart ch3 half-wave family** | RL (Ex 3-2: P = 22.4 W, pf = 0.67); **RL-source (Ex 3-5: P_R ≈ 31.7 W, P_dc = 225 W, pf ≈ 0.54)**; freewheeling diode (Ex 3-7, 3-8); controlled half-wave (Ex 3-10) | L17 |
| 10 | **Bridge with RL (Hart 4-1)** | Fourier method: V_o = 2V_m/π, V_n = (2V_m/π)[1/(n−1) − 1/(n+1)]; I_0 = 6.37 A, P = 464 W, pf = 0.964 | L18 |
| 11 | **Buck / boost / buck-boost** | Circuit, **ON and OFF equivalent circuits**, i_L, i_D, i_C, v_o waveforms; derive V_o/V_s from volt-second balance; L_min, ΔV_o/V_o. Hart 6-1 (buck), 6-4/6-5 (boost design), **6-6 (buck-boost)** | L09–L13 |
| 12 | **SEPIC and Ćuk** | Circuits; V_o = V_s·D/(1−D) for both; SEPIC output **not inverted**, Ćuk output inverted; Ćuk has **continuous input and output current** (low ripple); SEPIC/Ćuk advantage over buck-boost (non-pulsating input current, less EMI; SEPIC is non-inverting with a common ground) | L14–L15 |
| 13 | **Square-wave inverters (half and full bridge)** | Half bridge: V_o,rms = V_dc/2, V_o1 = 0.45V_dc. Full bridge: V_o,rms = V_dc, **V_o = Σ (4V_dc/nπ) sin nωt**, V_o1 = 0.90V_dc, **THD = 48.34%**, LOH = 3rd, HF₃ = 33.3%. RL load current via Z_n = √(R² + (nωL)²). Class example: V_dc = 48 V, R = 2.4 Ω gives P = 240 W, I_peak = 10 A, I_avg(sw) = 5 A, V_BR = 48 V, THD = 48.4% | L25–L26 |
| 14 | **Quasi-square / amplitude and harmonic control** (Assessment #5) | Q1, Q2 on from δ to π−δ: **V_o,rms = V_dc√((π−2δ)/π)**, **V_n = (4V_dc/nπ) cos(nδ)** (n odd). For δ = π/6: V_rms = 0.8165V_dc, V_o1,rms = 0.7797V_dc, THD = 31.1%. **δ = 30° removes the 3rd harmonic**, which is how amplitude and harmonics are controlled | L26 + Assessment |
| 15 | **Three-phase inverter, 180° and 120°** (Assessment #6) | Gate sequence table (S1 to S6 every 60°). 180° mode: **V_L,rms = √(2/3)V_dc = 0.8165V_dc**, V_L1 = 0.7797V_dc, V_p = 0.4714V_dc, v_ab = Σ (4V_dc/nπ) cos(nπ/6) sin n(ωt+π/6). 120° mode: v_an = ±V_dc/2 for 120°, 0 for 60°, so **V_p = V_dc/√6 = 0.408V_dc, V_L,rms = V_dc/√2 = 0.707V_dc** | L28 |
| 16 | **Multilevel (cascaded H-bridge)** | Levels = 2s + 1 (s = number of H-bridges; 5-level needs 2 bridges, 7-level needs 3); draw the switch state table for each level; staircase waveform; THD falls as levels rise (2-level 48.3%, 7-level about 31.5%; V_rms = √2·V_dc for the notes example) | L29 |
| 17 | **AC voltage controller, 1-φ** (Assessment #7, 2024 Q5d) | **V_o = V_s√(1 − α/π + sin 2α / 2π)**, PF = V_o/V_s. 120 V, R = 10 Ω, α = 90°: **V_o = 84.85 V, P = 720 W, PF = 0.707, I_T,avg = 2.7 A, I_T,rms = 6 A**. Assessment #7 uses asymmetric α₁ = 80°, α₂ = 100°. Use V_o² = (V_m²/4π)[(π−α₁+½sin2α₁) + (π−α₂+½sin2α₂)], which gives V_o = 84.85 V, PF = 0.707 | L31–32 |
| 18 | **AC voltage controller, 3-φ** | Bidirectional (6 SCRs) circuit; draw v_an for α = 60° from the 30°-shifted grid: 0, v_an, v_ab/2 … segments (copy the class-note drawing) | L31–32 |
| 19 | **Cycloconverter** | Definition (AC to AC at lower frequency, no DC link); uses (low-speed high-power motors: rolling mills, cement kilns, ship propulsion); 1-φ circuit with P and N converters; waveform for f_o = f_s/3 (T_o = 3T_s) and f_o = f_s/5 for 3-φ | L33 |

### TIER 2: Study after Tier 1

| Topic | Slide |
|---|---|
| Ideal switch characteristics (10 points), device classification (9 categories) | L02–L03 |
| Power BJT: modes (cutoff, active, quasi-saturation, hard saturation), switching times t_d, t_r, t_s, t_f, SOA | L05 |
| Power MOSFET: VDMOS structure, features and drawbacks, turn-on/off intervals, pinch-off | L06 |
| IGBT: structure, advantages, disadvantages, half-cell/equivalent circuit, punch-through (PT) vs non-punch-through (NPT) | L06 |
| Diodes: types (general, fast recovery, Schottky, SiC), series diodes (needs voltage sharing resistors), parallel diodes (needs current sharing) | L04 |
| Half-wave R load performance: η = 40.5%, FF = 1.57, RF = 121%, TUF = 0.286, PIV = V_m | L16 |
| Capacitor-filtered rectifier: ΔV_o ≈ V_m/(2fRC) full-wave (Hart 4-4); half-wave ΔV_o ≈ V_m/(fRC) | L17–18 |
| Controlled bridge with RL, continuous vs discontinuous condition (α < β − π for continuous; Hart 4-7) | L20 |
| Multiphase star rectifier, 3-φ uncontrolled bridge (V_dc = 1.654V_m, Ex 3.7 performance) | L21–22 |
| 3-φ full converter input PF (Ex 10.5: HF = 31.08%, DF = cos α, PF = 0.955 cos α) | L22 |
| Linear regulator circuit, drawback (low efficiency, since the transistor drops V_s − V_o); SMPS solves it | L09 |
| Ćuk design (Hart 6-7), SEPIC numerical (Hart 6-8), boost design 2 (Hart 6-5) | L12, L14, L15 |
| ZCS (Hart 9-1) and ZVS (Hart 9-2): circuit, the four intervals, V_o = V_s·f_s·[…] equations | L23–24 |
| Solar PV standalone: PV array, MPPT DC-DC (boost/buck), charge controller, battery, inverter, load. DC-DC types used: buck, boost, buck-boost. **"Why pattern swapping"** in multi-source inverters: so each DC source is discharged equally | L35, L29 |

### TIER 3: External-risk zone (not in slides, but repeated in earlier papers)

Give these **one focused session** (Day 4). The external examiner tends to pick these.

1. **Parallel resonant DC-DC converter.** Same numbers in 2022 and 2024. V_s = 100 V, L_r = 8 µH, C_r = 0.32 µF, R_L = 10 Ω, f_s = 120 kHz.
   ω₀ = 1/√(LC) = 625 krad/s, ω_s = 754 krad/s, R_e = π²R_L/8 = 12.34 Ω. The fundamental of the square wave is 4V_s/π. Divide it between jX_L = j6.03 Ω and (R_e ∥ −j4.14 Ω) to get V_C1,peak ≈ 190 V. Then **V_o = 2V_C1/π ≈ 121 V** (≈ 1.2 V_s). Check this against Hart §9.6 if you can.
2. **Non-sinusoidal power computation** (Hart ch2), asked in every TT-1 and in 2021 and 2023. P = V₀I₀ + Σ V_n,rms I_n,rms cos θ_n; PF = P/(V_rms I_rms); **DF = I₁,rms/I_rms = 1/√(1+THD²)** (derivation asked in 2023); THD = √(I_rms² − I₁²)/I₁; crest factor = I_peak/I_rms.
3. **Bipolar PWM inverter** (m_a, m_f, table of normalised coefficients) and **harmonic elimination.** Know V₁ = m_a·V_dc, and that harmonics appear at m_f, m_f ± 2.
4. **DC motor speed control** with a chopper (field chopping, separately excited: V_a = DV_s, E_a = K_vωI_f) and **induction motor** speed control (variable voltage via AC controller, variable V/f via inverter).
5. **Effect of ESR and inductor resistance** on DC-DC output; buck **design** (5 V to 3.3 V, 2022).
6. TRIAC and DIAC structure, GTO, advantages of HVDC.

---

## 3. Four-day plan

Use a "3-pass" method for each topic: **(1)** read the slide and redraw the circuit and waveform from memory, **(2)** solve the slide example **without looking**, **(3)** write a 5-line summary of formulas and key words for your one-page formula sheet.

### Day 1: Devices and rectifiers (Part A core)
| Time block | Work |
|---|---|
| 3 h | **L02–L08**: device comparison table, BJT modes and switching, MOSFET/IGBT, **SCR (I-V, two-transistor derivation, turn-on methods, commutation A–E)**, diode reverse recovery numerical. Practise writing a 4-mark theory answer in 6–7 minutes. |
| 4 h | **L16–L22**: Hart 3-2, 3-5, 3-7, 3-8, 3-10, 4-1, 4-4, 4-6, 4-7; Rashid 3.4, 10.1, 10.4, 10.5, 3.7. **Do 10.4, 3-5, 4-1 and 3.4 twice.** Practise the 3-φ full converter derivation and waveform drawing. |
| 1 h | Solve 2024 Q1–Q3 under time. |

### Day 2: DC-DC and resonant
| Time block | Work |
|---|---|
| 4 h | **L09–L15**: derive buck, boost and buck-boost (equivalent circuits, waveforms, V_o, L_min, ΔV_o). Solve Hart 6-1, 6-4, 6-5, 6-6, 6-7, 6-8. Memorise SEPIC/Ćuk circuits and advantages. Linear regulator vs SMPS. |
| 2 h | **L23–L24**: ZCS (9-1), ZVS (9-2); learn the parallel resonant method from Tier 3. |
| 1 h | Solve 2023 Q4 and 2021 Q4 as practice. |

### Day 3: Inverters, AC-AC, cycloconverter and solar (Part B core)
| Time block | Work |
|---|---|
| 4 h | **L25–L29** handwritten notes: half and full bridge Fourier derivation, THD, DF, LOH; class example (48 V, 2.4 Ω); RL-load current; **Assessment #5 (quasi-square) and #6 (120° and 180° derivations)**; multilevel (5- and 7-level switch tables). |
| 2.5 h | **L31–L33**: 1-φ AC controller derivation and numerical (α = 90°, Assessment #7), 3-φ controller α = 60° waveform, cycloconverter 1-φ and 3-φ circuits and waveforms (f_s/3, f_s/4, f_s/5). |
| 0.5 h | **L35** solar standalone block diagram. |
| 1 h | Solve 2024 Q4–Q6 under time. |

### Day 4: Tier 3, mock exam and revision
| Time block | Work |
|---|---|
| 2 h | Tier 3: non-sinusoidal power (TT-1 problems from 2019/2020), bipolar PWM basics, motor drives, parallel resonant. |
| 2 h | **Full mock:** pick 6 questions (3 per part) from §5 below and write them in the exam time limit. |
| 2 h | Fix weak points; reread the formula sheet; redraw every waveform once (rectifier α waveforms, 3-φ grid, inverter gate sequence, cycloconverter). |
| Night | Sleep. Glance at the formula sheet only. |

---

## 4. Examples most likely to appear in your paper

The 2024 paper already used Ex 3.4, 10.4, 3-5, 4-1, 6-6, the gate-pulse example and the α = 90° AC controller. The instructor will probably either **reuse them** (as happened with parallel resonant in 2022 and 2024) or **take the next unused example from the same slides**:

| Rank | Example | Why |
|---|---|---|
| ★★★ | Inverter class example (48 V, 2.4 Ω) and full-bridge RL load | Inverters were barely used in 2024 and heavily emphasised for your batch |
| ★★★ | Assessment #5 quasi-square (δ = π/6), Assessment #6 120° derivation, Assessment #7 AC controller | The instructor's own recent problems for your batch |
| ★★★ | Rashid 10.1 (1-φ full converter HF, DF, PF) and 10.5 (3-φ input PF) | The paired example to 3.4 and 10.4 that were used in 2024 |
| ★★★ | Hart 4-6 (controlled bridge R load), 4-7 (discontinuous) | 4-6 was asked in 2022 and 2023 |
| ★★ | Hart 6-1 (buck), 6-4 and 6-5 (boost design), 6-7 (Ćuk), 6-8 (SEPIC) | 6-6 was used; the rest of the DC-DC set is open |
| ★★ | Hart 3-2, 3-7, 3-8, 3-10 | Half-wave family; 3-5 was used |
| ★★ | Hart 9-1 (ZCS), 9-2 (ZVS) | Resonant topic, 2021 used ZVS |
| ★★ | Multilevel 7-level switch table and THD | Detailed in your notes |
| ★★ | Cycloconverter f_o = f_s/3 waveform | Asked 4 out of 4 years |
| ★ | Hart 4-4 capacitor filter, Rashid 3.7 three-phase bridge | Supporting |

---

## 5. Model paper for practice (60 marks, my prediction)

**Part A** (answer Q1, Q2, and Q3 or Q4)
1. (a) Two-transistor model of SCR and derivation of I_A. [4] (b) Natural vs forced commutation with one example each; describe Class C. [3] (c) Gate pulse width numerical. [3]
2. (a) Derive V_o/V_s, L_min and ΔV_o/V_o for a boost converter, with waveforms. [5] (b) Hart 6-1 (buck) or 6-6 (buck-boost). [5]
3. (a) Single-phase full converter with ripple-free I_a: Fourier series of i_s, HF, DF, PF (Ex 10.1). [6] (b) Why can MOSFETs be paralleled but BJTs/SCRs cannot? [4]
4. (a) Three-phase full converter: derive V_dc and draw waveforms. [5] (b) Ex 10.4 or a variant. [5]

**Part B** (answer Q1, Q2, and Q3 or Q4)
1. (a) Full-bridge square-wave inverter Fourier series, V_o1,rms, THD. [4] (b) Quasi-square (δ) V_rms, V_n, and show that δ = 30° removes the 3rd harmonic. [6]
2. (a) 1-φ AC voltage controller derivation and α = 90° numerical. [6] (b) Cycloconverter principle with waveform for f_o = f_s/3. [4]
3. (a) Three-phase inverter in 180° (or 120°) mode: gate table, V_L,rms. [6] (b) 5-level cascaded inverter: circuit and switching table. [4]
4. (a) ZCS or parallel resonant converter numerical. [5] (b) Standalone solar PV diagram and the DC-DC converters used. [5]

---

## 6. One-page formula sheet

**Rectifiers**
- 1-φ half-wave R: V_o = V_m/π. Full-wave: V_o = 2V_m/π. Controlled half-wave: (V_m/2π)(1 + cos α). Controlled full-wave R: (V_m/π)(1 + cos α). Full converter (continuous): (2V_m/π) cos α.
- 3-φ bridge: V_o = 3V_m,LL/π = 1.35V_LL. Full converter: 1.35V_LL cos α. Harmonics at n = 6k.
- RL half-wave: i(ωt) = (V_m/Z)[sin(ωt−θ) + sin θ·e^(−ωt/ωτ)], Z = √(R²+(ωL)²), θ = tan⁻¹(ωL/R), ωτ = ωL/R.
- RL-source: α = sin⁻¹(V_dc/V_m); P_dc = I_o·V_dc; P_R = I_rms²·R.
- Fourier for full-wave: V_n = (2V_m/π)[1/(n−1) − 1/(n+1)], n = 2, 4, 6…
- Square-wave i_s: I_s1 = (2√2/π)I_a = 0.90I_a, HF = 0.4834.

**DC-DC** (CCM, D = duty ratio)
- Buck: V_o = DV_s; ΔI_L = (V_s−V_o)DT/L; L_min = (1−D)R/(2f); ΔV_o/V_o = (1−D)/(8LCf²).
- Boost: V_o = V_s/(1−D); I_L = V_s/((1−D)²R); L_min = D(1−D)²R/(2f); ΔV_o/V_o = D/(RCf).
- Buck-boost: V_o = −V_s·D/(1−D); I_L = V_sD/(R(1−D)²); L_min = (1−D)²R/(2f); ΔV_o/V_o = D/(RCf).
- Ćuk: V_o = −V_s·D/(1−D). SEPIC: V_o = +V_s·D/(1−D).

**Inverters**
- Half bridge: V_n = 2V_dc/(nπ). Full bridge: V_n = 4V_dc/(nπ). Quasi-square: V_n = (4V_dc/nπ) cos(nδ). THD(square) = 48.34%.
- 3-φ 180°: V_L = 0.8165V_dc, V_p = 0.4714V_dc. 3-φ 120°: V_L = 0.7071V_dc, V_p = 0.4082V_dc.
- I_n = V_n/√(R² + (nωL)²); P = Σ I_n,rms²·R.
- DF = (1/V₁)√Σ(V_n/n²)²; HF_n = V_n/V₁.

**AC-AC**
- 1-φ R: V_o = V_s√(1 − α/π + sin 2α / 2π); PF = V_o/V_s; I_T,avg = (√2V_s/2πR)(1 + cos α); I_T,rms = I_o/√2.
- Cycloconverter: f_o = f_s/k (k = 3, 4, 5…).

**Devices**
- I_A = (α₂I_G + I_CBO1 + I_CBO2)/(1 − α₁ − α₂).
- Q_RR = ½I_RR·t_rr; I_RR = t_rr·di/dt; t_rr = √(2Q_RR/(di/dt)).
- Gate pulse: i(t) = (V_s/R)(1 − e^(−tR/L)) with V_s = √2V sin α; t_G = t(I_H) + t_d.

---

## 7. Exam-hall strategy for full marks

1. **Choose the optional question in 2 minutes.** Pick the one with more numericals you have practised. Slide-example numericals give full marks if the method is right.
2. **For every derivation:** draw the circuit, then equivalent circuits, then waveforms with aligned time axes ("with proper alignment" appears in almost every paper), then the equation, then the boxed result.
3. **Label every waveform** (V_m, α, π, 2π, T_on = DT). Waveform marks are easy to lose.
4. **For numericals:** write the formula, substitute, give the answer with units, and box it. Partial marks depend on the formula line.
5. **Theory "compare/differentiate" questions:** always use a table of at least 5 rows.
6. **Time:** about 1.8–2 minutes per mark. Leave 10 minutes to review.
7. **If the external examiner adds a surprise:** it usually comes from Tier 3 or Hart/Rashid chapters near your slides. Write the governing equation, draw the circuit, and attempt the method. Partial credit counts.
