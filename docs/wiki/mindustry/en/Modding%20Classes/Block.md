# Block

## Block

*extends UnlockableContent*

| field | type | default | notes |
|---|---|---|---|
| hasItems | boolean | false | If true, buildings have an ItemModule. |
| hasLiquids | boolean | false | If true, buildings have a LiquidModule. |
| hasPower | boolean | false | If true, buildings have a PowerModule. |
| outputsLiquid | boolean | false | Flag for determining whether this block outputs liquid somewhere; used for connections. |
| consumesPower | boolean | true | Used by certain power blocks (nodes) to flag as non-consuming of power. True by default, even if this block has no power. |
| outputsPower | boolean | false | If true, this block is a generator that can produce power. |
| connectedPower | boolean | true | If false, power nodes cannot connect to this block. |
| conductivePower | boolean | false | If true, this block can conduct power like a cable. |
| outputsPayload | boolean | false | If true, this block can output payloads; affects blending. |
| acceptsUnitPayloads | boolean | false | If true, this block can input payloads. Affects unit payload enter and pathfinding behaviors. |
| acceptsPayload | boolean | false | If true, payloads will attempt to move into this block. |
| acceptsItems | boolean | false | Visual flag use for blending of certain transportation blocks. |
| alwaysAllowDeposit | boolean | false | If true, this block won't be affected by the onlyDepositCore rule. |
| allowedInPayloads | boolean | true | If false, this block cannot be placed in payloads. |
| depositCooldown | float | -1.0 | Cooldown, in seconds, applied to player item depositing when any item is deposited to this block. Overrides the itemDepositCooldown if non-negative. |
| separateItemCapacity | boolean | false | If true, all item capacities of this block are separate instead of pooled as one number. |
| itemCapacity | int | 10 | maximum items this block can carry (usually, this is per-type of item) |
| liquidCapacity | float | -1.0 | maximum total liquids this block can carry if hasLiquids = true. Default value is 10, scales with max liquid consumption in ConsumeLiquid |
| liquidPressure | float | 1.0 | higher numbers increase liquid output speed; TODO remove and replace with better liquids system |
| outputFacing | boolean | true | If true, this block outputs to its facing direction, when applicable. Used for blending calculations. |
| noSideBlend | boolean | false | if true, this block does not accept input from the sides (used for armored conveyors) |
| displayFlow | boolean | true | whether to display flow rate |
| inEditor | boolean | true | whether this block is visible in the editor |
| editorConfigurable | boolean | false | if true, {@link #buildEditorConfig(Table)} will be called for configuring this block in the editor. |
| lastConfig | Object | null | the last configuration value applied to this block. |
| saveConfig | boolean | false | whether to save the last config and apply it to newly placed blocks |
| copyConfig | boolean | true | whether to allow copying the config through middle click |
| clearOnDoubleTap | boolean | false | if true, double-tapping this configurable block clears configuration. |
| update | boolean | false | whether this block has a tile entity that updates |
| destructible | boolean | false | whether this block has health and can be destroyed. note that setting this to false does nothing if update = true! |
| unloadable | boolean | true | whether unloaders work on this block |
| isDuct | boolean | false | if true, this block acts a duct and will connect to armored ducts from the side. |
| allowResupply | boolean | false | whether units can resupply by taking items from this block |
| solid | boolean | false | whether this is solid |
| solidifes | boolean | false | whether this block CAN be solid. |
| teamPassable | boolean | false | if true, this counts as a non-solid block to this team. |
| underBullets | boolean | false | if true, this block cannot be hit by bullets unless explicitly targeted. |
| rotate | boolean | false | whether this is rotatable |
| rotateDraw | boolean | true | if rotate is true and this is false, the region won't rotate when drawing |
| rotateDrawEditor | boolean | true | if rotate is true and this is false, the region won't rotate when drawing in the editor |
| visualRotationOffset | float | 0.0 | visual rotation offset used in broken plan rendering |
| lockRotation | boolean | true | if rotate = false and this is true, rotation will be locked at 0 when placing (default); advanced use only |
| ignoreLineRotation | boolean | false | if true, this block won't face the line drag direction |
| invertFlip | boolean | false | if true, schematic flips with this block are inverted. |
| variants | int | 0 | number of different variant regions to use |
| drawArrow | boolean | true | whether to draw a rotation arrow - this does not apply to lines of blocks |
| drawTeamOverlay | boolean | true | whether to draw the team corner by default |
| saveData | boolean | false | for static blocks only: if true, tile data() is saved in world data. |
| breakable | boolean | false | whether you can break this with rightclick |
| unitMoveBreakable | boolean | false | if true, this block will be broken by certain units stepping/moving over it |
| rebuildable | boolean | true | whether to add this block to brokenblocks |
| privileged | boolean | false | if true, this logic-related block can only be used with privileged processors (or is one itself) |
| requiresWater | boolean | false | whether this block can only be placed on water |
| placeableLiquid | boolean | false | whether this block can be placed on any liquids, anywhere |
| placeablePlayer | boolean | true | whether this block can be placed directly by the player via PlacementFragment |
| placeableOn | boolean | true | whether this floor can be placed on. |
| insulated | boolean | false | whether this block has insulating properties. |
| squareSprite | boolean | true | whether the sprite is a full square. |
| absorbLasers | boolean | false | whether this block absorbs laser attacks. |
| enableDrawStatus | boolean | true | if false, the status is never drawn |
| drawDisabled | boolean | true | whether to draw disabled status |
| autoResetEnabled | boolean | true | whether to automatically reset enabled status after a logic block has not interacted for a while. |
| noUpdateDisabled | boolean | false | if true, the block stops updating when disabled |
| updateInUnits | boolean | true | if true, this block updates when it's a payload in a unit. |
| alwaysUpdateInUnits | boolean | false | if true, this block updates in payloads in units regardless of the experimental game rule |
| canPickup | boolean | true | @deprecated use allowedInPayloads instead |
| deconstructDropAllLiquid | boolean | false | if false, only incinerable liquids are dropped when deconstructing; otherwise, all liquids are dropped. |
| useColor | boolean | true | Whether to use this block's color in the minimap. Only used for overlays. |
| itemDrop | Item | null | item that drops from this block, used for drills |
| playerUnmineable | boolean | false | if true, this block cannot be mined by players. useful for annoying things like sand. |
| attributes | Attributes | new Attributes() | Affinities for floors. |
| scaledHealth | float | -1.0 | Health per square tile that this block occupies; essentially, this is multiplied by size * size. Overridden if health is > 0. If () | Cost multipliers per-item. |
| researchCost | ItemStack[] | null | Override for research cost. Uses multipliers above and building requirements if not set. |
| forceTeam | Team | null | If set, all blocks will be forced to be this team. |
| instantTransfer | boolean | false | Whether this block has instant transfer. |
| maxConsecutive | int | 2 | Maximum number of instantTransfer consecutive blocks. |
| quickRotate | boolean | true | Whether you can rotate this block after it is placed. |
| allowDerelictRepair | boolean | true | If true, this derelict block can be repair by clicking it. |
| subclass | Class of ? | class mindustry.world.Block | Main subclass. Non-anonymous. |
| selectScroll | float | 0.0 | Scroll position for certain blocks. |
| buildType | Prov of Building | null | Building that is created for this block. Initialized in init() via reflection. Set manually if modded. |
| configurations | ObjectMap of Class of ?, Cons2 | {} | Configuration handlers by type. |
| itemFilter | boolean[] | [] | Consumption filters. |
| liquidFilter | boolean[] | [] | Consumption filters. |
| consumers | Consume[] | [] | Array of consumers used by this block. Only populated after init(). |
| optionalConsumers | Consume[] | [] | Array of consumers used by this block. Only populated after init(). |
| nonOptionalConsumers | Consume[] | [] | Array of consumers used by this block. Only populated after init(). |
| updateConsumers | Consume[] | [] | Array of consumers used by this block. Only populated after init(). |
| hasConsumers | boolean | false | Set to true if this block has any consumers in its array. |
| consPower | ConsumePower | null | The single power consumer, if applicable. |
| regionRotated1 | int | -1 | Regions indexes from icons() that are rotated. If either of these is not -1, other regions won't be rotated in ConstructBlocks. |
| regionRotated2 | int | -1 | Regions indexes from icons() that are rotated. If either of these is not -1, other regions won't be rotated in ConstructBlocks. |
| region | TextureRegion | null |  |
| customShadowRegion | TextureRegion | null |  |
| teamRegion | TextureRegion | null |  |
| teamRegions | TextureRegion[] | null |  |
| variantRegions | TextureRegion[] | null |  |
| variantShadowRegions | TextureRegion[] | null |  |
| dumpTime | int | 5 | How often to try dumping items in ticks, e.g. 5 = 12 times/sec |
