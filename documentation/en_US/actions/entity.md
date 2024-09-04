<h2 id=entity>
  <code>entity</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

### Селекторы

| **Name**           | **Description**           |
|--------------------|---------------------------|
| `<current>`        | Current entity            |
| `<default_entity>` | Default entity            |
| `<killer_entity>`  | Killer                    |
| `<shooter_entity>` | Shooter                   |
| `<projectile>`     | projectile of the shooter |
| `<victim_entity>`  | Victim                    |
| `<random_entity>`  | Random entity             |
| `<all_mobs>`       | All mobs                  |
| `<all_entities>`   | All entities              |
| `<last_entity>`    | Last entity               |

<h3 id=entity_attach_lead>
  <code>entity::attach_lead</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Attach Lead\
**Type:** Action without value\
**Description:** Tethers an entity to a fence or entity.

**Usage example:** 
```ts
entity::attach_lead("name_or_uuid",location(0,0,0,0,0));
```

<h3 id=entity_clear_merchant_recipes>
  <code>entity::clear_merchant_recipes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Merchant Recipes\
**Type:** Action without value\
**Description:** Clears all trades to a Villager.
**Work_with:**\
&nbsp;&nbsp;Villagers\
&nbsp;&nbsp;Wandering Traders

**Usage example:** 
```ts
entity::clear_merchant_recipes();
```

<h3 id=entity_celar_potion_effects>
  <code>entity::clear_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear All Potion Effects\
**Type:** Action without value\
**Description:** Clears all effects on an entity.

**Usage example:** 
```ts
entity::clear_potion_effects();
```

<h3 id=entity_damage>
  <code>entity::damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Deal Damage\
**Type:** Action without value\
**Description:** Deals damage to an entity.

**Usage example:** 
```ts
entity::damage(1,"source");
```

<h3 id=entity_disguise_as_block>
  <code>entity::disguise_as_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Block\
**Type:** Action without value\
**Description:** Disguise an entity as a block.

**Usage example:** 
```ts
entity::disguise_as_block(item("stone"));
```

<h3 id=entity_disguise_as_entity>
  <code>entity::disguise_as_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Entity\
**Type:** Action without value\
**Description:** Disguise an entity as an entity.

**Usage example:** 
```ts
entity::disguise_as_entity(item("stick"));
```

<h3 id=entity_disguise_as_item>
  <code>entity::disguise_as_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Item\
**Type:** Action without value\
**Description:** Disguises an entity as an item.

**Usage example:** 
```ts
entity::disguise_as_item(item("stick"));
```

<h3 id=entity_disguise_as_player>
  <code>entity::disguise_as_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Player\
**Type:** Action without value\
**Description:** Disguises an entity as a player.

**Usage example:** 
```ts
entity::disguise_as_player("name_or_uuid","display_name","MOJANG");
```

<h3 id=entity_eat_grass>
  <code>entity::eat_grass</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Eat Grass\
**Type:** Action without value\
**Description:** Makes a sheep eat grass.
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
**Type:** Action without value\
**Description:** Sets a target for an entity to eat.
**Work_with:**\
&nbsp;&nbsp;Toads

**Usage example:** 
```ts
entity::eat_target("name_or_uuid");
```

<h3 id=entity_explode>
  <code>entity::explode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Explode\
**Type:** Action without value\
**Description:** Causes an entity to explode.
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
**Type:** Action without value\
**Description:** Turns an entity towards a location.

**Usage example:** 
```ts
entity::face_location(location(0,0,0,0,0));
```

<h3 id=entity_get_custom_tag>
  <code>entity::get_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Custom Tag\
**Type:** An action that returns a value\
**Description:** Gets a creature's custom nbt tag.

**Usage example:** 
```ts
a1 = entity::get_custom_tag("name","any value");

#Or dry

entity::get_custom_tag(a1,"name","any value");
```

<h3 id=entity_give_potion_effects>
  <code>entity::give_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give Potion Effect\
**Type:** Action without value\
**Description:** Gives the selected effects to the creature.

**Usage example:** 
```ts
entity::give_potion_effects([potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");
```

<h3 id=entity_heal>
  <code>entity::heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Heal Entity\
**Type:** Action without value\
**Description:** Heals an entity.

**Usage example:** 
```ts
entity::heal(1);
```

<h3 id=entity_ignite_creeper>
  <code>entity::ignite_creeper</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ignite Creeper\
**Type:** Action without value\
**Description:** Sets a creeper on fire, causing it to explode after a certain period.
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
**Type:** Action without value\
**Description:** Makes an entity jump.
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
**Type:** Action without value\
**Description:** Launches an entity forward or backward in the direction it is facing based on its power.

**Usage example:** 
```ts
entity::launch_forward(1,"TRUE","YAW_AND_PITCH");
```

<h3 id=entity_launch_projectile>
  <code>entity::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Projectile\
**Type:** Action without value\
**Description:** Launch a projectile from an entity's location.

**Usage example:** 
```ts
entity::launch_projectile(item("stick"),location(0,0,0,0,0),"name",1,2,particle("fire"));
```

<h3 id=entity_launch_to_location>
  <code>entity::launch_to_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch To Location\
**Type:** Action without value\
**Description:** Launches creatures to the selected location.

**Usage example:** 
```ts
entity::launch_to_location(location(0,0,0,0,0),1,"TRUE");
```

<h3 id=entity_launch_up>
  <code>entity::launch_up</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Up\
**Type:** Action without value\
**Description:** Tosses an entity up or down based on strength.

**Usage example:** 
```ts
entity::launch_up(1,"TRUE");
```

<h3 id=entity_modify_piglin_barter_materials>
  <code>entity::modify_piglin_barter_materials</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None\
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::modify_piglin_barter_materials([item("stick"), item("stick")],"ADD");
```

<h3 id=entity_modify_piglin_interested_materials>
  <code>entity::modify_piglin_interested_materials</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None\
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::modify_piglin_interested_materials([item("stick"), item("stick")],"ADD");
```

<h3 id=entity_move_to_location>
  <code>entity::move_to_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Move To Location\
**Type:** Action without value\
**Description:** Instructs the entity AI to always find its way to a certain location at a certain speed.
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:** 
```ts
entity::move_to_location(location(0,0,0,0,0),1);
```

<h3 id=entity_move_to_location_stop>
  <code>entity::move_to_location_stop</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Stop Moving To Location\
**Type:** Action without value\
**Description:** Stops an entity moving to a location.
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
**Type:** Action without value\
**Description:** Displays an entity damage animation.

**Usage example:** 
```ts
entity::play_damage_animation("DAMAGE");
```

