<h2 id=entity>
  <code>entity</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

| **ID**             | **Name**         |
|--------------------|------------------|
| `<current>`        | Current Target   |
| `<default_entity>` | Default Entity   |
| `<killer_entity>`  | Killer           |
| `<damager_entity>` | Attacking Entity |
| `<shooter_entity>` | Shooter          |
| `<projectile>`     | Projectile Arrow |
| `<victim_entity>`  | Victim           |
| `<random_entity>`  | Random Entity    |
| `<all_mobs>`       | All Mobs         |
| `<all_entities>`   | All Entities     |
| `<last_entity>`    | Last Entity      |


**Important:** These selectors are only available for actions from object `entity`.

<h3 id=entity_attach_lead>
  <code>entity::attach_lead</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Attach Lead\
**Action type:** Action without value\
**Description:** Tethers an entity to a fence or entity.\
**Additional info:**\
&nbsp;&nbsp;If the lead is more than 10 blocks long, the lead will break.

**Usage example:**
```ts
entity::attach_lead("name_or_uuid", location(0,0,0,0,0));

//Or dry by keywords

entity::attach_lead(name_or_uuid="name_or_uuid", location=location(0,0,0,0,0));
```

**Arguments:**

| ID           | Type     | Description         |
|--------------|----------|---------------------|
| name_or_uuid | Text     | Entity name or UUID |
| location     | Location | Fence Location      |

<h3 id=entity_celar_potion_effects>
  <code>entity::clear_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear All Potion Effects\
**Action type:** Action without value\
**Description:** Clears all effects on an entity.

**Usage example:**
```ts
entity::clear_potion_effects();
```

<h3 id=entity_clear_merchant_recipes>
  <code>entity::clear_merchant_recipes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Merchant Recipes\
**Action type:** Action without value\
**Description:** Clears all trades to a Villager.\
**Work_with:**\
&nbsp;&nbsp;Villagers\
&nbsp;&nbsp;Wandering Traders

**Usage example:**
```ts
entity::clear_merchant_recipes();
```

<h3 id=entity_complete_using_active_item>
  <code>entity::complete_using_active_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_complete_using_active_item.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_complete_using_active_item.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_complete_using_active_item.work_with.living_entity

**Usage example:**
```ts
entity::complete_using_active_item();
```

<h3 id=entity_damage>
  <code>entity::damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Deal Damage\
**Action type:** Action without value\
**Description:** Deals damage to an entity.

**Usage example:**
```ts
entity::damage(1, "source");

//Or dry by keywords

entity::damage(damage=1, source="source");
```

**Arguments:**

| ID     | Type   | Description                         |
|--------|--------|-------------------------------------|
| damage | Number | Damage Amount                       |
| source | Text   | Damage Source (Entity Name or UUID) |

<h3 id=entity_disguise_as_block>
  <code>entity::disguise_as_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Block\
**Action type:** Action without value\
**Description:** Disguise an entity as a block.

**Usage example:**
```ts
entity::disguise_as_block("minecraft:oak_log[axis=x]");

//Or dry by keywords

entity::disguise_as_block(block="minecraft:oak_log[axis=x]");
```

**Arguments:**

| ID    | Type  | Description    |
|-------|-------|----------------|
| block | Block | Disguise Block |

<h3 id=entity_disguise_as_entity>
  <code>entity::disguise_as_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Entity\
**Action type:** Action without value\
**Description:** Disguise an entity as an entity.

**Usage example:**
```ts
entity::disguise_as_entity(item("stick"));

//Or dry by keywords

entity::disguise_as_entity(entity_type=item("stick"));
```

**Arguments:**

| ID          | Type | Description        |
|-------------|------|--------------------|
| entity_type | Item | Entity to Disguise |

<h3 id=entity_disguise_as_item>
  <code>entity::disguise_as_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Item\
**Action type:** Action without value\
**Description:** Disguises an entity as an item.

**Usage example:**
```ts
entity::disguise_as_item(item("stick"));

//Or dry by keywords

entity::disguise_as_item(item=item("stick"));
```

**Arguments:**

| ID   | Type | Description   |
|------|------|---------------|
| item | Item | Disguise Item |

<h3 id=entity_disguise_as_player>
  <code>entity::disguise_as_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Player\
**Action type:** Action without value\
**Description:** Disguises an entity as a player.

**Usage example:**
```ts
entity::disguise_as_player("name_or_uuid", "display_name", "MOJANG");

//Or dry by keywords

entity::disguise_as_player(name_or_uuid="name_or_uuid", display_name="display_name", server_type="MOJANG");
```

**Arguments:**

| ID           | Type                                                             | Description         |
|--------------|------------------------------------------------------------------|---------------------|
| name_or_uuid | Text                                                             | Name or UUID        |
| display_name | Text                                                             | Entity Display Name |
| server_type  | Marker<br/>**MOJANG** - Mojang Skin<br/>**SERVER** - JustMC Skin | Skin Server Type    |

<h3 id=entity_dummy>
  <code>entity::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Action type:** Action without value\
**Description:** ...

**Usage example:**
```ts
entity::dummy();
```

<h3 id=entity_eat_grass>
  <code>entity::eat_grass</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Eat Grass\
**Action type:** Action without value\
**Description:** Makes a sheep eat grass.\
**Work_with:**\
&nbsp;&nbsp;Sheep

**Usage example:**
```ts
entity::eat_grass();
```

<h3 id=entity_eat_target>
  <code>entity::eat_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Eat Target\
**Action type:** Action without value\
**Description:** Sets a target for an entity to eat.\
**Work_with:**\
&nbsp;&nbsp;Toads

**Usage example:**
```ts
entity::eat_target("name_or_uuid");

//Or dry by keywords

entity::eat_target(name_or_uuid="name_or_uuid");
```

**Arguments:**

| ID           | Type | Description                |
|--------------|------|----------------------------|
| name_or_uuid | Text | Name or UUID of the target |

<h3 id=entity_explode>
  <code>entity::explode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Explode\
**Action type:** Action without value\
**Description:** Causes an entity to explode.\
**Work_with:**\
&nbsp;&nbsp;Creepers\
&nbsp;&nbsp;Dynamite\
&nbsp;&nbsp;Fireworks

**Usage example:**
```ts
entity::explode();
```

<h3 id=entity_face_location>
  <code>entity::face_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Face to Location\
**Action type:** Action without value\
**Description:** Turns an entity towards a location.

**Usage example:**
```ts
entity::face_location(location(0,0,0,0,0));

//Or dry by keywords

entity::face_location(location=location(0,0,0,0,0));
```

**Arguments:**

| ID       | Type     | Description |
|----------|----------|-------------|
| location | Location | Location    |

<h3 id=entity_get_attribute>
  <code>entity::get_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_get_attribute.name\
**Action type:** An action that returns a value\
**Description:** creative_plus.action.entity_get_attribute.description

**Usage example:**
```ts
`variable` = entity::get_attribute("GENERIC_MAX_HEALTH", "VALUE");

//Or dry by positionals

entity::get_attribute(`variable`, "GENERIC_MAX_HEALTH", "VALUE");

//Or dry by keywords

entity::get_attribute(variable=`variable`, attribute_type="GENERIC_MAX_HEALTH", return_value="VALUE");
```

**Arguments:**

