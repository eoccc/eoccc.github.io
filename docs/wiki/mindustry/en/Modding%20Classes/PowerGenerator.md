# PowerGenerator

## PowerGenerator

*extends PowerDistributor*

| field | type | default | notes |
|---|---|---|---|
| powerProduction | float | 0.0 | The amount of power produced per tick in case of an efficiency of 1.0, which represents 100%. |
| generationType | Stat | basePowerGeneration |  |
| drawer | DrawBlock | new DrawDefault() |  |
| explosionRadius | int | 12 |  |
| explosionDamage | int | 0 |  |
| explodeEffect | Effect | none |  |
| explodeSound | Sound | none |  |
| explosionPuddles | int | 10 |  |
| explosionPuddleRange | float | 16.0 |  |
| explosionPuddleAmount | float | 100.0 |  |
| explosionPuddleLiquid | Liquid | null |  |
| explosionMinWarmup | float | 0.0 |  |
| explosionShake | float | 0.0 |  |
| explosionShakeDuration | float | 6.0 |  |
| explosionBreaksProps | boolean | true |  |
| explosionScorchSize | int | 0 | Size of scorch effect on the ground after explosion. Value from 1-9. < 1 to disable. |
| explosionIgnitionChance | float | 0.0 | Chance for each tile in the explosion radius to catch on fire. |
| explosionScaleIgnitionChance | boolean | true | If true, the ignition chance decreases with distance. |
| explosionSpeed | float | 0.4 | The speed at which ignition spreads. |
| explosionFireballs | int | 0 | Extra number of fireballs spawned from explosions. |
