# APPENDIX A: MATHEMATICAL DERIVATIONS FOR LIGHTNING PROTECTION SYSTEMS

## A.1 Lightning Current and Electromagnetic Parameters

### A.1.1 Striking Distance Relationship

The striking distance relates directly to the peak lightning current through empirical relationships derived from laboratory measurements and field observations. This fundamental relationship establishes the protection zone dimensions used in the rolling sphere method.

**Derivation: Striking Distance Formula**

The striking distance rs (in meters) for lightning attachment to ground or structures varies with peak current I (in kiloamperes):

\[ r_s = 10 \times I^{0.65} \]

This empirical relationship originated from electrogeometric model (EGM) research conducted by CIGRE working groups and validated through extensive field observations. The exponent 0.65 represents statistical averaging of numerous lightning attachment observations, with the base coefficient 10 calibrated to meter and kiloampere units.

**Physical Interpretation:**

The non-linear relationship (exponent < 1) indicates that striking distance increases at a decreasing rate with increasing current. Higher currents exhibit stronger electric field intensification but do not increase striking distance proportionally. The formula applies for:
- Peak currents: 2-200 kA typical range
- Return stroke component analysis
- Protection level differentiation

**Protection Level Implications:**

For the four protection levels defined in NBR 5419:2015:

**Level I Protection:** Maximum current Imax = 200 kA
\[ r_{s,I} = 10 \times 200^{0.65} = 10 \times 31.62 = 316.2 \text{ m} \]

However, the rolling sphere radius limited to 20 m reflects practical optimization rather than pure striking distance, as higher percentile currents (near 200 kA) represent extreme events (1-5% probability).

**Level II Protection:** Maximum current Imax = 150 kA
\[ r_{s,II} = 10 \times 150^{0.65} = 10 \times 26.85 = 268.5 \text{ m} \]

**Level III Protection:** Maximum current Imax = 100 kA
\[ r_{s,III} = 10 \times 100^{0.65} = 10 \times 21.54 = 215.4 \text{ m} \]

**Level IV Protection:** Maximum current Imax = 100 kA
\[ r_{s,IV} = 10 \times 100^{0.65} = 10 \times 21.54 = 215.4 \text{ m} \]

**Design Consideration:** The rolling sphere radius represents a compromise between theoretical striking distance and practical protection coverage, selected through statistical analysis of lightning attachment probability distributions.

### A.1.2 Magnetic Field Calculation

Lightning currents generate intense transient magnetic fields inducing voltages in building wiring through time-derivative coupling mechanisms.

**Derivation: Magnetic Field Strength**

Magnetic field strength H (in A/m) at perpendicular distance d (in meters) from a lightning channel carrying current I follows Ampère's law:

\[ H(d) = \frac{I}{2\pi d} \]

This represents the azimuthal magnetic field component in cylindrical coordinates, valid for d >> channel radius.

**Current Rate of Change Effects:**

The induced voltage in a loop circuit depends on the magnetic flux variation:

\[ \Phi = \int \int B \cdot dA = \mu_0 \int \int H \cdot dA \]

For a rectangular loop enclosing area A at distance d:

\[ \Phi(d) = \frac{\mu_0 I A}{2\pi d} \]

The induced voltage follows Faraday's law:

\[ V = -\frac{d\Phi}{dt} = -\frac{\mu_0 A}{2\pi d} \frac{dI}{dt} \]

**Example Calculation (Building Wiring):**

Consider a 10 m × 20 m building loop at d = 50 m from a lightning channel carrying:
- Peak current I = 30 kA
- Current steepness dI/dt = 30 kA / 1 μs = 30 × 10⁹ A/s

\[ V = -\frac{4\pi \times 10^{-7} \times 10 \times 20}{2\pi \times 50} \times 30 \times 10^9 \]

\[ V = -\frac{2 \times 10^{-6} \times 30 \times 10^9}{50} = -1,200 \text{ V} \]

This represents significant overvoltage for equipment rated at 600 V nominal.

### A.1.3 Lightning Impulse Waveforms

Standard test waveforms characterize lightning current effects for protective device design.

**Derivation: Normalized Current Waveform**

Standard impulse currents follow mathematical models combining front rise and tail decay:

**Double-Exponential Model:**

\[ i(t) = I_p \left( e^{-\alpha t} - e^{-\beta t} \right) \]

where:
- Ip = peak current (A)
- α = tail decay coefficient (1/s)
- β = front rise coefficient (1/s)

**Parameters for Standard Waveforms:**

For 10/350 μs first-stroke representation (Level I protection):
- Tf = 10 μs (front time to 90% peak, defined as rise to 90%)
- Td = 350 μs (tail time to 50% peak)
- Peak current Ip = 30 kA (50% probability)

Coefficient calculation:
\[ \alpha = 0.693 / T_d = 0.693 / 350 \times 10^{-6} = 1,980 \text{ s}^{-1} \]

\[ \beta = 2.303 / T_f = 2.303 / 10 \times 10^{-6} = 230,300 \text{ s}^{-1} \]

