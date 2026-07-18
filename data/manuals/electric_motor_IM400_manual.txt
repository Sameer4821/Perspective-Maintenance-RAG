THREE-PHASE INDUCTION MOTOR SERIES IM-400
OPERATION & MAINTENANCE MANUAL
Frame Sizes: 160M to 280S
Manufacturer: ElectraDrive Motor Systems
Document Number: ED-MNL-002 | Revision: 2.8

================================================================================
TABLE OF CONTENTS
================================================================================
1. Introduction and Safety
2. Motor Nameplate Data
3. Installation Requirements
4. Insulation and Winding Care
5. Bearing Maintenance
6. Troubleshooting
7. Fault Codes
8. Rewinding Criteria

================================================================================
SECTION 1: INTRODUCTION AND SAFETY
================================================================================

This manual covers the installation, operation, and maintenance of ElectraDrive
IM-400 series three-phase induction motors for industrial applications.

WARNING: Hazardous voltage. Risk of electric shock.
Always de-energize and lockout/tagout before performing maintenance.

Motor Protection Ratings:
- IP55 (standard): Dust-tight, protected against water jets
- IP65 (optional): Dust-tight, protected against water jets from all directions
- ATEX Zone 2 (optional): Suitable for potentially explosive atmospheres

================================================================================
SECTION 2: MOTOR NAMEPLATE DATA
================================================================================

2.1 Understanding the Nameplate

| Parameter      | Description                  | Typical Values           |
|----------------|------------------------------|--------------------------|
| kW             | Rated shaft output power     | 7.5 / 11 / 15 / 18.5 kW |
| V              | Supply voltage               | 380-420V / 660-690V      |
| A              | Full load current (FLA)      | 16.2A (at 7.5kW, 400V)  |
| Hz             | Supply frequency             | 50 Hz                    |
| RPM            | Synchronous / Full load RPM  | 3000 / 2950              |
| cos φ          | Power factor                 | 0.87                     |
| η              | Efficiency at full load      | 91.5%                    |
| Class          | Insulation class             | F (155°C max)            |
| Temp Rise      | Maximum temperature rise     | 80°C (Class B rise)      |
| S.F.           | Service factor               | 1.15                     |

2.2 Connection Configurations

| Supply Voltage | Terminal Connection | Diagram |
|----------------|---------------------|---------|
| 380V           | Delta (Δ)           | L1-W2,U2 / L2-U2,V1 / L3-V2,W1 |
| 660V           | Star (Y)            | U2-V2-W2 linked / L1-U1 / L2-V1 / L3-W1 |

================================================================================
SECTION 3: INSTALLATION REQUIREMENTS
================================================================================

3.1 Mounting and Alignment

Alignment Tolerances (Flexible Coupling):
- Parallel misalignment: < 0.1 mm
- Angular misalignment: < 0.1 mm per 100mm coupling diameter
- Axial float: 1-2mm

3.2 Ventilation Requirements
- Minimum clearance at fan cover: 100mm
- Ambient temperature range: -20°C to +40°C
- Altitude derating: > 1000m above sea level requires 1% power deduction per 100m

================================================================================
SECTION 4: INSULATION AND WINDING CARE
================================================================================

4.1 Insulation Resistance Testing

Measure insulation resistance before first start and after any rewinding:

| Condition             | Minimum Acceptable Resistance |
|-----------------------|-------------------------------|
| New motor (20°C)      | > 100 MΩ                      |
| After rewinding       | > 50 MΩ                       |
| In service (40°C)     | > 10 MΩ                       |
| Caution zone          | 1 - 10 MΩ (monitor closely)   |
| Do NOT energize       | < 1 MΩ (dry out winding first)|

4.2 Winding Drying Procedure (If Insulation Resistance < 1 MΩ)
Step 1: Disconnect motor from supply completely
Step 2: Remove motor from installation if possible
Step 3: Place in oven at 90°C for 8 hours
Step 4: Increase oven temperature to 105°C for additional 8 hours
Step 5: Allow to cool to ambient temperature
Step 6: Re-measure insulation resistance — must exceed 10 MΩ before re-energizing

================================================================================
SECTION 5: BEARING MAINTENANCE
================================================================================

5.1 Bearing Specifications

| Frame Size | Drive End Bearing | Non-Drive End Bearing |
|------------|-------------------|-----------------------|
| 160M       | 6309-2Z           | 6207-2Z               |
| 180L       | 6311-2Z           | 6209-2Z               |
| 200L       | 6312-2Z           | 6210-2Z               |
| 225M       | 6314-2Z           | 6212-2Z               |
| 280S       | 6316-2Z           | 6214-2Z               |

5.2 Bearing Lubrication

Greasing Intervals:
| Operating Condition    | Temperature  | Greasing Interval  |
|------------------------|--------------|---------------------|
| Normal (light load)    | < 70°C       | Every 4000 hours    |
| Medium (normal load)   | 70 - 85°C    | Every 2000 hours    |
| Severe (high load)     | 85 - 100°C   | Every 1000 hours    |
| Very Severe (heavy)    | > 100°C      | Every 500 hours     |

