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

<h3 id=if_player_chat_message_equals>
  <code>player::chat_message_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Chat Message Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the player's message is equal to the selected one.

**Usage example:** 
```ts
if(player::chat_message_equals(["chat_messages", "chat_messages"]){
    player::message("Condition is true");
}
```

<h3 id=if_player_collides_at_location>
  <code>player::collides_at_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

**Usage example:** 
```ts
if(player::collides_at_location(location(0,0,0,0,0)){
    player::message("Condition is true");
}
```

<h3 id=if_player_collides_using_hitbox>
  <code>player::collides_using_hitbox</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

**Usage example:** 
```ts
if(player::collides_using_hitbox(location(0,0,0,0,0),location(0,0,0,0,0)){
    player::message("Condition is true");
}
```

<h3 id=if_player_collides_with_entity>
  <code>player::collides_with_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

**Usage example:** 
```ts
if(player::collides_with_entity("name_or_uuid","OVERLAPS"){
    player::message("Condition is true");
}
```

<h3 id=if_player_cursor_item_equals>
  <code>player::cursor_item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Cursor Item Is Equal To\
**Type:** Action that checks the conditions\
**Description:** Checks if the item at the player's cursor is equal to the selected item.

**Usage example:** 
```ts
if(player::cursor_item_equals([item("stick"), item("stick")],"EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_gamemode_equals>
  <code>player::gamemode_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Game Mode Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the player's gamemode is equal to the selected one.

**Usage example:** 
```ts
if(player::gamemode_equals("SURVIVAL"){
    player::message("Condition is true");
}
```

<h3 id=if_player_has_item>
  <code>player::has_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has an Item\
**Type:** Action that checks the conditions\
**Description:** Checks if the player has an item in their inventory.

**Usage example:** 
```ts
if(player::has_item([item("stick"), item("stick")],"ANY","EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_has_item_at_least>
  <code>player::has_item_at_least</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has an Item in Quantity\
**Type:** Action that checks the conditions\
**Description:** Checks if a player has an item in a certain quantity.

**Usage example:** 
```ts
if(player::has_item_at_least(item("stick"),1,"EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_has_item_in_slot>
  <code>player::has_item_in_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has an Item In Slot\
**Type:** Action that checks the conditions\
**Description:** Checks if a player has an item in a specific inventory slot.

**Usage example:** 
```ts
if(player::has_item_in_slot([item("stick"), item("stick")],[1, 2],"EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_has_potion_effect>
  <code>player::has_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has Potion Effect\
**Type:** Action that checks the conditions\
**Description:** Checks if a player has the effect of a potion.

**Usage example:** 
```ts
if(player::has_potion_effect([potion("slow_falling"), potion("slow_falling")],"ANY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_has_privilege>
  <code>player::has_privilege</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has Permission\
**Type:** Action that checks the conditions\
**Description:** Checks if a player has certain rights in the world.\
**Additional info:**\
&nbsp;&nbsp;If the "Check Accuracy" marker is enabled, building and development permissions will be checked even if the player is whitelisted.

**Usage example:** 
```ts
if(player::has_privilege("BUILDER","TRUE"){
    player::message("Condition is true");
}
```

<h3 id=if_player_has_room_for_item>
  <code>player::has_room_for_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Has a Room For Item\
**Type:** Action that checks the conditions\
**Description:** Checks if the player has room for one or more items in their inventory.

**Usage example:** 
```ts
if(player::has_room_for_item([item("stick"), item("stick")],"ANY","ENTIRE_INVENTORY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_hotbar_slot_equals>
  <code>player::hotbar_slot_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Hotbar Slot Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the player's current hotbar slot matches slot 1 to 9 in the chest.

**Usage example:** 
```ts
if(player::hotbar_slot_equals(1){
    player::message("Condition is true");
}
```

<h3 id=if_player_inventory_menu_slot_equals>
  <code>player::inventory_menu_slot_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Inventory Slot Contains\
**Type:** Action that checks the conditions\
**Description:** Checks if a player with an open inventory currently has a specific item in a slot.

**Usage example:** 
```ts
if(player::inventory_menu_slot_equals([item("stick"), item("stick")],[1, 2],"EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_inventory_type_open>
  <code>player::inventory_type_open</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Open Inventory Type Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a player's inventory type is open.

**Usage example:** 
```ts
if(player::inventory_type_open("CHEST"){
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
if(player::is_blocking(){
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
if(player::is_disguised(){
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
if(player::is_flying(){
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
if(player::is_gliding(){
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
if(player::holding([item("stick"), item("stick")],"EITHER_HAND","EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_in_area>
  <code>player::in_area</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Inside Region\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is in a certain region.

**Usage example:** 
```ts
if(player::in_area(location(0,0,0,0,0),location(0,0,0,0,0),"TRUE","POINT","OVERLAPS"){
    player::message("Condition is true");
}
```

<h3 id=if_player_item_is_not_on_cooldown>
  <code>player::item_is_not_on_cooldown</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Has No Cooldown\
**Type:** Action that checks the conditions\
**Description:** Checks if the player's item has a cooldown applicable to a specific item type.

**Usage example:** 
```ts
if(player::item_is_not_on_cooldown([item("stick"), item("stick")]){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_looking_at_block>
  <code>player::is_looking_at_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Looks at a Block\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is looking at a specific block or location.

**Usage example:** 
```ts
if(player::is_looking_at_block([item("stone"), item("stone")],[location(0,0,0,0,0), location(0,0,0,0,0)],1,"NEVER"){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_near>
  <code>player::is_near</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Near Location\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is near the specified location (Default: 5 blocks).

**Usage example:** 
```ts
if(player::is_near("TRUE",location(0,0,0,0,0),1){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_on_ground>
  <code>player::is_on_ground</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Is On Ground\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is not in the air.

**Usage example:** 
```ts
if(player::is_on_ground(){
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
if(player::is_online_mode(){
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
if(player::is_riding_entity(["entity_ids", "entity_ids"],"NEAREST"){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_self_disguised>
  <code>player::is_self_disguised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Self Disguised\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is disguised to himself.

**Usage example:** 
```ts
if(player::is_self_disguised(){
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
if(player::is_sleeping(){
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
if(player::is_sneaking(){
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
if(player::is_sprinting(){
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
if(player::is_standing_on_block([item("stone"), item("stone")],[location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE"){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_swimming>
  <code>player::is_swimming</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Swimming\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is swimming in water or lava.

**Usage example:** 
```ts
if(player::is_swimming(){
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
if(player::is_using_item([item("stick"), item("stick")],"EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_is_wearing_item>
  <code>player::is_wearing_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Wearing an Item\
**Type:** Action that checks the conditions\
**Description:** Checks if the player is wearing an item.

**Usage example:** 
```ts
if(player::is_wearing_item([item("stick"), item("stick")],"ANY","EXACTLY"){
    player::message("Condition is true");
}
```

<h3 id=if_player_name_equals>
  <code>player::name_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Name Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the player's name is equal to the name in the chest.

**Usage example:** 
```ts
if(player::name_equals(["names_or_uuids", "names_or_uuids"]){
    player::message("Condition is true");
}
```

<h3 id=player_add_inventory_menu_row>
  <code>player::add_inventory_menu_row</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Inventory Menu Row\
**Type:** Action without value\
**Description:** Adds a row with the specified items to the "Chest" type inventory.

**Usage example:** 
```ts
player::add_inventory_menu_row([item("stick"), item("stick")],"TOP");
```

<h3 id=player_allow_placing_breaking_blocks>
  <code>player::allow_placing_breaking_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::allow_placing_breaking_blocks("TRUE",[item("stone"), item("stone")]);
```

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
```

<h3 id=player_clear_chat>
  <code>player::clear_chat</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Chat\
**Type:** Action without value\
**Description:** Clears all messages from the selected player's chat window.

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
**Description:** Clears items in a player's Ender Chest inventory.

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
**Description:** Clears the player's inventory.

**Usage example:** 
```ts
player::clear_inventory("ENTIRE");
```

<h3 id=player_clear_items>
  <code>player::clear_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Items\
**Type:** Action without value\
**Description:** Removes all selected items from the player's inventory.

**Usage example:** 
```ts
player::clear_items([item("stick"), item("stick")]);
```

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

<h3 id=player_close_inventory>
  <code>player::close_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Close Inventory Menu\
**Type:** Action without value\
**Description:** Closes a player's opened inventory menu.

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
**Description:** Deals damage to the player.

**Usage example:** 
```ts
player::damage(1,"source");
```

<h3 id=player_disguise_as_block>
  <code>player::disguise_as_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Block\
**Type:** Action without value\
**Description:** Maxes the player under the selected block.

**Usage example:** 
```ts
player::disguise_as_block(item("stone"),"TRUE");
```

<h3 id=player_disguise_as_entity>
  <code>player::disguise_as_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise as Entity\
**Type:** Action without value\
**Description:** Maximizes the player to the selected entity.

**Usage example:** 
```ts
player::disguise_as_entity(item("stick"),"TRUE");
```

<h3 id=player_disguise_as_item>
  <code>player::disguise_as_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Disguise player as item\
**Type:** Action without value\
**Description:** Maxes the player as an item.

**Usage example:** 
```ts
player::disguise_as_item(item("stick"),"TRUE");
```

<h3 id=player_display_bell_ring>
  <code>player::display_bell_ring</code>
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
player::display_bell_ring(location(0,0,0,0,0),"DOWN");

#Or from the object

location(0,0,0,0,0).display_bell_ring("DOWN");
```

<h3 id=player_display_block>
  <code>player::display_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Block\
**Type:** Action without value\
**Description:** Display a block to a player without affecting other players.

**Usage example:** 
```ts
player::display_block([location(0,0,0,0,0), location(0,0,0,0,0)],item("stone"));
```

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
player::set_block_opened_state(location(0,0,0,0,0),"TRUE");
```

<h3 id=player_display_end_gateway_beam>
  <code>player::display_end_gateway_beam</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display End Gateway Beam Animation\
**Type:** Action without value\
**Description:** Displays an End Gateway beam animation at a specific location.

**Usage example:** 
```ts
player::display_end_gateway_beam(location(0,0,0,0,0),"LIGHT_PURPLE");
```

<h3 id=player_display_hologram>
  <code>player::display_hologram</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Hologram\
**Type:** Action without value\
**Description:** Shows the player a hologram. To remove a hologram at a location, leave the text blank.\
**Additional info:**\
&nbsp;&nbsp;To wrap text on a new line, use "n", eg : "Line1nLine2".

**Usage example:** 
```ts
player::display_hologram(location(0,0,0,0,0),"text");
```

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
```

<h3 id=player_display_particle>
  <code>player::display_particle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Effect\
**Type:** Action without value\
**Description:** Displays the particle effect at the selected location to the player.

**Usage example:** 
```ts
player::display_particle([particle("fire"), particle("fire")],[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

<h3 id=player_display_particle_circle>
  <code>player::display_particle_circle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::display_particle_circle(particle("fire"),location(0,0,0,0,0),1,2,3,vector(0,0,0),"DEGREES");
```

<h3 id=player_display_particle_cube>
  <code>player::display_particle_cube</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::display_particle_cube(particle("fire"),location(0,0,0,0,0),location(0,0,0,0,0),1,"SOLID");
```

<h3 id=player_display_particle_line>
  <code>player::display_particle_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Line\
**Type:** Action without value\
**Description:** Displays a particle effect line to the player from the start location to the end location at a specified distance.

**Usage example:** 
```ts
player::display_particle_line(particle("fire"),location(0,0,0,0,0),location(0,0,0,0,0),1,"POINTS");
```

<h3 id=player_display_particle_ray>
  <code>player::display_particle_ray</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Particle Ray\
**Type:** Action without value\
**Description:** Displays a particle effect ray to the player from the starting location along the specified vector with the specified distance.

**Usage example:** 
```ts
player::display_particle_ray(particle("fire"),location(0,0,0,0,0),vector(0,0,0),1,"POINTS");
```

<h3 id=player_display_particle_sphere>
  <code>player::display_particle_sphere</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::display_particle_sphere(particle("fire"),location(0,0,0,0,0),1,2);
```

<h3 id=player_display_particle_spiral>
  <code>player::display_particle_spiral</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::display_particle_spiral(particle("fire"),location(0,0,0,0,0),1,2,3,4,5,"DEGREES");
```

<h3 id=player_display_pick_up_animation>
  <code>player::display_pick_up_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Pick Up Animation\
**Type:** Action without value\
**Description:** Shows the player a pickup animation.\
**Additional info:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
player::display_pick_up_animation("collected_name_or_uuid","collector_name_or_uuid",1);
```

<h3 id=player_display_sign_text>
  <code>player::display_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Sign Text\
**Type:** Action without value\
**Description:** Show the sign's text change to the player without changing its text for other players.

**Usage example:** 
```ts
player::display_sign_text(location(0,0,0,0,0),"line_1","line_2","line_3","line_4");
```

<h3 id=player_display_vibration>
  <code>player::display_vibration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Display Vibration Particle\
**Type:** Action without value\
**Description:** Displays to the player a particle of vibration moving from one point to another.

**Usage example:** 
```ts
player::display_vibration(location(0,0,0,0,0),location(0,0,0,0,0),1);
```

<h3 id=player_expand_inventory_menu>
  <code>player::expand_inventory_menu</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Expand Inventory Menu\
**Type:** Action without value\
**Description:** Expands the player's opened inventory menu by the selected number of lines and populates it with the specified items.

**Usage example:** 
```ts
player::expand_inventory_menu([item("stick"), item("stick")],1);
```

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
```

<h3 id=player_force_flight_mode>
  <code>player::force_flight_mode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::force_flight_mode("TRUE");
```

<h3 id=player_give_experience>
  <code>player::give_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give Experience\
**Type:** Action without value\
**Description:** Gives a player an experience.

**Usage example:** 
```ts
player::give_experience(1,"POINTS");
```

<h3 id=player_give_items>
  <code>player::give_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give Item\
**Type:** Action without value\
**Description:** Gives players items from a chest.

**Usage example:** 
```ts
player::give_items([item("stick"), item("stick")],1);
```

<h3 id=player_give_potion_effect>
  <code>player::give_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give Potion Effect\
**Type:** Action without value\
**Description:** Gives the selected effects to the player.

**Usage example:** 
```ts
player::give_potion_effect([potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");
```

<h3 id=player_give_random_item>
  <code>player::give_random_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Give a Random Item\
**Type:** Action without value\
**Description:** Gives the player a random item or a stack of items in a chest.

**Usage example:** 
```ts
player::give_random_item([item("stick"), item("stick")]);
```

<h3 id=player_heal>
  <code>player::heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Heal Player\
**Type:** Action without value\
**Description:** Heals the player.

**Usage example:** 
```ts
player::heal(1);
```

<h3 id=player_hide_entity>
  <code>player::hide_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Hide Entity From Player\
**Type:** Action without value\
**Description:** Hides the specified entity from the player.

**Usage example:** 
```ts
player::hide_entity(["name_or_uuid", "name_or_uuid"],"TRUE");
```

<h3 id=player_hide_scoreboard>
  <code>player::hide_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Hide Scoreboard\
**Type:** Action without value\
**Description:** Hides the player's current scoreboard.

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
player::launch_forward(1,"TRUE","YAW_AND_PITCH");
```

<h3 id=player_launch_projectile>
  <code>player::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Projectile\
**Type:** Action without value\
**Description:** Launch a projectile from the player's location.

**Usage example:** 
```ts
player::launch_projectile(item("stick"),location(0,0,0,0,0),"name",1,2,particle("fire"));
```

<h3 id=player_launch_to_location>
  <code>player::launch_to_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch to Location\
**Type:** Action without value\
**Description:** Launches the player to the selected location.

**Usage example:** 
```ts
player::launch_to_location(location(0,0,0,0,0),1,"TRUE");
```

<h3 id=player_launch_up>
  <code>player::launch_up</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Launch Up\
**Type:** Action without value\
**Description:** Tosses the player up or down based on strength.

**Usage example:** 
```ts
player::launch_up(1,"TRUE");
```

<h3 id=player_load_inventory>
  <code>player::load_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Load Saved Inventory\
**Type:** Action without value\
**Description:** Loads the selected saved inventory.

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
```

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
```

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
```

<h3 id=player_play_hurt_animation>
  <code>player::play_hurt_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::play_hurt_animation(1);
```

<h3 id=player_play_sound>
  <code>player::play_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Sound\
**Type:** Action without value\
**Description:** Plays a sound to the player.

**Usage example:** 
```ts
player::play_sound(sound("entity.zombie.hurt"),location(0,0,0,0,0));
```

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
player::play_sound_from_entity([sound("entity.zombie.hurt"), sound("entity.zombie.hurt")],"name_or_uuid");
```

<h3 id=player_play_sound_sequence>
  <code>player::play_sound_sequence</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Play Sound Sequence\
**Type:** Action without value\
**Description:** Plays a sequence of sounds to the player with a delay between each sound.

**Usage example:** 
```ts
player::play_sound_sequence([sound("entity.zombie.hurt"), sound("entity.zombie.hurt")],1,location(0,0,0,0,0));
```

<h3 id=player_randomized_teleport>
  <code>player::randomized_teleport</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Randomized Teleport\
**Type:** Action without value\
**Description:** Teleports the player to a random location.

**Usage example:** 
```ts
player::randomized_teleport([location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE","TRUE","TRUE");
```

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
```

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
```

<h3 id=player_remove_disguise>
  <code>player::remove_disguise</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Disguise\
**Type:** Action without value\
**Description:** Removes a player's disguise.

**Usage example:** 
```ts
player::remove_disguise();
```

<h3 id=player_remove_display_blocks>
  <code>player::remove_display_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::remove_display_blocks(location(0,0,0,0,0),location(0,0,0,0,0));
```

<h3 id=player_remove_inventory_menu_row>
  <code>player::remove_inventory_menu_row</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Inventory Menu Rows\
**Type:** Action without value\
**Description:** Removes one or more rows from the "Chest" inventory.

**Usage example:** 
```ts
player::remove_inventory_menu_row(1,"TOP");
```

<h3 id=player_remove_items>
  <code>player::remove_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Items\
**Type:** Action without value\
**Description:** Removes the specified items from the player's inventory.

**Usage example:** 
```ts
player::remove_items([item("stick"), item("stick")]);
```

<h3 id=player_remove_pose>
  <code>player::remove_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reset Player Pose\
**Type:** Action without value\
**Description:** Resets a player's pose.

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
**Description:** Removes the selected effects from the player.

**Usage example:** 
```ts
player::remove_potion_effect([potion("slow_falling"), potion("slow_falling")]);
```

<h3 id=player_remove_self_disguise>
  <code>player::remove_self_disguise</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Self Disguise\
**Type:** Action without value\
**Description:** Removes a player's disguise that only they can see.

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
**Description:** Set the player's world border to the default value.

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
player::replace_items([item("stick"), item("stick")],item("stick"),1);
```

<h3 id=player_reset_weather>
  <code>player::reset_weather</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

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
```

<h3 id=player_save_inventory>
  <code>player::save_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Save Current Inventory\
**Type:** Action without value\
**Description:** Saves the player's current inventory. It can be loaded later using 'Load Saved Inventory'.

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
```

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
```

<h3 id=player_self_disguise_as_item>
  <code>player::self_disguise_as_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::self_disguise_as_item(item("stick"));
```

<h3 id=player_send_action_bar>
  <code>player::send_action_bar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Action Bar Message\
**Type:** Action without value\
**Description:** Shows an action bar to the selected player.

**Usage example:** 
```ts
player::send_action_bar(["messages", "messages"],"SPACES");
```

<h3 id=player_send_advancement>
  <code>player::send_advancement</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send an Advancement to a Player\
**Type:** Action without value\
**Description:** Shows the player a custom advancement popup.

**Usage example:** 
```ts
player::send_advancement("TASK","name",item("stick"));
```

<h3 id=player_send_break_animation>
  <code>player::send_break_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Block Break Animation\
**Type:** Action without value\
**Description:** Shows a block breaking animation for the player without affecting other players.

**Usage example:** 
```ts
player::send_break_animation([location(0,0,0,0,0), location(0,0,0,0,0)],1);
```

<h3 id=player_send_dialogue>
  <code>player::send_dialogue</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dialogue\
**Type:** Action without value\
**Description:** Sends multiple chat messages to selected players with a delay after each message.

**Usage example:** 
```ts
player::send_dialogue(["messages", "messages"],1);
```

<h3 id=player_send_hover>
  <code>player::send_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Hover Message\
**Type:** Action without value\
**Description:** Sends a message to the selected player. When the player 'hovers' over it, a second message appears.

**Usage example:** 
```ts
player::send_hover("message","hover");
```

<h3 id=player_send_message>
  <code>player::message</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Message\
**Type:** Action without value\
**Description:** Sends a message to the chat to the specified players.

**Usage example:** 
```ts
player::message(["messages", "messages"],"SPACES");
```

<h3 id=player_send_minimessage>
  <code>player::send_minimessage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send a MiniMessage\
**Type:** Action without value\
**Description:** Sends a MiniMessage message to the player.

**Usage example:** 
```ts
player::send_minimessage("minimessage");
```

<h3 id=player_send_title>
  <code>player::send_title</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Send Title\
**Type:** Action without value\
**Description:** Shows two captions to the screen for the selected player - a title and a subtitle.

**Usage example:** 
```ts
player::send_title("title","subtitle",1,2,3);
```

<h3 id=player_set_absorption_health>
  <code>player::set_absorption_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Bonus Health\
**Type:** Action without value\
**Description:** Sets the player's bonus health.

**Usage example:** 
```ts
player::set_absorption_health(1);
```

<h3 id=player_set_air_ticks>
  <code>player::set_air_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Remaining Air\
**Type:** Action without value\
**Description:** Sets the player's remaining air.

**Usage example:** 
```ts
player::set_air_ticks(1);
```

<h3 id=player_set_allow_flying>
  <code>player::set_allow_flying</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Flying Permission\
**Type:** Action without value\
**Description:** Sets the flying permission for the player.

**Usage example:** 
```ts
player::set_allow_flying("TRUE");
```

<h3 id=player_set_armor>
  <code>player::set_armor</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor\
**Type:** Action without value\
**Description:** Sets the player's armor.

**Usage example:** 
```ts
player::set_armor(item("stick"),item("stick"),item("stick"),item("stick"));
```

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
```

<h3 id=player_set_attack_speed>
  <code>player::set_attack_speed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Attack Speed\
**Type:** Action without value\
**Description:** Sets the player's attack speed.

**Usage example:** 
```ts
player::set_attack_speed(1);
```

<h3 id=player_set_attribute>
  <code>player::set_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::set_attribute(1,"MAX_HEALTH");
```

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
```

<h3 id=player_set_boss_bar>
  <code>player::set_boss_bar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Boss Bar\
**Type:** Action without value\
**Description:** Sets a custom boss bar for a specific player.

**Usage example:** 
```ts
player::set_boss_bar("id","title",1,"PINK","PROGRESS","NONE");
```

<h3 id=player_set_chat_completions>
  <code>player::set_chat_completions</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::set_chat_completions(["completions", "completions"],"ADD");
```

<h3 id=player_set_collidable>
  <code>player::set_collidable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Collidable Mode\
**Type:** Action without value\
**Description:** Sets the player's creature collision mode.

**Usage example:** 
```ts
player::set_collidable("TRUE");
```

<h3 id=player_set_compass_target>
  <code>player::set_compass_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Compass Target\
**Type:** Action without value\
**Description:** Sets the player's compass target in which direction the compass needle will point.

**Usage example:** 
```ts
player::set_compass_target(location(0,0,0,0,0));
```

<h3 id=player_set_cursor_item>
  <code>player::set_cursor_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item on Cursor\
**Type:** Action without value\
**Description:** Sets an item on the player's cursor.

**Usage example:** 
```ts
player::set_cursor_item(item("stick"));
```

<h3 id=player_set_death_drops>
  <code>player::set_death_drops</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Death Drops\
**Type:** Action without value\
**Description:** Sets items dropped from a player upon death.

**Usage example:** 
```ts
player::set_death_drops("TRUE");
```

<h3 id=player_set_ender_chest_contents>
  <code>player::set_ender_chest_contents</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Ender Chest Contents\
**Type:** Action without value\
**Description:** Sets items in the player's Ender Chest inventory.

**Usage example:** 
```ts
player::set_ender_chest_contents([item("stick"), item("stick")]);
```

<h3 id=player_set_entity_glowing>
  <code>player::set_entity_glowing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::set_entity_glowing(["name_or_uuid", "name_or_uuid"],"WHITE","TRUE");
```

<h3 id=player_set_equipment>
  <code>player::set_equipment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Equipment\
**Type:** Action without value\
**Description:** Sets an item to one of the player's equipment slots (armor and items in hand).

**Usage example:** 
```ts
player::set_equipment(item("stick"),"CHEST");
```

<h3 id=player_set_exhaustion>
  <code>player::set_exhaustion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::set_exhaustion(1,"SET");
```

<h3 id=player_set_experience>
  <code>player::set_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Experience\
**Type:** Action without value\
**Description:** Sets a player's level.

**Usage example:** 
```ts
player::set_experience(1,"POINTS");
```

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
```

<h3 id=player_set_fire_ticks>
  <code>player::set_fire_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player on Fire\
**Type:** Action without value\
**Description:** Sets the player on fire for the selected amount of time.

**Usage example:** 
```ts
player::set_fire_ticks(1);
```

<h3 id=player_set_flying>
  <code>player::set_flying</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Flying\
**Type:** Action without value\
**Description:** Sets the player's flying state.

**Usage example:** 
```ts
player::set_flying("TRUE");
```

<h3 id=player_set_fog_distance>
  <code>player::set_fog_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Fog Distance\
**Type:** Action without value\
**Description:** Sets the chunk draw distance for the player. The value "-1" resets to standard.

**Usage example:** 
```ts
player::set_fog_distance(1);
```

<h3 id=player_set_food>
  <code>player::set_food</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Hunger\
**Type:** Action without value\
**Description:** Sets the player's hunger level.

**Usage example:** 
```ts
player::set_food(1,"SET");
```

<h3 id=player_set_freeze_ticks>
  <code>player::set_freeze_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Freeze Time\
**Type:** Action without value\
**Description:** Sets the player's freeze time (the number of ticks the player has spent in loose snow).

**Usage example:** 
```ts
player::set_freeze_ticks(1,"TRUE");
```

<h3 id=player_set_gamemode>
  <code>player::set_gamemode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Game Mode\
**Type:** Action without value\
**Description:** Sets the game mode for the player.

**Usage example:** 
```ts
player::set_gamemode("SURVIVAL","RESPECT_GAMEMODE");
```

<h3 id=player_set_gliding>
  <code>player::set_gliding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Elytra Flying\
**Type:** Action without value\
**Description:** Sets the player's elytra flying state.

**Usage example:** 
```ts
player::set_gliding("TRUE");
```

<h3 id=player_set_health>
  <code>player::set_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Health\
**Type:** Action without value\
**Description:** Sets the player's health to the selected amount.

**Usage example:** 
```ts
player::set_health(1);
```

<h3 id=player_set_hotbar_slot>
  <code>player::set_hotbar_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Hotbar Slot\
**Type:** Action without value\
**Description:** Sets the selected slot to the player.

**Usage example:** 
```ts
player::set_hotbar_slot(1);
```

<h3 id=player_set_instant_respawn>
  <code>player::set_instant_respawn</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Instant Respawn\
**Type:** Action without value\
**Description:** Sets an instant respawn for a player.

**Usage example:** 
```ts
player::set_instant_respawn("TRUE");
```

<h3 id=player_set_inventory_kept>
  <code>player::set_inventory_kept</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Keep Inventory\
**Type:** Action without value\
**Description:** Sets the player to keep their inventory on death.

**Usage example:** 
```ts
player::set_inventory_kept("TRUE");
```

<h3 id=player_set_inventory_menu_item>
  <code>player::set_inventory_menu_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Into Inventory Slot\
**Type:** Action without value\
**Description:** Sets an item to the specified slot in the player's open inventory menu.

**Usage example:** 
```ts
player::set_inventory_menu_item(item("stick"),1);
```

<h3 id=player_set_inventory_menu_name>
  <code>player::set_inventory_menu_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Inventory Menu Name\
**Type:** Action without value\
**Description:** Sets a new name for the player's opened inventory menu.

**Usage example:** 
```ts
player::set_inventory_menu_name("text");
```

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
```

<h3 id=player_set_item_cooldown>
  <code>player::set_item_cooldown</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Cooldown\
**Type:** Action without value\
**Description:** Applies a cooldown visual effect to all items of the selected type.

**Usage example:** 
```ts
player::set_item_cooldown(item("stick"),1,sound("entity.zombie.hurt"));
```

<h3 id=player_set_items>
  <code>player::set_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Items\
**Type:** Action without value\
**Description:** Sets the player's inventory accordingly to items from the chest.

**Usage example:** 
```ts
player::set_items([item("stick"), item("stick")]);
```

<h3 id=player_set_max_health>
  <code>player::set_max_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Max Health\
**Type:** Action without value\
**Description:** Sets the player's maximum health.

**Usage example:** 
```ts
player::set_max_health(1,"TRUE");
```

<h3 id=player_set_movement_speed>
  <code>player::set_movement_speed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Movement Speed\
**Type:** Action without value\
**Description:** Sets the player's movement speed.

**Usage example:** 
```ts
player::set_movement_speed(1,"WALK");
```

<h3 id=player_set_nametag_visible>
  <code>player::set_nametag_visible</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Nickname Visible\
**Type:** Action without value\
**Description:** Display or hide the nickname above the head.

**Usage example:** 
```ts
player::set_nametag_visible("TRUE");
```

<h3 id=player_set_player_list_info>
  <code>player::set_player_list_info</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Tab List Text\
**Type:** Action without value\
**Description:** Sets the text above or below the player list for the player.

**Usage example:** 
```ts
player::set_player_list_info(["text", "text"],"HEADER","SPACES");
```

<h3 id=player_set_pose>
  <code>player::set_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Pose\
**Type:** Action without value\
**Description:** Sets a specific player pose.

**Usage example:** 
```ts
player::set_pose("CROAKING","TRUE");
```

<h3 id=player_set_pvp>
  <code>player::set_pvp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set PVP Enabled\
**Type:** Action without value\
**Description:** Sets the player's permission to attack and damage other players.

**Usage example:** 
```ts
player::set_pvp("TRUE");
```

<h3 id=player_set_rain_level>
  <code>player::set_rain_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::set_rain_level(1);
```

<h3 id=player_set_rotation>
  <code>player::set_rotation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Rotation\
**Type:** Action without value\
**Description:** Sets the player's rotation.

**Usage example:** 
```ts
player::set_rotation(1,2);
```

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
```

<h3 id=player_set_saturation>
  <code>player::set_saturation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Saturation\
**Type:** Action without value\
**Description:** Sets the player's secondary hunger level (saturation).

**Usage example:** 
```ts
player::set_saturation(1,"SET");
```

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
```

<h3 id=player_set_skin>
  <code>player::set_skin</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Skin\
**Type:** Action without value\
**Description:** Sets the specified player's skin for the target of the event.

**Usage example:** 
```ts
player::set_skin("name_or_uuid","MOJANG");
```

<h3 id=player_set_slot_item>
  <code>player::set_slot_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item In Slot\
**Type:** Action without value\
**Description:** Sets an item to a slot in the player's inventory.

**Usage example:** 
```ts
player::set_slot_item(item("stick"),1);
```

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
```

<h3 id=player_set_thunder_level>
  <code>player::set_thunder_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
player::set_thunder_level(1);
```

<h3 id=player_set_tick_rate>
  <code>player::set_tick_rate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
player::set_tick_rate(1);
```

<h3 id=player_set_time>
  <code>player::set_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Player Time\
**Type:** Action without value\
**Description:** Set a player's time without changing it for other players.

**Usage example:** 
```ts
player::set_time(1);
```

<h3 id=player_set_velocity>
  <code>player::set_velocity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Velocity\
**Type:** Action without value\
**Description:** Launches the player along the specified vector.

**Usage example:** 
```ts
player::set_velocity(vector(0,0,0),"TRUE");
```

<h3 id=player_set_visual_fire>
  <code>player::set_visual_fire</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Visual Fire\
**Type:** Action without value\
**Description:** Sets the player to a burning effect.

**Usage example:** 
```ts
player::set_visual_fire("TRUE");
```

<h3 id=player_set_weather>
  <code>player::set_weather</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Weather\
**Type:** Action without value\
**Description:** Set player weather without affecting other players.

**Usage example:** 
```ts
player::set_weather("DOWNFALL");
```

<h3 id=player_set_world_border>
  <code>player::set_world_border</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set World Border\
**Type:** Action without value\
**Description:** Set the world border for a player without changing it for other players.

**Usage example:** 
```ts
player::set_world_border(location(0,0,0,0,0),1,2);
```

<h3 id=player_shift_world_border>
  <code>player::shift_world_border</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift World Border\
**Type:** Action without value\
**Description:** Move the world border for the player without changing it for other players.

**Usage example:** 
```ts
player::shift_world_border(1,2,3);
```

<h3 id=player_show_debug_marker>
  <code>player::show_debug_marker</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Debug Marker\
**Type:** Action without value\
**Description:** Shows the player a debug marker at the location at the specified time. Red and blue colors work for players on version 1.19.4 and above.\
**Additional info:**\
&nbsp;&nbsp;Leave the "Display Name" argument blank to hide the name completely.

**Usage example:** 
```ts
player::show_debug_marker(location(0,0,0,0,0),"name",1,2,3,4,5);
```

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

<h3 id=player_show_inventory_menu>
  <code>player::show_inventory_menu</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Inventory Menu\
**Type:** Action without value\
**Description:** Shows the player an inventory menu with selected items and title.

**Usage example:** 
```ts
player::show_inventory_menu([item("stick"), item("stick")],"name","CHEST");
```

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
```

<h3 id=player_show_win_screen>
  <code>player::show_win_screen</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Show Credits Screen\
**Type:** Action without value\
**Description:** Shows the player the credits screen.

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
**Description:** Sets the player's spectate target in spectator mode.

**Usage example:** 
```ts
player::spectate_target("name_or_uuid");
```

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
```

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
```

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
```

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
player::teleport(location(0,0,0,0,0),"TRUE","TRUE","TRUE");
```

<h3 id=player_teleport_sequence>
  <code>player::teleport_sequence</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Teleport Sequence\
**Type:** Action without value\
**Description:** Teleports the player between locations with the specified delay.

**Usage example:** 
```ts
player::teleport_sequence(1,[location(0,0,0,0,0), location(0,0,0,0,0)]);
```
