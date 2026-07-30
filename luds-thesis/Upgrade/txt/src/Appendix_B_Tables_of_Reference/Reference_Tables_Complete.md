# REFERENCE TABLES FOR LIGHTNING PROTECTION SYSTEMS THESIS

## Table 1: Protection Level Parameters according to NBR 5419:2015

| Parameter                                         | Level I                                         | Level II                                       | Level III                                     | Level IV                         |
|:--------------------------------------------------|:------------------------------------------------|:-----------------------------------------------|:----------------------------------------------|:---------------------------------|
| Peak Current (kA)                                 | 200                                             | 150                                            | 100                                           | 100                              |
| Striking Distance rs (m)                          | 316                                             | 269                                            | 216                                           | 216                              |
| Rolling Sphere Radius (m)                         | 20                                              | 30                                             | 45                                            | 60                               |
| Mesh Dimension (m)                                | 5×5                                             | 10×10                                          | 15×15                                         | 20×20                            |
| Down Conductor Spacing (m)                        | 10                                              | 15                                             | 20                                            | 25                               |
| Protection Angle (°)                              | 25-30                                           | 35-45                                          | 45-55                                         | 55-60                            |
| Max Mesh Height Above Structure (m)               | 5                                               | 7.5                                            | 10                                            | 15                               |
| Standard Test Current (10/350 μs) kA              | 200                                             | 150                                            | 100                                           | 100                              |
| Subsequent Stroke (0.25/100 μs) kA                | 50                                              | 37.5                                           | 25                                            | 25                               |
| Charge per Event (C)                              | 300-400                                         | 225-300                                        | 150-200                                       | 150-200                          |
| Typical Application                               | Strategic facilities, monuments, power stations | Government buildings, hospitals, fire stations | Educational buildings, commercial, industrial | Rural structures, farm buildings |
| Annual Lightning Frequency / Building (events/yr) | 0.1-0.5                                         | 0.05-0.2                                       | 0.02-0.1                                      | 0.01-0.05                        |
| Risk Category                                     | Very High                                       | High                                           | Normal                                        | Low                              |

### Table 1 Notes:
- Peak current values represent the 50% probability level from CIGRE research
- Striking distance calculated from rs = 10 × I^0.65 formula
- Rolling sphere radii define the protected volume below each level
- Mesh dimensions represent maximum conductor spacing requirements
- Protection angles apply to simplified structures without multiple features
- Standard test currents follow IEC 62305 impulse definitions
- Typical annual frequencies represent expected direct strike events based on Brazilian lightning density data
- Risk categories reflect probability and consequence of events

## Table 2: Mesh Dimensions and Down Conductor Spacing Requirements

| Requirement                             | Level I   | Level II   | Level III   | Level IV     |
|:----------------------------------------|:----------|:-----------|:------------|:-------------|
| Maximum Mesh Dimension (m)              | 5         | 10         | 15          | 20           |
| Mesh Conductor Minimum Diameter (mm)    | 10-12     | 8-10       | 6-8         | 6-8          |
| Down Conductor Spacing Max (m)          | 10        | 15         | 20          | 25           |
| Distance Between Roof Terminals (m)     | 5-8       | 8-12       | 12-15       | 15-20        |
| Vertical Conductor Spacing (m)          | 5-8       | 8-12       | 12-15       | 15-20        |
| Horizontal Loop Spacing (m)             | 5         | 10         | 15          | 20           |
| Corner Terminal Spacing (m)             | 3-5       | 5-8        | 8-10        | 10-12        |
| Field Connection Points per 50 m (min)  | 2-3       | 1-2        | 1           | 1 (optional) |
| Horizontal Conductor Min Section (mm²)  | 50-70     | 40-50      | 35-40       | 35-40        |
| Vertical Conductor Min Section (mm²)    | 70-100    | 50-70      | 40-50       | 40-50        |
| External Bonding Points Max Spacing (m) | 5         | 10         | 15          | 20           |

