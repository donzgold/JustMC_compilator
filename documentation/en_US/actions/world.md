<h3 id=game_block_growth>
  <code>world::block_growth</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Growth Stage\
**Type:** Action without value\
**Description:** Sets the growth stage for the block at the selected location.

**Usage example:** 
```ts
world::block_growth(location(0,0,0,0,0),1,"STAGE_NUMBER");
```

<h3 id=game_bloom_skulk_catalyst>
  <code>world::bloom_skulk_catalyst</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::bloom_skulk_catalyst(location(0,0,0,0,0),location(0,0,0,0,0),1);
```

<h3 id=game_bone_meal_block>
  <code>world::bone_meal_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Bonemeal Block\
**Type:** Action without value\
**Description:** Bonemeals a block at the selected location.

**Usage example:** 
```ts
world::bone_meal_block(location(0,0,0,0,0),1);
```

<h3 id=game_break_block>
  <code>world::break_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Break Block\
**Type:** Action without value\
**Description:** Breaks blocks at the specified locations as if it were done by a Survival player with the right tool.

**Usage example:** 
```ts
world::break_block([location(0,0,0,0,0), location(0,0,0,0,0)],item("stick"),"TRUE");
```

<h3 id=game_cancel_event>
  <code>world::cancel_event</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Cancel Event\
**Type:** Action without value\
**Description:** Cancels the start event that triggered this code.

**Usage example:** 
```ts
world::cancel_event();
```

<h3 id=game_clear_container>
  <code>world::clear_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Container\
**Type:** Action without value\
**Description:** Removes all items from a container at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::clear_container(location(0,0,0,0,0));
```

<h3 id=game_clear_container_items>
  <code>world::clear_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Container Items\
**Type:** Action without value\
**Description:** Clears the specified items from a container.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::clear_container_items(location(0,0,0,0,0),[item("stick"), item("stick")]);
```

<h3 id=game_clear_exploded_blocks>
  <code>world::clear_exploded_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Exploded Blocks\
**Type:** Action without value\
**Description:** Returns exploded blocks to their original position.
**Work_with:**\
&nbsp;&nbsp;Entity Explode Event\
&nbsp;&nbsp;Block Explode Event

**Usage example:** 
```ts
world::clear_exploded_blocks([location(0,0,0,0,0), location(0,0,0,0,0)]);
```

<h3 id=game_clear_region>
  <code>world::clear_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Region\
**Type:** Action without value\
**Description:** Removes all blocks in a region.

**Usage example:** 
```ts
world::clear_region(location(0,0,0,0,0),location(0,0,0,0,0));
```

<h3 id=game_clear_scoreboard_scores>
  <code>world::clear_scoreboard_scores</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Scoreboard Values\
**Type:** Action without value\
**Description:** Clears all values of the specified scoreboard.

**Usage example:** 
```ts
world::clear_scoreboard_scores("id");
```

<h3 id=game_clone_region>
  <code>world::clone_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clone Region Blocks\
**Type:** Action without value\
**Description:** Clones a region to the selected location.

**Usage example:** 
```ts
world::clone_region(location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),"TRUE","TRUE");
```

<h3 id=game_create_explosion>
  <code>world::create_explosion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Explosion\
**Type:** Action without value\
**Description:** Creates an explosion at the specified location.

**Usage example:** 
```ts
world::create_explosion(location(0,0,0,0,0),1);
```

<h3 id=game_create_scoreboard>
  <code>world::create_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Scoreboard\
**Type:** Action without value\
**Description:** Creates a scoreboard with a specific ID. To display a scoreboard to a player, use the "Show scoreboard" action.

**Usage example:** 
```ts
world::create_scoreboard("id","display_name");
```

<h3 id=game_fill_container>
  <code>world::fill_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Fill Container\
**Type:** Action without value\
**Description:** Fills a container at the selected location with the specified items.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::fill_container(location(0,0,0,0,0),[item("stick"), item("stick")]);
```

<h3 id=game_generate_tree>
  <code>world::generate_tree</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Generate Tree\
**Type:** Action without value\
**Description:** Generates a tree at the selected location.

**Usage example:** 
```ts
world::generate_tree(location(0,0,0,0,0),"TREE");
```

<h3 id=game_hide_event_message>
  <code>world::hide_event_message</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Hide Event Message\