<h3 id=entity_play_hurt_animation>
  <code>entity::play_hurt_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
entity::play_hurt_animation(1);
```

<h3 id=entity_ram_target>
  <code>entity::ram_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ram Entity\
**Type:** Action without value\
**Description:** Causes goats to ram the target entity.
**Work_with:**\
&nbsp;&nbsp;Goat

**Usage example:** 
```ts
entity::ram_target("name_or_uuid");
```

<h3 id=entity_remove>
  <code>entity::remove</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Entity\
**Type:** Action without value\
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
**Type:** Action without value\
**Description:** Removes a custom NBT tag from an entity.

**Usage example:** 
```ts
entity::remove_custom_tag("name");
```

<h3 id=entity_remove_disguise>
  <code>entity::remove_disguise</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Disguise\
**Type:** Action without value\
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
**Type:** Action without value\
**Description:** Removes an item to the Villager at the specified index.
**Work_with:**\
&nbsp;&nbsp;Villager\
&nbsp;&nbsp;Wandering Traders

**Usage example:** 
```ts
entity::remove_merchant_recipe(1);
```

<h3 id=entity_remove_potion_effect>
  <code>entity::remove_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Potion Effect\
**Type:** Action without value\
**Description:** Removes the selected effects from an entity.

**Usage example:** 
```ts
entity::remove_potion_effect([potion("slow_falling"), potion("slow_falling")]);
```

<h3 id=entity_reset_display_brightness>
  <code>entity::reset_display_brightness</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reset Brightness\
**Type:** Action without value\
**Description:** Reset the brightness of an entity renderer.
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
**Type:** Action without value\
**Description:** Reset the glow color of the render entity.
**Work_with:**\
&nbsp;&nbsp;Item Renderers\
&nbsp;&nbsp;Block Renderers

**Usage example:** 
```ts
entity::reset_display_glow_color();
```

<h3 id=entity_reset_text_display_background>
  <code>entity::reset_text_display_background</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reset Background Color\
**Type:** Action without value\
**Description:** Reset the background color and transparency of the text renderer.
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:** 
```ts
entity::reset_text_display_background();
```

<h3 id=entity_ride_entity>
  <code>entity::ride_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ride an Entity\
**Type:** Action without value\
**Description:** Rides an entity onto another entity or player.

**Usage example:** 
```ts
entity::ride_entity("name_or_uuid");
```

<h3 id=entity_set_absorption_health>
  <code>entity::set_absorption_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Extra Health\
**Type:** Action without value\
**Description:** Sets an entity's bonus health.

**Usage example:** 
```ts
entity::set_absorption_health(1);
```

<h3 id=entity_set_ai>
  <code>entity::set_ai</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Intelligence\
**Type:** Action without value\
**Description:** Sets the intelligence of an entity.

**Usage example:** 
```ts
entity::set_ai("TRUE");
```

<h3 id=entity_set_allay_dancing>
  <code>entity::set_allay_dancing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Allay Dancing\
**Type:** Action without value\
**Description:** Sets the Quiet Entity to display a dancing animation.
**Work_with:**\
&nbsp;&nbsp;Allays

**Usage example:** 
```ts
entity::set_allay_dancing("TRUE");
```

<h3 id=entity_set_angry>
  <code>entity::set_angry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Anger Mode\
**Type:** Action without value\
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
entity::set_angry("TRUE","target");
```

<h3 id=entity_set_animal_age>
  <code>entity::set_animal_age</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Animal Age\
**Type:** Action without value\
**Description:** Sets the age of an animal.

**Usage example:** 
```ts
entity::set_animal_age(1,"ENABLE");
```

<h3 id=entity_set_armor_items>
  <code>entity::set_armor_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor\
**Type:** Action without value\
**Description:** Sets an entity's armor.

**Usage example:** 
```ts
entity::set_armor_items(item("stick"),item("stick"),item("stick"),item("stick"));
```

<h3 id=entity_set_armor_stand_parts>
  <code>entity::set_armor_stand_parts</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor Stand Parts\
**Type:** Action without value\
**Description:** Set armor stand parts.
**Work_with:**\
&nbsp;&nbsp;Armor Stands

**Usage example:** 
```ts
entity::set_armor_stand_parts("ENABLE","ENABLE");
```

<h3 id=entity_set_armor_stand_pose>
  <code>entity::set_armor_stand_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor Stand Pose\
**Type:** Action without value\
**Description:** Sets the pose of an armor stand.
**Work_with:**\
&nbsp;&nbsp;Armor Stands

**Usage example:** 
```ts
entity::set_armor_stand_pose(1,2,3,"HEAD");
```

<h3 id=entity_set_attribute>
  <code>entity::set_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Attribute\
**Type:** Action without value\
**Description:** Sets the specified attribute to the specified entity value.

**Usage example:** 
```ts
entity::set_attribute(1,"MAX_HEALTH");
```

<h3 id=entity_set_aware>
  <code>entity::set_aware</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Mob Awareness\
**Type:** Action without value\
**Description:** When disabled, disables the AI of the mob, but leaves interaction with gravity, pushing, etc.
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:** 
```ts
entity::set_aware("TRUE");
```

<h3 id=entity_set_axolotl_type>
  <code>entity::set_axolotl_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Axolotl Type\
**Type:** Action without value\
**Description:** Sets the axolotl type.
**Work_with:**\
&nbsp;&nbsp;Axolotl

**Usage example:** 
```ts
entity::set_axolotl_type("BLUE");
```

<h3 id=entity_set_baby>
  <code>entity::set_baby</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Child Mode\
**Type:** Action without value\
**Description:** Sets an entity to child mode.

**Usage example:** 
```ts
entity::set_baby("TRUE");
```

<h3 id=entity_set_bee_nectar>
  <code>entity::set_bee_nectar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Bee Pollen\
**Type:** Action without value\
**Description:** Sets the visibility of pollen to the bee.
**Work_with:**\
&nbsp;&nbsp;Bees

**Usage example:** 
```ts
entity::set_bee_nectar("TRUE");
```

<h3 id=entity_set_block_display_block>
  <code>entity::set_block_display_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Display Block\
**Type:** Action without value\
**Description:** Sets the display block to the block renderer.
**Work_with:**\
&nbsp;&nbsp;Block Renderers

**Usage example:** 
```ts
entity::set_block_display_block(item("stone"));
```

<h3 id=entity_set_camel_dashing>
  <code>entity::set_camel_dashing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Camel Dashing Animation\
**Type:** Action without value\
**Description:** Sets the dashing animation for the camel.
**Work_with:**\
&nbsp;&nbsp;Camels