### Table 2 Notes:
- All dimensions measured in meters (m) except conductor diameter in millimeters (mm)
- Maximum mesh dimension represents the largest cell that maintains protection level effectiveness
- Conductor diameter influences current distribution and corrosion resistance
- Down conductor spacing affects both protection coverage and system cost
- Distance between roof terminals influenced by roof structure size and material
- Vertical conductor spacing represents both external conductors and internal bonding requirements
- Horizontal loop spacing for upper building levels ensures complete perimeter protection
- Field connection points ensure proper current distribution in large mesh systems
- Conductor cross-sections refer to electrical area for current-carrying capacity
- External bonding points maintain equipotential surfaces critical for electromagnetic compatibility

## Table 3: Risk Component Factors for Different Structure Types

| Risk Component                         | Educational Building   | Hospital/Critical   | Residential   |   Historical/Monument | Industrial/Factory   |
|:---------------------------------------|:-----------------------|:--------------------|:--------------|----------------------:|:---------------------|
| RA: Direct strike - structural damage  | 0.0023                 | 0.0008              | 0.0005        |                0.0015 | 0.0050               |
| RB: Direct strike - fire initiation    | 0.0028                 | 0.0005              | 0.0008        |                0.001  | 0.0150               |
| RC: Direct strike - electronic failure | 0.0345                 | 0.0100              | 0.0050        |                0.02   | 0.0800               |
| RM: Near strike - LEMP effects         | 0.0360                 | 0.0200              | 0.0150        |                0.01   | 0.1200               |
| RU: Service line - structural damage   | 0.0030                 | 0.0010              | 0.0005        |                0.0008 | 0.0100               |
| RV: Service line - fire initiation     | 0.0030                 | 0.0008              | 0.0005        |                0.001  | 0.0200               |
| RW: Service line - electronic failure  | 0.0180                 | 0.0050              | 0.0025        |                0.005  | 0.0500               |
| RZ: Service line - LEMP effects        | 0.0100                 | 0.0030              | 0.0015        |                0.002  | 0.0300               |
| Total R1 (Human Life Loss)             | 0.0966                 | 0.0211              | 0.0163        |                0.0113 | 0.2300               |
| Total R2 (Public Service Loss)         | 0.0150                 | 0.0500              | 0.0050        |                0.008  | 0.1000               |
| Total R3 (Cultural Heritage)           | N/A                    | N/A                 | N/A           |                0.08   | N/A                  |
| Total R4 (Economic Loss)               | 0.1200                 | 0.0800              | 0.0300        |                0.15   | 0.5000               |

### Table 3 Notes:
- All risk components follow the formula: Rx = Nx × Px × Lx (frequency × probability × loss)
- Risk values represent annual probability (dimensionless, ranging 0-1)
- Tolerable risk limits per NBR 5419:2015 Part 2:
  - R1 (Loss of Human Life): RT = 10⁻⁵ (0.00001)
  - R2 (Loss of Public Service): RT = 10⁻³ (0.001)
  - R3 (Cultural Heritage): RT = 10⁻⁴ (0.0001)
  - R4 (Economic Loss): No absolute limit, but cost-benefit evaluated
- Educational buildings typical for Brazilian universities and law schools
- Hospital/Critical includes trauma centers, intensive care facilities, surgery suites
- Historical/Monument applies to registered cultural heritage structures
- Industrial/Factory represents high-risk manufacturing with explosive or combustible materials
- N/A indicates component not applicable to that structure type
- Values assume no protection measures; actual risk reduced significantly by implemented SPDA and SPD systems
- Component RA and RB address direct lightning strikes to structure
- Component RM, RU, RV, RW, RZ address both direct strikes and near-strike electromagnetic effects
- Total R values represent sum of all relevant components for human life loss risk (R1)

## Table 4: SPD Classification and Test Parameters

