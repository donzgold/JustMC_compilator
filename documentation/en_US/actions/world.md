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

**Arguments:**

| **Name**       | **Type**                                                                                 | **Description** |
| -------------- | ---------------------------------------------------------------------------------------- | --------------- |
| `location`     | Location                                                                                 | Block Location  |
| `growth_stage` | Number                                                                                   | Growth Stage    |
| `growth_type`  | Marker<br/>**STAGE_NUMBER** - Growth Stage Number<br/>**PERCENTAGE** - Growth Percentage | Growth Type     |
<h3 id=game_bloom_skulk_catalyst>
  <code>world::bloom_skulk_catalyst</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Bloom Skulk Catalyst\
**Type:** Action without value\
**Description:** It extends the rock and the disposal to the location.
**Work_with:**\
&nbsp;&nbsp;Catalist rocks

**Usage example:** 
```ts
world::bloom_skulk_catalyst(location(0,0,0,0,0),location(0,0,0,0,0),1);
```

**Arguments:**

| **Name**         | **Type** | **Description**                  |
| ---------------- | -------- | -------------------------------- |
| `location`       | Location | The location of a rocky catalyst |
| `bloom_location` | Location | The final location               |
| `charge`         | Number   | The power of infection           |
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

**Arguments:**

| **Name**   | **Type** | **Description**                 |
| ---------- | -------- | ------------------------------- |
| `location` | Location | Block Location                  |
| `count`    | Number   | Number of Attempts to Fertilize |
<h3 id=game_break_block>
  <code>world::break_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Break Block\
**Type:** Action without value\
**Description:** Breaks blocks at the specified locations as if it were done by a Survival player with the right tool.

**Usage example:** 
```ts
world::break_block([location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE",item("stick"));
```

**Arguments:**

| **Name**    | **Type**                                               | **Description** |
| ----------- | ------------------------------------------------------ | --------------- |
| `locations` | list[Location]                                         | Block Locations |
| `drop_exp`  | Marker<br/>**TRUE** - Turn on<br/>**FALSE** - Turn off | Experience loss |
| `tool`      | Item                                                   | Tool            |
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
&nbsp;&nbsp;Any containers

