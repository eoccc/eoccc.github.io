# Accelerator

## Accelerator

*继承自 Block*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| arrowRegion | TextureRegion | null |  |
| selectArrowRegion | TextureRegion | null |  |
| launchBlock | Block | coreNucleus | 被发射的核心方块，应与目标星球的初始核心一致。 |
| powerBufferRequirement | float | 0.0 |  |
| launchCandidates | Seq of Planet | null | 该方块可发射至的星球覆盖值。为 null 时使用星球的默认发射候选。 |
| lightningSound | Sound | shootArc) |  |
| lightningSoundVolume | float | 0.85 |  |
| chargeSound | Sound | acceleratorCharge |  |
| launchSound | Sound | acceleratorLaunch |  |
| constructSound | Sound | acceleratorConstruct |  |
| launchDuration | float | 120.0 |  |
| chargeDuration | float | 220.0 |  |
| buildDuration | float | 120.0 |  |
| landZoomInterp | Interp | pow4In |  |
| chargeZoomInterp | Interp | pow4In |  |
| landZoomFrom | float | 0.02 |  |
| landZoomTo | float | 4.0 |  |
| chargeZoomTo | float | 5.0 |  |
| chargeRings | int | 4 |  |
| ringRadBase | float | 60.0 |  |
| ringRadSpacing | float | 25.0 |  |
| ringRadPow | float | 1.6 |  |
| ringStroke | float | 3.0 |  |
| ringSpeedup | float | 1.4 |  |
| chargeRingMerge | float | 2.0 |  |
| ringArrowRad | float | 3.0 |  |
| ringHandleTilt | float | 0.8 |  |
| ringHandleLen | float | 30.0 |  |
| ringColor | Color | ffd37fff |  |
| launchLightning | int | 20 |  |
| lightningColor | Color | ffd37fff |  |
| lightningDamage | float | 40.0 |  |
| lightningOffset | float | 24.0 |  |
| lightningLengthMin | int | 5 |  |
| lightningLengthMax | int | 25 |  |
| lightningLaunchChance | double | 0.8 |  |
