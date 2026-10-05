# MoveLightningAbility

## MoveLightningAbility

*extends Ability*

| field | type | default | notes |
|---|---|---|---|
| damage | float | 35.0 | Lightning damage |
| chance | float | 0.15 | Chance of firing every tick. Set >= 1 to always fire lightning every tick at max speed |
| length | int | 12 | Length of the lightning. <= 0 to disable |
| minSpeed | float | 0.8 | Speeds for when to start lightninging and when to stop getting faster |
| maxSpeed | float | 1.2 | Speeds for when to start lightninging and when to stop getting faster |
| color | Color | a9d8ffff | Lightning color |
| y | float | 0.0 | Shifts where the lightning spawns along the Y axis |
| x | float | 0.0 | Offset along the X axis |
| alternate | boolean | true | Whether the spawn side alternates |
| heatRegion | String | "error" | Jittering heat sprite like the shield on v5 Javelin |
| bullet | BulletType | null | Bullet type that is fired. Can be null |
| bulletAngle | float | 0.0 | Bullet angle parameters |
| bulletSpread | float | 0.0 | Bullet angle parameters |
| shootEffect | Effect | sparkShoot |  |
| parentizeEffects | boolean | false |  |
| shootSound | Sound | shootArc |  |