| ID             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| variable       | Variable\[Number\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | creative_plus.action.entity_get_attribute.argument.variable.name       |
| attribute_type | Marker<br/>**GENERIC_MAX_HEALTH** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_max_health.name<br/>**GENERIC_MAX_ABSORPTION** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_max_absorption.name<br/>**GENERIC_FOLLOW_RANGE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_follow_range.name<br/>**GENERIC_KNOCKBACK_RESISTANCE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_knockback_resistance.name<br/>**GENERIC_MOVEMENT_SPEED** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_movement_speed.name<br/>**GENERIC_FLYING_SPEED** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_flying_speed.name<br/>**GENERIC_ATTACK_DAMAGE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_attack_damage.name<br/>**GENERIC_ATTACK_KNOCKBACK** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_attack_knockback.name<br/>**GENERIC_ATTACK_SPEED** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_attack_speed.name<br/>**GENERIC_ARMOR** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_armor.name<br/>**GENERIC_ARMOR_TOUGHNESS** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_armor_toughness.name<br/>**GENERIC_LUCK** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_luck.name<br/>**GENERIC_JUMP_STRENGTH** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_jump_strength.name<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_fall_damage_multiplier.name<br/>**GENERIC_SAFE_FALL_DISTANCE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_safe_fall_distance.name<br/>**GENERIC_SCALE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_scale.name<br/>**GENERIC_STEP_HEIGHT** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_step_height.name<br/>**GENERIC_GRAVITY** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_gravity.name<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.player_block_interaction_range.name<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.player_entity_interaction_range.name<br/>**PLAYER_BLOCK_BREAK_SPEED** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.player_block_break_speed.name<br/>**GENERIC_BURNING_TIME** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_burning_time.name<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_explosion_knockback_resistance.name<br/>**GENERIC_MOVEMENT_EFFICIENCY** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_movement_efficiency.name<br/>**PLAYER_MINING_EFFICIENCY** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.player_mining_efficiency.name<br/>**PLAYER_SNEAKING_SPEED** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.player_sneaking_speed.name<br/>**PLAYER_SUBMERGED_MINING_SPEED** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.player_submerged_mining_speed.name<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.player_sweeping_damage_ratio.name<br/>**GENERIC_OXYGEN_BONUS** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_oxygen_bonus.name<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.generic_water_movement_efficiency.name<br/>**TEMP_RANGE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.temp_range.name<br/>**WAYPOINT_TRANSMIT_RANGE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.waypoint_transmit_range.name<br/>**WAYPOINT_RECEIVE_RANGE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.waypoint_receive_range.name<br/>**CAMERA_DISTANCE** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.camera_distance.name<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - creative_plus.action.entity_get_attribute.argument.attribute_type.enum.zombie_spawn_reinforcements.name | creative_plus.action.entity_get_attribute.argument.attribute_type.name |
| return_value   | Marker<br/>**VALUE** - creative_plus.action.entity_get_attribute.argument.return_value.enum.value.name<br/>**BASE_VALUE** - creative_plus.action.entity_get_attribute.argument.return_value.enum.base_value.name<br/>**DEFAULT_VALUE** - creative_plus.action.entity_get_attribute.argument.return_value.enum.default_value.name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | creative_plus.action.entity_get_attribute.argument.return_value.name   |

<h3 id=entity_get_custom_tag>
  <code>entity::get_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Custom Tag\
**Action type:** An action that returns a value\
**Description:** Gets a creature's custom nbt tag.

**Usage example:**
```ts
`variable` = entity::get_custom_tag("name", "any value");

//Or dry by positionals

entity::get_custom_tag(`variable`, "name", "any value");

//Or dry by keywords

entity::get_custom_tag(variable=`variable`, name="name", default="any value");
```

**Arguments:**

| ID       | Type                  | Description        |
|----------|-----------------------|--------------------|
| variable | Variable\[Any Value\] | Variable to Assign |
| name     | Text                  | Tag name           |
| default  | Any Value             | Default value      |

<h3 id=entity_get_equipment_item>
  <code>entity::get_equipment_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_get_equipment_item.name\
**Action type:** An action that returns a value\
**Description:** creative_plus.action.entity_get_equipment_item.description

**Usage example:**
```ts
`variable` = entity::get_equipment_item("HAND");

//Or dry by positionals

entity::get_equipment_item(`variable`, "HAND");

//Or dry by keywords

entity::get_equipment_item(variable=`variable`, slot="HAND");
```

**Arguments:**

| ID       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                           |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| variable | Variable\[Item\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | creative_plus.action.entity_get_equipment_item.argument.variable.name |
| slot     | Marker<br/>**HAND** - creative_plus.action.entity_get_equipment_item.argument.slot.enum.hand.name<br/>**OFF_HAND** - creative_plus.action.entity_get_equipment_item.argument.slot.enum.off_hand.name<br/>**FEET** - creative_plus.action.entity_get_equipment_item.argument.slot.enum.feet.name<br/>**LEGS** - creative_plus.action.entity_get_equipment_item.argument.slot.enum.legs.name<br/>**CHEST** - creative_plus.action.entity_get_equipment_item.argument.slot.enum.chest.name<br/>**HEAD** - creative_plus.action.entity_get_equipment_item.argument.slot.enum.head.name<br/>**BODY** - creative_plus.action.entity_get_equipment_item.argument.slot.enum.body.name<br/>**SADDLE** - creative_plus.action.entity_get_equipment_item.argument.slot.enum.saddle.name | creative_plus.action.entity_get_equipment_item.argument.slot.name     |

<h3 id=entity_get_nbt>
  <code>entity::get_nbt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_get_nbt.name\
**Action type:** An action that returns a value\
**Description:** creative_plus.action.entity_get_nbt.description

**Usage example:**
```ts
`variable` = entity::get_nbt("path", "ANY_VALUE");

//Or dry by positionals

entity::get_nbt(`variable`, "path", "ANY_VALUE");

//Or dry by keywords

entity::get_nbt(variable=`variable`, path="path", value_type="ANY_VALUE");
```

**Arguments:**

| ID         | Type                                                                                                                                                                                                     | Description                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| variable   | Variable\[Any Value\]                                                                                                                                                                                    | creative_plus.action.entity_get_nbt.argument.variable.name   |
| path       | Text                                                                                                                                                                                                     | creative_plus.action.entity_get_nbt.argument.path.name       |
| value_type | Marker<br/>**ANY_VALUE** - creative_plus.action.entity_get_nbt.argument.value_type.enum.any_value.name<br/>**NBT_STRING** - creative_plus.action.entity_get_nbt.argument.value_type.enum.nbt_string.name | creative_plus.action.entity_get_nbt.argument.value_type.name |

<h3 id=entity_give_potion_effects>
  <code>entity::give_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give Potion Effect\
**Action type:** Action without value\
**Description:** Gives the selected effects to the creature.

**Usage example:**
```ts
entity::give_potion_effects([potion("slow_falling"), potion("slow_falling")], "FALSE", "FALSE", "AMBIENT");

//Or dry by keywords

entity::give_potion_effects(potions=[potion("slow_falling"), potion("slow_falling")], overwrite="FALSE", show_icon="FALSE", particle_mode="AMBIENT");
```

**Arguments:**

| ID            | Type                                                                           | Description                                                  |
|---------------|--------------------------------------------------------------------------------|--------------------------------------------------------------|
| potions       | Array\[Potion\]                                                                | Effects to Give<br/>The argument supports list decomposition |
| overwrite     | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes                                 | Overwrite existing effects                                   |
| show_icon     | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes                                 | Show Effect Icon                                             |
| particle_mode | Marker<br/>**AMBIENT** - Transparent<br/>**NONE** - None<br/>**REGULAR** - Yes | Give Particles                                               |

<h3 id=entity_heal>
  <code>entity::heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Heal Entity\
**Action type:** Action without value\
**Description:** Heals an entity.

**Usage example:**
```ts
entity::heal(1);

//Or dry by keywords

entity::heal(heal=1);
```

**Arguments:**

| ID   | Type   | Description                   |
|------|--------|-------------------------------|
| heal | Number | Amount of Half Hearts to Heal |

<h3 id=entity_ignite_creeper>
  <code>entity::ignite_creeper</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ignite Creeper\
**Action type:** Action without value\
**Description:** Sets a creeper on fire, causing it to explode after a certain period.\
**Work_with:**\
&nbsp;&nbsp;Creepers

**Usage example:**
```ts
entity::ignite_creeper();
```

<h3 id=entity_jump>
  <code>entity::jump</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Jump\
**Action type:** Action without value\
**Description:** Makes an entity jump.\
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:**
```ts
entity::jump();
```

<h3 id=entity_launch_forward>
  <code>entity::launch_forward</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Forward\
**Action type:** Action without value\
**Description:** Launches an entity forward or backward in the direction it is facing based on its power.

**Usage example:**
```ts
entity::launch_forward(1, "FALSE", "YAW");

//Or dry by keywords

entity::launch_forward(power=1, increment="FALSE", launch_axis="YAW");
```

**Arguments:**

| ID          | Type                                                                  | Description              |
|-------------|-----------------------------------------------------------------------|--------------------------|
| power       | Number                                                                | Forward Force            |
| increment   | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                | Consider current inertia |
| launch_axis | Marker<br/>**YAW** - Horizontal Only<br/>**YAW_AND_PITCH** - All Axis | Launch Axis              |

<h3 id=entity_launch_projectile>
  <code>entity::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Projectile\
**Action type:** Action without value\
**Description:** Launch a projectile from an entity's location.

**Usage example:**
```ts
entity::launch_projectile(item("stick"), location(0,0,0,0,0), "name", 1, 2, particle("fire"));

//Or dry by keywords

entity::launch_projectile(projectile=item("stick"), location=location(0,0,0,0,0), name="name", speed=1, inaccuracy=2, trail=particle("fire"));
```

**Arguments:**

| ID         | Type            | Description                                                   |
|------------|-----------------|---------------------------------------------------------------|
| projectile | Item            | Projectile to Launch                                          |
| location   | Location        | Launch Location                                               |
| name       | Text            | Projectile Name                                               |
| speed      | Number          | Projectile Speed                                              |
| inaccuracy | Number          | Projectile deflection (0 to make the projectile fly straight) |
| trail      | Particle Effect | The trail the projectile will leave                           |

<h3 id=entity_launch_to_location>
  <code>entity::launch_to_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch To Location\
**Action type:** Action without value\
**Description:** Launches creatures to the selected location.

**Usage example:**
```ts
entity::launch_to_location(location(0,0,0,0,0), 1, "FALSE");

//Or dry by keywords

entity::launch_to_location(location=location(0,0,0,0,0), power=1, increment="FALSE");
```

**Arguments:**

| ID        | Type                                                   | Description              |
|-----------|--------------------------------------------------------|--------------------------|
| location  | Location                                               | End Position             |
| power     | Number                                                 | Launch Power             |
| increment | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Consider current inertia |

<h3 id=entity_launch_up>
  <code>entity::launch_up</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Up\
**Action type:** Action without value\
**Description:** Tosses an entity up or down based on strength.

**Usage example:**
```ts
entity::launch_up(1, "FALSE");

//Or dry by keywords

entity::launch_up(power=1, increment="FALSE");
```

**Arguments:**

| ID        | Type                                                   | Description              |
|-----------|--------------------------------------------------------|--------------------------|
| power     | Number                                                 | Power                    |
| increment | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Consider current inertia |

<h3 id=entity_leave_vehicle>
  <code>entity::leave_vehicle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dismount\
**Action type:** Action without value\
**Description:** Dismounts an entity from another entity or vehicle.

**Usage example:**
```ts
entity::leave_vehicle();
```

<h3 id=entity_mimic_disguise_from_entity>
  <code>entity::mimic_disguise_from_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_mimic_disguise_from_entity.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_mimic_disguise_from_entity.description

**Usage example:**
```ts
entity::mimic_disguise_from_entity("name_or_uuid", "TRUE", "TRUE");

//Or dry by keywords

entity::mimic_disguise_from_entity(name_or_uuid="name_or_uuid", include_disguise="TRUE", remove_original_entity="TRUE");
```

**Arguments:**

| ID                     | Type                                                                                                                                                                                                                                               | Description                                                                                 |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| name_or_uuid           | Text                                                                                                                                                                                                                                               | creative_plus.action.entity_mimic_disguise_from_entity.argument.name_or_uuid.name           |
| include_disguise       | Marker<br/>**TRUE** - creative_plus.action.entity_mimic_disguise_from_entity.argument.include_disguise.enum.true.name<br/>**FALSE** - creative_plus.action.entity_mimic_disguise_from_entity.argument.include_disguise.enum.false.name             | creative_plus.action.entity_mimic_disguise_from_entity.argument.include_disguise.name       |
| remove_original_entity | Marker<br/>**TRUE** - creative_plus.action.entity_mimic_disguise_from_entity.argument.remove_original_entity.enum.true.name<br/>**FALSE** - creative_plus.action.entity_mimic_disguise_from_entity.argument.remove_original_entity.enum.false.name | creative_plus.action.entity_mimic_disguise_from_entity.argument.remove_original_entity.name |

<h3 id=entity_modify_piglin_barter_materials>
  <code>entity::modify_piglin_barter_materials</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Modify Piglin Barter Materials\
**Action type:** Action without value\
**Description:** Modify the items a Piglin gives after bartering.\
**Additional info:**\
&nbsp;&nbsp;You cannot modify the items a Piglin gives by default.\
**Work_with:**\
&nbsp;&nbsp;Piglin

**Usage example:**
```ts
entity::modify_piglin_barter_materials([item("stick"), item("stick")], "ADD");

//Or dry by keywords

entity::modify_piglin_barter_materials(materials=[item("stick"), item("stick")], modification_mode="ADD");
```

**Arguments:**

| ID                | Type                                             | Description                                            |
|-------------------|--------------------------------------------------|--------------------------------------------------------|
| materials         | Array\[Item\]                                    | Materials<br/>The argument supports list decomposition |
| modification_mode | Marker<br/>**ADD** - Add<br/>**REMOVE** - Remove | Modification mode                                      |

<h3 id=entity_modify_piglin_interested_materials>
  <code>entity::modify_piglin_interested_materials</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Modify Piglin Interested Materials\
**Action type:** Action without value\
**Description:** Modify the items a Piglin is interested in.\
**Additional info:**\
&nbsp;&nbsp;You cannot modify the items a Piglin is interested in by default.\
**Work_with:**\
&nbsp;&nbsp;Piglin

**Usage example:**
```ts
entity::modify_piglin_interested_materials([item("stick"), item("stick")], "ADD");

//Or dry by keywords

entity::modify_piglin_interested_materials(materials=[item("stick"), item("stick")], modification_mode="ADD");
```

**Arguments:**

| ID                | Type                                             | Description                                            |
|-------------------|--------------------------------------------------|--------------------------------------------------------|
| materials         | Array\[Item\]                                    | Materials<br/>The argument supports list decomposition |
| modification_mode | Marker<br/>**ADD** - Add<br/>**REMOVE** - Remove | Modification mode                                      |

<h3 id=entity_move_to_location>
  <code>entity::move_to_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Move To Location\
**Action type:** Action without value\
**Description:** Instructs the entity AI to always find its way to a certain location at a certain speed.\
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:**
```ts
entity::move_to_location(location(0,0,0,0,0), 1);

//Or dry by keywords

entity::move_to_location(location=location(0,0,0,0,0), speed=1);
```

**Arguments:**

| ID       | Type     | Description          |
|----------|----------|----------------------|
| location | Location | Destination Location |
| speed    | Number   | Movement Speed       |

<h3 id=entity_move_to_location_stop>
  <code>entity::move_to_location_stop</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Stop Moving To Location\
**Action type:** Action without value\
**Description:** Stops an entity moving to a location.\
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:**
```ts
entity::move_to_location_stop();
```

<h3 id=entity_play_damage_animation>
  <code>entity::play_damage_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Damage Animation\
**Action type:** Action without value\
**Description:** Displays an entity damage animation.

**Usage example:**
```ts
entity::play_damage_animation("CRITICAL_DAMAGE");

//Or dry by keywords

entity::play_damage_animation(damage_type="CRITICAL_DAMAGE");
```

**Arguments:**

| ID          | Type                                                                                               | Description |
|-------------|----------------------------------------------------------------------------------------------------|-------------|
| damage_type | Marker<br/>**CRITICAL_DAMAGE** - Critical<br/>**DAMAGE** - Normal<br/>**MAGICAL_DAMAGE** - Magical | Damage Type |

<h3 id=entity_play_hurt_animation>
  <code>entity::play_hurt_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Hurt Animation\
**Action type:** Action without value\
**Description:** Plays the damage animation.

**Usage example:**
```ts
entity::play_hurt_animation(1);

//Or dry by keywords

entity::play_hurt_animation(yaw=1);
```

**Arguments:**

| ID  | Type   | Description             |
|-----|--------|-------------------------|
| yaw | Number | Angle of damage (0-360) |

<h3 id=entity_ram_target>
  <code>entity::ram_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ram Entity\
**Action type:** Action without value\
**Description:** Causes goats to ram the target entity.\
**Work_with:**\
&nbsp;&nbsp;Goat

**Usage example:**
```ts
entity::ram_target("name_or_uuid");

//Or dry by keywords

entity::ram_target(name_or_uuid="name_or_uuid");
```

**Arguments:**

| ID           | Type | Description         |
|--------------|------|---------------------|
| name_or_uuid | Text | Entity name or UUID |

<h3 id=entity_remove>
  <code>entity::remove</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Entity\
**Action type:** Action without value\
**Description:** Removes an entity from the world.

**Usage example:**
```ts
entity::remove();
```

<h3 id=entity_remove_custom_tag>
  <code>entity::remove_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Custom Tag\
**Action type:** Action without value\
**Description:** Removes a custom NBT tag from an entity.

**Usage example:**
```ts
entity::remove_custom_tag("name");

//Or dry by keywords

entity::remove_custom_tag(name="name");
```

**Arguments:**

| ID   | Type | Description |
|------|------|-------------|
| name | Text | Tag name    |

<h3 id=entity_remove_disguise>
  <code>entity::remove_disguise</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Disguise\
**Action type:** Action without value\
**Description:** Removes an entity's disguise.

**Usage example:**
```ts
entity::remove_disguise();
```

<h3 id=entity_remove_merchant_recipe>
  <code>entity::remove_merchant_recipe</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Merchant Recipe\
**Action type:** Action without value\
**Description:** Removes an item to the Villager at the specified index.\
**Work_with:**\
&nbsp;&nbsp;Villager\
&nbsp;&nbsp;Wandering Traders

**Usage example:**
```ts
entity::remove_merchant_recipe(1);

//Or dry by keywords

entity::remove_merchant_recipe(recipe_index=1);
```

**Arguments:**

| ID           | Type   | Description   |
|--------------|--------|---------------|
| recipe_index | Number | Product Index |

<h3 id=entity_remove_potion_effect>
  <code>entity::remove_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Potion Effect\
**Action type:** Action without value\
**Description:** Removes the selected effects from an entity.

**Usage example:**
```ts
entity::remove_potion_effect([potion("slow_falling"), potion("slow_falling")]);

//Or dry by keywords

entity::remove_potion_effect(effects=[potion("slow_falling"), potion("slow_falling")]);
```

**Arguments:**

| ID      | Type            | Description                                                    |
|---------|-----------------|----------------------------------------------------------------|
| effects | Array\[Potion\] | Effects to Remove<br/>The argument supports list decomposition |

<h3 id=entity_reset_display_brightness>
  <code>entity::reset_display_brightness</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reset Brightness\
**Action type:** Action without value\
**Description:** Reset the brightness of an entity renderer.\
**Work_with:**\
&nbsp;&nbsp;Any Display Entity

**Usage example:**
```ts
entity::reset_display_brightness();
```

<h3 id=entity_reset_display_glow_color>
  <code>entity::reset_display_glow_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reset Glow Color\
**Action type:** Action without value\
**Description:** Reset the glow color of the render entity.\
**Work_with:**\
&nbsp;&nbsp;Item Renderers\
&nbsp;&nbsp;Block Renderers

**Usage example:**
```ts
entity::reset_display_glow_color();
```

<h3 id=entity_reset_mannequin_description>
  <code>entity::reset_mannequin_description</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_reset_mannequin_description.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_reset_mannequin_description.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_reset_mannequin_description.work_with.mannequin

**Usage example:**
```ts
entity::reset_mannequin_description();
```

<h3 id=entity_reset_text_display_background>
  <code>entity::reset_text_display_background</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reset Background Color\
**Action type:** Action without value\
**Description:** Reset the background color and transparency of the text renderer.\
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:**
```ts
entity::reset_text_display_background();
```

<h3 id=entity_reset_waypoint_color>
  <code>entity::reset_waypoint_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_reset_waypoint_color.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_reset_waypoint_color.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.entity_reset_waypoint_color.additional_information.needs_enabled_gamerule_location_bar\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_reset_waypoint_color.work_with.living_entity

**Usage example:**
```ts
entity::reset_waypoint_color();
```

<h3 id=entity_retrieve_fishing_hook>
  <code>entity::retrieve_fishing_hook</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_retrieve_fishing_hook.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_retrieve_fishing_hook.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_retrieve_fishing_hook.work_with.fishing_rod

**Usage example:**
```ts
entity::retrieve_fishing_hook("MAIN_HAND");

//Or dry by keywords

entity::retrieve_fishing_hook(slot="MAIN_HAND");
```

**Arguments:**

| ID   | Type                                                                                                                                                                                                                 | Description                                                          |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| slot | Marker<br/>**MAIN_HAND** - creative_plus.action.entity_retrieve_fishing_hook.argument.slot.enum.main_hand.name<br/>**OFF_HAND** - creative_plus.action.entity_retrieve_fishing_hook.argument.slot.enum.off_hand.name | creative_plus.action.entity_retrieve_fishing_hook.argument.slot.name |

<h3 id=entity_ride_entity>
  <code>entity::ride_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ride an Entity\
**Action type:** Action without value\
**Description:** Rides an entity onto another entity or player.

**Usage example:**
```ts
entity::ride_entity("name_or_uuid");

//Or dry by keywords

entity::ride_entity(name_or_uuid="name_or_uuid");
```

**Arguments:**

| ID           | Type | Description                |
|--------------|------|----------------------------|
| name_or_uuid | Text | Name or UUID of the target |

<h3 id=entity_roll_armadillo>
  <code>entity::roll_armadillo</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_roll_armadillo.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_roll_armadillo.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_roll_armadillo.work_with.armadillo

**Usage example:**
```ts
entity::roll_armadillo("ROLL_OUT");

//Or dry by keywords

entity::roll_armadillo(roll="ROLL_OUT");
```

**Arguments:**

| ID   | Type                                                                                                                                                                                               | Description                                                   |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| roll | Marker<br/>**ROLL_OUT** - creative_plus.action.entity_roll_armadillo.argument.roll.enum.roll_out.name<br/>**ROLL_UP** - creative_plus.action.entity_roll_armadillo.argument.roll.enum.roll_up.name | creative_plus.action.entity_roll_armadillo.argument.roll.name |

<h3 id=entity_set_absorption_health>
  <code>entity::set_absorption_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Extra Health\
**Action type:** Action without value\
**Description:** Sets an entity's bonus health.

**Usage example:**
```ts
entity::set_absorption_health(1);

//Or dry by keywords

entity::set_absorption_health(health=1);
```

**Arguments:**

| ID     | Type   | Description            |
|--------|--------|------------------------|
| health | Number | Amount of Extra Health |

<h3 id=entity_set_ai>
  <code>entity::set_ai</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Intelligence\
**Action type:** Action without value\
**Description:** Sets the intelligence of an entity.

**Usage example:**
```ts
entity::set_ai("FALSE");

//Or dry by keywords

entity::set_ai(ai="FALSE");
```

**Arguments:**

| ID | Type                                                 | Description  |
|----|------------------------------------------------------|--------------|
| ai | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Intelligence |

<h3 id=entity_set_allay_dancing>
  <code>entity::set_allay_dancing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Allay Dancing\
**Action type:** Action without value\
**Description:** Sets the Quiet Entity to display a dancing animation.\
**Work_with:**\
&nbsp;&nbsp;Allays

**Usage example:**
```ts
entity::set_allay_dancing("FALSE");

//Or dry by keywords

entity::set_allay_dancing(dance="FALSE");
```

**Arguments:**

| ID    | Type                                                 | Description     |
|-------|------------------------------------------------------|-----------------|
| dance | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Dance Animation |

<h3 id=entity_set_angry>
  <code>entity::set_angry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Anger Mode\
**Action type:** Action without value\
**Description:** Sets an entity to anger mode on a specific target.\
**Additional info:**\
&nbsp;&nbsp;An entity needs a target to work properly.\
**Work_with:**\
&nbsp;&nbsp;Bees\
&nbsp;&nbsp;Wolf\
&nbsp;&nbsp;Zombie Piglins\
&nbsp;&nbsp;Endermen\
&nbsp;&nbsp;Mobs

**Usage example:**
```ts
entity::set_angry("target", "FALSE");

//Or dry by keywords

entity::set_angry(target="target", angry="FALSE");
```

**Arguments:**

| ID     | Type                                                 | Description |
|--------|------------------------------------------------------|-------------|
| target | Text                                                 | Target Name |
| angry  | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Angry Mode  |

<h3 id=entity_set_animal_age>
  <code>entity::set_animal_age</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Animal Age\
**Action type:** Action without value\
**Description:** Sets the age of an animal.

**Usage example:**
```ts
entity::set_animal_age(1, "DISABLE");

//Or dry by keywords

entity::set_animal_age(age=1, lock="DISABLE");
```

**Arguments:**

| ID   | Type                                                                                           | Description     |
|------|------------------------------------------------------------------------------------------------|-----------------|
| age  | Number                                                                                         | Age             |
| lock | Marker<br/>**DISABLE** - Disabled<br/>**DONT_CHANGE** - Don't Replace<br/>**ENABLE** - Enabled | Stop Growing Up |

<h3 id=entity_set_armor_items>
  <code>entity::set_armor_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor\
**Action type:** Action without value\
**Description:** Sets an entity's armor.\
**Additional info:**\
&nbsp;&nbsp;Any item or block will appear on the head when placed in a helmet slot.

**Usage example:**
```ts
entity::set_armor_items(item("stick"), item("stick"), item("stick"), item("stick"));

//Or dry by keywords

entity::set_armor_items(helmet=item("stick"), chestplate=item("stick"), leggings=item("stick"), boots=item("stick"));
```

**Arguments:**

| ID         | Type | Description |
|------------|------|-------------|
| helmet     | Item | Headgear    |
| chestplate | Item | Chestplate  |
| leggings   | Item | Pants       |
| boots      | Item | Boots       |

<h3 id=entity_set_armor_stand_parts>
  <code>entity::set_armor_stand_parts</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor Stand Parts\
**Action type:** Action without value\
**Description:** Set armor stand parts.\
**Work_with:**\
&nbsp;&nbsp;Armor Stands

**Usage example:**
```ts
entity::set_armor_stand_parts("DISABLE", "DISABLE");

//Or dry by keywords

entity::set_armor_stand_parts(arms="DISABLE", base_plate="DISABLE");
```

**Arguments:**

| ID         | Type                                                                                        | Description     |
|------------|---------------------------------------------------------------------------------------------|-----------------|
| arms       | Marker<br/>**DISABLE** - Disable<br/>**DONT_CHANGE** - Don't Change<br/>**ENABLE** - Enable | Hand Visibility |
| base_plate | Marker<br/>**DISABLE** - Disable<br/>**DONT_CHANGE** - Don't Change<br/>**ENABLE** - Enable | Slab Visibility |

<h3 id=entity_set_armor_stand_pose>
  <code>entity::set_armor_stand_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor Stand Pose\
**Action type:** Action without value\
**Description:** Sets the pose of an armor stand.\
**Work_with:**\
&nbsp;&nbsp;Armor Stands

**Usage example:**
```ts
entity::set_armor_stand_pose(1, 2, 3, "BODY");

//Or dry by keywords

entity::set_armor_stand_pose(x_rotation=1, y_rotation=2, z_rotation=3, body_part="BODY");
```

**Arguments:**

| ID         | Type                                                                                                                                                               | Description          |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| x_rotation | Number                                                                                                                                                             | X Rotation           |
| y_rotation | Number                                                                                                                                                             | Y Rotation           |
| z_rotation | Number                                                                                                                                                             | Rotation Z           |
| body_part  | Marker<br/>**BODY** - Body<br/>**HEAD** - Head<br/>**LEFT_ARM** - Left Arm<br/>**LEFT_LEG** - Left Leg<br/>**RIGHT_ARM** - Right Arm<br/>**RIGHT_LEG** - Right Leg | Stand Part to Change |

<h3 id=entity_set_arrow_hit_sound>
  <code>entity::set_arrow_hit_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Projectile Hit Sound\
**Action type:** Action without value\
**Description:** Sets the sound a projectile makes when it hits an entity or player.\
**Work_with:**\
&nbsp;&nbsp;Arrows\
&nbsp;&nbsp;Tridents

**Usage example:**
```ts
entity::set_arrow_hit_sound(sound("entity.zombie.hurt"));

//Or dry by keywords

entity::set_arrow_hit_sound(sound=sound("entity.zombie.hurt"));
```

**Arguments:**

| ID    | Type  | Description |
|-------|-------|-------------|
| sound | Sound | Hit Sound   |

<h3 id=entity_set_arrow_pierce>
  <code>entity::set_arrow_pierce</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Arrow Pierce Count\
**Action type:** Action without value\
**Description:** Sets the amount of times an arrow can pierce an entity (from 0 to 127).

**Usage example:**
```ts
entity::set_arrow_pierce(1);

//Or dry by keywords

entity::set_arrow_pierce(pierce=1);
```

**Arguments:**

| ID     | Type   | Description       |
|--------|--------|-------------------|
| pierce | Number | Number of pierces |

<h3 id=entity_set_attribute>
  <code>entity::set_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Attribute\
**Action type:** Action without value\
**Description:** Sets the specified attribute to the specified entity value.

**Usage example:**
```ts
entity::set_attribute(1, "CAMERA_DISTANCE");

//Or dry by keywords

entity::set_attribute(value=1, attribute_type="CAMERA_DISTANCE");
```

**Arguments:**

| ID             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description     |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| value          | Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Attribute Value |
| attribute_type | Marker<br/>**CAMERA_DISTANCE** - creative_plus.action.entity_set_attribute.argument.attribute_type.enum.camera_distance.name<br/>**GENERIC_ARMOR** - Armor points (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Armor toughness points (generic.armor_toughness)<br/>**GENERIC_ATTACK_DAMAGE** - Attack damage (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Attack knockback (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Attack speed (generic.attack_speed)<br/>**GENERIC_BURNING_TIME** - Burning Time<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Explosion Knockback Resistance<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Fall Damage Multiplier<br/>**GENERIC_FLYING_SPEED** - Flying speed (generic.flying_speed)<br/>**GENERIC_FOLLOW_RANGE** - Follor range (generic.follow_range)<br/>**GENERIC_GRAVITY** - Gravity<br/>**GENERIC_JUMP_STRENGTH** - Jump Strength<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Knockback resistance (generic.knockback_resistance)<br/>**GENERIC_LUCK** - Fishing luck (generic.luck)<br/>**GENERIC_MAX_ABSORPTION** - Max absorption (generic.max_absorption)<br/>**GENERIC_MAX_HEALTH** - Max health (generic.max_health)<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Movement Efficiency<br/>**GENERIC_MOVEMENT_SPEED** - Movement speed (generic.movement_speed)<br/>**GENERIC_OXYGEN_BONUS** - Oxygen Bonus<br/>**GENERIC_SAFE_FALL_DISTANCE** - Safe Fall Distance<br/>**GENERIC_SCALE** - Scale<br/>**GENERIC_STEP_HEIGHT** - Step Height<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Water Movement Efficiency<br/>**PLAYER_BLOCK_BREAK_SPEED** - Block Breaking Speed<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - Block Interaction Range<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - Entity Interaction Range<br/>**PLAYER_MINING_EFFICIENCY** - Mining Efficiency<br/>**PLAYER_SNEAKING_SPEED** - Sneaking Speed<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Mining Speed<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - Sweeping Damage Ratio<br/>**TEMP_RANGE** - creative_plus.action.entity_set_attribute.argument.attribute_type.enum.temp_range.name<br/>**WAYPOINT_RECEIVE_RANGE** - creative_plus.action.entity_set_attribute.argument.attribute_type.enum.waypoint_receive_range.name<br/>**WAYPOINT_TRANSMIT_RANGE** - creative_plus.action.entity_set_attribute.argument.attribute_type.enum.waypoint_transmit_range.name<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Zombie reinforcements chance | Attribute Type  |

<h3 id=entity_set_aware>
  <code>entity::set_aware</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Mob Awareness\
**Action type:** Action without value\
**Description:** When disabled, disables the AI of the mob, but leaves interaction with gravity, pushing, etc.\
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:**
```ts
entity::set_aware("FALSE");

//Or dry by keywords

entity::set_aware(aware="FALSE");
```

**Arguments:**

| ID    | Type                                                 | Description |
|-------|------------------------------------------------------|-------------|
| aware | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Awareness   |

<h3 id=entity_set_axolotl_type>
  <code>entity::set_axolotl_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Axolotl Type\
**Action type:** Action without value\
**Description:** Sets the axolotl type.\
**Work_with:**\
&nbsp;&nbsp;Axolotl

**Usage example:**
```ts
entity::set_axolotl_type("BLUE");

//Or dry by keywords

entity::set_axolotl_type(axolotl_type="BLUE");
```

**Arguments:**

| ID           | Type                                                                                                           | Description  |
|--------------|----------------------------------------------------------------------------------------------------------------|--------------|
| axolotl_type | Marker<br/>**BLUE** - Blue<br/>**CYAN** - Cyan<br/>**GOLD** - Gold<br/>**LUCY** - Leukist<br/>**WILD** - Brown | Axolotl Type |

<h3 id=entity_set_baby>
  <code>entity::set_baby</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Child Mode\
**Action type:** Action without value\
**Description:** Sets an entity to child mode.

**Usage example:**
```ts
entity::set_baby("FALSE");

//Or dry by keywords

entity::set_baby(baby="FALSE");
```

**Arguments:**

| ID   | Type                                                 | Description |
|------|------------------------------------------------------|-------------|
| baby | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Child Mode  |

<h3 id=entity_set_base_arrow_damage>
  <code>entity::set_base_arrow_damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Projectile Base Damage\
**Action type:** Action without value\
**Description:** Sets the projectile's base damage, which will be used in the projectile's damage formula when it hits.\
**Additional info:**\
&nbsp;&nbsp;Formula for arrows: Base Damage * Projectile Speed = Damage Dealt\
&nbsp;&nbsp;Formula for tridents: Base Damage = Damage Dealt\
**Work_with:**\
&nbsp;&nbsp;Arrows\
&nbsp;&nbsp;Tridents

**Usage example:**
```ts
entity::set_base_arrow_damage(1);

//Or dry by keywords

entity::set_base_arrow_damage(damage=1);
```

**Arguments:**

| ID     | Type   | Description |
|--------|--------|-------------|
| damage | Number | Damage      |

<h3 id=entity_set_bee_has_stinger>
  <code>entity::set_bee_has_stinger</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Bee Stinger\
**Action type:** Action without value\
**Description:** Toggles whether a bee has a stinger.\
**Work_with:**\
&nbsp;&nbsp;Bee

**Usage example:**
```ts
entity::set_bee_has_stinger("TRUE");

//Or dry by keywords

entity::set_bee_has_stinger(stinger="TRUE");
```

**Arguments:**

| ID      | Type                                             | Description |
|---------|--------------------------------------------------|-------------|
| stinger | Marker<br/>**TRUE** - True<br/>**FALSE** - False | Has Stinger |

<h3 id=entity_set_bee_nectar>
  <code>entity::set_bee_nectar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Bee Pollen\
**Action type:** Action without value\
**Description:** Sets the visibility of pollen to the bee.\
**Work_with:**\
&nbsp;&nbsp;Bees

**Usage example:**
```ts
entity::set_bee_nectar("FALSE");

//Or dry by keywords

entity::set_bee_nectar(nectar="FALSE");
```

**Arguments:**

| ID     | Type                                                | Description       |
|--------|-----------------------------------------------------|-------------------|
| nectar | Marker<br/>**FALSE** - Enable<br/>**TRUE** - Enable | Pollen Visibility |

<h3 id=entity_set_block_display_block>
  <code>entity::set_block_display_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Display Block\
**Action type:** Action without value\
**Description:** Sets the display block to the block renderer.\
**Work_with:**\
&nbsp;&nbsp;Block Renderers

**Usage example:**
```ts
entity::set_block_display_block("minecraft:oak_log[axis=x]");

//Or dry by keywords

entity::set_block_display_block(displayed_block="minecraft:oak_log[axis=x]");
```

**Arguments:**

| ID              | Type  | Description     |
|-----------------|-------|-----------------|
| displayed_block | Block | Displayed Block |

<h3 id=entity_set_camel_dashing>
  <code>entity::set_camel_dashing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Camel Dashing Animation\
**Action type:** Action without value\
**Description:** Sets the dashing animation for the camel.\
**Work_with:**\
&nbsp;&nbsp;Camels

**Usage example:**
```ts
entity::set_camel_dashing("FALSE");

//Or dry by keywords

entity::set_camel_dashing(dashing="FALSE");
```

**Arguments:**

| ID      | Type                                                 | Description       |
|---------|------------------------------------------------------|-------------------|
| dashing | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Dashing Animation |

<h3 id=entity_set_carrying_chest>
  <code>entity::set_carrying_chest</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Chest Visibility\
**Action type:** Action without value\
**Description:** Sets the visibility of the chest on the entity.\
**Work_with:**\
&nbsp;&nbsp;Donkeys\
&nbsp;&nbsp;Mules\
&nbsp;&nbsp;Lamas

**Usage example:**
```ts
entity::set_carrying_chest("FALSE");

//Or dry by keywords

entity::set_carrying_chest(carrying="FALSE");
```

**Arguments:**

| ID       | Type                                                 | Description    |
|----------|------------------------------------------------------|----------------|
| carrying | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Having a Chest |

<h3 id=entity_set_cat_lying_down>
  <code>entity::set_cat_lying_down</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Cat Lying Down\
**Action type:** Action without value\
**Description:** Sets the lying down mode for the cat.\
**Work_with:**\
&nbsp;&nbsp;Cats

**Usage example:**
```ts
entity::set_cat_lying_down("FALSE");

//Or dry by keywords

entity::set_cat_lying_down(lying_down="FALSE");
```

**Arguments:**

| ID         | Type                                                 | Description |
|------------|------------------------------------------------------|-------------|
| lying_down | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Lying Mode  |

<h3 id=entity_set_cat_type>
  <code>entity::set_cat_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Cat Type\
**Action type:** Action without value\
**Description:** Sets the type of cat.\
**Work_with:**\
&nbsp;&nbsp;Cats

**Usage example:**
```ts
entity::set_cat_type("ALL_BLACK");

//Or dry by keywords

entity::set_cat_type(cat_type="ALL_BLACK");
```

**Arguments:**

| ID       | Type                                                                                                                                                                                                                                                                                                           | Description |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| cat_type | Marker<br/>**ALL_BLACK** - Black<br/>**BLACK** - Black and White<br/>**BRITISH_SHORTHAIR** - British Shorthair<br/>**CALICO** - Calico<br/>**JELLIE** - White-Grey<br/>**PERSIAN** - Persian<br/>**RAGDOLL** - Ragdoll<br/>**RED** - Red<br/>**SIAMESE** - Siamese<br/>**TABBY** - Tabby<br/>**WHITE** - White | Cat Type    |

<h3 id=entity_set_celebrating>
  <code>entity::set_celebrating</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Celebrating Mode\
**Action type:** Action without value\
**Description:** Sets the entity's celebrating mode.\
**Work_with:**\
&nbsp;&nbsp;Piglin\
&nbsp;&nbsp;Raiders

**Usage example:**
```ts
entity::set_celebrating("FALSE");

//Or dry by keywords

entity::set_celebrating(celebrating="FALSE");
```

**Arguments:**

| ID          | Type                                                 | Description      |
|-------------|------------------------------------------------------|------------------|
| celebrating | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Celebration Mode |

<h3 id=entity_set_chicken_type>
  <code>entity::set_chicken_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_chicken_type.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_chicken_type.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_chicken_type.work_with.chicken

**Usage example:**
```ts
entity::set_chicken_type("COLD");

//Or dry by keywords

entity::set_chicken_type(variant="COLD");
```

**Arguments:**

| ID      | Type                                                                                                                                                                                                                                                                                                 | Description                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| variant | Marker<br/>**COLD** - creative_plus.action.entity_set_chicken_type.argument.variant.enum.cold.name<br/>**WARM** - creative_plus.action.entity_set_chicken_type.argument.variant.enum.warm.name<br/>**TEMPERATE** - creative_plus.action.entity_set_chicken_type.argument.variant.enum.temperate.name | creative_plus.action.entity_set_chicken_type.argument.variant.name |

<h3 id=entity_set_collidable>
  <code>entity::set_collidable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Collidable Mode\
**Action type:** Action without value\
**Description:** Sets an entity to collide with other entities.

**Usage example:**
```ts
entity::set_collidable("FALSE");

//Or dry by keywords

entity::set_collidable(collidable="FALSE");
```

**Arguments:**

| ID         | Type                                                                                                 | Description    |
|------------|------------------------------------------------------------------------------------------------------|----------------|
| collidable | Marker<br/>**FALSE** - Does not collide with other creatures<br/>**TRUE** - Collides other creatures | Collision Mode |

<h3 id=entity_set_copper_golem_oxidizing>
  <code>entity::set_copper_golem_oxidizing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_copper_golem_oxidizing.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_copper_golem_oxidizing.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_copper_golem_oxidizing.work_with.copper_golem

**Usage example:**
```ts
entity::set_copper_golem_oxidizing("WAXED");

//Or dry by keywords

entity::set_copper_golem_oxidizing(oxidizing_state="WAXED");
```

**Arguments:**

| ID              | Type                                                                                                                                                                                                                                   | Description                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| oxidizing_state | Marker<br/>**WAXED** - creative_plus.action.entity_set_copper_golem_oxidizing.argument.oxidizing_state.enum.waxed.name<br/>**UNSET** - creative_plus.action.entity_set_copper_golem_oxidizing.argument.oxidizing_state.enum.unset.name | creative_plus.action.entity_set_copper_golem_oxidizing.argument.oxidizing_state.name |

<h3 id=entity_set_copper_golem_oxidizing_at_time>
  <code>entity::set_copper_golem_oxidizing_at_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_copper_golem_oxidizing_at_time.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_copper_golem_oxidizing_at_time.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_copper_golem_oxidizing_at_time.work_with.copper_golem

**Usage example:**
```ts
entity::set_copper_golem_oxidizing_at_time(1);

//Or dry by keywords

entity::set_copper_golem_oxidizing_at_time(time=1);
```

**Arguments:**

| ID   | Type   | Description                                                                       |
|------|--------|-----------------------------------------------------------------------------------|
| time | Number | creative_plus.action.entity_set_copper_golem_oxidizing_at_time.argument.time.name |

<h3 id=entity_set_copper_golem_weathering>
  <code>entity::set_copper_golem_weathering</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_copper_golem_weathering.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_copper_golem_weathering.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_copper_golem_weathering.work_with.copper_golem

**Usage example:**
```ts
entity::set_copper_golem_weathering(1);

//Or dry by keywords

entity::set_copper_golem_weathering(weathering_state=1);
```

**Arguments:**

| ID               | Type   | Description                                                                            |
|------------------|--------|----------------------------------------------------------------------------------------|
| weathering_state | Number | creative_plus.action.entity_set_copper_golem_weathering.argument.weathering_state.name |

<h3 id=entity_set_cow_type>
  <code>entity::set_cow_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_cow_type.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_cow_type.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_cow_type.work_with.cow

**Usage example:**
```ts
entity::set_cow_type("COLD");

//Or dry by keywords

entity::set_cow_type(variant="COLD");
```

**Arguments:**

| ID      | Type                                                                                                                                                                                                                                                                                     | Description                                                    |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| variant | Marker<br/>**COLD** - creative_plus.action.entity_set_cow_type.argument.variant.enum.cold.name<br/>**WARM** - creative_plus.action.entity_set_cow_type.argument.variant.enum.warm.name<br/>**TEMPERATE** - creative_plus.action.entity_set_cow_type.argument.variant.enum.temperate.name | creative_plus.action.entity_set_cow_type.argument.variant.name |

<h3 id=entity_set_creeper_charge>
  <code>entity::set_creeper_charge</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Creeper Charge\
**Action type:** Action without value\
**Description:** Sets whether the creeper will be charged.\
**Work_with:**\
&nbsp;&nbsp;Creepers

**Usage example:**
```ts
entity::set_creeper_charge("FALSE");

//Or dry by keywords

entity::set_creeper_charge(charged="FALSE");
```

**Arguments:**

| ID      | Type                                                      | Description     |
|---------|-----------------------------------------------------------|-----------------|
| charged | Marker<br/>**FALSE** - Not Charged<br/>**TRUE** - Charged | Creeper Charged |

<h3 id=entity_set_creeper_fuse>
  <code>entity::set_creeper_fuse</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Creeper Max Fuse Time\
**Action type:** Action without value\
**Description:** Sets the creeper's time before it explodes.\
**Work_with:**\
&nbsp;&nbsp;Creepers

**Usage example:**
```ts
entity::set_creeper_fuse(1);

//Or dry by keywords

entity::set_creeper_fuse(fuse_ticks=1);
```

**Arguments:**

| ID         | Type   | Description             |
|------------|--------|-------------------------|
| fuse_ticks | Number | Time to Explode (Ticks) |

<h3 id=entity_set_current_health>
  <code>entity::set_current_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Health\
**Action type:** Action without value\
**Description:** Sets an entity's health to the selected amount.

**Usage example:**
```ts
entity::set_current_health(1);

//Or dry by keywords

entity::set_current_health(health=1);
```

**Arguments:**

| ID     | Type   | Description      |
|--------|--------|------------------|
| health | Number | Amount of Health |

<h3 id=entity_set_custom_name>
  <code>entity::set_custom_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Name\
**Action type:** Action without value\
**Description:** Sets a name for an entity.

**Usage example:**
```ts
entity::set_custom_name("custom_name");

//Or dry by keywords

entity::set_custom_name(custom_name="custom_name");
```

**Arguments:**

| ID          | Type | Description |
|-------------|------|-------------|
| custom_name | Text | Entity Name |

<h3 id=entity_set_custom_name_visibility>
  <code>entity::set_custom_name_visibility</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Name Visibility\
**Action type:** Action without value\
**Description:** Sets the visibility of the entity name.

**Usage example:**
```ts
entity::set_custom_name_visibility("FALSE");

//Or dry by keywords

entity::set_custom_name_visibility(visibility="FALSE");
```

**Arguments:**

| ID         | Type                                                 | Description     |
|------------|------------------------------------------------------|-----------------|
| visibility | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Name Visibility |

<h3 id=entity_set_custom_tag>
  <code>entity::set_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Custom Tag\
**Action type:** Action without value\
**Description:** Sets a custom nbt tag to an entity.

**Usage example:**
```ts
entity::set_custom_tag("name", "value");

//Or dry by keywords

entity::set_custom_tag(name="name", value="value");
```

**Arguments:**

| ID    | Type | Description |
|-------|------|-------------|
| name  | Text | Tag name    |
| value | Text | Tag Value   |

<h3 id=entity_set_death_drops>
  <code>entity::set_death_drops</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Drops Items\
**Action type:** Action without value\
**Description:** Sets whether an entity will drop loot.

**Usage example:**
```ts
entity::set_death_drops("FALSE");

//Or dry by keywords

entity::set_death_drops(drops="FALSE");
```

**Arguments:**

| ID    | Type                                                 | Description |
|-------|------------------------------------------------------|-------------|
| drops | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Item Drops  |

<h3 id=entity_set_death_time>
  <code>entity::set_death_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Death Time\
**Action type:** Action without value\
**Description:** Sets the death duration for an entity.

**Usage example:**
```ts
entity::set_death_time(1);

//Or dry by keywords

entity::set_death_time(death_time=1);
```

**Arguments:**

| ID         | Type   | Description            |
|------------|--------|------------------------|
| death_time | Number | Death Duration (Ticks) |

<h3 id=entity_set_default_visible>
  <code>entity::set_default_visible</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visibility\
**Action type:** Action without value\
**Description:** Sets whether an entity is visible.\
**Additional info:**\
&nbsp;&nbsp;The visibility of an entity to a player or group of players can be changed via the action "Hide Entity to Player"

**Usage example:**
```ts
entity::set_default_visible("TRUE");

//Or dry by keywords

entity::set_default_visible(default_visible="TRUE");
```

**Arguments:**

| ID              | Type                                                    | Description |
|-----------------|---------------------------------------------------------|-------------|
| default_visible | Marker<br/>**TRUE** - Visible<br/>**FALSE** - Invisible | Visibility  |

<h3 id=entity_set_despawning>
  <code>entity::set_despawning</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Despawning\
**Action type:** Action without value\
**Description:** Sets whether an entity will despawn.

**Usage example:**
```ts
entity::set_despawning("FALSE");

//Or dry by keywords

entity::set_despawning(despawning="FALSE");
```

**Arguments:**

| ID         | Type                                                 | Description         |
|------------|------------------------------------------------------|---------------------|
| despawning | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Entity Disappearing |

<h3 id=entity_set_display_billboard>
  <code>entity::set_display_billboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Display Mode\
**Action type:** Action without value\
**Description:** Sets the display mode of the billboard entity.\
**Work_with:**\
&nbsp;&nbsp;Any renderer entity

**Usage example:**
```ts
entity::set_display_billboard("CENTER");

//Or dry by keywords

entity::set_display_billboard(billboard_type="CENTER");
```

**Arguments:**

| ID             | Type                                                                                                                                       | Description  |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| billboard_type | Marker<br/>**CENTER** - Always Facing Player<br/>**FIXED** - Fixed<br/>**HORIZONTAL** - Fixed Horizontal<br/>**VERTICAL** - Fixed Vertical | Display Mode |

<h3 id=entity_set_display_brightness>
  <code>entity::set_display_brightness</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Brightness\
**Action type:** Action without value\
**Description:** Sets the brightness of the renderer entity.\
**Work_with:**\
&nbsp;&nbsp;Any Display Entity

**Usage example:**
```ts
entity::set_display_brightness(1, 2);

//Or dry by keywords

entity::set_display_brightness(block_light_level=1, sky_light_level=2);
```

**Arguments:**

| ID                | Type   | Description       |
|-------------------|--------|-------------------|
| block_light_level | Number | Block Light Level |
| sky_light_level   | Number | Sky light level   |

<h3 id=entity_set_display_correct_transformation_matrix>
  <code>entity::set_display_correct_transformation_matrix</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_display_correct_transformation_matrix.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_display_correct_transformation_matrix.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_display_correct_transformation_matrix.work_with.any_display_entity

**Usage example:**
```ts
entity::set_display_correct_transformation_matrix([1, 2]);

//Or dry by keywords

entity::set_display_correct_transformation_matrix(matrix=[1, 2]);
```

**Arguments:**

| ID     | Type            | Description                                                                                                                             |
|--------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| matrix | Array\[Number\] | creative_plus.action.entity_set_display_correct_transformation_matrix.argument.matrix.name<br/>The argument supports list decomposition |

<h3 id=entity_set_display_culling_suze>
  <code>entity::set_display_culling_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visibility Size\
**Action type:** Action without value\
**Description:** Sets the size of the visualizer entity's model scope.\
**Work_with:**\
&nbsp;&nbsp;Any Visualizer Entity

**Usage example:**
```ts
entity::set_display_culling_size(1, 2);

//Or dry by keywords

entity::set_display_culling_size(width=1, height=2);
```

**Arguments:**

| ID     | Type   | Description     |
|--------|--------|-----------------|
| width  | Number | Horizontal Size |
| height | Number | Vertical Size   |

<h3 id=entity_set_display_glow_color>
  <code>entity::set_display_glow_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Glow Color\
**Action type:** Action without value\
**Description:** Sets the glow color for the render entity.\
**Work_with:**\
&nbsp;&nbsp;Item Renderers\
&nbsp;&nbsp;Block Renderers

**Usage example:**
```ts
entity::set_display_glow_color("color_hexadecimal");

//Or dry by keywords

entity::set_display_glow_color(color_hexadecimal="color_hexadecimal");
```

**Arguments:**

| ID                | Type | Description |
|-------------------|------|-------------|
| color_hexadecimal | Text | HEX color   |

<h3 id=entity_set_display_interpolation>
  <code>entity::set_display_interpolation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Interpolation\
**Action type:** Action without value\
**Description:** Sets the interpolation duration for the renderer entity.\
**Work_with:**\
&nbsp;&nbsp;Any Display Entity

**Usage example:**
```ts
entity::set_display_interpolation(1, 2);

//Or dry by keywords

entity::set_display_interpolation(interpolation_duration=1, interpolation_delay=2);
```

**Arguments:**

| ID                     | Type   | Description            |
|------------------------|--------|------------------------|
| interpolation_duration | Number | Interpolation Duration |
| interpolation_delay    | Number | Interpolation Delay    |

<h3 id=entity_set_display_rotation_from_axis_angle>
  <code>entity::set_display_rotation_from_axis_angle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation From Axis Vector\
**Action type:** Action without value\
**Description:** Sets left or right rotation by axis vector and angle of the renderer entity.\
**Work_with:**\
&nbsp;&nbsp;Any Render Entity

**Usage example:**
```ts
entity::set_display_rotation_from_axis_angle(vector(0,0,0), 1, "ADD", "DEGREES", "LEFT_ROTATION");

//Or dry by keywords

entity::set_display_rotation_from_axis_angle(axis_vector=vector(0,0,0), angle=1, mode="ADD", input="DEGREES", rotation="LEFT_ROTATION");
```

**Arguments:**

| ID          | Type                                                                                                                     | Description             |
|-------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------|
| axis_vector | Vector                                                                                                                   | Axis Vector             |
| angle       | Number                                                                                                                   | Rotation Angle          |
| mode        | Marker<br/>**ADD** - Add<br/>**SET** - Set                                                                               | Set Mode                |
| input       | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                                               | Angle type              |
| rotation    | Marker<br/>**LEFT_ROTATION** - Left Rotation (Rotation x Size)<br/>**RIGHT_ROTATION** - Right Rotation (Size x Rotation) | Order to Apply Rotation |

<h3 id=entity_set_display_rotation_from_euler_angles>
  <code>entity::set_display_rotation_from_euler_angles</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation From Euler Angles\
**Action type:** Action without value\
**Description:** Sets left or right Euler angle rotation for the renderer entity.\
**Work_with:**\
&nbsp;&nbsp;Any renderer entity

**Usage example:**
```ts
entity::set_display_rotation_from_euler_angles(1, 2, 3, "ADD", "DEGREES", "LEFT_ROTATION");

//Or dry by keywords

entity::set_display_rotation_from_euler_angles(pitch=1, yaw=2, roll=3, mode="ADD", input="DEGREES", rotation="LEFT_ROTATION");
```

**Arguments:**

| ID       | Type                                                                                                                     | Description             |
|----------|--------------------------------------------------------------------------------------------------------------------------|-------------------------|
| pitch    | Number                                                                                                                   | Pitch Angle             |
| yaw      | Number                                                                                                                   | Yaw Angle (yaw)         |
| roll     | Number                                                                                                                   | Roll Angle (roll)       |
| mode     | Marker<br/>**ADD** - Add<br/>**SET** - Set                                                                               | Set Mode                |
| input    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                                               | Angle type              |
| rotation | Marker<br/>**LEFT_ROTATION** - Left Rotation (Rotation x Size)<br/>**RIGHT_ROTATION** - Right Rotation (Size x Rotation) | Order to Apply Rotation |

<h3 id=entity_set_display_scale>
  <code>entity::set_display_scale</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scale\
**Action type:** Action without value\
**Description:** Sets the size of the renderer entity.\
**Work_with:**\
&nbsp;&nbsp;Any Render Entity

**Usage example:**
```ts
entity::set_display_scale(vector(0,0,0), "ADD");

//Or dry by keywords

entity::set_display_scale(scale_vector=vector(0,0,0), mode="ADD");
```

**Arguments:**

| ID           | Type                                       | Description |
|--------------|--------------------------------------------|-------------|
| scale_vector | Vector                                     | New Size    |
| mode         | Marker<br/>**ADD** - Add<br/>**SET** - Set | Set Mode    |

<h3 id=entity_set_display_shadow>
  <code>entity::set_display_shadow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Shadow Settings\
**Action type:** Action without value\
**Description:** Sets the size and transparency of the shadow of the entity renderer.\
**Work_with:**\
&nbsp;&nbsp;Any Display Entity

**Usage example:**
```ts
entity::set_display_shadow(1, 2);

//Or dry by keywords

entity::set_display_shadow(shadow_radius=1, shadow_opacity_percentage=2);
```

**Arguments:**

| ID                        | Type   | Description        |
|---------------------------|--------|--------------------|
| shadow_radius             | Number | Shadow Radius      |
| shadow_opacity_percentage | Number | Opacity Percentage |

<h3 id=entity_set_display_teleport_duration>
  <code>entity::set_display_teleport_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Display Teleport Duration\
**Action type:** Action without value\
**Description:** Sets the interpolation duration for display entity teleports.\
**Work_with:**\
&nbsp;&nbsp;Any display entity

**Usage example:**
```ts
entity::set_display_teleport_duration(1);

//Or dry by keywords

entity::set_display_teleport_duration(duration=1);
```

**Arguments:**

| ID       | Type   | Description       |
|----------|--------|-------------------|
| duration | Number | Teleport duration |

<h3 id=entity_set_display_transformation_matrix>
  <code>entity::set_display_transformation_matrix</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Transformation Matrix\
**Action type:** Action without value\
**Description:** Sets the transformation matrix (row-column) of the renderer entity.\
**Work_with:**\
&nbsp;&nbsp;Any Render Entity

Currently hidden. Most likely, it is either outdated or does not work.

**Usage example:**
```ts
entity::set_display_transformation_matrix([1, 2]);

//Or dry by keywords

entity::set_display_transformation_matrix(row_major_matrix=[1, 2]);
```

**Arguments:**

| ID               | Type            | Description                                                   |
|------------------|-----------------|---------------------------------------------------------------|
| row_major_matrix | Array\[Number\] | 16 Number Matrix<br/>The argument supports list decomposition |

<h3 id=entity_set_display_translation>
  <code>entity::set_display_translation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Translation\
**Action type:** Action without value\
**Description:** Sets an offset to the renderer entity.\
**Work_with:**\
&nbsp;&nbsp;Any Display Entity

**Usage example:**
```ts
entity::set_display_translation(vector(0,0,0), "ADD");

//Or dry by keywords

entity::set_display_translation(translation_vector=vector(0,0,0), mode="ADD");
```

**Arguments:**

| ID                 | Type                                       | Description |
|--------------------|--------------------------------------------|-------------|
| translation_vector | Vector                                     | New Offset  |
| mode               | Marker<br/>**ADD** - Add<br/>**SET** - Set | Set Mode    |

<h3 id=entity_set_display_view_range>
  <code>entity::set_display_view_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visibility Range\
**Action type:** Action without value\
**Description:** Sets the visibility range of the renderer entity.\
**Work_with:**\
&nbsp;&nbsp;Any Viewer Entity

**Usage example:**
```ts
entity::set_display_view_range(1);

//Or dry by keywords

entity::set_display_view_range(view_range=1);
```

**Arguments:**

| ID         | Type   | Description |
|------------|--------|-------------|
| view_range | Number | View Range  |

<h3 id=entity_set_dragon_phase>
  <code>entity::set_dragon_phase</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Ender Dragon Phase\
**Action type:** Action without value\
**Description:** Sets a specific phase for an Ender Dragon.\
**Work_with:**\
&nbsp;&nbsp;Ender Dragons

**Usage example:**
```ts
entity::set_dragon_phase("BREATH_ATTACK");

//Or dry by keywords

entity::set_dragon_phase(phase="BREATH_ATTACK");
```

**Arguments:**

| ID    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description        |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| phase | Marker<br/>**BREATH_ATTACK** - Breath Attack<br/>**CHARGE_PLAYER** - Attack Player<br/>**CIRCLING** - Circling<br/>**DYING** - Death<br/>**FLY_TO_PORTAL** - Fly to Portal<br/>**HOVER** - Flying<br/>**LAND_ON_PORTAL** - Landing on Portal<br/>**LEAVE_PORTAL** - Leave Portal<br/>**ROAR_BEFORE_ATTACK** - Scream before attack<br/>**SEARCH_FOR_BREATH_ATTACK_TARGET** - Search for a breath attack target<br/>**STRAFING** - Dodge | Ender Dragon Phase |

<h3 id=entity_set_dye_color>
  <code>entity::set_dye_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Color\
**Action type:** Action without value\
**Description:** Sets a specific color for an entity.\
**Work_with:**\
&nbsp;&nbsp;Sheep\
&nbsp;&nbsp;Shulkers\
&nbsp;&nbsp;Dog Collars\
&nbsp;&nbsp;Cat Collars

**Usage example:**
```ts
entity::set_dye_color("BLACK");

//Or dry by keywords

entity::set_dye_color(color="BLACK");
```

**Arguments:**

| ID    | Type                                                                                                                                                                                                                                                                                                                                                                             | Description  |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| color | Marker<br/>**BLACK** - Black<br/>**BLUE** - Blue<br/>**BROWN** - Brown<br/>**CYAN** - Cyan<br/>**GRAY** - Gray<br/>**GREEN** - Green<br/>**LIGHT_BLUE** - Blue<br/>**LIGHT_GRAY** - Light Gray<br/>**LIME** - Lime<br/>**MAGENTA** - Magenta<br/>**ORANGE** - Orange<br/>**PINK** - Pink<br/>**PURPLE** - Purple<br/>**RED** - Red<br/>**WHITE** - White<br/>**YELLOW** - Yellow | Entity Color |

<h3 id=entity_set_end_crystal_beam>
  <code>entity::set_end_crystal_beam</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set End Crystal Beam\
**Action type:** Action without value\
**Description:** Points an End Crystal Beam to a specific location.\
**Work_with:**\
&nbsp;&nbsp;End Crystals

**Usage example:**
```ts
entity::set_end_crystal_beam(location(0,0,0,0,0));

//Or dry by keywords

entity::set_end_crystal_beam(beam=location(0,0,0,0,0));
```

**Arguments:**

| ID   | Type     | Description         |
|------|----------|---------------------|
| beam | Location | Location to Specify |

<h3 id=entity_set_enderman_block>
  <code>entity::set_enderman_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block to Enderman\
**Action type:** Action without value\
**Description:** Sets the rendered block to the enderman.\
**Work_with:**\
&nbsp;&nbsp;Endermen

**Usage example:**
```ts
entity::set_enderman_block("minecraft:oak_log[axis=x]");

//Or dry by keywords

entity::set_enderman_block(block="minecraft:oak_log[axis=x]");
```

**Arguments:**

| ID    | Type  | Description   |
|-------|-------|---------------|
| block | Block | Display Block |

<h3 id=entity_set_equipment_item>
  <code>entity::set_equipment_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Equipment\
**Action type:** Action without value\
**Description:** Sets an item to one of the equipment slots (armor and items in hands) of an entity.

**Usage example:**
```ts
entity::set_equipment_item(item("stick"), "BODY");

//Or dry by keywords

entity::set_equipment_item(item=item("stick"), slot="BODY");
```

**Arguments:**

| ID   | Type                                                                                                                                                                 | Description    |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| item | Item                                                                                                                                                                 | Items to Grant |
| slot | Marker<br/>**BODY** - Body<br/>**CHEST** - Chest<br/>**FEET** - Boots<br/>**HAND** - Main Hand<br/>**HEAD** - Helmet<br/>**LEGS** - Legs<br/>**OFF_HAND** - Sub-Hand | Equipment Slot |

<h3 id=entity_set_explosive_power>
  <code>entity::set_explosive_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Explosive Power\
**Action type:** Action without value\
**Description:** Sets the power of an entity's explosion.\
**Work_with:**\
&nbsp;&nbsp;Creepers\
&nbsp;&nbsp;TNT\
&nbsp;&nbsp;Fireballs

**Usage example:**
```ts
entity::set_explosive_power(1);

//Or dry by keywords

entity::set_explosive_power(power=1);
```

**Arguments:**

| ID    | Type   | Description     |
|-------|--------|-----------------|
| power | Number | Explosion Power |

<h3 id=entity_set_fall_distance>
  <code>entity::set_fall_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fall Distance\
**Action type:** Action without value\
**Description:** Sets the distance at which an entity falls.

**Usage example:**
```ts
entity::set_fall_distance(1);

//Or dry by keywords

entity::set_fall_distance(fall_distance=1);
```

**Arguments:**

| ID            | Type   | Description   |
|---------------|--------|---------------|
| fall_distance | Number | Fall Distance |

<h3 id=entity_set_falling_block_type>
  <code>entity::set_falling_block_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Falling Block Type\
**Action type:** Action without value\
**Description:** Sets a block type to a Falling block\
**Work_with:**\
&nbsp;&nbsp;Falling blocks

**Usage example:**
```ts
entity::set_falling_block_type("minecraft:oak_log[axis=x]");

//Or dry by keywords

entity::set_falling_block_type(block="minecraft:oak_log[axis=x]");
```

**Arguments:**

| ID    | Type  | Description |
|-------|-------|-------------|
| block | Block | New block   |

<h3 id=entity_set_fire_ticks>
  <code>entity::set_fire_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set on Fire\
**Action type:** Action without value\
**Description:** Sets an entity on fire for the selected amount of time.

**Usage example:**
```ts
entity::set_fire_ticks(1);

//Or dry by keywords

entity::set_fire_ticks(ticks=1);
```

**Arguments:**

| ID    | Type   | Description      |
|-------|--------|------------------|
| ticks | Number | Duration (Ticks) |

<h3 id=entity_set_fishing_wait>
  <code>entity::set_fishing_wait</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fishing Delay\
**Action type:** Action without value\
**Description:** Sets the entity's fishing delay in ticks.\
**Work_with:**\
&nbsp;&nbsp;Fish Hook

**Usage example:**
```ts
entity::set_fishing_wait(1, "MAX_WAIT");

//Or dry by keywords

entity::set_fishing_wait(time=1, wait_type="MAX_WAIT");
```

**Arguments:**

| ID        | Type                                                                                                                                   | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------|-------------|
| time      | Number                                                                                                                                 | Delay       |
| wait_type | Marker<br/>**MAX_WAIT** - Max Delay<br/>**MIN_MAX_WAIT** - Min and Max Delay<br/>**MIN_WAIT** - Min Delay<br/>**WAIT** - Current Delay | Delay Type  |

<h3 id=entity_set_fox_leaping>
  <code>entity::set_fox_leaping</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fox Leaping Animation\
**Action type:** Action without value\
**Description:** Sets the fox's jumping animation.\
**Work_with:**\
&nbsp;&nbsp;Foxes

**Usage example:**
```ts
entity::set_fox_leaping("FALSE");

//Or dry by keywords

entity::set_fox_leaping(leaping="FALSE");
```

**Arguments:**

| ID      | Type                                                 | Description       |
|---------|------------------------------------------------------|-------------------|
| leaping | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Leaping Animation |

<h3 id=entity_set_fox_type>
  <code>entity::set_fox_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fox Type\
**Action type:** Action without value\
**Description:** Sets the fox type.\
**Work_with:**\
&nbsp;&nbsp;Foxes

**Usage example:**
```ts
entity::set_fox_type("RED");

//Or dry by keywords

entity::set_fox_type(fox_type="RED");
```

**Arguments:**

| ID       | Type                                                | Description |
|----------|-----------------------------------------------------|-------------|
| fox_type | Marker<br/>**RED** - Standard<br/>**SNOW** - Winter | Fox Type    |

<h3 id=entity_set_freeze_ticks>
  <code>entity::set_freeze_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Freeze Time\
**Action type:** Action without value\
**Description:** Sets the freeze time for an entity (the number of ticks an entity has spent in powder snow).

**Usage example:**
```ts
entity::set_freeze_ticks(1, "FALSE");

//Or dry by keywords

entity::set_freeze_ticks(ticks=1, ticking_locked="FALSE");
```

**Arguments:**

| ID             | Type                                                 | Description                         |
|----------------|------------------------------------------------------|-------------------------------------|
| ticks          | Number                                               | Freeze Time in Ticks                |
| ticking_locked | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | State Locked (Time will not change) |

<h3 id=entity_set_friction>
  <code>entity::set_friction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Friction\
**Action type:** Action without value\
**Description:** Sets whether the entity will experience friction.

**Usage example:**
```ts
entity::set_friction("NOT_SET");

//Or dry by keywords

entity::set_friction(friction="NOT_SET");
```

**Arguments:**

| ID       | Type                                                                       | Description |
|----------|----------------------------------------------------------------------------|-------------|
| friction | Marker<br/>**NOT_SET** - Default<br/>**TRUE** - True<br/>**FALSE** - False | Friction    |

<h3 id=entity_set_frog_type>
  <code>entity::set_frog_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Frog Type\
**Action type:** Action without value\
**Description:** Sets the color of the frog.\
**Work_with:**\
&nbsp;&nbsp;Toads

**Usage example:**
```ts
entity::set_frog_type("COLD");

//Or dry by keywords

entity::set_frog_type(frog_variant="COLD");
```

**Arguments:**

| ID           | Type                                                                        | Description |
|--------------|-----------------------------------------------------------------------------|-------------|
| frog_variant | Marker<br/>**COLD** - Cold<br/>**TEMPERATE** - Moderate<br/>**WARM** - Warm | Toad Type   |

<h3 id=entity_set_fuse_ticks>
  <code>entity::set_fuse_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fuse Time\
**Action type:** Action without value\
**Description:** Sets the entity's time before it explodes.\
**Work_with:**\
&nbsp;&nbsp;Creepers\
&nbsp;&nbsp;TNT\
&nbsp;&nbsp;Fireworks

**Usage example:**
```ts
entity::set_fuse_ticks(1);

//Or dry by keywords

entity::set_fuse_ticks(fuse_ticks=1);
```

**Arguments:**

| ID         | Type   | Description             |
|------------|--------|-------------------------|
| fuse_ticks | Number | Time to Explode (Ticks) |

<h3 id=entity_set_gliding>
  <code>entity::set_gliding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Elytra Flying\
**Action type:** Action without value\
**Description:** Sets the creature's elytra flying state.

**Usage example:**
```ts
entity::set_gliding("FALSE");

//Or dry by keywords

entity::set_gliding(is_gliding="FALSE");
```

**Arguments:**

| ID         | Type                                                   | Description   |
|------------|--------------------------------------------------------|---------------|
| is_gliding | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Elytra Flying |

<h3 id=entity_set_glow_squid_dark>
  <code>entity::set_glow_squid_dark</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Squid Glow Time\
**Action type:** Action without value\
**Description:** Sets the duration of darkness in ticks for the glowing octopus.\
**Work_with:**\
&nbsp;&nbsp;Glowing Octopuses

**Usage example:**
```ts
entity::set_glow_squid_dark(1);

//Or dry by keywords

entity::set_glow_squid_dark(dark_ticks=1);
```

**Arguments:**

| ID         | Type   | Description       |
|------------|--------|-------------------|
| dark_ticks | Number | Dark Time (Ticks) |

<h3 id=entity_set_glowing>
  <code>entity::set_glowing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Glowing\
**Action type:** Action without value\
**Description:** Sets an entity to a glowing effect.

**Usage example:**
```ts
entity::set_glowing("FALSE");

//Or dry by keywords

entity::set_glowing(glowing="FALSE");
```

**Arguments:**

| ID      | Type                                                 | Description |
|---------|------------------------------------------------------|-------------|
| glowing | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Glow        |

<h3 id=entity_set_goat_screaming>
  <code>entity::set_goat_screaming</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Goat Screaming\
**Action type:** Action without value\
**Description:** Sets the "screaming" goat tag.\
**Work_with:**\
&nbsp;&nbsp;Goat

**Usage example:**
```ts
entity::set_goat_screaming("FALSE");

//Or dry by keywords

entity::set_goat_screaming(screams="FALSE");
```

**Arguments:**

| ID      | Type                                                 | Description   |
|---------|------------------------------------------------------|---------------|
| screams | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Screaming Tag |

<h3 id=entity_set_gravity>
  <code>entity::set_gravity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Gravity\
**Action type:** Action without value\
**Description:** Sets whether an entity will obey gravity.

**Usage example:**
```ts
entity::set_gravity("FALSE");

//Or dry by keywords

entity::set_gravity(gravity="FALSE");
```

**Arguments:**

| ID      | Type                                                 | Description |
|---------|------------------------------------------------------|-------------|
| gravity | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Gravity     |

<h3 id=entity_set_hanging_facing_location>
  <code>entity::set_hanging_facing_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_hanging_facing_location.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_hanging_facing_location.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.entity_set_hanging_facing_location.additional_information.painting_do_not_have_vertical_facing\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_hanging_facing_location.work_with.item_frame\
&nbsp;&nbsp;creative_plus.action.entity_set_hanging_facing_location.work_with.glow_item_frame\
&nbsp;&nbsp;creative_plus.action.entity_set_hanging_facing_location.work_with.painting

**Usage example:**
```ts
entity::set_hanging_facing_location("NORTH", "TRUE");

//Or dry by keywords

entity::set_hanging_facing_location(facing="NORTH", force="TRUE");
```

**Arguments:**

| ID     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| facing | Marker<br/>**NORTH** - creative_plus.action.entity_set_hanging_facing_location.argument.facing.enum.north.name<br/>**EAST** - creative_plus.action.entity_set_hanging_facing_location.argument.facing.enum.east.name<br/>**SOUTH** - creative_plus.action.entity_set_hanging_facing_location.argument.facing.enum.south.name<br/>**WEST** - creative_plus.action.entity_set_hanging_facing_location.argument.facing.enum.west.name<br/>**UP** - creative_plus.action.entity_set_hanging_facing_location.argument.facing.enum.up.name<br/>**DOWN** - creative_plus.action.entity_set_hanging_facing_location.argument.facing.enum.down.name | creative_plus.action.entity_set_hanging_facing_location.argument.facing.name |
| force  | Marker<br/>**TRUE** - creative_plus.action.entity_set_hanging_facing_location.argument.force.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_hanging_facing_location.argument.force.enum.false.name                                                                                                                                                                                                                                                                                                                                                                                                                         | creative_plus.action.entity_set_hanging_facing_location.argument.force.name  |

<h3 id=entity_set_horse_jump>
  <code>entity::set_horse_jump</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Horse Jump Power\
**Action type:** Action without value\
**Description:** Sets the horse's jump power.\
**Work_with:**\
&nbsp;&nbsp;Horses\
&nbsp;&nbsp;Donkeys\
&nbsp;&nbsp;Mules\
&nbsp;&nbsp;Lamas

**Usage example:**
```ts
entity::set_horse_jump(1);

//Or dry by keywords

entity::set_horse_jump(power=1);
```

**Arguments:**

| ID    | Type   | Description |
|-------|--------|-------------|
| power | Number | Jump Power  |

<h3 id=entity_set_horse_pattern>
  <code>entity::set_horse_pattern</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Horse Pattern\
**Action type:** Action without value\
**Description:** Sets the color and pattern of the horse.\
**Work_with:**\
&nbsp;&nbsp;Horses

**Usage example:**
```ts
entity::set_horse_pattern("BLACK", "BLACK_DOTS");

//Or dry by keywords

entity::set_horse_pattern(horse_color="BLACK", horse_style="BLACK_DOTS");
```

**Arguments:**

| ID          | Type                                                                                                                                                                                                                                      | Description   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| horse_color | Marker<br/>**BLACK** - Black<br/>**BROWN** - Brown<br/>**CHESTNUT** - Red<br/>**CREAMY** - Beige<br/>**DARK_BROWN** - Dark Brown<br/>**DO_NOT_CHANGE** - Don't Change<br/>**GRAY** - Grey<br/>**WHITE** - White                           | Horse Color   |
| horse_style | Marker<br/>**BLACK_DOTS** - Dark Dots on Back<br/>**DO_NOT_CHANGE** - Don't Change<br/>**NONE** - No Pattern<br/>**WHITE** - White stripes on legs and head<br/>**WHITEFIELD** - Large White Fields<br/>**WHITE_DOTS** - Small White Dots | Horse Pattern |

<h3 id=entity_set_immune_to_zombification>
  <code>entity::set_immune_to_zombification</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Immune To Zombification\
**Action type:** Action without value\
**Description:** Sets entity immunity to zombification.\
**Work_with:**\
&nbsp;&nbsp;Piglins\
&nbsp;&nbsp;Brute piglins\
&nbsp;&nbsp;Hoglins

**Usage example:**
```ts
entity::set_immune_to_zombification("FALSE");

//Or dry by keywords

entity::set_immune_to_zombification(is_immune="FALSE");
```

**Arguments:**

| ID        | Type                                                   | Description               |
|-----------|--------------------------------------------------------|---------------------------|
| is_immune | Marker<br/>**FALSE** - Turn off<br/>**TRUE** - Turn on | Immunity to zombification |

<h3 id=entity_set_interaction_responsive>
  <code>entity::set_interaction_responsive</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Interaction Entity Responsiveness\
**Action type:** Action without value\
**Description:** Sets whether an interaction entity will be responsive to interactions.\
**Work_with:**\
&nbsp;&nbsp;Interaction Entities

**Usage example:**
```ts
entity::set_interaction_responsive("FALSE");

//Or dry by keywords

entity::set_interaction_responsive(responsive="FALSE");
```

**Arguments:**

| ID         | Type                                                 | Description |
|------------|------------------------------------------------------|-------------|
| responsive | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Responsive  |

<h3 id=entity_set_interaction_size>
  <code>entity::set_interaction_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Interaction Entity Size\
**Action type:** Action without value\
**Description:** Sets the horizontal and vertical sizes of an interaction entity.\
**Work_with:**\
&nbsp;&nbsp;Interaction Entities

**Usage example:**
```ts
entity::set_interaction_size(1, 2);

//Or dry by keywords

entity::set_interaction_size(width=1, height=2);
```

**Arguments:**

| ID     | Type   | Description     |
|--------|--------|-----------------|
| width  | Number | Horizontal Size |
| height | Number | Vertical Size   |

<h3 id=entity_set_invisible>
  <code>entity::set_invisible</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Invisible Mode\
**Action type:** Action without value\
**Description:** Sets an entity to invisible mode.

**Usage example:**
```ts
entity::set_invisible("FALSE");

//Or dry by keywords

entity::set_invisible(invisible="FALSE");
```

**Arguments:**

| ID        | Type                                                 | Description    |
|-----------|------------------------------------------------------|----------------|
| invisible | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Invisible Mode |

<h3 id=entity_set_invulnerability_ticks>
  <code>entity::set_invulnerability_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Invulnerability Duration\
**Action type:** Action without value\
**Description:** Sets the invulnerability duration for a creature.

**Usage example:**
```ts
entity::set_invulnerability_ticks(1);

//Or dry by keywords

entity::set_invulnerability_ticks(ticks=1);
```

**Arguments:**

| ID    | Type   | Description                      |
|-------|--------|----------------------------------|
| ticks | Number | Invulnerability Duration (Ticks) |

<h3 id=entity_set_invulnerable>
  <code>entity::set_invulnerable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Invulnerable\
**Action type:** Action without value\
**Description:** Sets an entity's invulnerability, but can deal damage in creative mode.

**Usage example:**
```ts
entity::set_invulnerable("FALSE");

//Or dry by keywords

entity::set_invulnerable(invulnerable="FALSE");
```

**Arguments:**

| ID           | Type                                                 | Description  |
|--------------|------------------------------------------------------|--------------|
| invulnerable | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Invulnerable |

<h3 id=entity_set_item>
  <code>entity::set_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Item Type\
**Action type:** Action without value\
**Description:** Sets a specific type (ID) to an Item entity.\
**Work_with:**\
&nbsp;&nbsp;Items

**Usage example:**
```ts
entity::set_item(item("stick"));

//Or dry by keywords

entity::set_item(item=item("stick"));
```

**Arguments:**

| ID   | Type | Description |
|------|------|-------------|
| item | Item | Item to Set |

<h3 id=entity_set_item_display_item>
  <code>entity::set_item_display_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Display Item\
**Action type:** Action without value\
**Description:** Sets the display item to the item renderer.\
**Work_with:**\
&nbsp;&nbsp;Item Renderers

**Usage example:**
```ts
entity::set_item_display_item(item("stick"));

//Or dry by keywords

entity::set_item_display_item(displayed_item=item("stick"));
```

**Arguments:**

| ID             | Type | Description    |
|----------------|------|----------------|
| displayed_item | Item | Displayed Item |

<h3 id=entity_set_item_display_model_type>
  <code>entity::set_item_display_model_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Model Type\
**Action type:** Action without value\
**Description:** Sets the type of the item's display model to the item renderer.\
**Work_with:**\
&nbsp;&nbsp;Item Renderers

**Usage example:**
```ts
entity::set_item_display_model_type("FIRSTPERSON_LEFTHAND");

//Or dry by keywords

entity::set_item_display_model_type(display_model_type="FIRSTPERSON_LEFTHAND");
```

**Arguments:**

| ID                 | Type                                                                                                                                                                                                                                                                                                                                                        | Description |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| display_model_type | Marker<br/>**FIRSTPERSON_LEFTHAND** - First Person Left Hand<br/>**FIRSTPERSON_RIGHTHAND** - First Person Right Hand<br/>**FIXED** - Fixed<br/>**GROUND** - On the ground<br/>**GUI** - Inventory<br/>**HEAD** - Head<br/>**NONE** - Standard<br/>**THIRDPERSON_LEFTHAND** - Third Person Left Hand<br/>**THIRDPERSON_RIGHTHAND** - Third Person Right Hand | Model Type  |

<h3 id=entity_set_item_frame_item_drop_chance>
  <code>entity::set_item_frame_item_drop_chance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_item_frame_item_drop_chance.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_item_frame_item_drop_chance.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_item_frame_item_drop_chance.work_with.item_frame\
&nbsp;&nbsp;creative_plus.action.entity_set_item_frame_item_drop_chance.work_with.glow_item_frame

**Usage example:**
```ts
entity::set_item_frame_item_drop_chance(1);

//Or dry by keywords

entity::set_item_frame_item_drop_chance(drop_chance=1);
```

**Arguments:**

| ID          | Type   | Description                                                                           |
|-------------|--------|---------------------------------------------------------------------------------------|
| drop_chance | Number | creative_plus.action.entity_set_item_frame_item_drop_chance.argument.drop_chance.name |

<h3 id=entity_set_item_in_frame>
  <code>entity::set_item_in_frame</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item in Frame\
**Action type:** Action without value\
**Description:** Sets the specified item in a frame.\
**Work_with:**\
&nbsp;&nbsp;Within Frames

**Usage example:**
```ts
entity::set_item_in_frame(item("stick"), "FALSE");

//Or dry by keywords

entity::set_item_in_frame(item=item("stick"), play_sound="FALSE");
```

**Arguments:**

| ID         | Type                                                                                                                                                                                                     | Description                                                            |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| item       | Item                                                                                                                                                                                                     | Item                                                                   |
| play_sound | Marker<br/>**FALSE** - creative_plus.action.entity_set_item_in_frame.argument.play_sound.enum.false.name<br/>**TRUE** - creative_plus.action.entity_set_item_in_frame.argument.play_sound.enum.true.name | creative_plus.action.entity_set_item_in_frame.argument.play_sound.name |

<h3 id=entity_set_item_owner>
  <code>entity::set_item_owner</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_item_owner.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_item_owner.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_item_owner.work_with.item

**Usage example:**
```ts
entity::set_item_owner("name_or_uuid");

//Or dry by keywords

entity::set_item_owner(name_or_uuid="name_or_uuid");
```

**Arguments:**

| ID           | Type | Description                                                           |
|--------------|------|-----------------------------------------------------------------------|
| name_or_uuid | Text | creative_plus.action.entity_set_item_owner.argument.name_or_uuid.name |

<h3 id=entity_set_llama_type>
  <code>entity::set_llama_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Llama Color\
**Action type:** Action without value\
**Description:** Sets the color of the llama.\
**Work_with:**\
&nbsp;&nbsp;Lamas

**Usage example:**
```ts
entity::set_llama_type("BROWN");

//Or dry by keywords

entity::set_llama_type(type="BROWN");
```

**Arguments:**

| ID   | Type                                                                                          | Description  |
|------|-----------------------------------------------------------------------------------------------|--------------|
| type | Marker<br/>**BROWN** - Brown<br/>**CREAMY** - Beige<br/>**GRAY** - Gray<br/>**WHITE** - White | Color to Set |

<h3 id=entity_set_location>
  <code>entity::set_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch By Vector\
**Action type:** Action without value\
**Description:** Launches an entity at the specified vector.

**Usage example:**
```ts
entity::set_location(vector(0,0,0), "FALSE");

//Or dry by keywords

entity::set_location(velocity=vector(0,0,0), increment="FALSE");
```

**Arguments:**

| ID        | Type                                                   | Description              |
|-----------|--------------------------------------------------------|--------------------------|
| velocity  | Vector                                                 | Motion Vector            |
| increment | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Consider current inertia |

<h3 id=entity_set_mannequin_description>
  <code>entity::set_mannequin_description</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_mannequin_description.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_mannequin_description.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_mannequin_description.work_with.mannequin

**Usage example:**
```ts
entity::set_mannequin_description("description");

//Or dry by keywords

entity::set_mannequin_description(description="description");
```

**Arguments:**

| ID          | Type | Description                                                                     |
|-------------|------|---------------------------------------------------------------------------------|
| description | Text | creative_plus.action.entity_set_mannequin_description.argument.description.name |

<h3 id=entity_set_mannequin_immovable>
  <code>entity::set_mannequin_immovable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_mannequin_immovable.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_mannequin_immovable.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_mannequin_immovable.work_with.mannequin

**Usage example:**
```ts
entity::set_mannequin_immovable("TRUE");

//Or dry by keywords

entity::set_mannequin_immovable(immovable="TRUE");
```

**Arguments:**

| ID        | Type                                                                                                                                                                                                               | Description                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| immovable | Marker<br/>**TRUE** - creative_plus.action.entity_set_mannequin_immovable.argument.immovable.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_mannequin_immovable.argument.immovable.enum.false.name | creative_plus.action.entity_set_mannequin_immovable.argument.immovable.name |

<h3 id=entity_set_mannequin_main_hand>
  <code>entity::set_mannequin_main_hand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_mannequin_main_hand.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_mannequin_main_hand.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_mannequin_main_hand.work_with.mannequin

**Usage example:**
```ts
entity::set_mannequin_main_hand("RIGHT");

//Or dry by keywords

entity::set_mannequin_main_hand(hand="RIGHT");
```

**Arguments:**

| ID   | Type                                                                                                                                                                                                     | Description                                                            |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| hand | Marker<br/>**RIGHT** - creative_plus.action.entity_set_mannequin_main_hand.argument.hand.enum.right.name<br/>**LEFT** - creative_plus.action.entity_set_mannequin_main_hand.argument.hand.enum.left.name | creative_plus.action.entity_set_mannequin_main_hand.argument.hand.name |

<h3 id=entity_set_mannequin_skin>
  <code>entity::set_mannequin_skin</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_mannequin_skin.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_mannequin_skin.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_mannequin_skin.work_with.mannequin

**Usage example:**
```ts
entity::set_mannequin_skin("name_or_uuid", "MOJANG");

//Or dry by keywords

entity::set_mannequin_skin(name_or_uuid="name_or_uuid", server_type="MOJANG");
```

**Arguments:**

| ID           | Type                                                                                                                                                                                                               | Description                                                               |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| name_or_uuid | Text                                                                                                                                                                                                               | creative_plus.action.entity_set_mannequin_skin.argument.name_or_uuid.name |
| server_type  | Marker<br/>**MOJANG** - creative_plus.action.entity_set_mannequin_skin.argument.server_type.enum.mojang.name<br/>**SERVER** - creative_plus.action.entity_set_mannequin_skin.argument.server_type.enum.server.name | creative_plus.action.entity_set_mannequin_skin.argument.server_type.name  |

<h3 id=entity_set_mannequin_skin_model>
  <code>entity::set_mannequin_skin_model</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_mannequin_skin_model.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_mannequin_skin_model.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_mannequin_skin_model.work_with.mannequin

**Usage example:**
```ts
entity::set_mannequin_skin_model("CLASSIC");

//Or dry by keywords

entity::set_mannequin_skin_model(model="CLASSIC");
```

**Arguments:**

| ID    | Type                                                                                                                                                                                                                                                                                                                 | Description                                                              |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| model | Marker<br/>**CLASSIC** - creative_plus.action.entity_set_mannequin_skin_model.argument.model.enum.classic.name<br/>**SLIM** - creative_plus.action.entity_set_mannequin_skin_model.argument.model.enum.slim.name<br/>**UNSET** - creative_plus.action.entity_set_mannequin_skin_model.argument.model.enum.unset.name | creative_plus.action.entity_set_mannequin_skin_model.argument.model.name |

<h3 id=entity_set_mannequin_skin_parts>
  <code>entity::set_mannequin_skin_parts</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_mannequin_skin_parts.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_mannequin_skin_parts.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_mannequin_skin_parts.work_with.mannequin

**Usage example:**
```ts
entity::set_mannequin_skin_parts("TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE");

//Or dry by keywords

entity::set_mannequin_skin_parts(hat="TRUE", jacket="TRUE", left_sleeve="TRUE", right_sleeve="TRUE", left_pants="TRUE", right_pants="TRUE", cape="TRUE");
```

**Arguments:**

| ID           | Type                                                                                                                                                                                                                                                                                                                                      | Description                                                                     |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| hat          | Marker<br/>**TRUE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.hat.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.hat.enum.false.name<br/>**NOT_SET** - creative_plus.action.entity_set_mannequin_skin_parts.argument.hat.enum.not_set.name                            | creative_plus.action.entity_set_mannequin_skin_parts.argument.hat.name          |
| jacket       | Marker<br/>**TRUE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.jacket.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.jacket.enum.false.name<br/>**NOT_SET** - creative_plus.action.entity_set_mannequin_skin_parts.argument.jacket.enum.not_set.name                   | creative_plus.action.entity_set_mannequin_skin_parts.argument.jacket.name       |
| left_sleeve  | Marker<br/>**TRUE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.left_sleeve.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.left_sleeve.enum.false.name<br/>**NOT_SET** - creative_plus.action.entity_set_mannequin_skin_parts.argument.left_sleeve.enum.not_set.name    | creative_plus.action.entity_set_mannequin_skin_parts.argument.left_sleeve.name  |
| right_sleeve | Marker<br/>**TRUE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.right_sleeve.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.right_sleeve.enum.false.name<br/>**NOT_SET** - creative_plus.action.entity_set_mannequin_skin_parts.argument.right_sleeve.enum.not_set.name | creative_plus.action.entity_set_mannequin_skin_parts.argument.right_sleeve.name |
| left_pants   | Marker<br/>**TRUE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.left_pants.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.left_pants.enum.false.name<br/>**NOT_SET** - creative_plus.action.entity_set_mannequin_skin_parts.argument.left_pants.enum.not_set.name       | creative_plus.action.entity_set_mannequin_skin_parts.argument.left_pants.name   |
| right_pants  | Marker<br/>**TRUE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.right_pants.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.right_pants.enum.false.name<br/>**NOT_SET** - creative_plus.action.entity_set_mannequin_skin_parts.argument.right_pants.enum.not_set.name    | creative_plus.action.entity_set_mannequin_skin_parts.argument.right_pants.name  |
| cape         | Marker<br/>**TRUE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.cape.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_mannequin_skin_parts.argument.cape.enum.false.name<br/>**NOT_SET** - creative_plus.action.entity_set_mannequin_skin_parts.argument.cape.enum.not_set.name                         | creative_plus.action.entity_set_mannequin_skin_parts.argument.cape.name         |

<h3 id=entity_set_mannequin_skin_patch>
  <code>entity::set_mannequin_skin_patch</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_mannequin_skin_patch.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_mannequin_skin_patch.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.entity_set_mannequin_skin_patch.additional_information.empty_key_to_unset\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_mannequin_skin_patch.work_with.mannequin

**Usage example:**
```ts
entity::set_mannequin_skin_patch("texture_key", "BODY");

//Or dry by keywords

entity::set_mannequin_skin_patch(texture_key="texture_key", patch_target="BODY");
```

**Arguments:**

| ID           | Type                                                                                                                                                                                                                                                                                                                                  | Description                                                                     |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| texture_key  | Text                                                                                                                                                                                                                                                                                                                                  | creative_plus.action.entity_set_mannequin_skin_patch.argument.texture_key.name  |
| patch_target | Marker<br/>**BODY** - creative_plus.action.entity_set_mannequin_skin_patch.argument.patch_target.enum.body.name<br/>**CAPE** - creative_plus.action.entity_set_mannequin_skin_patch.argument.patch_target.enum.cape.name<br/>**ELYTRA** - creative_plus.action.entity_set_mannequin_skin_patch.argument.patch_target.enum.elytra.name | creative_plus.action.entity_set_mannequin_skin_patch.argument.patch_target.name |

<h3 id=entity_set_marker>
  <code>entity::set_marker</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Marker Mode\
**Action type:** Action without value\
**Description:** Sets the armor rack marker mode.\
**Work_with:**\
&nbsp;&nbsp;Armor Stands

**Usage example:**
```ts
entity::set_marker("FALSE");

//Or dry by keywords

entity::set_marker(marker="FALSE");
```

**Arguments:**

| ID     | Type                                                 | Description |
|--------|------------------------------------------------------|-------------|
| marker | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Marker Mode |

<h3 id=entity_set_max_health>
  <code>entity::set_max_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Max Health\
**Action type:** Action without value\
**Description:** Sets the maximum amount of health for an entity.

**Usage example:**
```ts
entity::set_max_health(1, "FALSE");

//Or dry by keywords

entity::set_max_health(max_health=1, heal_to_max="FALSE");
```

**Arguments:**

| ID          | Type                                           | Description   |
|-------------|------------------------------------------------|---------------|
| max_health  | Number                                         | Max Health    |
| heal_to_max | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes | Heal Creature |

<h3 id=entity_set_merchant_recipe>
  <code>entity::set_merchant_recipe</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Merchant Recipe\
**Action type:** Action without value\
**Description:** Sets an item to a Villager for certain items at the specified index.\
**Work_with:**\
&nbsp;&nbsp;Villagers\
&nbsp;&nbsp;Wandering Traders

**Usage example:**
```ts
entity::set_merchant_recipe(item("stick"), 1, 2, item("stick"), 3, item("stick"), 4, 5, 6, 7, "APPEND", "FALSE", "FALSE");

//Or dry by keywords

entity::set_merchant_recipe(result=item("stick"), uses=1, max_uses=2, ingredient_one=item("stick"), villager_experience=3, ingredient_two=item("stick"), price_multiplifier=4, demand=5, index=6, special_price=7, mode="APPEND", experience_reward="FALSE", ignore_discounts="FALSE");
```

**Arguments:**

| ID                  | Type                                                 | Description         |
|---------------------|------------------------------------------------------|---------------------|
| result              | Item                                                 | Purchasable Item    |
| uses                | Number                                               | Number of Uses      |
| max_uses            | Number                                               | Max Uses            |
| ingredient_one      | Item                                                 | First Item          |
| villager_experience | Number                                               | Villager Experience |
| ingredient_two      | Item                                                 | Second Item         |
| price_multiplifier  | Number                                               | Price Multiplier    |
| demand              | Number                                               | Product Demand      |
| index               | Number                                               | Product Index       |
| special_price       | Number                                               | Special Price       |
| mode                | Marker<br/>**APPEND** - Add<br/>**MERGE** - Replace  | Set Mode            |
| experience_reward   | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Experience Reward   |
| ignore_discounts    | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Ignore Discounts    |

<h3 id=entity_set_minecart_block>
  <code>entity::set_minecart_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block to Minecart\
**Action type:** Action without value\
**Description:** Sets the specified block into the Minecart.\
**Work_with:**\
&nbsp;&nbsp;Minecarts

**Usage example:**
```ts
entity::set_minecart_block("minecraft:oak_log[axis=x]", 1);

//Or dry by keywords

entity::set_minecart_block(block="minecraft:oak_log[axis=x]", block_offset=1);
```

**Arguments:**

| ID           | Type   | Description   |
|--------------|--------|---------------|
| block        | Block  | Block to set  |
| block_offset | Number | Offset Blocks |

<h3 id=entity_set_mob_aggressive>
  <code>entity::set_mob_aggressive</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Mob Aggressive\
**Action type:** Action without value\
**Description:** Sets the agression of the mob.\
**Work_with:**\
&nbsp;&nbsp;Drowned\
&nbsp;&nbsp;Piglin\
&nbsp;&nbsp;Skeleton\
&nbsp;&nbsp;Zombie\
&nbsp;&nbsp;Zombie Villager\
&nbsp;&nbsp;Illusioner\
&nbsp;&nbsp;Vindicator\
&nbsp;&nbsp;Panda\
&nbsp;&nbsp;Pillager\
&nbsp;&nbsp;Piglin Brute

**Usage example:**
```ts
entity::set_mob_aggressive("FALSE");

//Or dry by keywords

entity::set_mob_aggressive(aggressive="FALSE");
```

**Arguments:**

| ID         | Type                                             | Description |
|------------|--------------------------------------------------|-------------|
| aggressive | Marker<br/>**FALSE** - False<br/>**TRUE** - True | Aggressive  |

<h3 id=entity_set_mushroom_cow_type>
  <code>entity::set_mushroom_cow_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Mushroom Cow Type\
**Action type:** Action without value\
**Description:** Sets the mushroom cow type.\
**Work_with:**\
&nbsp;&nbsp;Mushroom Cows

**Usage example:**
```ts
entity::set_mushroom_cow_type("BROWN");

//Or dry by keywords

entity::set_mushroom_cow_type(cow_type="BROWN");
```

**Arguments:**

| ID       | Type                                           | Description       |
|----------|------------------------------------------------|-------------------|
| cow_type | Marker<br/>**BROWN** - Brown<br/>**RED** - Red | Mushroom Cow Type |

<h3 id=entity_set_no_physics>
  <code>entity::no_physics</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Physics\
**Action type:** Action without value\
**Description:** Toggles whether an entity is affected by physics.

**Usage example:**
```ts
entity::no_physics("TRUE");

//Or dry by keywords

entity::no_physics(no_physics="TRUE");
```

**Arguments:**

| ID         | Type                                             | Description |
|------------|--------------------------------------------------|-------------|
| no_physics | Marker<br/>**TRUE** - False<br/>**FALSE** - True | Physics     |

<h3 id=entity_set_painting_art>
  <code>entity::set_painting_art</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_painting_art.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_painting_art.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_painting_art.work_with.painting

**Usage example:**
```ts
entity::set_painting_art("art", "TRUE");

//Or dry by keywords

entity::set_painting_art(art="art", force="TRUE");
```

**Arguments:**

| ID    | Type                                                                                                                                                                                         | Description                                                      |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| art   | Text                                                                                                                                                                                         | creative_plus.action.entity_set_painting_art.argument.art.name   |
| force | Marker<br/>**TRUE** - creative_plus.action.entity_set_painting_art.argument.force.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_painting_art.argument.force.enum.false.name | creative_plus.action.entity_set_painting_art.argument.force.name |

<h3 id=entity_set_panda_gene>
  <code>entity::set_panda_gene</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Panda Gene\
**Action type:** Action without value\
**Description:** Sets the panda gene. This affects their behavior and appearance.\
**Work_with:**\
&nbsp;&nbsp;Pandas

**Usage example:**
```ts
entity::set_panda_gene("BOTH", "AGGRESSIVE");

//Or dry by keywords

entity::set_panda_gene(gene="BOTH", gene_type="AGGRESSIVE");
```

**Arguments:**

| ID        | Type                                                                                                                                                                              | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| gene      | Marker<br/>**BOTH** - Both Genes<br/>**HIDDEN** - Hidden Gene<br/>**MAIN** - Main Gene                                                                                            | Gene        |
| gene_type | Marker<br/>**AGGRESSIVE** - Aggressive<br/>**BROWN** - Severe<br/>**LAZY** - Lazy<br/>**NORMAL** - Normal<br/>**PLAYFUL** - Playful<br/>**WEAK** - Weak<br/>**WORRIED** - Worried | Gene Type   |

<h3 id=entity_set_panda_on_back>
  <code>entity::set_panda_on_back</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Panda Sitting\
**Action type:** Action without value\
**Description:** Toggles whether a panda is sitting.\
**Work_with:**\
&nbsp;&nbsp;Panda

**Usage example:**
```ts
entity::set_panda_on_back("TRUE");

//Or dry by keywords

entity::set_panda_on_back(on_back="TRUE");
```

**Arguments:**

| ID      | Type                                             | Description |
|---------|--------------------------------------------------|-------------|
| on_back | Marker<br/>**TRUE** - True<br/>**FALSE** - False | Sitting     |

<h3 id=entity_set_panda_rolling>
  <code>entity::set_panda_rolling</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Panda Rolling\
**Action type:** Action without value\
**Description:** Set whether a panda is rolling.\
**Work_with:**\
&nbsp;&nbsp;Panda

**Usage example:**
```ts
entity::set_panda_rolling("TRUE");

//Or dry by keywords

entity::set_panda_rolling(rolling="TRUE");
```

**Arguments:**

| ID      | Type                                             | Description |
|---------|--------------------------------------------------|-------------|
| rolling | Marker<br/>**TRUE** - True<br/>**FALSE** - False | Rolling     |

<h3 id=entity_set_panda_sad_ticks>
  <code>entity::set_panda_sad_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Panda Sad Time\
**Action type:** Action without value\
**Description:** Sets how long a panda is sad for in ticks.\
**Work_with:**\
&nbsp;&nbsp;Panda

**Usage example:**
```ts
entity::set_panda_sad_ticks(1);

//Or dry by keywords

entity::set_panda_sad_ticks(sad_ticks=1);
```

**Arguments:**

| ID        | Type   | Description |
|-----------|--------|-------------|
| sad_ticks | Number | Sad Time    |

<h3 id=entity_set_parrot_type>
  <code>entity::set_parrot_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Parrot Type\
**Action type:** Action without value\
**Description:** Sets the parrot type.\
**Work_with:**\
&nbsp;&nbsp;Parrots

**Usage example:**
```ts
entity::set_parrot_type("BLUE");

//Or dry by keywords

entity::set_parrot_type(parrot_type="BLUE");
```

**Arguments:**

| ID          | Type                                                                                                            | Description |
|-------------|-----------------------------------------------------------------------------------------------------------------|-------------|
| parrot_type | Marker<br/>**BLUE** - Blue<br/>**CYAN** - Turquoise<br/>**GRAY** - Grey<br/>**GREEN** - Green<br/>**RED** - Red | Parrot Type |

<h3 id=entity_set_persistence>
  <code>entity::set_persistence</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Persistence\
**Action type:** Action without value\
**Description:** Sets whether an item or falling block will persist.\
**Work_with:**\
&nbsp;&nbsp;Entity\
&nbsp;&nbsp;Falling Blocks

**Usage example:**
```ts
entity::set_persistence("FALSE");

//Or dry by keywords

entity::set_persistence(persistence="FALSE");
```

**Arguments:**

| ID          | Type                                                                    | Description       |
|-------------|-------------------------------------------------------------------------|-------------------|
| persistence | Marker<br/>**FALSE** - Will disappear<br/>**TRUE** - Will not disappear | Entity Disappears |

<h3 id=entity_set_persistent>
  <code>entity::set_persistent</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_persistent.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_persistent.description

**Usage example:**
```ts
entity::set_persistent("TRUE");

//Or dry by keywords

entity::set_persistent(persistent="TRUE");
```

**Arguments:**

| ID         | Type                                                                                                                                                                                               | Description                                                         |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| persistent | Marker<br/>**TRUE** - creative_plus.action.entity_set_persistent.argument.persistent.enum.true.name<br/>**FALSE** - creative_plus.action.entity_set_persistent.argument.persistent.enum.false.name | creative_plus.action.entity_set_persistent.argument.persistent.name |

<h3 id=entity_set_pickup>
  <code>entity::set_pickup</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Entity Set Pickup\
**Action type:** Action without value\
**Description:** Sets which entities can pick up.\
**Work_with:**\
&nbsp;&nbsp;Item Entities

**Usage example:**
```ts
entity::set_pickup("TRUE", "TRUE");

//Or dry by keywords

entity::set_pickup(can_mob_pickup="TRUE", can_player_pickup="TRUE");
```

**Arguments:**

| ID                | Type                                             | Description |
|-------------------|--------------------------------------------------|-------------|
| can_mob_pickup    | Marker<br/>**TRUE** - True<br/>**FALSE** - False | Mobs        |
| can_player_pickup | Marker<br/>**TRUE** - True<br/>**FALSE** - False | Players     |

<h3 id=entity_set_pickup_delay>
  <code>entity::set_pickup_delay</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Pickup Delay\
**Action type:** Action without value\
**Description:** Sets the number of ticks an item cannot be picked up.\
**Work_with:**\
&nbsp;&nbsp;Items

**Usage example:**
```ts
entity::set_pickup_delay(1);

//Or dry by keywords

entity::set_pickup_delay(delay=1);
```

**Arguments:**

| ID    | Type   | Description |
|-------|--------|-------------|
| delay | Number | Delay       |

<h3 id=entity_set_pig_type>
  <code>entity::set_pig_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_pig_type.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_pig_type.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_pig_type.work_with.pig

**Usage example:**
```ts
entity::set_pig_type("COLD");

//Or dry by keywords

entity::set_pig_type(variant="COLD");
```

**Arguments:**

| ID      | Type                                                                                                                                                                                                                                                                                     | Description                                                    |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| variant | Marker<br/>**COLD** - creative_plus.action.entity_set_pig_type.argument.variant.enum.cold.name<br/>**WARM** - creative_plus.action.entity_set_pig_type.argument.variant.enum.warm.name<br/>**TEMPERATE** - creative_plus.action.entity_set_pig_type.argument.variant.enum.temperate.name | creative_plus.action.entity_set_pig_type.argument.variant.name |

<h3 id=entity_set_piglin_able_to_hunt>
  <code>entity::set_piglin_able_to_hunt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Piglin Able To Hunt\
**Action type:** Action without value\
**Description:** Sets the status of the Piglin's hunting state.\
**Work_with:**\
&nbsp;&nbsp;Piglin

**Usage example:**
```ts
entity::set_piglin_able_to_hunt("FALSE");

//Or dry by keywords

entity::set_piglin_able_to_hunt(able="FALSE");
```

**Arguments:**

| ID   | Type                                                      | Description |
|------|-----------------------------------------------------------|-------------|
| able | Marker<br/>**FALSE** - Not hunting<br/>**TRUE** - Hunting | Status      |

<h3 id=entity_set_piglin_charging_crossbow>
  <code>entity::set_piglin_charging_crossbow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Pigling Charging Crossbow\
**Action type:** Action without value\
**Description:** Sets the Piglin's crossbow loaded status.\
**Work_with:**\
&nbsp;&nbsp;Piglin

**Usage example:**
```ts
entity::set_piglin_charging_crossbow("FALSE");

//Or dry by keywords

entity::set_piglin_charging_crossbow(charging="FALSE");
```

**Arguments:**

| ID       | Type                                                    | Description |
|----------|---------------------------------------------------------|-------------|
| charging | Marker<br/>**FALSE** - Not loaded<br/>**TRUE** - Loaded | Status      |

<h3 id=entity_set_piglin_dancing>
  <code>entity::set_piglin_dancing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Piglin Dancing\
**Action type:** Action without value\
**Description:** Plays the dancing animation for a Piglin.\
**Additional info:**\
&nbsp;&nbsp;If the value is less than zero, the Piglin dances forever.\
**Work_with:**\
&nbsp;&nbsp;Piglin

**Usage example:**
```ts
entity::set_piglin_dancing(1);

//Or dry by keywords

entity::set_piglin_dancing(dancing_time=1);
```

**Arguments:**

| ID           | Type   | Description             |
|--------------|--------|-------------------------|
| dancing_time | Number | Dancing time (in ticks) |

<h3 id=entity_set_pose>
  <code>entity::set_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Pose\
**Action type:** Action without value\
**Description:** Sets a specific pose for an entity.

**Usage example:**
```ts
entity::set_pose("CROAKING");

//Or dry by keywords

entity::set_pose(pose="CROAKING");
```

**Arguments:**

| ID   | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description  |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| pose | Marker<br/>**CROAKING** - Croaking (for Toads)<br/>**CROUCHING** - Crouching<br/>**DIGGING** - Digging (For Guardian)<br/>**DYING** - Death<br/>**EMERGING** - Emerging from the Earth (for Guardian)<br/>**FALL_FLYING** - Elytra Flying<br/>**INHALING** - creative_plus.action.entity_set_pose.argument.pose.enum.inhaling.name<br/>**LONG_JUMPING** - Long Jump<br/>**ROARING** - Roar (for Guardian)<br/>**SHOOTING** - creative_plus.action.entity_set_pose.argument.pose.enum.shooting.name<br/>**SITTING** - Sitting<br/>**SLEEPING** - Sleeping<br/>**SLIDING** - creative_plus.action.entity_set_pose.argument.pose.enum.sliding.name<br/>**SNEAKING** - creative_plus.action.entity_set_pose.argument.pose.enum.sneaking.name<br/>**SNIFFING** - Sniffing (for Guardian)<br/>**SPIN_ATTACK** - Use Thruster<br/>**STANDING** - Normal State<br/>**SWIMMING** - Swimming<br/>**USING_TONGUE** - Using Tongue (For Toads) | Display Pose |

<h3 id=entity_set_potion_cloud_radius>
  <code>entity::set_potion_cloud_radius</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Effect Cloud Radius\
**Action type:** Action without value\
**Description:** Sets the radius of the effect cloud and how fast it expands.\
**Additional info:**\
&nbsp;&nbsp;Expansion Speed - The amount of change in radius per tick, can be negative.\
**Work_with:**\
&nbsp;&nbsp;Effect Cloud

**Usage example:**
```ts
entity::set_potion_cloud_radius(1, 2);

//Or dry by keywords

entity::set_potion_cloud_radius(radius=1, shrinking_speed=2);
```

**Arguments:**

| ID              | Type   | Description |
|-----------------|--------|-------------|
| radius          | Number | Radius      |
| shrinking_speed | Number | Speed       |

<h3 id=entity_set_primed_tnt_block>
  <code>entity::set_primed_tnt_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Primed Tnt Block\
**Action type:** Action without value\
**Description:** Disguises the Primed TNT as another block.\
**Work_with:**\
&nbsp;&nbsp;Primed TNT

**Usage example:**
```ts
entity::set_primed_tnt_block("minecraft:oak_log[axis=x]");

//Or dry by keywords

entity::set_primed_tnt_block(block="minecraft:oak_log[axis=x]");
```

**Arguments:**

| ID    | Type  | Description |
|-------|-------|-------------|
| block | Block | Block       |

<h3 id=entity_set_projectile_display_item>
  <code>entity::set_projectile_display_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Projectile Item\
**Action type:** Action without value\
**Description:** Sets the projectile's visible item.\
**Work_with:**\
&nbsp;&nbsp;Snowballs\
&nbsp;&nbsp;Eggs\
&nbsp;&nbsp;Small fireballs\
&nbsp;&nbsp;Fireballs\
&nbsp;&nbsp;Ender Pearl\
&nbsp;&nbsp;Experience Bubbles\
&nbsp;&nbsp;Okami Edge\
&nbsp;&nbsp;Thrown Potions

**Usage example:**
```ts
entity::set_projectile_display_item(item("stick"));

//Or dry by keywords

entity::set_projectile_display_item(item=item("stick"));
```

**Arguments:**

| ID   | Type | Description |
|------|------|-------------|
| item | Item | Item to Set |

<h3 id=entity_set_projectile_power>
  <code>entity::set_projectile_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Projectile Vector Power\
**Action type:** Action without value\
**Description:** Sets the projectile's motion vector.\
**Work_with:**\
&nbsp;&nbsp;Fireball\
&nbsp;&nbsp;Dragon Fireball\
&nbsp;&nbsp;Wither Skull

**Usage example:**
```ts
entity::set_projectile_power(vector(0,0,0));

//Or dry by keywords

entity::set_projectile_power(power=vector(0,0,0));
```

**Arguments:**

| ID    | Type   | Description   |
|-------|--------|---------------|
| power | Vector | Motion vector |

<h3 id=entity_set_projectile_shooter>
  <code>entity::set_projectile_shooter</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Projectile Shooter\
**Action type:** Action without value\
**Description:** Sets the specified creature as a projectile shooter.

**Usage example:**
```ts
entity::set_projectile_shooter("uuid");

//Or dry by keywords

entity::set_projectile_shooter(uuid="uuid");
```

**Arguments:**

| ID   | Type | Description                 |
|------|------|-----------------------------|
| uuid | Text | Name or UUID of the shooter |

<h3 id=entity_set_rabbit_type>
  <code>entity::set_rabbit_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rabbit Type\
**Action type:** Action without value\
**Description:** Sets the rabbit type.\
**Work_with:**\
&nbsp;&nbsp;Rabbits

**Usage example:**
```ts
entity::set_rabbit_type("BLACK");

//Or dry by keywords

entity::set_rabbit_type(rabbit_type="BLACK");
```

**Arguments:**

| ID          | Type                                                                                                                                                                                                                 | Description |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| rabbit_type | Marker<br/>**BLACK** - Black<br/>**BLACK_AND_WHITE** - Black and White<br/>**BROWN** - Brown<br/>**GOLD** - Gold<br/>**SALT_AND_PEPPER** - White Brown<br/>**THE_KILLER_BUNNY** - Killer Bunny<br/>**WHITE** - White | Rabbit Type |

<h3 id=entity_set_rearing>
  <code>entity::set_rearing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Horse Pose\
**Action type:** Action without value\
**Description:** Sets whether the horse will stand on its hind legs.\
**Work_with:**\
&nbsp;&nbsp;Horses

**Usage example:**
```ts
entity::set_rearing("FALSE");

//Or dry by keywords

entity::set_rearing(rearing="FALSE");
```

**Arguments:**

| ID      | Type                                                                        | Description |
|---------|-----------------------------------------------------------------------------|-------------|
| rearing | Marker<br/>**FALSE** - Regular State<br/>**TRUE** - Stand on your hind legs | Horse Pose  |

<h3 id=entity_set_riptiding>
  <code>entity::set_riptiding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Riptiding Animation\
**Action type:** Action without value\
**Description:** Sets the animation for an entity to use the Riptiding Trident Enchantment.

**Usage example:**
```ts
entity::set_riptiding("FALSE");

//Or dry by keywords

entity::set_riptiding(riptiding="FALSE");
```

**Arguments:**

| ID        | Type                                                 | Description         |
|-----------|------------------------------------------------------|---------------------|
| riptiding | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Riptiding Animation |

<h3 id=entity_set_rotation>
  <code>entity::set_rotation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation\
**Action type:** Action without value\
**Description:** Sets the rotation of an entity.

**Usage example:**
```ts
entity::set_rotation(1, 2);

//Or dry by keywords

entity::set_rotation(yaw=1, pitch=2);
```

**Arguments:**

| ID    | Type   | Description               |
|-------|--------|---------------------------|
| yaw   | Number | Horizontal rotation (yaw) |
| pitch | Number | Pitch                     |

<h3 id=entity_set_rotation_by_vector>
  <code>entity::set_rotation_by_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation By Vector\
**Action type:** Action without value\
**Description:** Sets the entity rotation by vector.

**Usage example:**
```ts
entity::set_rotation_by_vector(vector(0,0,0));

//Or dry by keywords

entity::set_rotation_by_vector(vector=vector(0,0,0));
```

**Arguments:**

| ID     | Type   | Description      |
|--------|--------|------------------|
| vector | Vector | Vector to Rotate |

<h3 id=entity_set_sheep_sheared>
  <code>entity::set_sheep_sheared</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sheep Wool\
**Action type:** Action without value\
**Description:** Sets whether sheep will have wool.\
**Work_with:**\
&nbsp;&nbsp;Sheep

**Usage example:**
```ts
entity::set_sheep_sheared("FALSE");

//Or dry by keywords

entity::set_sheep_sheared(sheared="FALSE");
```

**Arguments:**

| ID      | Type                                               | Description      |
|---------|----------------------------------------------------|------------------|
| sheared | Marker<br/>**FALSE** - No Fur<br/>**TRUE** - Sheep | Presence of Wool |

<h3 id=entity_set_shulker_bullet_target>
  <code>entity::set_shulker_bullet_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Shulker Bullet Target\
**Action type:** Action without value\
**Description:** Sets an attack target for a Shulker projectile.\
**Work_with:**\
&nbsp;&nbsp;Shulker Bullets

**Usage example:**
```ts
entity::set_shulker_bullet_target("target");

//Or dry by keywords

entity::set_shulker_bullet_target(target="target");
```

**Arguments:**

| ID     | Type | Description                |
|--------|------|----------------------------|
| target | Text | Name or UUID of the target |

<h3 id=entity_set_shulker_peek>
  <code>entity::set_shulker_peek</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Shulker Open Percentage\
**Action type:** Action without value\
**Description:** Sets the percentage of which a shulker is peeking out of its shell.\
**Work_with:**\
&nbsp;&nbsp;Shulker

**Usage example:**
```ts
entity::set_shulker_peek(1, "TRUE");

//Or dry by keywords

entity::set_shulker_peek(rolling=1, silent="TRUE");
```

**Arguments:**

| ID      | Type                                             | Description             |
|---------|--------------------------------------------------|-------------------------|
| rolling | Number                                           | Open Percentage         |
| silent  | Marker<br/>**TRUE** - False<br/>**FALSE** - True | Play shulker open sound |

<h3 id=entity_set_silenced>
  <code>entity::set_silenced</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Silence Entity\
**Action type:** Action without value\
**Description:** Removes entity sounds.

**Usage example:**
```ts
entity::set_silenced("FALSE");

//Or dry by keywords

entity::set_silenced(silenced="FALSE");
```

**Arguments:**

| ID       | Type                                                 | Description |
|----------|------------------------------------------------------|-------------|
| silenced | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Mute        |

<h3 id=entity_set_sitting>
  <code>entity::set_sitting</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sitting Mode\
**Action type:** Action without value\
**Description:** Sets the entity's sitting mode.\
**Work_with:**\
&nbsp;&nbsp;Wolf\
&nbsp;&nbsp;Cats\
&nbsp;&nbsp;Parrot\
&nbsp;&nbsp;Foxes\
&nbsp;&nbsp;Pandas

**Usage example:**
```ts
entity::set_sitting("FALSE");

//Or dry by keywords

entity::set_sitting(sitting="FALSE");
```

**Arguments:**

| ID      | Type                                                 | Description  |
|---------|------------------------------------------------------|--------------|
| sitting | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Setting Mode |

<h3 id=entity_set_size>
  <code>entity::set_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Size\
**Action type:** Action without value\
**Description:** Sets the size of an entity.\
**Work_with:**\
&nbsp;&nbsp;Slime\
&nbsp;&nbsp;Phantoms

**Usage example:**
```ts
entity::set_size(1);

//Or dry by keywords

entity::set_size(size=1);
```

**Arguments:**

| ID   | Type   | Description |
|------|--------|-------------|
| size | Number | Size        |

<h3 id=entity_set_sniffer_state>
  <code>entity::set_sniffer_state</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sniffer State\
**Action type:** Action without value\
**Description:** Sets a specific state for the sniffer.\
**Work_with:**\
&nbsp;&nbsp;Sniffer

**Usage example:**
```ts
entity::set_sniffer_state("DIGGING");

//Or dry by keywords

entity::set_sniffer_state(state="DIGGING");
```

**Arguments:**

| ID    | Type                                                                                                                                                                                                             | Description   |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| state | Marker<br/>**DIGGING** - Digging<br/>**FEELING_HAPPY** - Feels Happy<br/>**IDLING** - Normal State<br/>**RISING** - Rising<br/>**SCENTING** - Tracking<br/>**SEARCHING** - Searching<br/>**SNIFFING** - Sniffing | Sniffer State |

<h3 id=entity_set_snowman_pumpkin>
  <code>entity::set_snowman_pumpkin</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Pumpkin to Snow Golem\
**Action type:** Action without value\
**Description:** Sets the visibility of the pumpkin to the Snow Golem.\
**Work_with:**\
&nbsp;&nbsp;Snow Golems

**Usage example:**
```ts
entity::set_snowman_pumpkin("FALSE");

//Or dry by keywords

entity::set_snowman_pumpkin(pumpkin="FALSE");
```

**Arguments:**

| ID      | Type                                                 | Description        |
|---------|------------------------------------------------------|--------------------|
| pumpkin | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Pumpkin Visibility |

<h3 id=entity_set_tame>
  <code>entity::set_tame</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Tame Entity\
**Action type:** Action without value\
**Description:** Sets an entity's tame to the specified owner.\
**Work_with:**\
&nbsp;&nbsp;Wolf\
&nbsp;&nbsp;Cats\
&nbsp;&nbsp;Horses\
&nbsp;&nbsp;Mules\
&nbsp;&nbsp;Lamas\
&nbsp;&nbsp;Parrot

**Usage example:**
```ts
entity::set_tame("name_or_uuid");

//Or dry by keywords

entity::set_tame(name_or_uuid="name_or_uuid");
```

**Arguments:**

| ID           | Type | Description         |
|--------------|------|---------------------|
| name_or_uuid | Text | Entity name or UUID |

<h3 id=entity_set_target>
  <code>entity::set_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Target\
**Action type:** Action without value\
**Description:** Instructs the entity AI to target a specific entity.\
**Additional info:**\
&nbsp;&nbsp;Leave an empty slot in the Text field to remove the target.\
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:**
```ts
entity::set_target("name_or_uuid");

//Or dry by keywords

entity::set_target(name_or_uuid="name_or_uuid");
```

**Arguments:**

| ID           | Type | Description                |
|--------------|------|----------------------------|
| name_or_uuid | Text | Name or UUID of the target |

<h3 id=entity_set_text_display_alignment>
  <code>entity::set_text_display_alignment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text Alignment\
**Action type:** Action without value\
**Description:** Sets the text alignment of the text renderer.\
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:**
```ts
entity::set_text_display_alignment("CENTER");

//Or dry by keywords

entity::set_text_display_alignment(text_alignment="CENTER");
```

**Arguments:**

| ID             | Type                                                                     | Description    |
|----------------|--------------------------------------------------------------------------|----------------|
| text_alignment | Marker<br/>**CENTER** - Center<br/>**LEFT** - Left<br/>**RIGHT** - Right | Text Alignment |

<h3 id=entity_set_text_display_background>
  <code>entity::set_text_display_background</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Background Color\
**Action type:** Action without value\
**Description:** Sets the background color and transparency of the text renderer.\
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:**
```ts
entity::set_text_display_background("color_hexadecimal", 1);

//Or dry by keywords

entity::set_text_display_background(color_hexadecimal="color_hexadecimal", opacity=1);
```

**Arguments:**

| ID                | Type   | Description     |
|-------------------|--------|-----------------|
| color_hexadecimal | Text   | HEX color       |
| opacity           | Number | Percent Opacity |

<h3 id=entity_set_text_display_line_width>
  <code>entity::set_text_display_line_width</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Line Width\
**Action type:** Action without value\
**Description:** Sets the maximum line width for the text renderer.\
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:**
```ts
entity::set_text_display_line_width(1);

//Or dry by keywords

entity::set_text_display_line_width(line_width=1);
```

**Arguments:**

| ID         | Type   | Description |
|------------|--------|-------------|
| line_width | Number | Line Width  |

<h3 id=entity_set_text_display_opacity>
  <code>entity::set_text_display_opacity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text Opacity\
**Action type:** Action without value\
**Description:** Sets the transparency of text to the text renderer.\
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:**
```ts
entity::set_text_display_opacity(1);

//Or dry by keywords

entity::set_text_display_opacity(text_opacity=1);
```

**Arguments:**

| ID           | Type   | Description  |
|--------------|--------|--------------|
| text_opacity | Number | Text Opacity |

<h3 id=entity_set_text_display_see_through>
  <code>entity::set_text_display_see_through</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visibility Through Blocks\
**Action type:** Action without value\
**Description:** Sets the visibility of text through blocks to the text renderer.\
**Work_with:**\
&nbsp;&nbsp;Text Visualizers

**Usage example:**
```ts
entity::set_text_display_see_through("FALSE");

//Or dry by keywords

entity::set_text_display_see_through(enable_see_through="FALSE");
```

**Arguments:**

| ID                 | Type                                                 | Description               |
|--------------------|------------------------------------------------------|---------------------------|
| enable_see_through | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Visibility Through Blocks |

<h3 id=entity_set_text_display_text>
  <code>entity::set_text_display_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Display Text\
**Action type:** Action without value\
**Description:** Sets the display text for the text renderer.\
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:**
```ts
entity::set_text_display_text(["displayed_text", "displayed_text"], "CONCATENATION");

//Or dry by keywords

entity::set_text_display_text(displayed_text=["displayed_text", "displayed_text"], merging_mode="CONCATENATION");
```

**Arguments:**

| ID             | Type                                                                                                           | Description                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| displayed_text | Array\[Text\]                                                                                                  | Displayed Text<br/>The argument supports list decomposition |
| merging_mode   | Marker<br/>**CONCATENATION** - Merge<br/>**SEPARATE_LINES** - Separate Lines<br/>**SPACES** - Space Separation | Merge Text                                                  |

<h3 id=entity_set_text_display_text_shadow>
  <code>entity::set_text_display_text_shadow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text Shadow\
**Action type:** Action without value\
**Description:** Sets the visibility of the text shadow to the text renderer.\
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:**
```ts
entity::set_text_display_text_shadow("FALSE");

//Or dry by keywords

entity::set_text_display_text_shadow(enable_text_shadow="FALSE");
```

**Arguments:**

| ID                 | Type                                                 | Description |
|--------------------|------------------------------------------------------|-------------|
| enable_text_shadow | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Text Shadow |

<h3 id=entity_set_tropical_fish_pattern>
  <code>entity::set_tropical_fish_pattern</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fish Pattern\
**Action type:** Action without value\
**Description:** Sets the color and pattern of a tropical fish.\
**Work_with:**\
&nbsp;&nbsp;Tropical Fish

**Usage example:**
```ts
entity::set_tropical_fish_pattern("BLACK", "BLACK", "BETTY");

//Or dry by keywords

entity::set_tropical_fish_pattern(pattern_color="BLACK", body_color="BLACK", pattern="BETTY");
```

**Arguments:**

| ID            | Type                                                                                                                                                                                                                                                                                                                                                                                                                       | Description   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| pattern_color | Marker<br/>**BLACK** - Black<br/>**BLUE** - Blue<br/>**BROWN** - Brown<br/>**CYAN** - Turquoise<br/>**DO_NOT_CHANGE** - Don't Change<br/>**GRAY** - Gray<br/>**GREEN** - Green<br/>**LIGHT_BLUE** - Blue<br/>**LIGHT_GRAY** - Light Gray<br/>**LIME** - Lime<br/>**MAGENTA** - Magenta<br/>**ORANGE** - Orange<br/>**PINK** - Pink<br/>**PURPLE** - Purple<br/>**RED** - Red<br/>**WHITE** - White<br/>**YELLOW** - Yellow | Pattern Color |
| body_color    | Marker<br/>**BLACK** - Black<br/>**BLUE** - Blue<br/>**BROWN** - Brown<br/>**CYAN** - Turquoise<br/>**DO_NOT_CHANGE** - Don't Change<br/>**GRAY** - Gray<br/>**GREEN** - Green<br/>**LIGHT_BLUE** - Blue<br/>**LIGHT_GRAY** - Light Gray<br/>**LIME** - Lime<br/>**MAGENTA** - Magenta<br/>**ORANGE** - Orange<br/>**PINK** - Pink<br/>**PURPLE** - Purple<br/>**RED** - Red<br/>**WHITE** - White<br/>**YELLOW** - Yellow | Body Color    |
| pattern       | Marker<br/>**BETTY** - Betty<br/>**BLOCKFISH** - Blockfish<br/>**BRINELY** - Brinely<br/>**CLAYFISH** - Clayfish<br/>**DASHER** - Dasher<br/>**DO_NOT_CHANGE** - Don't Change<br/>**FLOPPER** - Flopper<br/>**GLITTER** - Glitter<br/>**KOB** - Kob<br/>**SNOOPER** - Snooper<br/>**SPOTTY** - Spotty<br/>**STRIPEY** - Stripey<br/>**SUNSTREAK** - SunStreak                                                              | Pattern       |

<h3 id=entity_set_vex_charging>
  <code>entity::set_vex_charging</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Vex Charging\
**Action type:** Action without value\
**Description:** Sets if the Vex is currently charging.\
**Work_with:**\
&nbsp;&nbsp;Vex

**Usage example:**
```ts
entity::set_vex_charging("FALSE");

//Or dry by keywords

entity::set_vex_charging(charging="FALSE");
```

**Arguments:**

| ID       | Type                                             | Description |
|----------|--------------------------------------------------|-------------|
| charging | Marker<br/>**FALSE** - False<br/>**TRUE** - True | Charging    |

<h3 id=entity_set_vex_limited_lifetime_ticks>
  <code>entity::set_vex_limited_lifetime_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Vex Limited Lifetime\
**Action type:** Action without value\
**Description:** Sets the Vex's life time in ticks.\
**Work_with:**\
&nbsp;&nbsp;Vex

**Usage example:**
```ts
entity::set_vex_limited_lifetime_ticks(1);

//Or dry by keywords

entity::set_vex_limited_lifetime_ticks(lifetime=1);
```

**Arguments:**

| ID       | Type   | Description |
|----------|--------|-------------|
| lifetime | Number | Life time   |

<h3 id=entity_set_villager_biome>
  <code>entity::set_villager_biome</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Villager Biome\
**Action type:** Action without value\
**Description:** Sets a villager's color based on the selected biome.\
**Work_with:**\
&nbsp;&nbsp;Villagers

**Usage example:**
```ts
entity::set_villager_biome("DESERT");

//Or dry by keywords

entity::set_villager_biome(biome="DESERT");
```

**Arguments:**

| ID    | Type                                                                                                                                                                       | Description |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| biome | Marker<br/>**DESERT** - Desert<br/>**JUNGLE** - Jungle<br/>**PLAINS** - Plains<br/>**SAVANNA** - Savannah<br/>**SNOW** - Snowy<br/>**SWAMP** - Swamp<br/>**TAIGA** - Taiga | Biome       |

<h3 id=entity_set_villager_experience>
  <code>entity::set_villager_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Villager Experience\
**Action type:** Action without value\
**Description:** Sets the villager experience amount.\
**Work_with:**\
&nbsp;&nbsp;Villagers

**Usage example:**
```ts
entity::set_villager_experience(1);

//Or dry by keywords

entity::set_villager_experience(experience=1);
```

**Arguments:**

| ID         | Type   | Description          |
|------------|--------|----------------------|
| experience | Number | Amount of Experience |

<h3 id=entity_set_villager_profession>
  <code>entity::set_villager_profession</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set a Villager's Profession\
**Action type:** Action without value\
**Description:** Sets a specific profession for a villager.\
**Work_with:**\
&nbsp;&nbsp;Villager\
&nbsp;&nbsp;Zombie Villagers

**Usage example:**
```ts
entity::set_villager_profession("ARMORER");

//Or dry by keywords

entity::set_villager_profession(profession="ARMORER");
```

**Arguments:**

| ID         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description         |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| profession | Marker<br/>**ARMORER** - Armorer<br/>**BUTCHER** - Butcher<br/>**CARTOGRAPHER** - Cartographer<br/>**CLERIC** - Priest<br/>**FARMER** - Farmer<br/>**FISHERMAN** - Fisherman<br/>**FLETCHER** - Archer<br/>**LEATHERWORKER** - Leatherworker<br/>**LIBRARIAN** - Librarian<br/>**MASON** - Mason<br/>**NITWIT** - Beggar<br/>**NONE** - No Profession<br/>**SHEPHERD** - Shepherd<br/>**TOOLSMITH** - Toolsmith<br/>**WEAPONSMITH** - Weaponsmith | Villager Profession |

<h3 id=entity_set_visual_fire>
  <code>entity::set_visual_fire</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Fire\
**Action type:** Action without value\
**Description:** Displays fire on a creature.

**Usage example:**
```ts
entity::set_visual_fire("FALSE");

//Or dry by keywords

entity::set_visual_fire(visual_fire="FALSE");
```

**Arguments:**

| ID          | Type                                                                                                                                                      | Description  |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| visual_fire | Marker<br/>**FALSE** - Disable<br/>**NOT_SET** - creative_plus.action.entity_set_visual_fire.argument.visual_fire.enum.not_set.name<br/>**TRUE** - Enable | Fire Display |

<h3 id=entity_set_warden_anger_level>
  <code>entity::set_warden_anger_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Warden Anger Level\
**Action type:** Action without value\
**Description:** Sets the Guardian's anger level to the specified creature.\
**Additional info:**\
&nbsp;&nbsp;If an entity's anger level reaches 80, the Guardian will actively pursue it.\
**Work_with:**\
&nbsp;&nbsp;Guardians

**Usage example:**
```ts
entity::set_warden_anger_level("name_or_uuid", 1);

//Or dry by keywords

entity::set_warden_anger_level(name_or_uuid="name_or_uuid", anger=1);
```

**Arguments:**

| ID           | Type   | Description            |
|--------------|--------|------------------------|
| name_or_uuid | Text   | Entity name or UUID    |
| anger        | Number | Anger Level (0 to 150) |

<h3 id=entity_set_warden_digging>
  <code>entity::set_warden_digging</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Warden Digging\
**Action type:** Action without value\
**Description:** Set a warden's digging type\
**Work_with:**\
&nbsp;&nbsp;Warden

**Usage example:**
```ts
entity::set_warden_digging("DIG_DOWN");

//Or dry by keywords

entity::set_warden_digging(digging="DIG_DOWN");
```

**Arguments:**

| ID      | Type                                                     | Description  |
|---------|----------------------------------------------------------|--------------|
| digging | Marker<br/>**DIG_DOWN** - Burrow<br/>**EMERGE** - Emerge | Digging Type |

<h3 id=entity_set_waypoint_color>
  <code>entity::set_waypoint_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_waypoint_color.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_waypoint_color.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.entity_set_waypoint_color.additional_information.needs_enabled_gamerule_location_bar\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_waypoint_color.work_with.living_entity

**Usage example:**
```ts
entity::set_waypoint_color(1, 2, 3);

//Or dry by keywords

entity::set_waypoint_color(red=1, green=2, blue=3);
```

**Arguments:**

| ID    | Type   | Description                                                        |
|-------|--------|--------------------------------------------------------------------|
| red   | Number | creative_plus.action.entity_set_waypoint_color.argument.red.name   |
| green | Number | creative_plus.action.entity_set_waypoint_color.argument.green.name |
| blue  | Number | creative_plus.action.entity_set_waypoint_color.argument.blue.name  |

<h3 id=entity_set_waypoint_style>
  <code>entity::set_waypoint_style</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_waypoint_style.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_waypoint_style.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.entity_set_waypoint_style.additional_information.needs_enabled_gamerule_location_bar\
&nbsp;&nbsp;creative_plus.action.entity_set_waypoint_style.additional_information.exist_build_in_vanilla_keys\
&nbsp;&nbsp;creative_plus.action.entity_set_waypoint_style.additional_information.empty_to_reset\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_waypoint_style.work_with.living_entity

**Usage example:**
```ts
entity::set_waypoint_style("style");

//Or dry by keywords

entity::set_waypoint_style(style="style");
```

**Arguments:**

| ID    | Type | Description                                                        |
|-------|------|--------------------------------------------------------------------|
| style | Text | creative_plus.action.entity_set_waypoint_style.argument.style.name |

<h3 id=entity_set_wearing_saddle>
  <code>entity::set_wearing_saddle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Saddle Visibility\
**Action type:** Action without value\
**Description:** Sets a saddle to an entity.\
**Work_with:**\
&nbsp;&nbsp;Pigs\
&nbsp;&nbsp;Horses\
&nbsp;&nbsp;Lavomers

**Usage example:**
```ts
entity::set_wearing_saddle("FALSE");

//Or dry by keywords

entity::set_wearing_saddle(wearing="FALSE");
```

**Arguments:**

| ID      | Type                                                 | Description     |
|---------|------------------------------------------------------|-----------------|
| wearing | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Having a Saddle |

<h3 id=entity_set_wither_invulnerability_ticks>
  <code>entity::set_wither_invulnerability_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Wither Invulnerability\
**Action type:** Action without value\
**Description:** Sets the duration of the Wither's invulnerability.\
**Work_with:**\
&nbsp;&nbsp;Wither

**Usage example:**
```ts
entity::set_wither_invulnerability_ticks(1);

//Or dry by keywords

entity::set_wither_invulnerability_ticks(ticks=1);
```

**Arguments:**

| ID    | Type   | Description                      |
|-------|--------|----------------------------------|
| ticks | Number | Invulnerability Duration (Ticks) |

<h3 id=entity_set_wolf_sound_variant>
  <code>entity::set_wolf_sound_variant</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_wolf_sound_variant.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_wolf_sound_variant.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_wolf_sound_variant.work_with.wolf

**Usage example:**
```ts
entity::set_wolf_sound_variant("ANGRY");

//Or dry by keywords

entity::set_wolf_sound_variant(sound_variant="ANGRY");
```

**Arguments:**

| ID            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| sound_variant | Marker<br/>**ANGRY** - creative_plus.action.entity_set_wolf_sound_variant.argument.sound_variant.enum.angry.name<br/>**BIG** - creative_plus.action.entity_set_wolf_sound_variant.argument.sound_variant.enum.big.name<br/>**CLASSIC** - creative_plus.action.entity_set_wolf_sound_variant.argument.sound_variant.enum.classic.name<br/>**CUTE** - creative_plus.action.entity_set_wolf_sound_variant.argument.sound_variant.enum.cute.name<br/>**GRUMPY** - creative_plus.action.entity_set_wolf_sound_variant.argument.sound_variant.enum.grumpy.name<br/>**PUGLIN** - creative_plus.action.entity_set_wolf_sound_variant.argument.sound_variant.enum.puglin.name<br/>**SAD** - creative_plus.action.entity_set_wolf_sound_variant.argument.sound_variant.enum.sad.name | creative_plus.action.entity_set_wolf_sound_variant.argument.sound_variant.name |

<h3 id=entity_set_wolf_type>
  <code>entity::set_wolf_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Wolf Type\
**Action type:** Action without value\
**Description:** Sets the wolf type.\
**Work_with:**\
&nbsp;&nbsp;Wolf

**Usage example:**
```ts
entity::set_wolf_type("ASHEN");

//Or dry by keywords

entity::set_wolf_type(wolf_type="ASHEN");
```

**Arguments:**

| ID        | Type                                                                                                                                                                                                         | Description |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| wolf_type | Marker<br/>**ASHEN** - Ashen<br/>**SNOWY** - Snowy<br/>**RUSTY** - Rusty<br/>**BLACK** - Black<br/>**CHESTNUT** - Chestnut<br/>**SPOTTED** - Spotted<br/>**STRIPED** - Striped<br/>**PALE** - Pale (Default) | Wolf Type   |

<h3 id=entity_set_zombie_arms_raised>
  <code>entity::set_zombie_arms_raised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Zombie Arms Raised\
**Action type:** Action without value\
**Description:** Sets the zombie arm raise animation.\
**Work_with:**\
&nbsp;&nbsp;Zombies

**Usage example:**
```ts
entity::set_zombie_arms_raised("FALSE");

//Or dry by keywords

entity::set_zombie_arms_raised(arms_raised="FALSE");
```

**Arguments:**

| ID          | Type                                                 | Description |
|-------------|------------------------------------------------------|-------------|
| arms_raised | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Raise Hands |

<h3 id=entity_set_zombie_nautilus_variant>
  <code>entity::set_zombie_nautilus_variant</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.entity_set_zombie_nautilus_variant.name\
**Action type:** Action without value\
**Description:** creative_plus.action.entity_set_zombie_nautilus_variant.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.entity_set_zombie_nautilus_variant.work_with.zombie_nautilus

**Usage example:**
```ts
entity::set_zombie_nautilus_variant("TEMPERATE");

//Or dry by keywords

entity::set_zombie_nautilus_variant(variant="TEMPERATE");
```

**Arguments:**

| ID      | Type                                                                                                                                                                                                                           | Description                                                                   |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| variant | Marker<br/>**TEMPERATE** - creative_plus.action.entity_set_zombie_nautilus_variant.argument.variant.enum.temperate.name<br/>**WARM** - creative_plus.action.entity_set_zombie_nautilus_variant.argument.variant.enum.warm.name | creative_plus.action.entity_set_zombie_nautilus_variant.argument.variant.name |

<h3 id=entity_shear>
  <code>entity::shear</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shear Entity\
**Action type:** Action without value\
**Description:** Shears the entity.\
**Work_with:**\
&nbsp;&nbsp;Sheep\
&nbsp;&nbsp;Mooshroom\
&nbsp;&nbsp;Bogged\
&nbsp;&nbsp;Snow Golem

**Usage example:**
```ts
entity::shear();
```

<h3 id=entity_shear_sheep>
  <code>entity::shear_sheep</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shear Sheep\
**Action type:** Action without value\
**Description:** Shears a sheep.\
**Work_with:**\
&nbsp;&nbsp;Sheep

**Usage example:**
```ts
entity::shear_sheep();
```

<h3 id=entity_sleep>
  <code>entity::sleep</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sleep Animation\
**Action type:** Action without value\
**Description:** Sets an entity's sleep animation. It is best to use this action in a loop.\
**Work_with:**\
&nbsp;&nbsp;Foxes

**Usage example:**
```ts
entity::sleep("FALSE");

//Or dry by keywords

entity::sleep(sleep="FALSE");
```

**Arguments:**

| ID    | Type                                                 | Description |
|-------|------------------------------------------------------|-------------|
| sleep | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Sleep Mode  |

<h3 id=entity_swing_hand>
  <code>entity::swing_hand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Swing Hand Animation\
**Action type:** Action without value\
**Description:** Plays a swinging hand animation for the entity.

**Usage example:**
```ts
entity::swing_hand("MAIN");

//Or dry by keywords

entity::swing_hand(hand_type="MAIN");
```

**Arguments:**

| ID        | Type                                           | Description |
|-----------|------------------------------------------------|-------------|
| hand_type | Marker<br/>**MAIN** - Main<br/>**OFF** - Minor | Hand Type   |

<h3 id=entity_teleport>
  <code>entity::teleport</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Teleport\
**Action type:** Action without value\
**Description:** Teleports an entity to the selected location.

**Usage example:**
```ts
entity::teleport(location(0,0,0,0,0), "FALSE");

//Or dry by keywords

entity::teleport(location=location(0,0,0,0,0), keep_rotation="FALSE");
```

**Arguments:**

| ID            | Type                                                   | Description           |
|---------------|--------------------------------------------------------|-----------------------|
| location      | Location                                               | New Position          |
| keep_rotation | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Keep Current Rotation |

<h3 id=entity_use_item>
  <code>entity::use_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Use an Item\
**Action type:** Action without value\
**Description:** Instructs the AI creature to use the item in its hand.\
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:**
```ts
entity::use_item("MAIN_HAND", "FALSE");

//Or dry by keywords

entity::use_item(hand="MAIN_HAND", enable="FALSE");
```

**Arguments:**

| ID     | Type                                                            | Description |
|--------|-----------------------------------------------------------------|-------------|
| hand   | Marker<br/>**MAIN_HAND** - Main Hand<br/>**OFF_HAND** - Offhand | Hand Type   |
| enable | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable            | Use         |

<h3 id=if_entity_collides_at_location>
  <code>entity::collides_at_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Collidies At Location\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity collides with blocks, shulkers, boats and worldborder on a given location.

**Usage example:**
```ts
if(entity::collides_at_location(location(0,0,0,0,0))){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::collides_at_location(location=location(0,0,0,0,0))){
    player::message("Condition is true");
}
```

**Arguments:**

| ID       | Type     | Description       |
|----------|----------|-------------------|
| location | Location | Location to check |

<h3 id=if_entity_collides_using_hitbox>
  <code>entity::collides_using_hitbox</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Collides Using Custom Hitbox\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity collides with blocks, shulkers, boats and worldborder using a custom hitbox.

**Usage example:**
```ts
if(entity::collides_using_hitbox(location(0,0,0,0,0), location(0,0,0,0,0))){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::collides_using_hitbox(min=location(0,0,0,0,0), max=location(0,0,0,0,0))){
    player::message("Condition is true");
}
```

**Arguments:**

| ID  | Type     | Description             |
|-----|----------|-------------------------|
| min | Location | First corner of hitbox  |
| max | Location | Second corner of hitbox |

<h3 id=if_entity_collides_with_entity>
  <code>entity::collides_with_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Collidies With Entity\
**Action type:** Action that checks the conditions\
**Description:** Check if a hitbox of an entity collides with a hitbox of another entity.

**Usage example:**
```ts
if(entity::collides_with_entity("name_or_uuid", "CONTAINS")){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::collides_with_entity(name_or_uuid="name_or_uuid", check_type="CONTAINS")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID           | Type                                                             | Description             |
|--------------|------------------------------------------------------------------|-------------------------|
| name_or_uuid | Text                                                             | Entity name or UUID     |
| check_type   | Marker<br/>**CONTAINS** - Contains<br/>**OVERLAPS** - Intersects | Intersection check type |

<h3 id=if_entity_dummy>
  <code>entity::is_dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Action type:** Action that checks the conditions\
**Description:** ...

**Usage example:**
```ts
if(entity::is_dummy()){
    player::message("Condition is true");
}
```

<h3 id=if_entity_exists>
  <code>entity::exists</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Exists\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is in the world.

**Usage example:**
```ts
if(entity::exists()){
    player::message("Condition is true");
}
```

<h3 id=if_entity_has_custom_tag>
  <code>entity::has_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has Custom Tag\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity has a custom tag with the specified value.

**Usage example:**
```ts
if(entity::has_custom_tag("tag", ["tag_value", "tag_value"], "CONTAINS")){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::has_custom_tag(tag="tag", tag_value=["tag_value", "tag_value"], compare_type="CONTAINS")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID           | Type                                                                                                                       | Description                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| tag          | Text                                                                                                                       | Tag Name                                               |
| tag_value    | Array\[Text\]                                                                                                              | Tag Value<br/>The argument supports list decomposition |
| compare_type | Marker<br/>**CONTAINS** - Contains<br/>**ENDS_WITH** - Ends With<br/>**EQUALS** - Equals<br/>**STARTS_WITH** - Starts With | Comparison Type                                        |

<h3 id=if_entity_has_potion_effect>
  <code>entity::has_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has Potion Effect\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity has the effect of a potion.

**Usage example:**
```ts
if(entity::has_potion_effect([potion("slow_falling"), potion("slow_falling")], "ALL")){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::has_potion_effect(potions=[potion("slow_falling"), potion("slow_falling")], check_mode="ALL")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID         | Type                                                      | Description                                                  |
|------------|-----------------------------------------------------------|--------------------------------------------------------------|
| potions    | Array\[Potion\]                                           | Potions to Test<br/>The argument supports list decomposition |
| check_mode | Marker<br/>**ALL** - All Effects<br/>**ANY** - Any Effect | Check Mode                                                   |

<h3 id=if_entity_in_area>
  <code>entity::in_area</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Inside Region\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is in a certain region.

**Usage example:**
```ts
if(entity::in_area(location(0,0,0,0,0), location(0,0,0,0,0), "FALSE", "HITBOX", "CONTAINS")){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::in_area(location_1=location(0,0,0,0,0), location_2=location(0,0,0,0,0), ignore_y_axis="FALSE", intersect_type="HITBOX", check_type="CONTAINS")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID             | Type                                                             | Description            |
|----------------|------------------------------------------------------------------|------------------------|
| location_1     | Location                                                         | First corner of region |
| location_2     | Location                                                         | Second Region Corner   |
| ignore_y_axis  | Marker<br/>**FALSE** - Don't ignore<br/>**TRUE** - Ignore        | Ignore Y Axis          |
| intersect_type | Marker<br/>**HITBOX** - Hitbox<br/>**POINT** - Location          | Intersection type      |
| check_type     | Marker<br/>**CONTAINS** - Contains<br/>**OVERLAPS** - Intersects | Hitbox check type      |

<h3 id=if_entity_is_disguised>
  <code>entity::is_disguised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguised\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is disguised.

**Usage example:**
```ts
if(entity::is_disguised()){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_grounded>
  <code>entity::is_grounded</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is On Ground\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is touching the surface of a block.

**Usage example:**
```ts
if(entity::is_grounded()){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_item>
  <code>entity::is_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is an Item\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is an item.

**Usage example:**
```ts
if(entity::is_item()){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_minecraft_tagged>
  <code>entity::is_minecraft_tagged</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.if_entity_is_minecraft_tagged.name\
**Action type:** Action that checks the conditions\
**Description:** creative_plus.action.if_entity_is_minecraft_tagged.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.if_entity_is_minecraft_tagged.additional_information.checks_is_minecraft_registry_tagged

**Usage example:**
```ts
if(entity::is_minecraft_tagged("namespace")){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::is_minecraft_tagged(namespace="namespace")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID        | Type | Description                                                                |
|-----------|------|----------------------------------------------------------------------------|
| namespace | Text | creative_plus.action.if_entity_is_minecraft_tagged.argument.namespace.name |

<h3 id=if_entity_is_mob>
  <code>entity::is_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is a Mob\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is a mob.

**Usage example:**
```ts
if(entity::is_mob()){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_near_location>
  <code>entity::is_near_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Near location\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is near the specified location.

**Usage example:**
```ts
if(entity::is_near_location(1, location(0,0,0,0,0), "FALSE")){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::is_near_location(range=1, location=location(0,0,0,0,0), ignore_y_axis="FALSE")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID            | Type                                                      | Description       |
|---------------|-----------------------------------------------------------|-------------------|
| range         | Number                                                    | Check Radius      |
| location      | Location                                                  | Location to check |
| ignore_y_axis | Marker<br/>**FALSE** - Don't ignore<br/>**TRUE** - Ignore | Ignore Y Axis     |

<h3 id=if_entity_is_projectile>
  <code>entity::is_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is a Projectile\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is a projectile.

**Usage example:**
```ts
if(entity::is_projectile()){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_riding_entity>
  <code>entity::is_riding_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Riding Entity\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is riding any of the other specified entities.

**Usage example:**
```ts
if(entity::is_riding_entity(["entity_ids", "entity_ids"], "FARTHEST")){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::is_riding_entity(entity_ids=["entity_ids", "entity_ids"], compare_mode="FARTHEST")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID           | Type                                                                                                                                                                                                                                                                                          | Description                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| entity_ids   | Array\[Text\]                                                                                                                                                                                                                                                                                 | Name or UUID of entities<br/>The argument supports list decomposition |
| compare_mode | Marker<br/>**FARTHEST** - creative_plus.action.if_entity_is_riding_entity.argument.compare_mode.enum.farthest.name<br/>**NAME_OR_UUID** - Name or UUID<br/>**NEAREST** - creative_plus.action.if_entity_is_riding_entity.argument.compare_mode.enum.nearest.name<br/>**TYPE** - Creature Type | Riding Mode                                                           |

<h3 id=if_entity_is_standing_on_block>
  <code>entity::is_standing_on_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Standing On a Block\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is standing on a block of a certain category or a certain location.

**Usage example:**
```ts
if(entity::is_standing_on_block(["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], [location(0,0,0,0,0), location(0,0,0,0,0)], "FALSE")){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::is_standing_on_block(blocks=["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], locations=[location(0,0,0,0,0), location(0,0,0,0,0)], only_solid="FALSE")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID         | Type                                                                                                                                                                                                                 | Description                                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| blocks     | Array\[Block\]                                                                                                                                                                                                       | Blocks to Check<br/>The argument supports list decomposition                 |
| locations  | Array\[Location\]                                                                                                                                                                                                    | Locations to Check<br/>The argument supports list decomposition              |
| only_solid | Marker<br/>**FALSE** - creative_plus.action.if_entity_is_standing_on_block.argument.only_solid.enum.false.name<br/>**TRUE** - creative_plus.action.if_entity_is_standing_on_block.argument.only_solid.enum.true.name | creative_plus.action.if_entity_is_standing_on_block.argument.only_solid.name |

<h3 id=if_entity_is_type>
  <code>entity::is_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Entity Type Is\
**Action type:** Action that checks the conditions\
**Description:** Checks if the entity type is equal to the type in the chest.

**Usage example:**
```ts
if(entity::is_type([item("stick"), item("stick")])){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::is_type(entity_types=[item("stick"), item("stick")])){
    player::message("Condition is true");
}
```

**Arguments:**

| ID           | Type          | Description                                              |
|--------------|---------------|----------------------------------------------------------|
| entity_types | Array\[Item\] | Entity Type<br/>The argument supports list decomposition |

<h3 id=if_entity_is_undead>
  <code>entity::is_undead</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is Undead\
**Action type:** Action that checks the conditions\
**Description:** Checks if the entity is undead.

**Usage example:**
```ts
if(entity::is_undead()){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_vehicle>
  <code>entity::is_vehicle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is a Vehicle\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity is a vehicle.

**Usage example:**
```ts
if(entity::is_vehicle()){
    player::message("Condition is true");
}
```

<h3 id=if_entity_name_equals>
  <code>entity::name_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Name Equals\
**Action type:** Action that checks the conditions\
**Description:** Checks if an entity's name is equal to the name in the chest.

**Usage example:**
```ts
if(entity::name_equals(["names_or_uuids", "names_or_uuids"])){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::name_equals(names_or_uuids=["names_or_uuids", "names_or_uuids"])){
    player::message("Condition is true");
}
```

**Arguments:**

| ID             | Type          | Description                                                          |
|----------------|---------------|----------------------------------------------------------------------|
| names_or_uuids | Array\[Text\] | Names or UUIDs to check<br/>The argument supports list decomposition |

<h3 id=if_entity_spawn_reason_equals>
  <code>entity::spawn_reason_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Reason Is\
**Action type:** Action that checks the conditions\
**Description:** Checks if the entity spawn reason is equal to a certain value.

**Usage example:**
```ts
if(entity::spawn_reason_equals("BEEHIVE")){
    player::message("Condition is true");
}

//Or dry by keywords

if(entity::spawn_reason_equals(reason="BEEHIVE")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description  |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| reason | Marker<br/>**BEEHIVE** - Beehive Spawn<br/>**BREEDING** - From breeding<br/>**BUILD_IRONGOLEM** - From Build Iron Golem<br/>**BUILD_SNOWMAN** - From Build Snow Golem<br/>**BUILD_WITHER** - From Build Wither<br/>**COMMAND** - Command<br/>**CURED** - Cure Citizen<br/>**CUSTOM** - Custom<br/>**DEFAULT** - Standard<br/>**DISPENSE_EGG** - Dispenser Spawn<br/>**DROWNED** - From drowning<br/>**EGG** - Egg Spawn<br/>**ENDER_PEARL** - Spawn from End Pearl<br/>**EXPLOSION** - After Explosion<br/>**FROZEN** - From Freezing<br/>**INFECTION** - From Zombie Infection<br/>**JOCKEY** - As an Entity Jockey<br/>**LIGHTNING** - From Lightning<br/>**MOUNT** - As Entity Transport<br/>**NATURAL** - Natural Spawn<br/>**NETHER_PORTAL** - From Nether Portal<br/>**OCELOT_BABY** - Ocelot's Baby<br/>**PATROL** - Rogue Patrol<br/>**PIGLIN_ZOMBIFIED** - Zombie<br/>**RAID** - From Raid<br/>**REINFORCEMENTS** - Reinforcements<br/>**SHEARED** - From Shearing<br/>**SHOULDER_ENTITY** - Shoulder Jump<br/>**SILVERFISH_BLOCK** - From Block<br/>**SLIME_SPLIT** - Slime Split<br/>**SPAWNER** - From Mob Spawner<br/>**SPAWNER_EGG** - From the Spawn Egg<br/>**TRAP** - Trap<br/>**VILLAGER_DEFENSE** - Villager Defense<br/>**VILLAGE_INVASION** - Village Attack | Spawn Reason |

