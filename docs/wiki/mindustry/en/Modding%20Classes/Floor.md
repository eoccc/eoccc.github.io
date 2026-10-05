# Floor

## Floor

*extends Block*

| field | type | default | notes |
|---|---|---|---|
| edge | String | "stone" | edge fallback, used mainly for ores |
| speedMultiplier | float | 1.0 | Multiplies unit velocity by this when walked on. |
| dragMultiplier | float | 1.0 | Multiplies unit drag by this when walked on. |
| damageTaken | float | 0.0 | Damage taken per tick on this tile. |
| drownTime | float | 0.0 | How many ticks it takes to drown on this. 0 to disable. |
| walkEffect | Effect | none | Effect when walking on this floor. |
| walkSound | Sound | none | Sound made when walking. |
| walkSoundVolume | float | 0.1 | Volume of sound made when walking. |
| walkSoundPitchMin | float | 0.8 | Volume of sound made when walking. |
| walkSoundPitchMax | float | 1.2 | Volume of sound made when walking. |
| drownUpdateEffect | Effect | bubble | Effect displayed when drowning on this floor. |
| status | StatusEffect | none | Status effect applied when walking on. |
| statusDuration | float | 60.0 | Intensity of applied status effect. |
| liquidDrop | Liquid | null | liquids that drop from this block, used for pumps. |
| liquidMultiplier | float | 1.0 | Multiplier for pumped liquids, used for deep water. |
| isLiquid | boolean | false | whether this block is liquid. |
| overlayAlpha | float | 0.65 | for liquid floors, this is the opacity of the overlay drawn on top. |
| supportsOverlay | boolean | false | whether this floor supports an overlay floor |
| supportsBeingOverlaid | boolean | true | if false, this floor can't be used as an overlay (liquid underlay), even if the floor it's placed on supports it |
| shallow | boolean | false | shallow water flag used for generation |
| blendGroup | Block | this | Group of blocks that this block does not draw edges on. |
| oreDefault | boolean | false | Whether this ore generates in maps by default. |
| oreScale | float | 24.0 | Ore generation params. |
| oreThreshold | float | 0.828 | Ore generation params. |
| wall | Block | air | Wall variant of this block. May be Blocks.air if not found. |
| decoration | Block | air | Decoration block. Usually a rock. May be air. |
| canShadow | boolean | true | Whether units can draw shadows over this. |
| forceDrawLight | boolean | false | If true, this floor ignores the obstructsLight flag of overlays. |
| needsSurface | boolean | true | Whether this overlay needs a surface to be on. False for floating blocks, like spawns. |
| allowCorePlacement | boolean | false | If true, cores can be placed on this floor. |
| wallOre | boolean | false | If true, this ore is allowed on walls. |
| blendId | int | -1 | Actual ID used for blend groups. Internal. |
| tilingVariants | int | 0 | If >0, this floor is drawn as parts of a large texture. |
| autotile | boolean | false | If true, this floor uses autotiling; variants are not supported. See https://github.com/GglLfr/tile-gen |
| autotileMidVariants | int | 1 | If >1, the middle region of the autotile has random variants. |
| autotileVariants | int | 1 | Variants of the main autotile sprite. |
| drawEdgeIn | boolean | true | If true (default), this floor will draw edges of other floors on itself. |
| drawEdgeOut | boolean | true | If true (default), this floor will draw its edges onto other floors. |
