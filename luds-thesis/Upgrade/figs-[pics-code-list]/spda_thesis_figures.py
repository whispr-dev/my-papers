#!/usr/bin/env python3
"""
Technical Figures for Doctoral Thesis on Lightning Protection Systems (SPDA)
According to ABNT NBR 5419:2015 Standard
Author: Ludmilla Pereira Hillerman
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Polygon, Rectangle
from matplotlib.collections import PatchCollection
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D
import warnings
warnings.filterwarnings('ignore')

# Set academic publication parameters
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['lines.linewidth'] = 1.5

def figure_1_rolling_sphere_method():
    """
    Fig. 1: Rolling Sphere Method for Protection Level Determination
    According to NBR 5419:2015 Part 3
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left subplot - Rolling sphere concept
    ax1.set_xlim(-60, 60)
    ax1.set_ylim(0, 80)
    ax1.set_aspect('equal')
    
    # Building structure
    building_width = 30
    building_height = 40
    building = Rectangle((-building_width/2, 0), building_width, building_height, 
                         fill=False, edgecolor='black', linewidth=2)
    ax1.add_patch(building)
    
    # Rolling spheres for different protection levels
    sphere_radii = {'I': 20, 'II': 30, 'III': 45, 'IV': 60}
    colors = {'I': 'red', 'II': 'orange', 'III': 'yellow', 'IV': 'green'}
    
    for level, radius in sphere_radii.items():
        # Calculate sphere position
        y_center = building_height + radius
        sphere = Circle((0, y_center), radius, fill=False, 
                       edgecolor=colors[level], linestyle='--', linewidth=1.5)
        ax1.add_patch(sphere)
        ax1.text(radius + 5, y_center, f'Level {level}\nr={radius}m', 
                fontsize=9, ha='left')
    
    ax1.set_xlabel('Horizontal Distance (m)')
    ax1.set_ylabel('Height (m)')
    ax1.set_title('(a) Rolling Sphere Radii by Protection Level')
    ax1.grid(True, alpha=0.3)
    
    # Right subplot - Protection angle variation with height
    ax2.set_xlim(0, 70)
    ax2.set_ylim(0, 90)
    
    heights = np.array([2, 5, 10, 20, 30, 45, 60])
    angles_I = np.array([79, 75, 70, 55, 45, 35, 25])
    angles_II = np.array([80, 77, 72, 60, 50, 40, 30])
    angles_III = np.array([81, 79, 74, 65, 55, 45, 35])
    angles_IV = np.array([82, 80, 76, 70, 60, 50, 40])
    
    ax2.plot(heights, angles_I, 'r-', marker='o', label='Level I', markersize=4)
    ax2.plot(heights, angles_II, 'orange', marker='s', label='Level II', markersize=4)
    ax2.plot(heights, angles_III, 'y-', marker='^', label='Level III', markersize=4)
    ax2.plot(heights, angles_IV, 'g-', marker='d', label='Level IV', markersize=4)
    
    ax2.set_xlabel('Height h (m)')
    ax2.set_ylabel('Protection Angle α (degrees)')
    ax2.set_title('(b) Protection Angle vs Height (NBR 5419:2015)')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    
    plt.suptitle('Figure 1: Rolling Sphere Method and Protection Angles per NBR 5419:2015', 
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/home/claude/fig1_rolling_sphere_method.png', dpi=300)
    plt.show()
    return fig

def figure_2_mesh_conductor_spacing():
    """
    Fig. 2: Mesh Conductor (Faraday Cage) Spacing Requirements
    According to NBR 5419:2015 Table 2
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # Define mesh spacings for different protection levels
    mesh_data = {
        'I': {'spacing': 5, 'color': 'red'},
        'II': {'spacing': 10, 'color': 'orange'},
        'III': {'spacing': 15, 'color': 'yellow'},
        'IV': {'spacing': 20, 'color': 'green'}
    }
    
    # Building outline
    building_width = 40
    building_height = 30
    ax.set_xlim(-5, building_width + 5)
    ax.set_ylim(-5, building_height + 5)
    ax.set_aspect('equal')
    
    # Draw building
    building = Rectangle((0, 0), building_width, building_height, 
                         fill=False, edgecolor='black', linewidth=3)
    ax.add_patch(building)
    
    # Draw mesh patterns for each protection level
    y_offset = 0
    section_height = building_height / 4
    
    for level, data in mesh_data.items():
        spacing = data['spacing']
        color = data['color']
        
        # Horizontal conductors
        y_positions = np.arange(y_offset, y_offset + section_height, spacing/2)
        for y in y_positions:
            if y <= y_offset + section_height:
                ax.plot([0, building_width], [y, y], color=color, linewidth=1, alpha=0.7)
        
        # Vertical conductors
        x_positions = np.arange(0, building_width + 1, spacing)
        for x in x_positions:
            ax.plot([x, x], [y_offset, y_offset + section_height], 
                   color=color, linewidth=1, alpha=0.7)
        
        # Label
        ax.text(building_width + 2, y_offset + section_height/2, 
               f'Level {level}\n{spacing}×{spacing}m', 
               fontsize=10, va='center')
        
        y_offset += section_height
    
    # Add down conductors
    down_conductor_spacing = 10  # meters
    x_positions = np.arange(0, building_width + 1, down_conductor_spacing)
    for x in x_positions:
        ax.plot([x, x], [0, -3], 'k-', linewidth=2)
        ax.plot([x-1, x+1], [-3, -3], 'k-', linewidth=2)  # Ground connection
    
    ax.set_xlabel('Horizontal Distance (m)')
    ax.set_ylabel('Vertical Distance (m)')
    ax.set_title('Figure 2: Mesh Conductor Spacing Requirements per Protection Level\n(NBR 5419:2015, Table 2)', 
                fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.text(building_width/2, -4.5, 'Down Conductors at 10m Spacing', 
           ha='center', fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('/home/claude/fig2_mesh_conductor_spacing.png', dpi=300)
    plt.show()
    return fig

def figure_3_risk_assessment_flowchart():
    """
    Fig. 3: Risk Management Methodology Flowchart
    According to NBR 5419:2015 Part 2
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Define box properties
    box_props = dict(boxstyle="round,pad=0.3", facecolor="lightblue", 
                    edgecolor="black", linewidth=1.5)
    decision_props = dict(boxstyle="round,pad=0.3", facecolor="lightyellow", 
                         edgecolor="black", linewidth=1.5)
    action_props = dict(boxstyle="round,pad=0.3", facecolor="lightgreen", 
                       edgecolor="black", linewidth=1.5)
    
    # Process boxes
    boxes = [
        (5, 13, "Structure Identification\nand Characterization", box_props),
        (5, 11.5, "Identification of Loss Types\nL1: Loss of human life\nL2: Loss of service\nL3: Loss of cultural heritage\nL4: Economic loss", box_props),
        (5, 9.5, "Risk Components Calculation\nRA, RB, RC, RM, RU, RV, RW, RZ", box_props),
        (5, 7.5, "Total Risk Calculation\nR = ΣRx", box_props),
        (5, 5.5, "R ≤ RT?", decision_props),
        (2, 3.5, "Structure\nProtected", action_props),
        (8, 3.5, "Select and Implement\nProtection Measures", action_props),
        (5, 1.5, "Recalculate Risk\nwith SPMs", box_props),
    ]
    
    for x, y, text, props in boxes:
        ax.text(x, y, text, bbox=props, ha='center', va='center', fontsize=10)
    
    # Arrows
    arrow_props = dict(arrowstyle='->', connectionstyle='arc3', 
                      color='black', lw=1.5)
    
    # Vertical arrows
    ax.annotate('', xy=(5, 11), xytext=(5, 12),
               arrowprops=arrow_props)
    ax.annotate('', xy=(5, 9), xytext=(5, 10),
               arrowprops=arrow_props)
    ax.annotate('', xy=(5, 7), xytext=(5, 8),
               arrowprops=arrow_props)
    ax.annotate('', xy=(5, 5), xytext=(5, 6),
               arrowprops=arrow_props)
    
    # Decision arrows
    ax.annotate('YES', xy=(2, 4), xytext=(4.5, 5),
               arrowprops=arrow_props, fontsize=9)
    ax.annotate('NO', xy=(8, 4), xytext=(5.5, 5),
               arrowprops=arrow_props, fontsize=9)
    
    # Loop arrow
    ax.annotate('', xy=(8, 7.5), xytext=(8, 3),
               arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', 
                             color='red', lw=1.5))
    ax.annotate('', xy=(5, 2), xytext=(8, 3),
               arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    
    # Add formulas
    formula_text = "RT = Tolerable Risk Level\nRx = Individual Risk Components\nSPM = Surge Protection Measures"
    ax.text(1, 0.5, formula_text, fontsize=8, style='italic', 
           bbox=dict(boxstyle="round,pad=0.3", facecolor="white", 
                    edgecolor="gray", alpha=0.7))
    
    ax.set_title('Figure 3: Risk Assessment Methodology per NBR 5419:2015 Part 2', 
                fontsize=13, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/claude/fig3_risk_assessment_flowchart.png', dpi=300)
    plt.show()
    return fig

def figure_4_spd_coordination():
    """
    Fig. 4: SPD Coordination and Installation Zones
    According to NBR 5419:2015 Part 4
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Top subplot - LPZ concept
    ax1.set_xlim(-2, 12)
    ax1.set_ylim(0, 8)
    ax1.set_aspect('equal')
    
    # Define zones
    zones = [
        {'name': 'LPZ 0A', 'x': 0, 'width': 2, 'color': 'red', 'alpha': 0.2},
        {'name': 'LPZ 0B', 'x': 2, 'width': 2, 'color': 'orange', 'alpha': 0.2},
        {'name': 'LPZ 1', 'x': 4, 'width': 2, 'color': 'yellow', 'alpha': 0.2},
        {'name': 'LPZ 2', 'x': 6, 'width': 2, 'color': 'lightgreen', 'alpha': 0.2},
        {'name': 'LPZ 3', 'x': 8, 'width': 2, 'color': 'lightblue', 'alpha': 0.2},
    ]
    
    for zone in zones:
        rect = Rectangle((zone['x'], 0), zone['width'], 6, 
                        facecolor=zone['color'], alpha=zone['alpha'], 
                        edgecolor='black', linewidth=1)
        ax1.add_patch(rect)
        ax1.text(zone['x'] + zone['width']/2, 7, zone['name'], 
                ha='center', fontweight='bold', fontsize=10)
    
    # Add SPD symbols
    spd_positions = [(3, 3), (5, 3), (7, 3), (9, 3)]
    spd_types = ['Type 1', 'Type 2', 'Type 3', 'Coordinated']
    
    for (x, y), spd_type in zip(spd_positions, spd_types):
        circle = Circle((x, y), 0.3, facecolor='white', edgecolor='black', linewidth=2)
        ax1.add_patch(circle)
        ax1.text(x, y-0.8, spd_type, ha='center', fontsize=9)
        # Add surge symbol
        ax1.plot([x-0.3, x-0.1, x+0.1, x+0.3], [y, y+0.2, y-0.2, y], 'b-', linewidth=2)
    
    # Add field strength indicators
    field_strengths = [100, 50, 10, 1, 0.1]
    for i, strength in enumerate(field_strengths):
        ax1.text(i*2 + 1, 0.5, f'{strength} kA/m', ha='center', 
                fontsize=8, style='italic')
    
    ax1.set_xlabel('Distance from Structure')
    ax1.set_ylabel('Protection Zone Height')
    ax1.set_title('(a) Lightning Protection Zones (LPZ) and SPD Placement', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Bottom subplot - Voltage protection levels
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 5)
    
    # Voltage levels
    voltage_levels = [
        {'x': 1, 'height': 4.5, 'label': 'Unprotected\n6 kV', 'color': 'red'},
        {'x': 3, 'height': 3, 'label': 'Type 1\n4 kV', 'color': 'orange'},
        {'x': 5, 'height': 2, 'label': 'Type 2\n2.5 kV', 'color': 'yellow'},
        {'x': 7, 'height': 1, 'label': 'Type 3\n1.5 kV', 'color': 'green'},
        {'x': 9, 'height': 0.5, 'label': 'Equipment\n0.8 kV', 'color': 'blue'},
    ]
    
    for level in voltage_levels:
        bar = Rectangle((level['x']-0.3, 0), 0.6, level['height'], 
                       facecolor=level['color'], alpha=0.6, edgecolor='black')
        ax2.add_patch(bar)
        ax2.text(level['x'], level['height']+0.2, level['label'], 
                ha='center', fontsize=9)
    
    # Add coordination line
    x_coord = np.array([1, 3, 5, 7, 9])
    y_coord = np.array([4.5, 3, 2, 1, 0.5])
    ax2.plot(x_coord, y_coord, 'k--', linewidth=2, label='Protection Level Cascade')
    
    ax2.set_xlabel('SPD Installation Point')
    ax2.set_ylabel('Voltage Protection Level Up (kV)')
    ax2.set_title('(b) SPD Coordination - Voltage Protection Levels', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    
    plt.suptitle('Figure 4: SPD Coordination per NBR 5419:2015 Part 4', 
                fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/home/claude/fig4_spd_coordination.png', dpi=300)
    plt.show()
    return fig

def figure_5_grounding_arrangements():
    """
    Fig. 5: Grounding Arrangements and Equipotential Bonding
    According to NBR 5419:2015 Part 3
    """
    fig = plt.figure(figsize=(14, 10))
    
    # Type A - Ring Earth Electrode
    ax1 = plt.subplot(2, 3, 1)
    ax1.set_xlim(-15, 15)
    ax1.set_ylim(-15, 15)
    ax1.set_aspect('equal')
    
    # Building footprint
    building = Rectangle((-8, -8), 16, 16, fill=False, edgecolor='black', linewidth=2)
    ax1.add_patch(building)
    
    # Ring electrode
    ring = Circle((0, 0), 12, fill=False, edgecolor='green', linewidth=3)
    ax1.add_patch(ring)
    
    # Connection points
    angles = np.linspace(0, 2*np.pi, 9)
    for angle in angles[:-1]:
        x = 12 * np.cos(angle)
        y = 12 * np.sin(angle)
        ax1.plot(x, y, 'ro', markersize=6)
    
    ax1.set_title('(a) Type A - Ring Electrode')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Distance (m)')
    ax1.set_ylabel('Distance (m)')
    
    # Type B - Foundation Earth Electrode
    ax2 = plt.subplot(2, 3, 2)
    ax2.set_xlim(-15, 15)
    ax2.set_ylim(-15, 15)
    ax2.set_aspect('equal')
    
    # Foundation outline
    foundation = Rectangle((-10, -10), 20, 20, fill=True, 
                          facecolor='lightgray', edgecolor='black', linewidth=2)
    ax2.add_patch(foundation)
    
    # Mesh in foundation
    for i in range(-8, 9, 4):
        ax2.plot([-10, 10], [i, i], 'g-', linewidth=2)
        ax2.plot([i, i], [-10, 10], 'g-', linewidth=2)
    
    # Building
    building = Rectangle((-8, -8), 16, 16, fill=False, edgecolor='black', linewidth=2)
    ax2.add_patch(building)
    
    ax2.set_title('(b) Type B - Foundation Electrode')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Distance (m)')
    ax2.set_ylabel('Distance (m)')
    
    # Vertical Rod Configuration
    ax3 = plt.subplot(2, 3, 3)
    ax3.set_xlim(-15, 15)
    ax3.set_ylim(-5, 20)
    
    # Ground level
    ax3.axhline(y=0, color='brown', linewidth=3, alpha=0.5)
    ax3.fill_between([-15, 15], -5, 0, color='brown', alpha=0.2)
    
    # Vertical rods
    rod_positions = [-8, -4, 0, 4, 8]
    for x in rod_positions:
        ax3.plot([x, x], [0, -3], 'k-', linewidth=4)
        ax3.plot(x, 0, 'ro', markersize=8)
    
    # Connection cable
    ax3.plot(rod_positions, [0]*len(rod_positions), 'g-', linewidth=2)
    
    ax3.set_title('(c) Vertical Rod Array')
    ax3.set_xlabel('Distance (m)')
    ax3.set_ylabel('Depth (m)')
    ax3.grid(True, alpha=0.3)
    ax3.text(0, -4, 'L = 3m rods', ha='center', fontsize=9, style='italic')
    
    # Equipotential Bonding
    ax4 = plt.subplot(2, 3, 4)
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 10)
    
    # Main grounding bar
    ax4.plot([2, 8], [5, 5], 'g-', linewidth=6, label='Main Earth Bar')
    
    # Connected systems
    systems = [
        (3, 5, 'SPDA'),
        (4, 5, 'Power'),
        (5, 5, 'Telecom'),
        (6, 5, 'Water'),
        (7, 5, 'Gas'),
    ]
    
    for x, y, label in systems:
        ax4.plot([x, x], [y, y+2], 'k-', linewidth=2)
        ax4.plot(x, y, 'ro', markersize=8)
        ax4.text(x, y+2.5, label, ha='center', fontsize=8, rotation=0)
    
    ax4.set_title('(d) Equipotential Bonding')
    ax4.set_xlabel('Position')
    ax4.set_ylabel('Height')
    ax4.grid(True, alpha=0.3)
    ax4.legend(loc='lower right')
    
    # Resistance vs Soil Resistivity
    ax5 = plt.subplot(2, 3, 5)
    
    resistivity = np.logspace(1, 4, 50)  # 10 to 10000 ohm.m
    
    # Resistance formulas for different arrangements
    R_vertical = resistivity / (2 * np.pi * 3) * np.log(8 * 3 / 0.025)  # Single rod
    R_ring = resistivity / (2 * np.pi**2 * 12)  # Ring electrode
    R_mesh = resistivity / (4 * 20)  # Mesh electrode
    
    ax5.loglog(resistivity, R_vertical, 'r-', label='Single Rod (3m)')
    ax5.loglog(resistivity, R_ring, 'g-', label='Ring (r=12m)')
    ax5.loglog(resistivity, R_mesh, 'b-', label='Mesh (20×20m)')
    
    ax5.set_xlabel('Soil Resistivity ρ (Ω·m)')
    ax5.set_ylabel('Grounding Resistance R (Ω)')
    ax5.set_title('(e) Resistance vs Soil Resistivity')
    ax5.grid(True, alpha=0.3, which='both')
    ax5.legend(loc='upper left')
    ax5.axhline(y=10, color='red', linestyle='--', alpha=0.5)
    ax5.text(100, 12, 'Max 10Ω (NBR 5419)', fontsize=8, color='red')
    
    # Impulse Impedance
    ax6 = plt.subplot(2, 3, 6)
    
    time = np.linspace(0, 100, 1000)  # microseconds
    
    # Typical impulse response
    Z_steady = 10  # Steady state resistance
    tau = 10  # Time constant
    Z_impulse = Z_steady * (1 + 2 * np.exp(-time/tau))
    
    ax6.plot(time, Z_impulse, 'b-', linewidth=2)
    ax6.axhline(y=Z_steady, color='red', linestyle='--', alpha=0.5)
    
    ax6.set_xlabel('Time (μs)')
    ax6.set_ylabel('Impedance Z (Ω)')
    ax6.set_title('(f) Impulse Impedance Response')
    ax6.grid(True, alpha=0.3)
    ax6.text(50, Z_steady + 0.5, f'Steady State = {Z_steady}Ω', 
            fontsize=8, color='red')
    
    plt.suptitle('Figure 5: Grounding Arrangements per NBR 5419:2015', 
                fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/home/claude/fig5_grounding_arrangements.png', dpi=300)
    plt.show()
    return fig

def figure_6_separation_distances():
    """
    Fig. 6: Separation Distance Calculation
    According to NBR 5419:2015 Part 3, Section 6.3
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Left subplot - Separation distance concept
    ax1.set_xlim(-10, 30)
    ax1.set_ylim(0, 25)
    
    # Building structure
    building = Rectangle((0, 0), 15, 20, fill=False, edgecolor='black', linewidth=2)
    ax1.add_patch(building)
    
    # Down conductor
    ax1.plot([2, 2], [0, 20], 'r-', linewidth=3, label='Down Conductor')
    
    # Internal installation
    ax1.plot([8, 8], [5, 15], 'b-', linewidth=2, label='Internal Installation')
    
    # Separation distance
    ax1.annotate('', xy=(8, 10), xytext=(2, 10),
                arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax1.text(5, 11, 's', fontsize=12, fontweight='bold', color='green')
    
    # Formula
    formula = r's = $k_i$ × $\frac{k_c}{k_m}$ × L'
    ax1.text(16, 15, formula, fontsize=11, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    # Legend for formula
    legend_text = ('where:\n'
                  'ki = depends on protection level\n'
                  'kc = current distribution\n'
                  'km = material insulation\n'
                  'L = length along conductor')
    ax1.text(16, 8, legend_text, fontsize=9, style='italic')
    
    ax1.set_xlabel('Horizontal Distance (m)')
    ax1.set_ylabel('Height (m)')
    ax1.set_title('(a) Separation Distance Concept')
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # Right subplot - Separation distance vs height for different configurations
    ax2.set_xlim(0, 25)
    ax2.set_ylim(0, 1.5)
    
    heights = np.linspace(0, 25, 100)
    
    # Different ki values for protection levels
    ki_values = {'I': 0.08, 'II': 0.06, 'III-IV': 0.04}
    kc = 0.44  # Single down conductor
    km = 1.0   # Air insulation
    
    for level, ki in ki_values.items():
        s = ki * (kc/km) * heights
        ax2.plot(heights, s, label=f'Level {level} (ki={ki})', linewidth=2)
    
    # Add configuration with multiple down conductors
    kc_multi = 0.66  # Multiple down conductors
    s_multi = 0.08 * (kc_multi/km) * heights
    ax2.plot(heights, s_multi, '--', label='Level I (Multiple DC)', linewidth=2)
    
    ax2.set_xlabel('Length L (m)')
    ax2.set_ylabel('Separation Distance s (m)')
    ax2.set_title('(b) Required Separation Distance')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper left')
    
    # Add critical distance line
    ax2.axhline(y=0.5, color='red', linestyle=':', alpha=0.5)
    ax2.text(20, 0.52, 'Typical wall thickness', fontsize=8, color='red')
    
    plt.suptitle('Figure 6: Separation Distance Requirements per NBR 5419:2015', 
                fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/home/claude/fig6_separation_distances.png', dpi=300)
    plt.show()
    return fig

def figure_7_brasilia_lightning_density():
    """
    Fig. 7: Lightning Ground Flash Density Map - Federal District Region
    Focus on Brasília's High Incidence Area
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Left subplot - Density map
    ax1.set_xlim(-48.3, -47.3)
    ax1.set_ylim(-16.1, -15.4)
    
    # Create density heatmap
    lon = np.linspace(-48.3, -47.3, 50)
    lat = np.linspace(-16.1, -15.4, 50)
    LON, LAT = np.meshgrid(lon, lat)
    
    # Simulate density data (Ng - ground flash density)
    # Brasília has high values around 13-17 flashes/km²/year
    center_lon, center_lat = -47.85, -15.78  # Brasília coordinates
    density = 15 * np.exp(-((LON - center_lon)**2 + (LAT - center_lat)**2) / 0.1)
    density += 8  # Background density
    
    # Add some variation
    noise = np.random.randn(50, 50) * 1
    density += noise
    density = np.clip(density, 5, 20)
    
    im = ax1.contourf(LON, LAT, density, levels=15, cmap='hot_r')
    plt.colorbar(im, ax=ax1, label='Ng (flashes/km²/year)')
    
    # Mark key locations
    ax1.plot(-47.85, -15.78, 'b*', markersize=15, label='Brasília Center')
    ax1.plot(-47.92, -15.83, 'wo', markersize=8, label='Airport')
    ax1.plot(-47.88, -15.75, 'ws', markersize=8, label='Gov. District')
    
    ax1.set_xlabel('Longitude')
    ax1.set_ylabel('Latitude')
    ax1.set_title('(a) Lightning Density Map - Federal District')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='lower left')
    
    # Right subplot - Annual variation
    ax2.set_xlim(0, 13)
    ax2.set_ylim(0, 40)
    
    months = np.arange(1, 13)
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Typical distribution for Brasília (wet season Oct-Apr)
    monthly_percent = np.array([18, 16, 14, 8, 2, 0.5, 
                               0.5, 1, 3, 12, 15, 10])
    
    bars = ax2.bar(months, monthly_percent, color='darkblue', alpha=0.7, 
                  edgecolor='black', linewidth=1)
    
    # Highlight wet season
    for i in [0, 1, 2, 3, 9, 10, 11]:
        bars[i].set_facecolor('red')
        bars[i].set_alpha(0.8)
    
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Percentage of Annual Lightning Activity (%)')
    ax2.set_title('(b) Seasonal Distribution - Brasília Region')
    ax2.set_xticks(months)
    ax2.set_xticklabels(month_names, rotation=45)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Add season indicators
    ax2.axvspan(0.5, 4.5, alpha=0.1, color='red', label='Wet Season')
    ax2.axvspan(9.5, 12.5, alpha=0.1, color='red')
    ax2.axvspan(4.5, 9.5, alpha=0.1, color='blue', label='Dry Season')
    ax2.legend(loc='upper right')
    
    # Add statistics
    stats_text = ('Annual Average: 77.8 million strikes (Brazil)\n'
                 'Federal District: ~15 flashes/km²/year\n'
                 '90% occur during wet season')
    ax2.text(0.5, 35, stats_text, fontsize=8, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    plt.suptitle('Figure 7: Lightning Activity in Brasília Federal District Region', 
                fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/home/claude/fig7_brasilia_lightning_density.png', dpi=300)
    plt.show()
    return fig

def figure_8_material_specifications():
    """
    Fig. 8: Material Specifications and Cross-Sections
    According to NBR 5419:2015 Part 3, Section 5.3
    """
    fig = plt.figure(figsize=(14, 10))
    
    # Material comparison table
    ax1 = plt.subplot(2, 2, 1)
    ax1.axis('off')
    
    # Create table data
    materials = ['Copper', 'Aluminum', 'Stainless\nSteel', 'Galvanized\nSteel']
    properties = ['Min. Section\n(mm²)', 'Corrosion\nResistance', 'Cost\nIndex', 'Weight\n(kg/m)']
    
    data = [
        ['35', '50', '50', '50'],  # Min section
        ['Excellent', 'Good', 'Excellent', 'Moderate'],  # Corrosion
        ['100', '40', '120', '30'],  # Cost index
        ['0.31', '0.14', '0.39', '0.39'],  # Weight
    ]
    
    # Create table
    table = ax1.table(cellText=data, rowLabels=properties, colLabels=materials,
                     cellLoc='center', loc='center',
                     colWidths=[0.15]*4, cellColours=None)
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    ax1.set_title('(a) Material Specifications per NBR 5419:2015', fontweight='bold')
    
    # Conductor cross-sections
    ax2 = plt.subplot(2, 2, 2)
    ax2.set_xlim(-2, 10)
    ax2.set_ylim(-1, 6)
    ax2.set_aspect('equal')
    
    # Round conductor
    circle = Circle((1, 3), 0.5, facecolor='#B87333', edgecolor='black', linewidth=1)
    ax2.add_patch(circle)
    ax2.text(1, 1.5, 'Round\n8mm ø\n50mm²', ha='center', fontsize=9)
    
    # Flat conductor
    rect = Rectangle((3, 2.5), 2, 0.5, facecolor='silver', edgecolor='black', linewidth=1)
    ax2.add_patch(rect)
    ax2.text(4, 1.5, 'Flat\n30×3mm\n90mm²', ha='center', fontsize=9)
    
    # Stranded conductor
    for i in range(7):
        angle = i * 2 * np.pi / 7
        x = 7 + 0.2 * np.cos(angle)
        y = 3 + 0.2 * np.sin(angle)
        small_circle = Circle((x, y), 0.1, facecolor='gray', edgecolor='black', linewidth=0.5)
        ax2.add_patch(small_circle)
    ax2.text(7, 1.5, 'Stranded\n7×2.5mm\n35mm²', ha='center', fontsize=9)
    
    ax2.set_title('(b) Conductor Cross-Sections', fontweight='bold')
    ax2.axis('off')
    
    # Connection methods
    ax3 = plt.subplot(2, 2, 3)
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 8)
    
    # Exothermic welding
    ax3.add_patch(Rectangle((0.5, 6), 2, 1, facecolor='orange', alpha=0.8))
    ax3.text(1.5, 6.5, 'Exothermic\nWelding', ha='center', fontsize=9, fontweight='bold')
    
    # Compression connector
    ax3.add_patch(Rectangle((3, 6), 2, 1, facecolor='lightblue', alpha=0.8))
    ax3.text(4, 6.5, 'Compression\nConnector', ha='center', fontsize=9, fontweight='bold')
    
    # Bolted connection
    ax3.add_patch(Rectangle((5.5, 6), 2, 1, facecolor='lightgreen', alpha=0.8))
    ax3.text(6.5, 6.5, 'Bolted\nConnection', ha='center', fontsize=9, fontweight='bold')
    
    # Clamped connection
    ax3.add_patch(Rectangle((8, 6), 2, 1, facecolor='lightyellow', alpha=0.8))
    ax3.text(9, 6.5, 'Clamped\nConnection', ha='center', fontsize=9, fontweight='bold')
    
    # Add resistance values
    resistances = ['< 0.001Ω', '< 0.005Ω', '< 0.01Ω', '< 0.02Ω']
    durabilities = ['50+ years', '30+ years', '20+ years', '10+ years']
    
    for i, (res, dur) in enumerate(zip(resistances, durabilities)):
        x = 1.5 + i * 2.5
        ax3.text(x, 5, res, ha='center', fontsize=8, color='red')
        ax3.text(x, 4.5, dur, ha='center', fontsize=8, color='blue')
    
    ax3.text(5, 3.5, 'Connection Resistance', ha='center', fontsize=9, 
            color='red', fontweight='bold')
    ax3.text(5, 3, 'Expected Durability', ha='center', fontsize=9, 
            color='blue', fontweight='bold')
    
    ax3.set_title('(c) Connection Methods', fontweight='bold')
    ax3.axis('off')
    
    # Corrosion compatibility matrix
    ax4 = plt.subplot(2, 2, 4)
    
    metals = ['Cu', 'Al', 'SS', 'GS', 'Pb']
    compatibility = np.array([
        [0, 2, 1, 2, 1],  # Cu
        [2, 0, 2, 2, 1],  # Al
        [1, 2, 0, 1, 1],  # SS
        [2, 2, 1, 0, 1],  # GS
        [1, 1, 1, 1, 0],  # Pb
    ])
    
    im = ax4.imshow(compatibility, cmap='RdYlGn_r', vmin=0, vmax=2, aspect='equal')
    
    ax4.set_xticks(range(5))
    ax4.set_yticks(range(5))
    ax4.set_xticklabels(metals)
    ax4.set_yticklabels(metals)
    
    # Add text annotations
    for i in range(5):
        for j in range(5):
            if compatibility[i, j] == 0:
                text = 'OK'
                color = 'white'
            elif compatibility[i, j] == 1:
                text = 'Care'
                color = 'black'
            else:
                text = 'Avoid'
                color = 'white'
            ax4.text(j, i, text, ha='center', va='center', 
                    color=color, fontsize=9, fontweight='bold')
    
    ax4.set_title('(d) Galvanic Corrosion Compatibility', fontweight='bold')
    ax4.set_xlabel('Material 1')
    ax4.set_ylabel('Material 2')
    
    # Add legend
    legend_elements = [plt.Rectangle((0, 0), 1, 1, fc='green', label='Compatible'),
                      plt.Rectangle((0, 0), 1, 1, fc='yellow', label='Caution'),
                      plt.Rectangle((0, 0), 1, 1, fc='red', label='Avoid')]
    ax4.legend(handles=legend_elements, loc='center', bbox_to_anchor=(1.15, 0.5))
    
    plt.suptitle('Figure 8: Material Specifications and Installation Methods per NBR 5419:2015', 
                fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/home/claude/fig8_material_specifications.png', dpi=300)
    plt.show()
    return fig

def generate_all_figures():
    """Generate all figures for the thesis"""
    print("Generating Figure 1: Rolling Sphere Method...")
    figure_1_rolling_sphere_method()
    
    print("Generating Figure 2: Mesh Conductor Spacing...")
    figure_2_mesh_conductor_spacing()
    
    print("Generating Figure 3: Risk Assessment Flowchart...")
    figure_3_risk_assessment_flowchart()
    
    print("Generating Figure 4: SPD Coordination...")
    figure_4_spd_coordination()
    
    print("Generating Figure 5: Grounding Arrangements...")
    figure_5_grounding_arrangements()
    
    print("Generating Figure 6: Separation Distances...")
    figure_6_separation_distances()
    
    print("Generating Figure 7: Brasília Lightning Density...")
    figure_7_brasilia_lightning_density()
    
    print("Generating Figure 8: Material Specifications...")
    figure_8_material_specifications()
    
    print("\nAll figures generated successfully!")
    print("Files saved in /home/claude/ directory")

if __name__ == "__main__":
    generate_all_figures()