**Usage example:** 
```ts
entity::set_camel_dashing("TRUE");
```

<h3 id=entity_set_carrying_chest>
  <code>entity::set_carrying_chest</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Chest Visibility\
**Type:** Action without value\
**Description:** Sets the visibility of the chest on the entity.
**Work_with:**\
&nbsp;&nbsp;Donkeys\
&nbsp;&nbsp;Mules\
&nbsp;&nbsp;Lamas

**Usage example:** 
```ts
entity::set_carrying_chest("TRUE");
```

<h3 id=entity_set_cat_lying_down>
  <code>entity::set_cat_lying_down</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Cat Lying Down\
**Type:** Action without value\
**Description:** Sets the lying down mode for the cat.
**Work_with:**\
&nbsp;&nbsp;Cats

**Usage example:** 
```ts
entity::set_cat_lying_down("TRUE");
```

<h3 id=entity_set_cat_type>
  <code>entity::set_cat_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Cat Type\
**Type:** Action without value\
**Description:** Sets the type of cat.
**Work_with:**\
&nbsp;&nbsp;Cats

**Usage example:** 
```ts
entity::set_cat_type("ALL_BLACK");
```

<h3 id=entity_set_celebrating>
  <code>entity::set_celebrating</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Celebrating Mode\
**Type:** Action without value\
**Description:** Sets the entity's celebrating mode.
**Work_with:**\
&nbsp;&nbsp;Piglin\
&nbsp;&nbsp;Raiders

**Usage example:** 
```ts
entity::set_celebrating("TRUE");
```

<h3 id=entity_set_collidable>
  <code>entity::set_collidable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Collidable Mode\
**Type:** Action without value\
**Description:** Sets an entity to collide with other entities.

**Usage example:** 
```ts
entity::set_collidable("TRUE");
```

<h3 id=entity_set_creeper_charge>
  <code>entity::set_creeper_charge</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Creeper Charge\
**Type:** Action without value\
**Description:** Sets whether the creeper will be charged.
**Work_with:**\
&nbsp;&nbsp;Creepers

**Usage example:** 
```ts
entity::set_creeper_charge("TRUE");
```

<h3 id=entity_set_creeper_fuse>
  <code>entity::set_creeper_fuse</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Creeper Fuse Time\
**Type:** Action without value\
**Description:** Sets the creeper's time before it explodes.
**Work_with:**\
&nbsp;&nbsp;Creepers

**Usage example:** 
```ts
entity::set_creeper_fuse(1);
```

<h3 id=entity_set_current_health>
  <code>entity::set_current_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Health\
**Type:** Action without value\
**Description:** Sets an entity's health to the selected amount.

**Usage example:** 
```ts
entity::set_current_health(1);
```

<h3 id=entity_set_custom_name>
  <code>entity::set_custom_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Name\
**Type:** Action without value\
**Description:** Sets a name for an entity.

**Usage example:** 
```ts
entity::set_custom_name("custom_name");
```

<h3 id=entity_set_custom_name_visibility>
  <code>entity::set_custom_name_visibility</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Name Visibility\
**Type:** Action without value\
**Description:** Sets the visibility of the entity name.

**Usage example:** 
```ts
entity::set_custom_name_visibility("TRUE");
```

<h3 id=entity_set_custom_tag>
  <code>entity::set_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Custom Tag\
**Type:** Action without value\
**Description:** Sets a custom nbt tag to an entity.

**Usage example:** 
```ts
entity::set_custom_tag("name","value");
```

<h3 id=entity_set_death_drops>
  <code>entity::set_death_drops</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Drops Items\
**Type:** Action without value\
**Description:** Sets whether or not an entity will drop loot.

**Usage example:** 
```ts
entity::set_death_drops("TRUE");
```

<h3 id=entity_set_death_time>
  <code>entity::set_death_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Death Time\
**Type:** Action without value\
**Description:** Sets the death duration for an entity.

**Usage example:** 
```ts
entity::set_death_time(1);
```

<h3 id=entity_set_despawning>
  <code>entity::set_despawning</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Despawning\
**Type:** Action without value\
**Description:** Sets whether an entity will despawn.

**Usage example:** 
```ts
entity::set_despawning("TRUE");
```

<h3 id=entity_set_display_billboard>
  <code>entity::set_display_billboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Display Mode\
**Type:** Action without value\
**Description:** Sets the display mode of the billboard entity.
**Work_with:**\
&nbsp;&nbsp;Any renderer entity

**Usage example:** 
```ts
entity::set_display_billboard("CENTER");
```

<h3 id=entity_set_display_brightness>
  <code>entity::set_display_brightness</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Brightness\
**Type:** Action without value\
**Description:** Sets the brightness of the renderer entity.
**Work_with:**\
&nbsp;&nbsp;Any Display Entity

**Usage example:** 
```ts
entity::set_display_brightness(1,2);
```

<h3 id=entity_set_display_culling_suze>
  <code>entity::set_display_culling_suze</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visibility Size\
**Type:** Action without value\
**Description:** Sets the size of the visualizer entity's model scope.
**Work_with:**\
&nbsp;&nbsp;Any Visualizer Entity

**Usage example:** 
```ts
entity::set_display_culling_suze(1,2);
```

<h3 id=entity_set_display_glow_color>
  <code>entity::set_display_glow_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Glow Color\
**Type:** Action without value\
**Description:** Sets the glow color for the render entity.
**Work_with:**\
&nbsp;&nbsp;Item Renderers\
&nbsp;&nbsp;Block Renderers

**Usage example:** 
```ts
entity::set_display_glow_color("color_hexadecimal");
```

<h3 id=entity_set_display_interpolation>
  <code>entity::set_display_interpolation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Interpolation\
**Type:** Action without value\
**Description:** Sets the interpolation duration for the renderer entity.
**Work_with:**\
&nbsp;&nbsp;Any Display Entity

**Usage example:** 
```ts
entity::set_display_interpolation(1,2);
```

<h3 id=entity_set_display_rotation_from_axis_angle>
  <code>entity::set_display_rotation_from_axis_angle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation From Axis Vector\
**Type:** Action without value\
**Description:** Sets left or right rotation by axis vector and angle of the renderer entity.
**Work_with:**\
&nbsp;&nbsp;Any Render Entity

**Usage example:** 
```ts
entity::set_display_rotation_from_axis_angle(vector(0,0,0),1,"SET","DEGREES","LEFT_ROTATION");
```

<h3 id=entity_set_display_rotation_from_euler_angles>
  <code>entity::set_display_rotation_from_euler_angles</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation From Euler Angles\
**Type:** Action without value\
**Description:** Sets left or right Euler angle rotation for the renderer entity.
**Work_with:**\
&nbsp;&nbsp;Any renderer entity

