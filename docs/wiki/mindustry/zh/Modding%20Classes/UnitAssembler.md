# UnitAssembler

## UnitAssembler

*继承自 PayloadBlock*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| sideRegion1 | TextureRegion | null |  |
| sideRegion2 | TextureRegion | null |  |
| areaSize | int | 11 |  |
| droneType | UnitType | assemblyDrone | 注意：所生成的单位必须以 AssemblerAI 作为控制器，并以 'tether'（BuildingTetherComp）作为单位组件。 |
| dronesCreated | int | 4 |  |
| droneConstructTime | float | 240.0 |  |
| capacities | int[] | [] |  |
| plans | Seq of AssemblerUnitPlan | [] |  |
| createSound | Sound | unitCreateBig |  |
| createSoundVolume | float | 1.0 |  |