| Parameter                       | Type 1                       | Type 2                             | Type 3                     |
|:--------------------------------|:-----------------------------|:-----------------------------------|:---------------------------|
| Installation Location           | Service entrance, main panel | Load side of disconnects, panels   | Outlet and equipment level |
| Rated Current In (A)            | 12.5k-100k                   | 20k-40k                            | 5k-20k                     |
| Test Current (8/20 μs)          | Direct connect               | 8/20 μs, 20 kA                     | 8/20 μs, 10 kA             |
| Impulse Current (10/350 μs)     | 10/350 μs, 10-12.5 kA        | 10/350 μs capable                  | Limited capability         |
| Combined Wave Test              | 1.2/50 μs (6 kV), 8/20 μs    | 1.2/50 μs (6 kV), 8/20 μs          | Basic                      |
| Operating Voltage UC (V)        | 230/400V 3-phase             | 230/400V, 1-3 phase                | 230/400V, single phase     |
| Voltage Protection Level Up (V) | 2-4                          | 1.5-2.5                            | 0.8-1.5                    |
| Response Time (ns)              | <50                          | <200                               | <500                       |
| Energy Absorption (kJ)          | 2.5-10                       | 1-5                                | 0.5-2                      |
| Max Temperature Rise (°C)       | 50-80                        | 40-60                              | 30-50                      |
| Primary Application             | Building main protection     | Secondary protection, distribution | Final protection at load   |
| Connection Method               | Connected to SPD circuits    | Panelboard mounted                 | Close to equipment         |
| Coordination Type               | Type 1 only                  | Type 1+Type 2                      | Type 2+Type 3              |
| Cost Range (USD)                | 1,500-5,000                  | 500-2,000                          | 100-500                    |
| Typical Lifespan (years)        | 10-15                        | 15-20                              | 10-15                      |

### Table 4 Notes:
- Type 1: Spark gap based, installed at service entrance between transformer secondary and building disconnect
- Type 2: Varistor-based (MOV), installed at load-side of main disconnect, typically in main panel
- Type 3: Combined spark gap and varistor, installed at outlet and equipment level protection
- Test currents follow IEC 61643-1 standards for SPD performance verification
- Combined wave test simulates actual lightning surge with both fast rise and energy components
- Voltage protection level (Up) represents maximum voltage clamped by SPD during surge event
- Response time critical for Type 1; slower response (>50 ns) still adequate given circuit inductance
- Energy absorption capacity determines device lifespan and replacement intervals
- Max temperature rise must not exceed insulation rating (typically 200°C)
- Type 1 and Type 2 coordination requires specific distance or coordinating devices to prevent nuisance trips
- Type coordination (cascading stages) reduces voltage stress on downstream equipment
- Modern Type 2 devices incorporate remote status indication via dry contacts or communication interface
- Lifespan estimates assume average 2-4 lightning events per year within protection zone

## Table 5: Minimum Conductor Cross-Sections by Material

| Application                      | Copper (mm²)   | Aluminum (mm²)   | Steel Galvanized (mm²)   | Steel Stainless 316 (mm²)   | Typical Diameter (mm)   |
|:---------------------------------|:---------------|:-----------------|:-------------------------|:----------------------------|:------------------------|
| Main Down Conductor (Level I)    | 70-100         | 120-150          | 150-200                  | 100-120                     | 10-12                   |
| Main Down Conductor (Level II)   | 50-70          | 85-100           | 100-150                  | 70-85                       | 8-10                    |
| Main Down Conductor (Level III)  | 40-50          | 70-85            | 85-100                   | 50-70                       | 7-8                     |
| Main Down Conductor (Level IV)   | 35-40          | 60-70            | 70-85                    | 40-50                       | 6-7                     |
| Mesh Conductor (Level I)         | 50-70          | 85-100           | 100-150                  | 70-85                       | 8-10                    |
| Mesh Conductor (Level II)        | 35-50          | 60-85            | 70-100                   | 50-70                       | 6-8                     |
| Mesh Conductor (Level III)       | 25-35          | 50-70            | 50-85                    | 40-50                       | 5-6                     |
| Mesh Conductor (Level IV)        | 25-35          | 50-70            | 50-85                    | 35-50                       | 5-6                     |
| Grounding Electrode (All levels) | 50-70          | 85-100           | 100-150                  | 70-85                       | 8-10                    |
| Bonding Strap (Equipotential)    | 16-25          | 25-35            | 40-50                    | 20-25                       | 4-5                     |
| Service Line Protection          | 25-35          | 50-70            | 70-100                   | 50-70                       | 5-6                     |
| TV/Communication Lines           | 10-16          | 16-25            | 25-50                    | 10-16                       | 3-4                     |