**For 0.25/100 μs subsequent-stroke waveform (Level IV protection):**
- Faster rise with higher dI/dt
- Lower peak current (10 kA typical)
- More frequent events

### A.1.4 Energy Content Calculation

Protective device energy absorption capacity must accommodate impulse energy content.

**Derivation: Impulse Energy**

Total energy dissipated by lightning current in resistance R:

\[ W = \int_0^{\infty} i^2(t) R \, dt \]

For double-exponential waveform:

\[ W = \int_0^{\infty} I_p^2 \left( e^{-\alpha t} - e^{-\beta t} \right)^2 R \, dt \]

Expanding:

\[ W = I_p^2 R \int_0^{\infty} \left( e^{-2\alpha t} - 2e^{-(\alpha + \beta)t} + e^{-2\beta t} \right) dt \]

\[ W = I_p^2 R \left[ \frac{1}{2\alpha} - \frac{2}{\alpha + \beta} + \frac{1}{2\beta} \right] \]

**Example: 10/350 μs, 30 kA current through 1 Ω resistance**

With α = 1,980 s⁻¹, β = 230,300 s⁻¹:

\[ W = 30,000^2 \times 1 \times \left[ \frac{1}{3,960} - \frac{2}{232,280} + \frac{1}{460,600} \right] \]

\[ W = 9 \times 10^8 \times (0.000253 - 0.0000086 + 0.0000022) \]

\[ W \approx 2.16 \text{ MJ} \]

This represents typical Type 1 SPD energy absorption: 2.5-10 MJ capability.

---

## A.2 Grounding System Analysis

### A.2.1 Single Rod Resistance Derivation

The grounding resistance of a cylindrical rod in uniform soil follows from solving Laplace's equation in spherical coordinates with cylindrical geometry approximation.

**Derivation: Analytical Formula**

For a cylindrical rod of length L and radius a at depth h in uniform soil resistivity ρ:

\[ R = \frac{\rho}{2\pi L} \ln\left(\frac{4L}{a}\right) \]

**Derivation from First Principles:**

The potential distribution φ around a current-carrying rod follows:

\[ \nabla^2 \phi = 0 \]

In cylindrical coordinates, assuming current I entering at rod surface:

\[ \phi(r) = \frac{I\rho}{2\pi L} \ln(r) + C \]

At rod surface (r = a): φ = I × R (surface potential)

At remote ground (r → ∞): φ → 0

Therefore:
\[ I \times R = \frac{I\rho}{2\pi L} \ln(a) \]

Correction for end effects (current spreading at rod ends):

\[ R = \frac{\rho}{2\pi L} \left[\ln\left(\frac{4L}{a}\right) - 2\right] \]

**Practical Formula (neglecting -2 term for L >> a):**

\[ R \approx \frac{\rho}{2\pi L} \ln\left(\frac{4L}{a}\right) \]

**Example Calculation:**