**Usage example:** 
```ts
entity::set_display_rotation_from_euler_angles(1,2,3,"SET","DEGREES","LEFT_ROTATION");
```

<h3 id=entity_set_display_scale>
  <code>entity::set_display_scale</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scale\
**Type:** Action without value\
**Description:** Sets the size of the renderer entity.
**Work_with:**\
&nbsp;&nbsp;Any Render Entity

**Usage example:** 
```ts
entity::set_display_scale(vector(0,0,0),"SET");
```

<h3 id=entity_set_display_shadow>
  <code>entity::set_display_shadow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Shadow Settings\
**Type:** Action without value\
**Description:** Sets the size and transparency of the shadow of the entity renderer.
**Work_with:**\
&nbsp;&nbsp;Any Display Entity

**Usage example:** 
```ts
entity::set_display_shadow(1,2);
```

<h3 id=entity_set_display_teleport_duration>
  <code>entity::set_display_teleport_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::set_display_teleport_duration(1);
```

<h3 id=entity_set_display_transformation_matrix>
  <code>entity::set_display_transformation_matrix</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Transformation Matrix\
**Type:** Action without value\
**Description:** Sets the transformation matrix (row-column) of the renderer entity.
**Work_with:**\
&nbsp;&nbsp;Any Render Entity

**Usage example:** 
```ts
entity::set_display_transformation_matrix([1, 2]);
```

<h3 id=entity_set_display_translation>
  <code>entity::set_display_translation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Translation\
**Type:** Action without value\
**Description:** Sets an offset to the renderer entity.
**Work_with:**\
&nbsp;&nbsp;Any Display Entity

**Usage example:** 
```ts
entity::set_display_translation(vector(0,0,0),"SET");
```

<h3 id=entity_set_display_view_range>
  <code>entity::set_display_view_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visibility Range\
**Type:** Action without value\
**Description:** Sets the visibility range of the renderer entity.
**Work_with:**\
&nbsp;&nbsp;Any Viewer Entity

**Usage example:** 
```ts
entity::set_display_view_range(1);
```

<h3 id=entity_set_dragon_phase>
  <code>entity::set_dragon_phase</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Ender Dragon Phase\
**Type:** Action without value\
**Description:** Sets a specific phase for an Ender Dragon.
**Work_with:**\
&nbsp;&nbsp;Ender Dragons

**Usage example:** 
```ts
entity::set_dragon_phase("BREATH_ATTACK");
```

<h3 id=entity_set_dye_color>
  <code>entity::set_dye_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Color\
**Type:** Action without value\
**Description:** Sets a specific color for an entity.
**Work_with:**\
&nbsp;&nbsp;Sheep\
&nbsp;&nbsp;Shulkers\
&nbsp;&nbsp;Dog Collars\
&nbsp;&nbsp;Cat Collars

**Usage example:** 
```ts
entity::set_dye_color("BLACK");
```

<h3 id=entity_set_end_crystal_beam>
  <code>entity::set_end_crystal_beam</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set End Crystal Beam\
**Type:** Action without value\
**Description:** Points an End Crystal Beam to a specific location.
**Work_with:**\
&nbsp;&nbsp;End Crystals

**Usage example:** 
```ts
entity::set_end_crystal_beam(location(0,0,0,0,0));
```

<h3 id=entity_set_enderman_block>
  <code>entity::set_enderman_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block to Enderman\
**Type:** Action without value\
**Description:** Sets the rendered block to the enderman.
**Work_with:**\
&nbsp;&nbsp;Endermen

**Usage example:** 
```ts
entity::set_enderman_block(item("stone"));
```

<h3 id=entity_set_equipment_item>
  <code>entity::set_equipment_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Equipment\
**Type:** Action without value\
**Description:** Sets an item to one of the equipment slots (armor and items in hands) of an entity.

**Usage example:** 
```ts
entity::set_equipment_item(item("stick"),"CHEST");
```

<h3 id=entity_set_explosive_power>
  <code>entity::set_explosive_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Explosive Power\
**Type:** Action without value\
**Description:** Sets the power of an entity's explosion.
**Work_with:**\
&nbsp;&nbsp;Creepers\
&nbsp;&nbsp;TNT\
&nbsp;&nbsp;Fireballs

**Usage example:** 
```ts
entity::set_explosive_power(1);
```

<h3 id=entity_set_fall_distance>
  <code>entity::set_fall_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fall Distance\
**Type:** Action without value\
**Description:** Sets the distance at which an entity falls.

**Usage example:** 
```ts
entity::set_fall_distance(1);
```

<h3 id=entity_set_falling_block_type>
  <code>entity::set_falling_block_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::set_falling_block_type(item("stone"));
```

<h3 id=entity_set_fire_ticks>
  <code>entity::set_fire_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set on Fire\
**Type:** Action without value\
**Description:** Sets an entity on fire for the selected amount of time.

**Usage example:** 
```ts
entity::set_fire_ticks(1);
```

<h3 id=entity_set_fishing_wait>
  <code>entity::set_fishing_wait</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fishing Delay\
**Type:** Action without value\
**Description:** Sets the entity's fishing delay in ticks.
**Work_with:**\
&nbsp;&nbsp;Fish Hook

**Usage example:** 
```ts
entity::set_fishing_wait(1);
```

<h3 id=entity_set_fox_leaping>
  <code>entity::set_fox_leaping</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fox Leaping Animation\
**Type:** Action without value\
**Description:** Sets the fox's jumping animation.
**Work_with:**\
&nbsp;&nbsp;Foxes

**Usage example:** 
```ts
entity::set_fox_leaping("TRUE");
```

<h3 id=entity_set_fox_type>
  <code>entity::set_fox_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fox Type\
**Type:** Action without value\
**Description:** Sets the fox type.
**Work_with:**\
&nbsp;&nbsp;Foxes

**Usage example:** 
```ts
entity::set_fox_type("RED");
```

<h3 id=entity_set_freeze_ticks>
  <code>entity::set_freeze_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Freeze Time\
**Type:** Action without value\
**Description:** Sets the freeze time for an entity (the number of ticks an entity has spent in loose snow).

**Usage example:** 
```ts
entity::set_freeze_ticks(1,"TRUE");
```

<h3 id=entity_set_frog_type>
  <code>entity::set_frog_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Frog Type\
**Type:** Action without value\
**Description:** Sets the color of the frog.
**Work_with:**\
&nbsp;&nbsp;Toads

**Usage example:** 
```ts
entity::set_frog_type("COLD");
```