### Table 5 Notes:
- Cross-section values specified in square millimeters (mm²) for electrical conductivity
- Copper: Highest conductivity (58.5 × 10⁶ S/m), best choice but most expensive
- Aluminum: Lower conductivity (37.7 × 10⁶ S/m), requires ~40% larger cross-section than copper
- Steel Galvanized: Much lower conductivity (8.6 × 10⁶ S/m), requires ~2-3× copper area but lower cost
- Stainless Steel 316: Moderate conductivity (1.1 × 10⁶ S/m), excellent corrosion resistance but requires largest cross-section
- Minimum sections based on thermal capacity to withstand 10/350 μs lightning current without melting
- Melting point thresholds: Cu 1,083°C, Al 660°C, Steel 1,538°C determine thermal limits
- Down conductors must accommodate 100% of maximum current; mesh conductors carry distributed current
- Grounding electrodes specified for insertion into soil without physical support
- Bonding straps connect equipment frames and metal structures to main SPDA ground plane
- Service line protection includes power, data (copper pairs), fiber optic sheath
- TV/Communication lines minimize conductor mass while maintaining function
- Typical diameter conversions: 35 mm² ≈ 6.6 mm round; 50 mm² ≈ 8 mm round; 70 mm² ≈ 9.4 mm round
- Stranded conductors preferred over solid for flexibility in routing and mechanical vibration resistance

## Table 6: Soil Resistivity Values for Brasília Federal District

| Location/Zone                        | Resistivity ρ (Ω⋅m)   | Seasonal Variation (%)   | Depth Range (m)   | Recommended Testing Spacing (m)   | Treatment Needed   | Ground Rod Quantity (3m rods)   |
|:-------------------------------------|:----------------------|:-------------------------|:------------------|:----------------------------------|:-------------------|:--------------------------------|
| Central Business District (Downtown) | 800-1,200             | ±20                      | 0-5               | 3, 6                              | Moderate           | 3-4                             |
| Lake Paranoá Region                  | 1,200-1,800           | ±25                      | 0-8               | 5, 10                             | Moderate           | 4-5                             |
| North/South Sectors (Residential)    | 1,000-1,500           | ±20                      | 0-6               | 3, 6, 10                          | Moderate           | 3-4                             |
| Agricultural Areas (Periphery)       | 1,500-2,500           | ±30                      | 0-10              | 5, 10, 20                         | Yes (High ρ)       | 6-8                             |
| Plateau Edge (High Elevation)        | 2,000-3,500           | ±35                      | 0-15              | 10, 20                            | Yes (Very High ρ)  | 8-12                            |
| Valley Areas (Low Elevation)         | 900-1,400             | ±28                      | 0-5               | 3, 6                              | Minor              | 2-3                             |
| Areas with Red Soil (Terra Roxa)     | 600-1,000             | ±15                      | 0-3               | 3, 5                              | No                 | 2-3                             |
| Areas with Laterite (Iron Rich)      | 1,800-3,000           | ±25                      | 0-8               | 5, 10, 20                         | Yes                | 5-7                             |
| Areas with Clay (Expandable)         | 1,200-2,200           | ±40                      | 0-6               | 5, 10                             | Moderate           | 4-6                             |
| Recent Development (Disturbed)       | 1,400-2,100           | ±25                      | 0-5               | 3, 6, 10                          | Moderate           | 4-5                             |
| Forest/Vegetation Areas              | 1,100-1,800           | ±22                      | 0-8               | 5, 10                             | Minor              | 3-4                             |
| Average Federal District (Overall)   | 1,200-1,600           | ±25                      | 0-10              | 5, 10, 20                         | Frequently         | 4-6                             |

### Table 6 Notes:
- Resistivity values measured in ohm-meters (Ω⋅m) reflect subsurface electrical properties
- Lake Paranoá Region: Moisture from nearby lake significantly reduces resistivity
- Central Business District: Disturbed soil and underground infrastructure affects measurements
- Plateau Edge: High elevation and thin soil layer increase resistivity; bedrock proximity significant
- Agricultural Areas: Natural soil composition with minimal disturbance; high variability
- Red Soil (Terra Roxa): Iron oxide rich, relatively low resistivity, common in Central Brazil
- Laterite (Iron Rich): Weathered iron-rich layer, extremely high resistivity when dry, lower when wet
- Clay (Expandable): Seasonal expansion/contraction; very high seasonal variation (±40%)
- Seasonal variation critical: measurements in dry season (May-September) vs. wet season (October-April) may differ by 30-50%
- Measurements taken at 5, 10, 20 meter electrode spacings to determine resistivity profile with depth
- Treatment methods for high ρ sites: buried conductors in low-resistivity fill, bentonite clay conditioning, conductive cement
- Federal District average 1,200-1,600 Ω⋅m represents challenging environment requiring enhanced grounding
- Ground rod quantities estimated for achieving target 10 Ω resistance (educational buildings)
- Multiple rods spaced at 2-3× rod length reduces utilization factor; spacing optimization critical

