# Doctoral Thesis: Lightning Protection Systems (SPDA) According to NBR 5419:2015
## Figure Placement Guide and List of Figures

---

## CHAPTER 2: THEORETICAL FOUNDATIONS OF LIGHTNING PROTECTION SYSTEMS

### 2.1 Evolution of Brazilian Lightning Protection Standards

The transition from NBR 5419:2005 to NBR 5419:2015 represents a fundamental paradigm shift in lightning protection engineering in Brazil. The expansion from a 49-page prescriptive document to a comprehensive 309-page risk-management framework aligned with IEC 62305 necessitates detailed analysis.

### 2.2 Protection Methods and Determination Criteria

#### 2.2.1 Rolling Sphere Method

The rolling sphere method constitutes the primary methodology for determining protection zones in modern SPDA design. The sphere radius varies according to the selected protection level, ranging from 20m for Level I to 60m for Level IV, as specified in NBR 5419:2015 Part 3.

**.fig1** [Insert Figure 1: Rolling Sphere Method and Protection Angles per NBR 5419:2015]

The protection angle α decreases with increasing structure height h, following a non-linear relationship that becomes critical for structures exceeding 20m in height. For structures above 60m, the protection angle methodology becomes insufficient, necessitating exclusive application of the rolling sphere or mesh methods.

#### 2.2.2 Mesh Method (Faraday Cage)

The mesh method provides comprehensive protection through a network of conductors forming a Faraday cage around the structure. The mesh dimensions correlate directly with the protection level, as prescribed in Table 2 of NBR 5419:2015 Part 3.

**.fig2** [Insert Figure 2: Mesh Conductor Spacing Requirements per Protection Level]

The mesh spacing requirements range from 5×5m for Level I to 20×20m for Level IV, with intermediate values for Levels II and III. Down conductors must maintain maximum spacing of 10m for Level I, increasing to 20m for Level IV.

---

## CHAPTER 3: RISK MANAGEMENT METHODOLOGY

### 3.1 Probabilistic Risk Assessment Framework

The risk management approach introduced in NBR 5419:2015 Part 2 represents a significant advancement over the deterministic methods of the previous standard. The methodology requires systematic evaluation of four distinct loss types (L1-L4) and eight risk components (RA through RZ).

**.fig3** [Insert Figure 3: Risk Assessment Methodology per NBR 5419:2015 Part 2]

The iterative nature of the risk assessment process requires continuous refinement until the calculated risk R falls below the tolerable risk threshold RT. This probabilistic approach enables optimized protection solutions tailored to specific structure characteristics and environmental conditions.

---

## CHAPTER 4: INTERNAL PROTECTION SYSTEMS AND SPD COORDINATION

### 4.1 Lightning Protection Zones (LPZ) and SPD Implementation

The concept of Lightning Protection Zones, as defined in NBR 5419:2015 Part 4, establishes a systematic approach to electromagnetic compatibility within structures. The transition from LPZ 0A (direct strike zone) through successive zones requires coordinated SPD implementation.

**.fig4** [Insert Figure 4: SPD Coordination per NBR 5419:2015 Part 4]

The voltage protection level Up must decrease progressively from the structure boundary to sensitive equipment locations. Type 1 SPDs, capable of conducting partial lightning currents (Iimp), are mandatory at LPZ 0/1 boundaries. Subsequent protection stages employ Type 2 and Type 3 devices with progressively lower Up values.

---

## CHAPTER 5: GROUNDING SYSTEMS AND EQUIPOTENTIAL BONDING

### 5.1 Grounding Arrangements According to NBR 5419:2015

The standard prescribes three primary grounding arrangements: Type A (ring earth electrode), Type B (foundation earth electrode), and vertical rod configurations. Each arrangement presents distinct advantages regarding impulse impedance characteristics and long-term stability.

**.fig5** [Insert Figure 5: Grounding Arrangements per NBR 5419:2015]

The grounding resistance requirement of ≤10Ω, while generally applicable, must be evaluated in the context of soil resistivity variations and impulse impedance behavior. The relationship between steady-state resistance and impulse impedance becomes critical for high-frequency lightning current components.

### 5.2 Separation Distance Requirements

The separation distance s between the SPDA and internal metallic installations prevents dangerous sparking. The calculation methodology, specified in Section 6.3 of NBR 5419:2015 Part 3, incorporates factors for protection level (ki), current distribution (kc), and material insulation (km).

**.fig6** [Insert Figure 6: Separation Distance Requirements per NBR 5419:2015]

The separation distance increases linearly with conductor length L, necessitating careful consideration in tall structures where maintaining adequate separation becomes challenging.

---

## CHAPTER 6: REGIONAL CONSIDERATIONS - BRASÍLIA FEDERAL DISTRICT

### 6.1 Lightning Incidence Characteristics