**Type:** Action without value\
**Description:** Removes the message from the event that triggered this code.
**Work_with:**\
&nbsp;&nbsp;Player Join Event\
&nbsp;&nbsp;Player Quit Event\
&nbsp;&nbsp;Player Death Event

**Usage example:** 
```ts
world::hide_event_message("TRUE");
```

<h3 id=game_launch_firework>
  <code>world::launch_firework</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Firework\
**Type:** Action without value\
**Description:** Launches firework at the specified location.

**Usage example:** 
```ts
world::launch_firework(item("stick"),location(0,0,0,0,0),"UPWARDS","TRUE");
```

<h3 id=game_launch_projectile>
  <code>world::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Projectile\
**Type:** Action without value\
**Description:** Launches a projectile at the specified location.

**Usage example:** 
```ts
world::launch_projectile(item("stick"),location(0,0,0,0,0),1,2,"custom_name",particle("fire"));
```

<h3 id=game_random_tick_block>
  <code>world::random_tick_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Random Tick Block\
**Type:** Action without value\
**Description:** Updates a block (random tick) at the selected location.

**Usage example:** 
```ts
world::random_tick_block(location(0,0,0,0,0),1);
```

<h3 id=game_remove_container_items>
  <code>world::remove_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Items From Container\
**Type:** Action without value\
**Description:** Removes the specified items from a container at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::remove_container_items(location(0,0,0,0,0),[item("stick"), item("stick")]);
```

<h3 id=game_remove_scoreboard>
  <code>world::remove_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Scoreboard\
**Type:** Action without value\
**Description:** Removes the specified scoreboard.

**Usage example:** 
```ts
world::remove_scoreboard("id");
```

<h3 id=game_remove_scoreboard_score_by_name>
  <code>world::remove_scoreboard_score_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Scoreboard Value By Text\
**Type:** Action without value\
**Description:** Removes the value of the specified scoreboard by display text.

**Usage example:** 
```ts
world::remove_scoreboard_score_by_name("id","text");
```

<h3 id=game_remove_scoreboard_score_by_score>
  <code>world::remove_scoreboard_score_by_score</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Scoreboard Value By Score\
**Type:** Action without value\
**Description:** Removes the value of the specified scoreboard by score.

**Usage example:** 
```ts
world::remove_scoreboard_score_by_score("id",1);
```

<h3 id=game_replace_blocks_in_region>
  <code>world::replace_blocks_in_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Blocks in Region\
**Type:** Action without value\
**Description:** Replaces blocks with others in the selected region.

**Usage example:** 
```ts
world::replace_blocks_in_region([item("stone"), item("stone")],location(0,0,0,0,0),location(0,0,0,0,0),item("stone"));
```

<h3 id=game_replace_container_items>
  <code>world::replace_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Items in Container\
**Type:** Action without value\
**Description:** Replaces the specified items in a container at the selected location with a specific item.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::replace_container_items([item("stick"), item("stick")],location(0,0,0,0,0),item("stick"),1);
```

<h3 id=game_send_web_request>
  <code>world::send_web_request</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Web Request\
**Type:** Action without value\
**Description:** Sends a web request with the selected method and body to the selected URL.

**Usage example:** 
```ts
world::send_web_request("url","content_body","GET","TEXT_PLAIN");
```

<h3 id=game_set_age>
  <code>world::set_age</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Age\
**Type:** Action without value\
**Description:** Sets the age of the block at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_age(location(0,0,0,0,0),1);
```

<h3 id=game_set_block_analogue_power>
  <code>world::set_block_analogue_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Redstone Signal Strength\
**Type:** Action without value\
**Description:** Sets the selected location to a specific signal strength.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_block_analogue_power(location(0,0,0,0,0),1);
```

<h3 id=game_set_block>
  <code>world::set_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block\
**Type:** Action without value\
**Description:** Sets the selected block type on selected locations.

**Usage example:** 
```ts
world::set_block(item("stone"),[location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE");
```

<h3 id=game_set_block_custom_tag>
  <code>world::set_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
world::set_block_custom_tag(location(0,0,0,0,0),"tag_name","tag_value");
```

<h3 id=game_set_block_data>
  <code>world::set_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Data\
**Type:** Action without value\
**Description:** Sets the parameters of a block at a specific location.

**Usage example:** 
```ts
world::set_block_data(location(0,0,0,0,0),"block_data");
```

<h3 id=game_set_block_drops_enabled>
  <code>world::set_block_drops_enabled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Drops\
**Type:** Action without value\
**Description:** Sets a rule in the world to drop blocks when they are broken.

**Usage example:** 
```ts
world::set_block_drops_enabled("TRUE");
```

<h3 id=game_set_block_single_data>
  <code>world::set_block_single_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
world::set_block_single_data(location(0,0,0,0,0),"data","value");
```