<h3 id=entity_set_gliding>
  <code>entity::set_gliding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Elytra Flying\
**Type:** Action without value\
**Description:** Sets the creature's elytra flying state.

**Usage example:** 
```ts
entity::set_gliding("TRUE");
```

<h3 id=entity_set_glowing>
  <code>entity::set_glowing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Glowing\
**Type:** Action without value\
**Description:** Sets an entity to a glowing effect.

**Usage example:** 
```ts
entity::set_glowing("TRUE");
```

<h3 id=entity_set_glow_squid_dark>
  <code>entity::set_glow_squid_dark</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Squid Glow Time\
**Type:** Action without value\
**Description:** Sets the duration of darkness in ticks for the glowing octopus.
**Work_with:**\
&nbsp;&nbsp;Glowing Octopuses

**Usage example:** 
```ts
entity::set_glow_squid_dark(1);
```

<h3 id=entity_set_goat_screaming>
  <code>entity::set_goat_screaming</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Goat Screaming\
**Type:** Action without value\
**Description:** Sets the "screaming" goat tag.
**Work_with:**\
&nbsp;&nbsp;Goat

**Usage example:** 
```ts
entity::set_goat_screaming("TRUE");
```

<h3 id=entity_set_gravity>
  <code>entity::set_gravity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Gravity\
**Type:** Action without value\
**Description:** Sets whether an entity will obey gravity.

**Usage example:** 
```ts
entity::set_gravity("TRUE");
```

<h3 id=entity_set_horse_jump>
  <code>entity::set_horse_jump</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Horse Jump Power\
**Type:** Action without value\
**Description:** Sets the horse's jump power.
**Work_with:**\
&nbsp;&nbsp;Horses\
&nbsp;&nbsp;Donkeys\
&nbsp;&nbsp;Mules\
&nbsp;&nbsp;Lamas

**Usage example:** 
```ts
entity::set_horse_jump(1);
```

<h3 id=entity_set_horse_pattern>
  <code>entity::set_horse_pattern</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Horse Pattern\
**Type:** Action without value\
**Description:** Sets the color and pattern of the horse.
**Work_with:**\
&nbsp;&nbsp;Horses

**Usage example:** 
```ts
entity::set_horse_pattern("WHITE","NONE");
```

<h3 id=entity_set_immune_to_zombification>
  <code>entity::set_immune_to_zombification</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None\
&nbsp;&nbsp;None\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::set_immune_to_zombification("TRUE");
```

<h3 id=entity_set_interaction_responsive>
  <code>entity::set_interaction_responsive</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** SetInteractionEntityResponsiveness\
**Type:** Action without value\
**Description:** Sets whether an interaction entity will be responsive to interactions.

**Usage example:** 
```ts
entity::set_interaction_responsive("TRUE");
```

<h3 id=entity_set_interaction_size>
  <code>entity::set_interaction_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Interaction Entity Size\
**Type:** Action without value\
**Description:** Sets the horizontal and vertical sizes of an interaction entity.

**Usage example:** 
```ts
entity::set_interaction_size(1,2);
```

<h3 id=entity_set_invisible>
  <code>entity::set_invisible</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Invisible Mode\
**Type:** Action without value\
**Description:** Sets an entity to invisible mode.

**Usage example:** 
```ts
entity::set_invisible("TRUE");
```

<h3 id=entity_set_invulnerability_ticks>
  <code>entity::set_invulnerability_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Invulnerability Duration\
**Type:** Action without value\
**Description:** Sets the invulnerability duration for a creature.

**Usage example:** 
```ts
entity::set_invulnerability_ticks(1);
```

<h3 id=entity_set_invulnerable>
  <code>entity::set_invulnerable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Invulnerable\
**Type:** Action without value\
**Description:** Sets an entity's invulnerability, but can deal damage in creative mode.

**Usage example:** 
```ts
entity::set_invulnerable("TRUE");
```

<h3 id=entity_set_item>
  <code>entity::set_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Item Type\
**Type:** Action without value\
**Description:** Sets a specific type (ID) to an Item entity.
**Work_with:**\
&nbsp;&nbsp;Items

**Usage example:** 
```ts
entity::set_item(item("stick"));
```

<h3 id=entity_set_item_display_item>
  <code>entity::set_item_display_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Display Item\
**Type:** Action without value\
**Description:** Sets the display item to the item renderer.
**Work_with:**\
&nbsp;&nbsp;Item Renderers

**Usage example:** 
```ts
entity::set_item_display_item(item("stick"));
```

<h3 id=entity_set_item_display_model_type>
  <code>entity::set_item_display_model_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Model Type\
**Type:** Action without value\
**Description:** Sets the type of the item's display model to the item renderer.
**Work_with:**\
&nbsp;&nbsp;Item Renderers

**Usage example:** 
```ts
entity::set_item_display_model_type("FIRSTPERSON_LEFTHAND");
```

<h3 id=entity_set_item_in_frame>
  <code>entity::set_item_in_frame</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item in Frame\
**Type:** Action without value\
**Description:** Sets the specified item in a frame.
**Work_with:**\
&nbsp;&nbsp;Within Frames

**Usage example:** 
```ts
entity::set_item_in_frame(item("stick"));
```

<h3 id=entity_set_llama_type>
  <code>entity::set_llama_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Llama Color\
**Type:** Action without value\
**Description:** Sets the color of the llama.
**Work_with:**\
&nbsp;&nbsp;Lamas

**Usage example:** 
```ts
entity::set_llama_type("BROWN");
```

<h3 id=entity_set_marker>
  <code>entity::set_marker</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Marker Mode\
**Type:** Action without value\
**Description:** Sets the armor rack marker mode.
**Work_with:**\
&nbsp;&nbsp;Armor Stands

**Usage example:** 
```ts
entity::set_marker("TRUE");
```

<h3 id=entity_set_max_health>
  <code>entity::set_max_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Max Health\
**Type:** Action without value\
**Description:** Sets the maximum amount of health for an entity.

**Usage example:** 
```ts
entity::set_max_health(1,"TRUE");
```

<h3 id=entity_set_merchant_recipe>
  <code>entity::set_merchant_recipe</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Merchant Recipe\
**Type:** Action without value\
**Description:** Sets an item to a Villager for certain items at the specified index.
**Work_with:**\
&nbsp;&nbsp;Villagers\
&nbsp;&nbsp;Wandering Traders

**Usage example:** 
```ts
entity::set_merchant_recipe(item("stick"),item("stick"),item("stick"),1,"MERGE",2,3,4,5,6,7,"TRUE","TRUE");
```

<h3 id=entity_set_minecart_block>
  <code>entity::set_minecart_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block to Minecart\
**Type:** Action without value\
**Description:** Sets the specified block into the Minecart.
**Work_with:**\
&nbsp;&nbsp;Minecarts

**Usage example:** 
```ts
entity::set_minecart_block(item("stone"),1);
```

<h3 id=entity_set_mob_aggressive>
  <code>entity::set_mob_aggressive</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
entity::set_mob_aggressive("TRUE");
```

