<h2 id=player>
  <code>player</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

### Selectors

| **Name**           | **Description** |
|--------------------|-----------------|
| `<current>`        | Current player  |
| `<default_player>` | Default player  |
| `<killer_player>`  | Killer          |
| `<damager_player>` | Damager         |
| `<shooter_player>` | Shooter         |
| `<victim_player>`  | Victim          |
| `<random_player>`  | Random player   |
| `<all_players>`    | All players     |

<h3 id=if_player_chat_colors_enabled>
  <code>player::chat_colors_enabled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Chat Colors Enabled\
**Type:** Action that checks the conditions\
**Description:** Checks if the player enabled \"Chat Colors\" in settings.

**Usage example:** 
```ts
if(player::chat_colors_enabled()){
    player::message("Condition is true");
}
```

<h3 id=if_player_chat_message_equals>
  <code>player::chat_message_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Chat Message Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the player\'s message is equal to the selected one.

**Usage example:** 
```ts
if(player::chat_message_equals(["chat_messages", "chat_messages"])){
    player::message("Condition is true");
}

#Or dry by keywords

player::chat_message_equals(chat_messages=["chat_messages", "chat_messages"]){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**        | **Type**   | **Description** |
| --------------- | ---------- | --------------- |
| `chat_messages` | list[Text] | Message         |
<h3 id=if_player_collides_at_location>
  <code>player::collides_at_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Collidies At Location\
**Type:** Action that checks the conditions\
**Description:** Checks if a player collides with blocks, shulkers, boats and worldborder on given location.

**Usage example:** 
```ts
if(player::collides_at_location(location(0,0,0,0,0))){
    player::message("Condition is true");
}

#Or dry by keywords

