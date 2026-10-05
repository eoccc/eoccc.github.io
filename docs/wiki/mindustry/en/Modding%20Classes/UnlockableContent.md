# UnlockableContent

## UnlockableContent

*extends MappableContent*

Base interface for an unlockable content type.

| field | type | default | notes |
|---|---|---|---|
| stats | Stats | new Stats() | Stat storage for this content. Initialized on demand. |
| localizedName | String |  | Localized, formal name. Never null. Set to internal name if not found in bundle. |
| description | String | null | Localized description & details. May be null. |
| details | String | null | Localized description & details. May be null. |
| credit | String | null | Localized description & details. May be null. |
| alwaysUnlocked | boolean | false | Whether this content is always unlocked in the tech tree. |
| inlineDescription | boolean | true | Whether to show the description in the research dialog preview. |
| hideDetails | boolean | true | Whether details are hidden in custom games if this hasn't been unlocked in campaign mode. |
| hideDatabase | boolean | false | Whether this is hidden from the Core Database. |
| generateIcons | boolean | true | If false, all icon generation is disabled for this content; createIcons is not called. |
| selectionSize | float | 24.0 | How big the content appears in certain selection menus |
| uiIcon | TextureRegion | null | Icon of the content to use in UI. |
| fullIcon | TextureRegion | null | Icon of the full content. Unscaled. |
| fullOverride | String | "" | Override for the full icon. Useful for mod content with duplicate icons. Overrides any other full icon. |
| allDatabaseTabs | boolean | false | If true, this content will appear in all database tabs. |
| shownPlanets | ObjectSet of Planet | [] | Planets that this content is made for. If empty, a planet is decided based on item requirements. Currently, this is only meaningful for blocks. |
| databaseTabs | ObjectSet of UnlockableContent | [] | Content - usually a planet - that dictates which database tab(s) this content will appear in. If nothing is defined, it will use the values in shownPlanets. If shownPlanets is also empty, it will use Serpulo as the "default" tab. |
| databaseCategory | String | null | Content category. Defines the primary category of content classification in core database. For example, "block", "liquid", "unit". Uses getContentType().name() as a fallback when the value is null or empty. |
| databaseTag | String | null | Category tags. Secondary category of content classification in core database. For example, "turret", "wall" under databaseCategory "block", "core-unit", "ground-unit" under databaseCategory "units". Uses "default" as a fallback when the value is null or empty. When using "default", no extra tag label are displayed. |
| techNode | TechNode | null | The tech tree node for this content, if applicable. Null if not part of a tech tree. |
| techNodes | Seq of TechNode | [] | Tech nodes for all trees that this content is part of. |