<h3 id=entity_set_mushroom_cow_type>
  <code>entity::set_mushroom_cow_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Mushroom Cow Type\
**Type:** Action without value\
**Description:** Sets the mushroom cow type.
**Work_with:**\
&nbsp;&nbsp;Mushroom Cows

**Usage example:** 
```ts
entity::set_mushroom_cow_type("BROWN");
```

<h3 id=entity_set_panda_gene>
  <code>entity::set_panda_gene</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Panda Gene\
**Type:** Action without value\
**Description:** Sets the panda gene. This affects their behavior and appearance.
**Work_with:**\
&nbsp;&nbsp;Pandas

**Usage example:** 
```ts
entity::set_panda_gene("MAIN","NORMAL");
```

<h3 id=entity_set_parrot_type>
  <code>entity::set_parrot_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Parrot Type\
**Type:** Action without value\
**Description:** Sets the parrot type.
**Work_with:**\
&nbsp;&nbsp;Parrots

**Usage example:** 
```ts
entity::set_parrot_type("BLUE");
```

<h3 id=entity_set_persistence>
  <code>entity::set_persistence</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Persistence\
**Type:** Action without value\
**Description:** Sets whether an item or falling block will persist.
**Work_with:**\
&nbsp;&nbsp;Entity\
&nbsp;&nbsp;Falling Blocks

**Usage example:** 
```ts
entity::set_persistence("TRUE");
```

<h3 id=entity_set_pickup_delay>
  <code>entity::set_pickup_delay</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Pickup Delay\
**Type:** Action without value\
**Description:** Sets the number of ticks an item cannot be picked up.
**Work_with:**\
&nbsp;&nbsp;Items

**Usage example:** 
```ts
entity::set_pickup_delay(1);
```

<h3 id=entity_set_piglin_able_to_hunt>
  <code>entity::set_piglin_able_to_hunt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::set_piglin_able_to_hunt("TRUE");
```

<h3 id=entity_set_piglin_charging_crossbow>
  <code>entity::set_piglin_charging_crossbow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::set_piglin_charging_crossbow("TRUE");
```

<h3 id=entity_set_piglin_dancing>
  <code>entity::set_piglin_dancing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None\
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::set_piglin_dancing(1);
```

<h3 id=entity_set_pose>
  <code>entity::set_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Pose\
**Type:** Action without value\
**Description:** Sets a specific pose for an entity.

**Usage example:** 
```ts
entity::set_pose("CROAKING");
```

<h3 id=entity_set_potion_cloud_radius>
  <code>entity::set_potion_cloud_radius</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Effect Cloud Radius\
**Type:** Action without value\
**Description:** Sets the radius of the effect cloud and how fast it expands.
**Work_with:**\
&nbsp;&nbsp;Effect Cloud

**Usage example:** 
```ts
entity::set_potion_cloud_radius(1,2);
```

<h3 id=entity_set_primed_tnt_block>
  <code>entity::set_primed_tnt_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::set_primed_tnt_block(item("stone"));
```

<h3 id=entity_set_projectile_display_item>
  <code>entity::set_projectile_display_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Projectile Item\
**Type:** Action without value\
**Description:** Sets the projectile's visible item.

**Usage example:** 
```ts
entity::set_projectile_display_item(item("stick"));
```

<h3 id=entity_set_projectile_shooter>
  <code>entity::set_projectile_shooter</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Projectile Shooter\
**Type:** Action without value\
**Description:** Sets the specified creature as a projectile shooter.

**Usage example:** 
```ts
entity::set_projectile_shooter("uuid");
```

<h3 id=entity_set_rabbit_type>
  <code>entity::set_rabbit_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rabbit Type\
**Type:** Action without value\
**Description:** Sets the rabbit type.
**Work_with:**\
&nbsp;&nbsp;Rabbits

**Usage example:** 
```ts
entity::set_rabbit_type("BLACK");
```

<h3 id=entity_set_rearing>
  <code>entity::set_rearing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Horse Pose\
**Type:** Action without value\
**Description:** Sets whether the horse will stand on its hind legs.
**Work_with:**\
&nbsp;&nbsp;Horses

**Usage example:** 
```ts
entity::set_rearing("TRUE");
```

<h3 id=entity_set_riptiding>
  <code>entity::set_riptiding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Riptiding Animation\
**Type:** Action without value\
**Description:** Sets the animation for an entity to use the Riptiding Trident Enchantment.

**Usage example:** 
```ts
entity::set_riptiding("TRUE");
```

<h3 id=entity_set_rotation>
  <code>entity::set_rotation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation\
**Type:** Action without value\
**Description:** Sets the rotation of an entity.

**Usage example:** 
```ts
entity::set_rotation(1,2);
```

<h3 id=entity_set_rotation_by_vector>
  <code>entity::set_rotation_by_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation By Vector\
**Type:** Action without value\
**Description:** Sets the entity rotation by vector.

**Usage example:** 
```ts
entity::set_rotation_by_vector(vector(0,0,0));
```

<h3 id=entity_set_sheep_sheared>
  <code>entity::set_sheep_sheared</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sheep Wool\
**Type:** Action without value\
**Description:** Sets whether sheep will have wool.
**Work_with:**\
&nbsp;&nbsp;Sheep

**Usage example:** 
```ts
entity::set_sheep_sheared("TRUE");
```

<h3 id=entity_set_shulker_bullet_target>
  <code>entity::set_shulker_bullet_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Shulker Bullet Target\
**Type:** Action without value\
**Description:** Sets an attack target for a Shulker projectile.
**Work_with:**\
&nbsp;&nbsp;Shulker Bullets

**Usage example:** 
```ts
entity::set_shulker_bullet_target("target");
```

<h3 id=entity_set_silenced>
  <code>entity::set_silenced</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Silence Entity\
**Type:** Action without value\
**Description:** Removes entity sounds.

**Usage example:** 
```ts
entity::set_silenced("TRUE");
```

<h3 id=entity_set_sitting>
  <code>entity::set_sitting</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sitting Mode\
**Type:** Action without value\
**Description:** Sets the entity's sitting mode.
**Work_with:**\
&nbsp;&nbsp;Wolf\
&nbsp;&nbsp;Cats\
&nbsp;&nbsp;Parrot\
&nbsp;&nbsp;Foxes\
&nbsp;&nbsp;Pandas