player::collides_at_location(location=location(0,0,0,0,0)){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**   | **Type** | **Description**   |
| ---------- | -------- | ----------------- |
| `location` | Location | Location to check |
<h3 id=if_player_collides_using_hitbox>
  <code>player::collides_using_hitbox</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Collides Using Custom Hitbox\
**Type:** Action that checks the conditions\
**Description:** Checks if a player collides with blocks, shulkers, boats and worldborder using a custom hitbox.

**Usage example:** 
```ts
if(player::collides_using_hitbox(location(0,0,0,0,0), location(0,0,0,0,0))){
    player::message("Condition is true");
}

#Or dry by keywords

player::collides_using_hitbox(min=location(0,0,0,0,0), max=location(0,0,0,0,0)){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type** | **Description**             |
| -------- | -------- | --------------------------- |
| `min`    | Location | First corner of the hitbox  |
| `max`    | Location | Second corner of the hitbox |
<h3 id=if_player_collides_with_entity>
  <code>player::collides_with_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Collidies With Entity\
**Type:** Action that checks the conditions\
**Description:** Checks if player\'s hitbox collides with a hitbox of given entity.

**Usage example:** 
```ts
if(player::collides_with_entity("name_or_uuid", "CONTAINS")){
    player::message("Condition is true");
}

#Or dry by keywords

player::collides_with_entity(name_or_uuid="name_or_uuid", check_type="CONTAINS"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**       | **Type**                                                         | **Description**     |
| -------------- | ---------------------------------------------------------------- | ------------------- |
| `name_or_uuid` | Text                                                             | Entity name or UUID |
| `check_type`   | Marker<br/>**CONTAINS** - Contains<br/>**OVERLAPS** - Intersects | Collide check type  |
<h3 id=if_player_cursor_item_equals>
  <code>player::cursor_item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Cursor Item Is Equal To\
**Type:** Action that checks the conditions\
**Description:** Checks if the item at the player\'s cursor is equal to the selected item.

**Usage example:** 
```ts
if(player::cursor_item_equals([item("stick"), item("stick")], "EXACTLY")){
    player::message("Condition is true");
}

#Or dry by keywords

player::cursor_item_equals(items=[item("stick"), item("stick")], comparison_mode="EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                               | **Description** |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `items`           | list[Item]                                                                                                                                                                                             | Items to Check  |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**TYPE_ONLY** - Item type only | Comparison Mode |
<h3 id=if_player_dummy>
  <code>player::is_dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action that checks the conditions\
**Description:** ...

**Usage example:** 
```ts
if(player::is_dummy()){
    player::message("Condition is true");
}
```

<h3 id=if_player_gamemode_equals>
  <code>player::gamemode_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Game Mode Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the player\'s gamemode is equal to the selected one.

**Usage example:** 
```ts
if(player::gamemode_equals("ADVENTURE")){
    player::message("Condition is true");
}

#Or dry by keywords

player::gamemode_equals(gamemode="ADVENTURE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**   | **Type**                                                                                                                   | **Description** |
| ---------- | -------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `gamemode` | Marker<br/>**ADVENTURE** - Adventure<br/>**CREATIVE** - Creative<br/>**SPECTATOR** - Spectator<br/>**SURVIVAL** - Survival | Game Mode       |
<h3 id=if_player_has_input>
  <code>player::has_input</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

**Usage example:** 
```ts
if(player::has_input("FORWARD")){
    player::message("Condition is true");
}

#Or dry by keywords

player::has_input(input_type="FORWARD"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                                       | **Description** |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `input_type` | Marker<br/>**FORWARD** - None<br/>**BACKWARDS** - None<br/>**LEFT** - None<br/>**RIGHT** - None<br/>**JUMP** - None<br/>**SNEAK** - None<br/>**SPRINT** - None | None            |
<h3 id=if_player_has_item>
  <code>player::has_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has an Item\
**Type:** Action that checks the conditions\
**Description:** Checks if the player has an item in their inventory.

**Usage example:** 
```ts
if(player::has_item([item("stick"), item("stick")], "ALL", "EXACTLY")){
    player::message("Condition is true");
}

#Or dry by keywords

player::has_item(items=[item("stick"), item("stick")], check_mode="ALL", comparison_mode="EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                          | **Description** |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `items`           | list[Item]                                                                                                                                                                                        | Items to Check  |
| `check_mode`      | Marker<br/>**ALL** - All Items<br/>**ANY** - Any Item                                                                                                                                             | Check Mode      |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore quantity<br/>**TYPE_ONLY** - Item type only | Comparison Mode |
<h3 id=if_player_has_item_at_least>
  <code>player::has_item_at_least</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has an Item in Quantity\
**Type:** Action that checks the conditions\
**Description:** Checks if a player has an item in a certain quantity.

**Usage example:** 
```ts
if(player::has_item_at_least(item("stick"), 1, "EXACTLY")){
    player::message("Condition is true");
}

#Or dry by keywords

player::has_item_at_least(item=item("stick"), count=1, comparison_mode="EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                          | **Description**  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `item`            | Item                                                                                                                                                                                              | Item to Check    |
| `count`           | Number                                                                                                                                                                                            | Minimum Quantity |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore quantity<br/>**TYPE_ONLY** - Item Type Only | Comparison Mode  |
<h3 id=if_player_has_item_in_slot>
  <code>player::has_item_in_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has an Item In Slot\
**Type:** Action that checks the conditions\
**Description:** Checks if a player has an item in a specific inventory slot.

**Usage example:** 
```ts
if(player::has_item_in_slot([1, 2], [item("stick"), item("stick")], "EXACTLY")){
    player::message("Condition is true");
}

#Or dry by keywords

player::has_item_in_slot(slots=[1, 2], items=[item("stick"), item("stick")], comparison_mode="EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                               | **Description**      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| `slots`           | list[Number]                                                                                                                                                                                           | Slot number to check |
| `items`           | list[Item]                                                                                                                                                                                             | Items to Check       |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**TYPE_ONLY** - Item Type Only | Comparison Mode      |
<h3 id=if_player_has_potion_effect>
  <code>player::has_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has Potion Effect\
**Type:** Action that checks the conditions\
**Description:** Checks if a player has the effect of a potion.

**Usage example:** 
```ts
if(player::has_potion_effect([potion("slow_falling"), potion("slow_falling")], "ALL")){
    player::message("Condition is true");
}

#Or dry by keywords

player::has_potion_effect(potions=[potion("slow_falling"), potion("slow_falling")], check_mode="ALL"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                  | **Description** |
| ------------ | --------------------------------------------------------- | --------------- |
| `potions`    | list[Potion]                                              | Potions to Test |
| `check_mode` | Marker<br/>**ALL** - All Effects<br/>**ANY** - Any Effect | Check Mode      |
<h3 id=if_player_has_privilege>
  <code>player::has_privilege</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has Permission\
**Type:** Action that checks the conditions\
**Description:** Checks if a player has certain rights in the world.\
**Additional info:**\
&nbsp;&nbsp;If the \"Check Accuracy\" marker is enabled, building and development permissions will be checked even if the player is whitelisted.

**Usage example:** 
```ts
if(player::has_privilege("BUILDER", "FALSE")){
    player::message("Condition is true");
}

#Or dry by keywords

player::has_privilege(privilege="BUILDER", exact="FALSE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**    | **Type**                                                                                                                                                                           | **Description** |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `privilege` | Marker<br/>**BUILDER** - Builder<br/>**BUILDER_AND_DEVELOPER** - Builder and Developer<br/>**DEVELOPER** - Developer<br/>**OWNER** - World Owner<br/>**WHITELISTED** - Whitelisted | Right           |
| `exact`     | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable                                                                                                                               | Check Accuracy  |
<h3 id=if_player_has_room_for_item>
  <code>player::has_room_for_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has a Room For Item\
**Type:** Action that checks the conditions\
**Description:** Checks if the player has room for one or more items in their inventory.

**Usage example:** 
```ts
if(player::has_room_for_item([item("stick"), item("stick")], "ARMOR", "ALL")){
    player::message("Condition is true");
}

#Or dry by keywords

player::has_room_for_item(items=[item("stick"), item("stick")], checked_slots="ARMOR", check_mode="ALL"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**        | **Type**                                                                                                                                                                         | **Description**    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `items`         | list[Item]                                                                                                                                                                       | Items to Check     |
| `checked_slots` | Marker<br/>**ARMOR** - Armor<br/>**ENTIRE_INVENTORY** - All Inventory<br/>**HOTBAR** - Hot Bar<br/>**MAIN_INVENTORY** - Main Inventory<br/>**UPPER_INVENTORY** - Upper Inventory | Checked Slots Mode |
| `check_mode`    | Marker<br/>**ALL** - All Items<br/>**ANY** - Any Items                                                                                                                           | Check Item Mode    |
<h3 id=if_player_hotbar_slot_equals>
  <code>player::hotbar_slot_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Hotbar Slot Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the player\'s current hotbar slot matches slot 1 to 9 in the chest.

**Usage example:** 
```ts
if(player::hotbar_slot_equals(1)){
    player::message("Condition is true");
}

#Or dry by keywords

player::hotbar_slot_equals(slot=1){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type** | **Description**      |
| -------- | -------- | -------------------- |
| `slot`   | Number   | Slot number to check |
<h3 id=if_player_in_area>
  <code>player::in_area</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Inside Region\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is in a certain region.

**Usage example:** 
```ts
if(player::in_area(location(0,0,0,0,0), location(0,0,0,0,0), "FALSE", "HITBOX", "CONTAINS")){
    player::message("Condition is true");
}

#Or dry by keywords

player::in_area(location_1=location(0,0,0,0,0), location_2=location(0,0,0,0,0), ignore_y_axis="FALSE", intersect_type="HITBOX", check_type="CONTAINS"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**         | **Type**                                                         | **Description**        |
| ---------------- | ---------------------------------------------------------------- | ---------------------- |
| `location_1`     | Location                                                         | First corner of region |
| `location_2`     | Location                                                         | Second Region Corner   |
| `ignore_y_axis`  | Marker<br/>**FALSE** - Don\'t ignore<br/>**TRUE** - Ignore       | Ignore Y Axis          |
| `intersect_type` | Marker<br/>**HITBOX** - Hitbox<br/>**POINT** - Location          | Intersection type      |
| `check_type`     | Marker<br/>**CONTAINS** - Contains<br/>**OVERLAPS** - Intersects | Hitbox check type      |
<h3 id=if_player_inventory_menu_slot_equals>
  <code>player::inventory_menu_slot_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Inventory Slot Contains\
**Type:** Action that checks the conditions\
**Description:** Checks if a player with an open inventory currently has a specific item in a slot.

**Usage example:** 
```ts
if(player::inventory_menu_slot_equals([1, 2], [item("stick"), item("stick")], "EXACTLY")){
    player::message("Condition is true");
}

#Or dry by keywords

player::inventory_menu_slot_equals(slots=[1, 2], items=[item("stick"), item("stick")], comparison_mode="EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                               | **Description**      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| `slots`           | list[Number]                                                                                                                                                                                           | Slot number to check |
| `items`           | list[Item]                                                                                                                                                                                             | Items to Check       |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**TYPE_ONLY** - Item Type Only | Comparison Mode      |
<h3 id=if_player_inventory_type_open>
  <code>player::inventory_type_open</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Open Inventory Type Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a player\'s inventory type is open.

**Usage example:** 
```ts
if(player::inventory_type_open("ANVIL")){
    player::message("Condition is true");
}

#Or dry by keywords

player::inventory_type_open(inventory_type="ANVIL"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**         | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Description** |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `inventory_type` | Marker<br/>**ANVIL** - Anvil<br/>**BARREL** - Barrel<br/>**BEACON** - Beacon<br/>**BLAST_FURNACE** - Smelter<br/>**BREWING** - Potion Brewing<br/>**CARTOGRAPHY** - Cartographer\'s Desk<br/>**CHEST** - Chest<br/>**CHISELED_BOOKSHELF** - Chiseled Bookshelf<br/>**COMPOSTER** - Composter<br/>**CRAFTER** - Crafter<br/>**CRAFTING** - Not Open<br/>**CREATIVE** - Creative Inventory<br/>**DECORATED_POT** - Decorated Pot<br/>**DISPENSER** - Dispenser<br/>**DROPPER** - Dropper<br/>**ENCHANTING** - Enchanting Table<br/>**ENDER_CHEST** - Ender Chest<br/>**FURNACE** - Furnace<br/>**GRINDSTONE** - Grindstone<br/>**HOPPER** - Hopper<br/>**JUKEBOX** - Jukebox<br/>**LECTERN** - Pulpit<br/>**LOOM** - Loom<br/>**MERCHANT** - Merchant<br/>**PLAYER** - Player Inventory<br/>**SHULKER_BOX** - Shulker Box<br/>**SMITHING** - Blacksmith\'s Table<br/>**SMITHING_NEW** - Smithing Table<br/>**SMOKER** - Smoker<br/>**STONECUTTER** - Stonecutter<br/>**WORKBENCH** - Workbench | Inventory Type  |
<h3 id=if_player_is_allow_server_listing>
  <code>player::is_allow_server_listing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is Allow Server Listing\
**Type:** Action that checks the conditions\
**Description:** Checks if the player enabled \"Allow Server Listing\" in settings.

**Usage example:** 
```ts
if(player::is_allow_server_listing()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_blocking>
  <code>player::is_blocking</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Uses a Shield\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is using a shield.

**Usage example:** 
```ts
if(player::is_blocking()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_disguised>
  <code>player::is_disguised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguised for Everyone\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is disguised to other players.

**Usage example:** 
```ts
if(player::is_disguised()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_flying>
  <code>player::is_flying</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Flying\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is flying.

**Usage example:** 
```ts
if(player::is_flying()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_gliding>
  <code>player::is_gliding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Gliding\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is gliding on elytras.

**Usage example:** 
```ts
if(player::is_gliding()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_holding>
  <code>player::holding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Holding an Item\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is holding an item in their hands.

**Usage example:** 
```ts
if(player::holding([item("stick"), item("stick")], "EITHER_HAND", "EXACTLY")){
    player::message("Condition is true");
}

#Or dry by keywords

player::holding(items=[item("stick"), item("stick")], hand_slot="EITHER_HAND", comparison_mode="EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                               | **Description** |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `items`           | list[Item]                                                                                                                                                                                             | Items to Check  |
| `hand_slot`       | Marker<br/>**EITHER_HAND** - Any hand<br/>**MAIN_HAND** - Main Hand<br/>**OFF_HAND** - Sub Hand                                                                                                        | Hand            |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**TYPE_ONLY** - Item type only | Comparison Mode |
<h3 id=if_player_is_looking_at_block>
  <code>player::is_looking_at_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Looks at a Block\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is looking at a specific block or location.

**Usage example:** 
```ts
if(player::is_looking_at_block([item("stone"), item("stone")], [location(0,0,0,0,0), location(0,0,0,0,0)], 1, "ALWAYS")){
    player::message("Condition is true");
}

#Or dry by keywords

player::is_looking_at_block(blocks=[item("stone"), item("stone")], locations=[location(0,0,0,0,0), location(0,0,0,0,0)], distance=1, fluid_mode="ALWAYS"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                                                                           | **Description**             |
| ------------ | ------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| `blocks`     | list[Block]                                                                                                        | Block(s) to check           |
| `locations`  | list[Location]                                                                                                     | Location(s) to check        |
| `distance`   | Number                                                                                                             | Max Block Distance to Check |
| `fluid_mode` | Marker<br/>**ALWAYS** - All kinds of fluids<br/>**NEVER** - Ignore Fluids<br/>**SOURCE_ONLY** - Fluid Sources Only | Fluid Mode                  |
<h3 id=if_player_is_near>
  <code>player::is_near</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Near Location\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is near the specified location (Default: 5 blocks).

**Usage example:** 
```ts
if(player::is_near(1, location(0,0,0,0,0), "FALSE")){
    player::message("Condition is true");
}

#Or dry by keywords

player::is_near(range=1, location=location(0,0,0,0,0), ignore_y_axis="FALSE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**        | **Type**                                                   | **Description**   |
| --------------- | ---------------------------------------------------------- | ----------------- |
| `range`         | Number                                                     | Check Range       |
| `location`      | Location                                                   | Location to check |
| `ignore_y_axis` | Marker<br/>**FALSE** - Don\'t Ignore<br/>**TRUE** - Ignore | Ignore Y Axis     |
<h3 id=if_player_is_on_ground>
  <code>player::is_on_ground</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is On Ground\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is not in the air.

**Usage example:** 
```ts
if(player::is_on_ground()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_online_mode>
  <code>player::is_online_mode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has a Premium Account\
**Type:** Action that checks the conditions\
**Description:** Checks if the player has a premium account.

**Usage example:** 
```ts
if(player::is_online_mode()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_riding_entity>
  <code>player::is_riding_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Riding an Entity\
**Type:** Action that checks the conditions\
**Description:** Checks if the player has ridden an entity (including vehicles).

**Usage example:** 
```ts
if(player::is_riding_entity(["entity_ids", "entity_ids"], "FARTHEST")){
    player::message("Condition is true");
}

#Or dry by keywords

player::is_riding_entity(entity_ids=["entity_ids", "entity_ids"], compare_mode="FARTHEST"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**       | **Type**                                                                                                               | **Description**                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `entity_ids`   | list[Text]                                                                                                             | Name, UUID, or type of entity to check |
| `compare_mode` | Marker<br/>**FARTHEST** - None<br/>**NAME_OR_UUID** - Name or UUID<br/>**NEAREST** - None<br/>**TYPE** - Creature Type | Compare Mode                           |
<h3 id=if_player_is_self_disguised>
  <code>player::is_self_disguised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Self Disguised\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is disguised to himself.

**Usage example:** 
```ts
if(player::is_self_disguised()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_sleeping>
  <code>player::is_sleeping</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sleeping\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is sleeping.

**Usage example:** 
```ts
if(player::is_sleeping()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_sneaking>
  <code>player::is_sneaking</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sneaking\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is sneaking.

**Usage example:** 
```ts
if(player::is_sneaking()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_sprinting>
  <code>player::is_sprinting</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Running\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is running or using the sprint key when swimming.

**Usage example:** 
```ts
if(player::is_sprinting()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_standing_on_block>
  <code>player::is_standing_on_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Standing on a Block\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is standing on a block of a certain category or a certain location.

**Usage example:** 
```ts
if(player::is_standing_on_block([item("stone"), item("stone")], [location(0,0,0,0,0), location(0,0,0,0,0)], "FALSE")){
    player::message("Condition is true");
}

#Or dry by keywords

player::is_standing_on_block(blocks=[item("stone"), item("stone")], locations=[location(0,0,0,0,0), location(0,0,0,0,0)], only_solid="FALSE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                             | **Description**   |
| ------------ | -------------------------------------------------------------------- | ----------------- |
| `blocks`     | list[Block]                                                          | Blocks to Check   |
| `locations`  | list[Location]                                                       | Location to check |
| `only_solid` | Marker<br/>**FALSE** - All blocks.<br/>**TRUE** - Only solid blocks. | Block check type  |
<h3 id=if_player_is_swimming>
  <code>player::is_swimming</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Swimming\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is swimming in water or lava.

**Usage example:** 
```ts
if(player::is_swimming()){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_using_item>
  <code>player::is_using_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Using Item\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is using a bow, shield, or any other usable item.

**Usage example:** 
```ts
if(player::is_using_item([item("stick"), item("stick")], "EXACTLY")){
    player::message("Condition is true");
}

#Or dry by keywords

player::is_using_item(items=[item("stick"), item("stick")], comparison_mode="EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                               | **Description** |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `items`           | list[Item]                                                                                                                                                                                             | Items to Check  |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**TYPE_ONLY** - Item type only | Comparison Mode |
<h3 id=if_player_is_wearing_item>
  <code>player::is_wearing_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Wearing an Item\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is wearing an item.

**Usage example:** 
```ts
if(player::is_wearing_item([item("stick"), item("stick")], "ALL", "EXACTLY")){
    player::message("Condition is true");
}

#Or dry by keywords

player::is_wearing_item(items=[item("stick"), item("stick")], check_mode="ALL", comparison_mode="EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                               | **Description** |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `items`           | list[Item]                                                                                                                                                                                             | Item to check   |
| `check_mode`      | Marker<br/>**ALL** - Wearing All<br/>**ANY** - Wearing something                                                                                                                                       | Check Mode      |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore Quantity Only<br/>**TYPE_ONLY** - Item type only | Comparison Mode |
<h3 id=if_player_item_is_not_on_cooldown>
  <code>player::item_is_not_on_cooldown</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Has No Cooldown\
**Type:** Action that checks the conditions\
**Description:** Checks if the player\'s item has a cooldown applicable to a specific item type.

**Usage example:** 
```ts
if(player::item_is_not_on_cooldown([item("stick"), item("stick")])){
    player::message("Condition is true");
}

#Or dry by keywords

player::item_is_not_on_cooldown(items=[item("stick"), item("stick")]){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**   | **Description** |
| -------- | ---------- | --------------- |
| `items`  | list[Item] | Items to Check  |
<h3 id=if_player_name_equals>
  <code>player::name_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Name Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the player\'s name is equal to the name in the chest.

**Usage example:** 
```ts
if(player::name_equals(["names_or_uuids", "names_or_uuids"])){
    player::message("Condition is true");
}

#Or dry by keywords

player::name_equals(names_or_uuids=["names_or_uuids", "names_or_uuids"]){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**         | **Type**   | **Description**         |
| ---------------- | ---------- | ----------------------- |
| `names_or_uuids` | list[Text] | Names or UUIDs to check |
<h3 id=if_player_text_filtering_enabled>
  <code>player::text_filtering_enabled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Text Filtering Enabled\
**Type:** Action that checks the conditions\
**Description:** Checks if the player have Mojang word filters enabled.

**Usage example:** 
```ts
if(player::text_filtering_enabled()){
    player::message("Condition is true");
}
```

<h3 id=player_add_inventory_menu_row>
  <code>player::add_inventory_menu_row</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Inventory Menu Row\
**Type:** Action without value\
**Description:** Adds a row with the specified items to the \"Chest\" type inventory.

**Usage example:** 
```ts
player::add_inventory_menu_row([item("stick"), item("stick")], "BUTTON");

#Or dry by keywords

player::add_inventory_menu_row(items=[item("stick"), item("stick")], position="BUTTON");
```

**Arguments:**

| **Name**   | **Type**                                                           | **Description** |
| ---------- | ------------------------------------------------------------------ | --------------- |
| `items`    | list[Item]                                                         | Items           |
| `position` | Marker<br/>**BUTTON** - Add Row Below<br/>**TOP** - Add row to top | Row Position    |
<h3 id=player_allow_placing_breaking_blocks>
  <code>player::allow_placing_breaking_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::allow_placing_breaking_blocks([item("stone"), item("stone")], "FALSE");

#Or dry by keywords

player::allow_placing_breaking_blocks(blocks=[item("stone"), item("stone")], allow="FALSE");
```

**Arguments:**

| **Name** | **Type**                                        | **Description** |
| -------- | ----------------------------------------------- | --------------- |
| `blocks` | list[Block]                                     | None            |
| `allow`  | Marker<br/>**FALSE** - None<br/>**TRUE** - None | None            |
<h3 id=player_boost_elytra>
  <code>player::boost_elytra</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Boost Elytra\
**Type:** Action without value\
**Description:** Accelerates the flight of an Elytra player with the power of the specified firework.

**Usage example:** 
```ts
player::boost_elytra(item("stick"));

#Or dry by keywords

player::boost_elytra(firework=item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `firework` | Item     | Firework Boost  |
<h3 id=player_clear_chat>
  <code>player::clear_chat</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Chat\
**Type:** Action without value\
**Description:** Clears all messages from the selected player\'s chat window.

**Usage example:** 
```ts
player::clear_chat();
```

<h3 id=player_clear_debug_markers>
  <code>player::clear_debug_markers</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Debug Markers\
**Type:** Action without value\
**Description:** Removes all debug markers for the player.

**Usage example:** 
```ts
player::clear_debug_markers();
```

<h3 id=player_clear_ender_chest_contents>
  <code>player::clear_ender_chest_contents</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Ender Chest Contents\
**Type:** Action without value\
**Description:** Clears items in a player\'s Ender Chest inventory.

**Usage example:** 
```ts
player::clear_ender_chest_contents();
```

<h3 id=player_clear_inventory>
  <code>player::clear_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Inventory\
**Type:** Action without value\
**Description:** Clears the player\'s inventory.

**Usage example:** 
```ts
player::clear_inventory("ARMOR");

#Or dry by keywords

player::clear_inventory(clear_mode="ARMOR");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                           | **Description** |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `clear_mode` | Marker<br/>**ARMOR** - Armor<br/>**ENTIRE** - All Inventory<br/>**HOTBAR** - Hot Bar<br/>**MAIN** - Main Inventory<br/>**UPPER** - Upper Inventory | Clear Mode      |
<h3 id=player_clear_items>
  <code>player::clear_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Items\
**Type:** Action without value\
**Description:** Removes all selected items from the player\'s inventory.

**Usage example:** 
```ts
player::clear_items([item("stick"), item("stick")]);

#Or dry by keywords

player::clear_items(items=[item("stick"), item("stick")]);
```

**Arguments:**

| **Name** | **Type**   | **Description** |
| -------- | ---------- | --------------- |
| `items`  | list[Item] | Items to Clear  |
<h3 id=player_clear_potion_effects>
  <code>player::clear_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Effects\
**Type:** Action without value\
**Description:** Clears all player effects.

**Usage example:** 
```ts
player::clear_potion_effects();
```

<h3 id=player_close_dialog_menu>
  <code>player::close_dialog_menu</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::close_dialog_menu();
```

<h3 id=player_close_inventory>
  <code>player::close_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Close Inventory Menu\
**Type:** Action without value\
**Description:** Closes a player\'s opened inventory menu.

**Usage example:** 
```ts
player::close_inventory();
```

<h3 id=player_damage>
  <code>player::damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Deal Damage\
**Type:** Action without value\
**Description:** Deals damage to a player.

**Usage example:** 
```ts
player::damage(1, "source");

#Or dry by keywords

player::damage(damage=1, source="source");
```

**Arguments:**

| **Name** | **Type** | **Description**                       |
| -------- | -------- | ------------------------------------- |
| `damage` | Number   | Damage Amount                         |
| `source` | Text     | Damage Source (creature name or UUID) |
<h3 id=player_disguise_as_block>
  <code>player::disguise_as_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Block\
**Type:** Action without value\
**Description:** Maxes the player under the selected block.

**Usage example:** 
```ts
player::disguise_as_block(item("stone"), "FALSE");

#Or dry by keywords

player::disguise_as_block(block=item("stone"), visible_to_self="FALSE");
```

**Arguments:**

| **Name**          | **Type**                                         | **Description** |
| ----------------- | ------------------------------------------------ | --------------- |
| `block`           | Block                                            | Disguise Block  |
| `visible_to_self` | Marker<br/>**FALSE** - False<br/>**TRUE** - True | Visible to self |
<h3 id=player_disguise_as_entity>
  <code>player::disguise_as_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Entity\
**Type:** Action without value\
**Description:** Maximizes the player to the selected entity.

**Usage example:** 
```ts
player::disguise_as_entity(item("stick"), "FALSE");

#Or dry by keywords

player::disguise_as_entity(entity_type=item("stick"), visible_to_self="FALSE");
```

**Arguments:**

| **Name**          | **Type**                                         | **Description**    |
| ----------------- | ------------------------------------------------ | ------------------ |
| `entity_type`     | Item                                             | Entity to Disguise |
| `visible_to_self` | Marker<br/>**FALSE** - False<br/>**TRUE** - True | Visible to self    |
<h3 id=player_disguise_as_item>
  <code>player::disguise_as_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise player as item\
**Type:** Action without value\
**Description:** Maxes the player as an item.

**Usage example:** 
```ts
player::disguise_as_item(item("stick"), "FALSE");

#Or dry by keywords

player::disguise_as_item(item=item("stick"), visible_to_self="FALSE");
```

**Arguments:**

| **Name**          | **Type**                                         | **Description** |
| ----------------- | ------------------------------------------------ | --------------- |
| `item`            | Item                                             | Disguise Item   |
| `visible_to_self` | Marker<br/>**FALSE** - False<br/>**TRUE** - True | Visible to self |
<h3 id=player_display_bell_ring>
  <code>player::display_bell_ring</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Bell Ring\
**Type:** Action without value\
**Description:** Displays the Bell ringing animation.\
**Additional info:**\
&nbsp;&nbsp;The \"Down\" direction stops the punch animation.\
**Work_with:**\
&nbsp;&nbsp;Bell

**Usage example:** 
```ts
player::display_bell_ring(location(0,0,0,0,0), "DOWN");

#Or from the object

location(0,0,0,0,0).display_bell_ring("DOWN");

#Or dry by keywords

player::display_bell_ring(location=location(0,0,0,0,0), direction="DOWN");
```

**Arguments:**

| **Name**    | **Type**                                                                                                       | **Description** |
| ----------- | -------------------------------------------------------------------------------------------------------------- | --------------- |
| `location`  | Location                                                                                                       | Bell location   |
| `direction` | Marker<br/>**DOWN** - Down<br/>**EAST** - East<br/>**NORTH** - North<br/>**SOUTH** - South<br/>**WEST** - West | Direction       |
<h3 id=player_display_block>
  <code>player::display_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Block\
**Type:** Action without value\
**Description:** Display a block to a player without affecting other players.

**Usage example:** 
```ts
player::display_block([location(0,0,0,0,0), location(0,0,0,0,0)], item("stone"));

#Or dry by keywords

player::display_block(location=[location(0,0,0,0,0), location(0,0,0,0,0)], block=item("stone"));
```

**Arguments:**

| **Name**   | **Type**       | **Description**  |
| ---------- | -------------- | ---------------- |
| `location` | list[Location] | Block Location   |
| `block`    | Block          | Block to display |
<h3 id=player_display_end_gateway_beam>
  <code>player::display_end_gateway_beam</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display End Gateway Beam Animation\
**Type:** Action without value\
**Description:** Displays an End Gateway beam animation at a specific location.

**Usage example:** 
```ts
player::display_end_gateway_beam(location(0,0,0,0,0), "DARK_PURPLE");

#Or dry by keywords

player::display_end_gateway_beam(location=location(0,0,0,0,0), color="DARK_PURPLE");
```

**Arguments:**

| **Name**   | **Type**                                                                     | **Description** |
| ---------- | ---------------------------------------------------------------------------- | --------------- |
| `location` | Location                                                                     | Beam Location   |
| `color`    | Marker<br/>**DARK_PURPLE** - Dark Purple<br/>**LIGHT_PURPLE** - Light Purple | Beam color      |
<h3 id=player_display_hologram>
  <code>player::display_hologram</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Hologram\
**Type:** Action without value\
**Description:** Shows the player a hologram. To remove a hologram at a location, leave the text blank.\
**Additional info:**\
&nbsp;&nbsp;To wrap text on a new line, use \"\\n\", eg \: \"Line1\\nLine2\".

**Usage example:** 
```ts
player::display_hologram(location(0,0,0,0,0), "text");

#Or dry by keywords

player::display_hologram(location=location(0,0,0,0,0), text="text");
```

**Arguments:**

| **Name**   | **Type** | **Description**   |
| ---------- | -------- | ----------------- |
| `location` | Location | Hologram Location |
| `text`     | Text     | Hologram Text     |
<h3 id=player_display_lightning>
  <code>player::display_lightning</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Lightning Effect\
**Type:** Action without value\
**Description:** Display lightning to the player without showing it to other players or setting the area on fire.

**Usage example:** 
```ts
player::display_lightning(location(0,0,0,0,0));

#Or dry by keywords

player::display_lightning(location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**           |
| ---------- | -------- | ------------------------- |
| `location` | Location | Lightning Strike Location |
<h3 id=player_display_particle>
  <code>player::display_particle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Effect\
**Type:** Action without value\
**Description:** Displays the particle effect at the selected location to the player.

**Usage example:** 
```ts
player::display_particle([particle("fire"), particle("fire")], [location(0,0,0,0,0), location(0,0,0,0,0)]);

#Or dry by keywords

player::display_particle(particle=[particle("fire"), particle("fire")], location=[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

**Arguments:**

| **Name**   | **Type**              | **Description**            |
| ---------- | --------------------- | -------------------------- |
| `particle` | list[Particle Effect] | Particle Effect to Display |
| `location` | list[Location]        | Effect Location            |
<h3 id=player_display_particle_circle>
  <code>player::display_particle_circle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Circle\
**Type:** Action without value\
**Description:** Shows a player a circle out of particles with given parameters.

**Usage example:** 
```ts
player::display_particle_circle(particle("fire"), location(0,0,0,0,0), 1, 2, 3, vector(0,0,0), "DEGREES");

#Or dry by keywords

player::display_particle_circle(particle=particle("fire"), center=location(0,0,0,0,0), radius=1, points=2, start_angle=3, perpendicular=vector(0,0,0), angle_unit="DEGREES");
```

**Arguments:**

| **Name**        | **Type**                                                   | **Description**                                               |
| --------------- | ---------------------------------------------------------- | ------------------------------------------------------------- |
| `particle`      | Particle Effect                                            | Particle to show                                              |
| `center`        | Location                                                   | Circle center                                                 |
| `radius`        | Number                                                     | Circle radius                                                 |
| `points`        | Number                                                     | Amount of points on the circle                                |
| `start_angle`   | Number                                                     | Starting angle                                                |
| `perpendicular` | Vector                                                     | Normal of the plane to which the circle will be perpendicular |
| `angle_unit`    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians | Angle type                                                    |
<h3 id=player_display_particle_cube>
  <code>player::display_particle_cube</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Cube\
**Type:** Action without value\
**Description:** Displays a particle cuboid to the player.

**Usage example:** 
```ts
player::display_particle_cube(particle("fire"), location(0,0,0,0,0), location(0,0,0,0,0), 1, "HOLLOW");

#Or dry by keywords

player::display_particle_cube(particle=particle("fire"), first_corner=location(0,0,0,0,0), second_corner=location(0,0,0,0,0), spacing=1, type="HOLLOW");
```

**Arguments:**

| **Name**        | **Type**                                                                           | **Description** |
| --------------- | ---------------------------------------------------------------------------------- | --------------- |
| `particle`      | Particle Effect                                                                    | Particle        |
| `first_corner`  | Location                                                                           | First corner    |
| `second_corner` | Location                                                                           | Second corner   |
| `spacing`       | Number                                                                             | Spacing         |
| `type`          | Marker<br/>**HOLLOW** - Hollow<br/>**SOLID** - Solid<br/>**WIREFRAME** - Wireframe | Cuboid type     |
<h3 id=player_display_particle_line>
  <code>player::display_particle_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Line\
**Type:** Action without value\
**Description:** Displays a particle effect line to the player from the start location to the end location at a specified distance.

**Usage example:** 
```ts
player::display_particle_line(particle("fire"), location(0,0,0,0,0), location(0,0,0,0,0), 1, "DISTANCE");

#Or dry by keywords

player::display_particle_line(particle=particle("fire"), start=location(0,0,0,0,0), end=location(0,0,0,0,0), divider=1, unit_of_measurement="DISTANCE");
```

**Arguments:**

| **Name**              | **Type**                                                           | **Description**                |
| --------------------- | ------------------------------------------------------------------ | ------------------------------ |
| `particle`            | Particle Effect                                                    | Particle Effect to Display     |
| `start`               | Location                                                           | Start Location                 |
| `end`                 | Location                                                           | End Location                   |
| `divider`             | Number                                                             | Number/Space Between Particles |
| `unit_of_measurement` | Marker<br/>**DISTANCE** - By distance<br/>**POINTS** - By Quantity | Particle Display Type          |
<h3 id=player_display_particle_ray>
  <code>player::display_particle_ray</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Ray\
**Type:** Action without value\
**Description:** Displays a particle effect ray to the player from the starting location along the specified vector with the specified distance.

**Usage example:** 
```ts
player::display_particle_ray(particle("fire"), location(0,0,0,0,0), vector(0,0,0), 1, "DISTANCE");

#Or dry by keywords

player::display_particle_ray(particle=particle("fire"), start=location(0,0,0,0,0), ray=vector(0,0,0), divider=1, unit_of_measurement="DISTANCE");
```

**Arguments:**

| **Name**              | **Type**                                                           | **Description**                |
| --------------------- | ------------------------------------------------------------------ | ------------------------------ |
| `particle`            | Particle Effect                                                    | Particle Effect to Display     |
| `start`               | Location                                                           | Start Location                 |
| `ray`                 | Vector                                                             | Ray Direction                  |
| `divider`             | Number                                                             | Number/Space Between Particles |
| `unit_of_measurement` | Marker<br/>**DISTANCE** - By distance<br/>**POINTS** - By Quantity | Particle Display Type          |
<h3 id=player_display_particle_sphere>
  <code>player::display_particle_sphere</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Sphere\
**Type:** Action without value\
**Description:** Displays a particle sphere to the player.

**Usage example:** 
```ts
player::display_particle_sphere(particle("fire"), location(0,0,0,0,0), 1, 2);

#Or dry by keywords

player::display_particle_sphere(particle=particle("fire"), center=location(0,0,0,0,0), radius=1, points=2);
```

**Arguments:**

| **Name**   | **Type**        | **Description** |
| ---------- | --------------- | --------------- |
| `particle` | Particle Effect | Particle        |
| `center`   | Location        | Center          |
| `radius`   | Number          | Radius          |
| `points`   | Number          | Points          |
<h3 id=player_display_particle_spiral>
  <code>player::display_particle_spiral</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Spiral\
**Type:** Action without value\
**Description:** Displays a particle spiral to the player.

**Usage example:** 
```ts
player::display_particle_spiral(particle("fire"), location(0,0,0,0,0), 1, 2, 3, 4, 5, "DEGREES");

#Or dry by keywords

player::display_particle_spiral(particle=particle("fire"), center=location(0,0,0,0,0), distance=1, radius=2, points=3, rotations=4, start_angle=5, angle_unit="DEGREES");
```

**Arguments:**

| **Name**      | **Type**                                                   | **Description** |
| ------------- | ---------------------------------------------------------- | --------------- |
| `particle`    | Particle Effect                                            | Particle        |
| `center`      | Location                                                   | Center          |
| `distance`    | Number                                                     | Distance        |
| `radius`      | Number                                                     | Radius          |
| `points`      | Number                                                     | Points          |
| `rotations`   | Number                                                     | Rotations       |
| `start_angle` | Number                                                     | Start Angle     |
| `angle_unit`  | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians | Angle type      |
<h3 id=player_display_pick_up_animation>
  <code>player::display_pick_up_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Pick Up Animation\
**Type:** Action without value\
**Description:** Shows the player a pickup animation.\
**Additional info:**\
&nbsp;&nbsp;Essences that can be picked up can be items, experience orbs, and arrows.\
&nbsp;&nbsp;This action works with any entity, not just the player.

**Usage example:** 
```ts
player::display_pick_up_animation("collected_name_or_uuid", "collector_name_or_uuid", 1);

#Or dry by keywords

player::display_pick_up_animation(collected_name_or_uuid="collected_name_or_uuid", collector_name_or_uuid="collector_name_or_uuid", amount=1);
```

**Arguments:**

| **Name**                 | **Type** | **Description**                            |
| ------------------------ | -------- | ------------------------------------------ |
| `collected_name_or_uuid` | Text     | Name or UUID of the entity being picked up |
| `collector_name_or_uuid` | Text     | Name or UUID of the entity that picks up   |
| `amount`                 | Number   | Amount to pick up                          |
<h3 id=player_display_sign_text>
  <code>player::display_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Sign Text\
**Type:** Action without value\
**Description:** Show the sign\'s text change to the player without changing its text for other players.

**Usage example:** 
```ts
player::display_sign_text(location(0,0,0,0,0), "line_1", "line_2", "line_3", "line_4");

#Or dry by keywords

player::display_sign_text(location=location(0,0,0,0,0), line_1="line_1", line_2="line_2", line_3="line_3", line_4="line_4");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `location` | Location | Sign location      |
| `line_1`   | Text     | First Sign Line    |
| `line_2`   | Text     | Second Sign Line   |
| `line_3`   | Text     | Third line of sign |
| `line_4`   | Text     | Fourth Sign Line   |
<h3 id=player_display_vibration>
  <code>player::display_vibration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Vibration Particle\
**Type:** Action without value\
**Description:** Displays to the player a particle of vibration moving from one point to another.

**Usage example:** 
```ts
player::display_vibration(location(0,0,0,0,0), location(0,0,0,0,0), 1);

#Or dry by keywords

player::display_vibration(from=location(0,0,0,0,0), to=location(0,0,0,0,0), destination_time=1);
```

**Arguments:**

| **Name**           | **Type** | **Description**           |
| ------------------ | -------- | ------------------------- |
| `from`             | Location | Starting Location         |
| `to`               | Location | Final Location            |
| `destination_time` | Number   | Destination time in ticks |
<h3 id=player_dummy>
  <code>player::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action without value\
**Description:** ...

**Usage example:** 
```ts
player::dummy();
```

<h3 id=player_expand_inventory_menu>
  <code>player::expand_inventory_menu</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Expand Inventory Menu\
**Type:** Action without value\
**Description:** Expands the player\'s opened inventory menu by the selected number of lines and populates it with the specified items.

**Usage example:** 
```ts
player::expand_inventory_menu([item("stick"), item("stick")], 1);

#Or dry by keywords

player::expand_inventory_menu(items=[item("stick"), item("stick")], size=1);
```

**Arguments:**

| **Name** | **Type**   | **Description**          |
| -------- | ---------- | ------------------------ |
| `items`  | list[Item] | Items to Fill            |
| `size`   | Number     | Number of rows to expand |
<h3 id=player_face_location>
  <code>player::face_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Turn to Location\
**Type:** Action without value\
**Description:** Turns the player towards the location.

**Usage example:** 
```ts
player::face_location(location(0,0,0,0,0));

#Or dry by keywords

player::face_location(location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `location` | Location | Location        |
<h3 id=player_force_flight_mode>
  <code>player::force_flight_mode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::force_flight_mode("FALSE");

#Or dry by keywords

player::force_flight_mode(is_flying="FALSE");
```

**Arguments:**

| **Name**    | **Type**                                        | **Description** |
| ----------- | ----------------------------------------------- | --------------- |
| `is_flying` | Marker<br/>**FALSE** - None<br/>**TRUE** - None | None            |
<h3 id=player_give_experience>
  <code>player::give_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give Experience\
**Type:** Action without value\
**Description:** Gives a player an experience.

**Usage example:** 
```ts
player::give_experience(1, "LEVEL");

#Or dry by keywords

player::give_experience(experience=1, mode="LEVEL");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                  | **Description** |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `experience` | Number                                                                                                                    | Give Amount     |
| `mode`       | Marker<br/>**LEVEL** - As Level<br/>**LEVEL_PERCENTAGE** - As a percentage of level<br/>**POINTS** - As experience points | Give Type       |
<h3 id=player_give_items>
  <code>player::give_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give Item\
**Type:** Action without value\
**Description:** Gives players items from a chest.

**Usage example:** 
```ts
player::give_items([item("stick"), item("stick")], 1);

#Or dry by keywords

player::give_items(items=[item("stick"), item("stick")], amount=1);
```

**Arguments:**

| **Name** | **Type**   | **Description**             |
| -------- | ---------- | --------------------------- |
| `items`  | list[Item] | Items                       |
| `amount` | Number     | Amount of items to give out |
<h3 id=player_give_potion_effect>
  <code>player::give_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give Potion Effect\
**Type:** Action without value\
**Description:** Gives the selected effects to a player.

**Usage example:** 
```ts
player::give_potion_effect([potion("slow_falling"), potion("slow_falling")], "FALSE", "FALSE", "AMBIENT");

#Or dry by keywords

player::give_potion_effect(potions=[potion("slow_falling"), potion("slow_falling")], show_icon="FALSE", overwrite="FALSE", particle_mode="AMBIENT");
```

**Arguments:**

| **Name**        | **Type**                                                                       | **Description**            |
| --------------- | ------------------------------------------------------------------------------ | -------------------------- |
| `potions`       | list[Potion]                                                                   | Effects to Give            |
| `show_icon`     | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes                                 | Show Effect Icon           |
| `overwrite`     | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes                                 | Overwrite existing effects |
| `particle_mode` | Marker<br/>**AMBIENT** - Transparent<br/>**NONE** - None<br/>**REGULAR** - Yes | Give Particles             |
<h3 id=player_give_random_item>
  <code>player::give_random_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give a Random Item\
**Type:** Action without value\
**Description:** Gives a player a random item or a stack of items in a chest.

**Usage example:** 
```ts
player::give_random_item([item("stick"), item("stick")]);

#Or dry by keywords

player::give_random_item(items=[item("stick"), item("stick")]);
```

**Arguments:**

| **Name** | **Type**   | **Description** |
| -------- | ---------- | --------------- |
| `items`  | list[Item] | Items to Pick   |
<h3 id=player_heal>
  <code>player::heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Heal Player\
**Type:** Action without value\
**Description:** Heals a player.

**Usage example:** 
```ts
player::heal(1);

#Or dry by keywords

player::heal(heal=1);
```

**Arguments:**

| **Name** | **Type** | **Description**               |
| -------- | -------- | ----------------------------- |
| `heal`   | Number   | Amount of Half Hearts to Heal |
<h3 id=player_hide_entity>
  <code>player::hide_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Hide Entity From Player\
**Type:** Action without value\
**Description:** Hides the specified entity from the player.

**Usage example:** 
```ts
player::hide_entity(["name_or_uuid", "name_or_uuid"], "FALSE");

#Or dry by keywords

player::hide_entity(name_or_uuid=["name_or_uuid", "name_or_uuid"], hide="FALSE");
```

**Arguments:**

| **Name**       | **Type**                                             | **Description**            |
| -------------- | ---------------------------------------------------- | -------------------------- |
| `name_or_uuid` | list[Text]                                           | Name or UUID of the entity |
| `hide`         | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Hide                       |
<h3 id=player_hide_scoreboard>
  <code>player::hide_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Hide Scoreboard\
**Type:** Action without value\
**Description:** Hides the player\'s current scoreboard.

**Usage example:** 
```ts
player::hide_scoreboard();
```

<h3 id=player_kick>
  <code>player::kick</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Kick Player\
**Type:** Action without value\
**Description:** Kicks the player out of the world.

**Usage example:** 
```ts
player::kick();
```

<h3 id=player_launch_forward>
  <code>player::launch_forward</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Forward\
**Type:** Action without value\
**Description:** Launches the player forward or backward in the direction they are looking, depending on their strength.

**Usage example:** 
```ts
player::launch_forward(1, "FALSE", "YAW");

#Or dry by keywords

player::launch_forward(power=1, increment="FALSE", launch_axis="YAW");
```

**Arguments:**

| **Name**      | **Type**                                                              | **Description**          |
| ------------- | --------------------------------------------------------------------- | ------------------------ |
| `power`       | Number                                                                | Knock Up Power           |
| `increment`   | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                | Consider current inertia |
| `launch_axis` | Marker<br/>**YAW** - Horizontal Only<br/>**YAW_AND_PITCH** - All Axis | Launch Axis              |
<h3 id=player_launch_projectile>
  <code>player::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Projectile\
**Type:** Action without value\
**Description:** Launch a projectile from the player\'s location.

**Usage example:** 
```ts
player::launch_projectile(item("stick"), location(0,0,0,0,0), "name", 1, 2, particle("fire"));

#Or dry by keywords

player::launch_projectile(projectile=item("stick"), location=location(0,0,0,0,0), name="name", speed=1, inaccuracy=2, trail=particle("fire"));
```

**Arguments:**

| **Name**     | **Type**        | **Description**                                                  |
| ------------ | --------------- | ---------------------------------------------------------------- |
| `projectile` | Item            | Projectile to Launch                                             |
| `location`   | Location        | Launch Location                                                  |
| `name`       | Text            | Projectile Name                                                  |
| `speed`      | Number          | Projectile Speed                                                 |
| `inaccuracy` | Number          | Projectile deflection (0 to keep the projectile flying straight) |
| `trail`      | Particle Effect | The trail that the projectile will leave                         |
<h3 id=player_launch_to_location>
  <code>player::launch_to_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch to Location\
**Type:** Action without value\
**Description:** Launches the player to the selected location.

**Usage example:** 
```ts
player::launch_to_location(location(0,0,0,0,0), 1, "FALSE");

#Or dry by keywords

player::launch_to_location(location=location(0,0,0,0,0), power=1, increment="FALSE");
```

**Arguments:**

| **Name**    | **Type**                                               | **Description**          |
| ----------- | ------------------------------------------------------ | ------------------------ |
| `location`  | Location                                               | End Position             |
| `power`     | Number                                                 | Launch Power             |
| `increment` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Consider current inertia |
<h3 id=player_launch_up>
  <code>player::launch_up</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Up\
**Type:** Action without value\
**Description:** Tosses the player up or down based on strength.

**Usage example:** 
```ts
player::launch_up(1, "FALSE");

#Or dry by keywords

player::launch_up(power=1, increment="FALSE");
```

**Arguments:**

| **Name**    | **Type**                                               | **Description**          |
| ----------- | ------------------------------------------------------ | ------------------------ |
| `power`     | Number                                                 | Power                    |
| `increment` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Consider current inertia |
<h3 id=player_leave_vehicle>
  <code>player::leave_vehicle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dismount\
**Type:** Action without value\
**Description:** Dismounts a player from a vehicle or entity.

**Usage example:** 
```ts
player::leave_vehicle();
```

<h3 id=player_load_inventory>
  <code>player::load_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Load Saved Inventory\
**Type:** Action without value\
**Description:** Loads the selected saved inventory.\
**Additional info:**\
&nbsp;&nbsp;If there is no saved inventory, the player\'s inventory will be cleared.

**Usage example:** 
```ts
player::load_inventory();
```

<h3 id=player_open_book>
  <code>player::open_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Open Book\
**Type:** Action without value\
**Description:** Opens a book to a specific player.

**Usage example:** 
```ts
player::open_book(item("stick"));

#Or dry by keywords

player::open_book(book=item("stick"));
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `book`   | Item     | Book to Open    |
<h3 id=player_open_container_inventory>
  <code>player::open_container_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Open Container Menu\
**Type:** Action without value\
**Description:** Opens the block menu for the player at the specified location.

**Usage example:** 
```ts
player::open_container_inventory(location(0,0,0,0,0));

#Or dry by keywords

player::open_container_inventory(location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**           |
| ---------- | -------- | ------------------------- |
| `location` | Location | Location of block to open |
<h3 id=player_play_animation_action>
  <code>player::play_animation_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Animation to Player\
**Type:** Action without value\
**Description:** Plays a specific animation for the player.

**Usage example:** 
```ts
player::play_animation_action("DAMAGE");

#Or dry by keywords

player::play_animation_action(animation="DAMAGE");
```

**Arguments:**

| **Name**    | **Type**                                                                                                                            | **Description** |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `animation` | Marker<br/>**DAMAGE** - Taking Damage<br/>**JUMPSCARE** - Ancient Guardian<br/>**TOTEM** - Totem<br/>**WAKE_UP** - Wake Up From Bed | Animation Type  |
<h3 id=player_play_hurt_animation>
  <code>player::play_hurt_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Hurt Animation\
**Type:** Action without value\
**Description:** Plays a hurt animation for the player with a given angle.

**Usage example:** 
```ts
player::play_hurt_animation(1);

#Or dry by keywords

player::play_hurt_animation(yaw=1);
```

**Arguments:**

| **Name** | **Type** | **Description**                       |
| -------- | -------- | ------------------------------------- |
| `yaw`    | Number   | Received damage angle (from 0 to 360) |
<h3 id=player_play_sound>
  <code>player::play_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Sound\
**Type:** Action without value\
**Description:** Plays a sound to the player.

**Usage example:** 
```ts
player::play_sound(sound("entity.zombie.hurt"), location(0,0,0,0,0));

#Or dry by keywords

player::play_sound(sound=sound("entity.zombie.hurt"), location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `sound`    | Sound    | Sound to Play   |
| `location` | Location | Sound Location  |
<h3 id=player_play_sound_from_entity>
  <code>player::play_sound_from_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play sound from entity\
**Type:** Action without value\
**Description:** Plays a sound from the specified entity to the player.\
**Additional info:**\
&nbsp;&nbsp;Stereo sounds will not play.

**Usage example:** 
```ts
player::play_sound_from_entity("name_or_uuid", [sound("entity.zombie.hurt"), sound("entity.zombie.hurt")]);

#Or dry by keywords

player::play_sound_from_entity(name_or_uuid="name_or_uuid", sounds=[sound("entity.zombie.hurt"), sound("entity.zombie.hurt")]);
```

**Arguments:**

| **Name**       | **Type**    | **Description**     |
| -------------- | ----------- | ------------------- |
| `name_or_uuid` | Text        | Entity name or UUID |
| `sounds`       | list[Sound] | Sound to play       |
<h3 id=player_play_sound_sequence>
  <code>player::play_sound_sequence</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Sound Sequence\
**Type:** Action without value\
**Description:** Plays a sequence of sounds to the player with a delay between each sound.

**Usage example:** 
```ts
player::play_sound_sequence([sound("entity.zombie.hurt"), sound("entity.zombie.hurt")], location(0,0,0,0,0), 1);

#Or dry by keywords

player::play_sound_sequence(sounds=[sound("entity.zombie.hurt"), sound("entity.zombie.hurt")], location=location(0,0,0,0,0), delay=1);
```

**Arguments:**

| **Name**   | **Type**    | **Description** |
| ---------- | ----------- | --------------- |
| `sounds`   | list[Sound] | Playable Sounds |
| `location` | Location    | Sound Location  |
| `delay`    | Number      | Delay in ticks  |
<h3 id=player_randomized_teleport>
  <code>player::randomized_teleport</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Randomized Teleport\
**Type:** Action without value\
**Description:** Teleports the player to a random location.

**Usage example:** 
```ts
player::randomized_teleport([location(0,0,0,0,0), location(0,0,0,0,0)], "FALSE", "FALSE", "FALSE");

#Or dry by keywords

player::randomized_teleport(locations=[location(0,0,0,0,0), location(0,0,0,0,0)], keep_rotation="FALSE", keep_velocity="FALSE", dismount="FALSE");
```

**Arguments:**

| **Name**        | **Type**                                               | **Description**            |
| --------------- | ------------------------------------------------------ | -------------------------- |
| `locations`     | list[Location]                                         | Teleport Locations         |
| `keep_rotation` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Keep current rotation      |
| `keep_velocity` | Marker<br/>**FALSE** - Keep Off<br/>**TRUE** - Enable  | Keep Momentum              |
| `dismount`      | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes         | Dismount after teleporting |
<h3 id=player_redirect_world>
  <code>player::redirect_world</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send to Another World\
**Type:** Action without value\
**Description:** Redirects the player to the world with the given ID.

**Usage example:** 
```ts
player::redirect_world("world_id");

#Or dry by keywords

player::redirect_world(world_id="world_id");
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `world_id` | Text     | World ID        |
<h3 id=player_remove_boss_bar>
  <code>player::remove_boss_bar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Boss Bar\
**Type:** Action without value\
**Description:** Removes an existing boss bar from a specific player.

**Usage example:** 
```ts
player::remove_boss_bar("id");

#Or dry by keywords

player::remove_boss_bar(id="id");
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `id`     | Text     | Boss Bar ID     |
<h3 id=player_remove_disguise>
  <code>player::remove_disguise</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Disguise\
**Type:** Action without value\
**Description:** Removes a player\'s disguise.

**Usage example:** 
```ts
player::remove_disguise();
```

<h3 id=player_remove_display_blocks>
  <code>player::remove_display_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Display Blocks\
**Type:** Action without value\
**Description:** Removes all client-sided display blocks (maximum size: 500).

**Usage example:** 
```ts
player::remove_display_blocks(location(0,0,0,0,0), location(0,0,0,0,0));

#Or dry by keywords

player::remove_display_blocks(pos_1=location(0,0,0,0,0), pos_2=location(0,0,0,0,0));
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `pos_1`  | Location | First corner    |
| `pos_2`  | Location | Second corner   |
<h3 id=player_remove_inventory_menu_row>
  <code>player::remove_inventory_menu_row</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Inventory Menu Rows\
**Type:** Action without value\
**Description:** Removes one or more rows from the \"Chest\" inventory.

**Usage example:** 
```ts
player::remove_inventory_menu_row(1, "BUTTON");

#Or dry by keywords

player::remove_inventory_menu_row(size=1, position="BUTTON");
```

**Arguments:**

| **Name**   | **Type**                                                              | **Description** |
| ---------- | --------------------------------------------------------------------- | --------------- |
| `size`     | Number                                                                | Number of Rows  |
| `position` | Marker<br/>**BUTTON** - Remove Row Below<br/>**TOP** - Remove Top Row | Row Position    |
<h3 id=player_remove_items>
  <code>player::remove_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Items\
**Type:** Action without value\
**Description:** Removes the specified items from the player\'s inventory.

**Usage example:** 
```ts
player::remove_items([item("stick"), item("stick")]);

#Or dry by keywords

player::remove_items(items=[item("stick"), item("stick")]);
```

**Arguments:**

| **Name** | **Type**   | **Description** |
| -------- | ---------- | --------------- |
| `items`  | list[Item] | Items to Remove |
<h3 id=player_remove_pose>
  <code>player::remove_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reset Player Pose\
**Type:** Action without value\
**Description:** Resets a player\'s pose.

**Usage example:** 
```ts
player::remove_pose();
```

<h3 id=player_remove_potion_effect>
  <code>player::remove_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Potion Effect\
**Type:** Action without value\
**Description:** Removes the selected effects from a player.

**Usage example:** 
```ts
player::remove_potion_effect([potion("slow_falling"), potion("slow_falling")]);

#Or dry by keywords

player::remove_potion_effect(potions=[potion("slow_falling"), potion("slow_falling")]);
```

**Arguments:**

| **Name**  | **Type**     | **Description**   |
| --------- | ------------ | ----------------- |
| `potions` | list[Potion] | Effects to Remove |
<h3 id=player_remove_self_disguise>
  <code>player::remove_self_disguise</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Self Disguise\
**Type:** Action without value\
**Description:** Removes a player\'s disguise that only they can see.

**Usage example:** 
```ts
player::remove_self_disguise();
```

<h3 id=player_remove_skin>
  <code>player::remove_skin</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Skin\
**Type:** Action without value\
**Description:** Returns the normal skin of the event target.

**Usage example:** 
```ts
player::remove_skin();
```

<h3 id=player_remove_world_border>
  <code>player::remove_world_border</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove World Border\
**Type:** Action without value\
**Description:** Set the player\'s world border to the default value.

**Usage example:** 
```ts
player::remove_world_border();
```

<h3 id=player_replace_items>
  <code>player::replace_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Items\
**Type:** Action without value\
**Description:** Replaces the specified items in the inventory with a specific item.

**Usage example:** 
```ts
player::replace_items([item("stick"), item("stick")], item("stick"), 1);

#Or dry by keywords

player::replace_items(items=[item("stick"), item("stick")], replace=item("stick"), count=1);
```

**Arguments:**

| **Name**  | **Type**   | **Description**            |
| --------- | ---------- | -------------------------- |
| `items`   | list[Item] | Replace Items              |
| `replace` | Item       | Replacement Item           |
| `count`   | Number     | Number of Items to Replace |
<h3 id=player_reset_weather>
  <code>player::reset_weather</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reset Weather\
**Type:** Action without value\
**Description:** Resets player weather

**Usage example:** 
```ts
player::reset_weather();
```

<h3 id=player_ride_entity>
  <code>player::ride_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Ride an Entity\
**Type:** Action without value\
**Description:** Rides the player on an entity or another player.

**Usage example:** 
```ts
player::ride_entity("name_or_uuid");

#Or dry by keywords

player::ride_entity(name_or_uuid="name_or_uuid");
```

**Arguments:**

| **Name**       | **Type** | **Description**            |
| -------------- | -------- | -------------------------- |
| `name_or_uuid` | Text     | Name or UUID of the target |
<h3 id=player_save_inventory>
  <code>player::save_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Save Current Inventory\
**Type:** Action without value\
**Description:** Saves the player\'s current inventory. It can be loaded later using \'Load Saved Inventory\'.

**Usage example:** 
```ts
player::save_inventory();
```

<h3 id=player_self_disguise_as_block>
  <code>player::self_disguise_as_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise Self as a Block\
**Type:** Action without value\
**Description:** Disguises the player as a block, but this disguise is only visible to that player.

**Usage example:** 
```ts
player::self_disguise_as_block(item("stone"));

#Or dry by keywords

player::self_disguise_as_block(block=item("stone"));
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `block`  | Block    | Disguise Block  |
<h3 id=player_self_disguise_as_entity>
  <code>player::self_disguise_as_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise Self as an Entity\
**Type:** Action without value\
**Description:** Maximizes the player as an entity, but this disguise is only visible to that player.

**Usage example:** 
```ts
player::self_disguise_as_entity(item("stick"));

#Or dry by keywords

player::self_disguise_as_entity(entity_type=item("stick"));
```

**Arguments:**

| **Name**      | **Type** | **Description**    |
| ------------- | -------- | ------------------ |
| `entity_type` | Item     | Entity to Disguise |
<h3 id=player_self_disguise_as_item>
  <code>player::self_disguise_as_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise Self As Item\
**Type:** Action without value\
**Description:** Disguises the player as an item onto to themself.

**Usage example:** 
```ts
player::self_disguise_as_item(item("stick"));

#Or dry by keywords

player::self_disguise_as_item(item=item("stick"));
```

**Arguments:**

| **Name** | **Type** | **Description**     |
| -------- | -------- | ------------------- |
| `item`   | Item     | Item to disguise as |
<h3 id=player_send_action_bar>
  <code>player::send_action_bar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Action Bar Message\
**Type:** Action without value\
**Description:** Shows an action bar to the selected player.

**Usage example:** 
```ts
player::send_action_bar(["messages", "messages"], "CONCATENATION");

#Or dry by keywords

player::send_action_bar(messages=["messages", "messages"], merging="CONCATENATION");
```

**Arguments:**

| **Name**   | **Type**                                                               | **Description**     |
| ---------- | ---------------------------------------------------------------------- | ------------------- |
| `messages` | list[Text]                                                             | Action Bar Messages |
| `merging`  | Marker<br/>**CONCATENATION** - Merge<br/>**SPACES** - Space Separation | Merge Text          |
<h3 id=player_send_advancement>
  <code>player::send_advancement</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send an Advancement to a Player\
**Type:** Action without value\
**Description:** Shows a player a custom advancement popup.

**Usage example:** 
```ts
player::send_advancement(item("stick"), "name", "CHALLENGE");

#Or dry by keywords

player::send_advancement(icon=item("stick"), name="name", frame="CHALLENGE");
```

**Arguments:**

| **Name** | **Type**                                                                        | **Description**  |
| -------- | ------------------------------------------------------------------------------- | ---------------- |
| `icon`   | Item                                                                            | Icon             |
| `name`   | Text                                                                            | Name             |
| `frame`  | Marker<br/>**CHALLENGE** - Challenge<br/>**GOAL** - Goal<br/>**TASK** - Regular | Achievement Type |
<h3 id=player_send_break_animation>
  <code>player::send_break_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Block Break Animation\
**Type:** Action without value\
**Description:** Shows a block breaking animation for the player without affecting other players.

**Usage example:** 
```ts
player::send_break_animation([location(0,0,0,0,0), location(0,0,0,0,0)], 1);

#Or dry by keywords

player::send_break_animation(locations=[location(0,0,0,0,0), location(0,0,0,0,0)], stage=1);
```

**Arguments:**

| **Name**    | **Type**       | **Description**             |
| ----------- | -------------- | --------------------------- |
| `locations` | list[Location] | Block Locations             |
| `stage`     | Number         | Block Break Level (0 to 10) |
<h3 id=player_send_dialogue>
  <code>player::send_dialogue</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dialogue\
**Type:** Action without value\
**Description:** Sends multiple chat messages to selected players with a delay after each message.

**Usage example:** 
```ts
player::send_dialogue(["messages", "messages"], 1);

#Or dry by keywords

player::send_dialogue(messages=["messages", "messages"], delay=1);
```

**Arguments:**

| **Name**   | **Type**   | **Description**        |
| ---------- | ---------- | ---------------------- |
| `messages` | list[Text] | Text to send           |
| `delay`    | Number     | Delay between messages |
<h3 id=player_send_hover>
  <code>player::send_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Hover Message\
**Type:** Action without value\
**Description:** Sends a message to the selected player. When a player \'hovers\' over it, a second message appears.

**Usage example:** 
```ts
player::send_hover("message", "hover");

#Or dry by keywords

player::send_hover(message="message", hover="hover");
```

**Arguments:**

| **Name**  | **Type** | **Description** |
| --------- | -------- | --------------- |
| `message` | Text     | Message to Send |
| `hover`   | Text     | Hover Message   |
<h3 id=player_send_message>
  <code>player::message</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Message\
**Type:** Action without value\
**Description:** Sends a message to the chat to the specified players.

**Usage example:** 
```ts
player::message(["messages", "messages"], "CONCATENATION");

#Or dry by keywords

player::message(messages=["messages", "messages"], merging="CONCATENATION");
```

**Arguments:**

| **Name**   | **Type**                                                                                                       | **Description** |
| ---------- | -------------------------------------------------------------------------------------------------------------- | --------------- |
| `messages` | list[Text]                                                                                                     | Text to send    |
| `merging`  | Marker<br/>**CONCATENATION** - Merge<br/>**SEPARATE_LINES** - Separate Lines<br/>**SPACES** - Space Separation | Merge Text      |
<h3 id=player_send_minimessage>
  <code>player::send_minimessage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send a MiniMessage\
**Type:** Action without value\
**Description:** Sends a MiniMessage message to a player.

**Usage example:** 
```ts
player::send_minimessage("minimessage");

#Or dry by keywords

player::send_minimessage(minimessage="minimessage");
```

**Arguments:**

| **Name**      | **Type** | **Description**            |
| ------------- | -------- | -------------------------- |
| `minimessage` | Text     | MiniMessage Format Message |
<h3 id=player_send_title>
  <code>player::send_title</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Title\
**Type:** Action without value\
**Description:** Shows two captions to the screen for the selected player - a title and a subtitle.

**Usage example:** 
```ts
player::send_title("title", "subtitle", 1, 2, 3);

#Or dry by keywords

player::send_title(title="title", subtitle="subtitle", fade_in=1, stay=2, fade_out=3);
```

**Arguments:**

| **Name**   | **Type** | **Description**        |
| ---------- | -------- | ---------------------- |
| `title`    | Text     | Title Text             |
| `subtitle` | Text     | Subtitle Text          |
| `fade_in`  | Number   | Fade Time in Ticks     |
| `stay`     | Number   | Tick Delay             |
| `fade_out` | Number   | Fade Out Time in Ticks |
<h3 id=player_set_absorption_health>
  <code>player::set_absorption_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Bonus Health\
**Type:** Action without value\
**Description:** Sets a player\'s bonus health.

**Usage example:** 
```ts
player::set_absorption_health(1);

#Or dry by keywords

player::set_absorption_health(health=1);
```

**Arguments:**

| **Name** | **Type** | **Description**        |
| -------- | -------- | ---------------------- |
| `health` | Number   | Amount of Extra Health |
<h3 id=player_set_air_ticks>
  <code>player::set_air_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Remaining Air\
**Type:** Action without value\
**Description:** Sets the player\'s remaining air.

**Usage example:** 
```ts
player::set_air_ticks(1);

#Or dry by keywords

player::set_air_ticks(ticks=1);
```

**Arguments:**

| **Name** | **Type** | **Description**                    |
| -------- | -------- | ---------------------------------- |
| `ticks`  | Number   | Amount of Air Remaining (in ticks) |
<h3 id=player_set_allow_flying>
  <code>player::set_allow_flying</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Flying Permission\
**Type:** Action without value\
**Description:** Sets the flying permission for the player.

**Usage example:** 
```ts
player::set_allow_flying("FALSE");

#Or dry by keywords

player::set_allow_flying(allow_flying="FALSE");
```

**Arguments:**

| **Name**       | **Type**                                     | **Description** |
| -------------- | -------------------------------------------- | --------------- |
| `allow_flying` | Marker<br/>**FALSE** - No<br/>**TRUE** - Yes | Can fly         |
<h3 id=player_set_armor>
  <code>player::set_armor</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor\
**Type:** Action without value\
**Description:** Sets the player\'s armor.\
**Additional info:**\
&nbsp;&nbsp;Any item or block will appear on the head when placed in the helmet slot.

**Usage example:** 
```ts
player::set_armor(item("stick"), item("stick"), item("stick"), item("stick"));

#Or dry by keywords

player::set_armor(helmet=item("stick"), chestplate=item("stick"), leggings=item("stick"), boots=item("stick"));
```

**Arguments:**

| **Name**     | **Type** | **Description** |
| ------------ | -------- | --------------- |
| `helmet`     | Item     | Helmet          |
| `chestplate` | Item     | Chestplate      |
| `leggings`   | Item     | Leggings        |
| `boots`      | Item     | Boots           |
<h3 id=player_set_arrows_in_body>
  <code>player::set_arrows_in_body</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Arrows On Player\
**Type:** Action without value\
**Description:** Displays a set number of arrows on the player.

**Usage example:** 
```ts
player::set_arrows_in_body(1);

#Or dry by keywords

player::set_arrows_in_body(amount=1);
```

**Arguments:**

| **Name** | **Type** | **Description**             |
| -------- | -------- | --------------------------- |
| `amount` | Number   | Number of arrows to display |
<h3 id=player_set_attack_speed>
  <code>player::set_attack_speed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Attack Speed\
**Type:** Action without value\
**Description:** Sets the player\'s attack speed.

**Usage example:** 
```ts
player::set_attack_speed(1);

#Or dry by keywords

player::set_attack_speed(speed=1);
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `speed`  | Number   | Attack Speed    |
<h3 id=player_set_attribute>
  <code>player::set_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Attribute\
**Type:** Action without value\
**Description:** Sets the specified attribute of a player.

**Usage example:** 
```ts
player::set_attribute(1, "GENERIC_ARMOR");

#Or dry by keywords

player::set_attribute(value=1, attribute_type="GENERIC_ARMOR");
```

**Arguments:**

| **Name**         | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Description** |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `value`          | Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Attribute Value |
| `attribute_type` | Marker<br/>**GENERIC_ARMOR** - Armor points (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Armor toughness points (generic.armor_toughness)<br/>**GENERIC_ATTACK_DAMAGE** - Attack damage (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Attack knockback (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Attack speed (generic.attack_speed)<br/>**GENERIC_BURNING_TIME** - Burning Time<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Explosion Knockback Resistance<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Fall Damage Multiplier<br/>**GENERIC_FLYING_SPEED** - Flying speed (generic.flying_speed)<br/>**GENERIC_FOLLOW_RANGE** - Follow range (generic.follow_range)<br/>**GENERIC_GRAVITY** - Gravity<br/>**GENERIC_JUMP_STRENGTH** - Jump Strength<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Knockback resistance (generic.knockback_resistance)<br/>**GENERIC_LUCK** - Fishing luck (generic.luck)<br/>**GENERIC_MAX_ABSORPTION** - Max absorption (generic.max_absorption)<br/>**GENERIC_MAX_HEALTH** - Max health (generic.max_health)<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Movement Efficiency<br/>**GENERIC_MOVEMENT_SPEED** - Movement speed (generic.movement_speed)<br/>**GENERIC_OXYGEN_BONUS** - Oxygen Bonus<br/>**GENERIC_SAFE_FALL_DISTANCE** - Safe Fall Distance<br/>**GENERIC_SCALE** - Scale<br/>**GENERIC_STEP_HEIGHT** - Step Height<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Water Movement Efficiency<br/>**PLAYER_BLOCK_BREAK_SPEED** - Block Breaking Speed<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - Block Interaction Range<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - Entity Interaction Range<br/>**PLAYER_MINING_EFFICIENCY** - Mining Efficiency<br/>**PLAYER_SNEAKING_SPEED** - Sneaking Speed<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Submerged Mining Speed<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - Sweeping Damage Ratio<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Zomie spawn reinforcements | Attribute Type  |
<h3 id=player_set_bee_stingers_in_body>
  <code>player::set_bee_stingers_in_body</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Bee Stingers On Player\
**Type:** Action without value\
**Description:** Displays a set number of bee stingers on the player.

**Usage example:** 
```ts
player::set_bee_stingers_in_body(1);

#Or dry by keywords

player::set_bee_stingers_in_body(amount=1);
```

**Arguments:**

| **Name** | **Type** | **Description**                   |
| -------- | -------- | --------------------------------- |
| `amount` | Number   | Amount of bee stingers to display |
<h3 id=player_set_block_opened_state>
  <code>player::set_block_opened_state</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Open/Close Block\
**Type:** Action without value\
**Description:** Display block opening/closing to the player without changing the block state for other players.
**Work_with:**\
&nbsp;&nbsp;Chest\
&nbsp;&nbsp;Trap Chest\
&nbsp;&nbsp;Ender Chest\
&nbsp;&nbsp;Shulker Boxes\
&nbsp;&nbsp;Barrel

**Usage example:** 
```ts
player::set_block_opened_state(location(0,0,0,0,0), "FALSE");

#Or dry by keywords

player::set_block_opened_state(location=location(0,0,0,0,0), is_opened="FALSE");
```

**Arguments:**

| **Name**    | **Type**                                          | **Description** |
| ----------- | ------------------------------------------------- | --------------- |
| `location`  | Location                                          | Block Location  |
| `is_opened` | Marker<br/>**FALSE** - Closed<br/>**TRUE** - Open | State           |
<h3 id=player_set_boss_bar>
  <code>player::set_boss_bar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Boss Bar\
**Type:** Action without value\
**Description:** Sets a custom boss bar for a specific player.

**Usage example:** 
```ts
player::set_boss_bar("id", "title", 1, "DARK_SKY", "NOTCHED_10", "BLUE");

#Or dry by keywords

player::set_boss_bar(id="id", title="title", progress=1, sky_effect="DARK_SKY", style="NOTCHED_10", color="BLUE");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                                          | **Description**   |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `id`         | Text                                                                                                                                                              | Boss Bar ID       |
| `title`      | Text                                                                                                                                                              | Text              |
| `progress`   | Number                                                                                                                                                            | Occupancy (0-100) |
| `sky_effect` | Marker<br/>**DARK_SKY** - Dark Sky<br/>**FOG** - Fog<br/>**FOG_AND_DARK_SKY** - Fog and dark sky<br/>**NONE** - None                                              | Sky Effect        |
| `style`      | Marker<br/>**NOTCHED_10** - 10 segments<br/>**NOTCHED_12** - 12 segments<br/>**NOTCHED_20** - 20 segments<br/>**NOTCHED_6** - 6 segments<br/>**PROGRESS** - Solid | Style             |
| `color`      | Marker<br/>**BLUE** - Blue<br/>**GREEN** - Green<br/>**PINK** - Pink<br/>**PURPLE** - Purple<br/>**RED** - Red<br/>**WHITE** - White<br/>**YELLOW** - Yellow      | Color             |
<h3 id=player_set_chat_completions>
  <code>player::set_chat_completions</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Modify Chat Suggestions\
**Type:** Action without value\
**Description:** Modifies the player\'s auto-completion suggestions shown when typing in chat.

**Usage example:** 
```ts
player::set_chat_completions(["completions", "completions"], "ADD");

#Or dry by keywords

player::set_chat_completions(completions=["completions", "completions"], setting_mode="ADD");
```

**Arguments:**

| **Name**       | **Type**                                                           | **Description**   |
| -------------- | ------------------------------------------------------------------ | ----------------- |
| `completions`  | list[Text]                                                         | Chat Suggestions  |
| `setting_mode` | Marker<br/>**ADD** - Add<br/>**REMOVE** - Remove<br/>**SET** - Set | Modification Type |
<h3 id=player_set_collidable>
  <code>player::set_collidable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Collidable Mode\
**Type:** Action without value\
**Description:** Sets the player\'s creature collision mode.

**Usage example:** 
```ts
player::set_collidable("FALSE");

#Or dry by keywords

player::set_collidable(collidable="FALSE");
```

**Arguments:**

| **Name**     | **Type**                                                                                              | **Description** |
| ------------ | ----------------------------------------------------------------------------------------------------- | --------------- |
| `collidable` | Marker<br/>**FALSE** - Does not collide with other players<br/>**TRUE** - Collides with other players | Collision Mode  |
<h3 id=player_set_compass_target>
  <code>player::set_compass_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Compass Target\
**Type:** Action without value\
**Description:** Sets the player\'s compass target in which direction the compass needle will point.

**Usage example:** 
```ts
player::set_compass_target(location(0,0,0,0,0));

#Or dry by keywords

player::set_compass_target(location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `location` | Location | Compass Target  |
<h3 id=player_set_cursor_item>
  <code>player::set_cursor_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item on Cursor\
**Type:** Action without value\
**Description:** Sets an item on the player\'s cursor.

**Usage example:** 
```ts
player::set_cursor_item(item("stick"));

#Or dry by keywords

player::set_cursor_item(item=item("stick"));
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `item`   | Item     | Item to Set     |
<h3 id=player_set_death_drops>
  <code>player::set_death_drops</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Death Drops\
**Type:** Action without value\
**Description:** Sets items dropped from a player upon death.

**Usage example:** 
```ts
player::set_death_drops("FALSE");

#Or dry by keywords

player::set_death_drops(death_drops="FALSE");
```

**Arguments:**

| **Name**      | **Type**                                                 | **Description** |
| ------------- | -------------------------------------------------------- | --------------- |
| `death_drops` | Marker<br/>**FALSE** - Does not drop<br/>**TRUE** - Drop | Item Drops      |
<h3 id=player_set_death_screen_score>
  <code>player::set_death_screen_score</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
player::set_death_screen_score(1);

#Or dry by keywords

player::set_death_screen_score(score=1);
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `score`  | Number   | None            |
<h3 id=player_set_default_visible>
  <code>player::set_default_visible</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visibility\
**Type:** Action without value\
**Description:** Sets the player\'s visibility.\
**Additional info:**\
&nbsp;&nbsp;Player\'s visibility can be changed via the \"Hide Entity\" action.

**Usage example:** 
```ts
player::set_default_visible("TRUE");

#Or dry by keywords

player::set_default_visible(default_visible="TRUE");
```

**Arguments:**

| **Name**          | **Type**                                                | **Description** |
| ----------------- | ------------------------------------------------------- | --------------- |
| `default_visible` | Marker<br/>**TRUE** - Visible<br/>**FALSE** - Invisible | Visibility      |
<h3 id=player_set_ender_chest_contents>
  <code>player::set_ender_chest_contents</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Ender Chest Contents\
**Type:** Action without value\
**Description:** Sets items in the player\'s Ender Chest inventory.

**Usage example:** 
```ts
player::set_ender_chest_contents([item("stick"), item("stick")]);

#Or dry by keywords

player::set_ender_chest_contents(items=[item("stick"), item("stick")]);
```

**Arguments:**

| **Name** | **Type**   | **Description** |
| -------- | ---------- | --------------- |
| `items`  | list[Item] | Items to Set    |
<h3 id=player_set_entity_glowing>
  <code>player::set_entity_glowing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Entity Glowing\
**Type:** Action without value\
**Description:** Toggles entity glowing effect for a player.

**Usage example:** 
```ts
player::set_entity_glowing(["name_or_uuid", "name_or_uuid"], "AQUA", "FALSE");

#Or dry by keywords

player::set_entity_glowing(name_or_uuid=["name_or_uuid", "name_or_uuid"], color="AQUA", glow="FALSE");
```

**Arguments:**

| **Name**       | **Type**                                                                                                                                                                                                                                                                                                                                                                                                             | **Description**     |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `name_or_uuid` | list[Text]                                                                                                                                                                                                                                                                                                                                                                                                           | Entity name or UUID |
| `color`        | Marker<br/>**AQUA** - Light-blue<br/>**BLACK** - Black<br/>**BLUE** - Blue<br/>**DARK_AQUA** - Cyan<br/>**DARK_BLUE** - Dark-blue<br/>**DARK_GRAY** - Gray<br/>**DARK_GREEN** - Dark-green<br/>**DARK_PURPLE** - Dark-purple<br/>**DARK_RED** - Dark-red<br/>**GOLD** - Gold<br/>**GRAY** - Light-gray<br/>**GREEN** - Green<br/>**PURPLE** - Purple<br/>**RED** - Red<br/>**WHITE** - White<br/>**YELLOW** - Yellow | Glow color          |
| `glow`         | Marker<br/>**FALSE** - Turn off<br/>**TRUE** - Turn on                                                                                                                                                                                                                                                                                                                                                               | Glowing             |
<h3 id=player_set_equipment>
  <code>player::set_equipment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Equipment\
**Type:** Action without value\
**Description:** Sets an item to one of player\'s equipment slots (armor and items in hand).

**Usage example:** 
```ts
player::set_equipment(item("stick"), "BODY");

#Or dry by keywords

player::set_equipment(item=item("stick"), slot="BODY");
```

**Arguments:**

| **Name** | **Type**                                                                                                                                                            | **Description** |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `item`   | Item                                                                                                                                                                | Items to give   |
| `slot`   | Marker<br/>**BODY** - Body<br/>**CHEST** - Chest<br/>**FEET** - Boots<br/>**HAND** - Main Hand<br/>**HEAD** - Helmet<br/>**LEGS** - Legs<br/>**OFF_HAND** - OffHand | Equipment slot  |
<h3 id=player_set_exhaustion>
  <code>player::set_exhaustion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Exhaustion Level\
**Type:** Action without value\
**Description:** Sets the exhaustion level of the player.

**Usage example:** 
```ts
player::set_exhaustion(1, "ADD");

#Or dry by keywords

player::set_exhaustion(exhaustion=1, mode="ADD");
```

**Arguments:**

| **Name**     | **Type**                                   | **Description**  |
| ------------ | ------------------------------------------ | ---------------- |
| `exhaustion` | Number                                     | Exhaustion Level |
| `mode`       | Marker<br/>**ADD** - Add<br/>**SET** - Set | Set Mode         |
<h3 id=player_set_experience>
  <code>player::set_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Experience\
**Type:** Action without value\
**Description:** Sets a player\'s level.

**Usage example:** 
```ts
player::set_experience(1, "LEVEL");

#Or dry by keywords

player::set_experience(experience=1, mode="LEVEL");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                  | **Description** |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `experience` | Number                                                                                                                    | Amount to Set   |
| `mode`       | Marker<br/>**LEVEL** - As Level<br/>**LEVEL_PERCENTAGE** - As a percentage of level<br/>**POINTS** - As experience points | Set Type        |
<h3 id=player_set_fall_distance>
  <code>player::set_fall_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fall Distance\
**Type:** Action without value\
**Description:** Sets the distance at which the player falls.

**Usage example:** 
```ts
player::set_fall_distance(1);

#Or dry by keywords

player::set_fall_distance(distance=1);
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `distance` | Number   | Fall Distance   |
<h3 id=player_set_fire_ticks>
  <code>player::set_fire_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player on Fire\
**Type:** Action without value\
**Description:** Sets a player on fire for the selected amount of time.

**Usage example:** 
```ts
player::set_fire_ticks(1);

#Or dry by keywords

player::set_fire_ticks(ticks=1);
```

**Arguments:**

| **Name** | **Type** | **Description**  |
| -------- | -------- | ---------------- |
| `ticks`  | Number   | Duration (Ticks) |
<h3 id=player_set_flying>
  <code>player::set_flying</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Flying\
**Type:** Action without value\
**Description:** Sets the player\'s flying state.

**Usage example:** 
```ts
player::set_flying("FALSE");

#Or dry by keywords

player::set_flying(is_flying="FALSE");
```

**Arguments:**

| **Name**    | **Type**                                               | **Description** |
| ----------- | ------------------------------------------------------ | --------------- |
| `is_flying` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Flying          |
<h3 id=player_set_fog_distance>
  <code>player::set_fog_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fog Distance\
**Type:** Action without value\
**Description:** Sets the chunk draw distance for the player. The value \"-1\" resets to standard.

**Usage example:** 
```ts
player::set_fog_distance(1);

#Or dry by keywords

player::set_fog_distance(distance=1);
```

**Arguments:**

| **Name**   | **Type** | **Description**               |
| ---------- | -------- | ----------------------------- |
| `distance` | Number   | Fog distance in chunks (2-32) |
<h3 id=player_set_food>
  <code>player::set_food</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Hunger\
**Type:** Action without value\
**Description:** Sets a player\'s hunger level.

**Usage example:** 
```ts
player::set_food(1, "ADD");

#Or dry by keywords

player::set_food(food=1, mode="ADD");
```

**Arguments:**

| **Name** | **Type**                                   | **Description** |
| -------- | ------------------------------------------ | --------------- |
| `food`   | Number                                     | Hunger Level    |
| `mode`   | Marker<br/>**ADD** - Add<br/>**SET** - Set | Set Mode        |
<h3 id=player_set_freeze_ticks>
  <code>player::set_freeze_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Freeze Time\
**Type:** Action without value\
**Description:** Sets the player\'s freeze time (the number of ticks the player has spent in powder snow).

**Usage example:** 
```ts
player::set_freeze_ticks(1, "FALSE");

#Or dry by keywords

player::set_freeze_ticks(ticks=1, ticking_locked="FALSE");
```

**Arguments:**

| **Name**         | **Type**                                             | **Description**                     |
| ---------------- | ---------------------------------------------------- | ----------------------------------- |
| `ticks`          | Number                                               | Freeze Time in Ticks                |
| `ticking_locked` | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | State Locked (Time will not change) |
<h3 id=player_set_gamemode>
  <code>player::set_gamemode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Game Mode\
**Type:** Action without value\
**Description:** Sets the game mode for the player.

**Usage example:** 
```ts
player::set_gamemode("ADVENTURE", "KEEP_ORIGINAL");

#Or dry by keywords

player::set_gamemode(gamemode="ADVENTURE", flight_mode="KEEP_ORIGINAL");
```

**Arguments:**

| **Name**      | **Type**                                                                                                                   | **Description** |
| ------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `gamemode`    | Marker<br/>**ADVENTURE** - Adventure<br/>**CREATIVE** - Creative<br/>**SPECTATOR** - Spectator<br/>**SURVIVAL** - Survival | Game Mode       |
| `flight_mode` | Marker<br/>**KEEP_ORIGINAL** - Keep Original<br/>**RESPECT_GAMEMODE** - Respect Game Mode                                  | Flight Mode     |
<h3 id=player_set_gliding>
  <code>player::set_gliding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Elytra Flying\
**Type:** Action without value\
**Description:** Sets the player\'s elytra flying state.

**Usage example:** 
```ts
player::set_gliding("FALSE");

#Or dry by keywords

player::set_gliding(is_gliding="FALSE");
```

**Arguments:**

| **Name**     | **Type**                                               | **Description** |
| ------------ | ------------------------------------------------------ | --------------- |
| `is_gliding` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Elytra Flying   |
<h3 id=player_set_health>
  <code>player::set_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Health\
**Type:** Action without value\
**Description:** Sets a player\'s health to the selected amount.

**Usage example:** 
```ts
player::set_health(1);

#Or dry by keywords

player::set_health(health=1);
```

**Arguments:**

| **Name** | **Type** | **Description**  |
| -------- | -------- | ---------------- |
| `health` | Number   | Amount of Health |
<h3 id=player_set_hotbar_slot>
  <code>player::set_hotbar_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Hotbar Slot\
**Type:** Action without value\
**Description:** Sets the selected slot to a player.

**Usage example:** 
```ts
player::set_hotbar_slot(1);

#Or dry by keywords

player::set_hotbar_slot(slot=1);
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `slot`   | Number   | Slot            |
<h3 id=player_set_instant_respawn>
  <code>player::set_instant_respawn</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Instant Respawn\
**Type:** Action without value\
**Description:** Sets an instant respawn for a player.

**Usage example:** 
```ts
player::set_instant_respawn("FALSE");

#Or dry by keywords

player::set_instant_respawn(instant_respawn="FALSE");
```

**Arguments:**

| **Name**          | **Type**                                               | **Description** |
| ----------------- | ------------------------------------------------------ | --------------- |
| `instant_respawn` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Instant Respawn |
<h3 id=player_set_inventory_kept>
  <code>player::set_inventory_kept</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Keep Inventory\
**Type:** Action without value\
**Description:** Sets the player to keep their inventory on death.

**Usage example:** 
```ts
player::set_inventory_kept("FALSE");

#Or dry by keywords

player::set_inventory_kept(kept="FALSE");
```

**Arguments:**

| **Name** | **Type**                                               | **Description** |
| -------- | ------------------------------------------------------ | --------------- |
| `kept`   | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Keep Inventory  |
<h3 id=player_set_inventory_menu_item>
  <code>player::set_inventory_menu_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Into Inventory Slot\
**Type:** Action without value\
**Description:** Sets an item to the specified slot in the player\'s open inventory menu.

**Usage example:** 
```ts
player::set_inventory_menu_item(item("stick"), 1);

#Or dry by keywords

player::set_inventory_menu_item(item=item("stick"), slot=1);
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `item`   | Item     | Item to Set     |
| `slot`   | Number   | Set Slot        |
<h3 id=player_set_inventory_menu_name>
  <code>player::set_inventory_menu_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Inventory Menu Name\
**Type:** Action without value\
**Description:** Sets a new name for the player\'s opened inventory menu.

**Usage example:** 
```ts
player::set_inventory_menu_name("text");

#Or dry by keywords

player::set_inventory_menu_name(text="text");
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `text`   | Text     | New name        |
<h3 id=player_set_invulnerability_ticks>
  <code>player::set_invulnerability_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Invulnerability Duration\
**Type:** Action without value\
**Description:** Sets the invulnerability duration for the player.

**Usage example:** 
```ts
player::set_invulnerability_ticks(1);

#Or dry by keywords

player::set_invulnerability_ticks(ticks=1);
```

**Arguments:**

| **Name** | **Type** | **Description**                  |
| -------- | -------- | -------------------------------- |
| `ticks`  | Number   | Invulnerability Duration (Ticks) |
<h3 id=player_set_item_cooldown>
  <code>player::set_item_cooldown</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Cooldown\
**Type:** Action without value\
**Description:** Applies a cooldown visual effect to all items of the selected type.\
**Additional info:**\
&nbsp;&nbsp;Cooldown will be applied to all items of the selected type.

**Usage example:** 
```ts
player::set_item_cooldown(1, item("stick"), sound("entity.zombie.hurt"));

#Or dry by keywords

player::set_item_cooldown(cooldown=1, item=item("stick"), sound=sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type** | **Description**   |
| ---------- | -------- | ----------------- |
| `cooldown` | Number   | Delay in ticks    |
| `item`     | Item     | Delay Item Type   |
| `sound`    | Sound    | Delay reset sound |
<h3 id=player_set_items>
  <code>player::set_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Items\
**Type:** Action without value\
**Description:** Sets a player\'s inventory accordingly to items from the chest.

**Usage example:** 
```ts
player::set_items([item("stick"), item("stick")]);

#Or dry by keywords

player::set_items(items=[item("stick"), item("stick")]);
```

**Arguments:**

| **Name** | **Type**   | **Description**                             |
| -------- | ---------- | ------------------------------------------- |
| `items`  | list[Item] | Items to give out in their respective slots |
<h3 id=player_set_max_health>
  <code>player::set_max_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Max Health\
**Type:** Action without value\
**Description:** Sets a player\'s maximum health.

**Usage example:** 
```ts
player::set_max_health(1, "FALSE");

#Or dry by keywords

player::set_max_health(health=1, heal="FALSE");
```

**Arguments:**

| **Name** | **Type**                                       | **Description** |
| -------- | ---------------------------------------------- | --------------- |
| `health` | Number                                         | Max Health      |
| `heal`   | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes | Heal Player     |
<h3 id=player_set_movement_speed>
  <code>player::set_movement_speed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Movement Speed\
**Type:** Action without value\
**Description:** Sets the player\'s movement speed.

**Usage example:** 
```ts
player::set_movement_speed(1, "FLY");

#Or dry by keywords

player::set_movement_speed(distance=1, movement_type="FLY");
```

**Arguments:**

| **Name**        | **Type**                                     | **Description** |
| --------------- | -------------------------------------------- | --------------- |
| `distance`      | Number                                       | Movement Speed  |
| `movement_type` | Marker<br/>**FLY** - Fly<br/>**WALK** - Walk | Movement Type   |
<h3 id=player_set_nametag_visible>
  <code>player::set_nametag_visible</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Nickname Visible\
**Type:** Action without value\
**Description:** Display or hide the nickname above the head.

**Usage example:** 
```ts
player::set_nametag_visible("FALSE");

#Or dry by keywords

player::set_nametag_visible(visible="FALSE");
```

**Arguments:**

| **Name**  | **Type**                                                     | **Description** |
| --------- | ------------------------------------------------------------ | --------------- |
| `visible` | Marker<br/>**FALSE** - Do not display<br/>**TRUE** - Display | Nick Display    |
<h3 id=player_set_player_list_info>
  <code>player::set_player_list_info</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Tab List Text\
**Type:** Action without value\
**Description:** Sets the text above or below the player list for a player.

**Usage example:** 
```ts
player::set_player_list_info(["text", "text"], "CONCATENATION", "FOOTER");

#Or dry by keywords

player::set_player_list_info(text=["text", "text"], merging="CONCATENATION", position="FOOTER");
```

**Arguments:**

| **Name**   | **Type**                                                                                                       | **Description**     |
| ---------- | -------------------------------------------------------------------------------------------------------------- | ------------------- |
| `text`     | list[Text]                                                                                                     | Text in Player List |
| `merging`  | Marker<br/>**CONCATENATION** - Merge<br/>**SEPARATE_LINES** - Separate Lines<br/>**SPACES** - Space Separation | Merge Text          |
| `position` | Marker<br/>**FOOTER** - Bottom<br/>**HEADER** - Top                                                            | Position            |
<h3 id=player_set_pose>
  <code>player::set_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Pose\
**Type:** Action without value\
**Description:** Sets a specific player pose.

**Usage example:** 
```ts
player::set_pose("CROAKING", "FALSE");

#Or dry by keywords

player::set_pose(pose="CROAKING", locked="FALSE");
```

**Arguments:**

| **Name** | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Description** |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `pose`   | Marker<br/>**CROAKING** - Croaking (for Toads)<br/>**CROUCHING** - Crouching<br/>**DIGGING** - Digging (For Guardian)<br/>**DYING** - Death<br/>**EMERGING** - Emerging from the Earth (for Guardian)<br/>**FALL_FLYING** - Elytra Flying<br/>**INHALING** - Inhalation (for Vortex)<br/>**LONG_JUMPING** - Long Jump<br/>**ROARING** - Roar (for Guardian)<br/>**SHOOTING** - Shooting (for Vortex)<br/>**SITTING** - Sitting<br/>**SLEEPING** - Sleeping<br/>**SLIDING** - Sliding (for Vortex)<br/>**SNEAKING** - None<br/>**SNIFFING** - Sniffing (for Guardian)<br/>**SPIN_ATTACK** - Use Thrust<br/>**STANDING** - Normal State<br/>**SWIMMING** - Swimming<br/>**USING_TONGUE** - Using Tongue (For Toads) | Display Pose    |
| `locked` | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Lock Pose       |
<h3 id=player_set_pvp>
  <code>player::set_pvp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set PVP Enabled\
**Type:** Action without value\
**Description:** Sets the player\'s permission to attack and damage other players.

**Usage example:** 
```ts
player::set_pvp("FALSE");

#Or dry by keywords

player::set_pvp(pvp="FALSE");
```

**Arguments:**

| **Name** | **Type**                                       | **Description** |
| -------- | ---------------------------------------------- | --------------- |
| `pvp`    | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes | Can Attack      |
<h3 id=player_set_rain_level>
  <code>player::set_rain_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rain Level\
**Type:** Action without value\
**Description:** Sets player\'s level of rain

**Usage example:** 
```ts
player::set_rain_level(1);

#Or dry by keywords

player::set_rain_level(rain_level=1);
```

**Arguments:**

| **Name**     | **Type** | **Description**               |
| ------------ | -------- | ----------------------------- |
| `rain_level` | Number   | Level of rain (from 0 to 100) |
<h3 id=player_set_rotation>
  <code>player::set_rotation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation\
**Type:** Action without value\
**Description:** Sets the player\'s rotation.

**Usage example:** 
```ts
player::set_rotation(1, 2);

#Or dry by keywords

player::set_rotation(yaw=1, pitch=2);
```

**Arguments:**

| **Name** | **Type** | **Description**           |
| -------- | -------- | ------------------------- |
| `yaw`    | Number   | Horizontal rotation (yaw) |
| `pitch`  | Number   | Pitch                     |
<h3 id=player_set_rotation_by_vector>
  <code>player::set_rotation_by_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation By Vector\
**Type:** Action without value\
**Description:** Sets player rotation by vector.

**Usage example:** 
```ts
player::set_rotation_by_vector(vector(0,0,0));

#Or dry by keywords

player::set_rotation_by_vector(vector=vector(0,0,0));
```

**Arguments:**

| **Name** | **Type** | **Description**  |
| -------- | -------- | ---------------- |
| `vector` | Vector   | Vector to Rotate |
<h3 id=player_set_saturation>
  <code>player::set_saturation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Saturation\
**Type:** Action without value\
**Description:** Sets a player\'s secondary hunger level (saturation).

**Usage example:** 
```ts
player::set_saturation(1, "ADD");

#Or dry by keywords

player::set_saturation(saturation=1, mode="ADD");
```

**Arguments:**

| **Name**     | **Type**                                   | **Description**  |
| ------------ | ------------------------------------------ | ---------------- |
| `saturation` | Number                                     | Saturation Level |
| `mode`       | Marker<br/>**ADD** - Add<br/>**SET** - Set | Set Mode         |
<h3 id=player_set_simulation_distance>
  <code>player::set_simulation_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Simulation Distance\
**Type:** Action without value\
**Description:** Sets the chunk simulation distance for the player.

**Usage example:** 
```ts
player::set_simulation_distance(1);

#Or dry by keywords

player::set_simulation_distance(distance=1);
```

**Arguments:**

| **Name**   | **Type** | **Description**                      |
| ---------- | -------- | ------------------------------------ |
| `distance` | Number   | Simulation Distance in Chunks (2-32) |
<h3 id=player_set_skin>
  <code>player::set_skin</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Skin\
**Type:** Action without value\
**Description:** Sets the specified player\'s skin for the target of the event.

**Usage example:** 
```ts
player::set_skin("name_or_uuid", "MOJANG");

#Or dry by keywords

player::set_skin(name_or_uuid="name_or_uuid", server_type="MOJANG");
```

**Arguments:**

| **Name**       | **Type**                                                         | **Description**          |
| -------------- | ---------------------------------------------------------------- | ------------------------ |
| `name_or_uuid` | Text                                                             | Name or UUID of the skin |
| `server_type`  | Marker<br/>**MOJANG** - Mojang Skin<br/>**SERVER** - JustMC Skin | Skin Server Type         |
<h3 id=player_set_slot_item>
  <code>player::set_slot_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item In Slot\
**Type:** Action without value\
**Description:** Sets an item to a slot in a player\'s inventory.

**Usage example:** 
```ts
player::set_slot_item(item("stick"), 1);

#Or dry by keywords

player::set_slot_item(item=item("stick"), slot=1);
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `item`   | Item     | Item to give    |
| `slot`   | Number   | Giveaway slot   |
<h3 id=player_set_spawn_point>
  <code>player::set_spawn_point</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Spawn Location\
**Type:** Action without value\
**Description:** Sets the player to a new spawn location.

**Usage example:** 
```ts
player::set_spawn_point(location(0,0,0,0,0));

#Or dry by keywords

player::set_spawn_point(spawn_point=location(0,0,0,0,0));
```

**Arguments:**

| **Name**      | **Type** | **Description** |
| ------------- | -------- | --------------- |
| `spawn_point` | Location | Spawn Location  |
<h3 id=player_set_thunder_level>
  <code>player::set_thunder_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Thunder Level\
**Type:** Action without value\
**Description:** Sets player\'s level of thunder\
**Additional info:**\
&nbsp;&nbsp;Rainy weather is required to set thunder level

**Usage example:** 
```ts
player::set_thunder_level(1);

#Or dry by keywords

player::set_thunder_level(thunder_level=1);
```

**Arguments:**

| **Name**        | **Type** | **Description**                  |
| --------------- | -------- | -------------------------------- |
| `thunder_level` | Number   | Level of thunder (from 0 to 100) |
<h3 id=player_set_tick_rate>
  <code>player::set_tick_rate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Tick Rate\
**Type:** Action without value\
**Description:** Sets the player\'s tick rate.

**Usage example:** 
```ts
player::set_tick_rate(1);

#Or dry by keywords

player::set_tick_rate(tick_rate=1);
```

**Arguments:**

| **Name**    | **Type** | **Description** |
| ----------- | -------- | --------------- |
| `tick_rate` | Number   | Tick rate       |
<h3 id=player_set_time>
  <code>player::set_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Time\
**Type:** Action without value\
**Description:** Set a player\'s time without changing it for other players.

**Usage example:** 
```ts
player::set_time(1);

#Or dry by keywords

player::set_time(time=1);
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `time`   | Number   | Time in ticks   |
<h3 id=player_set_velocity>
  <code>player::set_velocity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Velocity\
**Type:** Action without value\
**Description:** Launches the player along the specified vector.

**Usage example:** 
```ts
player::set_velocity(vector(0,0,0), "FALSE");

#Or dry by keywords

player::set_velocity(velocity=vector(0,0,0), increment="FALSE");
```

**Arguments:**

| **Name**    | **Type**                                               | **Description**          |
| ----------- | ------------------------------------------------------ | ------------------------ |
| `velocity`  | Vector                                                 | Motion Vector            |
| `increment` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Consider current inertia |
<h3 id=player_set_visual_fire>
  <code>player::set_visual_fire</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visual Fire\
**Type:** Action without value\
**Description:** Sets the player to a burning effect.

**Usage example:** 
```ts
player::set_visual_fire("FALSE");

#Or dry by keywords

player::set_visual_fire(visual_fire="FALSE");
```

**Arguments:**

| **Name**      | **Type**                                             | **Description** |
| ------------- | ---------------------------------------------------- | --------------- |
| `visual_fire` | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Visual Fire     |
<h3 id=player_set_weather>
  <code>player::set_weather</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Weather\
**Type:** Action without value\
**Description:** Set player weather without affecting other players.

**Usage example:** 
```ts
player::set_weather("CLEAR");

#Or dry by keywords

player::set_weather(weather_type="CLEAR");
```

**Arguments:**

| **Name**       | **Type**                                              | **Description** |
| -------------- | ----------------------------------------------------- | --------------- |
| `weather_type` | Marker<br/>**CLEAR** - Solar<br/>**DOWNFALL** - Rainy | Weather Type    |
<h3 id=player_set_world_border>
  <code>player::set_world_border</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Border\
**Type:** Action without value\
**Description:** Set the world border for a player without changing it for other players.

**Usage example:** 
```ts
player::set_world_border(location(0,0,0,0,0), 1, 2);

#Or dry by keywords

player::set_world_border(center=location(0,0,0,0,0), size=1, warning=2);
```

**Arguments:**

| **Name**  | **Type** | **Description**                    |
| --------- | -------- | ---------------------------------- |
| `center`  | Location | World Border Center                |
| `size`    | Number   | World Border Size                  |
| `warning` | Number   | Distance before red border appears |
<h3 id=player_shift_world_border>
  <code>player::shift_world_border</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift World Border\
**Type:** Action without value\
**Description:** Move the world border for the player without changing it for other players.

**Usage example:** 
```ts
player::shift_world_border(1, 2, 3);

#Or dry by keywords

player::shift_world_border(old_size=1, size=2, time=3);
```

**Arguments:**

| **Name**   | **Type** | **Description**       |
| ---------- | -------- | --------------------- |
| `old_size` | Number   | Old World Border Size |
| `size`     | Number   | New World Border Size |
| `time`     | Number   | Size Time             |
<h3 id=player_show_debug_marker>
  <code>player::show_debug_marker</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Debug Marker\
**Type:** Action without value\
**Description:** Shows the player a debug marker at the location at the specified time. Red and blue colors work for players on version 1.19.4 and above.\
**Additional info:**\
&nbsp;&nbsp;Leave the \"Display Name\" argument blank to hide the name completely.

**Usage example:** 
```ts
player::show_debug_marker(location(0,0,0,0,0), "name", 1, 2, 3, 4, 5);

#Or dry by keywords

player::show_debug_marker(location=location(0,0,0,0,0), name="name", duration=1, red=2, green=3, blue=4, alpha=5);
```

**Arguments:**

| **Name**   | **Type** | **Description**                     |
| ---------- | -------- | ----------------------------------- |
| `location` | Location | Spawn Location                      |
| `name`     | Text     | Display Name                        |
| `duration` | Number   | Duration in milliseconds (optional) |
| `red`      | Number   | Color Red (0 to 100)                |
| `green`    | Number   | Green Color (0 to 100)              |
| `blue`     | Number   | Color Blue (0 to 100)               |
| `alpha`    | Number   | Transparency (0 to 100)             |
<h3 id=player_show_demo_screen>
  <code>player::show_demo_screen</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Demo Screen\
**Type:** Action without value\
**Description:** Shows the demo screen to the player.

**Usage example:** 
```ts
player::show_demo_screen();
```

<h3 id=player_show_dialog_menu_from_nbt>
  <code>player::show_dialog_menu_from_nbt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::show_dialog_menu_from_nbt("dialog_nbt");

#Or dry by keywords

player::show_dialog_menu_from_nbt(dialog_nbt="dialog_nbt");
```

**Arguments:**

| **Name**     | **Type** | **Description** |
| ------------ | -------- | --------------- |
| `dialog_nbt` | Text     | None            |
<h3 id=player_show_inventory_menu>
  <code>player::show_inventory_menu</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Inventory Menu\
**Type:** Action without value\
**Description:** Shows the player an inventory menu with selected items and title.

**Usage example:** 
```ts
player::show_inventory_menu([item("stick"), item("stick")], "name", "ANVIL");

#Or dry by keywords

player::show_inventory_menu(items=[item("stick"), item("stick")], name="name", inventory_type="ANVIL");
```

**Arguments:**

| **Name**         | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Description** |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `items`          | list[Item]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Inventory Items |
| `name`           | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Inventory name  |
| `inventory_type` | Marker<br/>**ANVIL** - Anvil<br/>**BARREL** - Barrel<br/>**BEACON** - Beacon<br/>**BLAST_FURNACE** - Smelter<br/>**BREWING** - Potion Brewing<br/>**CARTOGRAPHY** - Cartographer\'s Desk<br/>**CHEST** - Chest<br/>**COMPOSTER** - Composter<br/>**CRAFTER** - Crafter<br/>**CRAFTING** - Not opened<br/>**CREATIVE** - Creative Inventory<br/>**DISPENSER** - Dispenser<br/>**DROPPER** - Dropper<br/>**ENCHANTING** - Enchanting Table<br/>**ENDER_CHEST** - Ender Chest<br/>**FURNACE** - Furnace<br/>**GRINDSTONE** - Grindstone<br/>**HOPPER** - Hopper<br/>**LECTERN** - Pulpit<br/>**LOOM** - Loom<br/>**MERCHANT** - Merchant<br/>**PLAYER** - Player Inventory<br/>**SHULKER_BOX** - Shulker Box<br/>**SMITHING** - Blacksmith\'s Table<br/>**SMOKER** - Smoker<br/>**STONECUTTER** - Stonecutter<br/>**WORKBENCH** - Workbench | Inventory Type  |
<h3 id=player_show_scoreboard>
  <code>player::show_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Scoreboard\
**Type:** Action without value\
**Description:** Displays a specific scoreboard to a player. The specified scoreboard must have at least one value to be displayed.

**Usage example:** 
```ts
player::show_scoreboard("id");

#Or dry by keywords

player::show_scoreboard(id="id");
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `id`     | Text     | Scoreboard ID   |
<h3 id=player_show_win_screen>
  <code>player::show_win_screen</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Credits Screen\
**Type:** Action without value\
**Description:** Shows the player the credits screen.\
**Additional info:**\
&nbsp;&nbsp;The \"Close Inventory Menu\" action closes the credits.

**Usage example:** 
```ts
player::show_win_screen();
```

<h3 id=player_spectate_target>
  <code>player::spectate_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Spectate Target\
**Type:** Action without value\
**Description:** Sets the player\'s spectate target in spectator mode.

**Usage example:** 
```ts
player::spectate_target("name_or_uuid");

#Or dry by keywords

player::spectate_target(name_or_uuid="name_or_uuid");
```

**Arguments:**

| **Name**       | **Type** | **Description**            |
| -------------- | -------- | -------------------------- |
| `name_or_uuid` | Text     | Name or UUID of the target |
<h3 id=player_stop_sound>
  <code>player::stop_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Stop Sound\
**Type:** Action without value\
**Description:** Stops all or certain sounds for the player.

**Usage example:** 
```ts
player::stop_sound([sound("entity.zombie.hurt"), sound("entity.zombie.hurt")]);

#Or dry by keywords

player::stop_sound(sounds=[sound("entity.zombie.hurt"), sound("entity.zombie.hurt")]);
```

**Arguments:**

| **Name** | **Type**    | **Description** |
| -------- | ----------- | --------------- |
| `sounds` | list[Sound] | Stop Effects    |
<h3 id=player_stop_sounds_by_source>
  <code>player::stop_sounds_by_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Stop Sounds By Source\
**Type:** Action without value\
**Description:** Stops all sounds from the specified source.

**Usage example:** 
```ts
player::stop_sounds_by_source("AMBIENT");

#Or dry by keywords

player::stop_sounds_by_source(source="AMBIENT");
```

**Arguments:**

| **Name** | **Type**                                                                                                                                                                                                                                                                                                                                                                             | **Description** |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `source` | Marker<br/>**AMBIENT** - Environment (ambient)<br/>**BLOCK** - Blocks<br/>**HOSTILE** - Hostile creatures (hostile)<br/>**MASTER** - General (master)<br/>**MUSIC** - Music (music)<br/>**NEUTRAL** - Friendly Creatures (neutral)<br/>**PLAYER** - Players (player)<br/>**RECORD** - Music blocks (record)<br/>**VOICE** - Voice/Speech (voice)<br/>**WEATHER** - Weather (weather) | Sound Source    |
<h3 id=player_swing_hand>
  <code>player::swing_hand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Swing Hand Animation\
**Type:** Action without value\
**Description:** Plays a swinging hand animation for the player.

**Usage example:** 
```ts
player::swing_hand("MAIN");

#Or dry by keywords

player::swing_hand(hand_type="MAIN");
```

**Arguments:**

| **Name**    | **Type**                                       | **Description** |
| ----------- | ---------------------------------------------- | --------------- |
| `hand_type` | Marker<br/>**MAIN** - Main<br/>**OFF** - Minor | Hand Type       |
<h3 id=player_teleport>
  <code>player::teleport</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Teleport\
**Type:** Action without value\
**Description:** Teleports the player to the selected location.\
**Additional info:**\
&nbsp;&nbsp;Closes an open inventory menu.

**Usage example:** 
```ts
player::teleport(location(0,0,0,0,0), "FALSE", "FALSE", "FALSE");

#Or dry by keywords

player::teleport(location=location(0,0,0,0,0), keep_rotation="FALSE", keep_velocity="FALSE", dismount="FALSE");
```

**Arguments:**

| **Name**        | **Type**                                               | **Description**            |
| --------------- | ------------------------------------------------------ | -------------------------- |
| `location`      | Location                                               | New Position               |
| `keep_rotation` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled | Keep Current Rotation      |
| `keep_velocity` | Marker<br/>**FALSE** - Keep Off<br/>**TRUE** - Enable  | Keep Momentum              |
| `dismount`      | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes         | Dismount After Teleporting |
<h3 id=player_teleport_sequence>
  <code>player::teleport_sequence</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Teleport Sequence\
**Type:** Action without value\
**Description:** Teleports the player between locations with the specified delay.

**Usage example:** 
```ts
player::teleport_sequence([location(0,0,0,0,0), location(0,0,0,0,0)], 1);

#Or dry by keywords

player::teleport_sequence(locations=[location(0,0,0,0,0), location(0,0,0,0,0)], delay=1);
```

**Arguments:**

| **Name**    | **Type**       | **Description**    |
| ----------- | -------------- | ------------------ |
| `locations` | list[Location] | Teleport Locations |
| `delay`     | Number         | Delay in ticks     |