## Table 7: Grounding Resistance Targets for Different Applications

| Application Type                   | Target Rg (Ω)   | Maximum Acceptable (Ω)   | Verification Method   | Testing Frequency   | Re-testing After       | NBR 5419 Part   |
|:-----------------------------------|:----------------|:-------------------------|:----------------------|:--------------------|:-----------------------|:----------------|
| Hospitals/Life Safety              | <5              | 5-10                     | Fall-of-Potential     | Annual              | Structural changes     | Part 3, 4       |
| Data Centers/IT Facilities         | <10             | 10-20                    | Fall-of-Potential     | Annual              | Severe weather         | Part 3, 4       |
| Educational Buildings (Law School) | <10             | 10-15                    | Stakeless (Clamp)     | Bi-annual           | Major SPDA work        | Part 3, 4       |
| Public Administration (Government) | <5              | 5-10                     | Fall-of-Potential     | Annual              | Infrastructure upgrade | Part 3, 4       |
| Industrial Manufacturing           | <5              | 5-10                     | Fall-of-Potential     | Annual              | Storm damage           | Part 3, 4       |
| Telecommunications Facilities      | <5              | 5-10                     | Clamp/Continuity      | Semi-annual         | System modification    | Part 3, 4       |
| Airport/Air Traffic Control        | <3              | 3-5                      | Fall-of-Potential     | Annual              | Environmental work     | Part 3, 4       |
| Fire Stations/Emergency            | <5              | 5-10                     | Fall-of-Potential     | Annual              | Strike event           | Part 3, 4       |
| Commercial/Office Buildings        | <10             | 15-20                    | Stakeless             | Every 2 years       | Major renovation       | Part 3, 4       |
| Residential/Apartment              | <20             | 25-30                    | Continuity Check      | Every 3 years       | Lightning strike       | Part 3          |
| Historic Monuments                 | <5              | 5-10                     | Fall-of-Potential     | Annual              | Any modification       | Part 3, 4       |
| Power Substations                  | <1              | 1-2                      | Fall-of-Potential     | Semi-annual         | Maintenance work       | IEC 62305       |
| Petrol/Chemical Storage            | <1              | 1-2                      | Fall-of-Potential     | Quarterly           | Upgrades               | Part 3, 4       |

### Table 7 Notes:
- Rg targets represent practical goals based on risk assessment and service requirements
- Life safety applications (hospitals, fire stations) require <5 Ω for rapid fault clearing
- IT/Data centers require <10 Ω for equipment protection during transient events
- Fall-of-Potential method: driven stake method measuring potential drop between electrodes
- Stakeless/Clamp method: non-invasive measurement using clamp on conductor, less accurate but no site disturbance
- Annual verification recommended per IEEE Std 81 and NBR 5419:3
- Re-testing triggered by: severe storm events, nearby lightning strikes, ground modifications, or structure changes
- Historic monuments often challenging due to architectural limitations on ground conductor routing
- Power substations and chemical storage require specialized low-impedance grounding (<1 Ω) for equipment protection
- Verification method selection depends on site accessibility, soil conditions, and measurement accuracy requirements
- Equipment used: Fluke 1625-2, AEMC MRU-200, megohm meter with specialized accessories
- Seasonal variations require testing at same time annually for trend analysis

## Table 8: Cost-Benefit Analysis of Protection Measures