**Usage example:** 
```ts
entity::set_sitting("TRUE");
```

<h3 id=entity_set_size>
  <code>entity::set_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Size\
**Type:** Action without value\
**Description:** Sets the size of an entity.
**Work_with:**\
&nbsp;&nbsp;Slime\
&nbsp;&nbsp;Phantoms

**Usage example:** 
```ts
entity::set_size(1);
```

<h3 id=entity_set_sniffer_state>
  <code>entity::set_sniffer_state</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sniffer State\
**Type:** Action without value\
**Description:** Sets a specific state for the sniffer.
**Work_with:**\
&nbsp;&nbsp;Sniffer

**Usage example:** 
```ts
entity::set_sniffer_state("DIGGING");
```

<h3 id=entity_set_snowman_pumpkin>
  <code>entity::set_snowman_pumpkin</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Pumpkin to Snow Golem\
**Type:** Action without value\
**Description:** Sets the visibility of the pumpkin to the Snow Golem.
**Work_with:**\
&nbsp;&nbsp;Snow Golems

**Usage example:** 
```ts
entity::set_snowman_pumpkin("TRUE");
```

<h3 id=entity_set_tame>
  <code>entity::set_tame</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Tame Entity\
**Type:** Action without value\
**Description:** Sets an entity's tame to the specified owner.
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
```

<h3 id=entity_set_target>
  <code>entity::set_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Target\
**Type:** Action without value\
**Description:** Instructs the entity AI to target a specific entity.\
**Additional info:**\
&nbsp;&nbsp;Leave an empty slot in the Text field to remove the target.\
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:** 
```ts
entity::set_target("name_or_uuid");
```

<h3 id=entity_set_text_display_alignment>
  <code>entity::set_text_display_alignment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text Alignment\
**Type:** Action without value\
**Description:** Sets the text alignment of the text renderer.
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:** 
```ts
entity::set_text_display_alignment("CENTER");
```

<h3 id=entity_set_text_display_background>
  <code>entity::set_text_display_background</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Background Color\
**Type:** Action without value\
**Description:** Sets the background color and transparency of the text renderer.
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:** 
```ts
entity::set_text_display_background("color_hexadecimal",1);
```

<h3 id=entity_set_text_display_line_width>
  <code>entity::set_text_display_line_width</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Line Width\
**Type:** Action without value\
**Description:** Sets the maximum line width for the text renderer.
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:** 
```ts
entity::set_text_display_line_width(1);
```

<h3 id=entity_set_text_display_opacity>
  <code>entity::set_text_display_opacity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text Opacity\
**Type:** Action without value\
**Description:** Sets the transparency of text to the text renderer.
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:** 
```ts
entity::set_text_display_opacity(1);
```

<h3 id=entity_set_text_display_see_through>
  <code>entity::set_text_display_see_through</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visibility Through Blocks\
**Type:** Action without value\
**Description:** Sets the visibility of text through blocks to the text renderer.
**Work_with:**\
&nbsp;&nbsp;Text Visualizers

**Usage example:** 
```ts
entity::set_text_display_see_through("TRUE");
```

<h3 id=entity_set_text_display_text>
  <code>entity::set_text_display_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Display Text\
**Type:** Action without value\
**Description:** Sets the display text for the text renderer.
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:** 
```ts
entity::set_text_display_text(["displayed_text", "displayed_text"],"SPACES");
```

<h3 id=entity_set_text_display_text_shadow>
  <code>entity::set_text_display_text_shadow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text Shadow\
**Type:** Action without value\
**Description:** Sets the visibility of the text shadow to the text renderer.
**Work_with:**\
&nbsp;&nbsp;Text Renderers

**Usage example:** 
```ts
entity::set_text_display_text_shadow("TRUE");
```

<h3 id=entity_set_tropical_fish_pattern>
  <code>entity::set_tropical_fish_pattern</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fish Pattern\
**Type:** Action without value\
**Description:** Sets the color and pattern of a tropical fish.
**Work_with:**\
&nbsp;&nbsp;Tropical Fish

**Usage example:** 
```ts
entity::set_tropical_fish_pattern("WHITE","WHITE","KOB");
```

<h3 id=entity_set_location>
  <code>entity::set_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch By Vector\
**Type:** Action without value\
**Description:** Launches an entity at the specified vector.

**Usage example:** 
```ts
entity::set_location(vector(0,0,0),"TRUE");
```

<h3 id=entity_set_vex_charging>
  <code>entity::set_vex_charging</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::set_vex_charging("TRUE");
```

<h3 id=entity_set_vex_limited_lifetime_ticks>
  <code>entity::set_vex_limited_lifetime_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
entity::set_vex_limited_lifetime_ticks(1);
```

<h3 id=entity_set_villager_biome>
  <code>entity::set_villager_biome</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Villager Biome\
**Type:** Action without value\
**Description:** Sets a villager's color based on the selected biome.
**Work_with:**\
&nbsp;&nbsp;Villagers

**Usage example:** 
```ts
entity::set_villager_biome("DESERT");
```

<h3 id=entity_set_villager_experience>
  <code>entity::set_villager_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Villager Experience\
**Type:** Action without value\
**Description:** Sets the villager experience amount.
**Work_with:**\
&nbsp;&nbsp;Villagers

**Usage example:** 
```ts
entity::set_villager_experience(1);
```

<h3 id=entity_set_villager_profession>
  <code>entity::set_villager_profession</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set a Villager's Profession\
**Type:** Action without value\
**Description:** Sets a specific profession for a villager.
**Work_with:**\
&nbsp;&nbsp;Villager\
&nbsp;&nbsp;Zombie Villagers

**Usage example:** 
```ts
entity::set_villager_profession("NONE");
```

<h3 id=entity_set_visual_fire>
  <code>entity::set_visual_fire</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Fire\
**Type:** Action without value\
**Description:** Displays fire on a creature.

**Usage example:** 
```ts
entity::set_visual_fire("TRUE");
```

<h3 id=entity_set_warden_anger_level>
  <code>entity::set_warden_anger_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Warden Anger Level\
**Type:** Action without value\
**Description:** Sets the Guardian's anger level to the specified creature.\
**Additional info:**\
&nbsp;&nbsp;If an entity's anger level reaches 80, the Guardian will actively pursue it.\
**Work_with:**\
&nbsp;&nbsp;Guardians

**Usage example:** 
```ts
entity::set_warden_anger_level("name_or_uuid",1);
```

<h3 id=entity_set_warden_digging>
  <code>entity::set_warden_digging</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
entity::set_warden_digging("EMERGE");
```