<h3 id=game_set_brushable_block_item>
  <code>world::set_brushable_block_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item in Suspicious Block\
**Type:** Action without value\
**Description:** Sets an item into a suspicious block (sand, gravel) at the selected location.
**Work_with:**\
&nbsp;&nbsp;None\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_brushable_block_item(location(0,0,0,0,0),item("stick"));
```

<h3 id=game_set_campfire_item>
  <code>world::set_campfire_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Campfire Item\
**Type:** Action without value\
**Description:** Sets an item to a campfire at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_campfire_item(location(0,0,0,0,0),item("stick"),1,"FIRST");
```

<h3 id=game_set_container>
  <code>world::set_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Items In Container\
**Type:** Action without value\
**Description:** Sets the specified items into a container at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_container([location(0,0,0,0,0), location(0,0,0,0,0)],[item("stick"), item("stick")]);
```

<h3 id=game_set_container_lock>
  <code>world::set_container_lock</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Container Key\
**Type:** Action without value\
**Description:** Sets a specific key to a container at the selected location.

**Usage example:** 
```ts
world::set_container_lock(location(0,0,0,0,0),"container_key");
```

<h3 id=game_set_container_name>
  <code>world::set_container_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Container Name\
**Type:** Action without value\
**Description:** Sets the name of the container at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_container_name(location(0,0,0,0,0),"name");
```

<h3 id=game_set_decorate_pot_sherd>
  <code>world::set_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_decorate_pot_sherd(location(0,0,0,0,0),item("stick"),"BACK");
```

<h3 id=game_set_event_damage>
  <code>world::set_event_damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Damage\
**Type:** Action without value\
**Description:** Sets the damage associated with this event.
**Work_with:**\
&nbsp;&nbsp;Damage Events

**Usage example:** 
```ts
world::set_event_damage(1);
```

<h3 id=game_set_event_exhaustion>
  <code>world::set_event_exhaustion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_event_exhaustion(1);
```

<h3 id=game_set_event_experience>
  <code>world::set_event_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Experience\
**Type:** Action without value\
**Description:** Sets the experience value associated with this event.
**Work_with:**\
&nbsp;&nbsp;Fishing Event\
&nbsp;&nbsp;Experience Gain Event\
&nbsp;&nbsp;Kill Events

**Usage example:** 
```ts
world::set_event_experience(1);
```

<h3 id=game_set_event_heal>
  <code>world::set_event_heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Heal\
**Type:** Action without value\
**Description:** Sets the heal value associated with this event.
**Work_with:**\
&nbsp;&nbsp;Player Heal Event\
&nbsp;&nbsp;Entity Heal Event

**Usage example:** 
```ts
world::set_event_heal(1);
```

<h3 id=game_set_event_item>
  <code>world::set_event_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Item\
**Type:** Action without value\
**Description:** Sets the item associated with this event.

**Usage example:** 
```ts
world::set_event_item(item("stick"));
```

<h3 id=game_set_event_items>
  <code>world::set_event_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_event_items([item("stick"), item("stick")]);
```

<h3 id=game_set_event_move_allowed>
  <code>world::set_event_move_allowed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Allow Movement\
**Type:** Action without value\
**Description:** Allows movement if it fails.
**Work_with:**\
&nbsp;&nbsp;Player Failed to Move Event

**Usage example:** 
```ts
world::set_event_move_allowed("TRUE");
```

<h3 id=game_set_event_projectile>
  <code>world::set_event_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Projectile\
**Type:** Action without value\
**Description:** Replaces the projectile associated with this event.

**Usage example:** 
```ts
world::set_event_projectile(item("stick"),"name");
```

<h3 id=game_set_event_uery_info>
  <code>world::set_event_uery_info</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Tags To Received Info\
**Type:** Action without value\
**Description:** Adds additional tags to the received debug info that will be copied to the clipboard if the event is not cancelled.\
**Additional info:**\
&nbsp;&nbsp;Additional information only changes.\
**Work_with:**\
&nbsp;&nbsp;Player Receives Block Information Event\
&nbsp;&nbsp;Player Receives Entity Info Event

**Usage example:** 
```ts
world::set_event_uery_info("information");
```

<h3 id=game_set_event_sound>
  <code>world::set_event_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Sound\
**Type:** Action without value\
**Description:** Sets the sound to play associated with this event, replacing the original one.

**Usage example:** 
```ts
world::set_event_sound(sound("entity.zombie.hurt"));
```

<h3 id=game_set_event_source_slot>
  <code>world::set_event_source_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_event_source_slot(1);
```

