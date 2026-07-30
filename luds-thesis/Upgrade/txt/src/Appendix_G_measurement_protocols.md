# APPENDIX G
## Lightning Protection Systems (SPDA) - Measurement Protocols

---

# APPENDIX G: FIELD MEASUREMENT PROTOCOLS AND PROCEDURES

## G.1 Soil Resistivity Measurement - Wenner Four-Point Method

### G.1.1 Equipment Requirements

**Essential Equipment:**
- Soil resistivity tester (4-terminal instrument): Fluke 1625-2, AEMC MRU-200, or equivalent
- Four copper electrodes or stakes (minimum 5/8" diameter, 40 cm length)
- Connecting cables (insulated, rated for field conditions)
- Measuring tape (minimum 50 m length)
- GPS unit or surveying equipment (±5 m accuracy minimum)
- Data recording forms and notebook
- PPE: safety glasses, work gloves, steel-toed boots, hard hat
- Compass for directional reference

**Equipment Calibration Requirements:**
- Instruments must have current ISO 17025 certification
- Calibration date must be within 12 months prior to testing
- Certificates must be maintained in project documentation
- Field verification using known resistive standards ±5% accuracy required

### G.1.2 Site Preparation and Safety

**Pre-Test Safety Procedures:**
1. Mark and identify all underground utilities (call Dial Before You Dig service)
2. Locate high-voltage power lines; maintain minimum 10 m clearance
3. Identify buried communication cables and water/sewer lines
4. Obtain landowner permission and necessary site access permits
5. Post warning signs at active measurement locations
6. Ensure wet soil conditions (avoid measurements during drought) or note soil moisture status
7. Document weather conditions (temperature, rainfall, humidity)

**Personnel Requirements:**
- Minimum two qualified personnel on site (safety partner requirement)
- Personnel must complete field safety orientation
- One person designated as safety officer
- All personnel trained in electrical hazard recognition

### G.1.3 Wenner Four-Point Electrode Configuration

**Electrode Placement:**
```
    C1 -------- P1 -------- P2 -------- C2
    |           |           |           |
   0 m         a m         2a m        3a m

Spacing distance: a = measurement variable (5 m, 10 m, 20 m, 30 m typical)
```

**Configuration Details:**
- Four electrodes arranged in straight line
- Equal spacing (a) between adjacent electrodes
- Current electrodes: C1 (outer left), C2 (outer right)
- Potential electrodes: P1, P2 (inner pair at 61.8% of outer spacing distance)
- All electrodes driven perpendicular to earth surface at equal depth

**Multiple Traverse Requirements:**
- Minimum three perpendicular traverse lines at each site (120° orientation separation)
- Minimum 5 measurements per traverse
- Total minimum 15 independent measurements per site
- Document location of each measurement (GPS coordinates)

### G.1.4 Measurement Procedure

**Step-by-Step Protocol:**

1. **Electrode Installation:**
   - Drive current electrode C1 to full depth (typically 40 cm)
   - Measure distance a with tape measure
   - Drive potential electrode P1 at position a
   - Drive potential electrode P2 at position 2a
   - Drive current electrode C2 at position 3a
   - Verify electrode alignment and spacing

2. **Connection Verification:**
   - Connect C1 (current positive) to positive terminal on instrument
   - Connect P1 (potential positive) to potential positive terminal
   - Connect P2 (potential negative) to potential negative terminal
   - Connect C2 (current negative) to current negative terminal
   - Visually verify all connections secure and insulated

3. **Instrument Setup:**
   - Select 4-terminal measurement mode
   - Set measurement frequency to 1 kHz (if variable; standard configuration)
   - Zero instrument per manufacturer protocol
   - Record instrument serial number and calibration date

4. **Measurement Acquisition:**
   - Activate measurement (press start on instrument)
   - Allow 5-10 seconds for stabilization
   - Record resistance value to 0.1 ohm precision
   - Note any error indicators or warnings
   - Perform second measurement at same location
   - Record both values and average if within 5% agreement; otherwise repeat

5. **Data Recording:**
   - Record time of measurement (HHMM)
   - Record temperature (±1°C)
   - Record soil moisture condition (wet/moist/dry assessment)
   - Record recent rainfall (hours and approximate amount)
   - Note soil type visual observation (clay/sandy/rocky)
   - Record GPS coordinates (latitude/longitude ±5 m)
   - Record measured resistance value (Ω)
   - Record calculated resistivity: ρ = 2πaR (Ω·m)

### G.1.5 Multi-Spacing Depth Profiling

**Spacing Protocol for Resistivity Stratification:**

| Spacing (a, m) | Effective Depth (approx., m) | Purpose |
|---|---|---|
| 1 | 0.5-1.0 | Topsoil characterization |
| 2 | 1.0-2.0 | Shallow subsurface |
| 3 | 1.5-3.0 | Upper earth layer |
| 5 | 2.5-5.0 | Primary depth range |
| 10 | 5-10 | Deeper investigation |
| 20 | 10-20 | Deep layer assessment |
| 30 | 15-30 | Bedrock proximity |

**Recommended Measurement Sequence:**
1. Perform all 5 m spacing measurements (standard reference)
2. Perform 3 m spacing measurements (shallow verification)
3. Perform 10 m spacing measurements (deep characterization)
4. Perform 20 m spacing if available space permits
5. Plot ρ vs. depth to identify stratification

### G.1.6 Data Analysis and Interpretation

**Apparent Resistivity Calculation:**
ρ_a = 2πaR

Where:
- ρ_a = apparent resistivity (Ω·m)
- a = electrode spacing (m)
- R = measured resistance (Ω)
- Factor 2π ≈ 6.283 (geometric configuration constant)

**Layer Resistivity Determination:**
- Single-layer interpretation: ρ ≈ average of all measurements
- Multi-layer interpretation: requires slope change analysis
- Abrupt changes > 30% indicate layer boundaries
- Gradual changes indicate transition zones

**Federal District Typical Results:**
- Surface: 800-1,200 Ω·m (urban areas); 1,500-2,000 Ω·m (rural)
- Subsurface (5-10 m): 1,200-1,600 Ω·m
- Deep (20+ m): 1,800-3,500 Ω·m (laterite/bedrock influence)

### G.1.7 Quality Assurance Procedures

**In-Field QA/QC:**
- Duplicate measurements at 10% of locations: must agree within 5%
- Reference electrode set measurement: document baseline
- Verify GPS coordinate accuracy by independent check
- Photograph electrode configuration and site
- Document weather and soil condition changes during testing

**Post-Test QA/QC:**
- Plot all data on log-log graph (depth vs. resistivity)
- Identify and document outliers (>25% deviation from trend)
- Perform Wenner-to-Schlumberger conversion if comparative analysis needed
- Generate site summary with resistivity profile diagram
- Review for internal consistency (physical reasonableness)

### G.1.8 Seasonal Testing Requirements

**Federal District Two-Season Protocol:**
1. **Wet Season Testing (November-February):**
   - Baseline measurement condition
   - Record as "reference" or "winter" condition
   - Typically 20-40% lower resistivity than dry season

2. **Dry Season Testing (May-August):**
   - Worst-case design condition
   - Record as "design condition" or "summer" condition
   - Use for grounding system design calculations
   - Document rainfall history (months since last significant rain)

**Annual Verification (Optional):**
- Re-test same locations annually to establish trend
- Maintain historical database showing seasonal and long-term variations
- Identify any permanent changes (construction impact, soil settlement)

---

## G.2 Grounding Resistance Measurement - Fall-of-Potential Method

### G.2.1 Equipment and Personnel

**Required Equipment:**
- Ground resistance tester (3 or 4-terminal): Fluke 1625-2, AEMC MRU-200
- Auxiliary current electrode (copper stake, typically 1 m length)
- Auxiliary potential electrode (copper spike, 0.5 m length)
- Connecting cables (3 insulated conductors, minimum 30 m length each)
- Measuring tape (minimum 100 m)
- GPS unit
- Data recording forms
- Safety equipment: hard hat, safety glasses, gloves, steel-toed boots

**Personnel:**
- Minimum two qualified personnel
- One designated as measurement technician
- One designated as safety officer
- Both trained in electrical hazard recognition

### G.2.2 Measurement Site Requirements

**Location Selection:**
- Test performed at main grounding electrode connection point
- Remote auxiliary electrodes positioned at distances significantly beyond SPDA influence zone
- Auxiliary current electrode: positioned at 90-120% of design rod length distance from test point
- Auxiliary potential electrode: positioned at 61.8% of distance between test point and current electrode

**Example for 3 m Rod Installation:**
- Test point: main SPDA connection
- Auxiliary current electrode (C): 4-5 m distant in one direction
- Auxiliary potential electrode (P): 2.5-3 m from test point, on line toward C electrode

### G.2.3 Measurement Procedure

**Step-by-Step Protocol:**

1. **Electrode Installation:**
   - Drive auxiliary current electrode (stake) to full depth, noting resistance
   - If resistance > 50 Ω, relocate to better soil (more conductive location)
   - Drive auxiliary potential electrode to full depth
   - Connect test leads from instrument terminals to grounding system

2. **Connection Verification:**
   - Connect main grounding electrode (ES) to ES terminal on tester
   - Connect auxiliary current electrode (AC) to AC terminal
   - Connect auxiliary potential electrode (P) to P terminal
   - Verify all connections secure; inspect for corrosion or poor contact
   - If building is energized, verify no dangerous voltages present before proceeding

3. **Instrument Configuration:**
   - Select Fall-of-Potential mode (if multi-function tester)
   - Set frequency to 1 kHz (standard)
   - Zero instrument per manufacturer protocol
   - If available, select "3-terminal" mode for most accurate results

4. **Measurement Acquisition:**
   - Activate measurement
   - Allow 5-10 seconds for signal stabilization
   - Record resistance value displayed
   - Perform second independent measurement
   - If readings within 5%, record average; otherwise investigate cause and repeat

5. **Data Recording:**
   - Record date, time (HHMM)
   - Record electrode configuration (distance, orientation)
   - Record resistance value (Ω) to 0.01 Ω precision
   - Record air temperature (±1°C)
   - Record soil condition (wet/moist/dry)
   - Record ambient conditions (recent rain, flooding, drought)
   - Record GPS location
   - Record personnel names and company
   - Document any equipment issues or concerns

### G.2.4 Measurement Configurations

**Fall-of-Potential (Primary Method):**
- Most accurate for typical grounding systems
- Typical measurement: 10-15% variation around 62% point (theoretical optimum)
- Repeat measurement at 68-70% and 55-60% positions to verify accuracy
- If all three readings within 10%, use average; otherwise investigate ground configuration

**Three-Point Method (Verification):**
1. Measure at standard 61.8% position
2. Measure at 50% position (halfway between test and current electrode)
3. Measure at 71% position (further from test point)
4. Plot readings; should form relatively flat curve near 62% point
5. If not flat, suspect multiple ground electrodes interfering or poor electrode contact

### G.2.5 Quality Assurance

**In-Field QA/QC:**
- Verify auxiliary electrode stability (retest after 30 seconds to confirm no creep)
- Perform reference measurement with known resistor (if testing equipment supports)
- Document weather and soil changes during testing period
- Photograph test setup and electrode positions
- Record GPS coordinates to ±5 m accuracy

**Post-Test QA/QC:**
- Compare to previous measurements (if available); document any significant changes
- Verify measurement consistency (repeated measurements should agree within 3%)
- Compare to theoretical calculation based on electrode geometry and soil resistivity
- Identify any outliers or suspicious results
- Generate summary report with acceptance decision (pass/fail per NBR 5419:3)

### G.2.6 Acceptance Criteria

**Target Grounding Resistance (Educational Buildings):**
- Goal: Rg < 10 Ω
- Acceptable: Rg 10-15 Ω (with documented treatment plan)
- Requires improvement: Rg > 15 Ω
- High resistivity sites: May achieve 10-20 Ω after optimization with chemical treatment

**Documentation Requirement:**
- All measurements recorded on standardized form with date, time, personnel, equipment
- Photograph of test setup and electrodes
- GPS coordinates and site map showing measurement location
- Weather and soil condition notes
- Any deviations from standard procedure documented and explained

---

## G.3 Continuity Testing - Down Conductors and Equipotential Bonding

### G.3.1 Equipment Requirements

**Essential Equipment:**
- Low-resistance ohmmeter (typically 200 mΩ or less range)
- Four-wire resistance tester preferred (eliminates lead resistance)
- Connecting leads (insulated, color-coded per standard)
- Alligator clips and spade lugs for secure connection
- Measuring tape
- Flashlight or work light
- Safety equipment (hard hat, gloves, glasses, footwear)

**Calibration:**
- Instrument must have ISO 17025 certification within 12 months
- Zero-ohm check performed before and after test sequence
- Reference resistor verification (if available)

### G.3.2 Down Conductor Continuity Testing

**Testing Points:**
- Roof-level air terminal connection to conductor
- At each floor level (exterior wall measurement at accessible point)
- At basement/foundation level before grounding electrode connection
- At each major corner or direction change
- Maximum 20 m spacing between test points

**Test Procedure:**

1. **Preparation:**
   - Ensure conductor is not energized (verify with volt-tester if electrically active circuit)
   - Clean connection points (remove paint, corrosion) if possible without damage
   - Use contact cleaner or sandpaper gently on test points
   - Allow 30 seconds for ohmmeter to stabilize after connection

2. **Measurement:**
   - Connect ohmmeter leads to two adjacent test points
   - Record resistance value (mΩ) at each segment
   - Acceptable: < 0.2 Ω per segment (< 200 mΩ)
   - Note any suspicious readings or discontinuities

3. **Interpretation:**
   - Total down conductor resistance should be < 1 Ω for entire length
   - Individual connections: < 0.2 Ω maximum acceptable
   - Discontinuities (> 5 Ω suddenly): indicate poor joint or corrosion
   - Gradual increase with distance: normal (copper resistivity effect)

**Documentation:**
- Record resistance value for each segment
- Identify location of each test point (floor level, coordinates)
- Note conductor material and diameter (if visible)
- Document any corrosion, damage, or discontinuities observed
- Photograph poor-condition connections
- Identify non-conformances requiring remediation

### G.3.3 Equipotential Bonding Continuity

**Bonding Points to Test:**
- Metal roof penetrations (pipes, HVAC ducts, etc.)
- Structural steel framework
- Building electrical grounding system connection
- Telecommunications infrastructure
- Water and gas service lines (where accessible)
- Interior metallic systems (raceways, cable trays)
- Floor reinforcement mesh (if conducting)

**Test Procedure:**

1. **Mapping:**
   - Create diagram showing all metallic elements
   - Identify bonding points between elements
   - Verify visual continuity of bonding conductors

2. **Resistance Measurement:**
   - Test between each metallic element and main SPDA ground reference
   - Acceptable: < 0.1 Ω (< 100 mΩ)
   - Test between metallic elements laterally (should be < 0.5 Ω)
   - Document all measurements on bonding diagram

3. **Non-Bonded Elements:**
   - Identify metallic items not bonded to SPDA system
   - Assess hazard: potential side-flashover risk during lightning event
   - Document status and recommend remediation if necessary

### G.3.4 Service Line Bonding Verification

**Power Line Bonding:**
- Test bonding conductor from SPDA to power service grounding
- Acceptable: < 0.5 Ω
- Verify bonding path is uninterrupted (no open switches)

**Telecommunications Bonding:**
- Test bonding from cable shield/outer conductor to SPDA ground
- Acceptable: < 1 Ω (higher tolerance due to signal considerations)
- Verify bonding at service entrance and main distribution point

**Data/Network Bonding:**
- Test grounding path for data line shields
- Acceptable: < 0.5 Ω
- Verify no RF loops created by dual bonding paths (isolation may be required)

---

## G.4 Surge Protective Device (SPD) Testing

### G.4.1 In-Service SPD Verification

**Non-Destructive Testing (Performed on Installed Devices):**

1. **Visual Inspection:**
   - Check for physical damage, corrosion, discoloration
   - Verify proper installation per design (correct circuit position)
   - Confirm voltage markings match circuit voltage
   - Check for signs of overstress (burnt appearance, bulging)

2. **Continuity Verification:**
   - Verify conduction path exists between phase and ground
   - Acceptable: conductive path for Type 1 (spark gap); 0.1-10 MΩ for Type 2 (MOV)
   - Discontinuity indicates device failure or corruption

3. **Leakage Current Measurement (Type 2 SPD):**
   - Measure current from phase to ground at rated voltage (if safe)
   - Acceptable: < 1 mA for new devices; < 3 mA for end-of-life
   - Excessive leakage indicates degradation or failure

4. **Insulation Resistance (High-Voltage Test):**
   - Perform megohm measurement (typically 500V or 1000V test)
   - Acceptable: > 100 MΩ from line to ground
   - Low insulation resistance indicates moisture ingress or contamination

### G.4.2 SPD Surge Testing (Destructive Testing)

**Standard Test Waveforms (Per IEC 61643-1):**

**Type 1 SPD Test:**
- 10/350 μs impulse current waveform
- Test current: 10-12.5 kA
- Multiple impulses: 5-10 shots per test
- Monitor voltage protection level and energy absorption
- Record peak voltage and energy dissipated

**Type 2 SPD Test:**
- 8/20 μs impulse current waveform
- Test current: 20 kA (nominal)
- Combined wave test: 1.2/50 μs + 8/20 μs simulating realistic surge
- Verify voltage protection level < specification
- Confirm no thermal runaway or component failure

**Type 3 SPD Test:**
- 8/20 μs impulse current: 5-10 kA
- Limited energy testing
- Verify proper component function
- Check for isolation and coordination with upstream protection

### G.4.3 SPD End-of-Life Criteria

**Visual Indicators of Degradation:**
- Discoloration or darkening of components
- Cracking or bulging of ceramic elements
- Corrosion of terminals or connections
- Burning or melting of internal components
- Moisture or discoloration inside transparent housing

**Performance Degradation Indicators:**
- Leakage current increase: > 50% of new device value
- Voltage protection level increase: > 20% above specification
- Insulation resistance decrease: < 10 MΩ
- Operational temperature rise: > 50°C above ambient

**Replacement Trigger:**
- Device reaches 10-15 year operational age (typical SPD lifespan)
- Documented surge event occurrence (even if no visible damage)
- Leakage current exceeds safe operating limits
- Performance degradation exceeds 20% from original specification
- Evidence of prior surge event (scorching, component discoloration)

---

## G.5 Data Management and Documentation

### G.5.1 Standardized Data Recording Forms

**Soil Resistivity Testing Form:**
```
SOIL RESISTIVITY MEASUREMENT RECORD
Project: ___________________________  Date: _______________
Location: _________________________  Site Manager: ________
Weather: _________________________ Soil Condition: _______
Equipment: ________________________ Serial #: _____________
Calibration Date: ________________

Traverse Direction: ____________ (Cardinal Direction)
| Distance (m) | R measured (Ω) | ρ = 2πaR (Ω·m) | Notes |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

Traverse Average ρ: ________________ Ω·m
GPS Coordinates: Lat __________ Long __________
```

**Grounding Resistance Testing Form:**
```
GROUNDING RESISTANCE MEASUREMENT RECORD
Project: ___________________________  Date: _______________
Location: _________________________  Test Time: _________
Equipment: ________________________ Calibration Date: ____
Technician: _____________________ QA/QC By: ___________

Electrode Configuration:
- Test Point Location: _________________________
- Auxiliary Current (AC) Distance: ____________ m
- Auxiliary Potential (P) Distance: __________ m

Measurements:
| Attempt | Resistance (Ω) | Temperature (°C) | Notes |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 (if needed) | | | |

Final Result: _________________ Ω
PASS / FAIL [Target: < 10 Ω for educational buildings]
Acceptance Status: ______________________
```

### G.5.2 Data Analysis and Reporting

**Report Structure:**
1. Executive Summary (results and status)
2. Test Location Map (GPS coordinates, site photo)
3. Detailed Test Results (all measurements, calculations)
4. Comparison to Standards (acceptability assessment)
5. Recommendations (if improvements needed)
6. Appendices (raw data forms, photos, certificates)

**Archival Requirements:**
- Store original forms in secure location (5-year minimum retention)
- Maintain digital copies with metadata (test date, location, personnel)
- Link to maintenance records and repair history
- Create trend analysis plots (5+ year historical data if available)

---

