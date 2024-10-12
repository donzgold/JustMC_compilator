<h3 id=repeat_adjacently>
  <code>repeat::adjacently</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat Adjacently\
**Type:** Action without value\
**Description:** Assigns the current location to the specified variable among blocks adjacent to the specified location.

**Usage example:** 
```ts
repeat::adjacently(location(0,0,0,0,0),"TRUE","TRUE","CARDINAL"){a1->
    player::message("Code in cycle")
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                   | **Description**                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `variable`        | Variable                                                                                                   | To assign location                                                                     |
| `origin`          | Location                                                                                                   | Central block                                                                          |
| `change_rotation` | Marker<br/>**TRUE** - Rotate<br/>**FALSE** - Don't Rotate                                                  | Rotate the direction of view of the current element relative to the specified location |
| `include_self`    | Marker<br/>**TRUE** - Include<br/>**FALSE** - Do not include                                               | Include Center Block                                                                   |
| `pattern`         | Marker<br/>**CARDINAL** - Cardinal<br/>**SQUARE** - Square<br/>**ADJACENT** - Adjacent<br/>**CUBE** - Cube | Adjacent Block Selection Type                                                          |
<h3 id=repeat_for_each_in_list>
  <code>repeat::for_each_in_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat For List Values\
**Type:** Action without value\
**Description:** Retrieves each item in the specified list and outputs its index and value to the specified variables.

**Usage example:** 
```ts
repeat::for_each_in_list(`list`){a1, a2->
    player::message("Code in cycle")
}
```

**Arguments:**

| **Name**         | **Type** | **Description**                 |
| ---------------- | -------- | ------------------------------- |
| `index_variable` | Variable | To assign an item index         |
| `value_variable` | Variable | To assign a value to an element |
| `list`           | List     | List to traverse                |
<h3 id=repeat_for_each_map_entry>
  <code>repeat::for_each_map_entry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat For Dictionary Values\
**Type:** Action without value\
**Description:** Retrieves each element from the specified dictionary and outputs its index and value to the specified variables.

**Usage example:** 
```ts
repeat::for_each_map_entry(`map`){a1, a2->
    player::message("Code in cycle")
}
```

**Arguments:**

| **Name**         | **Type**   | **Description**                   |
| ---------------- | ---------- | --------------------------------- |
| `key_variable`   | Variable   | Variable to assign an element key |
| `value_variable` | Variable   | Variable to assign element value  |
| `map`            | Dictionary | Dictionary to traverse            |
<h3 id=repeat_forever>
  <code>repeat::forever</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat Forever\
**Type:** Action without value\
**Description:** Persistently repeats the code inside the pistons.

**Usage example:** 
```ts
repeat::forever(){
    player::message("Everything work");
}
```

<h3 id=repeat_multi_times>
  <code>repeat::multi_times</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat N Times\
**Type:** Action without value\
**Description:** Runs the code the specified number of times.

**Usage example:** 
```ts
repeat::multi_times(1){a1->
    player::message("Code in cycle")
}
```

**Arguments:**

| **Name**   | **Type** | **Description**           |
| ---------- | -------- | ------------------------- |
| `variable` | Variable | Current Counter Value     |
| `amount`   | Number   | Number of code executions |
<h3 id=repeat_on_circle>
  <code>repeat::on_circle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Circle\
**Type:** Action without value\
**Description:** Repeat the location of each circle block with the given parameters in sequence.

**Usage example:** 
```ts
repeat::on_circle(location(0,0,0,0,0),1,2,vector(0,0,0),3,"DEGREES"){a1->
    player::message("Code in cycle")
}
```

**Arguments:**

| **Name**                 | **Type**                                                   | **Description**                                        |
| ------------------------ | ---------------------------------------------------------- | ------------------------------------------------------ |
| `variable`               | Variable                                                   | To assign location                                     |
| `center`                 | Location                                                   | Circle Center                                          |
| `radius`                 | Number                                                     | Circle Radius                                          |
| `circle_points`          | Number                                                     | Number of Circle Points                                |
| `perpendicular_to_plane` | Vector                                                     | Plane normal to which the circle will be perpendicular |
| `start_angle`            | Number                                                     | Start Angle                                            |
| `angle_unit`             | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians | Angle Type                                             |
<h3 id=repeat_on_grid>
  <code>repeat::on_grid</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Grid\
**Type:** Action without value\
**Description:** Repeat the location of each block in the given region into the given variable.

**Usage example:** 
```ts
repeat::on_grid(location(0,0,0,0,0),location(0,0,0,0,0)){a1->
    player::message("Code in cycle")
}
```

**Arguments:**

| **Name**   | **Type** | **Description**                   |
| ---------- | -------- | --------------------------------- |
| `variable` | Variable | To assign current region location |
| `start`    | Location | Start Location                    |
| `end`      | Location | End Location                      |
<h3 id=repeat_on_path>
  <code>repeat::on_path</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Path\
**Type:** Action without value\
**Description:** Repeat from one location to another in increments, assigning the current location to the specified variable.

**Usage example:** 
```ts
repeat::on_path(1,[location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE"){a1->
    player::message("Code in cycle")
}
```

**Arguments:**

| **Name**    | **Type**                                              | **Description**                     |
| ----------- | ----------------------------------------------------- | ----------------------------------- |
| `variable`  | Variable                                              | To assign location                  |
| `step`      | Number                                                | Distance between points             |
| `locations` | list[Location]                                        | Line End Locations                  |
| `rotation`  | Marker<br/>**TRUE** - Keep<br/>**FALSE** - Don't Save | Keep rotation of specified location |
<h3 id=repeat_on_range>
  <code>repeat::on_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Range\
**Type:** Action without value\
**Description:** Assigns the current number to the specified variable from the specified range in increments.

**Usage example:** 
```ts
repeat::on_range(1,2,3){a1->
    player::message("Code in cycle")
}
```

**Arguments:**

| **Name**   | **Type** | **Description**         |
| ---------- | -------- | ----------------------- |
| `variable` | Variable | Current number in range |
| `start`    | Number   | Lower Range             |
| `end`      | Number   | Upper Range Limit       |
| `interval` | Number   | Step                    |
<h3 id=repeat_on_sphere>
  <code>repeat::on_sphere</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Sphere\
**Type:** Action without value\
**Description:** Sequentially returns the location of each point on a sphere with the specified parameters.

**Usage example:** 
```ts
repeat::on_sphere(location(0,0,0,0,0),1,2,"NO_CHANGES"){a1->
    player::message("Code in cycle")
}
```

**Arguments:**

| **Name**          | **Type**                                                                                             | **Description**                     |
| ----------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `variable`        | Variable                                                                                             | Current location of point on sphere |
| `center`          | Location                                                                                             | Sphere Center                       |
| `radius`          | Number                                                                                               | Sphere Radius                       |
| `points`          | Number                                                                                               | Number of Points                    |
| `rotate_location` | Marker<br/>**NO_CHANGES** - Same as Location<br/>**INWARDS** - Center<br/>**OUTWARDS** - From Center | Point Location Direction            |
<h3 id=repeat_while>
  <code>repeat::while</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat By Condition\
**Type:** Action without value\
**Description:** Runs code as long as the selected condition is true.

**Usage example:** 
```ts
repeat::while(a1.exists()){
    player::message("Everything work");
}
```

