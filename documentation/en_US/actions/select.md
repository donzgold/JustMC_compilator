<h3 id=select_add_all_entities>
  <code>select::add_all_entities</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add All Entities\
**Type:** Action without value\
**Description:** Adds all entities to the selection.

**Usage example:** 
```ts
select::add_all_entities();
```

<h3 id=select_add_all_mobs>
  <code>select::add_all_mobs</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add All Mobs\
**Type:** Action without value\
**Description:** Adds all mobs to the selection.

**Usage example:** 
```ts
select::add_all_mobs();
```

<h3 id=select_add_all_players>
  <code>select::add_all_players</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add All Players\
**Type:** Action without value\
**Description:** Adds all players to the selection.

**Usage example:** 
```ts
select::add_all_players();
```

<h3 id=select_add_entity_by_conditional>
  <code>select::add_entity_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Entity By Conditional\
**Type:** Action without value\
**Description:** Adds entities to the selection by a condition.

**Usage example:** 
```ts
select::add_entity_by_conditional(a1.exists());
```

<h3 id=select_add_entity_by_name>
  <code>select::add_entity_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Entity By Name/UUID\
**Type:** Action without value\
**Description:** Adds an entity by name/UUID to the selection.

**Usage example:** 
```ts
select::add_entity_by_name(["name_or_uuid", "name_or_uuid"]);

//Or dry by keywords

select::add_entity_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Arguments:**

| **Name**       | **Type**     | **Description** |
| -------------- | ------------ | --------------- |
| `name_or_uuid` | list\[Text\] | Name or UUID    |
<h3 id=select_add_event_target>
  <code>select::add_event_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Event Target\
**Type:** Action without value\
**Description:** Adds an event target to the selection

**Usage example:** 
```ts
select::add_event_target("DAMAGER");

//Or dry by keywords

select::add_event_target(selection_type="DAMAGER");
```

**Arguments:**

| **Name**         | **Type**                                                                                                                                                             | **Description** |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `selection_type` | Marker<br/>**DAMAGER** - Damager<br/>**DEFAULT** - Default<br/>**KILLER** - Killer<br/>**PROJECTILE** - Projectile<br/>**SHOOTER** - Shooter<br/>**VICTIM** - Victim | Selection Type  |
<h3 id=select_add_last_entity>
  <code>select::add_last_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Last Entity\
**Type:** Action without value\
**Description:** Adds the last entity to the selection.

**Usage example:** 
```ts
select::add_last_entity();
```

<h3 id=select_add_last_mob>
  <code>select::add_last_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Last Mob\
**Type:** Action without value\
**Description:** Adds the last mob to the selection.

**Usage example:** 
```ts
select::add_last_mob();
```

<h3 id=select_add_mob_by_name>
  <code>select::add_mob_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Mob By Name/UUID\
**Type:** Action without value\
**Description:** Adds a mob by name/UUID to the selection.

**Usage example:** 
```ts
select::add_mob_by_name(["name_or_uuid", "name_or_uuid"]);

//Or dry by keywords

select::add_mob_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Arguments:**

| **Name**       | **Type**     | **Description** |
| -------------- | ------------ | --------------- |
| `name_or_uuid` | list\[Text\] | Name or UUID    |
<h3 id=select_add_player_by_conditional>
  <code>select::add_player_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Player By Conditional\
**Type:** Action without value\
**Description:** Adds players to the selection by a condition.

**Usage example:** 
```ts
select::add_player_by_conditional(a1.exists());
```

<h3 id=select_add_player_by_name>
  <code>select::add_player_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Player By Name/UUID\
**Type:** Action without value\
**Description:** Adds a player by name/UUID to the selection.

