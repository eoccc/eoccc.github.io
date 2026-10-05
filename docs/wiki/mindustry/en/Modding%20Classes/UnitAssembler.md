# UnitAssembler

## UnitAssembler

*extends PayloadBlock*

| field | type | default | notes |
|---|---|---|---|
| sideRegion1 | TextureRegion | null |  |
| sideRegion2 | TextureRegion | null |  |
| areaSize | int | 11 |  |
| droneType | UnitType | assemblyDrone | Note: The spawned unit MUST have AssemblerAI as a controller and 'tether' (BuildingTetherComp) as a unit component. |
| dronesCreated | int | 4 |  |
| droneConstructTime | float | 240.0 |  |
| capacities | int[] | [] |  |
| plans | Seq of AssemblerUnitPlan | [] |  |
| createSound | Sound | unitCreateBig |  |
| createSoundVolume | float | 1.0 |  |