**Usage example:** 
```ts
world::clear_container(location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**       |
| ---------- | -------- | --------------------- |
| `location` | Location | Location of Container |
<h3 id=game_clear_container_items>
  <code>world::clear_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Container Items\
**Type:** Action without value\
**Description:** Clears the specified items from a container.
**Work_with:**\
&nbsp;&nbsp;Any containers

**Usage example:** 
```ts
world::clear_container_items([item("stick"), item("stick")],location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**   | **Description**       |
| ---------- | ---------- | --------------------- |
| `items`    | list[Item] | Items                 |
| `location` | Location   | Location of container |
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

**Arguments:**

| **Name**   | **Type**       | **Description** |
| ---------- | -------------- | --------------- |
| `location` | list[Location] | Block Locations |
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

**Arguments:**

| **Name** | **Type** | **Description**        |
| -------- | -------- | ---------------------- |
| `pos_1`  | Location | Region Corner          |
| `pos_2`  | Location | Opposite Region Corner |
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

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `id`     | Text     | Scoreboard ID   |
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

**Arguments:**

| **Name**      | **Type**                                                  | **Description**        |
| ------------- | --------------------------------------------------------- | ---------------------- |
| `pos_1`       | Location                                                  | Region Corner          |
| `pos_2`       | Location                                                  | Opposite Region Corner |
| `target_pos`  | Location                                                  | Copy Location          |
| `paste_pos`   | Location                                                  | Paste Location         |
| `ignore_air`  | Marker<br/>**TRUE** - Ignore<br/>**FALSE** - Don't Ignore | Ignore Air             |
| `copy_entity` | Marker<br/>**TRUE** - Clone<br/>**FALSE** - Don't clone   | Clone Creatures        |
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

**Arguments:**

| **Name**   | **Type** | **Description**          |
| ---------- | -------- | ------------------------ |
| `location` | Location | Creation Location        |
| `power`    | Number   | Explosion Power (0 to 4) |
<h3 id=game_create_scoreboard>
  <code>world::create_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Scoreboard\
**Type:** Action without value\
**Description:** Creates a scoreboard with a specific ID. To display a scoreboard to a player, use the \"Show scoreboard\" action.

**Usage example:** 
```ts
world::create_scoreboard("id","display_name");
```

**Arguments:**

| **Name**       | **Type** | **Description** |
| -------------- | -------- | --------------- |
| `id`           | Text     | Scoreboard ID   |
| `display_name` | Text     | Title           |
<h3 id=game_dummy>
  <code>world::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action without value\
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
**Type:** Action without value\
**Description:** Fills a container at the selected location with the specified items.
**Work_with:**\
&nbsp;&nbsp;Any containers

**Usage example:** 
```ts
world::fill_container([item("stick"), item("stick")],location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**   | **Description**       |
| ---------- | ---------- | --------------------- |
| `items`    | list[Item] | Items to Fill         |
| `location` | Location   | Location of Container |
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

**Arguments:**

| **Name**    | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Description** |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `location`  | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Tree Location   |
| `tree_type` | Marker<br/>**TREE** - Regular Tree<br/>**BIG_TREE** - Big Tree<br/>**REDWOOD** - Regular Spruce<br/>**TALL_REDWOOD** - Tall Spruce<br/>**BIRCH** - Common Birch<br/>**JUNGLE** - Jungle Tree<br/>**SMALL_JUNGLE** - Small Jungle Tree<br/>**COCOA_TREE** - Cocoa Bean Jungle Tree<br/>**JUNGLE_BUSH** - Jungle Bush<br/>**RED_MUSHROOM** - Red Mushroom<br/>**BROWN_MUSHROOM** - Brown Mushroom<br/>**SWAMP** - Swamp Tree<br/>**ACACIA** - Acacia<br/>**DARK_OAK** - Dark Oak<br/>**MEGA_REDWOOD** - Great Sequoia<br/>**TALL_BIRCH** - Tall Birch<br/>**CHORUS_PLANT** - Chorus Tree<br/>**CRIMSON_FUNGUS** - Crimson Mushroom<br/>**WARPED_FUNGUS** - Warped Mushroom<br/>**AZALEA** - Azalea<br/>**MANGROVE** - Mangrove Tree<br/>**TALL_MANGROVE** - Tall Mangrove Tree<br/>**CHERRY** - Cherry | Tree Type       |
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

**Arguments:**

| **Name** | **Type**                                       | **Description** |
| -------- | ---------------------------------------------- | --------------- |
| `hide`   | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None | Hide Message    |
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

**Arguments:**

| **Name**   | **Type**                                                           | **Description**    |
| ---------- | ------------------------------------------------------------------ | ------------------ |
| `firework` | Item                                                               | Firework to Create |
| `location` | Location                                                           | Creation Location  |
| `movement` | Marker<br/>**UPWARDS** - Upwards<br/>**DIRECTIONAL** - Directional | Move               |
| `instant`  | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None                     | Instant Explosion  |
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

**Arguments:**

| **Name**      | **Type**        | **Description**                                                  |
| ------------- | --------------- | ---------------------------------------------------------------- |
| `projectile`  | Item            | Projectile to Launch                                             |
| `location`    | Location        | Launch Location                                                  |
| `speed`       | Number          | Projectile Speed                                                 |
| `inaccuracy`  | Number          | Projectile deflection (0 to keep the projectile flying straight) |
| `custom_name` | Text            | Projectile Name                                                  |
| `trail`       | Particle Effect | The trail the projectile will leave                              |
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

**Arguments:**

| **Name**   | **Type** | **Description**   |
| ---------- | -------- | ----------------- |
| `location` | Location | Location          |
| `times`    | Number   | Number of Updates |
<h3 id=game_remove_container_items>
  <code>world::remove_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Items From Container\
**Type:** Action without value\
**Description:** Removes the specified items from a container at the selected location.
**Work_with:**\
&nbsp;&nbsp;Any containers

**Usage example:** 
```ts
world::remove_container_items([item("stick"), item("stick")],location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**   | **Description**       |
| ---------- | ---------- | --------------------- |
| `items`    | list[Item] | Items                 |
| `location` | Location   | Location of Container |
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

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `id`     | Text     | Scoreboard ID   |
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

**Arguments:**

| **Name** | **Type** | **Description**      |
| -------- | -------- | -------------------- |
| `id`     | Text     | Scoreboard ID        |
| `text`   | Text     | Value text to remove |
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

**Arguments:**

| **Name** | **Type** | **Description**          |
| -------- | -------- | ------------------------ |
| `id`     | Text     | Scoreboard ID            |
| `score`  | Number   | Score of value to remove |
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

**Arguments:**

| **Name**    | **Type**    | **Description**           |
| ----------- | ----------- | ------------------------- |
| `old_block` | list[Block] | Blocks to Replace         |
| `pos_1`     | Location    | Region Corner             |
| `pos_2`     | Location    | Opposite Corner of Region |
| `new_block` | Block       | New Block                 |
<h3 id=game_replace_container_items>
  <code>world::replace_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Items in Container\
**Type:** Action without value\
**Description:** Replaces the specified items in a container at the selected location with a specific item.
**Work_with:**\
&nbsp;&nbsp;Any containers

**Usage example:** 
```ts
world::replace_container_items([item("stick"), item("stick")],location(0,0,0,0,0),item("stick"),1);
```

**Arguments:**

| **Name**   | **Type**   | **Description**            |
| ---------- | ---------- | -------------------------- |
| `items`    | list[Item] | Replaceable Items          |
| `location` | Location   | Location of container      |
| `replace`  | Item       | Replace Item               |
| `count`    | Number     | Number of Items to Replace |
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

**Arguments:**

| **Name**       | **Type**                                                                                               | **Description**    |
| -------------- | ------------------------------------------------------------------------------------------------------ | ------------------ |
| `url`          | Text                                                                                                   | URL                |
| `content_body` | Text                                                                                                   | Request Body       |
| `request_type` | Marker<br/>**GET** - GET<br/>**POST** - POST<br/>**PUT** - PUT<br/>**DELETE** - DELETE                 | Request Type       |
| `content_type` | Marker<br/>**TEXT_PLAIN** - Plain Text (text/plain)<br/>**APPLICATION_JSON** - JSON (application/json) | Media Request Type |
<h3 id=game_set_age>
  <code>world::set_age</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Age\
**Type:** Action without value\
**Description:** Sets the age of the block at the selected location.
**Work_with:**\
&nbsp;&nbsp;Any blocks that can have age

**Usage example:** 
```ts
world::set_age(location(0,0,0,0,0),1);
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `location` | Location | Block Location  |
| `tick`     | Number   | Ticks           |
<h3 id=game_set_block>
  <code>world::set_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block\
**Type:** Action without value\
**Description:** Sets the selected block type on selected locations.

**Usage example:** 
```ts
world::set_block([location(0,0,0,0,0), location(0,0,0,0,0)],"FALSE",item("stone"));
```

**Arguments:**

| **Name**        | **Type**                                                   | **Description**      |
| --------------- | ---------------------------------------------------------- | -------------------- |
| `locations`     | list[Location]                                             | Block Set Locations  |
| `update_blocks` | Marker<br/>**FALSE** - Do not update<br/>**TRUE** - Update | Update blocks around |
| `block`         | Block                                                      | Block                |
<h3 id=game_set_block_analogue_power>
  <code>world::set_block_analogue_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Redstone Signal Strength\
**Type:** Action without value\
**Description:** Sets the selected location to a specific signal strength.
**Work_with:**\
&nbsp;&nbsp;Activated blocks

**Usage example:** 
```ts
world::set_block_analogue_power(location(0,0,0,0,0),1);
```

**Arguments:**

| **Name**      | **Type** | **Description**     |
| ------------- | -------- | ------------------- |
| `location`    | Location | Block Location      |
| `power_level` | Number   | New Signal Strength |
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

**Arguments:**

| **Name**    | **Type** | **Description** |
| ----------- | -------- | --------------- |
| `location`  | Location | None            |
| `tag_name`  | Text     | None            |
| `tag_value` | Text     | None            |
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

**Arguments:**

| **Name**     | **Type** | **Description**   |
| ------------ | -------- | ----------------- |
| `location`   | Location | Block Location    |
| `block_data` | Text     | New Block Options |
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

**Arguments:**

| **Name** | **Type**                                               | **Description** |
| -------- | ------------------------------------------------------ | --------------- |
| `enable` | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled | Drop Blocks     |
<h3 id=game_set_block_powered>
  <code>world::set_block_powered</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Activate Block\
**Type:** Action without value\
**Description:** Activates a block at the selected location.
**Work_with:**\
&nbsp;&nbsp;Activated blocks

**Usage example:** 
```ts
world::set_block_powered(location(0,0,0,0,0),"TRUE");
```

**Arguments:**

| **Name**   | **Type**                                             | **Description** |
| ---------- | ---------------------------------------------------- | --------------- |
| `location` | Location                                             | Block Location  |
| `powered`  | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable | Activation      |
<h3 id=game_set_block_single_data>
  <code>world::set_block_single_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Block Single Data\
**Type:** Action without value\
**Description:** Sets the indicated parameter of the block at the location for a given value.

**Usage example:** 
```ts
world::set_block_single_data(location(0,0,0,0,0),"data","value");
```

**Arguments:**

| **Name**   | **Type** | **Description**           |
| ---------- | -------- | ------------------------- |
| `location` | Location | The location of the block |
| `data`     | Text     | Changed parameter         |
| `value`    | Text     | New meaning               |
<h3 id=game_set_brushable_block_item>
  <code>world::set_brushable_block_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item in Suspicious Block\
**Type:** Action without value\
**Description:** Sets an item into a suspicious block (sand, gravel) at the selected location.
**Work_with:**\
&nbsp;&nbsp;Suspicious sand\
&nbsp;&nbsp;Suspicious gravel

**Usage example:** 
```ts
world::set_brushable_block_item(location(0,0,0,0,0),item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `location` | Location | Block Location  |
| `item`     | Item     | Item            |
<h3 id=game_set_campfire_item>
  <code>world::set_campfire_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Campfire Item\
**Type:** Action without value\
**Description:** Sets an item to a campfire at the selected location.
**Work_with:**\
&nbsp;&nbsp;Fires

**Usage example:** 
```ts
world::set_campfire_item(location(0,0,0,0,0),item("stick"),1,"FIRST");
```

**Arguments:**

| **Name**       | **Type**                                                                                           | **Description**   |
| -------------- | -------------------------------------------------------------------------------------------------- | ----------------- |
| `location`     | Location                                                                                           | Campfire Location |
| `item`         | Item                                                                                               | Item              |
| `cooking_time` | Number                                                                                             | Cooking Time      |
| `slot`         | Marker<br/>**FIRST** - First<br/>**SECOND** - Second<br/>**THIRD** - Third<br/>**FOURTH** - Fourth | Slot              |
<h3 id=game_set_container>
  <code>world::set_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Items In Container\
**Type:** Action without value\
**Description:** Sets the specified items into a container at the selected location.
**Work_with:**\
&nbsp;&nbsp;Any containers

**Usage example:** 
```ts
world::set_container([item("stick"), item("stick")],[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

**Arguments:**

| **Name**   | **Type**       | **Description**       |
| ---------- | -------------- | --------------------- |
| `items`    | list[Item]     | Items to Set          |
| `location` | list[Location] | Location of Container |
<h3 id=game_set_container_lock>
  <code>world::set_container_lock</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Container Key\
**Type:** Action without value\
**Description:** Sets a specific key to a container at the selected location.\
**Additional info:**\
&nbsp;&nbsp;Any item with a specific name can serve as a container key.

**Usage example:** 
```ts
world::set_container_lock(location(0,0,0,0,0),"container_key");
```

**Arguments:**

| **Name**        | **Type** | **Description**       |
| --------------- | -------- | --------------------- |
| `location`      | Location | Location of Container |
| `container_key` | Text     | Container Key Name    |
<h3 id=game_set_container_name>
  <code>world::set_container_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Container Name\
**Type:** Action without value\
**Description:** Sets the name of the container at the selected location.
**Work_with:**\
&nbsp;&nbsp;Any containers

**Usage example:** 
```ts
world::set_container_name(location(0,0,0,0,0),"name");
```

**Arguments:**

| **Name**   | **Type** | **Description**       |
| ---------- | -------- | --------------------- |
| `location` | Location | Location of container |
| `name`     | Text     | Container Name        |
<h3 id=game_set_decorate_pot_sherd>
  <code>world::set_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Decorate Pot Sherd\
**Type:** Action without value\
**Description:** Sets the indicated cherries of the selected side of the jug in the specified location.
**Work_with:**\
&nbsp;&nbsp;Vases

**Usage example:** 
```ts
world::set_decorate_pot_sherd(location(0,0,0,0,0),item("stick"),"BACK");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                       | **Description**          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| `location` | Location                                                                                                                       | The location of the jug  |
| `item`     | Item                                                                                                                           | Clousse for installation |
| `side`     | Marker<br/>**BACK** - The back side<br/>**LEFT** - The left side<br/>**RIGHT** - The right side<br/>**FRONT** - The front side | Side of the jug          |
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

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `damage` | Number   | Damage Amount   |
<h3 id=game_set_event_exhaustion>
  <code>world::set_event_exhaustion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Exhaustion\
**Type:** Action without value\
**Description:** Establishes the value of exhaustion associated with this event.
**Work_with:**\
&nbsp;&nbsp;Event of exhaustion

**Usage example:** 
```ts
world::set_event_exhaustion(1);
```

**Arguments:**

| **Name**     | **Type** | **Description**          |
| ------------ | -------- | ------------------------ |
| `exhaustion` | Number   | The amount of exhaustion |
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

**Arguments:**

| **Name**     | **Type** | **Description**      |
| ------------ | -------- | -------------------- |
| `experience` | Number   | Amount of Experience |
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

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `heal`   | Number   | Heal Amount     |
<h3 id=game_set_event_item>
  <code>world::set_event_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Item\
**Type:** Action without value\
**Description:** Sets the item associated with this event.
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
&nbsp;&nbsp;Witch Throws Potion Event

**Usage example:** 
```ts
world::set_event_item(item("stick"));
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `item`   | Item     | New Event Item  |
<h3 id=game_set_event_items>
  <code>world::set_event_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Items\
**Type:** Action without value\
**Description:** Sets objects related to this event.
**Work_with:**\
&nbsp;&nbsp;The event of the subject in the inventory

**Usage example:** 
```ts
world::set_event_items([item("stick"), item("stick")]);
```

**Arguments:**

| **Name** | **Type**   | **Description**        |
| -------- | ---------- | ---------------------- |
| `items`  | list[Item] | Items for installation |
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

**Arguments:**

| **Name**  | **Type**                                     | **Description** |
| --------- | -------------------------------------------- | --------------- |
| `allowed` | Marker<br/>**TRUE** - Yes<br/>**FALSE** - No | Allow Movement  |
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

**Arguments:**

| **Name**     | **Type** | **Description**         |
| ------------ | -------- | ----------------------- |
| `projectile` | Item     | Projectile              |
| `name`       | Text     | Projectile Display Name |
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

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `sound`  | Sound    | Playable sound  |
<h3 id=game_set_event_source_slot>
  <code>world::set_event_source_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Source Slot\
**Type:** Action without value\
**Description:** Sets the initial slot associated with this event.
**Work_with:**\
&nbsp;&nbsp;The event of the subject in the inventory

**Usage example:** 
```ts
world::set_event_source_slot(1);
```

**Arguments:**

| **Name**      | **Type** | **Description**       |
| ------------- | -------- | --------------------- |
| `source_slot` | Number   | Slot for installation |
<h3 id=game_set_event_target_slot>
  <code>world::set_event_target_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Event Target Slot\
**Type:** Action without value\
**Description:** It sets the final slot associated with this event.
**Work_with:**\
&nbsp;&nbsp;The event of the subject in the inventory

**Usage example:** 
```ts
world::set_event_target_slot(1);
```

**Arguments:**

| **Name** | **Type** | **Description**       |
| -------- | -------- | --------------------- |
| `target` | Number   | Slot for installation |
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

**Arguments:**

| **Name**      | **Type** | **Description** |
| ------------- | -------- | --------------- |
| `information` | Text     | Additional Tags |
<h3 id=game_set_furnace_cook_time>
  <code>world::set_furnace_cook_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Furnace Cooking Time\
**Type:** Action without value\
**Description:** Sets the cooking time for the oven at the selected location.
**Work_with:**\
&nbsp;&nbsp;Furnaces\
&nbsp;&nbsp;Blast furnaces\
&nbsp;&nbsp;Smokers

**Usage example:** 
```ts
world::set_furnace_cook_time(location(0,0,0,0,0),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**  |
| ---------- | -------- | ---------------- |
| `location` | Location | Furnace Location |
| `time`     | Number   | Cooking Time     |
<h3 id=game_set_item_in_container_slot>
  <code>world::set_item_in_container_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item In Container Slot\
**Type:** Action without value\
**Description:** Sets an item in the specified container slot at the selected location.
**Work_with:**\
&nbsp;&nbsp;Any containers

**Usage example:** 
```ts
world::set_item_in_container_slot(location(0,0,0,0,0),item("stick"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**       |
| ---------- | -------- | --------------------- |
| `location` | Location | Location of Container |
| `item`     | Item     | Item                  |
| `slot`     | Number   | Slot Number           |
<h3 id=game_set_lectern_book>
  <code>world::set_lectern_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Book In Lectern\
**Type:** Action without value\
**Description:** Sets a book in the lectern at the selected location.
**Work_with:**\
&nbsp;&nbsp;Departments

**Usage example:** 
```ts
world::set_lectern_book(location(0,0,0,0,0),item("stick"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `location` | Location | Pulpit Location |
| `item`     | Item     | Book to Set     |
| `page`     | Number   | Page            |
<h3 id=game_set_player_head>
  <code>world::set_player_head</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Head\
**Type:** Action without value\
**Description:** Sets the player's head at the selected location.
**Work_with:**\
&nbsp;&nbsp;Player heads

**Usage example:** 
```ts
world::set_player_head(location(0,0,0,0,0),"name_or_uuid","NAME_OR_UUID");
```

**Arguments:**

| **Name**       | **Type**                                                                                     | **Description**     |
| -------------- | -------------------------------------------------------------------------------------------- | ------------------- |
| `location`     | Location                                                                                     | Head Location       |
| `name_or_uuid` | Text                                                                                         | Player name or UUID |
| `receive_type` | Marker<br/>**NAME_OR_UUID** - Name or uuid player<br/>**VALUE** - The parameter "Value" skin | Type of value       |
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

**Arguments:**

| **Name** | **Type** | **Description**        |
| -------- | -------- | ---------------------- |
| `block`  | Block    | Block                  |
| `pos_1`  | Location | Region Corner          |
| `pos_2`  | Location | Opposite Region Corner |
<h3 id=game_set_scoreboard_line>
  <code>world::set_scoreboard_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Line\
**Type:** Action without value\
**Description:** Sets a line in a scorchor.

**Usage example:** 
```ts
world::set_scoreboard_line("id","line","display",1,"format_content","BLANK");

#Or from the object

"id".set_scoreboard_line("line","display",1,"format_content","BLANK");
```

**Arguments:**

| **Name**         | **Type**                                                                                          | **Description**        |
| ---------------- | ------------------------------------------------------------------------------------------------- | ---------------------- |
| `id`             | Text                                                                                              | ID Skorboard           |
| `line`           | Text                                                                                              | ID lines               |
| `display`        | Text                                                                                              | Displayed text         |
| `score`          | Number                                                                                            | Meaning                |
| `format_content` | Text                                                                                              | The format of the text |
| `format`         | Marker<br/>**BLANK** - Empty<br/>**FIXED** - Text<br/>**STYLED** - Style<br/>**RESET** - Ordinary | Type of format         |
<h3 id=game_set_scoreboard_line_display>
  <code>world::set_scoreboard_line_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Line Display\
**Type:** Action without value\
**Description:** The displayed text sets the specified scorchor line.

**Usage example:** 
```ts
world::set_scoreboard_line_display("id","line","display");

#Or from the object

"id".set_scoreboard_line_display("line","display");
```

**Arguments:**

| **Name**  | **Type** | **Description** |
| --------- | -------- | --------------- |
| `id`      | Text     | ID Skorboard    |
| `line`    | Text     | ID lines        |
| `display` | Text     | Displayed text  |
<h3 id=game_set_scoreboard_line_format>
  <code>world::set_scoreboard_line_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Line Format\
**Type:** Action without value\
**Description:** Establishes the formatting of the text of the specified Scorbox line.

**Usage example:** 
```ts
world::set_scoreboard_line_format("id","line","format_content","BLANK");

#Or from the object

"id".set_scoreboard_line_format("line","format_content","BLANK");
```

**Arguments:**

| **Name**         | **Type**                                                                                          | **Description**        |
| ---------------- | ------------------------------------------------------------------------------------------------- | ---------------------- |
| `id`             | Text                                                                                              | ID Skorboard           |
| `line`           | Text                                                                                              | ID lines               |
| `format_content` | Text                                                                                              | The format of the text |
| `format`         | Marker<br/>**BLANK** - Empty<br/>**FIXED** - Text<br/>**STYLED** - Style<br/>**RESET** - Ordinary | Type of format         |
<h3 id=game_set_scoreboard_number_format>
  <code>world::set_scoreboard_number_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Scoreboard Number Format\
**Type:** Action without value\
**Description:** Establishes formatting values for a scorching.

**Usage example:** 
```ts
world::set_scoreboard_number_format("id","format_content","BLANK");

#Or from the object

"id".set_scoreboard_number_format("format_content","BLANK");
```

**Arguments:**

| **Name**         | **Type**                                                                                          | **Description**        |
| ---------------- | ------------------------------------------------------------------------------------------------- | ---------------------- |
| `id`             | Text                                                                                              | ID Skorboard           |
| `format_content` | Text                                                                                              | The format of the text |
| `format`         | Marker<br/>**BLANK** - Empty<br/>**FIXED** - Text<br/>**STYLED** - Style<br/>**RESET** - Ordinary | Type of format         |
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

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `id`     | Text     | Scoreboard ID   |
| `text`   | Text     | Display Text    |
| `score`  | Number   | Score           |
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

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `id`     | Text     | Scoreboard ID   |
| `title`  | Text     | New Title       |
<h3 id=game_set_sculk_shrieker_can_summon>
  <code>world::set_sculk_shrieker_can_summon</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sculk Shrieker Can Summon\
**Type:** Action without value\
**Description:** It sets the indicated rock crkun with the possibility of calling Warden.
**Work_with:**\
&nbsp;&nbsp;Sculk shriekers

**Usage example:** 
```ts
world::set_sculk_shrieker_can_summon(location(0,0,0,0,0),"TRUE");
```

**Arguments:**

| **Name**     | **Type**                                                                | **Description**                 |
| ------------ | ----------------------------------------------------------------------- | ------------------------------- |
| `location`   | Location                                                                | The location of the rock-crkuna |
| `can_summon` | Marker<br/>**TRUE** - It can be called<br/>**FALSE** - Cannot be called | The possibility of calling      |
<h3 id=game_set_sculk_shrieker_shrieking>
  <code>world::set_sculk_shrieker_shrieking</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sculk Shrieker Shrieking\
**Type:** Action without value\
**Description:** Establishes the specified rock-ricked condition.
**Work_with:**\
&nbsp;&nbsp;Sculk shriekers

**Usage example:** 
```ts
world::set_sculk_shrieker_shrieking(location(0,0,0,0,0),"TRUE");
```

**Arguments:**

| **Name**    | **Type**                                                      | **Description**                 |
| ----------- | ------------------------------------------------------------- | ------------------------------- |
| `location`  | Location                                                      | The location of the rock-crkuna |
| `shrieking` | Marker<br/>**TRUE** - Screaming<br/>**FALSE** - Not screaming | State                           |
<h3 id=game_set_sculk_shrieker_warning_level>
  <code>world::set_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sculk Shrieker Warning Level\
**Type:** Action without value\
**Description:** Sets the indicated rock rod level of danger.
**Work_with:**\
&nbsp;&nbsp;Rock-rockers

**Usage example:** 
```ts
world::set_sculk_shrieker_warning_level(location(0,0,0,0,0),1);
```

**Arguments:**

| **Name**        | **Type** | **Description**                 |
| --------------- | -------- | ------------------------------- |
| `location`      | Location | The location of the rock-crkuna |
| `warning_level` | Number   | The level of danger             |
<h3 id=game_set_sign_text>
  <code>world::set_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sign Text\
**Type:** Action without value\
**Description:** Sets the sign text at the selected location.

**Usage example:** 
```ts
world::set_sign_text(location(0,0,0,0,0),"text",1,"FRONT");
```

**Arguments:**

| **Name**   | **Type**                                                           | **Description** |
| ---------- | ------------------------------------------------------------------ | --------------- |
| `location` | Location                                                           | Sign location   |
| `text`     | Text                                                               | Text to set     |
| `line`     | Number                                                             | Line            |
| `side`     | Marker<br/>**FRONT** - Front<br/>**BACK** - Back<br/>**ALL** - All | Sign Side       |
<h3 id=game_set_sign_text_color>
  <code>world::set_sign_text_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sign Text Color\
**Type:** Action without value\
**Description:** Sets the color of sign text at the selected location.
**Work_with:**\
&nbsp;&nbsp;Signs

**Usage example:** 
```ts
world::set_sign_text_color(location(0,0,0,0,0),"FRONT","WHITE","TRUE");
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                                                                                                                                                                                                         | **Description** |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `location`        | Location                                                                                                                                                                                                                                                                                                                                                                         | Sign location   |
| `side`            | Marker<br/>**FRONT** - Front<br/>**BACK** - Back<br/>**ALL** - All                                                                                                                                                                                                                                                                                                               | Sign Side       |
| `sign_text_color` | Marker<br/>**WHITE** - White<br/>**ORANGE** - Orange<br/>**MAGENTA** - Magenta<br/>**LIGHT_BLUE** - Blue<br/>**YELLOW** - Yellow<br/>**LIME** - Lime<br/>**PINK** - Pink<br/>**GRAY** - Grey<br/>**LIGHT_GRAY** - Light Gray<br/>**CYAN** - Cyan<br/>**PURPLE** - Purple<br/>**BLUE** - Blue<br/>**BROWN** - Brown<br/>**GREEN** - Green<br/>**RED** - Red<br/>**BLACK** - Black | Sign Color      |
| `glowing`         | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable                                                                                                                                                                                                                                                                                                                             | Text Glow       |
<h3 id=game_set_sign_waxed>
  <code>world::set_sign_waxed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sign Waxed\
**Type:** Action without value\
**Description:** Sets the waxedness of the sign at the selected location.
**Work_with:**\
&nbsp;&nbsp;Signs

**Usage example:** 
```ts
world::set_sign_waxed(location(0,0,0,0,0),"TRUE");
```

**Arguments:**

| **Name**   | **Type**                                             | **Description**     |
| ---------- | ---------------------------------------------------- | ------------------- |
| `location` | Location                                             | Sign Waxed Location |
| `waxed`    | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable | Waxed               |
<h3 id=game_set_spawner_entity>
  <code>world::set_spawner_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Spawner Entity\
**Type:** Action without value\
**Description:** It sets spavner in the selected location of the entity inside.
**Work_with:**\
&nbsp;&nbsp;Spawner

**Usage example:** 
```ts
world::set_spawner_entity(location(0,0,0,0,0),item("stick"));

#Or from the object

location(0,0,0,0,0).set_spawner_entity(item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**             |
| ---------- | -------- | --------------------------- |
| `location` | Location | The location of the spavner |
| `entity`   | Item     | The egg is an entity        |
<h3 id=game_set_world_difficulty>
  <code>world::set_world_difficulty</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Difficulty\
**Type:** Action without value\
**Description:** Sets a specific world difficulty.

**Usage example:** 
```ts
world::set_world_difficulty("PEACEFUL");
```

**Arguments:**

| **Name**     | **Type**                                                                                           | **Description** |
| ------------ | -------------------------------------------------------------------------------------------------- | --------------- |
| `difficulty` | Marker<br/>**PEACEFUL** - Peaceful<br/>**EASY** - Easy<br/>**NORMAL** - Normal<br/>**HARD** - Hard | Difficulty      |
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

**Arguments:**

| **Name**   | **Type** | **Description**                      |
| ---------- | -------- | ------------------------------------ |
| `distance` | Number   | Simulation Distance in Chunks (2-32) |
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

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `time`   | Number   | Time in ticks   |
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

**Arguments:**

| **Name**           | **Type**                                                                              | **Description** |
| ------------------ | ------------------------------------------------------------------------------------- | --------------- |
| `weather_type`     | Marker<br/>**CLEAR** - Clear<br/>**RAINING** - Raining<br/>**THUNDER** - Thunderstorm | Weather Type    |
| `weather_duration` | Number                                                                                | Duration        |
<h3 id=game_spawn_armor_stand>
  <code>world::spawn_armor_stand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Armor Stand\
**Type:** Action without value\
**Description:** Spawns an armor stand at the specified location.

**Usage example:** 
```ts
world::spawn_armor_stand(item("stick"),item("stick"),"TRUE","TRUE",item("stick"),item("stick"),location(0,0,0,0,0),"custom_name","TRUE","TRUE",item("stick"),item("stick"),"TRUE","TRUE");
```

**Arguments:**

| **Name**      | **Type**                                               | **Description** |
| ------------- | ------------------------------------------------------ | --------------- |
| `helmet`      | Item                                                   | Headgear        |
| `boots`       | Item                                                   | Boots           |
| `gravity`     | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable   | Set Gravity     |
| `marker`      | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled | Marker Mode     |
| `chestplate`  | Item                                                   | Chestplate      |
| `right_hand`  | Item                                                   | Right Hand Item |
| `location`    | Location                                               | Spawn Location  |
| `custom_name` | Text                                                   | Stand name      |
| `small`       | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable   | Make Small      |
| `show_arms`   | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable   | Show Arms       |
| `leggings`    | Item                                                   | Leggings        |
| `left_hand`   | Item                                                   | Left Hand Item  |
| `base_plate`  | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable   | Slab Display    |
| `invisible`   | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable   | Invisible       |
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

**Arguments:**

| **Name**         | **Type** | **Description** |
| ---------------- | -------- | --------------- |
| `spawn_location` | Location | Spawn Location  |
| `custom_name`    | Text     | Name            |
| `block`          | Block    | Display Block   |
<h3 id=game_spawn_effect_cloud>
  <code>world::spawn_effect_cloud</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Effect Cloud\
**Type:** Action without value\
**Description:** Spawns a cloud of misty potion that infuses the effects of the entities in it.

**Usage example:** 
```ts
world::spawn_effect_cloud(location(0,0,0,0,0),[potion("slow_falling"), potion("slow_falling")],particle("fire"),1,"custom_name",2);
```

**Arguments:**

| **Name**      | **Type**        | **Description** |
| ------------- | --------------- | --------------- |
| `location`    | Location        | Spawn Location  |
| `effects`     | list[Potion]    | Potion Effects  |
| `particle`    | Particle Effect | Cloud Particles |
| `duration`    | Number          | Duration        |
| `custom_name` | Text            | Name            |
| `radius`      | Number          | Cloud Radius    |
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

**Arguments:**

| **Name**      | **Type**                                     | **Description**  |
| ------------- | -------------------------------------------- | ---------------- |
| `location`    | Location                                     | Spawn Location   |
| `custom_name` | Text                                         | Name             |
| `show_bottom` | Marker<br/>**TRUE** - Yes<br/>**FALSE** - No | Spawn Foundation |
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

**Arguments:**

| **Name**      | **Type** | **Description** |
| ------------- | -------- | --------------- |
| `location`    | Location | Spawn Location  |
| `custom_name` | Text     | Name            |
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

**Arguments:**

| **Name**            | **Type** | **Description**   |
| ------------------- | -------- | ----------------- |
| `location`          | Location | Spawn Location    |
| `experience_amount` | Number   | Experience Amount |
| `custom_name`       | Text     | Name              |
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

**Arguments:**

| **Name**          | **Type**                                                                             | **Description** |
| ----------------- | ------------------------------------------------------------------------------------ | --------------- |
| `location`        | Location                                                                             | Spawn Location  |
| `destination`     | Location                                                                             | Destination     |
| `lifespan`        | Number                                                                               | Lifespan        |
| `custom_name`     | Text                                                                                 | Name            |
| `end_of_lifespan` | Marker<br/>**DROP** - Drop an item<br/>**SHATTER** - Shatter<br/>**RANDOM** - Random | At End          |
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

**Arguments:**

| **Name**        | **Type**                                       | **Description** |
| --------------- | ---------------------------------------------- | --------------- |
| `block`         | Block                                          | Block to Spawn  |
| `location`      | Location                                       | Spawn Location  |
| `name`          | Text                                           | Name            |
| `should_expire` | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None | Must Vanish     |
<h3 id=game_spawn_interaction_entity>
  <code>world::spawn_interaction_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Interaction Entity\
**Type:** Action without value\
**Description:** Spawns an interaction entity at the specified location\
**Additional info:**\
&nbsp;&nbsp;Detect interaction with entity attack and click events.

**Usage example:** 
```ts
world::spawn_interaction_entity(location(0,0,0,0,0),"custom_name",1,2,"TRUE");
```

**Arguments:**

| **Name**      | **Type**                                             | **Description** |
| ------------- | ---------------------------------------------------- | --------------- |
| `location`    | Location                                             | Spawn Location  |
| `custom_name` | Text                                                 | Name            |
| `width`       | Number                                               | Horizontal Size |
| `height`      | Number                                               | Vertical size   |
| `responsive`  | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable | Responsive      |
<h3 id=game_spawn_item>
  <code>world::spawn_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Item\
**Type:** Action without value\
**Description:** Spawns an item at the specified location with the selected options.

**Usage example:** 
```ts
world::spawn_item("TRUE",location(0,0,0,0,0),item("stick"),"custom_name","TRUE","TRUE");
```

**Arguments:**

| **Name**            | **Type**                                       | **Description**                     |
| ------------------- | ---------------------------------------------- | ----------------------------------- |
| `can_mob_pickup`    | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None | Can mobs pick up an item            |
| `location`          | Location                                       | Spawn Location                      |
| `item`              | Item                                           | Item to Spawn                       |
| `custom_name`       | Text                                           | Name                                |
| `can_player_pickup` | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None | Whether players can pick up an item |
| `apply_motion`      | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None | Set Item Motion on Spawn            |
<h3 id=game_spawn_item_display>
  <code>world::spawn_item_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Item Display\
**Type:** Action without value\
**Description:** Spawns an item display at the specified location

**Usage example:** 
```ts
world::spawn_item_display(location(0,0,0,0,0),"custom_name",item("stick"));
```

**Arguments:**

| **Name**         | **Type** | **Description** |
| ---------------- | -------- | --------------- |
| `spawn_location` | Location | Spawn Location  |
| `custom_name`    | Text     | Name            |
| `displayed_item` | Item     | Displayed Item  |
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

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `location` | Location | Spawn Location  |
<h3 id=game_spawn_mob>
  <code>world::spawn_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Entity\
**Type:** Action without value\
**Description:** Spawns a mob at the specified location with the selected options.

**Usage example:** 
```ts
world::spawn_mob([potion("slow_falling"), potion("slow_falling")],item("stick"),item("stick"),item("stick"),location(0,0,0,0,0),item("stick"),1,item("stick"),"custom_name",item("stick"),"TRUE",item("stick"));
```

**Arguments:**

| **Name**            | **Type**                                             | **Description**    |
| ------------------- | ---------------------------------------------------- | ------------------ |
| `potion_effects`    | list[Potion]                                         | Effects            |
| `main_hand`         | Item                                                 | Main Hand Item     |
| `mob`               | Item                                                 | Mob Type           |
| `helmet`            | Item                                                 | Headgear           |
| `location`          | Location                                             | Spawn Location     |
| `chestplate`        | Item                                                 | Chestplate         |
| `health`            | Number                                               | Amount of Health   |
| `leggings`          | Item                                                 | Leggings           |
| `custom_name`       | Text                                                 | Name               |
| `boots`             | Item                                                 | Boots              |
| `natural_equipment` | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable | Standard Equipment |
| `off_hand`          | Item                                                 | Offhand Item       |
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

**Arguments:**

| **Name**        | **Type** | **Description**         |
| --------------- | -------- | ----------------------- |
| `location`      | Location | Spawn Location          |
| `tnt_power`     | Number   | Dynamite Power (0 to 4) |
| `fuse_duration` | Number   | Explosion Delay Time    |
| `custom_name`   | Text     | Name                    |
| `block`         | Block    | Block for disguise      |
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

**Arguments:**

| **Name**      | **Type** | **Description** |
| ------------- | -------- | --------------- |
| `location`    | Location | Spawn Location  |
| `custom_name` | Text     | Name            |
<h3 id=game_spawn_text_display>
  <code>world::spawn_text_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spawn Text Display\
**Type:** Action without value\
**Description:** Spawns a text renderer at the specified location

**Usage example:** 
```ts
world::spawn_text_display(location(0,0,0,0,0),["displayed_text", "displayed_text"],"custom_name","SPACES");
```

**Arguments:**

| **Name**         | **Type**                                                                                                       | **Description** |
| ---------------- | -------------------------------------------------------------------------------------------------------------- | --------------- |
| `spawn_location` | Location                                                                                                       | Spawn Location  |
| `displayed_text` | list[Text]                                                                                                     | Displayed Text  |
| `custom_name`    | Text                                                                                                           | Name            |
| `merging_mode`   | Marker<br/>**SPACES** - Space Separation<br/>**CONCATENATION** - Merge<br/>**SEPARATE_LINES** - Separate Lines | Merge Text      |
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

**Arguments:**

| **Name**      | **Type** | **Description** |
| ------------- | -------- | --------------- |
| `vehicle`     | Item     | Vehicle Type    |
| `location`    | Location | Spawn Location  |
| `custom_name` | Text     | Name            |
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

**Name:** Update Adjacent Block\
**Type:** Action without value\
**Description:** Updates neighboring blocks in the indicated location if the block in the location is not air.The unit on its location is not updated, but can be updated from the neighboring ones.

**Usage example:** 
```ts
world::update_block(location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `location` | Location | Location        |
<h3 id=if_game_block_equals>
  <code>world::block_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Block Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a block at a specific location is a specific block type.

**Usage example:** 
```ts
if(world::block_equals([item("stone"), item("stone")],location(0,0,0,0,0)){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**   | **Type**    | **Description**     |
| ---------- | ----------- | ------------------- |
| `blocks`   | list[Block] | Block Type to Check |
| `location` | Location    | Block Location      |
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

**Arguments:**

| **Name**     | **Type**                                                                                                                                       | **Description**       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `locations`  | list[Location]                                                                                                                                 | Block Location        |
| `power_mode` | Marker<br/>**DIRECT** - Direct Powered<br/>**DIRECT** - Direct Powered<br/>**INDIRECT** - Indirect Powered<br/>**INDIRECT** - Indirect Powered | Redstone Powered Type |
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

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `location` | Location | Chunk Location  |
<h3 id=if_game_container_has>
  <code>world::container_has</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Container Has an Item\
**Type:** Action that checks the conditions\
**Description:** Checks if a container at a specific location has certain items in its inventory.

**Usage example:** 
```ts
if(world::container_has([item("stick"), item("stick")],location(0,0,0,0,0),"ANY","IGNORE_STACK_SIZE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                               | **Description**       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| `items`           | list[Item]                                                                                                                                                                                             | Items to Check        |
| `location`        | Location                                                                                                                                                                                               | Location of container |
| `check_mode`      | Marker<br/>**ANY** - Any Items<br/>**ALL** - All Items                                                                                                                                                 | Comparison Type       |
| `comparison_mode` | Marker<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**EXACTLY** - Full Comparison<br/>**TYPE_ONLY** - Item type only | Comparison Mode       |
<h3 id=if_game_container_has_room_for_item>
  <code>world::container_has_room_for_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Container Has Room For Items\
**Type:** Action that checks the conditions\
**Description:** Checks if a container at a specific location has room for items in its inventory.

**Usage example:** 
```ts
if(world::container_has_room_for_item([item("stick"), item("stick")],location(0,0,0,0,0),"ANY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                               | **Description**       |
| ------------ | ------------------------------------------------------ | --------------------- |
| `items`      | list[Item]                                             | Items to Check        |
| `location`   | Location                                               | Location of container |
| `check_mode` | Marker<br/>**ANY** - Any Items<br/>**ALL** - All Items | Comparison Type       |
<h3 id=if_game_damage_cause_equals>
  <code>world::damage_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Event Damage Source Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the event's damage source is equal to the selected one.

**Usage example:** 
```ts
if(world::damage_cause_equals("KILL"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Description** |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `cause`  | Marker<br/>**KILL** - Command<br/>**WORLD_BORDER** - World Border<br/>**CONTACT** - Contact<br/>**ENTITY_ATTACK** - Entity Attack<br/>**ENTITY_SWEEP_ATTACK** - Entity Sweep Attack.name=Entity Sweep Attack<br/>**PROJECTILE** - Projectile<br/>**SUFFOCATION** - Suffocation<br/>**FALL** - Fall<br/>**FIRE** - Direct Fire<br/>**FIRE_TICK** - Burning<br/>**MELTING** - Melting<br/>**LAVA** - Lava<br/>**DROWNING** - Drowning<br/>**BLOCK_EXPLOSION** - Block Explosion<br/>**ENTITY_EXPLOSION** - Entity Explosion<br/>**VOID** - Void<br/>**LIGHTNING** - Lightning<br/>**SUICIDE** - Suicide (Sin)<br/>**STARVATION** - Hunger<br/>**POISON** - Poison<br/>**MAGIC** - Magic<br/>**WITHER** - Wither<br/>**FALLING_BLOCK** - Falling Block<br/>**THORNS** - Thorns<br/>**DRAGON_BREATH** - Dragon Breath<br/>**CUSTOM** - Custom<br/>**FLY_INTO_WALL** - Kinetic Energy<br/>**HOT_FLOOR** - Magma<br/>**CRAMMING** - Crowd<br/>**DRYOUT** - Dryout<br/>**FREEZE** - Freeze<br/>**SONIC_BOOM** - Explosive Wave | Damage Source   |
<h3 id=if_game_dummy>
  <code>world::is_dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action that checks the conditions\
**Description:** ...

**Usage example:** 
```ts
if(world::is_dummy(){
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

**Arguments:**

| **Name**    | **Type**       | **Description**          |
| ----------- | -------------- | ------------------------ |
| `blocks`    | list[Block]    | Block Types to Check     |
| `locations` | list[Location] | Block Locations to Check |
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
if(world::event_item_equals([item("stick"), item("stick")],"IGNORE_STACK_SIZE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                               | **Description** |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `items`           | list[Item]                                                                                                                                                                                             | Items to Check  |
| `comparison_mode` | Marker<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**EXACTLY** - Full Comparison<br/>**TYPE_ONLY** - Item type only | Comparison Mode |
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

**Arguments:**

| **Name**         | **Type**   | **Description**         |
| ---------------- | ---------- | ----------------------- |
| `names_or_uuids` | list[Text] | Player Nickname or UUID |
<h3 id=if_game_heal_cause_equals>
  <code>world::heal_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Healing Source Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the heal source is equal to the selected one.

**Usage example:** 
```ts
if(world::heal_cause_equals("REGEN"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                                                                                                                                                                                                                            | **Description**   |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `heal_cause` | Marker<br/>**REGEN** - Peaceful Healing<br/>**SATIATED** - Hunger Satisfied Heal<br/>**EATING** - From Eating<br/>**ENDER_CRYSTAL** - From End Crystal<br/>**MAGIC** - From a potion or spell<br/>**MAGIC_REGEN** - Over time from potion or spell<br/>**WITHER_SPAWN** - When Wither spawns<br/>**WITHER** - Wither effect<br/>**CUSTOM** - Custom | Source of Healing |
<h3 id=if_game_ignite_cause_equals>
  <code>world::ignite_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ignite Cause Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the fire source is equal to the selected one.

**Usage example:** 
```ts
if(world::ignite_cause_equals("LAVA"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**                                                                                                                                                                                                                                                                                         | **Description** |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `cause`  | Marker<br/>**LAVA** - Lava<br/>**FLINT_AND_STEEL** - Lighter<br/>**SPREAD** - Spread Fire<br/>**LIGHTNING** - Lightning<br/>**SUFFOCATION** - Suffocate<br/>**FALL** - Fall<br/>**FIREBALL** - Fire Bolt<br/>**ENDER_CRYSTAL** - End Crystal<br/>**EXPLOSION** - Explosion<br/>**ARROW** - Arrow | Fire Source     |
<h3 id=if_game_instrument_equals>
  <code>world::instrument_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sound Instrument Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the instrument in the event is equal to the selected one.

**Usage example:** 
```ts
if(world::instrument_equals("PIANO"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Description** |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `instrument` | Marker<br/>**PIANO** - Piano<br/>**BASS_DRUM** - Bass Drum<br/>**SNARE_DRUM** - Snare Drum<br/>**STICKS** - Klaves<br/>**BASS_GUITAR** - Bass Guitar<br/>**FLUTE** - Flute<br/>**BELL** - Bell<br/>**GUITAR** - Guitar<br/>**CHIME** - Chimes<br/>**XYLOPHONE** - Xylophone<br/>**IRON_XYLOPHONE** - Iron Xylophone<br/>**COW_BELL** - Cowbell<br/>**DIDGERIDOO** - Didgeridoo<br/>**BIT** - Bit<br/>**BANJO** - Banjo<br/>**PLING** - Pling<br/>**ZOMBIE** - Zombie<br/>**SKELETON** - Skeleton<br/>**CREEPER** - Creeper<br/>**DRAGON** - Ender Dragon<br/>**WITHER_SKELETON** - Wither skeleton<br/>**PIGLIN** - Piglin<br/>**CUSTOM_HEAD** - Custom head | Instrument      |
<h3 id=if_game_sign_contains>
  <code>world::sign_contains</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sign Contains Text\
**Type:** Action that checks the conditions\
**Description:** Checks if a sign at a given location contains the specified text.

**Usage example:** 
```ts
if(world::sign_contains(location(0,0,0,0,0),["texts", "texts"],"ANY","CONTAINS","FIRST"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                              | **Description**  |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `location`   | Location                                                                                                                                              | Sign location    |
| `texts`      | list[Text]                                                                                                                                            | Text to check    |
| `check_side` | Marker<br/>**ANY** - Any<br/>**FRONT** - Front<br/>**BACK** - Back                                                                                    | Sign Side        |
| `check_mode` | Marker<br/>**CONTAINS** - Content Compare<br/>**EQUALS** - Full Compare<br/>**ANY** - None<br/>**ALL** - None                                         | Comparison Type  |
| `lines`      | Marker<br/>**FIRST** - 1 line<br/>**SECOND** - 2 line<br/>**THIRD** - 3 line<br/>**FOURTH** - line 4<br/>**ALL** - All Lines<br/>**ANY** - Any String | Lines to Compare |
