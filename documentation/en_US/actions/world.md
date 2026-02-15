<h2 id=world>
  <code>world</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

<h3 id=game_block_growth>
  <code>world::block_growth</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Growth Stage\
**Action type:** Action without value\
**Description:** Sets the growth stage for the block at the selected location.

**Usage example:**
```ts
world::block_growth(location(0,0,0,0,0), 1, "PERCENTAGE");

//Or dry by keywords

world::block_growth(location=location(0,0,0,0,0), growth_stage=1, growth_type="PERCENTAGE");
```

**Arguments:**

| ID           | Type                                                                                     | Description    |
|--------------|------------------------------------------------------------------------------------------|----------------|
| location     | Location                                                                                 | Block Location |
| growth_stage | Number                                                                                   | Growth Stage   |
| growth_type  | Marker<br/>**PERCENTAGE** - Growth Percentage<br/>**STAGE_NUMBER** - Growth Stage Number | Growth Type    |

<h3 id=game_bloom_skulk_catalyst>
  <code>world::bloom_skulk_catalyst</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Bloom Skulk Catalyst\
**Action type:** Action without value\
**Description:** Spreads sculk from a sculk catalyst to a location.\
**Work_with:**\
&nbsp;&nbsp;Sculk Catalyst

**Usage example:**
```ts
world::bloom_skulk_catalyst(location(0,0,0,0,0), location(0,0,0,0,0), 1);

//Or dry by keywords

world::bloom_skulk_catalyst(location=location(0,0,0,0,0), bloom_location=location(0,0,0,0,0), charge=1);
```

**Arguments:**

| ID             | Type     | Description                    |
|----------------|----------|--------------------------------|
| location       | Location | Location of the sculk catalyst |
| bloom_location | Location | New location                   |
| charge         | Number   | Speed of spread                |

<h3 id=game_bone_meal_block>
  <code>world::bone_meal_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Bonemeal Block\
**Action type:** Action without value\
**Description:** Bonemeals a block at the selected location.

**Usage example:**
```ts
world::bone_meal_block(location(0,0,0,0,0), 1);

//Or dry by keywords

world::bone_meal_block(location=location(0,0,0,0,0), count=1);
```

**Arguments:**

| ID       | Type     | Description                     |
|----------|----------|---------------------------------|
| location | Location | Block Location                  |
| count    | Number   | Number of Attempts to Fertilize |

<h3 id=game_break_block>
  <code>world::break_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Break Block\
**Action type:** Action without value\
**Description:** Breaks blocks at the specified locations as if it were done by a Survival player with the right tool.

**Usage example:**
```ts
world::break_block([location(0,0,0,0,0), location(0,0,0,0,0)], item("stick"), "FALSE");

//Or dry by keywords

world::break_block(locations=[location(0,0,0,0,0), location(0,0,0,0,0)], tool=item("stick"), drop_exp="FALSE");
```

**Arguments:**

| ID        | Type                                                   | Description                                                  |
|-----------|--------------------------------------------------------|--------------------------------------------------------------|
| locations | Array\[Location\]                                      | Block Locations<br/>The argument supports list decomposition |
| tool      | Item                                                   | Tool                                                         |
| drop_exp  | Marker<br/>**FALSE** - Turn off<br/>**TRUE** - Turn on | Experience drop                                              |

<h3 id=game_cancel_event>
  <code>world::cancel_event</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Cancel Event\
**Action type:** Action without value\
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
**Action type:** Action without value\
**Description:** Removes all items from a container at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Containers

**Usage example:**
```ts
world::clear_container(location(0,0,0,0,0));

//Or dry by keywords

world::clear_container(location=location(0,0,0,0,0));
```

**Arguments:**

| ID       | Type     | Description           |
|----------|----------|-----------------------|
| location | Location | Location of Container |

<h3 id=game_clear_container_items>
  <code>world::clear_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Container Items\
**Action type:** Action without value\
**Description:** Clears the specified items from a container.\
**Work_with:**\
&nbsp;&nbsp;Containers

**Usage example:**
```ts
world::clear_container_items([item("stick"), item("stick")], location(0,0,0,0,0));

//Or dry by keywords

world::clear_container_items(items=[item("stick"), item("stick")], location=location(0,0,0,0,0));
```

**Arguments:**

| ID       | Type          | Description                                        |
|----------|---------------|----------------------------------------------------|
| items    | Array\[Item\] | Items<br/>The argument supports list decomposition |
| location | Location      | Location of container                              |

<h3 id=game_clear_exploded_blocks>
  <code>world::clear_exploded_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Exploded Blocks\
**Action type:** Action without value\
**Description:** Returns exploded blocks to their original position.\
**Work_with:**\
&nbsp;&nbsp;Entity Explode Event\
&nbsp;&nbsp;Block Explode Event

**Usage example:**
```ts
world::clear_exploded_blocks([location(0,0,0,0,0), location(0,0,0,0,0)]);

//Or dry by keywords

world::clear_exploded_blocks(location=[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

**Arguments:**

| ID       | Type              | Description                                                  |
|----------|-------------------|--------------------------------------------------------------|
| location | Array\[Location\] | Block Locations<br/>The argument supports list decomposition |

<h3 id=game_clear_region>
  <code>world::clear_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Region\
**Action type:** Action without value\
**Description:** Removes all blocks in a region.

**Usage example:**
```ts
world::clear_region(location(0,0,0,0,0), location(0,0,0,0,0));

//Or dry by keywords

world::clear_region(pos_1=location(0,0,0,0,0), pos_2=location(0,0,0,0,0));
```

**Arguments:**

| ID    | Type     | Description            |
|-------|----------|------------------------|
| pos_1 | Location | Region Corner          |
| pos_2 | Location | Opposite Region Corner |

<h3 id=game_clear_scoreboard_scores>
  <code>world::clear_scoreboard_scores</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Scoreboard Values\
**Action type:** Action without value\
**Description:** Clears all values of the specified scoreboard.

**Usage example:**
```ts
world::clear_scoreboard_scores("id");

//Or dry by keywords

world::clear_scoreboard_scores(id="id");
```

**Arguments:**

| ID | Type | Description   |
|----|------|---------------|
| id | Text | Scoreboard ID |

<h3 id=game_clone_region>
  <code>world::clone_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clone Region Blocks\
**Action type:** Action without value\
**Description:** Clones a region to the selected location.

**Usage example:**
```ts
world::clone_region(location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "FALSE", "FALSE");

//Or dry by keywords

world::clone_region(pos_1=location(0,0,0,0,0), pos_2=location(0,0,0,0,0), target_pos=location(0,0,0,0,0), paste_pos=location(0,0,0,0,0), ignore_air="FALSE", copy_entity="FALSE");
```

**Arguments:**

| ID          | Type                                                      | Description            |
|-------------|-----------------------------------------------------------|------------------------|
| pos_1       | Location                                                  | Region Corner          |
| pos_2       | Location                                                  | Opposite Region Corner |
| target_pos  | Location                                                  | Copy Location          |
| paste_pos   | Location                                                  | Paste Location         |
| ignore_air  | Marker<br/>**FALSE** - Don't Ignore<br/>**TRUE** - Ignore | Ignore Air             |
| copy_entity | Marker<br/>**FALSE** - Don't clone<br/>**TRUE** - Clone   | Clone Creatures        |

<h3 id=game_create_explosion>
  <code>world::create_explosion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Explosion\
**Action type:** Action without value\
**Description:** Creates an explosion at the specified location.

**Usage example:**
```ts
world::create_explosion(location(0,0,0,0,0), 1, "name_or_uuid", "FALSE", "FALSE");

//Or dry by keywords

world::create_explosion(location=location(0,0,0,0,0), power=1, name_or_uuid="name_or_uuid", fire="FALSE", break_blocks="FALSE");
```

**Arguments:**

| ID           | Type                                             | Description                                                           |
|--------------|--------------------------------------------------|-----------------------------------------------------------------------|
| location     | Location                                         | Creation Location                                                     |
| power        | Number                                           | Explosion Power (0 to 4)                                              |
| name_or_uuid | Text                                             | creative_plus.action.game_create_explosion.argument.name_or_uuid.name |
| fire         | Marker<br/>**FALSE** - False<br/>**TRUE** - True | Create fire                                                           |
| break_blocks | Marker<br/>**FALSE** - False<br/>**TRUE** - True | Break blocks                                                          |

<h3 id=game_create_scoreboard>
  <code>world::create_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Scoreboard\
**Action type:** Action without value\
**Description:** Creates a scoreboard with a specific ID. To display a scoreboard to a player, use the "Show scoreboard" action.

**Usage example:**
```ts
world::create_scoreboard("id", "display_name");

//Or dry by keywords

world::create_scoreboard(id="id", display_name="display_name");
```

**Arguments:**

| ID           | Type | Description   |
|--------------|------|---------------|
| id           | Text | Scoreboard ID |
| display_name | Text | Title         |

<h3 id=game_dummy>
  <code>world::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Action type:** Action without value\
**Description:** ...

**Usage example:**
```ts
world::dummy();
```

<h3 id=game_fill_container>
  <code>world::fill_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Fill Container\
**Action type:** Action without value\
**Description:** Fills a container at the selected location with the specified items.\
**Work_with:**\
&nbsp;&nbsp;Containers

**Usage example:**
```ts
world::fill_container([item("stick"), item("stick")], location(0,0,0,0,0));

//Or dry by keywords

world::fill_container(items=[item("stick"), item("stick")], location=location(0,0,0,0,0));
```

**Arguments:**

| ID       | Type          | Description                                                |
|----------|---------------|------------------------------------------------------------|
| items    | Array\[Item\] | Items to Fill<br/>The argument supports list decomposition |
| location | Location      | Location of Container                                      |

<h3 id=game_generate_tree>
  <code>world::generate_tree</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Generate Tree\
**Action type:** Action without value\
**Description:** Generates a tree at the selected location.

**Usage example:**
```ts
world::generate_tree(location(0,0,0,0,0), "ACACIA");

//Or dry by keywords

world::generate_tree(location=location(0,0,0,0,0), tree_type="ACACIA");
```

**Arguments:**

| ID        | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description   |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| location  | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Tree Location |
| tree_type | Marker<br/>**ACACIA** - Acacia<br/>**AZALEA** - Azalea<br/>**BIG_TREE** - Big Tree<br/>**BIRCH** - Common Birch<br/>**BROWN_MUSHROOM** - Brown Mushroom<br/>**CHERRY** - Cherry<br/>**CHORUS_PLANT** - Chorus Tree<br/>**COCOA_TREE** - Cocoa Bean Jungle Tree<br/>**CRIMSON_FUNGUS** - Crimson Mushroom<br/>**DARK_OAK** - Dark Oak<br/>**JUNGLE** - Jungle Tree<br/>**JUNGLE_BUSH** - Jungle Bush<br/>**MANGROVE** - Mangrove Tree<br/>**MEGA_PINE** - Mega Pine<br/>**MEGA_REDWOOD** - Great Sequoia<br/>**REDWOOD** - Regular Spruce<br/>**RED_MUSHROOM** - Red Mushroom<br/>**SMALL_JUNGLE** - Small Jungle Tree<br/>**SWAMP** - Swamp Tree<br/>**TALL_BIRCH** - Tall Birch<br/>**TALL_MANGROVE** - Tall Mangrove Tree<br/>**TALL_REDWOOD** - Tall Spruce<br/>**TREE** - Regular Tree<br/>**WARPED_FUNGUS** - Warped Mushroom | Tree Type     |

<h3 id=game_hide_event_message>
  <code>world::hide_event_message</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Hide Event Message\
**Action type:** Action without value\
**Description:** Removes the message from the event that triggered this code.\
**Work_with:**\
&nbsp;&nbsp;Player Join Event\
&nbsp;&nbsp;Player Quit Event\
&nbsp;&nbsp;Player Death Event

**Usage example:**
```ts
world::hide_event_message("FALSE");

//Or dry by keywords

world::hide_event_message(hide="FALSE");
```

**Arguments:**

| ID   | Type                                           | Description  |
|------|------------------------------------------------|--------------|
| hide | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes | Hide Message |

<h3 id=game_launch_firework>
  <code>world::launch_firework</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Firework\
**Action type:** Action without value\
**Description:** Launches firework at the specified location.

**Usage example:**
```ts
world::launch_firework(item("stick"), location(0,0,0,0,0), "DIRECTIONAL", "FALSE");

//Or dry by keywords

world::launch_firework(firework=item("stick"), location=location(0,0,0,0,0), movement="DIRECTIONAL", instant="FALSE");
```

**Arguments:**

| ID       | Type                                                               | Description        |
|----------|--------------------------------------------------------------------|--------------------|
| firework | Item                                                               | Firework to Create |
| location | Location                                                           | Creation Location  |
| movement | Marker<br/>**DIRECTIONAL** - Directional<br/>**UPWARDS** - Upwards | Move               |
| instant  | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes                     | Instant Explosion  |

<h3 id=game_launch_projectile>
  <code>world::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Projectile\
**Action type:** Action without value\
**Description:** Launches a projectile at the specified location.

**Usage example:**
```ts
world::launch_projectile(item("stick"), location(0,0,0,0,0), 1, 2, "custom_name", particle("fire"));

//Or dry by keywords

