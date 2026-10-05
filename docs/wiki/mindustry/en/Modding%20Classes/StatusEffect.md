# StatusEffect

Built-in constants:

`none` `burning` `freezing` `unmoving` `slow` `fast` `wet` `muddy` `melting` `sapped` `tarred` `overdrive` `overclock` `shielded` `shocked` `blasted` `corroded` `boss` `sporeSlowed` `disarmed` `electrified` `invincible` `dynamic`

## StatusEffect

*extends UnlockableContent*

| field | type | default | notes |
|---|---|---|---|
| damageMultiplier | float | 1.0 | Damage dealt by the unit with the effect. |
| healthMultiplier | float | 1.0 | Unit health multiplier. |
| speedMultiplier | float | 1.0 | Unit speed multiplier. |
| reloadMultiplier | float | 1.0 | Unit reload multiplier. |
| buildSpeedMultiplier | float | 1.0 | Unit build speed multiplier. |
| dragMultiplier | float | 1.0 | Unit drag multiplier. |
| transitionDamage | float | 0.0 | Damage dealt upon transition to an affinity. |
| disarm | boolean | false | Unit weapon(s) disabled. |
| damage | float | 0.0 | Damage per frame. |
| intervalDamageTime | float | 0.0 | Spacing (in ticks) between interval damage. <=0 to disable. |
| intervalDamage | float | 0.0 | Damage dealt by interval damage. |
| intervalDamagePierce | boolean | false | If true, interval damage is armor piercing. |
| effectChance | float | 0.15 | Chance of visual effect(s) appearing. |
| parentizeEffect | boolean | false | Should the effect be given a parent. |
| permanent | boolean | false | If true, the effect never disappears. |
| reactive | boolean | false | If true, this effect will only react with other effects and cannot be applied. |
| dynamic | boolean | false | Special flag for the dynamic effect type with custom stats - do not use. |
| show | boolean | true | Whether to show this effect in the database. |
| color | Color | ffffffff | Tint color of effect. |
| effect | Effect | none | Effect that happens randomly on top of the affected unit. |
| applyEffect | Effect | none | Effect that is displayed once when applied to a unit. |
| applyExtend | boolean | false | Whether the apply effect should display even if effect is already on the unit. |
| applyColor | Color | ffffffff | Tint color of apply effect. |
| parentizeApplyEffect | boolean | false | Should the apply effect be given a parent. |
| affinities | ObjectSet of StatusEffect | [] | Affinity & opposite values for stat displays. |
| opposites | ObjectSet of StatusEffect | [] | Affinity & opposite values for stat displays. |
| outline | boolean | true | Set to false to disable outline generation. |
