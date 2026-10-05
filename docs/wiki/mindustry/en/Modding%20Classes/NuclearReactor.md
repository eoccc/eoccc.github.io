# NuclearReactor

## NuclearReactor

*extends PowerGenerator*

| field | type | default | notes |
|---|---|---|---|
| timerFuel | int | 1 |  |
| lightColor | Color | 7f19eaff |  |
| coolColor | Color | ffffff00 |  |
| hotColor | Color | ff9575a3 |  |
| itemDuration | float | 120.0 | ticks to consume 1 fuel |
| heating | float | 0.01 | heating per frame * fullness |
| heatOutput | float | 8.0 | max heat this block can output per side |
| heatWarmupRate | float | 1.0 | rate at which heat progress increases |
| heatConsumeRate | float | 10.0 | rate at which fuel consumption scales with heat |
| ambientCooldownTime | float | 1200.0 | time taken to cool down if no fuel is inputted even if coolant is not present |
| smokeThreshold | float | 0.3 | threshold at which block starts smoking |
| flashThreshold | float | 0.46 | heat threshold at which lights start flashing |
| coolantPower | float | 0.5 | heat removed per unit of coolant |
| fuelItem | Item | thorium |  |
| topRegion | TextureRegion | null |  |
| lightsRegion | TextureRegion | null |  |