Approved Greases:
- Shell Alvania R2
- Mobilux EP2  
- Kluber Asonic GLY 32 (for high temperature)

Quantity: 10-15g per bearing (use grease gun, not air pressure)

CAUTION: Over-greasing causes overheating and premature bearing failure.
Remove relief plug during greasing to allow excess grease to escape.

5.3 Bearing Replacement Triggers

Replace bearings immediately when:
- Vibration velocity (10-1000Hz) exceeds 6.3 mm/s RMS
- Bearing running temperature exceeds 100°C
- Audible noise detected: rumbling, squealing, or grinding
- Shaft end-play exceeds 0.5mm
- Raceway pitting visible on inspection

================================================================================
SECTION 6: TROUBLESHOOTING
================================================================================

6.1 Motor Will Not Start

| Symptom                | Probable Cause           | Corrective Action                   |
|------------------------|--------------------------|-------------------------------------|
| No hum, no movement    | No power supply          | Check supply voltage at terminals   |
| Hum but no rotation    | Single phasing           | Check all three fuses and contactors|
| Hum but no rotation    | Rotor locked             | Check for mechanical blockage       |
| Overload trips on start| Load too high at start   | Check driven equipment; reduce load |
| Overload trips on start| Overload setting too low | Adjust overload to 110-115% FLA     |

6.2 Motor Runs But Overheats

| Symptom                | Probable Cause           | Corrective Action                   |
|------------------------|--------------------------|-------------------------------------|
| Temperature > 100°C    | Overloaded               | Measure current; reduce mechanical load |
| Temperature > 100°C    | Ventilation blocked      | Clean fan and air passages          |
| Temperature > 100°C    | Single phasing in service| Check supply voltage all 3 phases   |
| Temperature > 100°C    | High ambient temperature | Provide additional cooling/ventilation |
| Temperature > 100°C    | Voltage unbalance > 2%   | Investigate supply quality          |

6.3 Excessive Vibration and Noise

| Symptom                | Probable Cause           | Corrective Action                   |
|------------------------|--------------------------|-------------------------------------|
| Rumbling noise         | Worn or damaged bearing  | Replace bearings                    |
| High-pitched squeal    | Bearing dry (no grease)  | Regrease immediately; check bearing |
| Vibration at 1x RPM    | Rotor unbalance          | Balance rotor; check for deposits   |
| Vibration at 2x RPM    | Misalignment             | Re-align motor and driven equipment |
| Vibration at 2x supply | Loose stator laminations | Return to manufacturer for repair   |

================================================================================
SECTION 7: FAULT CODES (MOTOR PROTECTION RELAY)
================================================================================

7.1 Protection Relay Fault Codes

| Code  | Fault Description           | Setpoint         | Action Required                     |
|-------|-----------------------------|------------------|-------------------------------------|
| F-01  | Overload - Phase L1         | > 115% FLA       | Check current; reduce load          |
| F-02  | Overload - Phase L2         | > 115% FLA       | Check current; reduce load          |
| F-03  | Overload - Phase L3         | > 115% FLA       | Check current; reduce load          |
| F-04  | Phase Imbalance             | > 10% imbalance  | Check supply voltages and fuses     |
| F-05  | Phase Loss                  | Any phase absent | Check fuses, contactors, supply     |
| F-06  | Thermistor (PTC) Trip       | Winding too hot  | Allow motor to cool; check load     |
| F-07  | Earth Fault                 | > 30mA earth     | Megger test; check cable insulation |
| F-08  | Undercurrent                | < 20% FLA        | Check coupling; check driven equip  |
| F-09  | Stall / Locked Rotor        | Start time exceed| Check mechanical load; check supply |
| F-10  | Short Circuit               | Instantaneous    | Check winding; replace if damaged   |

================================================================================
SECTION 8: REWINDING CRITERIA
================================================================================

8.1 Rewind vs Replace Decision

Consider rewinding when:
- Motor > 37kW AND repair cost < 65% of replacement cost
- Motor is special design (Ex-proof, high-temperature, etc.)
- Long lead time for replacement

Consider replacing when:
- Motor < 11kW (replacement is more economical)
- Winding failed due to bearing-induced damage (second failure likely)
- Motor is more than 15 years old
- Replacement offers significant efficiency improvement (IE3 vs IE1)

8.2 Winding Failure Analysis

| Failure Pattern            | Probable Cause            | Prevention                  |
|----------------------------|---------------------------|-----------------------------|
| All three phases burned    | Voltage imbalance         | Improve power supply quality |
| Single phase burned        | Single phasing event      | Install phase loss protection|
| End turns burned           | Voltage spikes (VFD)      | Install output reactor      |
| Burn at 1/3 winding        | Turn-to-turn short        | Improve insulation class     |
| Burn at slot exit          | Vibration fretting        | Improve motor mounting      |

================================================================================
END OF DOCUMENT
================================================================================
Document: ED-MNL-002 | Revision: 2.8 | Date: 2024-03
ElectraDrive Motor Systems | www.electradrive-motors.com
Technical Hotline: +1-800-555-0200