<h3 id=game_set_event_target_slot>
  <code>world::set_event_target_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_event_target_slot(1);
```

<h3 id=game_set_furnace_cook_time>
  <code>world::set_furnace_cook_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Furnace Cooking Time\
**Type:** Action without value\
**Description:** Sets the cooking time for the oven at the selected location.
**Work_with:**\
&nbsp;&nbsp;None\
&nbsp;&nbsp;None\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_furnace_cook_time(location(0,0,0,0,0),1);
```

<h3 id=game_set_item_in_container_slot>
  <code>world::set_item_in_container_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item In Container Slot\
**Type:** Action without value\
**Description:** Sets an item in the specified container slot at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_item_in_container_slot(location(0,0,0,0,0),item("stick"),1);
```

<h3 id=game_set_lectern_book>
  <code>world::set_lectern_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Book In Lectern\
**Type:** Action without value\
**Description:** Sets a book in the lectern at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_lectern_book(location(0,0,0,0,0),item("stick"),1);
```

<h3 id=game_set_player_head>
  <code>world::set_player_head</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Head\
**Type:** Action without value\
**Description:** Sets the player's head at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_player_head(location(0,0,0,0,0),"name_or_uuid","NAME_OR_UUID");
```

<h3 id=game_set_block_powered>
  <code>world::set_block_powered</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Activate Block\
**Type:** Action without value\
**Description:** Activates a block at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_block_powered(location(0,0,0,0,0),"TRUE");
```

<h3 id=game_set_region>
  <code>world::set_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Blocks In Region\
**Type:** Action without value\
**Description:** Sets the selected block type to the entire selected region.

**Usage example:** 
```ts
world::set_region(item("stone"),location(0,0,0,0,0),location(0,0,0,0,0));
```

<h3 id=game_set_scoreboard_line>
  <code>world::set_scoreboard_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
world::set_scoreboard_line("id","line","display",1,"format_content","BLANK");

#Or from the object

"id".set_scoreboard_line("line","display",1,"format_content","BLANK");
```

<h3 id=game_set_scoreboard_line_display>
  <code>world::set_scoreboard_line_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
world::set_scoreboard_line_display("id","line","display");

#Or from the object

"id".set_scoreboard_line_display("line","display");
```

<h3 id=game_set_scoreboard_line_format>
  <code>world::set_scoreboard_line_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
world::set_scoreboard_line_format("id","line","format_content","BLANK");

#Or from the object

"id".set_scoreboard_line_format("line","format_content","BLANK");
```

<h3 id=game_set_scoreboard_number_format>
  <code>world::set_scoreboard_number_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
world::set_scoreboard_number_format("id","format_content","BLANK");

#Or from the object

"id".set_scoreboard_number_format("format_content","BLANK");
```

<h3 id=game_set_scoreboard_score>
  <code>world::set_scoreboard_score</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Value\
**Type:** Action without value\
**Description:** Sets the value of the specified scoreboard with the displayed text and score.

**Usage example:** 
```ts
world::set_scoreboard_score("id","text",1);
```

<h3 id=game_set_scoreboard_title>
  <code>world::set_scoreboard_title</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Change Scoreboard Title\
**Type:** Action without value\
**Description:** Changes the title of the specified scoreboard.

**Usage example:** 
```ts
world::set_scoreboard_title("id","title");
```

<h3 id=game_set_sculk_shrieker_can_summon>
  <code>world::set_sculk_shrieker_can_summon</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_sculk_shrieker_can_summon(location(0,0,0,0,0),"TRUE");
```

<h3 id=game_set_sculk_shrieker_shrieking>
  <code>world::set_sculk_shrieker_shrieking</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_sculk_shrieker_shrieking(location(0,0,0,0,0),"TRUE");
```