**Usage example:** 
```ts
select::add_player_by_name(["name_or_uuid", "name_or_uuid"]);

//Or dry by keywords

select::add_player_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Arguments:**

| **Name**       | **Type**     | **Description** |
| -------------- | ------------ | --------------- |
| `name_or_uuid` | list\[Text\] | Name or UUID    |
<h3 id=select_add_random_entity>
  <code>select::add_random_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Random Entity\
**Type:** Action without value\
**Description:** Adds a random entity to the selection.

**Usage example:** 
```ts
select::add_random_entity();
```

<h3 id=select_add_random_mob>
  <code>select::add_random_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Random Mob\
**Type:** Action without value\
**Description:** Adds a random mob to the selection.

**Usage example:** 
```ts
select::add_random_mob();
```

<h3 id=select_add_random_player>
  <code>select::add_random_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Random Player\
**Type:** Action without value\
**Description:** Adds a random player to the selection.

**Usage example:** 
```ts
select::add_random_player();
```

<h3 id=select_all_entities>
  <code>select::all_entities</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select All Entities\
**Type:** Action without value\
**Description:** Selects all entities in the world.

**Usage example:** 
```ts
select::all_entities();
```

<h3 id=select_all_mobs>
  <code>select::all_mobs</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select All Mobs\
**Type:** Action without value\
**Description:** Selects all mobs in the world.

**Usage example:** 
```ts
select::all_mobs();
```

<h3 id=select_all_players>
  <code>select::all_players</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select All Players\
**Type:** Action without value\
**Description:** Selects all players in the world.

**Usage example:** 
```ts
select::all_players();
```

<h3 id=select_dummy>
  <code>select::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action without value\
**Description:** ...

**Usage example:** 
```ts
select::dummy();
```

<h3 id=select_entity_by_conditional>
  <code>select::entity_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Entity By Condition\
**Type:** Action without value\
**Description:** Selects entities if the specified condition is met.

**Usage example:** 
```ts
select::entity_by_conditional(a1.exists());
```

<h3 id=select_entity_by_name>
  <code>select::entity_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Entity By Name\
**Type:** Action without value\
**Description:** Selects an entity or entities by name or UUID.

**Usage example:** 
```ts
select::entity_by_name(["name_or_uuid", "name_or_uuid"]);

//Or dry by keywords

select::entity_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Arguments:**

| **Name**       | **Type**     | **Description**            |
| -------------- | ------------ | -------------------------- |
| `name_or_uuid` | list\[Text\] | Name or UUID of the target |
<h3 id=select_event_target>
  <code>select::event_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Event Target\
**Type:** Action without value\
**Description:** Selects the target that triggered the event.

**Usage example:** 
```ts
select::event_target("DAMAGER");

//Or dry by keywords

select::event_target(selection_type="DAMAGER");
```

**Arguments:**

| **Name**         | **Type**                                                                                                                                                                      | **Description**    |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `selection_type` | Marker<br/>**DAMAGER** - Attacker<br/>**DEFAULT** - Default<br/>**KILLER** - Killer<br/>**PROJECTILE** - Projectile Shooter<br/>**SHOOTER** - Shooter<br/>**VICTIM** - Victim | Select Target Type |
<h3 id=select_filter_by_conditional>
  <code>select::filter_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Filter Selection By Condition\
**Type:** Action without value\
**Description:** Keep the selection of targets that match the selected condition.

**Usage example:** 
```ts
select::filter_by_conditional(a1.exists());
```

<h3 id=select_filter_by_distance>
  <code>select::filter_by_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Filter Selection By Distance\
**Type:** Action without value\
**Description:** Keep in the selection those targets that are at a distance from the location.

**Usage example:** 
```ts
select::filter_by_distance(location(0,0,0,0,0), 1, "FALSE", "FARTHEST");

//Or dry by keywords

select::filter_by_distance(location=location(0,0,0,0,0), selection_size=1, ignore_y_axis="FALSE", compare_mode="FARTHEST");
```

**Arguments:**

| **Name**         | **Type**                                                             | **Description**   |
| ---------------- | -------------------------------------------------------------------- | ----------------- |
| `location`       | Location                                                             | Center Location   |
| `selection_size` | Number                                                               | Number of Targets |
| `ignore_y_axis`  | Marker<br/>**FALSE** - Don\'t Ignore<br/>**TRUE** - Ignore           | Ignore Y Axis     |
| `compare_mode`   | Marker<br/>**FARTHEST** - Farthest<br/>**NEAREST** - Nearest Targets | Compare Type      |
<h3 id=select_filter_by_raycast>
  <code>select::filter_by_raycast</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Filter By Raycast\
**Type:** Action without value\
**Description:** Keep only the targets hit by the launched beam in the selection. Beamwidth only works on entities (increases or decreases creature hitboxes).

**Usage example:** 
```ts
select::filter_by_raycast(`variable`, location(0,0,0,0,0), 1, 2, 3, "FALSE", "FALSE", "ALWAYS");

//Or dry by keywords

select::filter_by_raycast(variable=`variable`, origin=location(0,0,0,0,0), max_distance=1, ray_size=2, selection_size=3, consider_blocks="FALSE", ignore_passable_blocks="FALSE", fluid_collision_mode="ALWAYS");
```

