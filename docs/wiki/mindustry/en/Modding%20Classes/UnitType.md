# UnitType

## UnitType

*extends UnlockableContent*

| field | type | default | notes |
|---|---|---|---|
| envRequired | int | 0 | Environmental flags that are *all* required for this unit to function. 0 = any environment |
| envEnabled | int | 1 | The environment flags that this unit can function in. If the env matches any of these, it will be enabled. |
| envDisabled | int | 16 | The environment flags that this unit *cannot* function in. If the env matches any of these, it will explode or be disabled. |
| speed | float | 1.1 | movement speed (world units/t) |
| boostMultiplier | float | 1.0 | multiplier for speed when boosting |
| floorMultiplier | float | 1.0 | how affected this unit is by terrain |
| rotateSpeed | float | 5.0 | body rotation speed in degrees/t |
| baseRotateSpeed | float | 5.0 | mech base rotation speed in degrees/t |
| drag | float | 0.3 | movement drag as fraction |
| accel | float | 0.5 | acceleration as fraction of speed |
| hitSize | float | 6.0 | size of one side of the hitbox square |
| deathShake | float | -1.0 | shake on unit death |
| stepShake | float | -1.0 | shake on each step for leg/mech units |
| rippleScale | float | 1.0 | ripple / dust size for legged units |
| riseSpeed | float | 0.08 | boosting rise speed as fraction |
| descentSpeed | float | 0.08 | boosting descent speed as fraction |
| fallSpeed | float | 0.018 | how fast this unit falls upon death |
| missileAccelTime | float | 0.0 | how many ticks it takes this missile to accelerate to full speed |
| health | float | 200.0 | raw health amount |
| armor | float | 0.0 | incoming damage is reduced by this amount |
| range | float | -1.0 | minimum range of any weapon; used for approaching targets. can be overridden by setting a value > 0. |
| maxRange | float | -1.0 | maximum range of any weapon |
| mineRange | float | 70.0 | range at which this unit can mine ores |
| buildRange | float | 220.0 | range at which this unit can build |
| circleTargetRadius | float | 80.0 | radius for circleTarget, if true |
| crashDamageMultiplier | float | 1.0 | multiplier for damage this (flying) unit deals when crashing on enemy things |
| wreckHealthMultiplier | float | 0.25 | multiplier for health that this flying unit has for its wreck, based on its max health. |
| dpsEstimate | float | -1.0 | a VERY ROUGH estimate of unit DPS; initialized in init() |
| clipSize | float | -1.0 | graphics clipping size;  0, this is the scale for how far away legs are from the body horizontally |
| legMaxLength | float | 1.75 | maximum length of an individual leg as fraction of real length |
| legMinLength | float | 0.0 | minimum length of an individual leg as fraction of real length |
| legSplashDamage | float | 0.0 | splash damage dealt when a leg touches the ground |
| legSplashRange | float | 5.0 | splash damage radius of legs |
| baseLegStraightness | float | 0.0 | how straight the leg base/origin is (0 = circular, 1 = line) |
| legStraightness | float | 0.0 | how straight the leg outward angles are (0 = circular, 1 = horizontal line) |
| legBaseUnder | boolean | false | If true, the base (further away) leg region is drawn under instead of over. |
| lockLegBase | boolean | false | If true, legs are locked to the base of the unit instead of being on an implicit rotating "mount". |
| legContinuousMove | boolean | false | If true, legs always try to move around even when the unit is not moving (leads to more natural behavior) |
| flipBackLegs | boolean | true | TODO neither of these appear to do much |
| flipLegSide | boolean | false | TODO neither of these appear to do much |
| emitWalkSound | boolean | true | Whether to emit a splashing noise in water. |
| emitWalkEffect | boolean | true | Whether to emit a splashing effect in water (fasle implies emitWalkSound false). |
| mechLandShake | float | 0.0 | screen shake amount for when this mech lands after boosting |
| mechSideSway | float | 0.54 | parameters for mech swaying animation |
| mechFrontSway | float | 0.1 | parameters for mech swaying animation |
| mechStride | float | -1.0 | parameters for mech swaying animation |
| mechStepParticles | boolean | false | whether particles are created when this mech takes a step |
| mechLegColor | Color | 6e7080ff | color that legs change to when moving, to simulate depth |
| treadRects | Rect[] | [] | list of treads as rectangles in IMAGE COORDINATES, relative to the center. these are mirrored. |
| treadFrames | int | 18 | number of frames of movement in a tread |
| treadPullOffset | int | 0 | how much of a top part of a tread sprite is "cut off" relative to the pattern; this is corrected for |
| crushFragile | boolean | false | if true, 'fragile' blocks will instantly be crushed in a 1x1 area around the tank |
| segments | int | 0 | number of independent segments |
| segmentUnits | int | 1 | TODO wave support - for multi-unit segmented units, this is the number of independent units that are spawned |
| segmentUnit | UnitType | null | unit spawned in segments; if null, the same unit is used |
| segmentEndUnit | UnitType | null | unit spawned at the end; if null, the segment unit is used |
| segmentLayerOrder | boolean | true | true - parent segments are on higher layers; false - parent segments are on lower layers than head |
| segmentMag | float | 2.0 | magnitude of sine offset between segments |
| segmentScl | float | 4.0 | scale of sine offset between segments |
| segmentPhase | float | 5.0 | index multiplier of sine offset between segments |
| segmentRotSpeed | float | 1.0 | how fast each segment moves towards the next one |
| segmentMaxRot | float | 30.0 | maximum difference between segment angles |
| segmentSpacing | float | -1.0 | spacing between separate unit segments (only used for multi-unit worms) |
| segmentRotationRange | float | 80.0 | rotation between segments is clamped to this range |
| crawlSlowdown | float | 0.5 | speed multiplier this unit will have when crawlSlowdownFrac is met. |
| crushDamage | float | 0.0 | damage dealt to blocks under this tank/crawler every frame. |
| crawlSlowdownFrac | float | 0.55 | the fraction of solids under this block necessary for it to reach crawlSlowdown. |
| lifetime | float | 300.0 | lifetime of this missile. |
| homingDelay | float | 10.0 | ticks that must pass before this missile starts homing. |
| baseRegion | TextureRegion | null |  |
| legRegion | TextureRegion | null |  |
| region | TextureRegion | null |  |
| previewRegion | TextureRegion | null |  |
| shadowRegion | TextureRegion | null |  |
| cellRegion | TextureRegion | null |  |
| itemCircleRegion | TextureRegion | null |  |
| softShadowRegion | TextureRegion | null |  |
| jointRegion | TextureRegion | null |  |
| footRegion | TextureRegion | null |  |
| legBaseRegion | TextureRegion | null |  |
| baseJointRegion | TextureRegion | null |  |
| outlineRegion | TextureRegion | null |  |
| treadRegion | TextureRegion | null |  |
| mineLaserRegion | TextureRegion | null |  |
| mineLaserEndRegion | TextureRegion | null |  |
| wreckRegions | TextureRegion[] | null |  |
| segmentRegions | TextureRegion[] | null |  |
| segmentCellRegions | TextureRegion[] | null |  |
| segmentOutlineRegions | TextureRegion[] | null |  |
| treadRegions | TextureRegion[][] | null |  |