<h3 id=game_set_sculk_shrieker_warning_level>
  <code>world::set_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_sculk_shrieker_warning_level(location(0,0,0,0,0),1);
```

<h3 id=game_set_sign_text>
  <code>world::set_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sign Text\
**Type:** Action without value\
**Description:** Sets the sign text at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_sign_text(location(0,0,0,0,0),"text",1,"FRONT");
```

<h3 id=game_set_sign_text_color>
  <code>world::set_sign_text_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sign Text Color\
**Type:** Action without value\
**Description:** Sets the color of sign text at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_sign_text_color(location(0,0,0,0,0),"FRONT","BLACK","TRUE");
```

<h3 id=game_set_sign_waxed>
  <code>world::set_sign_waxed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sign Waxed\
**Type:** Action without value\
**Description:** Sets the waxedness of the sign at the selected location.
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_sign_waxed(location(0,0,0,0,0),"TRUE");
```

<h3 id=game_set_spawner_entity>
  <code>world::set_spawner_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
world::set_spawner_entity(location(0,0,0,0,0),item("stick"));

#Or from the object

location(0,0,0,0,0).set_spawner_entity(item("stick"));
```

<h3 id=game_set_world_difficulty>
  <code>world::set_world_difficulty</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Difficulty\
**Type:** Action without value\
**Description:** Sets a specific world difficulty.

**Usage example:** 
```ts
world::set_world_difficulty("EASY");
```

<h3 id=game_set_world_simulation_distance>
  <code>world::set_world_simulation_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Simulation Distance\
**Type:** Action without value\
**Description:** Sets the chunk simulation distance for the world.

**Usage example:** 
```ts
world::set_world_simulation_distance(1);
```

<h3 id=game_set_world_time>
  <code>world::set_world_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Time\
**Type:** Action without value\
**Description:** Sets the world time in ticks.

**Usage example:** 
```ts
world::set_world_time(1);
```

<h3 id=game_set_world_weather>
  <code>world::set_world_weather</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Weather\
**Type:** Action without value\
**Description:** Sets the world's weather for a certain amount of time.\
**Additional info:**\
&nbsp;&nbsp;By default, if no duration is specified, the weather will not change.

**Usage example:** 
```ts
world::set_world_weather("CLEAR",1);
```

<h3 id=game_spawn_armor_stand>
  <code>world::spawn_armor_stand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Armor Stand\
**Type:** Action without value\
**Description:** Spawns an armor stand at the specified location.

**Usage example:** 
```ts
world::spawn_armor_stand(item("stick"),item("stick"),item("stick"),item("stick"),item("stick"),item("stick"),"TRUE","TRUE","TRUE","TRUE","TRUE","TRUE",location(0,0,0,0,0),"custom_name");
```

<h3 id=game_spawn_block_display>
  <code>world::spawn_block_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Block Display\
**Type:** Action without value\
**Description:** Spawns a block renderer at the specified location

**Usage example:** 
```ts
world::spawn_block_display(location(0,0,0,0,0),"custom_name",item("stone"));
```

<h3 id=game_spawn_effect_cloud>
  <code>world::spawn_effect_cloud</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Effect Cloud\
**Type:** Action without value\
**Description:** Spawns a cloud of misty potion that infuses the effects of the entities in it.

**Usage example:** 
```ts
world::spawn_effect_cloud(location(0,0,0,0,0),[potion("slow_falling"), potion("slow_falling")],1,2,particle("fire"),"custom_name");
```

<h3 id=game_spawn_end_crystal>
  <code>world::spawn_end_crystal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn End Crystal\
**Type:** Action without value\
**Description:** Spawns an End Crystal at the specified location.

**Usage example:** 
```ts
world::spawn_end_crystal(location(0,0,0,0,0),"custom_name","TRUE");
```

<h3 id=game_spawn_evoker_fangs>
  <code>world::spawn_evoker_fangs</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Evoker Fangs\
**Type:** Action without value\
**Description:** Spawns the Evoker fangs at the specified location.

**Usage example:** 
```ts
world::spawn_evoker_fangs(location(0,0,0,0,0),"custom_name");
```

<h3 id=game_spawn_experience_orb>
  <code>world::spawn_experience_orb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Experience Orb\
**Type:** Action without value\
**Description:** Spawns an Experience Orb at the specified location with the selected options.

**Usage example:** 
```ts
world::spawn_experience_orb(location(0,0,0,0,0),1,"custom_name");
```

<h3 id=game_spawn_eye_of_ender>
  <code>world::spawn_eye_of_ender</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Eye of Ender\
**Type:** Action without value\
**Description:** Spawns an Eye of End at the target location that will move towards the target.

**Usage example:** 
```ts
world::spawn_eye_of_ender(location(0,0,0,0,0),location(0,0,0,0,0),1,"custom_name","DROP");
```

<h3 id=game_spawn_falling_block>
  <code>world::spawn_falling_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Falling Block\
**Type:** Action without value\
**Description:** Spawns a falling block at the specified location.

**Usage example:** 
```ts
world::spawn_falling_block(item("stone"),location(0,0,0,0,0),"name","TRUE");
```

<h3 id=game_spawn_interaction_entity>
  <code>world::spawn_interaction_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Interaction Entity\
**Type:** Action without value\
**Description:** Spawns an interaction entity at the specified location

**Usage example:** 
```ts
world::spawn_interaction_entity(location(0,0,0,0,0),"custom_name",1,2,"TRUE");
```

<h3 id=game_spawn_item>
  <code>world::spawn_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Item\
**Type:** Action without value\
**Description:** Spawns an item at the specified location with the selected options.

**Usage example:** 
```ts
world::spawn_item(item("stick"),location(0,0,0,0,0),"custom_name","TRUE","TRUE","TRUE");
```

<h3 id=game_spawn_item_display>
  <code>world::spawn_item_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Item Display\
**Type:** Action without value\
**Description:** Spawns an item visualizer at the specified location

**Usage example:** 
```ts
world::spawn_item_display(location(0,0,0,0,0),"custom_name",item("stick"));
```

<h3 id=game_spawn_lightning_bolt>
  <code>world::spawn_lightning_bolt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Lightning\
**Type:** Action without value\
**Description:** Spawns lightning at the specified location.

**Usage example:** 
```ts
world::spawn_lightning_bolt(location(0,0,0,0,0));
```

<h3 id=game_spawn_mob>
  <code>world::spawn_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Entity\
**Type:** Action without value\
**Description:** Spawns a mob at the specified location with the selected options.

**Usage example:** 
```ts
world::spawn_mob(item("stick"),location(0,0,0,0,0),1,"custom_name",[potion("slow_falling"), potion("slow_falling")],item("stick"),item("stick"),item("stick"),item("stick"),item("stick"),item("stick"),"TRUE");
```

<h3 id=game_spawn_primed_tnt>
  <code>world::spawn_primed_tnt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Ignited TNT\
**Type:** Action without value\
**Description:** Spawns ignited dynamite at the specified location.

**Usage example:** 
```ts
world::spawn_primed_tnt(location(0,0,0,0,0),1,2,"custom_name",item("stone"));
```

<h3 id=game_spawn_shulker_bullet>
  <code>world::spawn_shulker_bullet</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Shulker Bullet\
**Type:** Action without value\
**Description:** Spawns a Shulker Bullet at the specified location.

**Usage example:** 
```ts
world::spawn_shulker_bullet(location(0,0,0,0,0),"custom_name");
```

<h3 id=game_spawn_text_display>
  <code>world::spawn_text_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Text Display\
**Type:** Action without value\
**Description:** Spawns a text renderer at the specified location

**Usage example:** 
```ts
world::spawn_text_display(location(0,0,0,0,0),"custom_name","SPACES",["displayed_text", "displayed_text"]);
```

<h3 id=game_spawn_vehicle>
  <code>world::spawn_vehicle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Vehicle\
**Type:** Action without value\
**Description:** Spawns a vehicle at the specified location with the selected options.

**Usage example:** 
```ts
world::spawn_vehicle(item("stick"),location(0,0,0,0,0),"custom_name");
```

<h3 id=game_uncancel_event>
  <code>world::uncancel_event</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Uncancel Event\
**Type:** Action without value\
**Description:** Returns the cancellation of the event that triggered this code.

**Usage example:** 
```ts
world::uncancel_event();
```

<h3 id=game_update_block>
  <code>world::update_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
world::update_block(location(0,0,0,0,0));
```