**Arguments:**

| **Name**                 | **Type**                                                                                                              | **Description**        |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `variable`               | Variable                                                                                                              | Ray End Point          |
| `origin`                 | Location                                                                                                              | Ray Origin             |
| `max_distance`           | Number                                                                                                                | Ray Length             |
| `ray_size`               | Number                                                                                                                | Ray Width              |
| `selection_size`         | Number                                                                                                                | Selection Size         |
| `consider_blocks`        | Marker<br/>**FALSE** - Don\'t Consider<br/>**TRUE** - Consider                                                        | Consider Blocks        |
| `ignore_passable_blocks` | Marker<br/>**FALSE** - Don\'t Ignore<br/>**TRUE** - Ignore                                                            | Ignore Passable Blocks |
| `fluid_collision_mode`   | Marker<br/>**ALWAYS** - Don\'t Ignore<br/>**NEVER** - Totally Ignore<br/>**SOURCE_ONLY** - Consider fluid source only | Ignore Fluid           |
<h3 id=select_filter_randomly>
  <code>select::filter_randomly</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Filter Selection Randomly\
**Type:** Action without value\
**Description:** Selects a random number of targets in the selection.

**Usage example:** 
```ts
select::filter_randomly(1);

//Or dry by keywords

select::filter_randomly(size=1);
```

**Arguments:**

| **Name** | **Type** | **Description**   |
| -------- | -------- | ----------------- |
| `size`   | Number   | Number of Targets |
<h3 id=select_invert>
  <code>select::invert</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Invert Selection\
**Type:** Action without value\
**Description:** Creates a new selection that includes all creatures except the selected ones.

**Usage example:** 
```ts
select::invert();
```

<h3 id=select_last_entity>
  <code>select::last_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Last Spawned Entity\
**Type:** Action without value\
**Description:** Selects the last spawned entity in the world.

**Usage example:** 
```ts
select::last_entity();
```

<h3 id=select_last_mob>
  <code>select::last_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Last Spawned Mob\
**Type:** Action without value\
**Description:** Selects the last mob that spawned in the world.

**Usage example:** 
```ts
select::last_mob();
```

<h3 id=select_mob_by_name>
  <code>select::mob_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Mob By Name\
**Type:** Action without value\
**Description:** Selects a mob or mobs by name or UUID.

**Usage example:** 
```ts
select::mob_by_name(["name_or_uuid", "name_or_uuid"]);

//Or dry by keywords

select::mob_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Arguments:**

| **Name**       | **Type**     | **Description**            |
| -------------- | ------------ | -------------------------- |
| `name_or_uuid` | list\[Text\] | Name or UUID of the target |
<h3 id=select_player_by_conditional>
  <code>select::player_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Player By Condition\
**Type:** Action without value\
**Description:** Selects players if the specified condition is met.

**Usage example:** 
```ts
select::player_by_conditional(a1.exists());
```

<h3 id=select_player_by_name>
  <code>select::player_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Player By Name\
**Type:** Action without value\
**Description:** Selects a player or players by name or UUID.

**Usage example:** 
```ts
select::player_by_name(["name_or_uuid", "name_or_uuid"]);

//Or dry by keywords

select::player_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Arguments:**

| **Name**       | **Type**     | **Description**            |
| -------------- | ------------ | -------------------------- |
| `name_or_uuid` | list\[Text\] | Name or UUID of the target |
<h3 id=select_random_entity>
  <code>select::random_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Random Entity\
**Type:** Action without value\
**Description:** Selects a random entity in the world.

**Usage example:** 
```ts
select::random_entity();
```

<h3 id=select_random_mob>
  <code>select::random_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Random Mob\
**Type:** Action without value\
**Description:** Selects a random mob in the world.

**Usage example:** 
```ts
select::random_mob();
```

<h3 id=select_random_player>
  <code>select::random_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Select Random Player\
**Type:** Action without value\
**Description:** Selects a random player in the world.

**Usage example:** 
```ts
select::random_player();
```

<h3 id=select_reset>
  <code>select::reset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reset Selection\
**Type:** Action without value\
**Description:** Resets the entire selection.

**Usage example:** 
```ts
select::reset();
```