world::launch_projectile(projectile=item("stick"), location=location(0,0,0,0,0), speed=1, inaccuracy=2, custom_name="custom_name", trail=particle("fire"));
```

**Arguments:**

| ID          | Type            | Description                                                      |
|-------------|-----------------|------------------------------------------------------------------|
| projectile  | Item            | Projectile to Launch                                             |
| location    | Location        | Launch Location                                                  |
| speed       | Number          | Projectile Speed                                                 |
| inaccuracy  | Number          | Projectile deflection (0 to keep the projectile flying straight) |
| custom_name | Text            | Projectile Name                                                  |
| trail       | Particle Effect | The trail the projectile will leave                              |

<h3 id=game_random_tick_block>
  <code>world::random_tick_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Random Tick Block\
**Action type:** Action without value\
**Description:** Updates a block (random tick) at the selected location.

**Usage example:**
```ts
world::random_tick_block(location(0,0,0,0,0), 1);

//Or dry by keywords

world::random_tick_block(location=location(0,0,0,0,0), times=1);
```

**Arguments:**

| ID       | Type     | Description       |
|----------|----------|-------------------|
| location | Location | Location          |
| times    | Number   | Number of Updates |

<h3 id=game_remove_container_items>
  <code>world::remove_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Items From Container\
**Action type:** Action without value\
**Description:** Removes the specified items from a container at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Containers

**Usage example:**
```ts
world::remove_container_items([item("stick"), item("stick")], location(0,0,0,0,0));

//Or dry by keywords

world::remove_container_items(items=[item("stick"), item("stick")], location=location(0,0,0,0,0));
```

**Arguments:**

| ID       | Type          | Description                                        |
|----------|---------------|----------------------------------------------------|
| items    | Array\[Item\] | Items<br/>The argument supports list decomposition |
| location | Location      | Location of Container                              |

<h3 id=game_remove_scoreboard>
  <code>world::remove_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Scoreboard\
**Action type:** Action without value\
**Description:** Removes the specified scoreboard.

**Usage example:**
```ts
world::remove_scoreboard("id");

//Or dry by keywords

world::remove_scoreboard(id="id");
```

**Arguments:**

| ID | Type | Description   |
|----|------|---------------|
| id | Text | Scoreboard ID |

<h3 id=game_remove_scoreboard_score_by_name>
  <code>world::remove_scoreboard_score_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Scoreboard Value By Text\
**Action type:** Action without value\
**Description:** Removes the value of the specified scoreboard by display text.

**Usage example:**
```ts
world::remove_scoreboard_score_by_name("id", "text");

//Or dry by keywords

world::remove_scoreboard_score_by_name(id="id", text="text");
```

**Arguments:**

| ID   | Type | Description          |
|------|------|----------------------|
| id   | Text | Scoreboard ID        |
| text | Text | Value text to remove |

<h3 id=game_remove_scoreboard_score_by_score>
  <code>world::remove_scoreboard_score_by_score</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Scoreboard Value By Score\
**Action type:** Action without value\
**Description:** Removes the value of the specified scoreboard by score.

**Usage example:**
```ts
world::remove_scoreboard_score_by_score("id", 1);

//Or dry by keywords

world::remove_scoreboard_score_by_score(id="id", score=1);
```

**Arguments:**

| ID    | Type   | Description              |
|-------|--------|--------------------------|
| id    | Text   | Scoreboard ID            |
| score | Number | Score of value to remove |

<h3 id=game_remove_tile_block_custom_tag>
  <code>world::remove_tile_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_remove_tile_block_custom_tag.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_remove_tile_block_custom_tag.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_remove_tile_block_custom_tag.work_with.tile_state_block

**Usage example:**
```ts
world::remove_tile_block_custom_tag(location(0,0,0,0,0), "tag_name");

//Or dry by keywords