<h3 id=if_game_block_equals>
  <code>world::block_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Block Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a block at a specific location is a specific block type.

**Usage example:** 
```ts
if(world::block_equals(location(0,0,0,0,0),[item("stone"), item("stone")]){
    player::message("Condition is true");
}
```

<h3 id=if_game_block_powered>
  <code>world::block_powered</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Block Powered by Redstone\
**Type:** Action that checks the conditions\
**Description:** Checks if a block at a specific location is powered by redstone.

**Usage example:** 
```ts
if(world::block_powered([location(0,0,0,0,0), location(0,0,0,0,0)],"DIRECT"){
    player::message("Condition is true");
}
```

<h3 id=if_game_chunk_is_loaded>
  <code>world::chunk_is_loaded</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Chunk Is Loaded\
**Type:** Action that checks the conditions\
**Description:** Checks if the location has a chunk loaded

**Usage example:** 
```ts
if(world::chunk_is_loaded(location(0,0,0,0,0)){
    player::message("Condition is true");
}
```

<h3 id=if_game_container_has>
  <code>world::container_has</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Container Has an Item\
**Type:** Action that checks the conditions\
**Description:** Checks if a container at a specific location has certain items in its inventory.

**Usage example:** 
```ts
if(world::container_has(location(0,0,0,0,0),[item("stick"), item("stick")],"ANY","EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_game_container_has_room_for_item>
  <code>world::container_has_room_for_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Container Has Room For Items\
**Type:** Action that checks the conditions\
**Description:** Checks if a container at a specific location has room for items in its inventory.

**Usage example:** 
```ts
if(world::container_has_room_for_item(location(0,0,0,0,0),[item("stick"), item("stick")],"ANY"){
    player::message("Condition is true");
}
```

<h3 id=if_game_damage_cause_equals>
  <code>world::damage_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Event Damage Source Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the event's damage source is equal to the selected one.

**Usage example:** 
```ts
if(world::damage_cause_equals("BLOCK_EXPLOSION"){
    player::message("Condition is true");
}
```

<h3 id=if_game_event_attack_is_critical>
  <code>world::event_attack_is_critical</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Attack Was Critical\
**Type:** Action that checks the conditions\
**Description:** Checks if an attack in an event was a critical attack.

**Usage example:** 
```ts
if(world::event_attack_is_critical(){
    player::message("Condition is true");
}
```

<h3 id=if_game_event_block_equals>
  <code>world::event_block_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Event Block Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the current event's block is equal to certain blocks.

**Usage example:** 
```ts
if(world::event_block_equals([item("stone"), item("stone")],[location(0,0,0,0,0), location(0,0,0,0,0)]){
    player::message("Condition is true");
}
```

<h3 id=if_game_event_is_canceled>
  <code>world::event_is_canceled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Event Cancelled\
**Type:** Action that checks the conditions\
**Description:** Checks if the event has been cancelled.

**Usage example:** 
```ts
if(world::event_is_canceled(){
    player::message("Condition is true");
}
```

<h3 id=if_game_event_item_equals>
  <code>world::event_item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Event Item Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the current event item is equal to certain items.

**Usage example:** 
```ts
if(world::event_item_equals([item("stick"), item("stick")],"EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_game_has_player>
  <code>world::has_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Player Online\
**Type:** Action that checks the conditions\
**Description:** Checks if a certain player is in the game.

**Usage example:** 
```ts
if(world::has_player(["names_or_uuids", "names_or_uuids"]){
    player::message("Condition is true");
}
```

<h3 id=if_game_heal_cause_equals>
  <code>world::heal_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Healing Source Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the heal source is equal to the selected one.

**Usage example:** 
```ts
if(world::heal_cause_equals("CUSTOM"){
    player::message("Condition is true");
}
```

<h3 id=if_game_ignite_cause_equals>
  <code>world::ignite_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ignite Cause Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the fire source is equal to the selected one.

**Usage example:** 
```ts
if(world::ignite_cause_equals("ARROW"){
    player::message("Condition is true");
}
```

<h3 id=if_game_instrument_equals>
  <code>world::instrument_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sound Instrument Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the instrument in the event is equal to the selected one.

**Usage example:** 
```ts
if(world::instrument_equals("BANJO"){
    player::message("Condition is true");
}
```

<h3 id=if_game_sign_contains>
  <code>world::sign_contains</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sign Contains Text\
**Type:** Action that checks the conditions\
**Description:** Checks if a sign at a given location contains the specified text.

**Usage example:** 
```ts
if(world::sign_contains(location(0,0,0,0,0),["texts", "texts"],"ANY","ANY","FIRST"){
    player::message("Condition is true");
}
```

