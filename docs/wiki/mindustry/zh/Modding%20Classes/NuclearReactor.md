# NuclearReactor

## NuclearReactor

*继承自 PowerGenerator*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| timerFuel | int | 1 |  |
| lightColor | Color | 7f19eaff |  |
| coolColor | Color | ffffff00 |  |
| hotColor | Color | ff9575a3 |  |
| itemDuration | float | 120.0 | ticks to consume 1 fuel |
| heating | float | 0.01 | heating per frame * fullness |
| heatOutput | float | 8.0 | 该方块每侧可输出的最大热量 |
| heatWarmupRate | float | 1.0 | 热量进度增加的速率 |
| heatConsumeRate | float | 10.0 | 燃料消耗随热量缩放的速率 |
| ambientCooldownTime | float | 1200.0 | 即使没有冷却液，若未输入燃料也会冷却所需的时间 |
| smokeThreshold | float | 0.3 | 方块开始冒烟的阈值 |
| flashThreshold | float | 0.46 | 灯光开始闪烁的热量阈值 |
| coolantPower | float | 0.5 | 每单位冷却液移除的热量 |
| fuelItem | Item | thorium |  |
| topRegion | TextureRegion | null |  |
| lightsRegion | TextureRegion | null |  |