| Protection Measure                    | Initial Cost (R$)   | Annual Maintenance (R$)   | Equipment Replacement (25yr, R$)   | Avoided Damage Value (Annual, R$)   |   Risk Reduction Factor | 25-Year NPV (r=8%)(R$)   | Payback Period (years)   | Protection Level Achieved   | Recommended For        |
|:--------------------------------------|:--------------------|:--------------------------|:-----------------------------------|:------------------------------------|------------------------:|:-------------------------|:-------------------------|:----------------------------|:-----------------------|
| External SPDA (Level III)             | 180,000             | 3,000                     | 30,000                             | 28,000                              |                    0.9  | 185,000                  | 6.4                      | III                         | Educational buildings  |
| External SPDA (Level II)              | 250,000             | 3,500                     | 35,000                             | 35,000                              |                    0.95 | 355,000                  | 7.1                      | II                          | Hospitals, Critical    |
| External SPDA (Level I)               | 350,000             | 4,000                     | 40,000                             | 45,000                              |                    0.98 | 625,000                  | 7.8                      | I                           | Strategic facilities   |
| Type 1 SPD Installation               | 45,000              | 2,000                     | 45,000                             | 12,000                              |                    0.7  | -95,000                  | >25                      | Basic                       | Basic protection       |
| Type 1 + Type 2 SPD System            | 95,000              | 3,000                     | 70,000                             | 22,000                              |                    0.85 | 185,000                  | 4.3                      | Moderate                    | Office buildings       |
| Complete SPD Cascade (3-Stage)        | 150,000             | 4,500                     | 120,000                            | 35,000                              |                    0.95 | 520,000                  | 4.3                      | High                        | Data centers           |
| Grounding Upgrade (8 rods, 30m rings) | 65,000              | 1,500                     | 15,000                             | 5,000                               |                    0.4  | -155,000                 | >25                      | Low                         | High resistivity areas |
| Soil Resistivity Treatment (2,000 m²) | 85,000              | 500                       | 20,000                             | 2,000                               |                    0.2  | -185,000                 | >25                      | Low                         | Clay/wetland areas     |
| Structural Bonding & Equipotential    | 55,000              | 1,000                     | 10,000                             | 8,000                               |                    0.5  | -85,000                  | >25                      | Moderate                    | All structures         |
| LPZ Implementation (Full)             | 200,000             | 5,000                     | 80,000                             | 40,000                              |                    0.98 | 450,000                  | 5.0                      | Very High                   | High-risk areas        |
| Smart Monitoring System               | 120,000             | 2,500                     | 180,000                            | 15,000                              |                    0.6  | 95,000                   | 8.0                      | Moderate                    | Critical facilities    |
| Combination: SPDA + SPD + Monitoring  | 900,000             | 15,000                    | 400,000                            | 80,000                              |                    0.99 | 920,000                  | 11.3                     | Very High                   | Premium protection     |

### Table 8 Notes:

**Cost Methodology:**
- Initial costs: Material, labor, and design for complete installation
- Annual maintenance: Inspection, minor repairs, vegetation management
- Equipment replacement: Planned obsolescence or storm damage replacement
- 25-year analysis horizon typical for building infrastructure investment
- All values in Brazilian Real (R$); international comparisons require exchange rate conversion

**Economic Indicators:**
- NPV (Net Present Value) calculated at 8% real discount rate over 25 years
- Positive NPV indicates investment returns exceed cost; justifies spending from economic perspective
- Payback period represents years until cumulative benefits equal initial investment
- Avoided damage values estimated from insurance industry data and historical loss statistics

**Risk Reduction Factors:**
- Dimensionless value from 0 (no protection) to 1 (complete elimination)
- Actual risk reduction depends on proper maintenance and periodic inspection
- Multiple measures applied together show synergistic effects (not simple addition)

**Recommendations:**
- Combinations provide superior protection at lower per-unit cost than single measures
- Monitoring systems justify cost through early detection of degradation
- Complete systems for critical facilities despite longer payback period
- Phased implementation possible: external protection first, then internal SPD coordination
- Government buildings and hospitals often prioritize life safety over economic payback

**Federal District Context:**
- High soil resistivity (1,200-1,600 Ω⋅m) increases grounding upgrade costs
- Lightning density 6 flashes/km²/year justifies investment in higher protection levels
- Educational buildings subject to NBR 5419:2015 compliance requirements
- Insurance requirements often mandate specific protection measures
- Climate change projections (+12%/°C temperature) suggest increasing future lightning frequency

**Long-term Considerations:**
- SPD technology advancing rapidly; devices from 10+ years ago may lack modern coordination features
- Modular design allows phased upgrades without complete system replacement
- Remote monitoring enables predictive maintenance and reduced emergency response costs
- Documented compliance and maintenance records enhance property value and insurance ratings