Standard 3 m rod (diameter 5/8" = 15.875 mm) in typical Federal District soil (ρ = 1,500 Ω⋅m):

\[ R = \frac{1,500}{2\pi \times 3} \ln\left(\frac{4 \times 3}{0.007938}\right) \]

\[ R = \frac{1,500}{18.85} \ln(1,508.6) \]

\[ R = 79.6 \times 7.32 = 582.6 \, \Omega \]

This confirms that single rods rarely achieve acceptable resistance in high-resistivity soil without chemical treatment or multiple rods.

### A.2.2 Multiple Rod Arrays

**Derivation: Parallel Rod Resistance**

For n identical rods of resistance Rs spaced at distance S >> L:

Simple parallel combination:
\[ R_{simple} = \frac{R_s}{n} \]

However, mutual coupling reduces effectiveness. More accurate formula:

\[ R_n = \frac{R_s}{n \times \eta} \]

where η = utilization factor (0.5-0.9 depending on spacing).

**Utilization Factor Calculation:**

For rods spaced at distance S = kL (k = spacing factor):

\[ \eta \approx \frac{1}{n} + \frac{n-1}{2n(2k-1)} \]

**Examples:**

For 3 rods at S = L (k = 1):
\[ \eta = \frac{1}{3} + \frac{2}{6(2-1)} = 0.333 + 0.333 = 0.667 \]

\[ R_3 = \frac{582.6}{3 \times 0.667} = \frac{582.6}{2.0} = 291.3 \, \Omega \]

For 6 rods at S = 2L (k = 2):
\[ \eta = \frac{1}{6} + \frac{5}{12(4-1)} = 0.167 + 0.139 = 0.306 \]

Wait, this doesn't appear right. Let me recalculate:

\[ \eta = \frac{1}{6} + \frac{5}{12(3)} = 0.167 + 0.139 = 0.306 \]

Actually, this formula needs correction. The more accurate Sunde formula for parallel rods:

\[ R_n = R_s \left[ \frac{1}{n} + \frac{1}{\pi n(n-1)} \ln\left(\frac{2S}{a}\right) \right] \]

For 6 rods, S = 2L = 6 m, a = 0.007938 m:

\[ R_6 = 582.6 \left[ \frac{1}{6} + \frac{1}{\pi \times 6 \times 5} \ln\left(\frac{12}{0.007938}\right) \right] \]

\[ R_6 = 582.6 \left[ 0.167 + \frac{1}{94.25} \times 7.41 \right] \]

\[ R_6 = 582.6 \times (0.167 + 0.0786) = 582.6 \times 0.246 = 143.3 \, \Omega \]

### A.2.3 Ring Electrode Resistance

**Derivation: Circular Ring Formula**

A circular ring of radius r at burial depth h in uniform soil resistivity ρ:

\[ R_{ring} = \frac{\rho}{2\pi r} \]

For typical installation (r = 3 m, ρ = 1,500 Ω⋅m):

\[ R_{ring} = \frac{1,500}{2\pi \times 3} = \frac{1,500}{18.85} = 79.6 \, \Omega \]

**Combined Ring + Vertical Rod System:**

Approximately parallel combination (approximate):

\[ R_{combined} = \frac{R_{ring} \times R_{rod}}{R_{ring} + R_{rod}} \]

\[ R_{combined} = \frac{79.6 \times 291.3}{79.6 + 291.3} = \frac{23,189}{370.9} = 62.5 \, \Omega \]

This represents significant improvement, though still above 10 Ω target for educational buildings.

### A.2.4 Soil Resistivity Averaging

**Derivation: Wenner Method Analysis**

Wenner four-electrode measurement averages resistivity over measured depth approximately equal to electrode spacing a.

Applied voltage between outer electrodes C1-C2, measured voltage drop between inner electrodes P1-P2 in straight line configuration:

From potential superposition:
\[ V = \frac{I \rho}{2\pi} \left( \frac{1}{a} - \frac{1}{2a} - \frac{1}{2a} + \frac{1}{a} \right) = \frac{I \rho}{2\pi a} \]

Therefore measured resistance:
\[ R = \frac{V}{I} = \frac{\rho}{2\pi a} \]

Solving for resistivity:
\[ \rho = 2\pi a R \]

**Depth of Investigation:**

Maximum depth sensitivity approximately equals electrode spacing a. Multiple measurements at varying spacing create resistivity profiles:

- a = 1 m: samples top 1 m
- a = 3 m: samples 0-3 m depth
- a = 5 m: samples 0-5 m depth
- a = 10 m: samples 0-10 m depth

**Federal District Typical Profile (example):**

| Spacing (m) | Resistance (Ω) | ρ (Ω⋅m) |
|-------------|----------------|---------|
| 1           | 120            | 754     |
| 3           | 180            | 1,131   |
| 5           | 220            | 1,382   |
| 10          | 240            | 1,508   |

This profile indicates gradually increasing resistivity with depth, typical of plateau regions with weathered rock.

### A.2.5 Frequency-Dependent Impedance

**Derivation: Transient Response**

Grounding impedance at lightning frequencies (kilohertz to megahertz range) exceeds DC resistance due to inductive effects.

For a cylindrical rod:
\[ Z(f) = R + j\omega L \]

where:
- R = DC resistance (Ω)
- ω = 2πf (rad/s)
- L = inductance per unit length (H/m)

Rod inductance per unit length (internal):
\[ L_{internal} = \frac{\mu_0}{8\pi} \]

External inductance depends on geometric configuration and current return path.

**Total Rod Inductance:**
\[ L_{total} \approx 0.5 \mu H/m \]

For 3 m rod:
\[ L = 1.5 \, \mu H \]

**Impedance at Different Frequencies:**

At DC (f = 0):
\[ Z(0) = R = 79.6 \, \Omega \]

At f = 1 kHz:
\[ Z(1k) = \sqrt{79.6^2 + (2\pi \times 1,000 \times 1.5 \times 10^{-6})^2} \]
\[ Z(1k) = \sqrt{6,336 + 0.0089} \approx 79.6 \, \Omega \]

At f = 100 kHz (typical lightning frequency):
\[ Z(100k) = \sqrt{79.6^2 + (2\pi \times 100,000 \times 1.5 \times 10^{-6})^2} \]
\[ Z(100k) = \sqrt{6,336 + 0.895} \approx 79.7 \, \Omega \]

At f = 1 MHz:
\[ Z(1M) = \sqrt{79.6^2 + (2\pi \times 1,000,000 \times 1.5 \times 10^{-6})^2} \]
\[ Z(1M) = \sqrt{6,336 + 89.5} = \sqrt{6,426} \approx 80.2 \, \Omega \]

The modest increase at lightning frequencies reflects relatively low inductance. Dramatic impedance increases occur with complex electrode arrays and long conductor lengths.

---

## A.3 Risk Assessment Mathematics

### A.3.1 Strike Frequency Calculation

**Derivation: Ground Flash Density Conversion**

Ground flash density Ng (flashes/km²/year) from INPE data converts to individual structure strike frequency through collection area concept.

**Basic Formula:**
\[ N_D = N_g \times A_d \times 10^{-6} \]

where:
- ND = direct strikes per year
- Ng = ground flash density (flashes/km²/year)
- Ad = collection area (m²)
- 10⁻⁶ = conversion from km² to m²

**Collection Area Derivation:**

For rectangular structure with dimensions L × W and height H, the rolling sphere of radius rs intercepts strikes in an area larger than footprint due to oblique approaches:

\[ A_d = L \times W + 6 r_s (L + W) + 9\pi r_s^2 \]

**Geometric Interpretation:**

1. Central rectangle: L × W (direct footprint)
2. Side strips: 6rs(L + W) (sloped approach zones)
3. Corner zones: 9πrs² (curved corner interceptions)

The factor 9π reflects the combined corner geometry of four quarter-circles.

**Example: Educational Building**

Building dimensions: 40 m × 30 m, height 15 m
Protection Level III: rs = 45 m

\[ A_d = 40 \times 30 + 6 \times 45 \times (40 + 30) + 9\pi \times 45^2 \]

\[ A_d = 1,200 + 6 \times 45 \times 70 + 9\pi \times 2,025 \]

\[ A_d = 1,200 + 18,900 + 57,128 = 77,228 \, m^2 \]

For Federal District: Ng = 6 flashes/km²/year:

\[ N_D = 6 \times 77,228 \times 10^{-6} = 0.463 \text{ strikes/year} \]

This represents approximately 1 strike every 2.16 years to the structure's exposure envelope.

### A.3.2 Probability of Damage

**Derivation: Multi-Factor Probability**

Probability of damage combines multiple independent factors through multiplication rule of probability:

\[ P = P_{touch} \times P_{SPDA} \times P_{insulation} \]

where:
- Ptouch = probability of dangerous touch voltage
- PSPDA = probability SPD placement prevents damage
- Pinsulation = probability insulation withstands transient

**Touch Voltage Probability:**

For person in contact with potential-carrying conductor during lightning strike:

\[ P_{touch} \approx \frac{F(U)}{U_{total}} \]

where F(U) represents the fraction of tolerable touch voltage and Utotal the expected transient voltage.

For modern buildings with good bonding:
- Conventional SPD (Type 2): Ptouch ≈ 0.15-0.20
- ESE terminals (optimized): Ptouch ≈ 0.05-0.10
- Dissipation Array: Ptouch ≈ 0.01-0.03

**SPD Protection Factor:**

Probability SPD prevents damage through effective coordination:

\[ P_{SPD} = P_{functional} \times P_{coordination} \]

- Functional probability (component working): 0.95-0.98
- Coordination probability (correct placement and rating): 0.95-0.99
- Combined: 0.90-0.97

**Insulation Withstand:**

Modern equipment impulse withstand levels (per IEC 61010):

- Office equipment: 2.5 kV impulse
- Laboratory instruments: 4 kV impulse
- Data center servers: 3-6 kV impulse

SPD voltage protection levels:
- Type 1: Up = 2-4 kV
- Type 2: Up = 1.5-2.5 kV
- Type 3: Up = 0.8-1.5 kV

Probability insulation survives (equipment immunity > SPD Up):
\[ P_{insulation} = 0.98-0.99 \]

**Combined Probability Example:**

\[ P_{damage} = 0.15 \times 0.94 \times 0.98 = 0.138 \]

This represents approximately 14% probability that a lightning event reaching the building causes damaging overvoltage despite protective measures.

### A.3.3 Risk Component Integration

**Derivation: Total Risk Formula**

Each risk component Rx accumulates from multiple sources through summation:

\[ R_1 = R_A + R_B + R_C + R_M + R_U + R_V + R_W + R_Z \]

where each component follows:
\[ R_x = N_x \times P_x \times L_x \]

**Component Contribution Analysis:**

For typical educational building:

| Component | Type | Nx (events/yr) | Px | Lx | Rx |
|-----------|------|----------------|-----|----|------|
| RA | Direct strike structural damage | 0.46 | 0.05 | 0.10 | 0.0023 |
| RB | Direct strike fire risk | 0.46 | 0.03 | 0.20 | 0.0028 |
| RC | Direct strike electronics fail | 0.46 | 0.50 | 0.15 | 0.0345 |
| RM | Near strike LEMP effects | 1.2 | 0.30 | 0.10 | 0.0360 |
| RU | Service line damage | 0.3 | 0.10 | 0.10 | 0.0030 |
| RV | Service line fire | 0.3 | 0.05 | 0.20 | 0.0030 |
| RW | Service line electronics | 0.3 | 0.40 | 0.15 | 0.0180 |
| RZ | Service line LEMP | 0.5 | 0.20 | 0.10 | 0.0100 |
| **Total R1** | | | | | **0.0966** |

**Tolerable Risk Comparison:**

Calculated R1 = 0.0966 >> RT = 10⁻⁵ (tolerable)

This indicates unacceptable risk requiring substantial protection measures.

### A.3.4 Risk Reduction Factor

**Derivation: Protection Measure Effectiveness**

Each protection measure reduces corresponding probability factors:

\[ P_{protected} = P_{baseline} \times (1 - efficiency) \]

**External LPS Efficiency:**

SPDA protects against direct strikes. Efficiency depends on protection level:
- Level I: εSPDA = 0.98 (98% reduction)
- Level II: εSPDA = 0.95
- Level III: εSPDA = 0.90
- Level IV: εSPDA = 0.80

After external SPDA: RA, RB, RC reduced by corresponding efficiency.

**Coordinated SPD Efficiency:**

Properly coordinated SPDs reduce LEMP damage:
- Type 1 + Type 2 + Type 3: εSPD = 0.85
- Advanced coordination: εSPD = 0.95
- Mesh + SPD combination: εSPD = 0.98

**Risk Reduction Cumulative:**

After implementing Level III SPDA + coordinated SPDs:

\[ R_1^{protected} = R_1^{baseline} \times (1 - 0.90) \times (1 - 0.90) = 0.0966 \times 0.01 = 0.000966 \]

Still exceeds tolerable limit, requiring additional measures.

**Service Line Protection Measure:**

Isolating service lines (fiber optic for data, underground power):
- Efficiency: εservice = 0.99

Final risk:
\[ R_1^{final} = 0.000966 \times (1 - 0.99) + (service risk residual) \]

After complete protection implementation:
\[ R_1^{final} < 10^{-5} \text{ (achieved tolerable limit)} \]

---

## A.4 Electromagnetic Shielding Calculations

### A.4.1 Shielding Effectiveness Formula

**Derivation: Absorption and Reflection**

Total shielding effectiveness combines absorption (SE_A), reflection (SE_R), and multiple reflection correction (SE_MRC):

\[ SE_{total} = SE_A + SE_R + SE_{MRC} \]

**Absorption Loss:**

For electromagnetic wave penetrating conductive material:

\[ SE_A = 20 \log_{10}\left(\sqrt{\sigma_r \mu_r f}\right)^{1/2} \times t \]

where:
- σr = relative conductivity (vs copper)
- μr = relative permeability (vs free space)
- f = frequency (Hz)
- t = material thickness (m)

Simplified for non-magnetic conductors (μr ≈ 1):

\[ SE_A = 20 \log_{10}\left(\sqrt{\sigma_r f t}\right) \]

**Reflection Loss:**

At conductive surface:

\[ SE_R = 20 \log_{10}\left(\frac{Z_{free} + Z_{material}}{4 Z_{material}}\right) \]

For highly conductive materials >> free space impedance:

\[ SE_R \approx 20 \log_{10}\left(\frac{f \mu \sigma}{2}\right) \]

**Example: Concrete Wall Shielding**

Concrete with moisture (acting as dielectric lossy medium):
- Conductivity: σ = 10⁻² S/m
- Thickness: t = 0.3 m
- Frequency: f = 100 kHz (typical lightning)

\[ SE_A = 20 \log_{10}\left(\sqrt{10^{-2} \times 100,000 \times 0.3}\right) \]

\[ SE_A = 20 \log_{10}\left(\sqrt{300}\right) = 20 \log_{10}(17.3) = 24.8 \text{ dB} \]

This represents approximately 99.7% field attenuation.

### A.4.2 Mesh Shielding Requirements

**Derivation: Aperture Limitation**

Mesh dimensions must limit aperture size to ensure effective shielding:

\[ \text{Mesh size} < \frac{\lambda}{10} \]

where λ = c/f (free-space wavelength).

**Lightning Frequency Spectrum:**

Peak energy occurs around 10-100 kHz (return stroke derivative).

At f = 100 kHz:
\[ \lambda = \frac{3 \times 10^8}{100,000} = 3,000 \text{ m} \]

Required mesh < 300 m (impractical!).

However, lightning frequencies extend to megahertz range where criterion becomes meaningful:

At f = 1 MHz:
\[ \lambda = \frac{3 \times 10^8}{1,000,000} = 300 \text{ m} \]

Required mesh < 30 m (still large).

At f = 10 MHz:
\[ \lambda = \frac{3 \times 10^8}{10,000,000} = 30 \text{ m} \]

Required mesh < 3 m ✓

**Practical Mesh Selection:**

NBR 5419 specifies mesh dimensions by protection level based on empirical validation rather than rigorous frequency-dependent analysis:

- Level I: 5×5 m mesh
- Level II: 10×10 m mesh
- Level III: 15×15 m mesh
- Level IV: 20×20 m mesh

These reflect conservative protection ensuring effectiveness across lightning frequency spectrum.

### A.4.3 Shielding Factor Cascade

**Derivation: Multiple Boundary Attenuation**

Progressive zone transitions each provide cumulative shielding:

\[ SE_{total} = SE_1 + SE_2 + SE_3 + SE_4 \]

Or in probability form (multiplicative):

\[ P_{LEMP} = P_0 \times K_{S1} \times K_{S2} \times K_{S3} \]

where KSi = 10^(-SEi/20) represents transmission coefficient.

**Example: Building Steel Frame + Mesh Shielding**

LPZ 0 → 1 (outer boundary):
- Concrete thickness: 0.3 m
- SE1 = 25 dB
- KS1 = 10^(-25/20) = 0.0562

LPZ 1 → 2 (equipment room boundary):
- Metal mesh ceiling: mesh 0.1 m
- SE2 = 40 dB
- KS2 = 10^(-40/20) = 0.01

Combined transmission:
\[ P_{LEMP} = 1.0 \times 0.0562 \times 0.01 = 0.000562 \]

This represents 99.94% field attenuation, providing excellent protection.

---

## A.5 Separation Distance Calculations

### A.5.1 Fundamental Separation Distance

**Derivation: Flashover Prevention**

Separation distance prevents dangerous side-flashing between SPDA conductors and internal installations during lightning surge:

\[ s = k_i \times \frac{k_c}{k_m} \times L \]

where:
- ki = protection level factor (0.04-0.08 depending on level)
- kc = current distribution factor (0.44-1.0)
- km = material factor (0.5-1.0)
- L = conductor length (m)

**Protection Level Factors:**

Derived from breakdown voltage testing:
- Level I: ki = 0.08 m/kA
- Level II: ki = 0.06 m/kA
- Level III: ki = 0.05 m/kA
- Level IV: ki = 0.04 m/kA

These factors ensure flashover voltage exceeds expected surge voltage.

### A.5.2 Current Distribution Coefficient

**Derivation: Multiple Path Effects**

Current distribution in parallel down-conductor network:

\[ I_1 = I \times \frac{Z_eq - Z_1}{\sum Z_{eq}} \]

For n identical down conductors in parallel, fraction through each:

\[ f = \frac{1}{n} \]

Current distribution factor:

\[ k_c = \sqrt{\sum f^2} = \sqrt{\frac{1}{n}} = \frac{1}{\sqrt{n}} \]

**Examples:**

Single down conductor: kc = 1.0
Two down conductors: kc = 1/√2 = 0.707
Three down conductors: kc = 1/√3 = 0.577
Four down conductors: kc = 1/√4 = 0.5

For standard educational building with 3-4 down conductors: kc ≈ 0.5-0.6

### A.5.3 Material Coefficients

**Derivation: Breakdown Voltage**

Material factor reflects dielectric strength:

\[ k_m = \frac{U_{breakdown}(concrete)}{U_{breakdown}(air)} \]

Experimental values:
- Air: km = 1.0 (baseline)
- Dry concrete: km = 0.5-0.6
- Wet concrete: km = 0.7-0.8
- Brick: km = 0.5-0.6
- Compressed board: km = 0.5

**Breakdown Voltage Relationships:**

Air breakdown: approximately 3 kV/mm (dry conditions)
Concrete: 1-1.5 kV/mm (depending on moisture and composition)

Ratio: km = 1.5/3 = 0.5 ✓

### A.5.4 Separation Distance Example

**Building Configuration:**

- Protection level: III
- Down conductors: 3 parallel paths
- Material: Wet concrete (km = 0.7)
- Down conductor length: 25 m
- Routing: Direct path from roof to ground

Calculation:

\[ s = 0.05 \times \frac{0.577}{0.7} \times 25 \]

\[ s = 0.05 \times 0.824 \times 25 = 1.03 \text{ m} \]

This indicates minimum 1 m separation between SPDA conductors and internal wiring must be maintained. Architectural routing must account for this constraint.

---

## A.6 Impulse Impedance and Transient Behavior

### A.6.1 Laplace Transform Analysis

**Derivation: Transient Response**

For RLC circuit representing grounding electrode network:

\[ L\frac{di}{dt} + Ri + \frac{1}{C}\int i \, dt = v(t) \]

Applying Laplace transform (s = σ + jω):

\[ LsI(s) + RI(s) + \frac{I(s)}{sC} = V(s) \]

\[ I(s) = \frac{V(s)}{R + Ls + \frac{1}{sC}} \]

Transfer function (impedance):

\[ Z(s) = R + Ls + \frac{1}{sC} \]

### A.6.2 Step Response to Impulse Current

**Derivation: Voltage Rise Time**

For step current input (current source suddenly reaching Imax), voltage rises through:

\[ v(t) = I_{max} \left(R + L\frac{d\delta(t)}{dt} + \int_0^t \frac{i(\tau)}{C}d\tau\right) \]

Impulse response (instantaneous):
\[ v(0^+) = I_{max} \times L \times \frac{d\delta(t)}{dt} \]

This represents the inductive spike responsible for transient overvoltages.

### A.6.3 Frequency Response

**Derivation: Magnitude Response**

For sinusoidal driving voltage v(t) = V0 cos(ωt):

\[ |Z(j\omega)| = \sqrt{R^2 + \left(\omega L - \frac{1}{\omega C}\right)^2} \]

At resonance frequency ω0 = 1/√(LC):

\[ |Z(j\omega_0)| = R \text{ (minimum)} \]

**Federal District Typical Values:**

- R ≈ 80 Ω (as calculated previously)
- L ≈ 1.5 μH (for 3 m rod)
- C ≈ 100 pF (distributed in soil)

Resonance frequency:

\[ f_0 = \frac{1}{2\pi\sqrt{LC}} = \frac{1}{2\pi\sqrt{1.5 \times 10^{-6} \times 100 \times 10^{-12}}} \]

\[ f_0 = \frac{1}{2\pi \times 1.22 \times 10^{-8}} \approx 1.3 \text{ MHz} \]

This indicates impedance minimum at megahertz frequencies, relevant to higher-frequency lightning components.

### A.6.4 Soil Ionization Effects

**Derivation: Nonlinear Resistance**

At high current densities (> 500 A/m²), soil ionization dramatically reduces resistance:

\[ R(I) = R_0 + R_{nonlinear}(I) \]

where nonlinear component:

\[ R_{nonlinear}(I) = -R_0 \times \left(1 - e^{-I/I_c}\right) \]

Critical current Ic (soil-dependent):
\[ I_c = 2\pi E_c d^2 / \rho \]

where Ec ≈ 300-500 kV/m (ionization field strength).

**Example: Federal District Soil**

- E c = 400 kV/m
- d = 0.008 m (rod radius)
- ρ = 1,500 Ω⋅m

\[ I_c = \frac{2\pi \times 400,000 \times (0.008)^2}{1,500} \]

\[ I_c = \frac{2\pi \times 400,000 \times 64 \times 10^{-6}}{1,500} \]

\[ I_c = \frac{160.8}{1,500} \approx 0.107 \text{ A} \]

This very low value indicates ionization occurs at minimal currents, with significant effects at lightning current levels (kiloamperes).

---

## A.7 SPD Protection Level Calculations

### A.7.1 Voltage Protection Level Coordination

**Derivation: Cascade Design**

Each SPD stage must provide adequate voltage limiting while coordinating with preceding stages.

**Type 1 SPD Voltage:**

For spark gap device with impulse current Iimp and gap distance d:

\[ U_p = U_{residual} + U_{front} \]

where:
- Uresidual = residual voltage across device conducting full Iimp
- Ufront = voltage drop in connecting leads during current rise

Typical values:
- Residual: 2-4 kV
- Lead drop: 1-2 kV
- Total: 3-6 kV

**Type 2 SPD Voltage:**

Varistor-based devices with lower conducting current:

\[ U_p = U_{MOV}(I_n) \]

where In = nominal discharge current (typically 20 kA):
- At 20 kA: Up = 1.5-2.5 kV

**Type 3 SPD Voltage:**

Point-of-use devices with lowest protection level:

\[ U_p = U_{equipment} - U_{safety\_margin} \]

For 600V equipment with 1.5 kV standard impulse withstand:
- Up = 800-1,200 V

### A.7.2 Let-Through Voltage Analysis

**Derivation: Lead Inductance Effects**

During SPD conduction, voltage across conducting device combines resistance and inductive components:

\[ V_{SPD} = I R_{SPD} + L\frac{dI}{dt} \]

Connection lead inductance dominates:

\[ L \approx 0.5 \mu H\text{/m for twin conductors} \]

Example: 1 m connection leads

\[ L = 0.5 \mu H \]

For 10/350 μs current waveform with peak 50 kA:

\[ \frac{dI}{dt} \approx \frac{50,000}{10 \times 10^{-6}} = 5 \times 10^9 \text{ A/s} \]

Inductive voltage:

\[ V_L = L \times \frac{dI}{dt} = 0.5 \times 10^{-6} \times 5 \times 10^9 = 2,500 \text{ V} \]

This emphasizes importance of minimizing lead length (< 0.5 m recommended).

### A.7.3 Cascading Voltage Drop

**Derivation: Cumulative Attenuation**

Total voltage appearing at equipment follows cascade:

\[ V_{equipment} = V_{Type1} + V_{leads1-2} + V_{Type2} + V_{leads2-3} + V_{Type3} \]

With 10 m separation between Type 1 and Type 2:

\[ V_{leads} = L \times \frac{dI}{dt} = (0.5 \mu H/m \times 10 m) \times 5 \times 10^9 \]

\[ V_{leads} = 5 \mu H \times 5 \times 10^9 = 25,000 \text{ V} \]

This illustrates why 10 m minimum separation requires decoupling inductors to reduce lead inductance effect.

---

## A.8 Climate Change Impact on Lightning Frequency

### A.8.1 Temperature Scaling Relationship

**Derivation: Thermodynamic Basis**

Lightning frequency correlates with atmospheric instability measured through Convective Available Potential Energy (CAPE):

\[ \text{CAPE} = g \int_{z_b}^{z_t} \frac{T_e - T_e}{T_e} dz \]

where Te = environmental temperature, Tep = parcel equivalent potential temperature.

Empirical observations show:

\[ \frac{\Delta f}{f} = k \times \Delta T \]

where k = sensitivity coefficient ≈ 0.12 (12% increase per °C).

### A.8.2 Federal District Projections

**Derivation: Regional Climate Model**

HADGEM2 and MIROC5 climate models for Central Brazil project:

**Temperature increase by 2100:**
- Conservative scenario: +2.5°C
- Intermediate scenario: +3.5°C
- High emission scenario: +5.0°C

**Lightning frequency change:**

Current frequency (baseline): f0 = 6 flashes/km²/year

Conservative scenario:
\[ f_{2100} = 6 \times (1 + 0.12 \times 2.5) = 6 \times 1.30 = 7.8 \text{ flashes/km}^2\text{/year} (+30\%) \]

High emission scenario:
\[ f_{2100} = 6 \times (1 + 0.12 \times 5.0) = 6 \times 1.60 = 9.6 \text{ flashes/km}^2\text{/year} (+60\%) \]

This implies protection systems designed for current lightning density become insufficient in coming decades, requiring:
- Protective level upgrades from IV to III or II
- Enhanced SPD coordination
- Preventive maintenance increases
- Replacement of degraded components

---

## A.9 Acoustic Analysis of Lightning Phenomena

### A.9.1 Thunder Generation

**Derivation: Sound from Heated Channel**

Lightning channel heating to 20,000 K creates rapid expansion:

\[ p(r) = \frac{\gamma_0 I^2 L}{c_v r} \]

where:
- γ₀ = atmospheric ratio of specific heats ≈ 1.4
- I = lightning current (A)
- L = channel length (m)
- cv = specific heat at constant volume
- r = distance (m)

Initial blast wave pressure:

\[ \Delta p = \frac{(\gamma_0 - 1) E_{channel}}{4\pi r^3 c_v} \]

Typical value at 100 m for 30 kA strike:
\[ \Delta p \approx 10 \text{ Pa (120 dB SPL)} \]

### A.9.2 Lightning Location from Thunder Timing

**Derivation: Sound Propagation**

Sound travels at vs ≈ 343 m/s in standard air. Distance to strike:

\[ d = v_s \times \Delta t \]

where Δt = time delay between lightning flash and thunder.

Example: 5 second delay
\[ d = 343 \times 5 = 1,715 \text{ m (1.7 km)} \]

Rule of thumb: 3 seconds per km for simplified calculation.

---

## A.10 Economic Analysis Formulas

### A.10.1 Net Present Value (NPV)

**Derivation: Time-Value Accounting**

Protection system cost-benefit analysis:

\[ NPV = -I_0 + \sum_{t=1}^{N} \frac{B_t - C_t}{(1+r)^t} \]

where:
- I₀ = initial investment
- Bt = benefits in year t
- Ct = operating costs in year t
- r = discount rate (typically 5-10% real)
- N = project lifetime (typically 20-30 years)

**Educational Building Example:**

Initial SPDA investment: I₀ = R$ 500,000
Annual maintenance: Ct = R$ 5,000
Annual inspection: Ct = R$ 2,000
Average annual benefit (avoided losses): Bt = R$ 25,000
Discount rate: r = 0.08
Project lifetime: N = 25 years

\[ NPV = -500,000 + \sum_{t=1}^{25} \frac{25,000 - 7,000}{(1.08)^t} \]

\[ NPV = -500,000 + 18,000 \times \sum_{t=1}^{25} \frac{1}{(1.08)^t} \]

\[ NPV = -500,000 + 18,000 \times 10.675 = -500,000 + 192,150 = -307,850 \]

Negative NPV indicates protection investment exceeds tangible benefits over 25 years. However, life safety value and risk tolerance justify investment despite negative NPV.

### A.10.2 Payback Period

**Derivation: Time to Cost Recovery**

Simple payback (undiscounted):

\[ T_{payback} = \frac{I_0}{\bar{B}} \]

where Ā = average annual net benefit.

\[ T_{payback} = \frac{500,000}{18,000} = 27.8 \text{ years} \]

This exceeds typical system lifetime, indicating recoup occurs only through avoided major incidents.

---

## A.11 Material Specifications and Conductor Sizing

### A.11.1 Cross-Section Calculation

**Derivation: Thermal Capacity**

Conductor cross-section must withstand lightning current heating without melting:

\[ A = \frac{I^2 t}{f \times c_m} \]

where:
- I = lightning current (A)
- t = current duration (s)
- f = material constant (A²s/mm²)
- cm = temperature coefficient

For copper with 10/350 μs waveform (charge Q = 250 C):

\[ A = \frac{I \times Q}{k \times T_{rise}} \]

Simplified formula from NBR 5419:

For 10/350 μs current, minimum cross-sections:

**Level I (200 kA potential):**
- Copper: 70 mm² (AWG 2/0)
- Aluminum: 120 mm² (AWG 1)
- Steel: 150 mm² (galvanized)

**Level IV (100 kA potential):**
- Copper: 50 mm² (AWG 1/0)
- Aluminum: 85 mm²
- Steel: 100 mm²

### A.11.2 Corrosion Compatibility

**Derivation: Galvanic Series**

Galvanic compatibility prevents galvanic corrosion at dissimilar metal contacts:

\[ I_{corrosion} = \frac{E_{cell}}{R_{polarization}} \]

where Ecell = difference in standard electrode potentials.

Copper-Steel contact in humid environment (typical for Brazil):

Ecell ≈ 0.5 V (large separation in galvanic series)

This promotes corrosion at steel surface unless:
- Electrical insulation prevents current flow
- Sacrificial protection applied
- Material compatibility ensured

**Solutions:**

- Copper-bonded steel (not susceptible to differential corrosion)
- Plated steel (zinc or nickel coating)
- Stainless steel 316 (excellent but expensive)
- Proper isolation and drainage
---

**End of Appendix A: Mathematical Derivations**
