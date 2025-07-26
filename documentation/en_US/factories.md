## Factories

Usage example:
```ts
var a = location(1, 2, 3);
var b = vector(1, 2, 3);
var c = item("stone");
```

### Types of factories

The arguments indicate the types of values that you must pass to the factory to get the value.

Those arguments ending in `*` must be specified.

| **Name**     | **Description**   | **Arguments**                                                                                                                                                                                                     |
| ------------ | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `location()` | Location          | (`x`: number*, `y`: number*, `z`: number*, `yaw`: number, `pitch`: number)                                                                                                                                        |
| `item()`     | Item              | (`id`: text*, `name`: text, `count`: number, `lore`: list[text], `nbt`: minecraft_nbt(components data), `custom_tags`: dictionary)                                                                                |
| `sound()`    | Sound             | (`sound`: text*, `volume`: number, `pitch`: number, `variation`: text, `source`: marker(**RECORD**, **BLOCK**, **MASTER**, **VOICE**, **WEATHER**, **AMBIENT**, **NEUTRAL**, **HOSTILE**, **PLAYER**, **MUSIC**)) |
| `vector()`   | Vector            | (`x`: number*, `y`: number*, `z`: number*)                                                                                                                                                                        |
| `particle()` | Particle effect   | (`particle`: text*, `count`: number, `spread_x`: number, `spread_y`: number, `motion_x`: number, `motion_y`: number, `motion_z`: number, `material`: текст, `color`: number, `size`: number, `to_color`: number)  |
| `potion()`   | Potion            | (`potion`: text*, `amplifier`: number, `duration`: number)                                                                                                                                                        |