<h3 id=entity_set_wearing_saddle>
  <code>entity::set_wearing_saddle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Saddle Visibility\
**Type:** Action without value\
**Description:** Sets a saddle to an entity.
**Work_with:**\
&nbsp;&nbsp;Pigs\
&nbsp;&nbsp;Horses\
&nbsp;&nbsp;Lavomers

**Usage example:** 
```ts
entity::set_wearing_saddle("TRUE");
```

<h3 id=entity_set_wither_invulnerability_ticks>
  <code>entity::set_wither_invulnerability_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Wither Invulnerability\
**Type:** Action without value\
**Description:** Sets the duration of the Wither's invulnerability.
**Work_with:**\
&nbsp;&nbsp;Wither

**Usage example:** 
```ts
entity::set_wither_invulnerability_ticks(1);
```

<h3 id=entity_set_zombie_arms_raised>
  <code>entity::set_zombie_arms_raised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Zombie Arms Raised\
**Type:** Action without value\
**Description:** Sets the zombie arm raise animation.

**Usage example:** 
```ts
entity::set_zombie_arms_raised("TRUE");
```

<h3 id=entity_shear_sheep>
  <code>entity::shear_sheep</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shear Sheep\
**Type:** Action without value\
**Description:** Shears a sheep.
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
**Type:** Action without value\
**Description:** Sets an entity's sleep animation. It is best to use this action in a loop.
**Work_with:**\
&nbsp;&nbsp;Foxes

**Usage example:** 
```ts
entity::sleep("TRUE");
```

<h3 id=entity_swing_hand>
  <code>entity::swing_hand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Swing Hand Animation\
**Type:** Action without value\
**Description:** Plays a swinging hand animation for the entity.

**Usage example:** 
```ts
entity::swing_hand("MAIN");
```

<h3 id=entity_teleport>
  <code>entity::teleport</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Teleport\
**Type:** Action without value\
**Description:** Teleports an entity to the selected location.

**Usage example:** 
```ts
entity::teleport(location(0,0,0,0,0),"TRUE");
```

<h3 id=entity_use_item>
  <code>entity::use_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Use an Item\
**Type:** Action without value\
**Description:** Instructs the AI creature to use the item in its hand.
**Work_with:**\
&nbsp;&nbsp;Mobs

**Usage example:** 
```ts
entity::use_item("MAIN_HAND","TRUE");
```

<h3 id=if_entity_collides_at_location>
  <code>entity::collides_at_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

**Usage example:** 
```ts
if(entity::collides_at_location(location(0,0,0,0,0)){
    player::message("Condition is true");
}
```

<h3 id=if_entity_collides_using_hitbox>
  <code>entity::collides_using_hitbox</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

**Usage example:** 
```ts
if(entity::collides_using_hitbox(location(0,0,0,0,0),location(0,0,0,0,0)){
    player::message("Condition is true");
}
```

<h3 id=if_entity_collides_with_entity>
  <code>entity::collides_with_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

**Usage example:** 
```ts
if(entity::collides_with_entity("name_or_uuid","OVERLAPS"){
    player::message("Condition is true");
}
```

<h3 id=if_entity_exists>
  <code>entity::exists</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Exists\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is in the world.

**Usage example:** 
```ts
if(entity::exists(){
    player::message("Condition is true");
}
```

<h3 id=if_entity_has_custom_tag>
  <code>entity::has_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has Custom Tag\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity has a custom tag with the specified value.

**Usage example:** 
```ts
if(entity::has_custom_tag("tag","tag_value"){
    player::message("Condition is true");
}
```

<h3 id=if_entity_has_potion_effect>
  <code>entity::has_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has Potion Effect\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity has the effect of a potion.

**Usage example:** 
```ts
if(entity::has_potion_effect([potion("slow_falling"), potion("slow_falling")],"ANY"){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_disguised>
  <code>entity::is_disguised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguised\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is disguised.

**Usage example:** 
```ts
if(entity::is_disguised(){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_grounded>
  <code>entity::is_grounded</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is On Ground\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is touching the surface of a block.

**Usage example:** 
```ts
if(entity::is_grounded(){
    player::message("Condition is true");
}
```

<h3 id=if_entity_in_area>
  <code>entity::in_area</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Inside Region\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is in a certain region.

**Usage example:** 
```ts
if(entity::in_area(location(0,0,0,0,0),location(0,0,0,0,0),"TRUE","POINT","OVERLAPS"){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_item>
  <code>entity::is_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is an Item\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is an item.

**Usage example:** 
```ts
if(entity::is_item(){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_mob>
  <code>entity::is_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is a Mob\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is a mob.

**Usage example:** 
```ts
if(entity::is_mob(){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_near_location>
  <code>entity::is_near_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Near location\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is near the specified location.

**Usage example:** 
```ts
if(entity::is_near_location("TRUE",location(0,0,0,0,0),1){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_projectile>
  <code>entity::is_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is a Projectile\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is a projectile.

**Usage example:** 
```ts
if(entity::is_projectile(){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_riding_entity>
  <code>entity::is_riding_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Riding Entity\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is riding any of the other specified entities.

**Usage example:** 
```ts
if(entity::is_riding_entity(["entity_ids", "entity_ids"],"NEAREST"){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_standing_on_block>
  <code>entity::is_standing_on_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Standing On a Block\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is standing on a block of a certain category or a certain location.

**Usage example:** 
```ts
if(entity::is_standing_on_block([item("stone"), item("stone")],[location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE"){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_type>
  <code>entity::is_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Entity Type Is\
**Type:** Action that checks the conditions\
**Description:** Checks if the entity type is equal to the type in the chest.

**Usage example:** 
```ts
if(entity::is_type([item("stick"), item("stick")]){
    player::message("Condition is true");
}
```

<h3 id=if_entity_is_vehicle>
  <code>entity::is_vehicle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is a Vehicle\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity is a vehicle.

**Usage example:** 
```ts
if(entity::is_vehicle(){
    player::message("Condition is true");
}
```

<h3 id=if_entity_name_equals>
  <code>entity::name_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Name Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if an entity's name is equal to the name in the chest.

**Usage example:** 
```ts
if(entity::name_equals(["names_or_uuids", "names_or_uuids"]){
    player::message("Condition is true");
}
```

<h3 id=if_entity_spawn_reason_equals>
  <code>entity::spawn_reason_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Reason Is\
**Type:** Action that checks the conditions\
**Description:** Checks if the entity spawn reason is equal to a certain value.

**Usage example:** 
```ts
if(entity::spawn_reason_equals("BEEHIVE"){
    player::message("Condition is true");
}
```