The Federal District of Brazil, particularly the Brasília region, experiences exceptional lightning activity with ground flash density (Ng) averaging 15 flashes/km²/year. This value significantly exceeds the national average and approaches the maximum values observed in tropical convective regions.

**.fig7** [Insert Figure 7: Lightning Activity in Brasília Federal District Region]

The seasonal distribution demonstrates pronounced concentration during the wet season (October-April), with over 90% of annual activity occurring during these months. This temporal clustering necessitates heightened vigilance in protection system maintenance and testing schedules.

---

## CHAPTER 7: MATERIAL SPECIFICATIONS AND INSTALLATION PRACTICES

### 7.1 Material Selection Criteria

The selection of appropriate materials for SPDA components requires consideration of mechanical strength, corrosion resistance, and galvanic compatibility. NBR 5419:2015 Part 3, Section 5.3, specifies minimum cross-sectional areas and material properties.

**.fig8** [Insert Figure 8: Material Specifications and Installation Methods per NBR 5419:2015]

Copper remains the preferred material for corrosion resistance, though economic considerations often favor galvanized steel. Aluminum applications require careful evaluation of galvanic corrosion potential, particularly in coastal or industrial environments. Connection methods significantly impact system longevity, with exothermic welding providing superior electrical and mechanical characteristics.

---

## APPENDIX A: LIST OF FIGURES

**Figure 1:** Rolling Sphere Method and Protection Angles per NBR 5419:2015
- (a) Rolling Sphere Radii by Protection Level
- (b) Protection Angle vs Height relationship according to NBR 5419:2015

**Figure 2:** Mesh Conductor Spacing Requirements per Protection Level (NBR 5419:2015, Table 2)
- Shows spacing requirements for Levels I-IV with down conductor positioning

**Figure 3:** Risk Assessment Methodology per NBR 5419:2015 Part 2
- Flowchart depicting iterative risk evaluation and SPM selection process

**Figure 4:** SPD Coordination per NBR 5419:2015 Part 4
- (a) Lightning Protection Zones (LPZ) and SPD Placement
- (b) Voltage Protection Level Cascade

**Figure 5:** Grounding Arrangements per NBR 5419:2015
- (a) Type A - Ring Electrode
- (b) Type B - Foundation Electrode
- (c) Vertical Rod Array
- (d) Equipotential Bonding
- (e) Resistance vs Soil Resistivity
- (f) Impulse Impedance Response

**Figure 6:** Separation Distance Requirements per NBR 5419:2015
- (a) Separation Distance Concept
- (b) Required Separation Distance vs Conductor Length

**Figure 7:** Lightning Activity in Brasília Federal District Region
- (a) Lightning Density Map - Federal District
- (b) Seasonal Distribution - Brasília Region

**Figure 8:** Material Specifications and Installation Methods per NBR 5419:2015
- (a) Material Specifications Table
- (b) Conductor Cross-Sections
- (c) Connection Methods
- (d) Galvanic Corrosion Compatibility Matrix

---

## APPENDIX B: FIGURE GENERATION METHODOLOGY

All technical figures were generated using Python 3.12 with Matplotlib 3.8 for precise technical accuracy. The visualizations incorporate data from NBR 5419:2015 tables and formulas, ensuring compliance with standard requirements. Color coding follows international conventions for protection levels (I-IV) and risk categories.

Figure generation parameters:
- Resolution: 300 DPI (publication quality)
- Format: PNG with transparency
- Dimensions: Optimized for A4 page layout
- Font: DejaVu Sans (fallback from Times New Roman)
- Line weights: 1.5pt for primary elements, 1.0pt for secondary

---

## TECHNICAL NOTES ON FIGURE INTERPRETATION

### Protection Level Color Scheme:
- Level I (Highest): Red (#FF0000)
- Level II: Orange (#FFA500)
- Level III: Yellow (#FFFF00)
- Level IV (Standard): Green (#00FF00)

### Coordinate Systems:
All spatial dimensions utilize metric units (meters) as prescribed by NBR 5419:2015. Electrical parameters employ SI units with appropriate scaling for readability.

### Data Sources:
- Protection angles: NBR 5419:2015 Part 3, Table 3
- Mesh spacing: NBR 5419:2015 Part 3, Table 2
- Material specifications: NBR 5419:2015 Part 3, Section 5.3
- SPD characteristics: NBR 5419:2015 Part 4, Annex D
- Lightning density data: INPE/ELAT database 2024

---

## CITATION GUIDELINES FOR FIGURES

When referencing these figures in the thesis text, employ the following format:

"As illustrated in Figure X, the [specific phenomenon] demonstrates [observed behavior] according to NBR 5419:2015 Part Y."

For comparative analyses:
"Comparing Figures X and Y reveals the critical relationship between [parameter 1] and [parameter 2] in SPDA design optimization."

Cross-references between figures should maintain consistency in terminology and symbology throughout the dissertation.

---

End of Figure Placement Guide