world::remove_tile_block_custom_tag(location=location(0,0,0,0,0), tag_name="tag_name");
```

**Arguments:**

| ID       | Type     | Description                                                                   |
|----------|----------|-------------------------------------------------------------------------------|
| location | Location | creative_plus.action.game_remove_tile_block_custom_tag.argument.location.name |
| tag_name | Text     | creative_plus.action.game_remove_tile_block_custom_tag.argument.tag_name.name |

<h3 id=game_replace_blocks_in_region>
  <code>world::replace_blocks_in_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Blocks in Region\
**Action type:** Action without value\
**Description:** Replaces blocks with others in the selected region.

**Usage example:**
```ts
world::replace_blocks_in_region(["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], location(0,0,0,0,0), location(0,0,0,0,0), "minecraft:oak_log[axis=x]");

//Or dry by keywords

world::replace_blocks_in_region(old_block=["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], pos_1=location(0,0,0,0,0), pos_2=location(0,0,0,0,0), new_block="minecraft:oak_log[axis=x]");
```

**Arguments:**

| ID        | Type           | Description                                                    |
|-----------|----------------|----------------------------------------------------------------|
| old_block | Array\[Block\] | Blocks to Replace<br/>The argument supports list decomposition |
| pos_1     | Location       | Region Corner                                                  |
| pos_2     | Location       | Opposite Corner of Region                                      |
| new_block | Block          | New Block                                                      |

<h3 id=game_replace_container_items>
  <code>world::replace_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Items in Container\
**Action type:** Action without value\
**Description:** Replaces the specified items in a container at the selected location with a specific item.\
**Work_with:**\
&nbsp;&nbsp;Containers

**Usage example:**
```ts
world::replace_container_items([item("stick"), item("stick")], location(0,0,0,0,0), item("stick"), 1);

//Or dry by keywords

world::replace_container_items(items=[item("stick"), item("stick")], location=location(0,0,0,0,0), replace=item("stick"), count=1);
```

**Arguments:**

| ID       | Type          | Description                                                    |
|----------|---------------|----------------------------------------------------------------|
| items    | Array\[Item\] | Replaceable Items<br/>The argument supports list decomposition |
| location | Location      | Location of container                                          |
| replace  | Item          | Replace Item                                                   |
| count    | Number        | Number of Items to Replace                                     |

<h3 id=game_send_web_request>
  <code>world::send_web_request</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Web Request\
**Action type:** Action without value\
**Description:** Sends a web request with the selected method and body to the selected URL.

**Usage example:**
```ts
world::send_web_request("url", "content_body", {"headers":`headers`}, "DELETE", "APPLICATION_JSON");

//Or dry by keywords

world::send_web_request(url="url", content_body="content_body", headers={"headers":`headers`}, request_type="DELETE", content_type="APPLICATION_JSON");
```

**Arguments:**

| ID           | Type                                                                                                                                                                                                        | Description                                                      |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| url          | Text                                                                                                                                                                                                        | URL                                                              |
| content_body | Text                                                                                                                                                                                                        | Request Body                                                     |
| headers      | Dictionary                                                                                                                                                                                                  | creative_plus.action.game_send_web_request.argument.headers.name |
| request_type | Marker<br/>**DELETE** - DELETE<br/>**GET** - GET<br/>**HEAD** - HEAD<br/>**PATCH** - creative_plus.action.game_send_web_request.argument.request_type.enum.patch.name<br/>**POST** - POST<br/>**PUT** - PUT | Request Type                                                     |
| content_type | Marker<br/>**APPLICATION_JSON** - JSON (application/json)<br/>**TEXT_PLAIN** - Plain Text (text/plain)                                                                                                      | Media Request Type                                               |

<h3 id=game_set_age>
  <code>world::set_age</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Age\
**Action type:** Action without value\
**Description:** Sets the age of the block at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Ageable blocks

**Usage example:**
```ts
world::set_age(location(0,0,0,0,0), 1);

//Or dry by keywords

world::set_age(location=location(0,0,0,0,0), tick=1);
```

**Arguments:**

| ID       | Type     | Description    |
|----------|----------|----------------|
| location | Location | Block Location |
| tick     | Number   | Ticks          |

<h3 id=game_set_block>
  <code>world::set_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block\
**Action type:** Action without value\
**Description:** Sets the selected block type on selected locations.

**Usage example:**
```ts
world::set_block([location(0,0,0,0,0), location(0,0,0,0,0)], "minecraft:oak_log[axis=x]", "FALSE");

//Or dry by keywords

world::set_block(locations=[location(0,0,0,0,0), location(0,0,0,0,0)], block="minecraft:oak_log[axis=x]", update_blocks="FALSE");
```

**Arguments:**

| ID            | Type                                                      | Description                                                      |
|---------------|-----------------------------------------------------------|------------------------------------------------------------------|
| locations     | Array\[Location\]                                         | Block Set Locations<br/>The argument supports list decomposition |
| block         | Block                                                     | Block                                                            |
| update_blocks | Marker<br/>**FALSE** - Don't update<br/>**TRUE** - Update | Update adjacent blocks                                           |

<h3 id=game_set_block_analogue_power>
  <code>world::set_block_analogue_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Redstone Signal Strength\
**Action type:** Action without value\
**Description:** Sets the selected location to a specific signal strength.\
**Work_with:**\
&nbsp;&nbsp;Powerable blocks

**Usage example:**
```ts
world::set_block_analogue_power(location(0,0,0,0,0), 1);

//Or dry by keywords

world::set_block_analogue_power(location=location(0,0,0,0,0), power_level=1);
```

**Arguments:**

| ID          | Type     | Description         |
|-------------|----------|---------------------|
| location    | Location | Block Location      |
| power_level | Number   | New Signal Strength |

<h3 id=game_set_block_data>
  <code>world::set_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Data\
**Action type:** Action without value\
**Description:** Sets the parameters of a block at a specific location.

**Usage example:**
```ts
world::set_block_data(location(0,0,0,0,0), "block_data");

//Or dry by keywords

world::set_block_data(location=location(0,0,0,0,0), block_data="block_data");
```

**Arguments:**

| ID         | Type     | Description       |
|------------|----------|-------------------|
| location   | Location | Block Location    |
| block_data | Text     | New Block Options |

<h3 id=game_set_block_drops_enabled>
  <code>world::set_block_drops_enabled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Drops\
**Action type:** Action without value\
**Description:** Sets a rule in the world to drop blocks when they are broken.

**Usage example:**
```ts
world::set_block_drops_enabled("FALSE");

//Or dry by keywords

world::set_block_drops_enabled(enable="FALSE");
```

**Arguments:**

| ID     | Type                                                   | Description |
|--------|--------------------------------------------------------|-------------|
| enable | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Drop Blocks |

<h3 id=game_set_block_powered>
  <code>world::set_block_powered</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Activate Block\
**Action type:** Action without value\
**Description:** Activates a block at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Powerable blocks

**Usage example:**
```ts
world::set_block_powered(location(0,0,0,0,0), "FALSE");

//Or dry by keywords

world::set_block_powered(location=location(0,0,0,0,0), powered="FALSE");
```

**Arguments:**

| ID       | Type                                                 | Description    |
|----------|------------------------------------------------------|----------------|
| location | Location                                             | Block Location |
| powered  | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Activation     |

<h3 id=game_set_block_single_data>
  <code>world::set_block_single_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Single Data\
**Action type:** Action without value\
**Description:** Sets the given parameter to a block at the location to a given value.

**Usage example:**
```ts
world::set_block_single_data(location(0,0,0,0,0), "data", "value");

//Or dry by keywords

world::set_block_single_data(location=location(0,0,0,0,0), data="data", value="value");
```

**Arguments:**

| ID       | Type     | Description       |
|----------|----------|-------------------|
| location | Location | Block location    |
| data     | Text     | Varying parameter |
| value    | Text     | New value         |

<h3 id=game_set_brushable_block_item>
  <code>world::set_brushable_block_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item in Suspicious Block\
**Action type:** Action without value\
**Description:** Sets an item into a suspicious block (sand, gravel) at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Suspicious Sand\
&nbsp;&nbsp;Suspicious Gravel

**Usage example:**
```ts
world::set_brushable_block_item(location(0,0,0,0,0), item("stick"));

//Or dry by keywords

world::set_brushable_block_item(location=location(0,0,0,0,0), item=item("stick"));
```

**Arguments:**

| ID       | Type     | Description    |
|----------|----------|----------------|
| location | Location | Block Location |
| item     | Item     | Item           |

<h3 id=game_set_campfire_item>
  <code>world::set_campfire_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Campfire Item\
**Action type:** Action without value\
**Description:** Sets an item to a campfire at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Campfires

**Usage example:**
```ts
world::set_campfire_item(location(0,0,0,0,0), item("stick"), 1, "FIRST");

//Or dry by keywords

world::set_campfire_item(location=location(0,0,0,0,0), item=item("stick"), cooking_time=1, slot="FIRST");
```

**Arguments:**

| ID           | Type                                                                                               | Description       |
|--------------|----------------------------------------------------------------------------------------------------|-------------------|
| location     | Location                                                                                           | Campfire Location |
| item         | Item                                                                                               | Item              |
| cooking_time | Number                                                                                             | Cooking Time      |
| slot         | Marker<br/>**FIRST** - First<br/>**FOURTH** - Fourth<br/>**SECOND** - Second<br/>**THIRD** - Third | Slot              |

<h3 id=game_set_container>
  <code>world::set_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Items In Container\
**Action type:** Action without value\
**Description:** Sets the specified items into a container at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Containers

**Usage example:**
```ts
world::set_container([item("stick"), item("stick")], [location(0,0,0,0,0), location(0,0,0,0,0)]);

//Or dry by keywords

world::set_container(items=[item("stick"), item("stick")], location=[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

**Arguments:**

| ID       | Type              | Description                                                        |
|----------|-------------------|--------------------------------------------------------------------|
| items    | Array\[Item\]     | Items to Set<br/>The argument supports list decomposition          |
| location | Array\[Location\] | Location of Container<br/>The argument supports list decomposition |

<h3 id=game_set_container_lock>
  <code>world::set_container_lock</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Container Key\
**Action type:** Action without value\
**Description:** Sets a specific key to a container at the selected location.\
**Additional info:**\
&nbsp;&nbsp;Any item with a specific name can serve as a container key.

**Usage example:**
```ts
world::set_container_lock(location(0,0,0,0,0), "container_key");

//Or dry by keywords

world::set_container_lock(location=location(0,0,0,0,0), container_key="container_key");
```

**Arguments:**

| ID            | Type     | Description           |
|---------------|----------|-----------------------|
| location      | Location | Location of Container |
| container_key | Text     | Container Key Name    |

<h3 id=game_set_container_name>
  <code>world::set_container_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Container Name\
**Action type:** Action without value\
**Description:** Sets the name of the container at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Containers

**Usage example:**
```ts
world::set_container_name(location(0,0,0,0,0), "name");

//Or dry by keywords

world::set_container_name(location=location(0,0,0,0,0), name="name");
```

**Arguments:**

| ID       | Type     | Description           |
|----------|----------|-----------------------|
| location | Location | Location of container |
| name     | Text     | Container Name        |

<h3 id=game_set_copper_golem_statue_pose>
  <code>world::set_copper_golem_statue_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_copper_golem_statue_pose.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_copper_golem_statue_pose.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_copper_golem_statue_pose.work_with.copper_golem_statue

**Usage example:**
```ts
world::set_copper_golem_statue_pose(location(0,0,0,0,0), "STANDING");

//Or dry by keywords

world::set_copper_golem_statue_pose(location=location(0,0,0,0,0), pose="STANDING");
```

**Arguments:**

| ID       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                   |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| location | Location                                                                                                                                                                                                                                                                                                                                                                                                                               | creative_plus.action.game_set_copper_golem_statue_pose.argument.location.name |
| pose     | Marker<br/>**STANDING** - creative_plus.action.game_set_copper_golem_statue_pose.argument.pose.enum.standing.name<br/>**SITTING** - creative_plus.action.game_set_copper_golem_statue_pose.argument.pose.enum.sitting.name<br/>**RUNNING** - creative_plus.action.game_set_copper_golem_statue_pose.argument.pose.enum.running.name<br/>**STAR** - creative_plus.action.game_set_copper_golem_statue_pose.argument.pose.enum.star.name | creative_plus.action.game_set_copper_golem_statue_pose.argument.pose.name     |

<h3 id=game_set_creaking_heart_natural>
  <code>world::set_creaking_heart_natural</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_creaking_heart_natural.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_creaking_heart_natural.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.game_set_creaking_heart_natural.additional_information.natural_dropping_experience\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_creaking_heart_natural.work_with.creaking_heart

**Usage example:**
```ts
world::set_creaking_heart_natural(location(0,0,0,0,0), "TRUE");

//Or dry by keywords

world::set_creaking_heart_natural(location=location(0,0,0,0,0), natural="TRUE");
```

**Arguments:**

| ID       | Type                                                                                                                                                                                                             | Description                                                                 |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| location | Location                                                                                                                                                                                                         | creative_plus.action.game_set_creaking_heart_natural.argument.location.name |
| natural  | Marker<br/>**TRUE** - creative_plus.action.game_set_creaking_heart_natural.argument.natural.enum.true.name<br/>**FALSE** - creative_plus.action.game_set_creaking_heart_natural.argument.natural.enum.false.name | creative_plus.action.game_set_creaking_heart_natural.argument.natural.name  |

<h3 id=game_set_creaking_heart_state>
  <code>world::set_creaking_heart_state</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_creaking_heart_state.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_creaking_heart_state.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_creaking_heart_state.work_with.creaking_heart

**Usage example:**
```ts
world::set_creaking_heart_state(location(0,0,0,0,0), "UPROOTED");

//Or dry by keywords

world::set_creaking_heart_state(location=location(0,0,0,0,0), heart_state="UPROOTED");
```

**Arguments:**

| ID          | Type                                                                                                                                                                                                                                                                                                                                     | Description                                                                  |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| location    | Location                                                                                                                                                                                                                                                                                                                                 | creative_plus.action.game_set_creaking_heart_state.argument.location.name    |
| heart_state | Marker<br/>**UPROOTED** - creative_plus.action.game_set_creaking_heart_state.argument.heart_state.enum.uprooted.name<br/>**DORMANT** - creative_plus.action.game_set_creaking_heart_state.argument.heart_state.enum.dormant.name<br/>**AWAKE** - creative_plus.action.game_set_creaking_heart_state.argument.heart_state.enum.awake.name | creative_plus.action.game_set_creaking_heart_state.argument.heart_state.name |

<h3 id=game_set_decorate_pot_sherd>
  <code>world::set_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Decorate Pot Sherd\
**Action type:** Action without value\
**Description:** Sets the specified shard to the selected side of the vase at the specified location.\
**Work_with:**\
&nbsp;&nbsp;Decorated Pots

**Usage example:**
```ts
world::set_decorate_pot_sherd(location(0,0,0,0,0), item("stick"), "BACK");

//Or dry by keywords

world::set_decorate_pot_sherd(location=location(0,0,0,0,0), item=item("stick"), side="BACK");
```

**Arguments:**

| ID       | Type                                                                                                           | Description            |
|----------|----------------------------------------------------------------------------------------------------------------|------------------------|
| location | Location                                                                                                       | Decorated pot location |
| item     | Item                                                                                                           | Sherd item             |
| side     | Marker<br/>**BACK** - Back side<br/>**FRONT** - Front side<br/>**LEFT** - Left side<br/>**RIGHT** - Right side | Decorated pot side     |

<h3 id=game_set_dried_ghast_hydration>
  <code>world::set_dried_ghast_hydration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_dried_ghast_hydration.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_dried_ghast_hydration.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_dried_ghast_hydration.work_with.dried_ghast

**Usage example:**
```ts
world::set_dried_ghast_hydration(location(0,0,0,0,0), 1);

//Or dry by keywords

world::set_dried_ghast_hydration(location=location(0,0,0,0,0), hydration=1);
```

**Arguments:**

| ID        | Type     | Description                                                                 |
|-----------|----------|-----------------------------------------------------------------------------|
| location  | Location | creative_plus.action.game_set_dried_ghast_hydration.argument.location.name  |
| hydration | Number   | creative_plus.action.game_set_dried_ghast_hydration.argument.hydration.name |

<h3 id=game_set_event_anvil_repair_cost>
  <code>world::set_event_anvil_repair_cost</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_event_anvil_repair_cost.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_event_anvil_repair_cost.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_event_anvil_repair_cost.work_with.player_prepare_anvil

**Usage example:**
```ts
world::set_event_anvil_repair_cost(1, "REPAIR_COST", "TRUE");

//Or dry by keywords

world::set_event_anvil_repair_cost(repair_cost=1, repair_cost_type="REPAIR_COST", bypass_cost="TRUE");
```

**Arguments:**

| ID               | Type                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| repair_cost      | Number                                                                                                                                                                                                                                                                                                                                                                                                                           | creative_plus.action.game_set_event_anvil_repair_cost.argument.repair_cost.name      |
| repair_cost_type | Marker<br/>**REPAIR_COST** - creative_plus.action.game_set_event_anvil_repair_cost.argument.repair_cost_type.enum.repair_cost.name<br/>**REPAIR_ITEM_COUNT_COST** - creative_plus.action.game_set_event_anvil_repair_cost.argument.repair_cost_type.enum.repair_item_count_cost.name<br/>**MAXIMUM_REPAIR_COST** - creative_plus.action.game_set_event_anvil_repair_cost.argument.repair_cost_type.enum.maximum_repair_cost.name | creative_plus.action.game_set_event_anvil_repair_cost.argument.repair_cost_type.name |
| bypass_cost      | Marker<br/>**TRUE** - creative_plus.action.game_set_event_anvil_repair_cost.argument.bypass_cost.enum.true.name<br/>**FALSE** - creative_plus.action.game_set_event_anvil_repair_cost.argument.bypass_cost.enum.false.name                                                                                                                                                                                                       | creative_plus.action.game_set_event_anvil_repair_cost.argument.bypass_cost.name      |

<h3 id=game_set_event_combust_duration>
  <code>world::set_event_combust_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_event_combust_duration.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_event_combust_duration.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_event_combust_duration.work_with.player_combust_event\
&nbsp;&nbsp;creative_plus.action.game_set_event_combust_duration.work_with.entity_combust_event

**Usage example:**
```ts
world::set_event_combust_duration(1);

//Or dry by keywords

world::set_event_combust_duration(duration=1);
```

**Arguments:**

| ID       | Type   | Description                                                                 |
|----------|--------|-----------------------------------------------------------------------------|
| duration | Number | creative_plus.action.game_set_event_combust_duration.argument.duration.name |

<h3 id=game_set_event_damage>
  <code>world::set_event_damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Damage\
**Action type:** Action without value\
**Description:** Sets the damage associated with this event.\
**Work_with:**\
&nbsp;&nbsp;Damage Events

**Usage example:**
```ts
world::set_event_damage(1);

//Or dry by keywords

world::set_event_damage(damage=1);
```

**Arguments:**

| ID     | Type   | Description   |
|--------|--------|---------------|
| damage | Number | Damage Amount |

<h3 id=game_set_event_death_screen_message>
  <code>world::set_event_death_screen_message</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_event_death_screen_message.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_event_death_screen_message.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.game_set_event_death_screen_message.additional_information.reset_to_default_when_empty\
&nbsp;&nbsp;creative_plus.action.game_set_event_death_screen_message.additional_information.caps_at_256_characters\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_event_death_screen_message.work_with.player_death_event

**Usage example:**
```ts
world::set_event_death_screen_message("message");

//Or dry by keywords

world::set_event_death_screen_message(message="message");
```

**Arguments:**

| ID      | Type | Description                                                                    |
|---------|------|--------------------------------------------------------------------------------|
| message | Text | creative_plus.action.game_set_event_death_screen_message.argument.message.name |

<h3 id=game_set_event_enchantment_offers>
  <code>world::set_event_enchantment_offers</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_event_enchantment_offers.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_event_enchantment_offers.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_event_enchantment_offers.work_with.player_prepare_item_enchant

**Usage example:**
```ts
world::set_event_enchantment_offers(["enchantments", "enchantments"], ["levels", "levels"], ["costs", "costs"]);

//Or dry by keywords

world::set_event_enchantment_offers(enchantments=["enchantments", "enchantments"], levels=["levels", "levels"], costs=["costs", "costs"]);
```

**Arguments:**

| ID           | Type          | Description                                                                                                                    |
|--------------|---------------|--------------------------------------------------------------------------------------------------------------------------------|
| enchantments | Array\[Text\] | creative_plus.action.game_set_event_enchantment_offers.argument.enchantments.name<br/>The argument supports list decomposition |
| levels       | Array\[Text\] | creative_plus.action.game_set_event_enchantment_offers.argument.levels.name<br/>The argument supports list decomposition       |
| costs        | Array\[Text\] | creative_plus.action.game_set_event_enchantment_offers.argument.costs.name<br/>The argument supports list decomposition        |

<h3 id=game_set_event_exhaustion>
  <code>world::set_event_exhaustion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Exhaustion\
**Action type:** Action without value\
**Description:** Sets the exhaustion level.\
**Work_with:**\
&nbsp;&nbsp;Player Exhaustion

**Usage example:**
```ts
world::set_event_exhaustion(1);

//Or dry by keywords

world::set_event_exhaustion(exhaustion=1);
```

**Arguments:**

| ID         | Type   | Description      |
|------------|--------|------------------|
| exhaustion | Number | Exhaustion level |

<h3 id=game_set_event_experience>
  <code>world::set_event_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Experience\
**Action type:** Action without value\
**Description:** Sets the experience value associated with this event.\
**Work_with:**\
&nbsp;&nbsp;Fishing Event\
&nbsp;&nbsp;Experience Gain Event\
&nbsp;&nbsp;Kill Events

**Usage example:**
```ts
world::set_event_experience(1);

//Or dry by keywords

world::set_event_experience(experience=1);
```

**Arguments:**

| ID         | Type   | Description          |
|------------|--------|----------------------|
| experience | Number | Amount of Experience |

<h3 id=game_set_event_gamemode>
  <code>world::set_event_gamemode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_event_gamemode.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_event_gamemode.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_event_gamemode.work_with.player_ask_gamemode_change_event

**Usage example:**
```ts
world::set_event_gamemode("CREATIVE");

//Or dry by keywords

world::set_event_gamemode(gamemode="CREATIVE");
```

**Arguments:**

| ID       | Type                                                                                                                                                                                                                                                                                                                                                                                                                           | Description                                                         |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| gamemode | Marker<br/>**CREATIVE** - creative_plus.action.game_set_event_gamemode.argument.gamemode.enum.creative.name<br/>**SURVIVAL** - creative_plus.action.game_set_event_gamemode.argument.gamemode.enum.survival.name<br/>**ADVENTURE** - creative_plus.action.game_set_event_gamemode.argument.gamemode.enum.adventure.name<br/>**SPECTATOR** - creative_plus.action.game_set_event_gamemode.argument.gamemode.enum.spectator.name | creative_plus.action.game_set_event_gamemode.argument.gamemode.name |

<h3 id=game_set_event_heal>
  <code>world::set_event_heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Heal\
**Action type:** Action without value\
**Description:** Sets the heal value associated with this event.\
**Work_with:**\
&nbsp;&nbsp;Player Heal Event\
&nbsp;&nbsp;Entity Heal Event

**Usage example:**
```ts
world::set_event_heal(1);

//Or dry by keywords

world::set_event_heal(heal=1);
```

**Arguments:**

| ID   | Type   | Description |
|------|--------|-------------|
| heal | Number | Heal Amount |

<h3 id=game_set_event_item>
  <code>world::set_event_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Item\
**Action type:** Action without value\
**Description:** Sets the item associated with this event.\
**Work_with:**\
&nbsp;&nbsp;Dispenser equips armor event\
&nbsp;&nbsp;Block Dispense Item Event\
&nbsp;&nbsp;Player Consumes Item Event\
&nbsp;&nbsp;Player Craft Item Event\
&nbsp;&nbsp;Player Drops Item Event\
&nbsp;&nbsp;Entity Drops Item Event\
&nbsp;&nbsp;Entity Pickup Event\
&nbsp;&nbsp;Player clicks in own inventory event\
&nbsp;&nbsp;Player Clicks Inventory Event\
&nbsp;&nbsp;Player Edit Book Event\
&nbsp;&nbsp;Player Picked Up Projectile Event\
&nbsp;&nbsp;Witch Throws Potion Event\
&nbsp;&nbsp;creative_plus.action.game_set_event_item.work_with.player_prepare_result

**Usage example:**
```ts
world::set_event_item(item("stick"));

//Or dry by keywords

world::set_event_item(item=item("stick"));
```

**Arguments:**

| ID   | Type | Description    |
|------|------|----------------|
| item | Item | New Event Item |

<h3 id=game_set_event_item_cooldown>
  <code>world::set_event_item_cooldown</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_event_item_cooldown.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_event_item_cooldown.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_event_item_cooldown.work_with.player_item_cooldown\
&nbsp;&nbsp;creative_plus.action.game_set_event_item_cooldown.work_with.player_item_group_cooldown

**Usage example:**
```ts
world::set_event_item_cooldown(1);

//Or dry by keywords

world::set_event_item_cooldown(cooldown=1);
```

**Arguments:**

| ID       | Type   | Description                                                              |
|----------|--------|--------------------------------------------------------------------------|
| cooldown | Number | creative_plus.action.game_set_event_item_cooldown.argument.cooldown.name |

<h3 id=game_set_event_items>
  <code>world::set_event_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Items\
**Action type:** Action without value\
**Description:** Sets the items related to the event.\
**Work_with:**\
&nbsp;&nbsp;Player Pick Item

**Usage example:**
```ts
world::set_event_items([item("stick"), item("stick")]);

//Or dry by keywords

world::set_event_items(items=[item("stick"), item("stick")]);
```

**Arguments:**

| ID    | Type          | Description                                               |
|-------|---------------|-----------------------------------------------------------|
| items | Array\[Item\] | Items to set<br/>The argument supports list decomposition |

<h3 id=game_set_event_knockback_vector>
  <code>world::set_event_knockback_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_event_knockback_vector.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_event_knockback_vector.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_event_knockback_vector.work_with.player_knockback\
&nbsp;&nbsp;creative_plus.action.game_set_event_knockback_vector.work_with.entity_knockback

**Usage example:**
```ts
world::set_event_knockback_vector(vector(0,0,0));

//Or dry by keywords

world::set_event_knockback_vector(knockback=vector(0,0,0));
```

**Arguments:**

| ID        | Type   | Description                                                                  |
|-----------|--------|------------------------------------------------------------------------------|
| knockback | Vector | creative_plus.action.game_set_event_knockback_vector.argument.knockback.name |

<h3 id=game_set_event_move_allowed>
  <code>world::set_event_move_allowed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Allow Movement\
**Action type:** Action without value\
**Description:** Allows movement if it fails.\
**Work_with:**\
&nbsp;&nbsp;Player Failed to Move Event

**Usage example:**
```ts
world::set_event_move_allowed("FALSE");

//Or dry by keywords

world::set_event_move_allowed(allowed="FALSE");
```

**Arguments:**

| ID      | Type                                         | Description    |
|---------|----------------------------------------------|----------------|
| allowed | Marker<br/>**FALSE** - No<br/>**TRUE** - Yes | Allow Movement |

<h3 id=game_set_event_projectile>
  <code>world::set_event_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Projectile\
**Action type:** Action without value\
**Description:** Replaces the projectile associated with this event.

**Usage example:**
```ts
world::set_event_projectile(item("stick"), "name");

//Or dry by keywords

world::set_event_projectile(projectile=item("stick"), name="name");
```

**Arguments:**

| ID         | Type | Description             |
|------------|------|-------------------------|
| projectile | Item | Projectile              |
| name       | Text | Projectile Display Name |

<h3 id=game_set_event_sound>
  <code>world::set_event_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Sound\
**Action type:** Action without value\
**Description:** Sets the sound to play associated with this event, replacing the original one.

**Usage example:**
```ts
world::set_event_sound(sound("entity.zombie.hurt"));

//Or dry by keywords

world::set_event_sound(sound=sound("entity.zombie.hurt"));
```

**Arguments:**

| ID    | Type  | Description    |
|-------|-------|----------------|
| sound | Sound | Playable sound |

<h3 id=game_set_event_source_slot>
  <code>world::set_event_source_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Source Slot\
**Action type:** Action without value\
**Description:** Sets the source slot of the event.\
**Work_with:**\
&nbsp;&nbsp;Player Pick Item

**Usage example:**
```ts
world::set_event_source_slot(1);

//Or dry by keywords

world::set_event_source_slot(source_slot=1);
```

**Arguments:**

| ID          | Type   | Description |
|-------------|--------|-------------|
| source_slot | Number | Slot        |

<h3 id=game_set_event_target_slot>
  <code>world::set_event_target_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Target Slot\
**Action type:** Action without value\
**Description:** Sets the destination slot of the event.\
**Work_with:**\
&nbsp;&nbsp;Player Pick Item

**Usage example:**
```ts
world::set_event_target_slot(1);

//Or dry by keywords

world::set_event_target_slot(target=1);
```

**Arguments:**

| ID     | Type   | Description |
|--------|--------|-------------|
| target | Number | Slot        |

<h3 id=game_set_event_uery_info>
  <code>world::set_event_uery_info</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Tags To Received Info\
**Action type:** Action without value\
**Description:** Adds additional tags to the received debug info that will be copied to the clipboard if the event is not cancelled.\
**Additional info:**\
&nbsp;&nbsp;Additional information only changes.\
**Work_with:**\
&nbsp;&nbsp;Player Receives Block Information Event\
&nbsp;&nbsp;Player Receives Entity Info Event

**Usage example:**
```ts
world::set_event_uery_info("information");

//Or dry by keywords

world::set_event_uery_info(information="information");
```

**Arguments:**

| ID          | Type | Description     |
|-------------|------|-----------------|
| information | Text | Additional Tags |

<h3 id=game_set_event_velocity>
  <code>world::set_event_velocity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_event_velocity.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_event_velocity.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_event_velocity.work_with.player_velocity

**Usage example:**
```ts
world::set_event_velocity(vector(0,0,0));

//Or dry by keywords

world::set_event_velocity(velocity=vector(0,0,0));
```

**Arguments:**

| ID       | Type   | Description                                                         |
|----------|--------|---------------------------------------------------------------------|
| velocity | Vector | creative_plus.action.game_set_event_velocity.argument.velocity.name |

<h3 id=game_set_furnace_cook_time>
  <code>world::set_furnace_cook_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Furnace Cooking Time\
**Action type:** Action without value\
**Description:** Sets the cooking time for the oven at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Furnaces\
&nbsp;&nbsp;Blast Furnaces\
&nbsp;&nbsp;Smokers

**Usage example:**
```ts
world::set_furnace_cook_time(location(0,0,0,0,0), 1);

//Or dry by keywords

world::set_furnace_cook_time(location=location(0,0,0,0,0), time=1);
```

**Arguments:**

| ID       | Type     | Description      |
|----------|----------|------------------|
| location | Location | Furnace Location |
| time     | Number   | Cooking Time     |

<h3 id=game_set_item_in_container_slot>
  <code>world::set_item_in_container_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item In Container Slot\
**Action type:** Action without value\
**Description:** Sets an item in the specified container slot at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Containers

**Usage example:**
```ts
world::set_item_in_container_slot(location(0,0,0,0,0), item("stick"), 1);

//Or dry by keywords

world::set_item_in_container_slot(location=location(0,0,0,0,0), item=item("stick"), slot=1);
```

**Arguments:**

| ID       | Type     | Description           |
|----------|----------|-----------------------|
| location | Location | Location of Container |
| item     | Item     | Item                  |
| slot     | Number   | Slot Number           |

<h3 id=game_set_lectern_book>
  <code>world::set_lectern_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Book In Lectern\
**Action type:** Action without value\
**Description:** Sets a book in the lectern at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Lecterns

**Usage example:**
```ts
world::set_lectern_book(location(0,0,0,0,0), item("stick"), 1);

//Or dry by keywords

world::set_lectern_book(location=location(0,0,0,0,0), item=item("stick"), page=1);
```

**Arguments:**

| ID       | Type     | Description     |
|----------|----------|-----------------|
| location | Location | Pulpit Location |
| item     | Item     | Book to Set     |
| page     | Number   | Page            |

<h3 id=game_set_player_head>
  <code>world::set_player_head</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Head\
**Action type:** Action without value\
**Description:** Sets the player's head at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Player Heads

**Usage example:**
```ts
world::set_player_head(location(0,0,0,0,0), "name_or_uuid", "NAME_OR_UUID");

//Or dry by keywords

world::set_player_head(location=location(0,0,0,0,0), name_or_uuid="name_or_uuid", receive_type="NAME_OR_UUID");
```

**Arguments:**

| ID           | Type                                                                  | Description         |
|--------------|-----------------------------------------------------------------------|---------------------|
| location     | Location                                                              | Head Location       |
| name_or_uuid | Text                                                                  | Player name or UUID |
| receive_type | Marker<br/>**NAME_OR_UUID** - Name or UUID<br/>**VALUE** - Skin value | Value type          |

<h3 id=game_set_region>
  <code>world::set_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Blocks In Region\
**Action type:** Action without value\
**Description:** Sets the selected block type to the entire selected region.

**Usage example:**
```ts
world::set_region("minecraft:oak_log[axis=x]", location(0,0,0,0,0), location(0,0,0,0,0));

//Or dry by keywords

world::set_region(block="minecraft:oak_log[axis=x]", pos_1=location(0,0,0,0,0), pos_2=location(0,0,0,0,0));
```

**Arguments:**

| ID    | Type     | Description            |
|-------|----------|------------------------|
| block | Block    | Block                  |
| pos_1 | Location | Region Corner          |
| pos_2 | Location | Opposite Region Corner |

<h3 id=game_set_scoreboard_line>
  <code>world::set_scoreboard_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Line\
**Action type:** Action without value\
**Description:** Sets a line in the scoreboard

**Usage example:**
```ts
world::set_scoreboard_line("id", "line", "display", 1, "format_content", "BLANK");

//Or from the object

"id".set_scoreboard_line("line", "display", 1, "format_content", "BLANK");

//Or dry by keywords

world::set_scoreboard_line(id="id", line="line", display="display", score=1, format_content="format_content", format="BLANK");
```

**Arguments:**

| ID             | Type                                                                                             | Description    |
|----------------|--------------------------------------------------------------------------------------------------|----------------|
| id             | Text                                                                                             | Scoreboard ID  |
| line           | Text                                                                                             | Line ID        |
| display        | Text                                                                                             | Displayed text |
| score          | Number                                                                                           | Score          |
| format_content | Text                                                                                             | Format content |
| format         | Marker<br/>**BLANK** - Blank<br/>**FIXED** - Fixed<br/>**RESET** - Reset<br/>**STYLED** - Styled | Format Type    |

<h3 id=game_set_scoreboard_line_display>
  <code>world::set_scoreboard_line_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Line Display\
**Action type:** Action without value\
**Description:** Sets a scoreboard line to a text.

**Usage example:**
```ts
world::set_scoreboard_line_display("id", "line", "display");

//Or from the object

"id".set_scoreboard_line_display("line", "display");

//Or dry by keywords

world::set_scoreboard_line_display(id="id", line="line", display="display");
```

**Arguments:**

| ID      | Type | Description    |
|---------|------|----------------|
| id      | Text | Scoreboard ID  |
| line    | Text | Line ID        |
| display | Text | Displayed text |

<h3 id=game_set_scoreboard_line_format>
  <code>world::set_scoreboard_line_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Line Format\
**Action type:** Action without value\
**Description:** Sets the text formatting of a specific scoreboard line.

**Usage example:**
```ts
world::set_scoreboard_line_format("id", "line", "format_content", "BLANK");

//Or from the object

"id".set_scoreboard_line_format("line", "format_content", "BLANK");

//Or dry by keywords

world::set_scoreboard_line_format(id="id", line="line", format_content="format_content", format="BLANK");
```

**Arguments:**

| ID             | Type                                                                                             | Description    |
|----------------|--------------------------------------------------------------------------------------------------|----------------|
| id             | Text                                                                                             | Scoreboard ID  |
| line           | Text                                                                                             | Line ID        |
| format_content | Text                                                                                             | Format content |
| format         | Marker<br/>**BLANK** - Blank<br/>**FIXED** - Fixed<br/>**RESET** - Reset<br/>**STYLED** - Styled | Format type    |

<h3 id=game_set_scoreboard_number_format>
  <code>world::set_scoreboard_number_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Number Format\
**Action type:** Action without value\
**Description:** Sets the format for the values of the scoreboard.

**Usage example:**
```ts
world::set_scoreboard_number_format("id", "format_content", "BLANK");

//Or from the object

"id".set_scoreboard_number_format("format_content", "BLANK");

//Or dry by keywords

world::set_scoreboard_number_format(id="id", format_content="format_content", format="BLANK");
```

**Arguments:**

| ID             | Type                                                                                             | Description    |
|----------------|--------------------------------------------------------------------------------------------------|----------------|
| id             | Text                                                                                             | Scoreboard ID  |
| format_content | Text                                                                                             | Format content |
| format         | Marker<br/>**BLANK** - Blank<br/>**FIXED** - Fixed<br/>**RESET** - Reset<br/>**STYLED** - Styled | Format type    |

<h3 id=game_set_scoreboard_score>
  <code>world::set_scoreboard_score</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Value\
**Action type:** Action without value\
**Description:** Sets the value of the specified scoreboard with the displayed text and score.

**Usage example:**
```ts
world::set_scoreboard_score("id", "text", 1);

//Or dry by keywords

world::set_scoreboard_score(id="id", text="text", score=1);
```

**Arguments:**

| ID    | Type   | Description   |
|-------|--------|---------------|
| id    | Text   | Scoreboard ID |
| text  | Text   | Display Text  |
| score | Number | Score         |

<h3 id=game_set_scoreboard_title>
  <code>world::set_scoreboard_title</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Change Scoreboard Title\
**Action type:** Action without value\
**Description:** Changes the title of the specified scoreboard.

**Usage example:**
```ts
world::set_scoreboard_title("id", "title");

//Or dry by keywords

world::set_scoreboard_title(id="id", title="title");
```

**Arguments:**

| ID    | Type | Description   |
|-------|------|---------------|
| id    | Text | Scoreboard ID |
| title | Text | New Title     |

<h3 id=game_set_sculk_shrieker_can_summon>
  <code>world::set_sculk_shrieker_can_summon</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sculk Shrieker Can Summon\
**Action type:** Action without value\
**Description:** Sets the Sculk Shriker's ability to summon Wardens.\
**Work_with:**\
&nbsp;&nbsp;Sculk Shrieker

**Usage example:**
```ts
world::set_sculk_shrieker_can_summon(location(0,0,0,0,0), "FALSE");

//Or dry by keywords

world::set_sculk_shrieker_can_summon(location=location(0,0,0,0,0), can_summon="FALSE");
```

**Arguments:**

| ID         | Type                                             | Description             |
|------------|--------------------------------------------------|-------------------------|
| location   | Location                                         | Sculk Shrieker location |
| can_summon | Marker<br/>**FALSE** - False<br/>**TRUE** - True | Can summon              |

<h3 id=game_set_sculk_shrieker_shrieking>
  <code>world::set_sculk_shrieker_shrieking</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sculk Shrieker Shrieking\
**Action type:** Action without value\
**Description:** Sets the shrieking status of a Sculk Shrieker.\
**Work_with:**\
&nbsp;&nbsp;Sculk Shrieker

**Usage example:**
```ts
world::set_sculk_shrieker_shrieking(location(0,0,0,0,0), "FALSE");

//Or dry by keywords

world::set_sculk_shrieker_shrieking(location=location(0,0,0,0,0), shrieking="FALSE");
```

**Arguments:**

| ID        | Type                                             | Description             |
|-----------|--------------------------------------------------|-------------------------|
| location  | Location                                         | Sculk Shrieker location |
| shrieking | Marker<br/>**FALSE** - False<br/>**TRUE** - True | Shrieking               |

<h3 id=game_set_sculk_shrieker_warning_level>
  <code>world::set_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sculk Shrieker Warning Level\
**Action type:** Action without value\
**Description:** Sets the warning levels of a Sculk Shrieker.\
**Work_with:**\
&nbsp;&nbsp;Sculk Shrieker

**Usage example:**
```ts
world::set_sculk_shrieker_warning_level(location(0,0,0,0,0), 1);

//Or dry by keywords

world::set_sculk_shrieker_warning_level(location=location(0,0,0,0,0), warning_level=1);
```

**Arguments:**

| ID            | Type     | Description             |
|---------------|----------|-------------------------|
| location      | Location | Sculk Shrieker location |
| warning_level | Number   | Warning level           |

<h3 id=game_set_sign_text>
  <code>world::set_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sign Text\
**Action type:** Action without value\
**Description:** Sets the sign text at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Signs

**Usage example:**
```ts
world::set_sign_text(location(0,0,0,0,0), "text", 1, "ALL");

//Or dry by keywords

world::set_sign_text(location=location(0,0,0,0,0), text="text", line=1, side="ALL");
```

**Arguments:**

| ID       | Type                                                               | Description   |
|----------|--------------------------------------------------------------------|---------------|
| location | Location                                                           | Sign location |
| text     | Text                                                               | Text to set   |
| line     | Number                                                             | Line          |
| side     | Marker<br/>**ALL** - All<br/>**BACK** - Back<br/>**FRONT** - Front | Sign Side     |

<h3 id=game_set_sign_text_color>
  <code>world::set_sign_text_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sign Text Color\
**Action type:** Action without value\
**Description:** Sets the color of sign text at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Signs

**Usage example:**
```ts
world::set_sign_text_color(location(0,0,0,0,0), "ALL", "BLACK", "FALSE");

//Or dry by keywords

world::set_sign_text_color(location=location(0,0,0,0,0), side="ALL", sign_text_color="BLACK", glowing="FALSE");
```

**Arguments:**

| ID              | Type                                                                                                                                                                                                                                                                                                                                                                             | Description   |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| location        | Location                                                                                                                                                                                                                                                                                                                                                                         | Sign location |
| side            | Marker<br/>**ALL** - All<br/>**BACK** - Back<br/>**FRONT** - Front                                                                                                                                                                                                                                                                                                               | Sign Side     |
| sign_text_color | Marker<br/>**BLACK** - Black<br/>**BLUE** - Blue<br/>**BROWN** - Brown<br/>**CYAN** - Cyan<br/>**GRAY** - Grey<br/>**GREEN** - Green<br/>**LIGHT_BLUE** - Blue<br/>**LIGHT_GRAY** - Light Gray<br/>**LIME** - Lime<br/>**MAGENTA** - Magenta<br/>**ORANGE** - Orange<br/>**PINK** - Pink<br/>**PURPLE** - Purple<br/>**RED** - Red<br/>**WHITE** - White<br/>**YELLOW** - Yellow | Sign Color    |
| glowing         | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable                                                                                                                                                                                                                                                                                                                             | Text Glow     |

<h3 id=game_set_sign_waxed>
  <code>world::set_sign_waxed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sign Waxed\
**Action type:** Action without value\
**Description:** Sets the waxedness of the sign at the selected location.\
**Work_with:**\
&nbsp;&nbsp;Signs

**Usage example:**
```ts
world::set_sign_waxed(location(0,0,0,0,0), "FALSE");

//Or dry by keywords

world::set_sign_waxed(location=location(0,0,0,0,0), waxed="FALSE");
```

**Arguments:**

| ID       | Type                                                 | Description         |
|----------|------------------------------------------------------|---------------------|
| location | Location                                             | Sign Waxed Location |
| waxed    | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Waxed               |

<h3 id=game_set_spawner_entity>
  <code>world::set_spawner_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Spawner Entity\
**Action type:** Action without value\
**Description:** Sets the entity that spawns near a Spawner.\
**Work_with:**\
&nbsp;&nbsp;Spawner

**Usage example:**
```ts
world::set_spawner_entity(location(0,0,0,0,0), item("stick"));

//Or from the object

location(0,0,0,0,0).set_spawner_entity(item("stick"));

//Or dry by keywords

world::set_spawner_entity(location=location(0,0,0,0,0), entity=item("stick"));
```

**Arguments:**

| ID       | Type     | Description      |
|----------|----------|------------------|
| location | Location | Spawner location |
| entity   | Item     | Entity           |

<h3 id=game_set_tile_block_custom_tag>
  <code>world::set_tile_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_tile_block_custom_tag.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_tile_block_custom_tag.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_tile_block_custom_tag.work_with.tile_state_block

**Usage example:**
```ts
world::set_tile_block_custom_tag(location(0,0,0,0,0), "tag_name", "tag_value");

//Or dry by keywords

world::set_tile_block_custom_tag(location=location(0,0,0,0,0), tag_name="tag_name", tag_value="tag_value");
```

**Arguments:**

| ID        | Type     | Description                                                                 |
|-----------|----------|-----------------------------------------------------------------------------|
| location  | Location | creative_plus.action.game_set_tile_block_custom_tag.argument.location.name  |
| tag_name  | Text     | creative_plus.action.game_set_tile_block_custom_tag.argument.tag_name.name  |
| tag_value | Text     | creative_plus.action.game_set_tile_block_custom_tag.argument.tag_value.name |

<h3 id=game_set_vault_displayed_item>
  <code>world::set_vault_displayed_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_vault_displayed_item.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_vault_displayed_item.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.game_set_vault_displayed_item.additional_information.next_cycle_will_override_item\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_vault_displayed_item.work_with.vault

**Usage example:**
```ts
world::set_vault_displayed_item(location(0,0,0,0,0), item("stick"));

//Or dry by keywords

world::set_vault_displayed_item(location=location(0,0,0,0,0), item=item("stick"));
```

**Arguments:**

| ID       | Type     | Description                                                               |
|----------|----------|---------------------------------------------------------------------------|
| location | Location | creative_plus.action.game_set_vault_displayed_item.argument.location.name |
| item     | Item     | creative_plus.action.game_set_vault_displayed_item.argument.item.name     |

<h3 id=game_set_vault_next_state_update_time>
  <code>world::set_vault_next_state_update_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_set_vault_next_state_update_time.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_set_vault_next_state_update_time.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.game_set_vault_next_state_update_time.additional_information.set_absolute_time_when_will_happen\
&nbsp;&nbsp;creative_plus.action.game_set_vault_next_state_update_time.additional_information.default_max_possible_time\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_set_vault_next_state_update_time.work_with.vault

**Usage example:**
```ts
world::set_vault_next_state_update_time(location(0,0,0,0,0), 1);

//Or dry by keywords

world::set_vault_next_state_update_time(location=location(0,0,0,0,0), time=1);
```

**Arguments:**

| ID       | Type     | Description                                                                       |
|----------|----------|-----------------------------------------------------------------------------------|
| location | Location | creative_plus.action.game_set_vault_next_state_update_time.argument.location.name |
| time     | Number   | creative_plus.action.game_set_vault_next_state_update_time.argument.time.name     |

<h3 id=game_set_world_difficulty>
  <code>world::set_world_difficulty</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Difficulty\
**Action type:** Action without value\
**Description:** Sets a specific world difficulty.

**Usage example:**
```ts
world::set_world_difficulty("EASY");

//Or dry by keywords

world::set_world_difficulty(difficulty="EASY");
```

**Arguments:**

| ID         | Type                                                                                               | Description |
|------------|----------------------------------------------------------------------------------------------------|-------------|
| difficulty | Marker<br/>**EASY** - Easy<br/>**HARD** - Hard<br/>**NORMAL** - Normal<br/>**PEACEFUL** - Peaceful | Difficulty  |

<h3 id=game_set_world_gamerule>
  <code>world::set_gamerule</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Gamerule\
**Action type:** Action without value\
**Description:** Sets a specific game rule in the world.\
**Additional info:**\
&nbsp;&nbsp;Leave the value argument empty to reset the gamerule to its default state.

**Usage example:**
```ts
world::set_gamerule("DISABLE_RAIDS", "value");

//Or dry by keywords

world::set_gamerule(gamerule="DISABLE_RAIDS", value="value");
```

**Arguments:**

| ID       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| gamerule | Marker<br/>**DISABLE_RAIDS** - disableRaids<br/>**DO_DAYLIGHT_CYCLE** - doDaylightCycle<br/>**DO_ENTITY_DROPS** - doEntityDrops<br/>**DO_FIRE_TICK** - doFireTick<br/>**DO_IMMEDIATE_RESPAWN** - doImmediateRespawn<br/>**DO_INSOMNIA** - doInsomnia<br/>**DO_MOB_LOOT** - doMobLoot<br/>**DO_MOB_SPAWNING** - doMobSpawning<br/>**DO_PATROL_SPAWNING** - doPatrolSpawning<br/>**DO_TILE_DROPS** - doTileDrops<br/>**DO_TRADER_SPAWNING** - doTraderSpawning<br/>**DO_WEATHER_CYCLE** - doWeatherCycle<br/>**DROWNING_DAMAGE** - drowningDamage<br/>**FALL_DAMAGE** - fallDamage<br/>**FIRE_DAMAGE** - fireDamage<br/>**FORGIVE_DEAD_PLAYERS** - forgiveDeadPlayers<br/>**KEEP_INVENTORY** - keepInventory<br/>**MOB_GRIEFING** - mobGriefing<br/>**PROJECTILES_CAN_BREAK_BLOCKS** - projectilesCanBreakBlocks<br/>**SHOW_DEATH_MESSAGES** - showDeathMessages<br/>**NATURAL_REGENERATION** - naturalRegeneration<br/>**UNIVERSAL_ANGER** - universalAnger<br/>**PLAYERS_SLEEPING_PERCENTAGE** - playersSleepingPercentage<br/>**REDUCED_DEBUG_INFO** - reducedDebugInfo<br/>**FREEZE_DAMAGE** - freezeDamage<br/>**RANDOM_TICK_SPEED** - randomTickSpeed<br/>**MAX_ENTITY_CRAMMING** - maxEntityCramming<br/>**SPAWN_RADIUS** - spawnRadius<br/>**LAVA_SOURCE_CONVERSION** - lavaSourceConversion<br/>**WATER_SOURCE_CONVERSION** - waterSourceConversion<br/>**TNT_EXPLOSION_DROP_DECAY** - tntExplosionDropDecay<br/>**BLOCK_EXPLOSION_DROP_DECAY** - blockExplosionDropDecay<br/>**MOB_EXPLOSION_DROP_DECAY** - mobExplosionDropDecay<br/>**DO_LIMITED_CRAFTING** - doLimitedCrafting<br/>**PLAYERS_NETHER_PORTAL_DEFAULT_DELAY** - playersNetherPortalDefaultDelay<br/>**PLAYERS_NETHER_PORTAL_CREATIVE_DELAY** - playersNetherPortalCreativeDelay<br/>**SNOW_ACCUMULATION_HEIGHT** - snowAccumulationHeight<br/>**SPAWN_CHUNK_RADIUS** - spawnChunkRadius<br/>**DO_WARDEN_SPAWNING** - doWardenSpawning<br/>**ENDER_PEARLS_VANISH_ON_DEATH** - enderPearlsVanishOnDeath<br/>**DO_VINES_SPREAD** - doVinesSpread<br/>**ALLOW_FIRE_TICKS_AWAY_FROM_PLAYER** - creative_plus.action.game_set_world_gamerule.argument.gamerule.enum.allow_fire_ticks_away_from_player.name<br/>**TNT_EXPLODER** - creative_plus.action.game_set_world_gamerule.argument.gamerule.enum.tnt_exploder.name<br/>**LOCATOR_BAR** - creative_plus.action.game_set_world_gamerule.argument.gamerule.enum.locator_bar.name<br/>**SPAWN_MONSTERS** - creative_plus.action.game_set_world_gamerule.argument.gamerule.enum.spawn_monsters.name<br/>**PVP** - creative_plus.action.game_set_world_gamerule.argument.gamerule.enum.pvp.name<br/>**SPAWNER_BLOCKS_WORK** - creative_plus.action.game_set_world_gamerule.argument.gamerule.enum.spawner_blocks_work.name | Gamerule    |
| value    | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Value       |

<h3 id=game_set_world_simulation_distance>
  <code>world::set_world_simulation_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Simulation Distance\
**Action type:** Action without value\
**Description:** Sets the chunk simulation distance for the world.

**Usage example:**
```ts
world::set_world_simulation_distance(1);

//Or dry by keywords

world::set_world_simulation_distance(distance=1);
```

**Arguments:**

| ID       | Type   | Description                          |
|----------|--------|--------------------------------------|
| distance | Number | Simulation Distance in Chunks (2-32) |

<h3 id=game_set_world_time>
  <code>world::set_world_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Time\
**Action type:** Action without value\
**Description:** Sets the world time in ticks.

**Usage example:**
```ts
world::set_world_time(1);

//Or dry by keywords

world::set_world_time(time=1);
```

**Arguments:**

| ID   | Type   | Description   |
|------|--------|---------------|
| time | Number | Time in ticks |

<h3 id=game_set_world_weather>
  <code>world::set_world_weather</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Weather\
**Action type:** Action without value\
**Description:** Sets the world's weather for a certain amount of time.\
**Additional info:**\
&nbsp;&nbsp;By default, if no duration is specified, the weather will not change.

**Usage example:**
```ts
world::set_world_weather(1, "CLEAR");

//Or dry by keywords

world::set_world_weather(weather_duration=1, weather_type="CLEAR");
```

**Arguments:**

| ID               | Type                                                                                  | Description  |
|------------------|---------------------------------------------------------------------------------------|--------------|
| weather_duration | Number                                                                                | Duration     |
| weather_type     | Marker<br/>**CLEAR** - Clear<br/>**RAINING** - Raining<br/>**THUNDER** - Thunderstorm | Weather Type |

<h3 id=game_spawn_armor_stand>
  <code>world::spawn_armor_stand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Armor Stand\
**Action type:** Action without value\
**Description:** Spawns an armor stand at the specified location.

**Usage example:**
```ts
world::spawn_armor_stand(item("stick"), item("stick"), item("stick"), item("stick"), item("stick"), item("stick"), location(0,0,0,0,0), "custom_name", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Or dry by keywords

world::spawn_armor_stand(helmet=item("stick"), chestplate=item("stick"), leggings=item("stick"), boots=item("stick"), right_hand=item("stick"), left_hand=item("stick"), location=location(0,0,0,0,0), custom_name="custom_name", gravity="FALSE", marker="FALSE", small="FALSE", show_arms="FALSE", base_plate="FALSE", invisible="FALSE");
```

**Arguments:**

| ID          | Type                                                   | Description     |
|-------------|--------------------------------------------------------|-----------------|
| helmet      | Item                                                   | Headgear        |
| chestplate  | Item                                                   | Chestplate      |
| leggings    | Item                                                   | Leggings        |
| boots       | Item                                                   | Boots           |
| right_hand  | Item                                                   | Right Hand Item |
| left_hand   | Item                                                   | Left Hand Item  |
| location    | Location                                               | Spawn Location  |
| custom_name | Text                                                   | Stand name      |
| gravity     | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable   | Set Gravity     |
| marker      | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Marker Mode     |
| small       | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable   | Make Small      |
| show_arms   | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable   | Show Arms       |
| base_plate  | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable   | Slab Display    |
| invisible   | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable   | Invisible       |

<h3 id=game_spawn_block_display>
  <code>world::spawn_block_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Block Display\
**Action type:** Action without value\
**Description:** Spawns a block renderer at the specified location

**Usage example:**
```ts
world::spawn_block_display(location(0,0,0,0,0), "custom_name", "minecraft:oak_log[axis=x]");

//Or dry by keywords

world::spawn_block_display(spawn_location=location(0,0,0,0,0), custom_name="custom_name", block="minecraft:oak_log[axis=x]");
```

**Arguments:**

| ID             | Type     | Description    |
|----------------|----------|----------------|
| spawn_location | Location | Spawn Location |
| custom_name    | Text     | Name           |
| block          | Block    | Display Block  |

<h3 id=game_spawn_effect_cloud>
  <code>world::spawn_effect_cloud</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Effect Cloud\
**Action type:** Action without value\
**Description:** Spawns a cloud of misty potion that infuses the effects of the entities in it.

**Usage example:**
```ts
world::spawn_effect_cloud(location(0,0,0,0,0), 1, 2, [potion("slow_falling"), potion("slow_falling")], particle("fire"), "custom_name");

//Or dry by keywords

world::spawn_effect_cloud(location=location(0,0,0,0,0), duration=1, radius=2, effects=[potion("slow_falling"), potion("slow_falling")], particle=particle("fire"), custom_name="custom_name");
```

**Arguments:**

| ID          | Type            | Description                                                 |
|-------------|-----------------|-------------------------------------------------------------|
| location    | Location        | Spawn Location                                              |
| duration    | Number          | Duration                                                    |
| radius      | Number          | Cloud Radius                                                |
| effects     | Array\[Potion\] | Potion Effects<br/>The argument supports list decomposition |
| particle    | Particle Effect | Cloud Particles                                             |
| custom_name | Text            | Name                                                        |

<h3 id=game_spawn_end_crystal>
  <code>world::spawn_end_crystal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn End Crystal\
**Action type:** Action without value\
**Description:** Spawns an End Crystal at the specified location.

**Usage example:**
```ts
world::spawn_end_crystal(location(0,0,0,0,0), "custom_name", "FALSE");

//Or dry by keywords

world::spawn_end_crystal(location=location(0,0,0,0,0), custom_name="custom_name", show_bottom="FALSE");
```

**Arguments:**

| ID          | Type                                         | Description      |
|-------------|----------------------------------------------|------------------|
| location    | Location                                     | Spawn Location   |
| custom_name | Text                                         | Name             |
| show_bottom | Marker<br/>**FALSE** - No<br/>**TRUE** - Yes | Spawn Foundation |

<h3 id=game_spawn_evoker_fangs>
  <code>world::spawn_evoker_fangs</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Evoker Fangs\
**Action type:** Action without value\
**Description:** Spawns the Evoker fangs at the specified location.

**Usage example:**
```ts
world::spawn_evoker_fangs(location(0,0,0,0,0), "custom_name");

//Or dry by keywords

world::spawn_evoker_fangs(location=location(0,0,0,0,0), custom_name="custom_name");
```

**Arguments:**

| ID          | Type     | Description    |
|-------------|----------|----------------|
| location    | Location | Spawn Location |
| custom_name | Text     | Name           |

<h3 id=game_spawn_experience_orb>
  <code>world::spawn_experience_orb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Experience Orb\
**Action type:** Action without value\
**Description:** Spawns an Experience Orb at the specified location with the selected options.

**Usage example:**
```ts
world::spawn_experience_orb(location(0,0,0,0,0), 1, "custom_name");

//Or dry by keywords

world::spawn_experience_orb(location=location(0,0,0,0,0), experience_amount=1, custom_name="custom_name");
```

**Arguments:**

| ID                | Type     | Description       |
|-------------------|----------|-------------------|
| location          | Location | Spawn Location    |
| experience_amount | Number   | Experience Amount |
| custom_name       | Text     | Name              |

<h3 id=game_spawn_eye_of_ender>
  <code>world::spawn_eye_of_ender</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Eye of Ender\
**Action type:** Action without value\
**Description:** Spawns an Eye of End at the target location that will move towards the target.

**Usage example:**
```ts
world::spawn_eye_of_ender(location(0,0,0,0,0), location(0,0,0,0,0), 1, "custom_name", "DROP");

//Or dry by keywords

world::spawn_eye_of_ender(location=location(0,0,0,0,0), destination=location(0,0,0,0,0), lifespan=1, custom_name="custom_name", end_of_lifespan="DROP");
```

**Arguments:**

| ID              | Type                                                                                 | Description    |
|-----------------|--------------------------------------------------------------------------------------|----------------|
| location        | Location                                                                             | Spawn Location |
| destination     | Location                                                                             | Destination    |
| lifespan        | Number                                                                               | Lifespan       |
| custom_name     | Text                                                                                 | Name           |
| end_of_lifespan | Marker<br/>**DROP** - Drop an item<br/>**RANDOM** - Random<br/>**SHATTER** - Shatter | At End         |

<h3 id=game_spawn_falling_block>
  <code>world::spawn_falling_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Falling Block\
**Action type:** Action without value\
**Description:** Spawns a falling block at the specified location.

**Usage example:**
```ts
world::spawn_falling_block("minecraft:oak_log[axis=x]", location(0,0,0,0,0), "name", "FALSE");

//Or dry by keywords

world::spawn_falling_block(block="minecraft:oak_log[axis=x]", location=location(0,0,0,0,0), name="name", should_expire="FALSE");
```

**Arguments:**

| ID            | Type                                           | Description    |
|---------------|------------------------------------------------|----------------|
| block         | Block                                          | Block to Spawn |
| location      | Location                                       | Spawn Location |
| name          | Text                                           | Name           |
| should_expire | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes | Must Vanish    |

<h3 id=game_spawn_interaction_entity>
  <code>world::spawn_interaction_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Interaction Entity\
**Action type:** Action without value\
**Description:** Spawns an interaction entity at the specified location\
**Additional info:**\
&nbsp;&nbsp;Detect interaction with entity attack and click events.

**Usage example:**
```ts
world::spawn_interaction_entity(location(0,0,0,0,0), "custom_name", 1, 2, "FALSE");

//Or dry by keywords

world::spawn_interaction_entity(location=location(0,0,0,0,0), custom_name="custom_name", width=1, height=2, responsive="FALSE");
```

**Arguments:**

| ID          | Type                                                 | Description     |
|-------------|------------------------------------------------------|-----------------|
| location    | Location                                             | Spawn Location  |
| custom_name | Text                                                 | Name            |
| width       | Number                                               | Horizontal Size |
| height      | Number                                               | Vertical size   |
| responsive  | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Responsive      |

<h3 id=game_spawn_item>
  <code>world::spawn_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Item\
**Action type:** Action without value\
**Description:** Spawns an item at the specified location with the selected options.

**Usage example:**
```ts
world::spawn_item(location(0,0,0,0,0), item("stick"), "custom_name", "FALSE", "FALSE", "FALSE");

//Or dry by keywords

world::spawn_item(location=location(0,0,0,0,0), item=item("stick"), custom_name="custom_name", can_mob_pickup="FALSE", can_player_pickup="FALSE", apply_motion="FALSE");
```

**Arguments:**

| ID                | Type                                           | Description                         |
|-------------------|------------------------------------------------|-------------------------------------|
| location          | Location                                       | Spawn Location                      |
| item              | Item                                           | Item to Spawn                       |
| custom_name       | Text                                           | Name                                |
| can_mob_pickup    | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes | Can mobs pick up an item            |
| can_player_pickup | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes | Whether players can pick up an item |
| apply_motion      | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes | Set Item Motion on Spawn            |

<h3 id=game_spawn_item_display>
  <code>world::spawn_item_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Item Display\
**Action type:** Action without value\
**Description:** Spawns an item visualizer at the specified location

**Usage example:**
```ts
world::spawn_item_display(location(0,0,0,0,0), "custom_name", item("stick"));

//Or dry by keywords

world::spawn_item_display(spawn_location=location(0,0,0,0,0), custom_name="custom_name", displayed_item=item("stick"));
```

**Arguments:**

| ID             | Type     | Description    |
|----------------|----------|----------------|
| spawn_location | Location | Spawn Location |
| custom_name    | Text     | Name           |
| displayed_item | Item     | Displayed Item |

<h3 id=game_spawn_item_frame>
  <code>world::spawn_item_frame</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_spawn_item_frame.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_spawn_item_frame.description

**Usage example:**
```ts
world::spawn_item_frame(location(0,0,0,0,0), item("stick"), "NONE", "NORTH", "TRUE", "TRUE", "TRUE");

//Or dry by keywords

world::spawn_item_frame(spawn_location=location(0,0,0,0,0), item=item("stick"), rotation="NONE", block_face="NORTH", glowing="TRUE", visible="TRUE", fixed="TRUE");
```

**Arguments:**

| ID             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                             |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| spawn_location | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | creative_plus.action.game_spawn_item_frame.argument.spawn_location.name |
| item           | Item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | creative_plus.action.game_spawn_item_frame.argument.item.name           |
| rotation       | Marker<br/>**NONE** - creative_plus.action.game_spawn_item_frame.argument.rotation.enum.none.name<br/>**CLOCKWISE_45** - creative_plus.action.game_spawn_item_frame.argument.rotation.enum.clockwise_45.name<br/>**CLOCKWISE** - creative_plus.action.game_spawn_item_frame.argument.rotation.enum.clockwise.name<br/>**CLOCKWISE_135** - creative_plus.action.game_spawn_item_frame.argument.rotation.enum.clockwise_135.name<br/>**FLIPPED** - creative_plus.action.game_spawn_item_frame.argument.rotation.enum.flipped.name<br/>**FLIPPED_45** - creative_plus.action.game_spawn_item_frame.argument.rotation.enum.flipped_45.name<br/>**COUNTER_CLOCKWISE** - creative_plus.action.game_spawn_item_frame.argument.rotation.enum.counter_clockwise.name<br/>**COUNTER_CLOCKWISE_45** - creative_plus.action.game_spawn_item_frame.argument.rotation.enum.counter_clockwise_45.name | creative_plus.action.game_spawn_item_frame.argument.rotation.name       |
| block_face     | Marker<br/>**NORTH** - creative_plus.action.game_spawn_item_frame.argument.block_face.enum.north.name<br/>**EAST** - creative_plus.action.game_spawn_item_frame.argument.block_face.enum.east.name<br/>**SOUTH** - creative_plus.action.game_spawn_item_frame.argument.block_face.enum.south.name<br/>**WEST** - creative_plus.action.game_spawn_item_frame.argument.block_face.enum.west.name<br/>**UP** - creative_plus.action.game_spawn_item_frame.argument.block_face.enum.up.name<br/>**DOWN** - creative_plus.action.game_spawn_item_frame.argument.block_face.enum.down.name                                                                                                                                                                                                                                                                                                   | creative_plus.action.game_spawn_item_frame.argument.block_face.name     |
| glowing        | Marker<br/>**TRUE** - creative_plus.action.game_spawn_item_frame.argument.glowing.enum.true.name<br/>**FALSE** - creative_plus.action.game_spawn_item_frame.argument.glowing.enum.false.name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | creative_plus.action.game_spawn_item_frame.argument.glowing.name        |
| visible        | Marker<br/>**TRUE** - creative_plus.action.game_spawn_item_frame.argument.visible.enum.true.name<br/>**FALSE** - creative_plus.action.game_spawn_item_frame.argument.visible.enum.false.name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | creative_plus.action.game_spawn_item_frame.argument.visible.name        |
| fixed          | Marker<br/>**TRUE** - creative_plus.action.game_spawn_item_frame.argument.fixed.enum.true.name<br/>**FALSE** - creative_plus.action.game_spawn_item_frame.argument.fixed.enum.false.name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | creative_plus.action.game_spawn_item_frame.argument.fixed.name          |

<h3 id=game_spawn_lightning_bolt>
  <code>world::spawn_lightning_bolt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Lightning\
**Action type:** Action without value\
**Description:** Spawns lightning at the specified location.

**Usage example:**
```ts
world::spawn_lightning_bolt(location(0,0,0,0,0));

//Or dry by keywords

world::spawn_lightning_bolt(location=location(0,0,0,0,0));
```

**Arguments:**

| ID       | Type     | Description    |
|----------|----------|----------------|
| location | Location | Spawn Location |

<h3 id=game_spawn_mob>
  <code>world::spawn_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Entity\
**Action type:** Action without value\
**Description:** Spawns a mob at the specified location with the selected options.

**Usage example:**
```ts
world::spawn_mob(item("stick"), location(0,0,0,0,0), 1, "custom_name", [potion("slow_falling"), potion("slow_falling")], item("stick"), item("stick"), item("stick"), item("stick"), item("stick"), item("stick"), "FALSE");

//Or dry by keywords

world::spawn_mob(mob=item("stick"), location=location(0,0,0,0,0), health=1, custom_name="custom_name", potion_effects=[potion("slow_falling"), potion("slow_falling")], main_hand=item("stick"), helmet=item("stick"), chestplate=item("stick"), leggings=item("stick"), boots=item("stick"), off_hand=item("stick"), natural_equipment="FALSE");
```

**Arguments:**

| ID                | Type                                                 | Description                                          |
|-------------------|------------------------------------------------------|------------------------------------------------------|
| mob               | Item                                                 | Mob Type                                             |
| location          | Location                                             | Spawn Location                                       |
| health            | Number                                               | Amount of Health                                     |
| custom_name       | Text                                                 | Name                                                 |
| potion_effects    | Array\[Potion\]                                      | Effects<br/>The argument supports list decomposition |
| main_hand         | Item                                                 | Main Hand Item                                       |
| helmet            | Item                                                 | Headgear                                             |
| chestplate        | Item                                                 | Chestplate                                           |
| leggings          | Item                                                 | Leggings                                             |
| boots             | Item                                                 | Boots                                                |
| off_hand          | Item                                                 | Offhand Item                                         |
| natural_equipment | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Standard Equipment                                   |

<h3 id=game_spawn_painting>
  <code>world::spawn_painting</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_spawn_painting.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_spawn_painting.description

**Usage example:**
```ts
world::spawn_painting(location(0,0,0,0,0), "art", "NORTH");

//Or dry by keywords

world::spawn_painting(spawn_location=location(0,0,0,0,0), art="art", block_face="NORTH");
```

**Arguments:**

| ID             | Type                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                           |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| spawn_location | Location                                                                                                                                                                                                                                                                                                                                                                               | creative_plus.action.game_spawn_painting.argument.spawn_location.name |
| art            | Text                                                                                                                                                                                                                                                                                                                                                                                   | creative_plus.action.game_spawn_painting.argument.art.name            |
| block_face     | Marker<br/>**NORTH** - creative_plus.action.game_spawn_painting.argument.block_face.enum.north.name<br/>**EAST** - creative_plus.action.game_spawn_painting.argument.block_face.enum.east.name<br/>**SOUTH** - creative_plus.action.game_spawn_painting.argument.block_face.enum.south.name<br/>**WEST** - creative_plus.action.game_spawn_painting.argument.block_face.enum.west.name | creative_plus.action.game_spawn_painting.argument.block_face.name     |

<h3 id=game_spawn_primed_tnt>
  <code>world::spawn_primed_tnt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Ignited TNT\
**Action type:** Action without value\
**Description:** Spawns ignited dynamite at the specified location.

**Usage example:**
```ts
world::spawn_primed_tnt(location(0,0,0,0,0), 1, 2, "custom_name", "minecraft:oak_log[axis=x]");

//Or dry by keywords

world::spawn_primed_tnt(location=location(0,0,0,0,0), tnt_power=1, fuse_duration=2, custom_name="custom_name", block="minecraft:oak_log[axis=x]");
```

**Arguments:**

| ID            | Type     | Description             |
|---------------|----------|-------------------------|
| location      | Location | Spawn Location          |
| tnt_power     | Number   | Dynamite Power (0 to 4) |
| fuse_duration | Number   | Explosion Delay Time    |
| custom_name   | Text     | Name                    |
| block         | Block    | Disguise block          |

<h3 id=game_spawn_shulker_bullet>
  <code>world::spawn_shulker_bullet</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Shulker Bullet\
**Action type:** Action without value\
**Description:** Spawns a Shulker Bullet at the specified location.

**Usage example:**
```ts
world::spawn_shulker_bullet(location(0,0,0,0,0), "custom_name");

//Or dry by keywords

world::spawn_shulker_bullet(location=location(0,0,0,0,0), custom_name="custom_name");
```

**Arguments:**

| ID          | Type     | Description    |
|-------------|----------|----------------|
| location    | Location | Spawn Location |
| custom_name | Text     | Name           |

<h3 id=game_spawn_text_display>
  <code>world::spawn_text_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Text Display\
**Action type:** Action without value\
**Description:** Spawns a text renderer at the specified location

**Usage example:**
```ts
world::spawn_text_display(location(0,0,0,0,0), "custom_name", ["displayed_text", "displayed_text"], "CONCATENATION");

//Or dry by keywords

world::spawn_text_display(spawn_location=location(0,0,0,0,0), custom_name="custom_name", displayed_text=["displayed_text", "displayed_text"], merging_mode="CONCATENATION");
```

**Arguments:**

| ID             | Type                                                                                                           | Description                                                 |
|----------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| spawn_location | Location                                                                                                       | Spawn Location                                              |
| custom_name    | Text                                                                                                           | Name                                                        |
| displayed_text | Array\[Text\]                                                                                                  | Displayed Text<br/>The argument supports list decomposition |
| merging_mode   | Marker<br/>**CONCATENATION** - Merge<br/>**SEPARATE_LINES** - Separate Lines<br/>**SPACES** - Space Separation | Merge Text                                                  |

<h3 id=game_spawn_vehicle>
  <code>world::spawn_vehicle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Vehicle\
**Action type:** Action without value\
**Description:** Spawns a vehicle at the specified location with the selected options.

**Usage example:**
```ts
world::spawn_vehicle(item("stick"), location(0,0,0,0,0), "custom_name");

//Or dry by keywords

world::spawn_vehicle(vehicle=item("stick"), location=location(0,0,0,0,0), custom_name="custom_name");
```

**Arguments:**

| ID          | Type     | Description    |
|-------------|----------|----------------|
| vehicle     | Item     | Vehicle Type   |
| location    | Location | Spawn Location |
| custom_name | Text     | Name           |

<h3 id=game_uncancel_event>
  <code>world::uncancel_event</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Uncancel Event\
**Action type:** Action without value\
**Description:** Returns the cancellation of the event that triggered this code.

**Usage example:**
```ts
world::uncancel_event();
```

<h3 id=game_update_block>
  <code>world::update_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Update Adjacent Block\
**Action type:** Action without value\
**Description:** Updates adjacent blocks at the specified location if the block is not air. The block on the location itself is not updated, but it can be updated from adjacent blocks.

**Usage example:**
```ts
world::update_block(location(0,0,0,0,0));

//Or dry by keywords

world::update_block(location=location(0,0,0,0,0));
```

**Arguments:**

| ID       | Type     | Description |
|----------|----------|-------------|
| location | Location | Location    |

<h3 id=game_wobble_decorated_pot>
  <code>world::wobble_decorated_pot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.game_wobble_decorated_pot.name\
**Action type:** Action without value\
**Description:** creative_plus.action.game_wobble_decorated_pot.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.game_wobble_decorated_pot.work_with.decorated_pot

**Usage example:**
```ts
world::wobble_decorated_pot(location(0,0,0,0,0), "POSITIVE");

//Or dry by keywords

world::wobble_decorated_pot(location=location(0,0,0,0,0), style="POSITIVE");
```

**Arguments:**

| ID       | Type                                                                                                                                                                                                           | Description                                                           |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| location | Location                                                                                                                                                                                                       | creative_plus.action.game_wobble_decorated_pot.argument.location.name |
| style    | Marker<br/>**POSITIVE** - creative_plus.action.game_wobble_decorated_pot.argument.style.enum.positive.name<br/>**NEGATIVE** - creative_plus.action.game_wobble_decorated_pot.argument.style.enum.negative.name | creative_plus.action.game_wobble_decorated_pot.argument.style.name    |

<h3 id=if_game_block_equals>
  <code>world::block_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Block Equals\
**Action type:** Action that checks the conditions\
**Description:** Checks if a block at a specific location is a specific block type.

**Usage example:**
```ts
if(world::block_equals(["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], location(0,0,0,0,0))){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::block_equals(blocks=["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], location=location(0,0,0,0,0))){
    player::message("Condition is true");
}
```

**Arguments:**

| ID       | Type           | Description                                                      |
|----------|----------------|------------------------------------------------------------------|
| blocks   | Array\[Block\] | Block Type to Check<br/>The argument supports list decomposition |
| location | Location       | Block Location                                                   |

<h3 id=if_game_block_powered>
  <code>world::block_powered</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Block Powered by Redstone\
**Action type:** Action that checks the conditions\
**Description:** Checks if a block at a specific location is powered by redstone.

**Usage example:**
```ts
if(world::block_powered([location(0,0,0,0,0), location(0,0,0,0,0)], "DIRECT")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::block_powered(locations=[location(0,0,0,0,0), location(0,0,0,0,0)], power_mode="DIRECT")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID         | Type                                                                       | Description                                                 |
|------------|----------------------------------------------------------------------------|-------------------------------------------------------------|
| locations  | Array\[Location\]                                                          | Block Location<br/>The argument supports list decomposition |
| power_mode | Marker<br/>**DIRECT** - Direct Powered<br/>**INDIRECT** - Indirect Powered | Redstone Powered Type                                       |

<h3 id=if_game_chunk_is_loaded>
  <code>world::chunk_is_loaded</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Chunk Is Loaded\
**Action type:** Action that checks the conditions\
**Description:** Checks if the location has a chunk loaded

**Usage example:**
```ts
if(world::chunk_is_loaded(location(0,0,0,0,0))){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::chunk_is_loaded(location=location(0,0,0,0,0))){
    player::message("Condition is true");
}
```

**Arguments:**

| ID       | Type     | Description    |
|----------|----------|----------------|
| location | Location | Chunk Location |

<h3 id=if_game_container_has>
  <code>world::container_has</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Container Has an Item\
**Action type:** Action that checks the conditions\
**Description:** Checks if a container at a specific location has certain items in its inventory.

**Usage example:**
```ts
if(world::container_has([item("stick"), item("stick")], location(0,0,0,0,0), "ALL", "EXACTLY")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::container_has(items=[item("stick"), item("stick")], location=location(0,0,0,0,0), check_mode="ALL", comparison_mode="EXACTLY")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID              | Type                                                                                                                                                                                                   | Description                                                 |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| items           | Array\[Item\]                                                                                                                                                                                          | Items to Check<br/>The argument supports list decomposition |
| location        | Location                                                                                                                                                                                               | Location of container                                       |
| check_mode      | Marker<br/>**ALL** - All Items<br/>**ANY** - Any Items                                                                                                                                                 | Comparison Type                                             |
| comparison_mode | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**TYPE_ONLY** - Item type only | Comparison Mode                                             |

<h3 id=if_game_container_has_room_for_item>
  <code>world::container_has_room_for_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Container Has Room For Items\
**Action type:** Action that checks the conditions\
**Description:** Checks if a container at a specific location has room for items in its inventory.

**Usage example:**
```ts
if(world::container_has_room_for_item([item("stick"), item("stick")], location(0,0,0,0,0), "ALL")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::container_has_room_for_item(items=[item("stick"), item("stick")], location=location(0,0,0,0,0), check_mode="ALL")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID         | Type                                                   | Description                                                 |
|------------|--------------------------------------------------------|-------------------------------------------------------------|
| items      | Array\[Item\]                                          | Items to Check<br/>The argument supports list decomposition |
| location   | Location                                               | Location of container                                       |
| check_mode | Marker<br/>**ALL** - All Items<br/>**ANY** - Any Items | Comparison Type                                             |

<h3 id=if_game_damage_cause_equals>
  <code>world::damage_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Event Damage Source Equals\
**Action type:** Action that checks the conditions\
**Description:** Checks if the event's damage source is equal to the selected one.

**Usage example:**
```ts
if(world::damage_cause_equals("BLOCK_EXPLOSION")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::damage_cause_equals(cause="BLOCK_EXPLOSION")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| cause | Marker<br/>**BLOCK_EXPLOSION** - Block Explosion<br/>**CAMPFIRE** - Campfire<br/>**CONTACT** - Contact<br/>**CRAMMING** - Crowd<br/>**CUSTOM** - Custom<br/>**DRAGON_BREATH** - Dragon Breath<br/>**DROWNING** - Drowning<br/>**DRYOUT** - Dryout<br/>**ENTITY_ATTACK** - Entity Attack<br/>**ENTITY_EXPLOSION** - Entity Explosion<br/>**ENTITY_SWEEP_ATTACK** - Entity Sweep Attack.name=Entity Sweep Attack<br/>**FALL** - Fall<br/>**FALLING_BLOCK** - Falling Block<br/>**FIRE** - Direct Fire<br/>**FIRE_TICK** - Burning<br/>**FLY_INTO_WALL** - Kinetic Energy<br/>**FREEZE** - Freeze<br/>**HOT_FLOOR** - Magma<br/>**KILL** - Command<br/>**LAVA** - Lava<br/>**LIGHTNING** - Lightning<br/>**MAGIC** - Magic<br/>**MELTING** - Melting<br/>**POISON** - Poison<br/>**PROJECTILE** - Projectile<br/>**SONIC_BOOM** - Explosive Wave<br/>**STARVATION** - Hunger<br/>**SUFFOCATION** - Suffocation<br/>**SUICIDE** - Suicide (Sin)<br/>**THORNS** - Thorns<br/>**VOID** - Void<br/>**WITHER** - Wither<br/>**WORLD_BORDER** - World Border | Damage Source |

<h3 id=if_game_dummy>
  <code>world::is_dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Action type:** Action that checks the conditions\
**Description:** ...

**Usage example:**
```ts
if(world::is_dummy()){
    player::message("Condition is true");
}
```

<h3 id=if_game_event_attack_is_critical>
  <code>world::event_attack_is_critical</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Attack Was Critical\
**Action type:** Action that checks the conditions\
**Description:** Checks if an attack in an event was a critical attack.

**Usage example:**
```ts
if(world::event_attack_is_critical()){
    player::message("Condition is true");
}
```

<h3 id=if_game_event_block_equals>
  <code>world::event_block_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Event Block Equals\
**Action type:** Action that checks the conditions\
**Description:** Checks if the current event's block is equal to certain blocks.

**Usage example:**
```ts
if(world::event_block_equals(["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], [location(0,0,0,0,0), location(0,0,0,0,0)])){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::event_block_equals(blocks=["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], locations=[location(0,0,0,0,0), location(0,0,0,0,0)])){
    player::message("Condition is true");
}
```

**Arguments:**

| ID        | Type              | Description                                                           |
|-----------|-------------------|-----------------------------------------------------------------------|
| blocks    | Array\[Block\]    | Block Types to Check<br/>The argument supports list decomposition     |
| locations | Array\[Location\] | Block Locations to Check<br/>The argument supports list decomposition |

<h3 id=if_game_event_has_input>
  <code>world::event_has_input</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.if_game_event_has_input.name\
**Action type:** Action that checks the conditions\
**Description:** creative_plus.action.if_game_event_has_input.description\
**Work_with:**\
&nbsp;&nbsp;creative_plus.action.if_game_event_has_input.work_with.player_input_event\
&nbsp;&nbsp;creative_plus.action.if_game_event_has_input.work_with.player_vehicle_move\
&nbsp;&nbsp;creative_plus.action.if_game_event_has_input.work_with.player_vehicle_jump

**Usage example:**
```ts
if(world::event_has_input("FORWARD")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::event_has_input(input_type="FORWARD")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description                                                           |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| input_type | Marker<br/>**FORWARD** - creative_plus.action.if_game_event_has_input.argument.input_type.enum.forward.name<br/>**BACKWARDS** - creative_plus.action.if_game_event_has_input.argument.input_type.enum.backwards.name<br/>**LEFT** - creative_plus.action.if_game_event_has_input.argument.input_type.enum.left.name<br/>**RIGHT** - creative_plus.action.if_game_event_has_input.argument.input_type.enum.right.name<br/>**JUMP** - creative_plus.action.if_game_event_has_input.argument.input_type.enum.jump.name<br/>**SNEAK** - creative_plus.action.if_game_event_has_input.argument.input_type.enum.sneak.name<br/>**SPRINT** - creative_plus.action.if_game_event_has_input.argument.input_type.enum.sprint.name | creative_plus.action.if_game_event_has_input.argument.input_type.name |

<h3 id=if_game_event_is_canceled>
  <code>world::event_is_canceled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Event Cancelled\
**Action type:** Action that checks the conditions\
**Description:** Checks if the event has been cancelled.

**Usage example:**
```ts
if(world::event_is_canceled()){
    player::message("Condition is true");
}
```

<h3 id=if_game_event_item_equals>
  <code>world::event_item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Event Item Equals\
**Action type:** Action that checks the conditions\
**Description:** Checks if the current event item is equal to certain items.

**Usage example:**
```ts
if(world::event_item_equals([item("stick"), item("stick")], "EXACTLY")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::event_item_equals(items=[item("stick"), item("stick")], comparison_mode="EXACTLY")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID              | Type                                                                                                                                                                                                   | Description                                                 |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| items           | Array\[Item\]                                                                                                                                                                                          | Items to Check<br/>The argument supports list decomposition |
| comparison_mode | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**TYPE_ONLY** - Item type only | Comparison Mode                                             |

<h3 id=if_game_has_player>
  <code>world::has_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Player Online\
**Action type:** Action that checks the conditions\
**Description:** Checks if a certain player is in the game.

**Usage example:**
```ts
if(world::has_player(["names_or_uuids", "names_or_uuids"])){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::has_player(names_or_uuids=["names_or_uuids", "names_or_uuids"])){
    player::message("Condition is true");
}
```

**Arguments:**

| ID             | Type          | Description                                                          |
|----------------|---------------|----------------------------------------------------------------------|
| names_or_uuids | Array\[Text\] | Player Nickname or UUID<br/>The argument supports list decomposition |

<h3 id=if_game_heal_cause_equals>
  <code>world::heal_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Healing Source Equals\
**Action type:** Action that checks the conditions\
**Description:** Checks if the heal source is equal to the selected one.

**Usage example:**
```ts
if(world::heal_cause_equals("CUSTOM")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::heal_cause_equals(heal_cause="CUSTOM")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID         | Type                                                                                                                                                                                                                                                                                                                                                | Description       |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| heal_cause | Marker<br/>**CUSTOM** - Custom<br/>**EATING** - From Eating<br/>**ENDER_CRYSTAL** - From End Crystal<br/>**MAGIC** - From a potion or spell<br/>**MAGIC_REGEN** - Over time from potion or spell<br/>**REGEN** - Peaceful Healing<br/>**SATIATED** - Hunger Satisfied Heal<br/>**WITHER** - Wither effect<br/>**WITHER_SPAWN** - When Wither spawns | Source of Healing |

<h3 id=if_game_ignite_cause_equals>
  <code>world::ignite_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ignite Cause Equals\
**Action type:** Action that checks the conditions\
**Description:** Checks if the fire source is equal to the selected one.

**Usage example:**
```ts
if(world::ignite_cause_equals("ARROW")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::ignite_cause_equals(cause="ARROW")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID    | Type                                                                                                                                                                                                                                                                                             | Description |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| cause | Marker<br/>**ARROW** - Arrow<br/>**ENDER_CRYSTAL** - End Crystal<br/>**EXPLOSION** - Explosion<br/>**FALL** - Fall<br/>**FIREBALL** - Fire Bolt<br/>**FLINT_AND_STEEL** - Lighter<br/>**LAVA** - Lava<br/>**LIGHTNING** - Lightning<br/>**SPREAD** - Spread Fire<br/>**SUFFOCATION** - Suffocate | Fire Source |

<h3 id=if_game_instrument_equals>
  <code>world::instrument_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sound Instrument Equals\
**Action type:** Action that checks the conditions\
**Description:** Checks if the instrument in the event is equal to the selected one.

**Usage example:**
```ts
if(world::instrument_equals("BANJO")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::instrument_equals(instrument="BANJO")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| instrument | Marker<br/>**BANJO** - Banjo<br/>**BASS_DRUM** - Bass Drum<br/>**BASS_GUITAR** - Bass Guitar<br/>**BELL** - Bell<br/>**BIT** - Bit<br/>**CHIME** - Chimes<br/>**COW_BELL** - Cowbell<br/>**CREEPER** - Creeper<br/>**CUSTOM_HEAD** - Custom head<br/>**DIDGERIDOO** - Didgeridoo<br/>**DRAGON** - Ender-dragon<br/>**FLUTE** - Flute<br/>**GUITAR** - Guitar<br/>**IRON_XYLOPHONE** - Iron Xylophone<br/>**PIANO** - Piano<br/>**PIGLIN** - Piglin<br/>**PLING** - Pling<br/>**SKELETON** - Skeleton<br/>**SNARE_DRUM** - Snare Drum<br/>**STICKS** - Klaves<br/>**WITHER_SKELETON** - Wither-skeleton<br/>**XYLOPHONE** - Xylophone<br/>**ZOMBIE** - Zombie | Instrument  |

<h3 id=if_game_location_in_block>
  <code>world::location_in_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** If Location in Block\
**Action type:** Action that checks the conditions\
**Description:** Checks if the specified location is in a block.

**Usage example:**
```ts
if(world::location_in_block(location(0,0,0,0,0))){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::location_in_block(location=location(0,0,0,0,0))){
    player::message("Condition is true");
}
```

**Arguments:**

| ID       | Type     | Description       |
|----------|----------|-------------------|
| location | Location | Location to check |

<h3 id=if_game_sign_contains>
  <code>world::sign_contains</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sign Contains Text\
**Action type:** Action that checks the conditions\
**Description:** Checks if a sign at a given location contains the specified text.

**Usage example:**
```ts
if(world::sign_contains(location(0,0,0,0,0), ["texts", "texts"], "ANY", "ALL", "ALL")){
    player::message("Condition is true");
}

//Or dry by keywords

if(world::sign_contains(location=location(0,0,0,0,0), texts=["texts", "texts"], check_side="ANY", check_mode="ALL", lines="ALL")){
    player::message("Condition is true");
}
```

**Arguments:**

| ID         | Type                                                                                                                                                                                                                                                          | Description                                                |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| location   | Location                                                                                                                                                                                                                                                      | Sign location                                              |
| texts      | Array\[Text\]                                                                                                                                                                                                                                                 | Text to check<br/>The argument supports list decomposition |
| check_side | Marker<br/>**ANY** - Any<br/>**BACK** - Back<br/>**FRONT** - Front                                                                                                                                                                                            | Sign Side                                                  |
| check_mode | Marker<br/>**ALL** - creative_plus.action.if_game_sign_contains.argument.check_mode.enum.all.name<br/>**ANY** - creative_plus.action.if_game_sign_contains.argument.check_mode.enum.any.name<br/>**CONTAINS** - Content Compare<br/>**EQUALS** - Full Compare | Comparison Type                                            |
| lines      | Marker<br/>**ALL** - All Lines<br/>**ANY** - Any String<br/>**FIRST** - 1 line<br/>**FOURTH** - line 4<br/>**SECOND** - 2 line<br/>**THIRD** - 3 line                                                                                                         | Lines to Compare                                           |

