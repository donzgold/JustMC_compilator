<h3 id=if_variable_block_is_minecraft_tagged>
  <code>variable::block_is_minecraft_tagged</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
if(variable::block_is_minecraft_tagged(item("stick"), "namespace")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::block_is_minecraft_tagged(item=item("stick"), namespace="namespace"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**    | **Type** | **Description** |
| ----------- | -------- | --------------- |
| `item`      | Item     | None            |
| `namespace` | Text     | None            |
<h3 id=if_variable_block_is_solid>
  <code>variable::block_is_solid</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Block Is Solid\
**Type:** Action that checks the conditions\
**Description:** Checks if the specified block is solid.

**Usage example:** 
```ts
if(variable::block_is_solid(item("stone"))){
    player::message("Condition is true");
}

//Or from the object

if(item("stone").block_is_solid()){
    player::message("Condition is true");
}

//Or dry by keywords

variable::block_is_solid(block=item("stone")){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `block`  | Block    | Block to check  |
<h3 id=if_variable_dummy>
  <code>variable::is_dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action that checks the conditions\
**Description:** ...

**Usage example:** 
```ts
if(variable::is_dummy()){
    player::message("Condition is true");
}
```

<h3 id=if_variable_equals>
  <code>variable::equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a variable is equal to at least one of the compared values.

**Usage example:** 
```ts
if(variable::equals("any value", ["any value", "any value"])){
    player::message("Condition is true");
}

//Or from the object

if("any value".equals(["any value", "any value"])){
    player::message("Condition is true");
}

//Or dry by keywords

variable::equals(value="any value", compare=["any value", "any value"]){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type**          | **Description**     |
| --------- | ----------------- | ------------------- |
| `value`   | Any Value         | Comparison Variable |
| `compare` | list\[Any Value\] | Compare Values      |
<h3 id=if_variable_exists>
  <code>variable::exists</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Variable Exists\
**Type:** Action that checks the conditions\
**Description:** Checks if the selected variable exists.

**Usage example:** 
```ts
if(variable::exists(`variable`)){
    player::message("Condition is true");
}

//Or from the object

if(`variable`.exists()){
    player::message("Condition is true");
}

//Or dry by keywords

variable::exists(variable=`variable`){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**   | **Type** | **Description**  |
| ---------- | -------- | ---------------- |
| `variable` | Variable | Variable to test |
<h3 id=if_variable_greater>
  <code>variable::greater</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Greater\
**Type:** Action that checks the conditions\
**Description:** Checks if a numeric variable is greater than the specified value.

**Usage example:** 
```ts
if(variable::greater(1, 2)){
    player::message("Condition is true");
}

//Or from the object

if((1).greater(2)){
    player::message("Condition is true");
}

//Or dry by keywords

variable::greater(value=1, compare=2){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type** | **Description**     |
| --------- | -------- | ------------------- |
| `value`   | Number   | Comparison Variable |
| `compare` | Number   | Compare Value       |
<h3 id=if_variable_greater_or_equals>
  <code>variable::greater_or_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Greater or Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a numeric variable is greater than or equal to the specified value.

**Usage example:** 
```ts
if(variable::greater_or_equals(1, 2)){
    player::message("Condition is true");
}

//Or from the object

if((1).greater_or_equals(2)){
    player::message("Condition is true");
}

//Or dry by keywords

variable::greater_or_equals(value=1, compare=2){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type** | **Description**     |
| --------- | -------- | ------------------- |
| `value`   | Number   | Comparable Variable |
| `compare` | Number   | Value to Compare    |
<h3 id=if_variable_in_range>
  <code>variable::in_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** In Range\
**Type:** Action that checks the conditions\
**Description:** Checks if a variable is in the specified range.
**Work_with:**\
&nbsp;&nbsp;Numbers\
&nbsp;&nbsp;Locations

**Usage example:** 
```ts
if(variable::in_range("any value", "any value", "any value")){
    player::message("Condition is true");
}

//Or from the object

if("any value".in_range("any value", "any value")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::in_range(value="any value", min="any value", max="any value"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**  | **Description**     |
| -------- | --------- | ------------------- |
| `value`  | Any Value | Comparison Variable |
| `min`    | Any Value | Minimum Value       |
| `max`    | Any Value | Max Value           |
<h3 id=if_variable_is_type>
  <code>variable::is_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Variable Type Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a variable\'s value type is equal to the specified one.

**Usage example:** 
```ts
if(variable::is_type("any value", "ARRAY")){
    player::message("Condition is true");
}

//Or from the object

if("any value".is_type("ARRAY")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::is_type(value="any value", variable_type="ARRAY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**        | **Type**                                                                                                                                                                                                                                           | **Description**   |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `value`         | Any Value                                                                                                                                                                                                                                          | Variable to check |
| `variable_type` | Marker<br/>**ARRAY** - List<br/>**ITEM** - Item<br/>**LOCATION** - Location<br/>**MAP** - Dictionary<br/>**NUMBER** - Number<br/>**PARTICLE** - Particle<br/>**POTION** - Potion<br/>**SOUND** - Sound<br/>**TEXT** - Text<br/>**VECTOR** - Vector | Variable Type     |
<h3 id=if_variable_item_equals>
  <code>variable::item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if an item variable is equal to at least one of the specified ones.

**Usage example:** 
```ts
if(variable::item_equals(item("stick"), [item("stick"), item("stick")], "EXACTLY")){
    player::message("Condition is true");
}

//Or from the object

if(item("stick").item_equals([item("stick"), item("stick")], "EXACTLY")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::item_equals(value=item("stick"), compare=[item("stick"), item("stick")], comparison_mode="EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                          | **Description**          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `value`           | Item                                                                                                                                                                                              | Item Variable to Compare |
| `compare`         | list\[Item\]                                                                                                                                                                                      | Compare Values           |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability<br/>**IGNORE_STACK_SIZE** - Ignore quantity<br/>**TYPE_ONLY** - Item type only | Comparison Mode          |
<h3 id=if_variable_item_has_enchantment>
  <code>variable::item_has_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Has Enchantment\
**Type:** Action that checks the conditions\
**Description:** Checks if an item have a specific enchantment of a specific level.

**Usage example:** 
```ts
if(variable::item_has_enchantment(item("stick"), "enchant", 1)){
    player::message("Condition is true");
}

//Or from the object

if(item("stick").item_has_enchantment("enchant", 1)){
    player::message("Condition is true");
}

//Or dry by keywords

variable::item_has_enchantment(item=item("stick"), enchant="enchant", level=1){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type** | **Description** |
| --------- | -------- | --------------- |
| `item`    | Item     | item            |
| `enchant` | Text     | Enchantment     |
| `level`   | Number   | Level           |
<h3 id=if_variable_item_has_tag>
  <code>variable::item_has_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Has Custom Tag\
**Type:** Action that checks the conditions\
**Description:** Checks if an item variable has the specified tag with the selected value.

**Usage example:** 
```ts
if(variable::item_has_tag(item("stick"), "tag", "value", "CONTAINS")){
    player::message("Condition is true");
}

//Or from the object

if(item("stick").item_has_tag("tag", "value", "CONTAINS")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::item_has_tag(item=item("stick"), tag="tag", value="value", compare_type="CONTAINS"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**       | **Type**                                                                                                                   | **Description** |
| -------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `item`         | Item                                                                                                                       | Item Variable   |
| `tag`          | Text                                                                                                                       | Tag name        |
| `value`        | Text                                                                                                                       | Tag Value       |
| `compare_type` | Marker<br/>**CONTAINS** - Contains<br/>**ENDS_WITH** - Ends With<br/>**EQUALS** - Equals<br/>**STARTS_WITH** - Starts With | Comparison Type |
<h3 id=if_variable_item_is_block>
  <code>variable::item_is_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Is Block\
**Type:** Action that checks the conditions\
**Description:** Checks if the provided item is a block.

**Usage example:** 
```ts
if(variable::item_is_block(item("stick"))){
    player::message("Condition is true");
}

//Or from the object

if(item("stick").item_is_block()){
    player::message("Condition is true");
}

//Or dry by keywords

variable::item_is_block(item=item("stick")){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type** | **Description** |
| -------- | -------- | --------------- |
| `item`   | Item     | Item to check   |
<h3 id=if_variable_item_is_minecraft_tagged>
  <code>variable::item_is_minecraft_tagged</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
if(variable::item_is_minecraft_tagged(item("stick"), "namespace")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::item_is_minecraft_tagged(item=item("stick"), namespace="namespace"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**    | **Type** | **Description** |
| ----------- | -------- | --------------- |
| `item`      | Item     | None            |
| `namespace` | Text     | None            |
<h3 id=if_variable_less>
  <code>variable::less</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Less\
**Type:** Action that checks the conditions\
**Description:** Checks if a numeric variable is less than the specified value.

**Usage example:** 
```ts
if(variable::less(1, 2)){
    player::message("Condition is true");
}

//Or from the object

if((1).less(2)){
    player::message("Condition is true");
}

//Or dry by keywords

variable::less(value=1, compare=2){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type** | **Description**     |
| --------- | -------- | ------------------- |
| `value`   | Number   | Comparison Variable |
| `compare` | Number   | Compare Value       |
<h3 id=if_variable_less_or_equals>
  <code>variable::less_or_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Less or Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a numeric variable is less than or equal to the specified value.

**Usage example:** 
```ts
if(variable::less_or_equals(1, 2)){
    player::message("Condition is true");
}

//Or from the object

if((1).less_or_equals(2)){
    player::message("Condition is true");
}

//Or dry by keywords

variable::less_or_equals(value=1, compare=2){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type** | **Description**     |
| --------- | -------- | ------------------- |
| `value`   | Number   | Comparable Variable |
| `compare` | Number   | Value to Compare    |
<h3 id=if_variable_list_contains_value>
  <code>variable::list_contains_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** List Contains Value\
**Type:** Action that checks the conditions\
**Description:** Checks if a list contains a specific value.

**Usage example:** 
```ts
if(variable::list_contains_value(`list`, ["any value", "any value"], "ALL")){
    player::message("Condition is true");
}

//Or from the object

if(`list`.list_contains_value(["any value", "any value"], "ALL")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::list_contains_value(list=`list`, values=["any value", "any value"], check_mode="ALL"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                | **Description** |
| ------------ | ------------------------------------------------------- | --------------- |
| `list`       | List                                                    | List to check   |
| `values`     | list\[Any Value\]                                       | Values to Check |
| `check_mode` | Marker<br/>**ALL** - All Values<br/>**ANY** - Any Value | Check Mode      |
<h3 id=if_variable_list_is_empty>
  <code>variable::list_is_empty</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Value Size Is Zero\
**Type:** Action that checks the conditions\
**Description:** Checks if the size of a value is zero.
**Work_with:**\
&nbsp;&nbsp;Text\
&nbsp;&nbsp;Lists\
&nbsp;&nbsp;Dictionaries\
&nbsp;&nbsp;None\
&nbsp;&nbsp;None\
&nbsp;&nbsp;None

**Usage example:** 
```ts
if(variable::list_is_empty("any value")){
    player::message("Condition is true");
}

//Or from the object

if("any value".list_is_empty()){
    player::message("Condition is true");
}

//Or dry by keywords

variable::list_is_empty(list="any value"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**  | **Description** |
| -------- | --------- | --------------- |
| `list`   | Any Value | Value to check  |
<h3 id=if_variable_list_value_equals>
  <code>variable::list_value_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** List Value Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the value of a list item is equal to at least one value being compared.

**Usage example:** 
```ts
if(variable::list_value_equals(`list`, 1, ["any value", "any value"])){
    player::message("Condition is true");
}

//Or from the object

if(`list`.list_value_equals(1, ["any value", "any value"])){
    player::message("Condition is true");
}

//Or dry by keywords

variable::list_value_equals(list=`list`, index=1, values=["any value", "any value"]){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**          | **Description**   |
| -------- | ----------------- | ----------------- |
| `list`   | List              | List to check     |
| `index`  | Number            | Value index       |
| `values` | list\[Any Value\] | Comparable Values |
<h3 id=if_variable_location_in_range>
  <code>variable::location_in_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Location In Range\
**Type:** Action that checks the conditions\
**Description:** Checks if the location is in the specified range.

**Usage example:** 
```ts
if(variable::location_in_range(location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "BLOCK")){
    player::message("Condition is true");
}

//Or from the object

if(location(0,0,0,0,0).location_in_range(location(0,0,0,0,0), location(0,0,0,0,0), "BLOCK")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::location_in_range(value=location(0,0,0,0,0), min=location(0,0,0,0,0), max=location(0,0,0,0,0), border_handling="BLOCK"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                          | **Description**        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `value`           | Location                                                                                                                                          | Location to check      |
| `min`             | Location                                                                                                                                          | First corner of region |
| `max`             | Location                                                                                                                                          | Second Region Angle    |
| `border_handling` | Marker<br/>**BLOCK** - Round to Block Coordinates<br/>**EXACT** - Exact Coordinates<br/>**FULL_BLOCK_RANGE** - Round to min. and max. block angle | Check Mode             |
<h3 id=if_variable_location_is_near>
  <code>variable::location_is_near</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Near Location\
**Type:** Action that checks the conditions\
**Description:** Checks if a location variable is near the specified location.

**Usage example:** 
```ts
if(variable::location_is_near(location(0,0,0,0,0), 1, [location(0,0,0,0,0), location(0,0,0,0,0)], "CIRCLE")){
    player::message("Condition is true");
}

//Or from the object

if(location(0,0,0,0,0).location_is_near(1, [location(0,0,0,0,0), location(0,0,0,0,0)], "CIRCLE")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::location_is_near(location=location(0,0,0,0,0), radius=1, check=[location(0,0,0,0,0), location(0,0,0,0,0)], shape="CIRCLE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**   | **Type**                                                                                           | **Description**       |
| ---------- | -------------------------------------------------------------------------------------------------- | --------------------- |
| `location` | Location                                                                                           | Location to check     |
| `radius`   | Number                                                                                             | Check Radius          |
| `check`    | list\[Location\]                                                                                   | Shape Center Location |
| `shape`    | Marker<br/>**CIRCLE** - Circle<br/>**CUBE** - Cube<br/>**SPHERE** - Sphere<br/>**SQUARE** - Square | Shape                 |
<h3 id=if_variable_map_has_key>
  <code>variable::map_has_key</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dictionary Has Key\
**Type:** Action that checks the conditions\
**Description:** Checks if a dictionary has a specific key.

**Usage example:** 
```ts
if(variable::map_has_key(`map`, ["any value", "any value"], "ALL")){
    player::message("Condition is true");
}

//Or from the object

if(`map`.map_has_key(["any value", "any value"], "ALL")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::map_has_key(map=`map`, key=["any value", "any value"], check_mode="ALL"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                     | **Description**     |
| ------------ | -------------------------------------------- | ------------------- |
| `map`        | Dictionary                                   | Dictionary to check |
| `key`        | list\[Any Value\]                            | Key                 |
| `check_mode` | Marker<br/>**ALL** - None<br/>**ANY** - None | None                |
<h3 id=if_variable_map_value_equals>
  <code>variable::map_value_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dictionary Value Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the value of a dictionary element by key is equal to at least one value being compared.

**Usage example:** 
```ts
if(variable::map_value_equals(`map`, "any value", ["any value", "any value"])){
    player::message("Condition is true");
}

//Or from the object

if(`map`.map_value_equals("any value", ["any value", "any value"])){
    player::message("Condition is true");
}

//Or dry by keywords

variable::map_value_equals(map=`map`, key="any value", values=["any value", "any value"]){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**          | **Description**     |
| -------- | ----------------- | ------------------- |
| `map`    | Dictionary        | Dictionary to check |
| `key`    | Any Value         | Key                 |
| `values` | list\[Any Value\] | Comparable Values   |
<h3 id=if_variable_not_equals>
  <code>variable::not_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Not Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a variable is not equal to all of the values being compared.

**Usage example:** 
```ts
if(variable::not_equals("any value", ["any value", "any value"])){
    player::message("Condition is true");
}

//Or from the object

if("any value".not_equals(["any value", "any value"])){
    player::message("Condition is true");
}

//Or dry by keywords

variable::not_equals(value="any value", compare=["any value", "any value"]){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type**          | **Description**     |
| --------- | ----------------- | ------------------- |
| `value`   | Any Value         | Comparable Variable |
| `compare` | list\[Any Value\] | Compare Values      |
<h3 id=if_variable_number_in_range>
  <code>variable::number_in_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

**Usage example:** 
```ts
if(variable::number_in_range(1, 2, 3, "NOT_INCLUDE")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::number_in_range(value=1, min=2, max=3, including="NOT_INCLUDE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**    | **Type**                                                                                                              | **Description** |
| ----------- | --------------------------------------------------------------------------------------------------------------------- | --------------- |
| `value`     | Number                                                                                                                | None            |
| `min`       | Number                                                                                                                | None            |
| `max`       | Number                                                                                                                | None            |
| `including` | Marker<br/>**NOT_INCLUDE** - None<br/>**INCLUDE_FIRST** - None<br/>**INCLUDE_LAST** - None<br/>**INCLUDE_ALL** - None | None            |
<h3 id=if_variable_range_intersects_range>
  <code>variable::range_intersects_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Range Intersects Range\
**Type:** Action that checks the conditions\
**Description:** Checks whether one region intersects with another.

**Usage example:** 
```ts
if(variable::range_intersects_range(location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "CONTAINS")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::range_intersects_range(min1=location(0,0,0,0,0), max1=location(0,0,0,0,0), min2=location(0,0,0,0,0), max2=location(0,0,0,0,0), check_type="CONTAINS"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                         | **Description**                    |
| ------------ | ---------------------------------------------------------------- | ---------------------------------- |
| `min1`       | Location                                                         | First corner of the first region   |
| `max1`       | Location                                                         | Second corner of the first region  |
| `min2`       | Location                                                         | First corner of the second region  |
| `max2`       | Location                                                         | Second corner of the second region |
| `check_type` | Marker<br/>**CONTAINS** - Contains<br/>**OVERLAPS** - Intersects | Check type                         |
<h3 id=if_variable_text_contains>
  <code>variable::text_contains</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Text Contains\
**Type:** Action that checks the conditions\
**Description:** Checks if a text variable contains the specified text.

**Usage example:** 
```ts
if(variable::text_contains("value", ["compare", "compare"], "FALSE")){
    player::message("Condition is true");
}

//Or from the object

if("value".text_contains(["compare", "compare"], "FALSE")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::text_contains(value="value", compare=["compare", "compare"], ignore_case="FALSE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**      | **Type**                                       | **Description**   |
| ------------- | ---------------------------------------------- | ----------------- |
| `value`       | Text                                           | Variable to check |
| `compare`     | list\[Text\]                                   | Text to check     |
| `ignore_case` | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes | Ignore case       |
<h3 id=if_variable_text_ends_with>
  <code>variable::text_ends_with</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Text Ends With\
**Type:** Action that checks the conditions\
**Description:** Checks if a text variable ends with the specified text.

**Usage example:** 
```ts
if(variable::text_ends_with("value", ["compare", "compare"], "FALSE")){
    player::message("Condition is true");
}

//Or from the object

if("value".text_ends_with(["compare", "compare"], "FALSE")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::text_ends_with(value="value", compare=["compare", "compare"], ignore_case="FALSE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**      | **Type**                                     | **Description**       |
| ------------- | -------------------------------------------- | --------------------- |
| `value`       | Text                                         | Text variable to test |
| `compare`     | list\[Text\]                                 | Compare Text          |
| `ignore_case` | Marker<br/>**FALSE** - No<br/>**TRUE** - Yes | Ignore case           |
<h3 id=if_variable_text_matches>
  <code>variable::text_matches</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Text Matches\
**Type:** Action that checks the conditions\
**Description:** Checks if a text variable matches the specified text or regular expression (RegEx).

**Usage example:** 
```ts
if(variable::text_matches("match", ["values", "values"], "FALSE", "FALSE")){
    player::message("Condition is true");
}

//Or from the object

if("match".text_matches(["values", "values"], "FALSE", "FALSE")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::text_matches(match="match", values=["values", "values"], regular_expressions="FALSE", ignore_case="FALSE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**              | **Type**                                                      | **Description**            |
| --------------------- | ------------------------------------------------------------- | -------------------------- |
| `match`               | Text                                                          | Text or Regular Expression |
| `values`              | list\[Text\]                                                  | Text Variables to Validate |
| `regular_expressions` | Marker<br/>**FALSE** - Text<br/>**TRUE** - Regular Expression | Validation Method          |
| `ignore_case`         | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes                | Ignore case                |
<h3 id=if_variable_text_starts_with>
  <code>variable::text_starts_with</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Text Starts With\
**Type:** Action that checks the conditions\
**Description:** Checks if a text variable starts with the specified text.

**Usage example:** 
```ts
if(variable::text_starts_with("value", ["compare", "compare"], "FALSE")){
    player::message("Condition is true");
}

//Or from the object

if("value".text_starts_with(["compare", "compare"], "FALSE")){
    player::message("Condition is true");
}

//Or dry by keywords

variable::text_starts_with(value="value", compare=["compare", "compare"], ignore_case="FALSE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**      | **Type**                                     | **Description**       |
| ------------- | -------------------------------------------- | --------------------- |
| `value`       | Text                                         | Text variable to test |
| `compare`     | list\[Text\]                                 | Compare Text          |
| `ignore_case` | Marker<br/>**FALSE** - No<br/>**TRUE** - Yes | Ignore Case           |
<h3 id=set_variable_absolute>
  <code>variable::absolute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Absolute Value\
**Type:** An action that returns a value\
**Description:** Sets the modulus of the selected number to a variable.

**Usage example:** 
```ts
`variable` = variable::absolute(1);

//Or from the object

`variable` = (1).absolute();

//Or dry by positionals

variable::absolute(`variable`, 1);

//Or dry by keywords

variable::absolute(variable=`variable`, number=1);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `number`   | Number             | Module Number      |
<h3 id=set_variable_add>
  <code>variable::add</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Addition (+)\
**Type:** An action that returns a value\
**Description:** Assigns a sum of numbers to a variable.

**Usage example:** 
```ts
`variable` = variable::add([1, 2]);

//Or dry by positionals

variable::add(`variable`, [1, 2]);

//Or dry by keywords

variable::add(variable=`variable`, value=[1, 2]);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `value`    | list\[Number\]     | Numbers to Add     |
<h3 id=set_variable_add_item_enchantment>
  <code>variable::add_item_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Enchantment To an Item\
**Type:** An action that returns a value\
**Description:** Adds an enchantment to an item and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::add_item_enchantment(item("stick"), "enchantment", 1);

//Or from the object

`variable` = item("stick").add_item_enchantment("enchantment", 1);

//Or dry by positionals

variable::add_item_enchantment(`variable`, item("stick"), "enchantment", 1);

//Or dry by keywords

variable::add_item_enchantment(variable=`variable`, item=item("stick"), enchantment="enchantment", level=1);
```

**Arguments:**

| **Name**      | **Type**         | **Description**    |
| ------------- | ---------------- | ------------------ |
| `variable`    | Variable\[Item\] | Variable to assign |
| `item`        | Item             | Item               |
| `enchantment` | Text             | Enchant ID         |
| `level`       | Number           | Enchant Level      |
<h3 id=set_variable_add_item_potion_effects>
  <code>variable::add_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Potion Effects\
**Type:** An action that returns a value\
**Description:** Sets the potion effects of an item and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::add_item_potion_effects([potion("slow_falling"), potion("slow_falling")], item("stick"), "FALSE", "FALSE", "AMBIENT");

//Or from the object

`variable` = item("stick").add_item_potion_effects([potion("slow_falling"), potion("slow_falling")], "FALSE", "FALSE", "AMBIENT");

//Or dry by positionals

variable::add_item_potion_effects(`variable`, [potion("slow_falling"), potion("slow_falling")], item("stick"), "FALSE", "FALSE", "AMBIENT");

//Or dry by keywords

variable::add_item_potion_effects(variable=`variable`, potions=[potion("slow_falling"), potion("slow_falling")], item=item("stick"), overwrite="FALSE", show_icon="FALSE", particle_mode="AMBIENT");
```

**Arguments:**

| **Name**        | **Type**                                                                       | **Description**            |
| --------------- | ------------------------------------------------------------------------------ | -------------------------- |
| `variable`      | Variable\[Item\]                                                               | Variable to assign         |
| `potions`       | list\[Potion\]                                                                 | Potion Effects             |
| `item`          | Item                                                                           | Item                       |
| `overwrite`     | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes                                 | Overwrite existing effects |
| `show_icon`     | Marker<br/>**FALSE** - None<br/>**TRUE** - Yes                                 | Show Effect Icon           |
| `particle_mode` | Marker<br/>**AMBIENT** - Transparent<br/>**NONE** - None<br/>**REGULAR** - Yes | Show Particles             |
<h3 id=set_variable_add_vectors>
  <code>variable::add_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sum Of Vectors\
**Type:** An action that returns a value\
**Description:** Sets the sum of vectors value to a variable.

**Usage example:** 
```ts
`variable` = variable::add_vectors([vector(0,0,0), vector(0,0,0)]);

//Or dry by positionals

variable::add_vectors(`variable`, [vector(0,0,0), vector(0,0,0)]);

//Or dry by keywords

variable::add_vectors(variable=`variable`, vectors=[vector(0,0,0), vector(0,0,0)]);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Vector\] | Variable to assign |
| `vectors`  | list\[Vector\]     | Vectors to Add     |
<h3 id=set_variable_align_location>
  <code>variable::align_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Round Location\
**Type:** An action that returns a value\
**Description:** Rounds the location to the center or corner of the block and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::align_location(location(0,0,0,0,0), "KEEP", "ALL", "BLOCK_CENTER");

//Or from the object

`variable` = location(0,0,0,0,0).align_location("KEEP", "ALL", "BLOCK_CENTER");

//Or dry by positionals

variable::align_location(`variable`, location(0,0,0,0,0), "KEEP", "ALL", "BLOCK_CENTER");

//Or dry by keywords

variable::align_location(variable=`variable`, location=location(0,0,0,0,0), rotation_mode="KEEP", coordinates_mode="ALL", align_mode="BLOCK_CENTER");
```

**Arguments:**

| **Name**           | **Type**                                                                                        | **Description**    |
| ------------------ | ----------------------------------------------------------------------------------------------- | ------------------ |
| `variable`         | Variable\[Location\]                                                                            | Variable to assign |
| `location`         | Location                                                                                        | Location           |
| `rotation_mode`    | Marker<br/>**KEEP** - Enable<br/>**REMOVE** - Disable                                           | Keep Rotation      |
| `coordinates_mode` | Marker<br/>**ALL** - All Coordinates<br/>**X_Z** - X and Z Coordinates<br/>**Y** - Y Coordinate | Coordinate Type    |
| `align_mode`       | Marker<br/>**BLOCK_CENTER** - Block Center<br/>**CORNER** - To Block Corner                     | Round Mode         |
<h3 id=set_variable_align_to_axis_vector>
  <code>variable::align_to_axis_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Align Vector\
**Type:** An action that returns a value\
**Description:** Aligns a vector to the nearest axis and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::align_to_axis_vector(vector(0,0,0), "FALSE");

//Or from the object

`variable` = vector(0,0,0).align_to_axis_vector("FALSE");

//Or dry by positionals

variable::align_to_axis_vector(`variable`, vector(0,0,0), "FALSE");

//Or dry by keywords

variable::align_to_axis_vector(variable=`variable`, vector=vector(0,0,0), normalize="FALSE");
```

**Arguments:**

| **Name**    | **Type**                                                         | **Description**       |
| ----------- | ---------------------------------------------------------------- | --------------------- |
| `variable`  | Variable\[Vector\]                                               | Variable to assign    |
| `vector`    | Vector                                                           | Vector to align       |
| `normalize` | Marker<br/>**FALSE** - Original Length<br/>**TRUE** - Normalized | Vector type to output |
<h3 id=set_variable_append_component>
  <code>variable::append_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Append Stylized Texts\
**Type:** An action that returns a value\
**Description:** Appends different Styled Text together.

**Usage example:** 
```ts
`variable` = variable::append_component(["components", "components"], "CONCATENATION");

//Or dry by positionals

variable::append_component(`variable`, ["components", "components"], "CONCATENATION");

//Or dry by keywords

variable::append_component(variable=`variable`, components=["components", "components"], merging="CONCATENATION");
```

**Arguments:**

| **Name**     | **Type**                                                                                                    | **Description** |
| ------------ | ----------------------------------------------------------------------------------------------------------- | --------------- |
| `variable`   | Variable\[Text\]                                                                                            | Variable to set |
| `components` | list\[Text\]                                                                                                | Texts to append |
| `merging`    | Marker<br/>**CONCATENATION** - Merging<br/>**SEPARATE_LINES** - Separate with lines<br/>**SPACES** - Spaces | Merge Text      |
<h3 id=set_variable_append_list>
  <code>variable::append_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Combine Two Lists\
**Type:** An action that returns a value\
**Description:** Combines two specified lists into one.

**Usage example:** 
```ts
`variable` = variable::append_list(`list_1`, `list_2`);

//Or from the object

`variable` = `list_1`.append_list(`list_2`);

//Or dry by positionals

variable::append_list(`variable`, `list_1`, `list_2`);

//Or dry by keywords

variable::append_list(variable=`variable`, list_1=`list_1`, list_2=`list_2`);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[List\] | Variable to Assign |
| `list_1`   | List             | First List         |
| `list_2`   | List             | Second List        |
<h3 id=set_variable_append_map>
  <code>variable::append_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Combine Dictionaries\
**Type:** An action that returns a value\
**Description:** Concatenates two dictionaries and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::append_map(`map`, `other_map`);

//Or from the object

`variable` = `map`.append_map(`other_map`);

//Or dry by positionals

variable::append_map(`variable`, `map`, `other_map`);

//Or dry by keywords

variable::append_map(variable=`variable`, map=`map`, other_map=`other_map`);
```

**Arguments:**

| **Name**    | **Type**               | **Description**    |
| ----------- | ---------------------- | ------------------ |
| `variable`  | Variable\[Dictionary\] | Variable to Assign |
| `map`       | Dictionary             | First Dictionary   |
| `other_map` | Dictionary             | Second Dictionary  |
<h3 id=set_variable_append_value>
  <code>variable::append_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add List Value\
**Type:** Action without value\
**Description:** Adds the specified values to the end of the list.

**Usage example:** 
```ts
variable::append_value(`variable`, ["any value", "any value"]);

//Or from the object

`variable`.append_value(["any value", "any value"]);

//Or dry by keywords

variable::append_value(variable=`variable`, values=["any value", "any value"]);
```

**Arguments:**

| **Name**   | **Type**          | **Description** |
| ---------- | ----------------- | --------------- |
| `variable` | Variable          | List            |
| `values`   | list\[Any Value\] | Values          |
<h3 id=set_variable_atan2>
  <code>variable::atan2</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Inverse Tangent\
**Type:** An action that returns a value\
**Description:** Returns the inverse tangent of the two specified numbers.

**Usage example:** 
```ts
`variable` = variable::atan2(1, 2);

//Or dry by positionals

variable::atan2(`variable`, 1, 2);

//Or dry by keywords

variable::atan2(variable=`variable`, y=1, x=2);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `y`        | Number             | First Number (y)   |
| `x`        | Number             | Second Number (x)  |
<h3 id=set_variable_average>
  <code>variable::average</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Average\
**Type:** An action that returns a value\
**Description:** Sets the average of numbers to a variable.

**Usage example:** 
```ts
`variable` = variable::average([1, 2], "ARITHMETIC");

//Or dry by positionals

variable::average(`variable`, [1, 2], "ARITHMETIC");

//Or dry by keywords

variable::average(variable=`variable`, value=[1, 2], type="ARITHMETIC");
```

**Arguments:**

| **Name**   | **Type**                                                                                                   | **Description**      |
| ---------- | ---------------------------------------------------------------------------------------------------------- | -------------------- |
| `variable` | Variable\[Number\]                                                                                         | Variable to assign   |
| `value`    | list\[Number\]                                                                                             | Numbers to get value |
| `type`     | Marker<br/>**ARITHMETIC** - None<br/>**GEOMETRIC** - None<br/>**HARMONIC** - None<br/>**QUADRATIC** - None | None                 |
<h3 id=set_variable_bitwise_operation>
  <code>variable::bitwise_operation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Bitwise Operation on Numbers\
**Type:** An action that returns a value\
**Description:** Sets the result of a bitwise operation on numbers to a variable.

**Usage example:** 
```ts
`variable` = variable::bitwise_operation(1, 2, "AND");

//Or dry by positionals

variable::bitwise_operation(`variable`, 1, 2, "AND");

//Or dry by keywords

variable::bitwise_operation(variable=`variable`, operand1=1, operand2=2, operator="AND");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                                                                                                                                                    | **Description**    |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable\[Number\]                                                                                                                                                                                                                                                          | Variable to assign |
| `operand1` | Number                                                                                                                                                                                                                                                                      | First operand      |
| `operand2` | Number                                                                                                                                                                                                                                                                      | Second Operand     |
| `operator` | Marker<br/>**AND** - And (and)<br/>**LEFT_SHIFT** - Shift Left (left_shift)<br/>**NOT** - NOT (not)<br/>**OR** - OR (or)<br/>**RIGHT_SHIFT** - Shift Right (right_shift)<br/>**UNSIGNED_RIGHT_SHIFT** - Unsigned Right Shift (unsigned_right_shift)<br/>**XOR** - XOR (xor) | Operation Type     |
<h3 id=set_variable_bytes_to_text>
  <code>variable::bytes_to_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Convert bytes to text\
**Type:** An action that returns a value\
**Description:** Converts bytes to text and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::bytes_to_text([1, 2], "UTF_8");

//Or dry by positionals

variable::bytes_to_text(`variable`, [1, 2], "UTF_8");

//Or dry by keywords

variable::bytes_to_text(variable=`variable`, bytes=[1, 2], charset="UTF_8");
```

**Arguments:**

| **Name**   | **Type**                                          | **Description**    |
| ---------- | ------------------------------------------------- | ------------------ |
| `variable` | Variable\[Text\]                                  | Variable to assign |
| `bytes`    | list\[Number\]                                    | Bytes to convert   |
| `charset`  | Marker<br/>**UTF_8** - None<br/>**ASCII** - ASCII | Encoding           |
<h3 id=set_variable_center_location>
  <code>variable::center_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Center Location\
**Type:** An action that returns a value\
**Description:** Sets the location to the center between other locations and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::center_location([location(0,0,0,0,0), location(0,0,0,0,0)]);

//Or dry by positionals

variable::center_location(`variable`, [location(0,0,0,0,0), location(0,0,0,0,0)]);

//Or dry by keywords

variable::center_location(variable=`variable`, locations=[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

**Arguments:**

| **Name**    | **Type**             | **Description**    |
| ----------- | -------------------- | ------------------ |
| `variable`  | Variable\[Location\] | Variable to assign |
| `locations` | list\[Location\]     | Locations to Set   |
<h3 id=set_variable_change_component_parsing>
  <code>variable::change_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Change Stylized Text Parsing\
**Type:** An action that returns a value\
**Description:** Change how the Styled Text is parsed.

**Usage example:** 
```ts
`variable` = variable::change_component_parsing("component", "JSON");

//Or from the object

`variable` = "component".change_component_parsing("JSON");

//Or dry by positionals

variable::change_component_parsing(`variable`, "component", "JSON");

//Or dry by keywords

variable::change_component_parsing(variable=`variable`, component="component", parsing="JSON");
```

**Arguments:**

| **Name**    | **Type**                                                                                                      | **Description**   |
| ----------- | ------------------------------------------------------------------------------------------------------------- | ----------------- |
| `variable`  | Variable\[Text\]                                                                                              | Variable to set   |
| `component` | Text                                                                                                          | The text to parse |
| `parsing`   | Marker<br/>**JSON** - JSON<br/>**LEGACY** - Colored (&)<br/>**MINIMESSAGE** - Stylized<br/>**PLAIN** - Normal | Parse method      |
<h3 id=set_variable_char_to_number>
  <code>variable::char_to_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number By Character\
**Type:** An action that returns a value\
**Description:** Gets a specific number from a character and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::char_to_number("char");

//Or from the object

`variable` = "char".char_to_number();

//Or dry by positionals

variable::char_to_number(`variable`, "char");

//Or dry by keywords

variable::char_to_number(variable=`variable`, char="char");
```

**Arguments:**

| **Name**   | **Type**           | **Description**         |
| ---------- | ------------------ | ----------------------- |
| `variable` | Variable\[Number\] | Variable to assign      |
| `char`     | Text               | Character to get number |
<h3 id=set_variable_clamp>
  <code>variable::clamp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clamp Number\
**Type:** An action that returns a value\
**Description:** Checks if a number is between the minimum and maximum values, and if not, sets it to the closest.

**Usage example:** 
```ts
`variable` = variable::clamp(1, 2, 3);

//Or from the object

`variable` = (1).clamp(2, 3);

//Or dry by positionals

variable::clamp(`variable`, 1, 2, 3);

//Or dry by keywords

variable::clamp(variable=`variable`, number=1, min=2, max=3);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to Assign |
| `number`   | Number             | Number to Clamp    |
| `min`      | Number             | Minimum Value      |
| `max`      | Number             | Max Value          |
<h3 id=set_variable_clamp_location>
  <code>variable::clamp_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::clamp_location(location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "XYZ");

//Or from the object

`variable` = location(0,0,0,0,0).clamp_location(location(0,0,0,0,0), location(0,0,0,0,0), "XYZ");

//Or dry by positionals

variable::clamp_location(`variable`, location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "XYZ");

//Or dry by keywords

variable::clamp_location(variable=`variable`, location=location(0,0,0,0,0), corner_1=location(0,0,0,0,0), corner_2=location(0,0,0,0,0), coordinates_mode="XYZ");
```

**Arguments:**

| **Name**           | **Type**                                                     | **Description** |
| ------------------ | ------------------------------------------------------------ | --------------- |
| `variable`         | Variable\[Location\]                                         | None            |
| `location`         | Location                                                     | None            |
| `corner_1`         | Location                                                     | None            |
| `corner_2`         | Location                                                     | None            |
| `coordinates_mode` | Marker<br/>**XYZ** - None<br/>**XZ** - None<br/>**Y** - None | None            |
<h3 id=set_variable_clear_color_codes>
  <code>variable::clear_color_codes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Text Colors\
**Type:** An action that returns a value\
**Description:** Clears text from color codes and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::clear_color_codes("text");

//Or from the object

`variable` = "text".clear_color_codes();

//Or dry by positionals

variable::clear_color_codes(`variable`, "text");

//Or dry by keywords

variable::clear_color_codes(variable=`variable`, text="text");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `text`     | Text             | Text to change     |
<h3 id=set_variable_clear_map>
  <code>variable::clear_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Dictionary\
**Type:** Action without value\
**Description:** Clears the dictionary.

**Usage example:** 
```ts
variable::clear_map(`map`);

//Or from the object

`map`.clear_map();

//Or dry by keywords

variable::clear_map(map=`map`);
```

**Arguments:**

| **Name** | **Type** | **Description**     |
| -------- | -------- | ------------------- |
| `map`    | Variable | Dictionary to Clear |
<h3 id=set_variable_code_bytes>
  <code>variable::code_bytes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::code_bytes([1, 2], "BASE64_ENCODE");

//Or dry by positionals

variable::code_bytes(`variable`, [1, 2], "BASE64_ENCODE");

//Or dry by keywords

variable::code_bytes(variable=`variable`, input=[1, 2], codec="BASE64_ENCODE");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                     | **Description** |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `variable` | Variable\[List\]                                                                                                             | None            |
| `input`    | list\[Number\]                                                                                                               | None            |
| `codec`    | Marker<br/>**BASE64_ENCODE** - None<br/>**BASE64_DECODE** - None<br/>**ZLIB_COMPRESS** - None<br/>**ZLIB_DECOMPRESS** - None | None            |
<h3 id=set_variable_compact_component>
  <code>variable::compact_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Compact Stylized Text\
**Type:** An action that returns a value\
**Description:** Compacts the Styled Text by removing all styles.

**Usage example:** 
```ts
`variable` = variable::compact_component("component");

//Or from the object

`variable` = "component".compact_component();

//Or dry by positionals

variable::compact_component(`variable`, "component");

//Or dry by keywords

variable::compact_component(variable=`variable`, component="component");
```

**Arguments:**

| **Name**    | **Type**         | **Description**    |
| ----------- | ---------------- | ------------------ |
| `variable`  | Variable\[Text\] | Variable to assign |
| `component` | Text             | The Styled Text    |
<h3 id=set_variable_component_of_children>
  <code>variable::component_of_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Styled Text From Children\
**Type:** An action that returns a value\
**Description:** Creates a new Styled Text from the children Styled Text.

**Usage example:** 
```ts
`variable` = variable::component_of_children(["components", "components"]);

//Or dry by positionals

variable::component_of_children(`variable`, ["components", "components"]);

//Or dry by keywords

variable::component_of_children(variable=`variable`, components=["components", "components"]);
```

**Arguments:**

| **Name**     | **Type**         | **Description**    |
| ------------ | ---------------- | ------------------ |
| `variable`   | Variable\[Text\] | Variable to assign |
| `components` | list\[Text\]     | Stylized texts     |
<h3 id=set_variable_convert_number_to_text>
  <code>variable::convert_number_to_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Convert Number To Text\
**Type:** An action that returns a value\
**Description:** Sets the result of converting a number to text to a variable.\
**Additional info:**\
&nbsp;&nbsp;Only works with integers.\
&nbsp;&nbsp;Number base must be between 2 and 36 inclusive.

**Usage example:** 
```ts
`variable` = variable::convert_number_to_text(1, 2);

//Or from the object

`variable` = (1).convert_number_to_text(2);

//Or dry by positionals

variable::convert_number_to_text(`variable`, 1, 2);

//Or dry by keywords

variable::convert_number_to_text(variable=`variable`, number=1, radix=2);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `number`   | Number           | Number to convert  |
| `radix`    | Number           | Number Base        |
<h3 id=set_variable_convert_text_to_number>
  <code>variable::convert_text_to_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Convert Text To Number\
**Type:** An action that returns a value\
**Description:** Sets the result of converting text to number to a variable. Works only with integers.

**Usage example:** 
```ts
`variable` = variable::convert_text_to_number("text", 1);

//Or from the object

`variable` = "text".convert_text_to_number(1);

//Or dry by positionals

variable::convert_text_to_number(`variable`, "text", 1);

//Or dry by keywords

variable::convert_text_to_number(variable=`variable`, text="text", radix=1);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `text`     | Text               | Text to convert    |
| `radix`    | Number             | Number Base        |
<h3 id=set_variable_cosine>
  <code>variable::cosine</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Cosine\
**Type:** An action that returns a value\
**Description:** Returns the cosine of a number.

**Usage example:** 
```ts
`variable` = variable::cosine(1, "ARCCOSINE", "DEGREES");

//Or from the object

`variable` = (1).cosine("ARCCOSINE", "DEGREES");

//Or dry by positionals

variable::cosine(`variable`, 1, "ARCCOSINE", "DEGREES");

//Or dry by keywords

variable::cosine(variable=`variable`, number=1, variant="ARCCOSINE", input="DEGREES");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                                       | **Description**      |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| `variable` | Variable\[Number\]                                                                                                                                             | Variable to assign   |
| `number`   | Number                                                                                                                                                         | Number to get cosine |
| `variant`  | Marker<br/>**ARCCOSINE** - Arccosine<br/>**COSINE** - Cosine<br/>**HYPERBOLIC_ARCCOSINE** - Hyperbolic Arccosine<br/>**HYPERBOLIC_COSINE** - Hyperbolic Cosine | Operation Type       |
| `input`    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                                                                                     | Corner Type          |
<h3 id=set_variable_cotangent>
  <code>variable::cotangent</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Cotangent\
**Type:** An action that returns a value\
**Description:** Returns the cotangent of a number.

**Usage example:** 
```ts
`variable` = variable::cotangent(1, "ARCCOTANGENT", "DEGREES");

//Or from the object

`variable` = (1).cotangent("ARCCOTANGENT", "DEGREES");

//Or dry by positionals

variable::cotangent(`variable`, 1, "ARCCOTANGENT", "DEGREES");

//Or dry by keywords

variable::cotangent(variable=`variable`, number=1, variant="ARCCOTANGENT", input="DEGREES");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                                                               | **Description**         |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `variable` | Variable\[Number\]                                                                                                                                                                     | Variable to assign      |
| `number`   | Number                                                                                                                                                                                 | Number to get cotangent |
| `variant`  | Marker<br/>**ARCCOTANGENT** - Arccotangent<br/>**COTANGENT** - Cotangent<br/>**HYPERBOLIC_ARCCOTANGENT** - Hyperbolic Arccotangent<br/>**HYPERBOLIC_COTANGENT** - Hyperbolic Cotangent | Operation Type          |
| `input`    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                                                                                                             | Angle Type              |
<h3 id=set_variable_create_keybind_component>
  <code>variable::create_keybind_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Stylized Text With Key Binding\
**Type:** An action that returns a value\
**Description:** Create a keybind Styled Text.

**Usage example:** 
```ts
`variable` = variable::create_keybind_component("key");

//Or dry by positionals

variable::create_keybind_component(`variable`, "key");

//Or dry by keywords

variable::create_keybind_component(variable=`variable`, key="key");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `key`      | Text             | Keybind key        |
<h3 id=set_variable_create_list>
  <code>variable::create_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create List\
**Type:** An action that returns a value\
**Description:** Creates a list containing the specified values.\
**Additional info:**\
&nbsp;&nbsp;Clears the list if it already exists.

**Usage example:** 
```ts
`variable` = variable::create_list(["any value", "any value"]);

//Or dry by positionals

variable::create_list(`variable`, ["any value", "any value"]);

//Or dry by keywords

variable::create_list(variable=`variable`, values=["any value", "any value"]);
```

**Arguments:**

| **Name**   | **Type**          | **Description**    |
| ---------- | ----------------- | ------------------ |
| `variable` | Variable\[List\]  | Variable to assign |
| `values`   | list\[Any Value\] | Values             |
<h3 id=set_variable_create_map>
  <code>variable::create_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Dictionary\
**Type:** An action that returns a value\
**Description:** Creates a dictionary from a list of keys and values and assigns the result to a variable.\
**Additional info:**\
&nbsp;&nbsp;Clears the dictionary if it already exists.

**Usage example:** 
```ts
`variable` = variable::create_map(`keys`, `values`);

//Or dry by positionals

variable::create_map(`variable`, `keys`, `values`);

//Or dry by keywords

variable::create_map(variable=`variable`, keys=`keys`, values=`values`);
```

**Arguments:**

| **Name**   | **Type**               | **Description**    |
| ---------- | ---------------------- | ------------------ |
| `variable` | Variable\[Dictionary\] | Variable to assign |
| `keys`     | List                   | List Keys          |
| `values`   | List                   | List of Values     |
<h3 id=set_variable_create_map_from_values>
  <code>variable::create_map_from_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Dictionary From Values\
**Type:** An action that returns a value\
**Description:** Creates a dictionary from keys and values and assigns the result to a variable.\
**Additional info:**\
&nbsp;&nbsp;Clears the dictionary if it already exists.

**Usage example:** 
```ts
`variable` = variable::create_map_from_values(["any value", "any value"], ["any value", "any value"]);

//Or dry by positionals

variable::create_map_from_values(`variable`, ["any value", "any value"], ["any value", "any value"]);

//Or dry by keywords

variable::create_map_from_values(variable=`variable`, keys=["any value", "any value"], values=["any value", "any value"]);
```

**Arguments:**

| **Name**   | **Type**               | **Description**    |
| ---------- | ---------------------- | ------------------ |
| `variable` | Variable\[Dictionary\] | Variable to assign |
| `keys`     | list\[Any Value\]      | Keys               |
| `values`   | list\[Any Value\]      | Values             |
<h3 id=set_variable_create_translatable_component>
  <code>variable::create_translatable_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Translatable Stylized Text\
**Type:** An action that returns a value\
**Description:** Creates a translated Styled Text.\
**Additional info:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
`variable` = variable::create_translatable_component("key", "fallback", ["args", "args"]);

//Or dry by positionals

variable::create_translatable_component(`variable`, "key", "fallback", ["args", "args"]);

//Or dry by keywords

variable::create_translatable_component(variable=`variable`, key="key", fallback="fallback", args=["args", "args"]);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `key`      | Text             | Key                |
| `fallback` | Text             | None               |
| `args`     | list\[Text\]     | Arguments to add   |
<h3 id=set_variable_decrement>
  <code>variable::decrement</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Decrement (-=)\
**Type:** Action without value\
**Description:** Subtracts the selected number from the variable.

**Usage example:** 
```ts
variable::decrement(`variable`, 1);

//Or from the object

`variable`.decrement(1);

//Or dry by keywords

variable::decrement(variable=`variable`, number=1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `number`   | Number   | Number to Subtract |
<h3 id=set_variable_divide>
  <code>variable::divide</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Divide (÷)\
**Type:** An action that returns a value\
**Description:** Assigns a quotient to a variable.

**Usage example:** 
```ts
`variable` = variable::divide([1, 2], "CEIL");

//Or dry by positionals

variable::divide(`variable`, [1, 2], "CEIL");

//Or dry by keywords

variable::divide(variable=`variable`, value=[1, 2], division_mode="CEIL");
```

**Arguments:**

| **Name**        | **Type**                                                                                                                    | **Description**    |
| --------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`      | Variable\[Number\]                                                                                                          | Variable to assign |
| `value`         | list\[Number\]                                                                                                              | Numbers to Divide  |
| `division_mode` | Marker<br/>**CEIL** - Round up<br/>**DEFAULT** - Default<br/>**FLOOR** - Round down<br/>**ROUND_TO_INT** - Round To Integer | Division Mode      |
<h3 id=set_variable_divide_vector>
  <code>variable::divide_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Vector Divide\
**Type:** An action that returns a value\
**Description:** Sets the result of dividing two vectors to a variable.

**Usage example:** 
```ts
`variable` = variable::divide_vector(vector(0,0,0), vector(0,0,0));

//Or dry by positionals

variable::divide_vector(`variable`, vector(0,0,0), vector(0,0,0));

//Or dry by keywords

variable::divide_vector(variable=`variable`, vector=vector(0,0,0), divider=vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Vector\] | Variable to assign |
| `vector`   | Vector             | Vector to change   |
| `divider`  | Vector             | Vector Divider     |
<h3 id=set_variable_dummy>
  <code>variable::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action without value\
**Description:** ...

**Usage example:** 
```ts
variable::dummy();
```

<h3 id=set_variable_edit_item_custom_model_data>
  <code>variable::edit_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::edit_item_custom_model_data(item("stick"), ["any value", "any value"], "FLOATS", "SET");

//Or from the object

`variable` = item("stick").edit_item_custom_model_data(["any value", "any value"], "FLOATS", "SET");

//Or dry by positionals

variable::edit_item_custom_model_data(`variable`, item("stick"), ["any value", "any value"], "FLOATS", "SET");

//Or dry by keywords

variable::edit_item_custom_model_data(variable=`variable`, item=item("stick"), data=["any value", "any value"], value_type="FLOATS", setup_mode="SET");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                      | **Description** |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `variable`   | Variable\[Item\]                                                                                                              | None            |
| `item`       | Item                                                                                                                          | None            |
| `data`       | list\[Any Value\]                                                                                                             | None            |
| `value_type` | Marker<br/>**FLOATS** - None<br/>**BOOLEANS** - None<br/>**STRINGS** - None<br/>**COLORS** - None                             | None            |
| `setup_mode` | Marker<br/>**SET** - None<br/>**ADD** - None<br/>**REMOVE_ALL** - None<br/>**REMOVE_FIRST** - None<br/>**REMOVE_LAST** - None | None            |
<h3 id=set_variable_face_location>
  <code>variable::face_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Location Face Another Location\
**Type:** An action that returns a value\
**Description:** Rotates a location in the direction of another location and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::face_location(location(0,0,0,0,0), location(0,0,0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).face_location(location(0,0,0,0,0));

//Or dry by positionals

variable::face_location(`variable`, location(0,0,0,0,0), location(0,0,0,0,0));

//Or dry by keywords

variable::face_location(variable=`variable`, location=location(0,0,0,0,0), target=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**             | **Description**    |
| ---------- | -------------------- | ------------------ |
| `variable` | Variable\[Location\] | Variable to assign |
| `location` | Location             | Locations to Set   |
| `target`   | Location             | Target Location    |
<h3 id=set_variable_find_nearest_location>
  <code>variable::find_nearest_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::find_nearest_location(location(0,0,0,0,0), [location(0,0,0,0,0), location(0,0,0,0,0)], "XYZ");

//Or from the object

`variable` = location(0,0,0,0,0).find_nearest_location([location(0,0,0,0,0), location(0,0,0,0,0)], "XYZ");

//Or dry by positionals

variable::find_nearest_location(`variable`, location(0,0,0,0,0), [location(0,0,0,0,0), location(0,0,0,0,0)], "XYZ");

//Or dry by keywords

variable::find_nearest_location(variable=`variable`, location=location(0,0,0,0,0), locations=[location(0,0,0,0,0), location(0,0,0,0,0)], distance_type="XYZ");
```

**Arguments:**

| **Name**        | **Type**                                                     | **Description** |
| --------------- | ------------------------------------------------------------ | --------------- |
| `variable`      | Variable\[Location\]                                         | None            |
| `location`      | Location                                                     | None            |
| `locations`     | list\[Location\]                                             | None            |
| `distance_type` | Marker<br/>**XYZ** - None<br/>**XZ** - None<br/>**Y** - None | None            |
<h3 id=set_variable_find_nearest_number>
  <code>variable::find_nearest_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::find_nearest_number(`number`, [1, 2]);

//Or from the object

`variable` = `number`.find_nearest_number([1, 2]);

//Or dry by positionals

variable::find_nearest_number(`variable`, `number`, [1, 2]);

//Or dry by keywords

variable::find_nearest_number(variable=`variable`, number=`number`, numbers=[1, 2]);
```

**Arguments:**

| **Name**   | **Type**           | **Description** |
| ---------- | ------------------ | --------------- |
| `variable` | Variable\[Number\] | None            |
| `number`   | Variable           | None            |
| `numbers`  | list\[Number\]     | None            |
<h3 id=set_variable_flatten_list>
  <code>variable::flatten_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Flatten List\
**Type:** An action that returns a value\
**Description:** Splits the sublists of the specified list into separate items.

**Usage example:** 
```ts
`variable` = variable::flatten_list(`list`, "FALSE");

//Or from the object

`variable` = `list`.flatten_list("FALSE");

//Or dry by positionals

variable::flatten_list(`variable`, `list`, "FALSE");

//Or dry by keywords

variable::flatten_list(variable=`variable`, list=`list`, deep="FALSE");
```

**Arguments:**

| **Name**   | **Type**                                        | **Description**    |
| ---------- | ----------------------------------------------- | ------------------ |
| `variable` | Variable\[List\]                                | Variable to assign |
| `list`     | List                                            | List               |
| `deep`     | Marker<br/>**FALSE** - None<br/>**TRUE** - None | None               |
<h3 id=set_variable_format_timestamp>
  <code>variable::format_timestamp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Time Format\
**Type:** An action that returns a value\
**Description:** Converts a number (milliseconds) to the specified time format and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::format_timestamp(1, "pattern", "zone_id", "locale", "CUSTOM");

//Or from the object

`variable` = (1).format_timestamp("pattern", "zone_id", "locale", "CUSTOM");

//Or dry by positionals

variable::format_timestamp(`variable`, 1, "pattern", "zone_id", "locale", "CUSTOM");

//Or dry by keywords

variable::format_timestamp(variable=`variable`, time=1, pattern="pattern", zone_id="zone_id", locale="locale", format="CUSTOM");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Description**                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| `variable` | Variable\[Text\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Variable to assign                  |
| `time`     | Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Number to convert                   |
| `pattern`  | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Time Pattern (e.g. mm\:ss)          |
| `zone_id`  | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Timezone (GMT+1\.\.13, GMT-1\.\.13) |
| `locale`   | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Language (ru_RU, en_US...)          |
| `format`   | Marker<br/>**CUSTOM** - Custom<br/>**DD_MM_YYYY** - 01\/01\/1970 (dd_mm_yyyy)<br/>**DD_MM_YYYY_HH_MM_S** - 01\/01\/1970 00\:00\:00 (dd_mm_yyyy_hh_mm_s)<br/>**EEEE** - Thursday (eeee)<br/>**EEE_D_MMMM** - Thu, 01 January (eee_d_mmmm)<br/>**EEE_MMMM_D** - Thu, January 01 (eee_mmmm_d)<br/>**HH_MM_SS** - 00\:00\:00 (hh_mm_ss)<br/>**H_H_M_M_S_S** - 00h00m00s (h_h_m_m_s_s)<br/>**H_MM_A** - 00\:00 AM (h_mm_a)<br/>**S_S** - 00.00 (s_s)<br/>**YYYY_MM_DD** - 1970\/01\/01 (yyyy_mm_dd)<br/>**YYYY_MM_DD_HH_MM_S** - 1970\/01\/01 00\:00\:00 (yyyy_mm_dd_hh_mm_s) | Time Format                         |
<h3 id=set_variable_gamma_function>
  <code>variable::gamma_function</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None\
&nbsp;&nbsp;None

**Usage example:** 
```ts
`variable` = variable::gamma_function(1);

//Or from the object

`variable` = (1).gamma_function();

//Or dry by positionals

variable::gamma_function(`variable`, 1);

//Or dry by keywords

variable::gamma_function(variable=`variable`, number=1);
```

**Arguments:**

| **Name**   | **Type**           | **Description** |
| ---------- | ------------------ | --------------- |
| `variable` | Variable\[Number\] | None            |
| `number`   | Number             | None            |
<h3 id=set_variable_gaussian_distribution>
  <code>variable::gaussian_distribution</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Normally Distributed Random Number\
**Type:** An action that returns a value\
**Description:** Produces a random number close to the mean μ with a standard deviation σ with a chance given by a normal distribution plot.

**Usage example:** 
```ts
`variable` = variable::gaussian_distribution(1, 2, "FOLDER_NORMAL");

//Or dry by positionals

variable::gaussian_distribution(`variable`, 1, 2, "FOLDER_NORMAL");

//Or dry by keywords

variable::gaussian_distribution(variable=`variable`, deviant=1, mean=2, distribution="FOLDER_NORMAL");
```

**Arguments:**

| **Name**       | **Type**                                                                            | **Description**            |
| -------------- | ----------------------------------------------------------------------------------- | -------------------------- |
| `variable`     | Variable\[Number\]                                                                  | Variable to Assign         |
| `deviant`      | Number                                                                              | Deviation of σ from mean μ |
| `mean`         | Number                                                                              | Mean μ                     |
| `distribution` | Marker<br/>**FOLDER_NORMAL** - Side Deviation >= μ<br/>**NORMAL** - Total Deviation | Type of σ deviation        |
<h3 id=set_variable_get_all_block_data>
  <code>variable::get_all_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get All Block Data\
**Type:** An action that returns a value\
**Description:** Sets all block data at the selected location to a variable.

**Usage example:** 
```ts
`variable` = variable::get_all_block_data(location(0,0,0,0,0), "FALSE");

//Or from the object

`variable` = location(0,0,0,0,0).get_all_block_data("FALSE");

//Or dry by positionals

variable::get_all_block_data(`variable`, location(0,0,0,0,0), "FALSE");

//Or dry by keywords

variable::get_all_block_data(variable=`variable`, location=location(0,0,0,0,0), hide_unspecified="FALSE");
```

**Arguments:**

| **Name**           | **Type**                                             | **Description**         |
| ------------------ | ---------------------------------------------------- | ----------------------- |
| `variable`         | Variable\[Text\]                                     | Variable to assign      |
| `location`         | Location                                             | Block Location          |
| `hide_unspecified` | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Hide Unspecified Values |
<h3 id=set_variable_get_all_coordinates>
  <code>variable::get_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get All Location Coordinates\
**Type:** An action that returns a value\
**Description:** Gets the value of all coordinates from a location and assigns them to variables.

**Usage example:** 
```ts
`x`, `y`, `z`, `yaw`, `pitch` = variable::get_all_coordinates(location(0,0,0,0,0));

//Or from the object

`x`, `y`, `z`, `yaw`, `pitch` = location(0,0,0,0,0).get_all_coordinates();

//Or dry by positionals

variable::get_all_coordinates(`x`, `y`, `z`, `yaw`, `pitch`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_all_coordinates(x=`x`, y=`y`, z=`z`, yaw=`yaw`, pitch=`pitch`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description**     |
| ---------- | ------------------ | ------------------- |
| `x`        | Variable\[Number\] | X Coordinate        |
| `y`        | Variable\[Number\] | Y Coordinate        |
| `z`        | Variable\[Number\] | Z Coordinate        |
| `yaw`      | Variable\[Number\] | Horizontal Rotation |
| `pitch`    | Variable\[Number\] | Pitch Vertical      |
| `location` | Location           | Location to Get     |
<h3 id=set_variable_get_angle_between_vectors>
  <code>variable::get_angle_between_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Angle Between Two Vectors\
**Type:** An action that returns a value\
**Description:** Sets the angle between two vectors to a variable.

**Usage example:** 
```ts
`variable` = variable::get_angle_between_vectors(vector(0,0,0), vector(0,0,0), "DEGREES");

//Or dry by positionals

variable::get_angle_between_vectors(`variable`, vector(0,0,0), vector(0,0,0), "DEGREES");

//Or dry by keywords

variable::get_angle_between_vectors(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0), angle_units="DEGREES");
```

**Arguments:**

| **Name**      | **Type**                                                   | **Description**    |
| ------------- | ---------------------------------------------------------- | ------------------ |
| `variable`    | Variable\[Number\]                                         | Variable to assign |
| `vector_1`    | Vector                                                     | First Vector       |
| `vector_2`    | Vector                                                     | Second Vector      |
| `angle_units` | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians | Angle Type         |
<h3 id=set_variable_get_block_custom_tag>
  <code>variable::get_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_block_custom_tag(location(0,0,0,0,0), "tag_name", "tag_value", "any value");

//Or dry by positionals

variable::get_block_custom_tag(`variable`, location(0,0,0,0,0), "tag_name", "tag_value", "any value");

//Or dry by keywords

variable::get_block_custom_tag(variable=`variable`, location=location(0,0,0,0,0), tag_name="tag_name", tag_value="tag_value", default_value="any value");
```

**Arguments:**

| **Name**        | **Type**              | **Description** |
| --------------- | --------------------- | --------------- |
| `variable`      | Variable\[Any Value\] | None            |
| `location`      | Location              | None            |
| `tag_name`      | Text                  | None            |
| `tag_value`     | Text                  | None            |
| `default_value` | Any Value             | None            |
<h3 id=set_variable_get_block_data>
  <code>variable::get_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Block Data\
**Type:** An action that returns a value\
**Description:** Gets the block data and assigns it to a variable.

**Usage example:** 
```ts
`variable` = variable::get_block_data(location(0,0,0,0,0), "tag_name");

//Or from the object

`variable` = location(0,0,0,0,0).get_block_data("tag_name");

//Or dry by positionals

variable::get_block_data(`variable`, location(0,0,0,0,0), "tag_name");

//Or dry by keywords

variable::get_block_data(variable=`variable`, location=location(0,0,0,0,0), tag_name="tag_name");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `location` | Location         | Block Location     |
| `tag_name` | Text             | Tag Name           |
<h3 id=set_variable_get_block_growth>
  <code>variable::get_block_growth</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Block Growth Level\
**Type:** An action that returns a value\
**Description:** Sets the block growth level at the specified location to a variable.

**Usage example:** 
```ts
`variable` = variable::get_block_growth(location(0,0,0,0,0), "GROWTH_PERCENTAGE");

//Or from the object

`variable` = location(0,0,0,0,0).get_block_growth("GROWTH_PERCENTAGE");

//Or dry by positionals

variable::get_block_growth(`variable`, location(0,0,0,0,0), "GROWTH_PERCENTAGE");

//Or dry by keywords

variable::get_block_growth(variable=`variable`, location=location(0,0,0,0,0), growth_unit="GROWTH_PERCENTAGE");
```

**Arguments:**

| **Name**      | **Type**                                                                                 | **Description**    |
| ------------- | ---------------------------------------------------------------------------------------- | ------------------ |
| `variable`    | Variable\[Number\]                                                                       | Variable to assign |
| `location`    | Location                                                                                 | Block Location     |
| `growth_unit` | Marker<br/>**GROWTH_PERCENTAGE** - Growth Percentage<br/>**GROWTH_STAGE** - Growth Stage | Unit               |
<h3 id=set_variable_get_block_material>
  <code>variable::get_block_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Block Type\
**Type:** An action that returns a value\
**Description:** Sets the block type at the selected location to a variable.

**Usage example:** 
```ts
`variable` = variable::get_block_material(location(0,0,0,0,0), "ID");

//Or from the object

`variable` = location(0,0,0,0,0).get_block_material("ID");

//Or dry by positionals

variable::get_block_material(`variable`, location(0,0,0,0,0), "ID");

//Or dry by keywords

variable::get_block_material(variable=`variable`, location=location(0,0,0,0,0), value_type="ID");
```

**Arguments:**

| **Name**     | **Type**                                                                                                               | **Description**    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable\[Text\]                                                                                                       | Variable to assign |
| `location`   | Location                                                                                                               | Block Location     |
| `value_type` | Marker<br/>**ID** - Block ID<br/>**ID_WITH_DATA** - ID and block data<br/>**ITEM** - As Item<br/>**NAME** - Block Name | Value Type         |
<h3 id=set_variable_get_block_material_property>
  <code>variable::get_block_material_property</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Block Property\
**Type:** An action that returns a value\
**Description:** Gets the specific block property and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_block_material_property(item("stone"), "BLAST_RESISTANCE");

//Or from the object

`variable` = item("stone").get_block_material_property("BLAST_RESISTANCE");

//Or dry by positionals

variable::get_block_material_property(`variable`, item("stone"), "BLAST_RESISTANCE");

//Or dry by keywords

variable::get_block_material_property(variable=`variable`, block=item("stone"), property="BLAST_RESISTANCE");
```

**Arguments:**

| **Name**   | **Type**                                                                                                           | **Description**    |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| `variable` | Variable\[Number\]                                                                                                 | Variable to assign |
| `block`    | Block                                                                                                              | Block to Get       |
| `property` | Marker<br/>**BLAST_RESISTANCE** - Blast Resistance<br/>**HARDNESS** - Hardness<br/>**SLIPPERINESS** - Slipperiness | Property           |
<h3 id=set_variable_get_block_power>
  <code>variable::get_block_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Redstone Power\
**Type:** An action that returns a value\
**Description:** Sets the redstone signal strength at the specified location to a variable.

**Usage example:** 
```ts
`variable` = variable::get_block_power(location(0,0,0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).get_block_power();

//Or dry by positionals

variable::get_block_power(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_block_power(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `location` | Location           | Block Location     |
<h3 id=set_variable_get_block_sound>
  <code>variable::get_block_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Block Sound\
**Type:** An action that returns a value\
**Description:** Gets the sound of a specified block and assigns it to a variable.

**Usage example:** 
```ts
`variable` = variable::get_block_sound(item("stone"), "BREAK");

//Or from the object

`variable` = item("stone").get_block_sound("BREAK");

//Or dry by positionals

variable::get_block_sound(`variable`, item("stone"), "BREAK");

//Or dry by keywords

variable::get_block_sound(variable=`variable`, block=item("stone"), source="BREAK");
```

**Arguments:**

| **Name**   | **Type**                                                                                                     | **Description**    |
| ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------ |
| `variable` | Variable\[Sound\]                                                                                            | Variable to assign |
| `block`    | Block                                                                                                        | Block              |
| `source`   | Marker<br/>**BREAK** - Break<br/>**PLACE** - Place<br/>**HIT** - Hit<br/>**FALL** - Fall<br/>**STEP** - Step | Sound Source       |
<h3 id=set_variable_get_blocks_by_tag>
  <code>variable::get_blocks_by_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_blocks_by_tag("namespace", "ID");

//Or dry by positionals

variable::get_blocks_by_tag(`variable`, "namespace", "ID");

//Or dry by keywords

variable::get_blocks_by_tag(variable=`variable`, namespace="namespace", result_type="ID");
```

**Arguments:**

| **Name**      | **Type**                                                                    | **Description** |
| ------------- | --------------------------------------------------------------------------- | --------------- |
| `variable`    | Variable\[List\]                                                            | None            |
| `namespace`   | Text                                                                        | None            |
| `result_type` | Marker<br/>**ID** - None<br/>**TRANSLATION_KEY** - None<br/>**ITEM** - None | None            |
<h3 id=set_variable_get_book_text>
  <code>variable::get_book_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Book Text\
**Type:** An action that returns a value\
**Description:** Sets the value of the book text on a specific page to a variable.

**Usage example:** 
```ts
`variable` = variable::get_book_text(item("stick"), 1);

//Or from the object

`variable` = item("stick").get_book_text(1);

//Or dry by positionals

variable::get_book_text(`variable`, item("stick"), 1);

//Or dry by keywords

variable::get_book_text(variable=`variable`, book=item("stick"), page=1);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `book`     | Item             | Book to get value  |
| `page`     | Number           | Page Number        |
<h3 id=set_variable_get_brushable_block_item>
  <code>variable::get_brushable_block_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Suspicious Block Item\
**Type:** An action that returns a value\
**Description:** Get an item from a suspicious block (sand, gravel) and assign the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_brushable_block_item(location(0,0,0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).get_brushable_block_item();

//Or dry by positionals

variable::get_brushable_block_item(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_brushable_block_item(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `location` | Location         | Block Location     |
<h3 id=set_variable_get_bundle_items>
  <code>variable::get_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Bundle Items\
**Type:** Action without value\
**Description:** Gets the list of items stored in a bundle.

**Usage example:** 
```ts
variable::get_bundle_items(`variable`, item("stick"));

//Or from the object

item("stick").get_bundle_items(`variable`);

//Or dry by keywords

variable::get_bundle_items(variable=`variable`, bundle=item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `variable` | Variable | Variable to set |
| `bundle`   | Item     | Bundle          |
<h3 id=set_variable_get_char_at>
  <code>variable::get_char_at</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Character By Index\
**Type:** An action that returns a value\
**Description:** Get the character from the text at the specified index and assign the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_char_at("text", 1);

//Or from the object

`variable` = "text".get_char_at(1);

//Or dry by positionals

variable::get_char_at(`variable`, "text", 1);

//Or dry by keywords

variable::get_char_at(variable=`variable`, text="text", index=1);
```

**Arguments:**

| **Name**   | **Type**         | **Description**       |
| ---------- | ---------------- | --------------------- |
| `variable` | Variable\[Text\] | Variable to assign    |
| `text`     | Text             | Text to get character |
| `index`    | Number           | Index                 |
<h3 id=set_variable_get_color_channels>
  <code>variable::get_color_channels</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Color Channels\
**Type:** An action that returns a value\
**Description:** Gets RGB/HSB/HSL color numeric values as a list.

**Usage example:** 
```ts
`variable` = variable::get_color_channels("color", "HSB");

//Or from the object

`variable` = "color".get_color_channels("HSB");

//Or dry by positionals

variable::get_color_channels(`variable`, "color", "HSB");

//Or dry by keywords

variable::get_color_channels(variable=`variable`, color="color", color_channels="HSB");
```

**Arguments:**

| **Name**         | **Type**                                                     | **Description**    |
| ---------------- | ------------------------------------------------------------ | ------------------ |
| `variable`       | Variable\[List\]                                             | Variable to assign |
| `color`          | Text                                                         | Color to get value |
| `color_channels` | Marker<br/>**HSB** - HSB<br/>**HSL** - HSL<br/>**RGB** - RGB | Color Channel      |
<h3 id=set_variable_get_compass_lodestone>
  <code>variable::get_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Lodestone Location\
**Type:** An action that returns a value\
**Description:** Get the location of lodestone from a magnetized compass and assign the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_compass_lodestone(item("stick"));

//Or from the object

`variable` = item("stick").get_compass_lodestone();

//Or dry by positionals

variable::get_compass_lodestone(`variable`, item("stick"));

//Or dry by keywords

variable::get_compass_lodestone(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**             | **Description**    |
| ---------- | -------------------- | ------------------ |
| `variable` | Variable\[Location\] | Variable to assign |
| `item`     | Item                 | Magnetized Compass |
<h3 id=set_variable_get_component_children>
  <code>variable::get_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Stylized Text Children Components\
**Type:** An action that returns a value\
**Description:** Gets children components of the Styled Text.

**Usage example:** 
```ts
`variable` = variable::get_component_children("component");

//Or from the object

`variable` = "component".get_component_children();

//Or dry by positionals

variable::get_component_children(`variable`, "component");

//Or dry by keywords

variable::get_component_children(variable=`variable`, component="component");
```

**Arguments:**

| **Name**    | **Type**         | **Description** |
| ----------- | ---------------- | --------------- |
| `variable`  | Variable\[List\] | Variable to set |
| `component` | Text             | Stylized text   |
<h3 id=set_variable_get_component_decorations>
  <code>variable::get_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Stylized Text Decorations\
**Type:** An action that returns a value\
**Description:** Gets the text decorations (bold, italics, underlined, strikethrough, obfuscated) of a Styled Text.

**Usage example:** 
```ts
`variable` = variable::get_component_decorations("component");

//Or from the object

`variable` = "component".get_component_decorations();

//Or dry by positionals

variable::get_component_decorations(`variable`, "component");

//Or dry by keywords

variable::get_component_decorations(variable=`variable`, component="component");
```

**Arguments:**

| **Name**    | **Type**         | **Description**    |
| ----------- | ---------------- | ------------------ |
| `variable`  | Variable\[List\] | Variable to assign |
| `component` | Text             | Stylized text      |
<h3 id=set_variable_get_component_hex_color>
  <code>variable::get_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Stylized Text Hex Color\
**Type:** An action that returns a value\
**Description:** Gets the color in hex of a Styled Text.

**Usage example:** 
```ts
`variable` = variable::get_component_hex_color("component");

//Or from the object

`variable` = "component".get_component_hex_color();

//Or dry by positionals

variable::get_component_hex_color(`variable`, "component");

//Or dry by keywords

variable::get_component_hex_color(variable=`variable`, component="component");
```

**Arguments:**

| **Name**    | **Type**         | **Description** |
| ----------- | ---------------- | --------------- |
| `variable`  | Variable\[Text\] | Variable to set |
| `component` | Text             | The Styled Text |
<h3 id=set_variable_get_component_parsing>
  <code>variable::get_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Type Stylized Text Parsing\
**Type:** An action that returns a value\
**Description:** Get the method of parsing for a Styled Text.

**Usage example:** 
```ts
`variable` = variable::get_component_parsing("component");

//Or from the object

`variable` = "component".get_component_parsing();

//Or dry by positionals

variable::get_component_parsing(`variable`, "component");

//Or dry by keywords

variable::get_component_parsing(variable=`variable`, component="component");
```

**Arguments:**

| **Name**    | **Type**         | **Description** |
| ----------- | ---------------- | --------------- |
| `variable`  | Variable\[Text\] | Variable to set |
| `component` | Text             | The styled text |
<h3 id=set_variable_get_container_contents>
  <code>variable::get_container_contents</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Container Contents\
**Type:** An action that returns a value\
**Description:** Sets a list of container contents at the selected location to a variable.

**Usage example:** 
```ts
`variable` = variable::get_container_contents(location(0,0,0,0,0), "FALSE");

//Or from the object

`variable` = location(0,0,0,0,0).get_container_contents("FALSE");

//Or dry by positionals

variable::get_container_contents(`variable`, location(0,0,0,0,0), "FALSE");

//Or dry by keywords

variable::get_container_contents(variable=`variable`, location=location(0,0,0,0,0), ignore_empty_slots="FALSE");
```

**Arguments:**

| **Name**             | **Type**                                                   | **Description**    |
| -------------------- | ---------------------------------------------------------- | ------------------ |
| `variable`           | Variable\[List\]                                           | Variable to assign |
| `location`           | Location                                                   | Container Location |
| `ignore_empty_slots` | Marker<br/>**FALSE** - Don\'t Ignore<br/>**TRUE** - Ignore | Ignore Empty Slots |
<h3 id=set_variable_get_container_lock>
  <code>variable::get_container_lock</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Container Key\
**Type:** An action that returns a value\
**Description:** Sets a container key item at the specified location to a variable.

**Usage example:** 
```ts
`variable` = variable::get_container_lock(location(0,0,0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).get_container_lock();

//Or dry by positionals

variable::get_container_lock(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_container_lock(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `location` | Location         | Block Location     |
<h3 id=set_variable_get_container_name>
  <code>variable::get_container_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Container Name\
**Type:** An action that returns a value\
**Description:** Sets the variable to the name of the container at the selected location.

**Usage example:** 
```ts
`variable` = variable::get_container_name(location(0,0,0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).get_container_name();

//Or dry by positionals

variable::get_container_name(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_container_name(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `location` | Location         | Container Location |
<h3 id=set_variable_get_coordinate>
  <code>variable::get_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Location Coordinate\
**Type:** An action that returns a value\
**Description:** Gets the value of the selected coordinate from the location and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_coordinate(location(0,0,0,0,0), "PITCH");

//Or from the object

`variable` = location(0,0,0,0,0).get_coordinate("PITCH");

//Or dry by positionals

variable::get_coordinate(`variable`, location(0,0,0,0,0), "PITCH");

//Or dry by keywords

variable::get_coordinate(variable=`variable`, location=location(0,0,0,0,0), type="PITCH");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                            | **Description**       |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `variable` | Variable\[Number\]                                                                                                                  | Variable to assign    |
| `location` | Location                                                                                                                            | Location to get value |
| `type`     | Marker<br/>**PITCH** - Horizontal Rotation<br/>**X** - X Axis<br/>**Y** - Y Axis<br/>**YAW** - Vertical rotation<br/>**Z** - Z Axis | Coordinate Type       |
<h3 id=set_variable_get_decorate_pot_sherd>
  <code>variable::get_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Decorate Pot Sherd\
**Type:** An action that returns a value\
**Description:** Gets the selected vase side shard material of the selected vase side at the specified location.

**Usage example:** 
```ts
`variable` = variable::get_decorate_pot_sherd(location(0,0,0,0,0), "BACK");

//Or from the object

`variable` = location(0,0,0,0,0).get_decorate_pot_sherd("BACK");

//Or dry by positionals

variable::get_decorate_pot_sherd(`variable`, location(0,0,0,0,0), "BACK");

//Or dry by keywords

variable::get_decorate_pot_sherd(variable=`variable`, location=location(0,0,0,0,0), side="BACK");
```

**Arguments:**

| **Name**   | **Type**                                                                                                       | **Description**        |
| ---------- | -------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `variable` | Variable\[Item\]                                                                                               | Variable to assign     |
| `location` | Location                                                                                                       | Decorated pot location |
| `side`     | Marker<br/>**BACK** - Back side<br/>**FRONT** - Front side<br/>**LEFT** - Left side<br/>**RIGHT** - Right side | Decorated pot side     |
<h3 id=set_variable_get_entity_types_by_tag>
  <code>variable::get_entity_types_by_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_entity_types_by_tag("namespace", "ID");

//Or dry by positionals

variable::get_entity_types_by_tag(`variable`, "namespace", "ID");

//Or dry by keywords

variable::get_entity_types_by_tag(variable=`variable`, namespace="namespace", result_type="ID");
```

**Arguments:**

| **Name**      | **Type**                                                | **Description** |
| ------------- | ------------------------------------------------------- | --------------- |
| `variable`    | Variable\[List\]                                        | None            |
| `namespace`   | Text                                                    | None            |
| `result_type` | Marker<br/>**ID** - None<br/>**TRANSLATION_KEY** - None | None            |
<h3 id=set_variable_get_index_of_subtext>
  <code>variable::get_index_of_subtext</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Subtext Index\
**Type:** An action that returns a value\
**Description:** Gets the subtext index from the text and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_index_of_subtext("text", "subtext", 1, "FIRST");

//Or from the object

`variable` = "text".get_index_of_subtext("subtext", 1, "FIRST");

//Or dry by positionals

variable::get_index_of_subtext(`variable`, "text", "subtext", 1, "FIRST");

//Or dry by keywords

variable::get_index_of_subtext(variable=`variable`, text="text", subtext="subtext", start_index=1, search_mode="FIRST");
```

**Arguments:**

| **Name**      | **Type**                                                                                     | **Description**    |
| ------------- | -------------------------------------------------------------------------------------------- | ------------------ |
| `variable`    | Variable\[Number\]                                                                           | Variable to assign |
| `text`        | Text                                                                                         | Text to get index  |
| `subtext`     | Text                                                                                         | Subtext            |
| `start_index` | Number                                                                                       | Starting Index     |
| `search_mode` | Marker<br/>**FIRST** - From Start (Get First Index)<br/>**LAST** - From End (Get Last Index) | Search Mode        |
<h3 id=set_variable_get_item_amount>
  <code>variable::get_item_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Amount\
**Type:** An action that returns a value\
**Description:** Sets the amount of items in a stack to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_amount(item("stick"));

//Or from the object

`variable` = item("stick").get_item_amount();

//Or dry by positionals

variable::get_item_amount(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_amount(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `item`     | Item               | Item               |
<h3 id=set_variable_get_item_attribute>
  <code>variable::get_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Attribute\
**Type:** An action that returns a value\
**Description:** Gets the specified attribute from an item as a \"UUID - Value\" dictionary and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_attribute(item("stick"), "name", "ARMOR", "ALL", "ADD_NUMBER");

//Or from the object

`variable` = item("stick").get_item_attribute("name", "ARMOR", "ALL", "ADD_NUMBER");

//Or dry by positionals

variable::get_item_attribute(`variable`, item("stick"), "name", "ARMOR", "ALL", "ADD_NUMBER");

//Or dry by keywords

variable::get_item_attribute(variable=`variable`, item=item("stick"), name="name", attribute="ARMOR", slot="ALL", operation="ADD_NUMBER");
```

**Arguments:**

| **Name**    | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Description**     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `variable`  | Variable\[Dictionary\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Variable to assign  |
| `item`      | Item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Item                |
| `name`      | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Attribute Name      |
| `attribute` | Marker<br/>**ARMOR** - Armor<br/>**ARMOR_TOUGHNESS** - Armor Toughness<br/>**ATTACK_DAMAGE** - Attack Damage<br/>**ATTACK_KNOCKBACK** - Attack Knockback<br/>**ATTACK_SPEED** - Attack Speed<br/>**FLYING_SPEED** - Flying Speed<br/>**FOLLOW_RANGE** - Follow Range<br/>**GENERIC_ARMOR** - Protection Points (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Defense Density Points (generic.armor_toughness)<br/>**GENERIC_ATTACK_DAMAGE** - Attack Damage (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Attack Knockback (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Attack Speed (generic.attack_speed)<br/>**GENERIC_BURNING_TIME** - Burning Time<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Explosion Knockback Resistance<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Fall Damage Multiplier<br/>**GENERIC_FLYING_SPEED** - Flying speed (generic.flying_speed)<br/>**GENERIC_FOLLOW_RANGE** - Follow Distance (generic.follow_range)<br/>**GENERIC_GRAVITY** - Gravity<br/>**GENERIC_JUMP_STRENGTH** - Jump Strength<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Knockback Resistance (generic.knockback_resistance)<br/>**GENERIC_LUCK** - Fishing Luck (generic.luck)<br/>**GENERIC_MAX_ABSORPTION** - Max absorption (generic.max_absorption)<br/>**GENERIC_MAX_HEALTH** - Maximum Health (generic.max_health)<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Movement Efficiency<br/>**GENERIC_MOVEMENT_SPEED** - Movement Speed (generic.movement_speed)<br/>**GENERIC_OXYGEN_BONUS** - Oxygen Bonus<br/>**GENERIC_SAFE_FALL_DISTANCE** - Safe Fall Distance<br/>**GENERIC_SCALE** - Scale<br/>**GENERIC_STEP_HEIGHT** - Step Height<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Water Movement Efficiency<br/>**HORSE_JUMP_STRENGTH** - Horse Jump Strength (horse.jump_strength)<br/>**KNOCKBACK_RESISTANCE** - Knockback Resistance<br/>**LUCK** - Luck<br/>**MAX_ABSORPTION** - Max Absorption<br/>**MAX_HEALTH** - Max Health<br/>**MOVEMENT_SPEED** - Movement Speed<br/>**PLAYER_BLOCK_BREAK_SPEED** - Block Breaking Speed<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - Block Interaction Range<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - Entity Interaction Range<br/>**PLAYER_MINING_EFFICIENCY** - Mining Efficiency<br/>**PLAYER_SNEAKING_SPEED** - Sneaking SPeed<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Submerged Mining Speed<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - Sweeping Damage Ratio<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Zombie reinforcements (zombie.spawn_reinforcements) | Attribute Type      |
| `slot`      | Marker<br/>**ALL** - All<br/>**ARMOR** - Armor<br/>**BODY** - Body (doesn\'t work with all entities)<br/>**BOOTS** - Boots<br/>**CHEST** - Chest<br/>**HAND** - Hand<br/>**HEAD** - Helmet<br/>**LEGGINGS** - Leggings<br/>**MAIN_HAND** - Main Hand<br/>**OFF_HAND** - Offhand                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Attribute Slot      |
| `operation` | Marker<br/>**ADD_NUMBER** - Amount<br/>**ADD_SCALAR** - Percentage<br/>**MULTIPLY_SCALAR_1** - Product (multiplicative)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Attribute Operation |
<h3 id=set_variable_get_item_break_sound>
  <code>variable::get_item_break_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_item_break_sound(item("stick"));

//Or from the object

`variable` = item("stick").get_item_break_sound();

//Or dry by positionals

variable::get_item_break_sound(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_break_sound(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Text\] | None            |
| `item`     | Item             | None            |
<h3 id=set_variable_get_item_color>
  <code>variable::get_item_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Color\
**Type:** An action that returns a value\
**Description:** Sets an item\'s color value to a variable.
**Work_with:**\
&nbsp;&nbsp;Leather Armor\
&nbsp;&nbsp;Potions\
&nbsp;&nbsp;Tipped Arrows\
&nbsp;&nbsp;Filled Maps

**Usage example:** 
```ts
`variable` = variable::get_item_color(item("stick"));

//Or from the object

`variable` = item("stick").get_item_color();

//Or dry by positionals

variable::get_item_color(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_color(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `item`     | Item             | Item               |
<h3 id=set_variable_get_item_component>
  <code>variable::get_item_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_item_component(item("stick"), "component");

//Or from the object

`variable` = item("stick").get_item_component("component");

//Or dry by positionals

variable::get_item_component(`variable`, item("stick"), "component");

//Or dry by keywords

variable::get_item_component(variable=`variable`, item=item("stick"), component="component");
```

**Arguments:**

| **Name**    | **Type**              | **Description** |
| ----------- | --------------------- | --------------- |
| `variable`  | Variable\[Any Value\] | None            |
| `item`      | Item                  | None            |
| `component` | Text                  | None            |
<h3 id=set_variable_get_item_custom_model_data>
  <code>variable::get_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Model Data\
**Type:** An action that returns a value\
**Description:** Gets the item\'s model data (CustomModelData) and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_custom_model_data(item("stick"));

//Or from the object

`variable` = item("stick").get_item_custom_model_data();

//Or dry by positionals

variable::get_item_custom_model_data(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_custom_model_data(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `item`     | Item               | Item               |
<h3 id=set_variable_get_item_custom_tag>
  <code>variable::get_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Custom Item Tag\
**Type:** An action that returns a value\
**Description:** Sets the item\'s custom tag value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_custom_tag(item("stick"), "tag_name", "any value");

//Or from the object

`variable` = item("stick").get_item_custom_tag("tag_name", "any value");

//Or dry by positionals

variable::get_item_custom_tag(`variable`, item("stick"), "tag_name", "any value");

//Or dry by keywords

variable::get_item_custom_tag(variable=`variable`, item=item("stick"), tag_name="tag_name", default_value="any value");
```

**Arguments:**

| **Name**        | **Type**              | **Description**    |
| --------------- | --------------------- | ------------------ |
| `variable`      | Variable\[Any Value\] | Variable to assign |
| `item`          | Item                  | Item               |
| `tag_name`      | Text                  | Tag Name           |
| `default_value` | Any Value             | Default Value      |
<h3 id=set_variable_get_item_custom_tags>
  <code>variable::get_item_custom_tags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Custom Item Tags\
**Type:** An action that returns a value\
**Description:** Sets a dictionary of custom item tags to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_custom_tags(item("stick"));

//Or from the object

`variable` = item("stick").get_item_custom_tags();

//Or dry by positionals

variable::get_item_custom_tags(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_custom_tags(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**               | **Description**    |
| ---------- | ---------------------- | ------------------ |
| `variable` | Variable\[Dictionary\] | Variable to assign |
| `item`     | Item                   | Item               |
<h3 id=set_variable_get_item_destroyable_blocks>
  <code>variable::get_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Destroyable Blocks\
**Type:** Action without value\
**Description:** Gets what blocks this item can break.

**Usage example:** 
```ts
variable::get_item_destroyable_blocks(`variable`, item("stick"));

//Or from the object

item("stick").get_item_destroyable_blocks(`variable`);

//Or dry by keywords

variable::get_item_destroyable_blocks(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `variable` | Variable | Variable to set |
| `item`     | Item     | Item            |
<h3 id=set_variable_get_item_durability>
  <code>variable::get_item_durability</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Durability\
**Type:** An action that returns a value\
**Description:** Sets the durability of the specified item to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_durability(item("stick"), "DAMAGE");

//Or from the object

`variable` = item("stick").get_item_durability("DAMAGE");

//Or dry by positionals

variable::get_item_durability(`variable`, item("stick"), "DAMAGE");

//Or dry by keywords

variable::get_item_durability(variable=`variable`, item=item("stick"), durability_type="DAMAGE");
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                                                                      | **Description**    |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`        | Variable\[Number\]                                                                                                                                                                                                                            | Variable to assign |
| `item`            | Item                                                                                                                                                                                                                                          | Item               |
| `durability_type` | Marker<br/>**DAMAGE** - Current Durability<br/>**DAMAGE_PERCENTAGE** - Current Durability Percentage<br/>**MAXIMUM** - Max Durability<br/>**REMAINING** - Remaining Durability<br/>**REMAINING_PERCENTAGE** - Remaining Durability Percentage | Durability Type    |
<h3 id=set_variable_get_item_effective_name>
  <code>variable::get_item_effective_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
`variable` = variable::get_item_effective_name(item("stick"));

//Or from the object

`variable` = item("stick").get_item_effective_name();

//Or dry by positionals

variable::get_item_effective_name(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_effective_name(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Text\] | None            |
| `item`     | Item             | None            |
<h3 id=set_variable_get_item_enchantments>
  <code>variable::get_item_enchantments</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Enchantments\
**Type:** An action that returns a value\
**Description:** Sets a dictionary of enchantments and their item levels to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_enchantments(item("stick"));

//Or from the object

`variable` = item("stick").get_item_enchantments();

//Or dry by positionals

variable::get_item_enchantments(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_enchantments(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**               | **Description**    |
| ---------- | ---------------------- | ------------------ |
| `variable` | Variable\[Dictionary\] | Variable to assign |
| `item`     | Item                   | Item               |
<h3 id=set_variable_get_item_food_properties>
  <code>variable::get_item_food_properties</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_item_food_properties(item("stick"), "");

//Or from the object

`variable` = item("stick").get_item_food_properties("");

//Or dry by positionals

variable::get_item_food_properties(`variable`, item("stick"), "");

//Or dry by keywords

variable::get_item_food_properties(variable=`variable`, item=item("stick"), property="");
```

**Arguments:**

| **Name**   | **Type**               | **Description** |
| ---------- | ---------------------- | --------------- |
| `variable` | Variable\[Number\]     | None            |
| `item`     | Item                   | None            |
| `property` | Marker<br/>**** - None | None            |
<h3 id=set_variable_get_item_lore>
  <code>variable::get_item_lore</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Description\
**Type:** An action that returns a value\
**Description:** Sets an item\'s description text to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_lore(item("stick"));

//Or from the object

`variable` = item("stick").get_item_lore();

//Or dry by positionals

variable::get_item_lore(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_lore(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[List\] | Variable to assign |
| `item`     | Item             | Item               |
<h3 id=set_variable_get_item_lore_line>
  <code>variable::get_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Description Line\
**Type:** An action that returns a value\
**Description:** Sets an item\'s description line to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_lore_line(item("stick"), 1);

//Or from the object

`variable` = item("stick").get_item_lore_line(1);

//Or dry by positionals

variable::get_item_lore_line(`variable`, item("stick"), 1);

//Or dry by keywords

variable::get_item_lore_line(variable=`variable`, item=item("stick"), line=1);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `item`     | Item             | Item               |
| `line`     | Number           | Line Number        |
<h3 id=set_variable_get_item_max_stack_size>
  <code>variable::get_item_max_stack_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Max Item Amount\
**Type:** An action that returns a value\
**Description:** Sets the maximum number of items in a stack to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_max_stack_size(item("stick"));

//Or from the object

`variable` = item("stick").get_item_max_stack_size();

//Or dry by positionals

variable::get_item_max_stack_size(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_max_stack_size(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `item`     | Item               | Item               |
<h3 id=set_variable_get_item_model_data>
  <code>variable::get_item_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_item_model_data(item("stick"));

//Or from the object

`variable` = item("stick").get_item_model_data();

//Or dry by positionals

variable::get_item_model_data(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_model_data(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Text\] | None            |
| `item`     | Item             | None            |
<h3 id=set_variable_get_item_name>
  <code>variable::get_item_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Name\
**Type:** An action that returns a value\
**Description:** Sets an item\'s display name to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_name(item("stick"));

//Or from the object

`variable` = item("stick").get_item_name();

//Or dry by positionals

variable::get_item_name(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_name(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `item`     | Item             | Item               |
<h3 id=set_variable_get_item_nbt_tags>
  <code>variable::get_item_nbt_tags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get NBT Item Tags\
**Type:** An action that returns a value\
**Description:** Sets the tags of the specified item to an NBT variable.

**Usage example:** 
```ts
`variable` = variable::get_item_nbt_tags(item("stick"), "ALL");

//Or from the object

`variable` = item("stick").get_item_nbt_tags("ALL");

//Or dry by positionals

variable::get_item_nbt_tags(`variable`, item("stick"), "ALL");

//Or dry by keywords

variable::get_item_nbt_tags(variable=`variable`, item=item("stick"), fetch_mode="ALL");
```

**Arguments:**

| **Name**     | **Type**                                                   | **Description**    |
| ------------ | ---------------------------------------------------------- | ------------------ |
| `variable`   | Variable\[Dictionary\]                                     | Variable to assign |
| `item`       | Item                                                       | Item               |
| `fetch_mode` | Marker<br/>**ALL** - All<br/>**CUSTOM_DATA** - Custom data | Get data           |
<h3 id=set_variable_get_item_placeable_blocks>
  <code>variable::get_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Placeable Blocks\
**Type:** Action without value\
**Description:** Gets what blocks this item is placeable against.

**Usage example:** 
```ts
variable::get_item_placeable_blocks(`variable`, item("stick"));

//Or from the object

item("stick").get_item_placeable_blocks(`variable`);

//Or dry by keywords

variable::get_item_placeable_blocks(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `variable` | Variable | Variable to set |
| `item`     | Item     | Item            |
<h3 id=set_variable_get_item_potion_effects>
  <code>variable::get_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Potion Effects From an Item\
**Type:** An action that returns a value\
**Description:** Get the potion effects from an item and assign the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_potion_effects(item("stick"));

//Or from the object

`variable` = item("stick").get_item_potion_effects();

//Or dry by positionals

variable::get_item_potion_effects(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_potion_effects(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[List\] | Variable to assign |
| `item`     | Item             | Item               |
<h3 id=set_variable_get_item_rarity>
  <code>variable::get_item_rarity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Rarity\
**Type:** An action that returns a value\
**Description:** Gets the rarity of an item and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_item_rarity(item("stick"));

//Or from the object

`variable` = item("stick").get_item_rarity();

//Or dry by positionals

variable::get_item_rarity(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_rarity(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `item`     | Item             | Item               |
<h3 id=set_variable_get_item_tooltip_style>
  <code>variable::get_item_tooltip_style</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_item_tooltip_style(item("stick"));

//Or from the object

`variable` = item("stick").get_item_tooltip_style();

//Or dry by positionals

variable::get_item_tooltip_style(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_tooltip_style(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Text\] | None            |
| `item`     | Item             | None            |
<h3 id=set_variable_get_item_type>
  <code>variable::get_item_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Type\
**Type:** An action that returns a value\
**Description:** Sets an item type to a variable, represented as text.

**Usage example:** 
```ts
`variable` = variable::get_item_type(item("stick"), "ID");

//Or from the object

`variable` = item("stick").get_item_type("ID");

//Or dry by positionals

variable::get_item_type(`variable`, item("stick"), "ID");

//Or dry by keywords

variable::get_item_type(variable=`variable`, type=item("stick"), value="ID");
```

**Arguments:**

| **Name**   | **Type**                                                                 | **Description**    |
| ---------- | ------------------------------------------------------------------------ | ------------------ |
| `variable` | Variable\[Text\]                                                         | Variable to assign |
| `type`     | Item                                                                     | Item               |
| `value`    | Marker<br/>**ID** - Item ID<br/>**ITEM** - Item<br/>**NAME** - Item Name | Text View          |
<h3 id=set_variable_get_item_use_remainder>
  <code>variable::get_item_use_remainder</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_item_use_remainder(item("stick"));

//Or from the object

`variable` = item("stick").get_item_use_remainder();

//Or dry by positionals

variable::get_item_use_remainder(`variable`, item("stick"));

//Or dry by keywords

variable::get_item_use_remainder(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Item\] | None            |
| `item`     | Item             | None            |
<h3 id=set_variable_get_item_weapon>
  <code>variable::get_item_weapon</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_item_weapon(item("stick"), "ITEM_DAMAGE_PER_ATTACK");

//Or from the object

`variable` = item("stick").get_item_weapon("ITEM_DAMAGE_PER_ATTACK");

//Or dry by positionals

variable::get_item_weapon(`variable`, item("stick"), "ITEM_DAMAGE_PER_ATTACK");

//Or dry by keywords

variable::get_item_weapon(variable=`variable`, item=item("stick"), property="ITEM_DAMAGE_PER_ATTACK");
```

**Arguments:**

| **Name**   | **Type**                                                                     | **Description** |
| ---------- | ---------------------------------------------------------------------------- | --------------- |
| `variable` | Variable\[Number\]                                                           | None            |
| `item`     | Item                                                                         | None            |
| `property` | Marker<br/>**ITEM_DAMAGE_PER_ATTACK** - None<br/>**DISABLE_BLOCKING** - None | None            |
<h3 id=set_variable_get_items_by_tag>
  <code>variable::get_items_by_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_items_by_tag("namespace", "ID");

//Or dry by positionals

variable::get_items_by_tag(`variable`, "namespace", "ID");

//Or dry by keywords

variable::get_items_by_tag(variable=`variable`, namespace="namespace", result_type="ID");
```

**Arguments:**

| **Name**      | **Type**                                                                    | **Description** |
| ------------- | --------------------------------------------------------------------------- | --------------- |
| `variable`    | Variable\[List\]                                                            | None            |
| `namespace`   | Text                                                                        | None            |
| `result_type` | Marker<br/>**ID** - None<br/>**TRANSLATION_KEY** - None<br/>**ITEM** - None | None            |
<h3 id=set_variable_get_lectern_book>
  <code>variable::get_lectern_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Lectern Book\
**Type:** An action that returns a value\
**Description:** Assigns the book from the lectern at the specified location to a variable.

**Usage example:** 
```ts
`variable` = variable::get_lectern_book(location(0,0,0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).get_lectern_book();

//Or dry by positionals

variable::get_lectern_book(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_lectern_book(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `location` | Location         | Block Location     |
<h3 id=set_variable_get_lectern_page>
  <code>variable::get_lectern_page</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Lectern Book Page\
**Type:** An action that returns a value\
**Description:** Sets a variable to the current page number of the book from the lectern at the specified location.

**Usage example:** 
```ts
`variable` = variable::get_lectern_page(location(0,0,0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).get_lectern_page();

//Or dry by positionals

variable::get_lectern_page(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_lectern_page(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `location` | Location           | Block Location     |
<h3 id=set_variable_get_light_level>
  <code>variable::get_light_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Light Level\
**Type:** An action that returns a value\
**Description:** Sets the value of the light level at the specified location to a variable.

**Usage example:** 
```ts
`variable` = variable::get_light_level(location(0,0,0,0,0), "BLOCKS");

//Or from the object

`variable` = location(0,0,0,0,0).get_light_level("BLOCKS");

//Or dry by positionals

variable::get_light_level(`variable`, location(0,0,0,0,0), "BLOCKS");

//Or dry by keywords

variable::get_light_level(variable=`variable`, location=location(0,0,0,0,0), value_type="BLOCKS");
```

**Arguments:**

| **Name**     | **Type**                                                                                         | **Description**       |
| ------------ | ------------------------------------------------------------------------------------------------ | --------------------- |
| `variable`   | Variable\[Number\]                                                                               | Variable to assign    |
| `location`   | Location                                                                                         | Location to get value |
| `value_type` | Marker<br/>**BLOCKS** - Block Light<br/>**SKY** - Light from the sky<br/>**TOTAL** - Total Light | Light Type            |
<h3 id=set_variable_get_list_index_of_value>
  <code>variable::get_list_index_of_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get List Value Index\
**Type:** An action that returns a value\
**Description:** Searchs for a value in a list and gets its index if found. Returns -1 on failure.

**Usage example:** 
```ts
`variable` = variable::get_list_index_of_value(`list`, "any value", "FIRST");

//Or from the object

`variable` = `list`.get_list_index_of_value("any value", "FIRST");

//Or dry by positionals

variable::get_list_index_of_value(`variable`, `list`, "any value", "FIRST");

//Or dry by keywords

variable::get_list_index_of_value(variable=`variable`, list=`list`, value="any value", search_mode="FIRST");
```

**Arguments:**

| **Name**      | **Type**                                                                                     | **Description**    |
| ------------- | -------------------------------------------------------------------------------------------- | ------------------ |
| `variable`    | Variable\[Number\]                                                                           | Variable to assign |
| `list`        | List                                                                                         | List               |
| `value`       | Any Value                                                                                    | Value              |
| `search_mode` | Marker<br/>**FIRST** - From Start (Get First Index)<br/>**LAST** - From End (Get Last Index) | Search Mode        |
<h3 id=set_variable_get_list_length>
  <code>variable::get_list_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get List Size\
**Type:** An action that returns a value\
**Description:** Gets the number of elements contained in the specified list.

**Usage example:** 
```ts
`variable` = variable::get_list_length(`list`);

//Or from the object

`variable` = `list`.get_list_length();

//Or dry by positionals

variable::get_list_length(`variable`, `list`);

//Or dry by keywords

variable::get_list_length(variable=`variable`, list=`list`);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `list`     | List               | List               |
<h3 id=set_variable_get_list_random_value>
  <code>variable::get_list_random_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Random List Value\
**Type:** An action that returns a value\
**Description:** Gets a random value from a list.

**Usage example:** 
```ts
`variable` = variable::get_list_random_value(`list`);

//Or from the object

`variable` = `list`.get_list_random_value();

//Or dry by positionals

variable::get_list_random_value(`variable`, `list`);

//Or dry by keywords

variable::get_list_random_value(variable=`variable`, list=`list`);
```

**Arguments:**

| **Name**   | **Type**              | **Description**    |
| ---------- | --------------------- | ------------------ |
| `variable` | Variable\[Any Value\] | Variable to assign |
| `list`     | List                  | List               |
<h3 id=set_variable_get_list_value>
  <code>variable::get_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get List Value\
**Type:** An action that returns a value\
**Description:** Get the value from the list at the specified index.

**Usage example:** 
```ts
`variable` = variable::get_list_value(`list`, 1, "any value");

//Or from the object

`variable` = `list`.get_list_value(1, "any value");

//Or dry by positionals

variable::get_list_value(`variable`, `list`, 1, "any value");

//Or dry by keywords

variable::get_list_value(variable=`variable`, list=`list`, number=1, default_value="any value");
```

**Arguments:**

| **Name**        | **Type**              | **Description**    |
| --------------- | --------------------- | ------------------ |
| `variable`      | Variable\[Any Value\] | Variable to assign |
| `list`          | List                  | List               |
| `number`        | Number                | Index              |
| `default_value` | Any Value             | Default value      |
<h3 id=set_variable_get_list_variables>
  <code>variable::get_list_variables</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Variable Names\
**Type:** An action that returns a value\
**Description:** Gets a list of all variable names and assigns the result to the variable.

**Usage example:** 
```ts
`variable` = variable::get_list_variables("GAME");

//Or dry by positionals

variable::get_list_variables(`variable`, "GAME");

//Or dry by keywords

variable::get_list_variables(variable=`variable`, scope="GAME");
```

**Arguments:**

| **Name**   | **Type**                                                              | **Description**    |
| ---------- | --------------------------------------------------------------------- | ------------------ |
| `variable` | Variable\[List\]                                                      | Variable to assign |
| `scope`    | Marker<br/>**GAME** - Game<br/>**LOCAL** - Local<br/>**SAVE** - Saved | Variable Type      |
<h3 id=set_variable_get_location_direction>
  <code>variable::get_location_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Location Direction\
**Type:** An action that returns a value\
**Description:** Assigns to a location direction variable.

**Usage example:** 
```ts
`variable` = variable::get_location_direction(location(0,0,0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).get_location_direction();

//Or dry by positionals

variable::get_location_direction(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_location_direction(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Vector\] | Variable to assign |
| `location` | Location           | Location to Get    |
<h3 id=set_variable_get_map_key_by_index>
  <code>variable::get_map_key_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Key By Index\
**Type:** An action that returns a value\
**Description:** Gets the key by the order it is inserted in.

**Usage example:** 
```ts
`variable` = variable::get_map_key_by_index(`map`, 1, "any value");

//Or from the object

`variable` = `map`.get_map_key_by_index(1, "any value");

//Or dry by positionals

variable::get_map_key_by_index(`variable`, `map`, 1, "any value");

//Or dry by keywords

variable::get_map_key_by_index(variable=`variable`, map=`map`, index=1, default_value="any value");
```

**Arguments:**

| **Name**        | **Type**              | **Description** |
| --------------- | --------------------- | --------------- |
| `variable`      | Variable\[Any Value\] | Variable to set |
| `map`           | Dictionary            | The dictionary  |
| `index`         | Number                | Index           |
| `default_value` | Any Value             | Default value   |
<h3 id=set_variable_get_map_keys>
  <code>variable::get_map_keys</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get List Of Dictionary Keys\
**Type:** An action that returns a value\
**Description:** Sets a list of dictionary keys to a variable.

**Usage example:** 
```ts
`variable` = variable::get_map_keys(`map`);

//Or from the object

`variable` = `map`.get_map_keys();

//Or dry by positionals

variable::get_map_keys(`variable`, `map`);

//Or dry by keywords

variable::get_map_keys(variable=`variable`, map=`map`);
```

**Arguments:**

| **Name**   | **Type**         | **Description**         |
| ---------- | ---------------- | ----------------------- |
| `variable` | Variable\[List\] | Variable to assign      |
| `map`      | Dictionary       | Dictionary to get value |
<h3 id=set_variable_get_map_keys_by_value>
  <code>variable::get_map_keys_by_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Keys By Value\
**Type:** An action that returns a value\
**Description:** Gets the key or list of dictionary keys by value and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_map_keys_by_value(`map`, "any value", "any value", "ALL");

//Or from the object

`variable` = `map`.get_map_keys_by_value("any value", "any value", "ALL");

//Or dry by positionals

variable::get_map_keys_by_value(`variable`, `map`, "any value", "any value", "ALL");

//Or dry by keywords

variable::get_map_keys_by_value(variable=`variable`, map=`map`, value="any value", default_value="any value", find_mode="ALL");
```

**Arguments:**

| **Name**        | **Type**                                                                                                                                 | **Description**    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`      | Variable\[List\]                                                                                                                         | Variable to assign |
| `map`           | Dictionary                                                                                                                               | Dictionary         |
| `value`         | Any Value                                                                                                                                | Value to get       |
| `default_value` | Any Value                                                                                                                                | Default value      |
| `find_mode`     | Marker<br/>**ALL** - All (gets all keys)<br/>**FIRST** - From Beginning (gets first key)<br/>**LAST** - From the end (gets the last key) | Find Mode          |
<h3 id=set_variable_get_map_size>
  <code>variable::get_map_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Size\
**Type:** An action that returns a value\
**Description:** Sets a dictionary size value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_map_size(`map`);

//Or from the object

`variable` = `map`.get_map_size();

//Or dry by positionals

variable::get_map_size(`variable`, `map`);

//Or dry by keywords

variable::get_map_size(variable=`variable`, map=`map`);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `map`      | Dictionary         | Dictionary         |
<h3 id=set_variable_get_map_value>
  <code>variable::get_map_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Value\
**Type:** An action that returns a value\
**Description:** Gets the specified dictionary value by key and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_map_value(`map`, "any value", "any value");

//Or from the object

`variable` = `map`.get_map_value("any value", "any value");

//Or dry by positionals

variable::get_map_value(`variable`, `map`, "any value", "any value");

//Or dry by keywords

variable::get_map_value(variable=`variable`, map=`map`, key="any value", default_value="any value");
```

**Arguments:**

| **Name**        | **Type**              | **Description**      |
| --------------- | --------------------- | -------------------- |
| `variable`      | Variable\[Any Value\] | Variable to assign   |
| `map`           | Dictionary            | Dictionary to change |
| `key`           | Any Value             | Key                  |
| `default_value` | Any Value             | Default Value        |
<h3 id=set_variable_get_map_value_by_index>
  <code>variable::get_map_value_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Value By Index\
**Type:** An action that returns a value\
**Description:** Gets the value by the order it is inserted in.

**Usage example:** 
```ts
`variable` = variable::get_map_value_by_index(`map`, 1, "any value");

//Or from the object

`variable` = `map`.get_map_value_by_index(1, "any value");

//Or dry by positionals

variable::get_map_value_by_index(`variable`, `map`, 1, "any value");

//Or dry by keywords

variable::get_map_value_by_index(variable=`variable`, map=`map`, index=1, default_value="any value");
```

**Arguments:**

| **Name**        | **Type**              | **Description** |
| --------------- | --------------------- | --------------- |
| `variable`      | Variable\[Any Value\] | Variable to set |
| `map`           | Dictionary            | The dictionary  |
| `index`         | Number                | Index           |
| `default_value` | Any Value             | Default value   |
<h3 id=set_variable_get_map_values>
  <code>variable::get_map_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get List Of Dictionary Values\
**Type:** An action that returns a value\
**Description:** Sets a list of dictionary values to a variable.

**Usage example:** 
```ts
`variable` = variable::get_map_values(`map`);

//Or from the object

`variable` = `map`.get_map_values();

//Or dry by positionals

variable::get_map_values(`variable`, `map`);

//Or dry by keywords

variable::get_map_values(variable=`variable`, map=`map`);
```

**Arguments:**

| **Name**   | **Type**         | **Description**         |
| ---------- | ---------------- | ----------------------- |
| `variable` | Variable\[List\] | Variable to assign      |
| `map`      | Dictionary       | Dictionary to get value |
<h3 id=set_variable_get_midpoint_between_vectors>
  <code>variable::get_midpoint_between_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Midpoint Between Vectors\
**Type:** An action that returns a value\
**Description:** Sets the midpoint between two vectors to a variable.

**Usage example:** 
```ts
`variable` = variable::get_midpoint_between_vectors(vector(0,0,0), vector(0,0,0));

//Or dry by positionals

variable::get_midpoint_between_vectors(`variable`, vector(0,0,0), vector(0,0,0));

//Or dry by keywords

variable::get_midpoint_between_vectors(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Vector\] | Variable to assign |
| `vector_1` | Vector             | First Vector       |
| `vector_2` | Vector             | Second Vector      |
<h3 id=set_variable_get_particle_amount>
  <code>variable::get_particle_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Amount\
**Type:** An action that returns a value\
**Description:** Sets a particle amount to a variable.

**Usage example:** 
```ts
`variable` = variable::get_particle_amount(particle("fire"));

//Or from the object

`variable` = particle("fire").get_particle_amount();

//Or dry by positionals

variable::get_particle_amount(`variable`, particle("fire"));

//Or dry by keywords

variable::get_particle_amount(variable=`variable`, particle=particle("fire"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**       |
| ---------- | ------------------ | --------------------- |
| `variable` | Variable\[Number\] | Variable to assign    |
| `particle` | Particle Effect    | Particle to get value |
<h3 id=set_variable_get_particle_color>
  <code>variable::get_particle_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Color\
**Type:** An action that returns a value\
**Description:** Sets a particle\'s color value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_particle_color(particle("fire"), "COLOR");

//Or from the object

`variable` = particle("fire").get_particle_color("COLOR");

//Or dry by positionals

variable::get_particle_color(`variable`, particle("fire"), "COLOR");

//Or dry by keywords

variable::get_particle_color(variable=`variable`, particle=particle("fire"), color_type="COLOR");
```

**Arguments:**

| **Name**     | **Type**                                                                | **Description**       |
| ------------ | ----------------------------------------------------------------------- | --------------------- |
| `variable`   | Variable\[Text\]                                                        | Variable to assign    |
| `particle`   | Particle Effect                                                         | Particle to get value |
| `color_type` | Marker<br/>**COLOR** - Normal color<br/>**TO_COLOR** - Transition color | Color type            |
<h3 id=set_variable_get_particle_material>
  <code>variable::get_particle_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Material\
**Type:** An action that returns a value\
**Description:** Sets a particle\'s material value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_particle_material(particle("fire"));

//Or from the object

`variable` = particle("fire").get_particle_material();

//Or dry by positionals

variable::get_particle_material(`variable`, particle("fire"));

//Or dry by keywords

variable::get_particle_material(variable=`variable`, particle=particle("fire"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**       |
| ---------- | ---------------- | --------------------- |
| `variable` | Variable\[Text\] | Variable to assign    |
| `particle` | Particle Effect  | Particle to get value |
<h3 id=set_variable_get_particle_offset>
  <code>variable::get_particle_offset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Motion\
**Type:** An action that returns a value\
**Description:** Sets a particle\'s movement value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_particle_offset(particle("fire"));

//Or from the object

`variable` = particle("fire").get_particle_offset();

//Or dry by positionals

variable::get_particle_offset(`variable`, particle("fire"));

//Or dry by keywords

variable::get_particle_offset(variable=`variable`, particle=particle("fire"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**       |
| ---------- | ------------------ | --------------------- |
| `variable` | Variable\[Vector\] | Variable to assign    |
| `particle` | Particle Effect    | Particle to get value |
<h3 id=set_variable_get_particle_size>
  <code>variable::get_particle_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Size\
**Type:** An action that returns a value\
**Description:** Sets a particle size value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_particle_size(particle("fire"));

//Or from the object

`variable` = particle("fire").get_particle_size();

//Or dry by positionals

variable::get_particle_size(`variable`, particle("fire"));

//Or dry by keywords

variable::get_particle_size(variable=`variable`, particle=particle("fire"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**       |
| ---------- | ------------------ | --------------------- |
| `variable` | Variable\[Number\] | Variable to assign    |
| `particle` | Particle Effect    | Particle to get value |
<h3 id=set_variable_get_particle_spread>
  <code>variable::get_particle_spread</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Spread\
**Type:** An action that returns a value\
**Description:** Sets a particle\'s spread value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_particle_spread(particle("fire"), "HORIZONTAL");

//Or from the object

`variable` = particle("fire").get_particle_spread("HORIZONTAL");

//Or dry by positionals

variable::get_particle_spread(`variable`, particle("fire"), "HORIZONTAL");

//Or dry by keywords

variable::get_particle_spread(variable=`variable`, particle=particle("fire"), type="HORIZONTAL");
```

**Arguments:**

| **Name**   | **Type**                                                           | **Description**       |
| ---------- | ------------------------------------------------------------------ | --------------------- |
| `variable` | Variable\[Number\]                                                 | Variable to assign    |
| `particle` | Particle Effect                                                    | Particle to get value |
| `type`     | Marker<br/>**HORIZONTAL** - Horizontal<br/>**VERTICAL** - Vertical | Spread Plane          |
<h3 id=set_variable_get_particle_type>
  <code>variable::get_particle_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Type\
**Type:** An action that returns a value\
**Description:** Sets a particle type to a variable.

**Usage example:** 
```ts
`variable` = variable::get_particle_type(particle("fire"));

//Or from the object

`variable` = particle("fire").get_particle_type();

//Or dry by positionals

variable::get_particle_type(`variable`, particle("fire"));

//Or dry by keywords

variable::get_particle_type(variable=`variable`, particle=particle("fire"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**       |
| ---------- | ---------------- | --------------------- |
| `variable` | Variable\[Text\] | Variable to assign    |
| `particle` | Particle Effect  | Particle to get value |
<h3 id=set_variable_get_player_head>
  <code>variable::get_player_head</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Player Head\
**Type:** An action that returns a value\
**Description:** Gets the player\'s head as an item and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_player_head("name_or_uuid", "NAME_OR_UUID");

//Or dry by positionals

variable::get_player_head(`variable`, "name_or_uuid", "NAME_OR_UUID");

//Or dry by keywords

variable::get_player_head(variable=`variable`, name_or_uuid="name_or_uuid", receive_type="NAME_OR_UUID");
```

**Arguments:**

| **Name**       | **Type**                                                                            | **Description**     |
| -------------- | ----------------------------------------------------------------------------------- | ------------------- |
| `variable`     | Variable\[Item\]                                                                    | Variable to assign  |
| `name_or_uuid` | Text                                                                                | Player name or UUID |
| `receive_type` | Marker<br/>**NAME_OR_UUID** - Player name or UUID<br/>**VALUE** - Value of the skin | Value type          |
<h3 id=set_variable_get_player_head_owner>
  <code>variable::get_player_head_owner</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Head Owner\
**Type:** An action that returns a value\
**Description:** Get the name or UUID of the owner of the item head and assign the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_player_head_owner(item("stick"), "NAME");

//Or from the object

`variable` = item("stick").get_player_head_owner("NAME");

//Or dry by positionals

variable::get_player_head_owner(`variable`, item("stick"), "NAME");

//Or dry by keywords

variable::get_player_head_owner(variable=`variable`, head=item("stick"), return_value="NAME");
```

**Arguments:**

| **Name**       | **Type**                                                                         | **Description**    |
| -------------- | -------------------------------------------------------------------------------- | ------------------ |
| `variable`     | Variable\[Text\]                                                                 | Variable to assign |
| `head`         | Item                                                                             | Player Head        |
| `return_value` | Marker<br/>**NAME** - Name<br/>**UUID** - UUID<br/>**VALUE** - Value of the skin | Return Value       |
<h3 id=set_variable_get_player_head_value>
  <code>variable::get_player_head_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Player Head At Location\
**Type:** An action that returns a value\
**Description:** Gets the skull owner at a location.

**Usage example:** 
```ts
`variable` = variable::get_player_head_value(location(0,0,0,0,0), "NAME");

//Or from the object

`variable` = location(0,0,0,0,0).get_player_head_value("NAME");

//Or dry by positionals

variable::get_player_head_value(`variable`, location(0,0,0,0,0), "NAME");

//Or dry by keywords

variable::get_player_head_value(variable=`variable`, location=location(0,0,0,0,0), return_value="NAME");
```

**Arguments:**

| **Name**       | **Type**                                                                  | **Description** |
| -------------- | ------------------------------------------------------------------------- | --------------- |
| `variable`     | Variable\[Text\]                                                          | Variable to set |
| `location`     | Location                                                                  | Skull location  |
| `return_value` | Marker<br/>**NAME** - Name<br/>**UUID** - UUID<br/>**VALUE** - Skin value | Return value    |
<h3 id=set_variable_get_potion_effect_amplifier>
  <code>variable::get_potion_effect_amplifier</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Potion Power\
**Type:** An action that returns a value\
**Description:** Sets a potion\'s power to a variable.

**Usage example:** 
```ts
`variable` = variable::get_potion_effect_amplifier(potion("slow_falling"));

//Or from the object

`variable` = potion("slow_falling").get_potion_effect_amplifier();

//Or dry by positionals

variable::get_potion_effect_amplifier(`variable`, potion("slow_falling"));

//Or dry by keywords

variable::get_potion_effect_amplifier(variable=`variable`, potion=potion("slow_falling"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `potion`   | Potion             | Potion             |
<h3 id=set_variable_get_potion_effect_duration>
  <code>variable::get_potion_effect_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Potion Duration\
**Type:** An action that returns a value\
**Description:** Sets the potion\'s duration to a variable.

**Usage example:** 
```ts
`variable` = variable::get_potion_effect_duration(potion("slow_falling"));

//Or from the object

`variable` = potion("slow_falling").get_potion_effect_duration();

//Or dry by positionals

variable::get_potion_effect_duration(`variable`, potion("slow_falling"));

//Or dry by keywords

variable::get_potion_effect_duration(variable=`variable`, potion=potion("slow_falling"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `potion`   | Potion             | Potion             |
<h3 id=set_variable_get_potion_effect_type>
  <code>variable::get_potion_effect_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Potion Effect\
**Type:** An action that returns a value\
**Description:** Sets a potion type to a variable.

**Usage example:** 
```ts
`variable` = variable::get_potion_effect_type(potion("slow_falling"));

//Or from the object

`variable` = potion("slow_falling").get_potion_effect_type();

//Or dry by positionals

variable::get_potion_effect_type(`variable`, potion("slow_falling"));

//Or dry by keywords

variable::get_potion_effect_type(variable=`variable`, potion=potion("slow_falling"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `potion`   | Potion           | Potion             |
<h3 id=set_variable_get_sculk_shrieker_warning_level>
  <code>variable::get_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sculk Shrieker Warning Level\
**Type:** An action that returns a value\
**Description:** Gets the warning levels of the Sculk Shrieker.

**Usage example:** 
```ts
`variable` = variable::get_sculk_shrieker_warning_level(location(0,0,0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).get_sculk_shrieker_warning_level();

//Or dry by positionals

variable::get_sculk_shrieker_warning_level(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_sculk_shrieker_warning_level(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description**         |
| ---------- | ------------------ | ----------------------- |
| `variable` | Variable\[Number\] | Variable to set         |
| `location` | Location           | Sculk Shrieker location |
<h3 id=set_variable_get_sign_text>
  <code>variable::get_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sign Line Text\
**Type:** An action that returns a value\
**Description:** Sets the text value of the sign line at the selected location to a variable.

**Usage example:** 
```ts
`variable` = variable::get_sign_text(location(0,0,0,0,0), "ALL", "ALL");

//Or from the object

`variable` = location(0,0,0,0,0).get_sign_text("ALL", "ALL");

//Or dry by positionals

variable::get_sign_text(`variable`, location(0,0,0,0,0), "ALL", "ALL");

//Or dry by keywords

variable::get_sign_text(variable=`variable`, location=location(0,0,0,0,0), check_side="ALL", sign_line="ALL");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                       | **Description**    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable\[Text\]                                                                                                                               | Variable to assign |
| `location`   | Location                                                                                                                                       | Sign Location      |
| `check_side` | Marker<br/>**ALL** - All<br/>**BACK** - Back<br/>**FRONT** - Front                                                                             | Sign Side          |
| `sign_line`  | Marker<br/>**ALL** - All lines<br/>**FIRST** - First Line<br/>**FOURTH** - Fourth line<br/>**SECOND** - Second Line<br/>**THIRD** - Third line | Line Number        |
<h3 id=set_variable_get_sound_pitch>
  <code>variable::get_sound_pitch</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Pitch\
**Type:** An action that returns a value\
**Description:** Sets the pitch of a sound to a variable.

**Usage example:** 
```ts
`variable` = variable::get_sound_pitch(sound("entity.zombie.hurt"));

//Or from the object

`variable` = sound("entity.zombie.hurt").get_sound_pitch();

//Or dry by positionals

variable::get_sound_pitch(`variable`, sound("entity.zombie.hurt"));

//Or dry by keywords

variable::get_sound_pitch(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `sound`    | Sound              | Sound to get value |
<h3 id=set_variable_get_sound_source>
  <code>variable::get_sound_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Source\
**Type:** An action that returns a value\
**Description:** Get the sound source and assign the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_sound_source(sound("entity.zombie.hurt"));

//Or from the object

`variable` = sound("entity.zombie.hurt").get_sound_source();

//Or dry by positionals

variable::get_sound_source(`variable`, sound("entity.zombie.hurt"));

//Or dry by keywords

variable::get_sound_source(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `sound`    | Sound            | Sound to get value |
<h3 id=set_variable_get_sound_type>
  <code>variable::get_sound_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Type\
**Type:** An action that returns a value\
**Description:** Sets a sound type value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_sound_type(sound("entity.zombie.hurt"));

//Or from the object

`variable` = sound("entity.zombie.hurt").get_sound_type();

//Or dry by positionals

variable::get_sound_type(`variable`, sound("entity.zombie.hurt"));

//Or dry by keywords

variable::get_sound_type(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `sound`    | Sound            | Sound to get value |
<h3 id=set_variable_get_sound_variation>
  <code>variable::get_sound_variation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Variation\
**Type:** An action that returns a value\
**Description:** Gets the sound variation and assigns the result to a variable.\
**Additional info:**\
&nbsp;&nbsp;Returns empty text if a random seed is used.

**Usage example:** 
```ts
`variable` = variable::get_sound_variation(sound("entity.zombie.hurt"));

//Or from the object

`variable` = sound("entity.zombie.hurt").get_sound_variation();

//Or dry by positionals

variable::get_sound_variation(`variable`, sound("entity.zombie.hurt"));

//Or dry by keywords

variable::get_sound_variation(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `sound`    | Sound            | Sound to get value |
<h3 id=set_variable_get_sound_variations>
  <code>variable::get_sound_variations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Variations\
**Type:** An action that returns a value\
**Description:** Gets a list of all sound variations and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_sound_variations(sound("entity.zombie.hurt"));

//Or from the object

`variable` = sound("entity.zombie.hurt").get_sound_variations();

//Or dry by positionals

variable::get_sound_variations(`variable`, sound("entity.zombie.hurt"));

//Or dry by keywords

variable::get_sound_variations(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**     |
| ---------- | ---------------- | ------------------- |
| `variable` | Variable\[List\] | Variable to assign  |
| `sound`    | Sound            | Sound to get values |
<h3 id=set_variable_get_sound_volume_action>
  <code>variable::get_sound_volume_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Volume\
**Type:** An action that returns a value\
**Description:** Sets a sound volume value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_sound_volume_action(sound("entity.zombie.hurt"));

//Or from the object

`variable` = sound("entity.zombie.hurt").get_sound_volume_action();

//Or dry by positionals

variable::get_sound_volume_action(`variable`, sound("entity.zombie.hurt"));

//Or dry by keywords

variable::get_sound_volume_action(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `sound`    | Sound              | Sound to get value |
<h3 id=set_variable_get_template_code>
  <code>variable::get_template_code</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Template Code\
**Type:** An action that returns a value\
**Description:** Assigns a template code to a variable.

**Usage example:** 
```ts
`variable` = variable::get_template_code(item("stick"), "MAP");

//Or from the object

`variable` = item("stick").get_template_code("MAP");

//Or dry by positionals

variable::get_template_code(`variable`, item("stick"), "MAP");

//Or dry by keywords

variable::get_template_code(variable=`variable`, template=item("stick"), return_type="MAP");
```

**Arguments:**

| **Name**      | **Type**                                                      | **Description**    |
| ------------- | ------------------------------------------------------------- | ------------------ |
| `variable`    | Variable\[Any Value\]                                         | Variable to assign |
| `template`    | Item                                                          | Template           |
| `return_type` | Marker<br/>**MAP** - JSON Dictionary<br/>**TEXT** - JSON Text | Return Value       |
<h3 id=set_variable_get_text_regex_groups>
  <code>variable::get_text_regex_groups</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_text_regex_groups("text", "regex", "group", "ALL", "INDEX", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE");

//Or from the object

`variable` = "text".get_text_regex_groups("regex", "group", "ALL", "INDEX", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE");

//Or dry by positionals

variable::get_text_regex_groups(`variable`, "text", "regex", "group", "ALL", "INDEX", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE");

//Or dry by keywords

variable::get_text_regex_groups(variable=`variable`, text="text", regex="regex", group="group", match_mode="ALL", get_group_by="INDEX", ignore_case="TRUE", multiline="TRUE", literal="TRUE", unix_lines="TRUE", comments="TRUE", dot_matches_all="TRUE", cannon_eq="TRUE");
```

**Arguments:**

| **Name**          | **Type**                                        | **Description** |
| ----------------- | ----------------------------------------------- | --------------- |
| `variable`        | Variable\[List\]                                | None            |
| `text`            | Text                                            | None            |
| `regex`           | Text                                            | None            |
| `group`           | Text                                            | None            |
| `match_mode`      | Marker<br/>**ALL** - None<br/>**FIRST** - None  | None            |
| `get_group_by`    | Marker<br/>**INDEX** - None<br/>**NAME** - None | None            |
| `ignore_case`     | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
| `multiline`       | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
| `literal`         | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
| `unix_lines`      | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
| `comments`        | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
| `dot_matches_all` | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
| `cannon_eq`       | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
<h3 id=set_variable_get_text_similarity>
  <code>variable::get_text_similarity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::get_text_similarity("text_1", "text_2", "SIMILARITY");

//Or from the object

`variable` = "text_1".get_text_similarity("text_2", "SIMILARITY");

//Or dry by positionals

variable::get_text_similarity(`variable`, "text_1", "text_2", "SIMILARITY");

//Or dry by keywords

variable::get_text_similarity(variable=`variable`, text_1="text_1", text_2="text_2", value_type="SIMILARITY");
```

**Arguments:**

| **Name**     | **Type**                                                             | **Description** |
| ------------ | -------------------------------------------------------------------- | --------------- |
| `variable`   | Variable\[Number\]                                                   | None            |
| `text_1`     | Text                                                                 | None            |
| `text_2`     | Text                                                                 | None            |
| `value_type` | Marker<br/>**SIMILARITY** - None<br/>**LEVENSHTEIN_DISTANCE** - None | None            |
<h3 id=set_variable_get_text_width>
  <code>variable::get_text_width</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Text Width In Pixels\
**Type:** An action that returns a value\
**Description:** Gets the size of each character in the text, sums them up, and assigns the result to a variable.\
**Additional info:**\
&nbsp;&nbsp;Values may not be relevant if using a resource pack with custom symbols.

**Usage example:** 
```ts
`variable` = variable::get_text_width("text");

//Or from the object

`variable` = "text".get_text_width();

//Or dry by positionals

variable::get_text_width(`variable`, "text");

//Or dry by keywords

variable::get_text_width(variable=`variable`, text="text");
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `text`     | Text               | Original Text      |
<h3 id=set_variable_get_vault_displayed_item>
  <code>variable::get_vault_displayed_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
`variable` = variable::get_vault_displayed_item(location(0,0,0,0,0));

//Or dry by positionals

variable::get_vault_displayed_item(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_vault_displayed_item(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Item\] | None            |
| `location` | Location         | None            |
<h3 id=set_variable_get_vault_next_state_update_time>
  <code>variable::get_vault_next_state_update_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None
**Work_with:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
`variable` = variable::get_vault_next_state_update_time(location(0,0,0,0,0));

//Or dry by positionals

variable::get_vault_next_state_update_time(`variable`, location(0,0,0,0,0));

//Or dry by keywords

variable::get_vault_next_state_update_time(variable=`variable`, location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description** |
| ---------- | ------------------ | --------------- |
| `variable` | Variable\[Number\] | None            |
| `location` | Location           | None            |
<h3 id=set_variable_get_vector_all_components>
  <code>variable::get_vector_all_components</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get All Vector Coordinates\
**Type:** An action that returns a value\
**Description:** Gets all coordinates of a vector and assigns the result to variables.

**Usage example:** 
```ts
`x`, `y`, `z` = variable::get_vector_all_components(vector(0,0,0));

//Or from the object

`x`, `y`, `z` = vector(0,0,0).get_vector_all_components();

//Or dry by positionals

variable::get_vector_all_components(`x`, `y`, `z`, vector(0,0,0));

//Or dry by keywords

variable::get_vector_all_components(x=`x`, y=`y`, z=`z`, vector=vector(0,0,0));
```

**Arguments:**

| **Name** | **Type**           | **Description**           |
| -------- | ------------------ | ------------------------- |
| `x`      | Variable\[Number\] | X location                |
| `y`      | Variable\[Number\] | Y location                |
| `z`      | Variable\[Number\] | Z location                |
| `vector` | Vector             | Vector to get values from |
<h3 id=set_variable_get_vector_between_locations>
  <code>variable::get_vector_between_locations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Vector Between Locations\
**Type:** An action that returns a value\
**Description:** Creates a vector between the start and end locations and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_vector_between_locations(location(0,0,0,0,0), location(0,0,0,0,0));

//Or dry by positionals

variable::get_vector_between_locations(`variable`, location(0,0,0,0,0), location(0,0,0,0,0));

//Or dry by keywords

variable::get_vector_between_locations(variable=`variable`, end_location=location(0,0,0,0,0), start_location=location(0,0,0,0,0));
```

**Arguments:**

| **Name**         | **Type**           | **Description**    |
| ---------------- | ------------------ | ------------------ |
| `variable`       | Variable\[Vector\] | Variable to assign |
| `end_location`   | Location           | Starting Location  |
| `start_location` | Location           | End Location       |
<h3 id=set_variable_get_vector_component>
  <code>variable::get_vector_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Vector Coordinate\
**Type:** An action that returns a value\
**Description:** Gets the specified vector coordinate and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::get_vector_component(vector(0,0,0), "X");

//Or from the object

`variable` = vector(0,0,0).get_vector_component("X");

//Or dry by positionals

variable::get_vector_component(`variable`, vector(0,0,0), "X");

//Or dry by keywords

variable::get_vector_component(variable=`variable`, vector=vector(0,0,0), vector_component="X");
```

**Arguments:**

| **Name**           | **Type**                                                                          | **Description**     |
| ------------------ | --------------------------------------------------------------------------------- | ------------------- |
| `variable`         | Variable\[Number\]                                                                | Variable to assign  |
| `vector`           | Vector                                                                            | Vector to get value |
| `vector_component` | Marker<br/>**X** - X Coordinate<br/>**Y** - Y Coordinate<br/>**Z** - Z Coordinate | Coordinate Type     |
<h3 id=set_variable_get_vector_from_block_face>
  <code>variable::get_vector_from_block_face</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Vector From Cardinal Direction\
**Type:** An action that returns a value\
**Description:** Generates a normalized vector based on the specified cardinal direction (\"south\", \"north\", \"east\", \"west\", \"up\", \" down\").

**Usage example:** 
```ts
`variable` = variable::get_vector_from_block_face("block_face");

//Or dry by positionals

variable::get_vector_from_block_face(`variable`, "block_face");

//Or dry by keywords

variable::get_vector_from_block_face(variable=`variable`, block_face="block_face");
```

**Arguments:**

| **Name**     | **Type**           | **Description**    |
| ------------ | ------------------ | ------------------ |
| `variable`   | Variable\[Vector\] | Variable to assign |
| `block_face` | Text               | Cardinal Direction |
<h3 id=set_variable_get_vector_length>
  <code>variable::get_vector_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Vector Length\
**Type:** An action that returns a value\
**Description:** Sets the length of a vector to a variable.

**Usage example:** 
```ts
`variable` = variable::get_vector_length(vector(0,0,0), "LENGTH");

//Or from the object

`variable` = vector(0,0,0).get_vector_length("LENGTH");

//Or dry by positionals

variable::get_vector_length(`variable`, vector(0,0,0), "LENGTH");

//Or dry by keywords

variable::get_vector_length(variable=`variable`, vector=vector(0,0,0), length_type="LENGTH");
```

**Arguments:**

| **Name**      | **Type**                                                                    | **Description**      |
| ------------- | --------------------------------------------------------------------------- | -------------------- |
| `variable`    | Variable\[Number\]                                                          | Variable to assign   |
| `vector`      | Vector                                                                      | Vector to get length |
| `length_type` | Marker<br/>**LENGTH** - Real Length<br/>**LENGTH_SQUARED** - Length Squared | Value Type           |
<h3 id=set_variable_hadamard_vector_product>
  <code>variable::hadamard_vector_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::hadamard_vector_product(vector(0,0,0), vector(0,0,0));

//Or from the object

`variable` = vector(0,0,0).hadamard_vector_product(vector(0,0,0));

//Or dry by positionals

variable::hadamard_vector_product(`variable`, vector(0,0,0), vector(0,0,0));

//Or dry by keywords

variable::hadamard_vector_product(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description** |
| ---------- | ------------------ | --------------- |
| `variable` | Variable\[Vector\] | None            |
| `vector_1` | Vector             | None            |
| `vector_2` | Vector             | None            |
<h3 id=set_variable_hash>
  <code>variable::get_text_hash</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Text Hash\
**Type:** An action that returns a value\
**Description:** Sets the text hash value to a variable.

**Usage example:** 
```ts
`variable` = variable::get_text_hash("text", "MD5");

//Or from the object

`variable` = "text".get_text_hash("MD5");

//Or dry by positionals

variable::get_text_hash(`variable`, "text", "MD5");

//Or dry by keywords

variable::get_text_hash(variable=`variable`, text="text", algorithm="MD5");
```

**Arguments:**

| **Name**    | **Type**                                                               | **Description**    |
| ----------- | ---------------------------------------------------------------------- | ------------------ |
| `variable`  | Variable\[Text\]                                                       | Variable to assign |
| `text`      | Text                                                                   | Original Text      |
| `algorithm` | Marker<br/>**MD5** - MD5<br/>**SHA1** - SHA-1<br/>**SHA256** - SHA-256 | Algorithm          |
<h3 id=set_variable_hide_item_components>
  <code>variable::hide_item_components</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::hide_item_components(item("stick"), ["components", "components"], "SET");

//Or from the object

`variable` = item("stick").hide_item_components(["components", "components"], "SET");

//Or dry by positionals

variable::hide_item_components(`variable`, item("stick"), ["components", "components"], "SET");

//Or dry by keywords

variable::hide_item_components(variable=`variable`, item=item("stick"), components=["components", "components"], mode="SET");
```

**Arguments:**

| **Name**     | **Type**                                                           | **Description** |
| ------------ | ------------------------------------------------------------------ | --------------- |
| `variable`   | Variable\[Item\]                                                   | None            |
| `item`       | Item                                                               | None            |
| `components` | list\[Text\]                                                       | None            |
| `mode`       | Marker<br/>**SET** - None<br/>**ADD** - None<br/>**REMOVE** - None | None            |
<h3 id=set_variable_increment>
  <code>variable::increment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Increment (+=)\
**Type:** Action without value\
**Description:** Adds the selected number to a variable.

**Usage example:** 
```ts
variable::increment(`variable`, 1);

//Or from the object

`variable`.increment(1);

//Or dry by keywords

variable::increment(variable=`variable`, number=1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `number`   | Number   | Number to add      |
<h3 id=set_variable_insert_list_value>
  <code>variable::insert_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Insert Value Into List\
**Type:** An action that returns a value\
**Description:** Inserts a value into the list at the specified index, shifting all values after it to the right.

**Usage example:** 
```ts
`variable` = variable::insert_list_value(`list`, 1, "any value");

//Or from the object

`variable` = `list`.insert_list_value(1, "any value");

//Or dry by positionals

variable::insert_list_value(`variable`, `list`, 1, "any value");

//Or dry by keywords

variable::insert_list_value(variable=`variable`, list=`list`, number=1, value="any value");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[List\] | Variable to assign |
| `list`     | List             | List               |
| `number`   | Number           | Index              |
| `value`    | Any Value        | Value              |
<h3 id=set_variable_join_text>
  <code>variable::join_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Join List To Text\
**Type:** An action that returns a value\
**Description:** Combines list items into a single text and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::join_text(`list`, "separator", "prefix", "postfix", 1, "truncated");

//Or from the object

`variable` = `list`.join_text("separator", "prefix", "postfix", 1, "truncated");

//Or dry by positionals

variable::join_text(`variable`, `list`, "separator", "prefix", "postfix", 1, "truncated");

//Or dry by keywords

variable::join_text(variable=`variable`, list=`list`, separator="separator", prefix="prefix", postfix="postfix", limit=1, truncated="truncated");
```

**Arguments:**

| **Name**    | **Type**         | **Description**                       |
| ----------- | ---------------- | ------------------------------------- |
| `variable`  | Variable\[Text\] | Variable to assign                    |
| `list`      | List             | List to Join                          |
| `separator` | Text             | Separator                             |
| `prefix`    | Text             | Prefix                                |
| `postfix`   | Text             | Postfix                               |
| `limit`     | Number           | Item Limit (if empty, all items)      |
| `truncated` | Text             | Text after limit (default is \"...\") |
<h3 id=set_variable_lerp_number>
  <code>variable::lerp_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Lerp Number\
**Type:** An action that returns a value\
**Description:** Calculates a number between two numbers with a certain factor and assigns the result to a variable. With a factor of 0, the first number will be returned, with 1 - the second, with 0.5 - the average value.

**Usage example:** 
```ts
`variable` = variable::lerp_number(1, 2, 3);

//Or from the object

`variable` = (3).lerp_number(1, 2);

//Or dry by positionals

variable::lerp_number(`variable`, 1, 2, 3);

//Or dry by keywords

variable::lerp_number(variable=`variable`, start=1, stop=2, amount=3);
```

**Arguments:**

| **Name**   | **Type**           | **Description**      |
| ---------- | ------------------ | -------------------- |
| `variable` | Variable\[Number\] | Variable to assign   |
| `start`    | Number             | First number         |
| `stop`     | Number             | Second number        |
| `amount`   | Number             | Factor (from 0 to 1) |
<h3 id=set_variable_location_relative>
  <code>variable::location_relative</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Relative Location\
**Type:** An action that returns a value\
**Description:** Sets the location relative to the side of the block at a certain distance, assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::location_relative(location(0,0,0,0,0), 1, "DOWN");

//Or from the object

`variable` = location(0,0,0,0,0).location_relative(1, "DOWN");

//Or dry by positionals

variable::location_relative(`variable`, location(0,0,0,0,0), 1, "DOWN");

//Or dry by keywords

variable::location_relative(variable=`variable`, location=location(0,0,0,0,0), distance=1, block_face="DOWN");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Description**    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable\[Location\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Variable to assign |
| `location`   | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Relative Location  |
| `distance`   | Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Distance           |
| `block_face` | Marker<br/>**DOWN** - Down<br/>**EAST** - East<br/>**EAST_NORTH_EAST** - East-North-East (east_north_east)<br/>**EAST_SOUTH_EAST** - East Southeast (east_south_east)<br/>**NORTH** - North<br/>**NORTH_EAST** - Northeast<br/>**NORTH_NORTH_EAST** - North-north-east (north_north_east)<br/>**NORTH_NORTH_WEST** - North-north-west (north_north_west)<br/>**NORTH_WEST** - Northwest<br/>**SELF** - Own (self)<br/>**SOUTH** - South<br/>**SOUTH_EAST** - Southeast<br/>**SOUTH_SOUTH_EAST** - South Southeast (south_south_east)<br/>**SOUTH_SOUTH_WEST** - South-South-West (south_south_west)<br/>**SOUTH_WEST** - Southwest<br/>**UP** - Up<br/>**WEST** - West<br/>**WEST_NORTH_WEST** - West-north-west (west_north_west)<br/>**WEST_SOUTH_WEST** - West-south-west (west_south_west) | Block Side         |
<h3 id=set_variable_locations_distance>
  <code>variable::locations_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Distance Between Locations\
**Type:** An action that returns a value\
**Description:** Gets the distance between locations and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::locations_distance(location(0,0,0,0,0), location(0,0,0,0,0), "ALTITUDE");

//Or dry by positionals

variable::locations_distance(`variable`, location(0,0,0,0,0), location(0,0,0,0,0), "ALTITUDE");

//Or dry by keywords

variable::locations_distance(variable=`variable`, location_1=location(0,0,0,0,0), location_2=location(0,0,0,0,0), type="ALTITUDE");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                 | **Description**    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable\[Number\]                                                                                                                       | Variable to assign |
| `location_1` | Location                                                                                                                                 | First Location     |
| `location_2` | Location                                                                                                                                 | Second Location    |
| `type`       | Marker<br/>**ALTITUDE** - Altitude<br/>**SQUARED_2D** - None<br/>**SQUARED_3D** - None<br/>**THREE_D** - Volume<br/>**TWO_D** - In Plane | Distance Type      |
<h3 id=set_variable_log>
  <code>variable::log</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Logarithm (log)\
**Type:** An action that returns a value\
**Description:** Sets a variable to the logarithm value with the selected argument and base.

**Usage example:** 
```ts
`variable` = variable::log(1, 2);

//Or from the object

`variable` = (1).log(2);

//Or dry by positionals

variable::log(`variable`, 1, 2);

//Or dry by keywords

variable::log(variable=`variable`, number=1, base=2);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `number`   | Number             | Log Argument       |
| `base`     | Number             | Log Base           |
<h3 id=set_variable_map_range>
  <code>variable::map_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set New Number Range\
**Type:** An action that returns a value\
**Description:** Converts a number from one range to another and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::map_range(1, 2, 3, 4, 5);

//Or from the object

`variable` = (1).map_range(2, 3, 4, 5);

//Or dry by positionals

variable::map_range(`variable`, 1, 2, 3, 4, 5);

//Or dry by keywords

variable::map_range(variable=`variable`, number=1, from_start=2, from_stop=3, to_start=4, to_stop=5);
```

**Arguments:**

| **Name**     | **Type**           | **Description**                    |
| ------------ | ------------------ | ---------------------------------- |
| `variable`   | Variable\[Number\] | Variable to assign                 |
| `number`     | Number             | Number to modify                   |
| `from_start` | Number             | Lowest limit of the initial range  |
| `from_stop`  | Number             | Highest limit of the initial range |
| `to_start`   | Number             | Lowest limit of the new range      |
| `to_stop`    | Number             | Highest limit of the new range     |
<h3 id=set_variable_mathematical_expectation>
  <code>variable::mathematical_expectation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::mathematical_expectation([1, 2], [3, 4]);

//Or dry by positionals

variable::mathematical_expectation(`variable`, [1, 2], [3, 4]);

//Or dry by keywords

variable::mathematical_expectation(variable=`variable`, values=[1, 2], probabilities=[3, 4]);
```

**Arguments:**

| **Name**        | **Type**           | **Description** |
| --------------- | ------------------ | --------------- |
| `variable`      | Variable\[Number\] | None            |
| `values`        | list\[Number\]     | None            |
| `probabilities` | list\[Number\]     | None            |
<h3 id=set_variable_max>
  <code>variable::max</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Maximum Value\
**Type:** An action that returns a value\
**Description:** Sets the largest number of the selected variable to a variable.

**Usage example:** 
```ts
`variable` = variable::max([1, 2]);

//Or dry by positionals

variable::max(`variable`, [1, 2]);

//Or dry by keywords

variable::max(variable=`variable`, value=[1, 2]);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `value`    | list\[Number\]     | Numbers to select  |
<h3 id=set_variable_median>
  <code>variable::median</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::median([1, 2]);

//Or dry by positionals

variable::median(`variable`, [1, 2]);

//Or dry by keywords

variable::median(variable=`variable`, value=[1, 2]);
```

**Arguments:**

| **Name**   | **Type**           | **Description** |
| ---------- | ------------------ | --------------- |
| `variable` | Variable\[Number\] | None            |
| `value`    | list\[Number\]     | None            |
<h3 id=set_variable_min>
  <code>variable::min</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Minimum Value\
**Type:** An action that returns a value\
**Description:** Sets the variable to the smallest number selected.

**Usage example:** 
```ts
`variable` = variable::min([1, 2]);

//Or dry by positionals

variable::min(`variable`, [1, 2]);

//Or dry by keywords

variable::min(variable=`variable`, value=[1, 2]);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `value`    | list\[Number\]     | Numbers to select  |
<h3 id=set_variable_multiple>
  <code>variable::set_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
variable::set_values([`variables`, `variables`], ["any value", "any value"]);

//Or dry by keywords

variable::set_values(variables=[`variables`, `variables`], values=["any value", "any value"]);
```

**Arguments:**

| **Name**    | **Type**          | **Description** |
| ----------- | ----------------- | --------------- |
| `variables` | list\[Variable\]  | None            |
| `values`    | list\[Any Value\] | None            |
<h3 id=set_variable_multiply>
  <code>variable::multiply</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Multiply (×)\
**Type:** An action that returns a value\
**Description:** Sets a multiplication of numbers to a variable.

**Usage example:** 
```ts
`variable` = variable::multiply([1, 2]);

//Or dry by positionals

variable::multiply(`variable`, [1, 2]);

//Or dry by keywords

variable::multiply(variable=`variable`, value=[1, 2]);
```

**Arguments:**

| **Name**   | **Type**           | **Description**     |
| ---------- | ------------------ | ------------------- |
| `variable` | Variable\[Number\] | Variable to assign  |
| `value`    | list\[Number\]     | Numbers to Multiply |
<h3 id=set_variable_multiply_vector>
  <code>variable::multiply_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Multiply Vector By Number\
**Type:** An action that returns a value\
**Description:** Sets the result of multiplying a vector by a number to a variable.

**Usage example:** 
```ts
`variable` = variable::multiply_vector(vector(0,0,0), 1);

//Or dry by positionals

variable::multiply_vector(`variable`, vector(0,0,0), 1);

//Or dry by keywords

variable::multiply_vector(variable=`variable`, vector=vector(0,0,0), multiplier=1);
```

**Arguments:**

| **Name**     | **Type**           | **Description**    |
| ------------ | ------------------ | ------------------ |
| `variable`   | Variable\[Vector\] | Variable to assign |
| `vector`     | Vector             | Vector to change   |
| `multiplier` | Number             | Number to Multiply |
<h3 id=set_variable_obtain_item_custom_model_data>
  <code>variable::obtain_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::obtain_item_custom_model_data(item("stick"), "FLOATS");

//Or from the object

`variable` = item("stick").obtain_item_custom_model_data("FLOATS");

//Or dry by positionals

variable::obtain_item_custom_model_data(`variable`, item("stick"), "FLOATS");

//Or dry by keywords

variable::obtain_item_custom_model_data(variable=`variable`, item=item("stick"), value_type="FLOATS");
```

**Arguments:**

| **Name**     | **Type**                                                                                          | **Description** |
| ------------ | ------------------------------------------------------------------------------------------------- | --------------- |
| `variable`   | Variable\[List\]                                                                                  | None            |
| `item`       | Item                                                                                              | None            |
| `value_type` | Marker<br/>**FLOATS** - None<br/>**BOOLEANS** - None<br/>**STRINGS** - None<br/>**COLORS** - None | None            |
<h3 id=set_variable_parse_json>
  <code>variable::parse_json</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Parse JSON\
**Type:** An action that returns a value\
**Description:** Parses JSON text into elements\: dictionaries (if the text is in curly braces) and lists (if the text is in square brackets) that can be manipulated to get the desired values.

**Usage example:** 
```ts
`variable` = variable::parse_json("json");

//Or dry by positionals

variable::parse_json(`variable`, "json");

//Or dry by keywords

variable::parse_json(variable=`variable`, json="json");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | For writing result |
| `json`     | Text             | JSON text          |
<h3 id=set_variable_parse_to_component>
  <code>variable::parse_to_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Parse To Stylized Text\
**Type:** An action that returns a value\
**Description:** Turns normal text into stylized text.

**Usage example:** 
```ts
`variable` = variable::parse_to_component("text", "JSON");

//Or from the object

`variable` = "text".parse_to_component("JSON");

//Or dry by positionals

variable::parse_to_component(`variable`, "text", "JSON");

//Or dry by keywords

variable::parse_to_component(variable=`variable`, text="text", parsing="JSON");
```

**Arguments:**

| **Name**   | **Type**                                                                                                      | **Description**    |
| ---------- | ------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable\[Text\]                                                                                              | Variable to assign |
| `text`     | Text                                                                                                          | Text to convert    |
| `parsing`  | Marker<br/>**JSON** - JSON<br/>**LEGACY** - Colored (&)<br/>**MINIMESSAGE** - Stylized<br/>**PLAIN** - Normal | Convertion type    |
<h3 id=set_variable_perlin_noise_3d>
  <code>variable::perlin_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Perlin Noise\
**Type:** An action that returns a value\
**Description:** Sets the perlin noise value at a specific location to a variable. Returns a number, with a value from -1 to 1.

**Usage example:** 
```ts
`variable` = variable::perlin_noise_3d(location(0,0,0,0,0), 1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Or dry by positionals

variable::perlin_noise_3d(`variable`, location(0,0,0,0,0), 1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Or dry by keywords

variable::perlin_noise_3d(variable=`variable`, location=location(0,0,0,0,0), seed=1, loc_frequency=2, octaves=3, frequency=4, amplitude=5, range_mode="FULL_RANGE", normalized="FALSE");
```

**Arguments:**

| **Name**        | **Type**                                                                              | **Description**            |
| --------------- | ------------------------------------------------------------------------------------- | -------------------------- |
| `variable`      | Variable\[Number\]                                                                    | Variable to assign         |
| `location`      | Location                                                                              | Location to set noise      |
| `seed`          | Number                                                                                | Noise Key                  |
| `loc_frequency` | Number                                                                                | Noise Frequency            |
| `octaves`       | Number                                                                                | Number of Noise Octaves    |
| `frequency`     | Number                                                                                | Frequency of Noise Octaves |
| `amplitude`     | Number                                                                                | Noise Octave Amplitude     |
| `range_mode`    | Marker<br/>**FULL_RANGE** - Full Range (-1 to 1 or more)<br/>**ZERO_TO_ONE** - 0 to 1 | Value Range                |
| `normalized`    | Marker<br/>**FALSE** - Don\'t Normalize<br/>**TRUE** - Normalize                      | Normalize Values           |
<h3 id=set_variable_pow>
  <code>variable::pow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Raise To Power (^)\
**Type:** An action that returns a value\
**Description:** Sets a variable to a power value with the selected base and exponent.

**Usage example:** 
```ts
`variable` = variable::pow(1, 2);

//Or from the object

`variable` = (1).pow(2);

//Or dry by positionals

variable::pow(`variable`, 1, 2);

//Or dry by keywords

variable::pow(variable=`variable`, base=1, power=2);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `base`     | Number             | Power base         |
| `power`    | Number             | Exponent           |
<h3 id=set_variable_purge>
  <code>variable::purge</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Variables\
**Type:** Action without value\
**Description:** Purges all variables matching the selected names.

**Usage example:** 
```ts
variable::purge(["names", "names"], "GAME", "ENDS_WITH", "FALSE");

//Or dry by keywords

variable::purge(names=["names", "names"], scope="GAME", match="ENDS_WITH", ignore_case="FALSE");
```

**Arguments:**

| **Name**      | **Type**                                                                                                                                                                     | **Description**  |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `names`       | list\[Text\]                                                                                                                                                                 | Names to Compare |
| `scope`       | Marker<br/>**GAME** - Game<br/>**LOCAL** - Local<br/>**SAVE** - Saved                                                                                                        | Variable Type    |
| `match`       | Marker<br/>**ENDS_WITH** - None<br/>**EQUALS** - Full Match<br/>**NAME_CONTAINS** - Name contains text<br/>**PART_CONTAINS** - Text contains name<br/>**STARTS_WITH** - None | Comparison Mode  |
| `ignore_case` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                                                                                                                       | Ignore case      |
<h3 id=set_variable_random>
  <code>variable::random</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Random Value\
**Type:** An action that returns a value\
**Description:** Sets a random value to a variable.

**Usage example:** 
```ts
`variable` = variable::random(["any value", "any value"]);

//Or dry by positionals

variable::random(`variable`, ["any value", "any value"]);

//Or dry by keywords

variable::random(variable=`variable`, values=["any value", "any value"]);
```

**Arguments:**

| **Name**   | **Type**              | **Description**    |
| ---------- | --------------------- | ------------------ |
| `variable` | Variable\[Any Value\] | Variable to assign |
| `values`   | list\[Any Value\]     | Values to choose   |
<h3 id=set_variable_random_location>
  <code>variable::random_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Random Location\
**Type:** An action that returns a value\
**Description:** Creates a random location in the region between two corners and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::random_location(location(0,0,0,0,0), location(0,0,0,0,0), "FALSE");

//Or dry by positionals

variable::random_location(`variable`, location(0,0,0,0,0), location(0,0,0,0,0), "FALSE");

//Or dry by keywords

variable::random_location(variable=`variable`, location_1=location(0,0,0,0,0), location_2=location(0,0,0,0,0), integer="FALSE");
```

**Arguments:**

| **Name**     | **Type**                                             | **Description**              |
| ------------ | ---------------------------------------------------- | ---------------------------- |
| `variable`   | Variable\[Location\]                                 | Variable to assign           |
| `location_1` | Location                                             | First corner of region       |
| `location_2` | Location                                             | Second Region Corner         |
| `integer`    | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Round to Integer Coordinates |
<h3 id=set_variable_random_number>
  <code>variable::random_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Random Number\
**Type:** An action that returns a value\
**Description:** Sets a variable to a random number within the selected range.

**Usage example:** 
```ts
`variable` = variable::random_number(1, 2, "FALSE");

//Or dry by positionals

variable::random_number(`variable`, 1, 2, "FALSE");

//Or dry by keywords

variable::random_number(variable=`variable`, min=1, max=2, integer="FALSE");
```

**Arguments:**

| **Name**   | **Type**                                                 | **Description**    |
| ---------- | -------------------------------------------------------- | ------------------ |
| `variable` | Variable\[Number\]                                       | Variable to assign |
| `min`      | Number                                                   | Minimum Value      |
| `max`      | Number                                                   | Max Value          |
| `integer`  | Marker<br/>**FALSE** - Fractional<br/>**TRUE** - Integer | Number Type        |
<h3 id=set_variable_randomize_list_order>
  <code>variable::randomize_list_order</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Randomize List\
**Type:** An action that returns a value\
**Description:** Sets the order of items randomly.

**Usage example:** 
```ts
`variable` = variable::randomize_list_order(`list`);

//Or from the object

`variable` = `list`.randomize_list_order();

//Or dry by positionals

variable::randomize_list_order(`variable`, `list`);

//Or dry by keywords

variable::randomize_list_order(variable=`variable`, list=`list`);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[List\] | Variable to assign |
| `list`     | List             | List               |
<h3 id=set_variable_ray_trace_result>
  <code>variable::ray_trace_result</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Raycast Result\
**Type:** An action that returns a value\
**Description:** Launches a ray with the given parameters. When the ray collides with the specified objects (entity or block), you can get the location of the ray, the location and side of the block, the UUID of the entity, and the side of the hitbox. Beamwidth only works on entities (increases or decreases creature hitboxes).

**Usage example:** 
```ts
`variable_for_hit_location`, `variable_for_hit_block_location`, `variable_for_hit_block_face`, `variable_for_hit_entity_uuid` = variable::ray_trace_result(location(0,0,0,0,0), 1, 2, `entities`, "BLOCKS_AND_ENTITIES", "FALSE", "ALWAYS");

//Or dry by positionals

variable::ray_trace_result(`variable_for_hit_location`, `variable_for_hit_block_location`, `variable_for_hit_block_face`, `variable_for_hit_entity_uuid`, location(0,0,0,0,0), 1, 2, `entities`, "BLOCKS_AND_ENTITIES", "FALSE", "ALWAYS");

//Or dry by keywords

variable::ray_trace_result(variable_for_hit_location=`variable_for_hit_location`, variable_for_hit_block_location=`variable_for_hit_block_location`, variable_for_hit_block_face=`variable_for_hit_block_face`, variable_for_hit_entity_uuid=`variable_for_hit_entity_uuid`, start=location(0,0,0,0,0), ray_size=1, max_distance=2, entities=`entities`, ray_collision_mode="BLOCKS_AND_ENTITIES", ignore_passable_blocks="FALSE", fluid_collision_mode="ALWAYS");
```

**Arguments:**

| **Name**                          | **Type**                                                                                                                                   | **Description**                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `variable_for_hit_location`       | Variable\[Location\]                                                                                                                       | Ray Impact Point                                                                     |
| `variable_for_hit_block_location` | Variable\[Location\]                                                                                                                       | Block Location                                                                       |
| `variable_for_hit_block_face`     | Variable\[Text\]                                                                                                                           | Block/Hitbox Side                                                                    |
| `variable_for_hit_entity_uuid`    | Variable\[List\]                                                                                                                           | Entity UUID                                                                          |
| `start`                           | Location                                                                                                                                   | Beam Start                                                                           |
| `ray_size`                        | Number                                                                                                                                     | Beam Width                                                                           |
| `max_distance`                    | Number                                                                                                                                     | Beam length                                                                          |
| `entities`                        | List                                                                                                                                       | Names or UUIDs of the entities to collide with (default is all players and entities) |
| `ray_collision_mode`              | Marker<br/>**BLOCKS_AND_ENTITIES** - With blocks and entities<br/>**ONLY_BLOCKS** - Only with Blocks<br/>**ONLY_ENTITIES** - Entities Only | Object Collision                                                                     |
| `ignore_passable_blocks`          | Marker<br/>**FALSE** - Don\'t Ignore<br/>**TRUE** - Ignore                                                                                 | Ignore Passable Blocks                                                               |
| `fluid_collision_mode`            | Marker<br/>**ALWAYS** - Don\'t Ignore<br/>**NEVER** - Ignore Completely<br/>**SOURCE_ONLY** - Consider Fluid Source Only                   | Ignore Fluid                                                                         |
<h3 id=set_variable_reflect_vector_product>
  <code>variable::reflect_vector_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reflect Vector By Second Vector\
**Type:** An action that returns a value\
**Description:** Reflects a vector relative to another vector and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::reflect_vector_product(vector(0,0,0), vector(0,0,0), 1);

//Or dry by positionals

variable::reflect_vector_product(`variable`, vector(0,0,0), vector(0,0,0), 1);

//Or dry by keywords

variable::reflect_vector_product(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0), bounce=1);
```

**Arguments:**

| **Name**   | **Type**           | **Description**                                            |
| ---------- | ------------------ | ---------------------------------------------------------- |
| `variable` | Variable\[Vector\] | Variable to assign                                         |
| `vector_1` | Vector             | Source Vector                                              |
| `vector_2` | Vector             | Reflection Surface Vector                                  |
| `bounce`   | Number             | Multiply the resulting vector by this number (default 1.0) |
<h3 id=set_variable_regex_replace_text>
  <code>variable::regex_replace_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Match With Regular Expression\
**Type:** An action that returns a value\
**Description:** Replaces text matching the specified regular expression and assigns the result to a variable. The \"Replacement\" argument can contain $\<group name\> to refer to the group. Include only the flags you need!

**Usage example:** 
```ts
`variable` = variable::regex_replace_text("text", "regex", "replacement", "ANY", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Or from the object

`variable` = "text".regex_replace_text("regex", "replacement", "ANY", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Or dry by positionals

variable::regex_replace_text(`variable`, "text", "regex", "replacement", "ANY", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Or dry by keywords

variable::regex_replace_text(variable=`variable`, text="text", regex="regex", replacement="replacement", first="ANY", ignore_case="FALSE", multiline="FALSE", literal="FALSE", unix_lines="FALSE", comments="FALSE", dot_matches_all="FALSE", cannon_eq="FALSE");
```

**Arguments:**

| **Name**          | **Type**                                                                          | **Description**                                  |
| ----------------- | --------------------------------------------------------------------------------- | ------------------------------------------------ |
| `variable`        | Variable\[Text\]                                                                  | Variable to assign                               |
| `text`            | Text                                                                              | Original Text                                    |
| `regex`           | Text                                                                              | Regular Expression                               |
| `replacement`     | Text                                                                              | Replacement                                      |
| `first`           | Marker<br/>**ANY** - Replace All Matches<br/>**FIRST** - Replace First Match Only | Number of replacements                           |
| `ignore_case`     | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                            | Ignore case (ignore_case flag)                   |
| `multiline`       | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                            | Multiline Mode (multiline flag)                  |
| `literal`         | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                            | Treat template verbatim (literal flag)           |
| `unix_lines`      | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                            | UNIX line mode (unix_lines flag)                 |
| `comments`        | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                            | Allow comments and ignore spaces (comments flag) |
| `dot_matches_all` | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                            | Dotall Mode (dotall flag)                        |
| `cannon_eq`       | Marker<br/>**FALSE** - Disabled<br/>**TRUE** - Enabled                            | Canonical Equivalence (cannon_eq Flag)           |
<h3 id=set_variable_remainder>
  <code>variable::remainder</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remainder (%)\
**Type:** An action that returns a value\
**Description:** Sets the remainder of the division of two numbers to a variable.

**Usage example:** 
```ts
`variable` = variable::remainder(1, 2, "MODULO");

//Or from the object

`variable` = (1).remainder(2, "MODULO");

//Or dry by positionals

variable::remainder(`variable`, 1, 2, "MODULO");

//Or dry by keywords

variable::remainder(variable=`variable`, dividend=1, divisor=2, remainder_mode="MODULO");
```

**Arguments:**

| **Name**         | **Type**                                                                                                                        | **Description**    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`       | Variable\[Number\]                                                                                                              | Variable to Assign |
| `dividend`       | Number                                                                                                                          | Dividend           |
| `divisor`        | Number                                                                                                                          | Divisor            |
| `remainder_mode` | Marker<br/>**MODULO** - Modulo Remainder (leaves divisor sign)<br/>**REMAINDER** - Remainder of division (leaves dividend sign) | Operation Mode     |
<h3 id=set_variable_remove_compass_lodestone>
  <code>variable::remove_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Lodestone Location\
**Type:** An action that returns a value\
**Description:** Removes a magnetite location from a magnetized compass and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::remove_compass_lodestone(item("stick"));

//Or from the object

`variable` = item("stick").remove_compass_lodestone();

//Or dry by positionals

variable::remove_compass_lodestone(`variable`, item("stick"));

//Or dry by keywords

variable::remove_compass_lodestone(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to Assign |
| `item`     | Item             | Magnetized Compass |
<h3 id=set_variable_remove_enchantment>
  <code>variable::remove_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Item Enchantment\
**Type:** An action that returns a value\
**Description:** Removes an enchantment from an item and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::remove_enchantment(item("stick"), "enchantment");

//Or from the object

`variable` = item("stick").remove_enchantment("enchantment");

//Or dry by positionals

variable::remove_enchantment(`variable`, item("stick"), "enchantment");

//Or dry by keywords

variable::remove_enchantment(variable=`variable`, item=item("stick"), enchantment="enchantment");
```

**Arguments:**

| **Name**      | **Type**         | **Description**    |
| ------------- | ---------------- | ------------------ |
| `variable`    | Variable\[Item\] | Variable to Assign |
| `item`        | Item             | Item               |
| `enchantment` | Text             | Enchant ID         |
<h3 id=set_variable_remove_item_attribute>
  <code>variable::remove_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Item Attribute\
**Type:** Action without value\
**Description:** Remove an attribute from the item.

**Usage example:** 
```ts
variable::remove_item_attribute(`variable`, item("stick"), "name_or_uuid", "ARMOR");

//Or from the object

item("stick").remove_item_attribute(`variable`, "name_or_uuid", "ARMOR");

//Or dry by keywords

variable::remove_item_attribute(variable=`variable`, item=item("stick"), name_or_uuid="name_or_uuid", attribute="ARMOR");
```

**Arguments:**

| **Name**       | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Description** |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `variable`     | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Variable to set |
| `item`         | Item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Item            |
| `name_or_uuid` | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Name or UUID    |
| `attribute`    | Marker<br/>**ARMOR** - Armor<br/>**ARMOR_TOUGHNESS** - Armor Toughness<br/>**ATTACK_DAMAGE** - Attack Damage<br/>**ATTACK_KNOCKBACK** - Attack Knockback<br/>**ATTACK_SPEED** - Attack Speed<br/>**FLYING_SPEED** - Flying Speed<br/>**FOLLOW_RANGE** - Follow Range<br/>**GENERIC_ARMOR** - Armor (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Armor Toughness (generic.armor_toughness)<br/>**GENERIC_ATTACK_DAMAGE** - Attack Damage (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Attack Knockback (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Attack Speed (generic.attack_speed)<br/>**GENERIC_BURNING_TIME** - Burning TIme<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Explosion Knockback Resistance<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Fall Damage Multiplier<br/>**GENERIC_FLYING_SPEED** - Flying Speed (generic.flying_speed)<br/>**GENERIC_FOLLOW_RANGE** - Follow Range (generic.follow_range)<br/>**GENERIC_GRAVITY** - Gravity<br/>**GENERIC_JUMP_STRENGTH** - Jump Strength<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Knockback Resistance (generic.knockback_resistance)<br/>**GENERIC_LUCK** - Luck (generic.luck)<br/>**GENERIC_MAX_ABSORPTION** - Max absorption (generic.max_absorption)<br/>**GENERIC_MAX_HEALTH** - Max Health (generic.max_health)<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Movement Efficiency<br/>**GENERIC_MOVEMENT_SPEED** - Movement Speed (generic.movement_speed)<br/>**GENERIC_OXYGEN_BONUS** - Oxygen Bonus<br/>**GENERIC_SAFE_FALL_DISTANCE** - Safe Fall Distance<br/>**GENERIC_SCALE** - Scale<br/>**GENERIC_STEP_HEIGHT** - Step Height<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Water Movement Efficiency<br/>**HORSE_JUMP_STRENGTH** - Horse Jump Strength (horse.jump_strength)<br/>**KNOCKBACK_RESISTANCE** - Knockback Resistance<br/>**LUCK** - Luck<br/>**MAX_ABSORPTION** - Max Absorption<br/>**MAX_HEALTH** - Max Health<br/>**MOVEMENT_SPEED** - Movement Speed<br/>**PLAYER_BLOCK_BREAK_SPEED** - Block Breaking Speed<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - Block Interaction Range<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - Entity Interaction Range<br/>**PLAYER_MINING_EFFICIENCY** - Mining Efficiency<br/>**PLAYER_SNEAKING_SPEED** - Sneaking Speed<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Submerged Mining Speed<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - Sweeping Damage Ratio<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Zomie spawn reinforcements (zombie.spawn_reinforcements) | Attribute       |
<h3 id=set_variable_remove_item_custom_model_data>
  <code>variable::remove_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Item Model Data\
**Type:** An action that returns a value\
**Description:** Removes item model data (CustomModelData) and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::remove_item_custom_model_data(item("stick"));

//Or from the object

`variable` = item("stick").remove_item_custom_model_data();

//Or dry by positionals

variable::remove_item_custom_model_data(`variable`, item("stick"));

//Or dry by keywords

variable::remove_item_custom_model_data(variable=`variable`, item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Item\] | Variable to set |
| `item`     | Item             | Item            |
<h3 id=set_variable_remove_item_custom_tag>
  <code>variable::remove_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Custom Item Tag\
**Type:** An action that returns a value\
**Description:** Removes a custom item tag and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::remove_item_custom_tag(item("stick"), "tag_name");

//Or from the object

`variable` = item("stick").remove_item_custom_tag("tag_name");

//Or dry by positionals

variable::remove_item_custom_tag(`variable`, item("stick"), "tag_name");

//Or dry by keywords

variable::remove_item_custom_tag(variable=`variable`, item=item("stick"), tag_name="tag_name");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `item`     | Item             | Item               |
| `tag_name` | Text             | Tag Name           |
<h3 id=set_variable_remove_item_lore_line>
  <code>variable::remove_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Item Description Line\
**Type:** An action that returns a value\
**Description:** Removes an item\'s description line and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::remove_item_lore_line(item("stick"), 1);

//Or from the object

`variable` = item("stick").remove_item_lore_line(1);

//Or dry by positionals

variable::remove_item_lore_line(`variable`, item("stick"), 1);

//Or dry by keywords

variable::remove_item_lore_line(variable=`variable`, item=item("stick"), line=1);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `item`     | Item             | Item               |
| `line`     | Number           | Line Number        |
<h3 id=set_variable_remove_item_potion_effects>
  <code>variable::remove_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Potion Effects From an Item\
**Type:** An action that returns a value\
**Description:** Removes potion effects from an item and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::remove_item_potion_effects([potion("slow_falling"), potion("slow_falling")], item("stick"));

//Or from the object

`variable` = item("stick").remove_item_potion_effects([potion("slow_falling"), potion("slow_falling")]);

//Or dry by positionals

variable::remove_item_potion_effects(`variable`, [potion("slow_falling"), potion("slow_falling")], item("stick"));

//Or dry by keywords

variable::remove_item_potion_effects(variable=`variable`, effects=[potion("slow_falling"), potion("slow_falling")], item=item("stick"));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `effects`  | list\[Potion\]   | Potion Effects     |
| `item`     | Item             | Item               |
<h3 id=set_variable_remove_list_duplicates>
  <code>variable::remove_list_duplicates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Duplicate Values\
**Type:** An action that returns a value\
**Description:** Removes all values that appear more than once in the list.

**Usage example:** 
```ts
`variable` = variable::remove_list_duplicates(`list`);

//Or from the object

`variable` = `list`.remove_list_duplicates();

//Or dry by positionals

variable::remove_list_duplicates(`variable`, `list`);

//Or dry by keywords

variable::remove_list_duplicates(variable=`variable`, list=`list`);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[List\] | Variable to Assign |
| `list`     | List             | List               |
<h3 id=set_variable_remove_list_value>
  <code>variable::remove_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Value From List\
**Type:** An action that returns a value\
**Description:** Removes the specified value from the list.

**Usage example:** 
```ts
`variable` = variable::remove_list_value(`list`, "any value", "ALL");

//Or from the object

`variable` = `list`.remove_list_value("any value", "ALL");

//Or dry by positionals

variable::remove_list_value(`variable`, `list`, "any value", "ALL");

//Or dry by keywords

variable::remove_list_value(variable=`variable`, list=`list`, value="any value", remove_mode="ALL");
```

**Arguments:**

| **Name**      | **Type**                                                           | **Description**    |
| ------------- | ------------------------------------------------------------------ | ------------------ |
| `variable`    | Variable\[List\]                                                   | Variable to Assign |
| `list`        | List                                                               | List               |
| `value`       | Any Value                                                          | Value              |
| `remove_mode` | Marker<br/>**ALL** - All<br/>**FIRST** - First<br/>**LAST** - Last | Remove mode        |
<h3 id=set_variable_remove_list_value_at_index>
  <code>variable::remove_list_value_at_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Value From List By Index\
**Type:** An action that returns a value\
**Description:** Removes the value at the specified index from the list.

**Usage example:** 
```ts
`variable`, `removed_value` = variable::remove_list_value_at_index(`list`, 1);

//Or from the object

`variable`, `removed_value` = `list`.remove_list_value_at_index(1);

//Or dry by positionals

variable::remove_list_value_at_index(`removed_value`, `variable`, `list`, 1);

//Or dry by keywords

variable::remove_list_value_at_index(removed_value=`removed_value`, variable=`variable`, list=`list`, index=1);
```

**Arguments:**

| **Name**        | **Type**              | **Description**    |
| --------------- | --------------------- | ------------------ |
| `removed_value` | Variable\[Any Value\] | Removed Value      |
| `variable`      | Variable\[List\]      | Variable to Assign |
| `list`          | List                  | List               |
| `index`         | Number                | Index              |
<h3 id=set_variable_remove_map_entry>
  <code>variable::remove_map_entry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Dictionary Entry\
**Type:** An action that returns a value\
**Description:** Removes a dictionary entry and assigns the result to a variable.

**Usage example:** 
```ts
`variable`, `removed_value` = variable::remove_map_entry(`map`, "any value", ["any value", "any value"]);

//Or from the object

`variable`, `removed_value` = `map`.remove_map_entry("any value", ["any value", "any value"]);

//Or dry by positionals

variable::remove_map_entry(`removed_value`, `variable`, `map`, "any value", ["any value", "any value"]);

//Or dry by keywords

variable::remove_map_entry(removed_value=`removed_value`, variable=`variable`, map=`map`, key="any value", values=["any value", "any value"]);
```

**Arguments:**

| **Name**        | **Type**               | **Description**      |
| --------------- | ---------------------- | -------------------- |
| `removed_value` | Variable\[Any Value\]  | Removed Value        |
| `variable`      | Variable\[Dictionary\] | Variable to assign   |
| `map`           | Dictionary             | Dictionary to change |
| `key`           | Any Value              | Key                  |
| `values`        | list\[Any Value\]      | Values               |
<h3 id=set_variable_remove_text>
  <code>variable::remove_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Text\
**Type:** An action that returns a value\
**Description:** Removes all or part of the text and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::remove_text(["remove", "remove"], "text", "FALSE");

//Or from the object

`variable` = "text".remove_text(["remove", "remove"], "FALSE");

//Or dry by positionals

variable::remove_text(`variable`, ["remove", "remove"], "text", "FALSE");

//Or dry by keywords

variable::remove_text(variable=`variable`, remove=["remove", "remove"], text="text", regex="FALSE");
```

**Arguments:**

| **Name**   | **Type**                                             | **Description**     |
| ---------- | ---------------------------------------------------- | ------------------- |
| `variable` | Variable\[Text\]                                     | Variable to assign  |
| `remove`   | list\[Text\]                                         | Text to Remove      |
| `text`     | Text                                                 | Original Text       |
| `regex`    | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Regular Expressions |
<h3 id=set_variable_repeat_text>
  <code>variable::repeat_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat Text\
**Type:** An action that returns a value\
**Description:** Sets a variable to text repeated a specified number of times.

**Usage example:** 
```ts
`variable` = variable::repeat_text("text", 1);

//Or from the object

`variable` = "text".repeat_text(1);

//Or dry by positionals

variable::repeat_text(`variable`, "text", 1);

//Or dry by keywords

variable::repeat_text(variable=`variable`, text="text", repeat=1);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `text`     | Text             | Text to repeat     |
| `repeat`   | Number           | Number of Repeats  |
<h3 id=set_variable_replace_text>
  <code>variable::replace_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Text\
**Type:** An action that returns a value\
**Description:** Replaces all or part of the text and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::replace_text("text", "replace", "replacement", "ANY", "FALSE");

//Or from the object

`variable` = "text".replace_text("replace", "replacement", "ANY", "FALSE");

//Or dry by positionals

variable::replace_text(`variable`, "text", "replace", "replacement", "ANY", "FALSE");

//Or dry by keywords

variable::replace_text(variable=`variable`, text="text", replace="replace", replacement="replacement", first="ANY", ignore_case="FALSE");
```

**Arguments:**

| **Name**      | **Type**                                                                          | **Description**        |
| ------------- | --------------------------------------------------------------------------------- | ---------------------- |
| `variable`    | Variable\[Text\]                                                                  | Variable to assign     |
| `text`        | Text                                                                              | Original Text          |
| `replace`     | Text                                                                              | Text to Replace        |
| `replacement` | Text                                                                              | Replacement            |
| `first`       | Marker<br/>**ANY** - Replace All Matches<br/>**FIRST** - Replace First Match Only | Number of replacements |
| `ignore_case` | Marker<br/>**FALSE** - Don\'t ignore<br/>**TRUE** - Ignore                        | Ignore case            |
<h3 id=set_variable_reverse_list>
  <code>variable::reverse_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reverse List\
**Type:** An action that returns a value\
**Description:** Reverses the order of items.

**Usage example:** 
```ts
`variable` = variable::reverse_list(`list`);

//Or from the object

`variable` = `list`.reverse_list();

//Or dry by positionals

variable::reverse_list(`variable`, `list`);

//Or dry by keywords

variable::reverse_list(variable=`variable`, list=`list`);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[List\] | Variable to assign |
| `list`     | List             | List               |
<h3 id=set_variable_root>
  <code>variable::root</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Root (√)\
**Type:** An action that returns a value\
**Description:** Sets a variable to a root value with the selected root number and exponent.

**Usage example:** 
```ts
`variable` = variable::root(1, 2);

//Or dry by positionals

variable::root(`variable`, 1, 2);

//Or dry by keywords

variable::root(variable=`variable`, base=1, root=2);
```

**Arguments:**

| **Name**   | **Type**           | **Description** |
| ---------- | ------------------ | --------------- |
| `variable` | Variable\[Number\] | Variable to set |
| `base`     | Number             | Root Root       |
| `root`     | Number             | Root Index      |
<h3 id=set_variable_rotate_vector_around_axis>
  <code>variable::rotate_vector_around_axis</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Rotate Vector Around an Axis\
**Type:** An action that returns a value\
**Description:** Rotates a vector around an axis by the specified amount and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::rotate_vector_around_axis(vector(0,0,0), 1, "X", "DEGREES");

//Or from the object

`variable` = vector(0,0,0).rotate_vector_around_axis(1, "X", "DEGREES");

//Or dry by positionals

variable::rotate_vector_around_axis(`variable`, vector(0,0,0), 1, "X", "DEGREES");

//Or dry by keywords

variable::rotate_vector_around_axis(variable=`variable`, vector=vector(0,0,0), angle=1, axis="X", angle_units="DEGREES");
```

**Arguments:**

| **Name**      | **Type**                                                                          | **Description**    |
| ------------- | --------------------------------------------------------------------------------- | ------------------ |
| `variable`    | Variable\[Vector\]                                                                | Variable to assign |
| `vector`      | Vector                                                                            | Vector to Rotate   |
| `angle`       | Number                                                                            | Rotation Angle     |
| `axis`        | Marker<br/>**X** - X Coordinate<br/>**Y** - Y Coordinate<br/>**Z** - Z Coordinate | Coordinate Type    |
| `angle_units` | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                        | Angle Type         |
<h3 id=set_variable_rotate_vector_around_vector>
  <code>variable::rotate_vector_around_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Rotate Vector Around Another Vector\
**Type:** An action that returns a value\
**Description:** Rotates a vector around another vector by the specified amount and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::rotate_vector_around_vector(vector(0,0,0), vector(0,0,0), 1, "DEGREES");

//Or from the object

`variable` = vector(0,0,0).rotate_vector_around_vector(vector(0,0,0), 1, "DEGREES");

//Or dry by positionals

variable::rotate_vector_around_vector(`variable`, vector(0,0,0), vector(0,0,0), 1, "DEGREES");

//Or dry by keywords

variable::rotate_vector_around_vector(variable=`variable`, rotating_vector=vector(0,0,0), axis_vector=vector(0,0,0), angle=1, angle_units="DEGREES");
```

**Arguments:**

| **Name**          | **Type**                                                   | **Description**    |
| ----------------- | ---------------------------------------------------------- | ------------------ |
| `variable`        | Variable\[Vector\]                                         | Variable to assign |
| `rotating_vector` | Vector                                                     | Vector to Rotate   |
| `axis_vector`     | Vector                                                     | Axis Vector        |
| `angle`           | Number                                                     | Rotation Angle     |
| `angle_units`     | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians | Angle Type         |
<h3 id=set_variable_round>
  <code>variable::round</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Round Number\
**Type:** An action that returns a value\
**Description:** Sets a number rounded in the chosen way to a variable.

**Usage example:** 
```ts
`variable` = variable::round(1, 2, "CEIL");

//Or from the object

`variable` = (1).round(2, "CEIL");

//Or dry by positionals

variable::round(`variable`, 1, 2, "CEIL");

//Or dry by keywords

variable::round(variable=`variable`, number=1, precision=2, round_type="CEIL");
```

**Arguments:**

| **Name**     | **Type**                                                                                  | **Description**                     |
| ------------ | ----------------------------------------------------------------------------------------- | ----------------------------------- |
| `variable`   | Variable\[Number\]                                                                        | Variable to assign                  |
| `number`     | Number                                                                                    | Number to Round                     |
| `precision`  | Number                                                                                    | Number of digits after integer part |
| `round_type` | Marker<br/>**CEIL** - Round Up<br/>**FLOOR** - Round Down<br/>**ROUND** - Normal Rounding | Rounding Method                     |
<h3 id=set_variable_set_all_coordinates>
  <code>variable::set_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set All Location Coordinates\
**Type:** An action that returns a value\
**Description:** Sets the values of all coordinates to a location.

**Usage example:** 
```ts
`variable` = variable::set_all_coordinates(1, 2, 3, 4, 5);

//Or dry by positionals

variable::set_all_coordinates(`variable`, 1, 2, 3, 4, 5);

//Or dry by keywords

variable::set_all_coordinates(variable=`variable`, x=1, y=2, z=3, yaw=4, pitch=5);
```

**Arguments:**

| **Name**   | **Type**             | **Description**     |
| ---------- | -------------------- | ------------------- |
| `variable` | Variable\[Location\] | Variable to assign  |
| `x`        | Number               | X Coordinate        |
| `y`        | Number               | Y Coordinate        |
| `z`        | Number               | Z Coordinate        |
| `yaw`      | Number               | Horizontal Rotation |
| `pitch`    | Number               | Pitch Vertical      |
<h3 id=set_variable_set_armor_trim>
  <code>variable::set_armor_trim</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor Trim\
**Type:** Action without value\
**Description:** Sets the armor trim on an armor piece.

**Usage example:** 
```ts
variable::set_armor_trim(`variable`, item("stick"), item("stick"), item("stick"));

//Or from the object

item("stick").set_armor_trim(`variable`, item("stick"), item("stick"));

//Or dry by keywords

variable::set_armor_trim(variable=`variable`, armor=item("stick"), material=item("stick"), pattern=item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `variable` | Variable | Variable to set |
| `armor`    | Item     | Armor           |
| `material` | Item     | Material        |
| `pattern`  | Item     | Pattern         |
<h3 id=set_variable_set_book_page>
  <code>variable::set_book_page</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Book Text On Page\
**Type:** An action that returns a value\
**Description:** Sets the book text on a specific page and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_book_page(item("stick"), "text", 1, "APPEND");

//Or from the object

`variable` = item("stick").set_book_page("text", 1, "APPEND");

//Or dry by positionals

variable::set_book_page(`variable`, item("stick"), "text", 1, "APPEND");

//Or dry by keywords

variable::set_book_page(variable=`variable`, book=item("stick"), text="text", page=1, mode="APPEND");
```

**Arguments:**

| **Name**   | **Type**                                               | **Description**    |
| ---------- | ------------------------------------------------------ | ------------------ |
| `variable` | Variable\[Item\]                                       | Variable to assign |
| `book`     | Item                                                   | Book to change     |
| `text`     | Text                                                   | New Text           |
| `page`     | Number                                                 | Page Number        |
| `mode`     | Marker<br/>**APPEND** - Append<br/>**MERGE** - Replace | Set Mode           |
<h3 id=set_variable_set_book_pages>
  <code>variable::set_book_pages</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Book Text\
**Type:** An action that returns a value\
**Description:** Sets the book text and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_book_pages(item("stick"), ["text", "text"]);

//Or from the object

`variable` = item("stick").set_book_pages(["text", "text"]);

//Or dry by positionals

variable::set_book_pages(`variable`, item("stick"), ["text", "text"]);

//Or dry by keywords

variable::set_book_pages(variable=`variable`, book=item("stick"), text=["text", "text"]);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `book`     | Item             | Book to change     |
| `text`     | list\[Text\]     | New Text           |
<h3 id=set_variable_set_bundle_items>
  <code>variable::set_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Bundle Items\
**Type:** Action without value\
**Description:** Sets the items in a bundle.

**Usage example:** 
```ts
variable::set_bundle_items(`variable`, item("stick"), [item("stick"), item("stick")], "ADD");

//Or from the object

item("stick").set_bundle_items(`variable`, [item("stick"), item("stick")], "ADD");

//Or dry by keywords

variable::set_bundle_items(variable=`variable`, bundle=item("stick"), items=[item("stick"), item("stick")], setting_mode="ADD");
```

**Arguments:**

| **Name**       | **Type**                                                           | **Description** |
| -------------- | ------------------------------------------------------------------ | --------------- |
| `variable`     | Variable                                                           | Variable to set |
| `bundle`       | Item                                                               | Bundle          |
| `items`        | list\[Item\]                                                       | Items           |
| `setting_mode` | Marker<br/>**ADD** - Add<br/>**REMOVE** - Remove<br/>**SET** - Set | Set mode        |
<h3 id=set_variable_set_compass_lodestone>
  <code>variable::set_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Lodestone Location\
**Type:** An action that returns a value\
**Description:** Sets the compass to the location of the magnetite and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_compass_lodestone(item("stick"), location(0,0,0,0,0), "FALSE");

//Or from the object

`variable` = item("stick").set_compass_lodestone(location(0,0,0,0,0), "FALSE");

//Or dry by positionals

variable::set_compass_lodestone(`variable`, item("stick"), location(0,0,0,0,0), "FALSE");

//Or dry by keywords

variable::set_compass_lodestone(variable=`variable`, item=item("stick"), location=location(0,0,0,0,0), tracked="FALSE");
```

**Arguments:**

| **Name**   | **Type**                                                 | **Description**             |
| ---------- | -------------------------------------------------------- | --------------------------- |
| `variable` | Variable\[Item\]                                         | Variable to Assign          |
| `item`     | Item                                                     | Compass                     |
| `location` | Location                                                 | Magnetite Location          |
| `tracked`  | Marker<br/>**FALSE** - Don\'t check<br/>**TRUE** - Track | Location Magnetite Presence |
<h3 id=set_variable_set_component_children>
  <code>variable::set_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Styled Text Children Components\
**Type:** An action that returns a value\
**Description:** Sets the children components of the Styled Text.

**Usage example:** 
```ts
`variable` = variable::set_component_children("component", ["children", "children"]);

//Or from the object

`variable` = "component".set_component_children(["children", "children"]);

//Or dry by positionals

variable::set_component_children(`variable`, "component", ["children", "children"]);

//Or dry by keywords

variable::set_component_children(variable=`variable`, component="component", children=["children", "children"]);
```

**Arguments:**

| **Name**    | **Type**         | **Description**         |
| ----------- | ---------------- | ----------------------- |
| `variable`  | Variable\[Text\] | Variable to assign      |
| `component` | Text             | Main stylized text      |
| `children`  | list\[Text\]     | Children stylized texts |
<h3 id=set_variable_set_component_click>
  <code>variable::set_component_click</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Click Action\
**Type:** An action that returns a value\
**Description:** Sets the click event of the Styled Text.

**Usage example:** 
```ts
`variable` = variable::set_component_click("component", "value", "CHANGE_PAGE");

//Or from the object

`variable` = "component".set_component_click("value", "CHANGE_PAGE");

//Or dry by positionals

variable::set_component_click(`variable`, "component", "value", "CHANGE_PAGE");

//Or dry by keywords

variable::set_component_click(variable=`variable`, component="component", value="value", click_action="CHANGE_PAGE");
```

**Arguments:**

| **Name**       | **Type**                                                                                                                                                                                                  | **Description**  |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `variable`     | Variable\[Text\]                                                                                                                                                                                          | Variable to set  |
| `component`    | Text                                                                                                                                                                                                      | The Styled Text  |
| `value`        | Text                                                                                                                                                                                                      | Value            |
| `click_action` | Marker<br/>**CHANGE_PAGE** - Change page<br/>**COPY_TO_CLIPBOARD** - Copy to Clipboard<br/>**COPY_TO_CLIPBORD** - Copy to clipboard<br/>**OPEN_URL** - Open URL<br/>**SUGGEST_COMMAND** - Suggest command | Click Event Type |
<h3 id=set_variable_set_component_decorations>
  <code>variable::set_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Decorations\
**Type:** An action that returns a value\
**Description:** Sets the text decorations (bold, italics, underlined, strikethrough, obfuscated) of a Styled Text.

**Usage example:** 
```ts
`variable` = variable::set_component_decorations("component", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Or from the object

`variable` = "component".set_component_decorations("FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Or dry by positionals

variable::set_component_decorations(`variable`, "component", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Or dry by keywords

variable::set_component_decorations(variable=`variable`, component="component", bold="FALSE", italic="FALSE", underlined="FALSE", strikethrough="FALSE", obfuscated="FALSE");
```

**Arguments:**

| **Name**        | **Type**                                                               | **Description**     |
| --------------- | ---------------------------------------------------------------------- | ------------------- |
| `variable`      | Variable\[Text\]                                                       | Variable to assign  |
| `component`     | Text                                                                   | Stylized text       |
| `bold`          | Marker<br/>**FALSE** - No<br/>**NOT_SET** - Not set<br/>**TRUE** - Yes | Bold text           |
| `italic`        | Marker<br/>**FALSE** - No<br/>**NOT_SET** - Not set<br/>**TRUE** - Yes | Italic text         |
| `underlined`    | Marker<br/>**FALSE** - No<br/>**NOT_SET** - Not set<br/>**TRUE** - Yes | Underlined text     |
| `strikethrough` | Marker<br/>**FALSE** - No<br/>**NOT_SET** - Not set<br/>**TRUE** - Yes | Strikedthrough text |
| `obfuscated`    | Marker<br/>**FALSE** - No<br/>**NOT_SET** - Not set<br/>**TRUE** - Yes | Obfuscated text     |
<h3 id=set_variable_set_component_entity_hover>
  <code>variable::set_component_entity_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Entity Hover\
**Type:** An action that returns a value\
**Description:** Sets the hover entity of the Styled Text.

**Usage example:** 
```ts
`variable` = variable::set_component_entity_hover("component", "name_or_uuid");

//Or from the object

`variable` = "component".set_component_entity_hover("name_or_uuid");

//Or dry by positionals

variable::set_component_entity_hover(`variable`, "component", "name_or_uuid");

//Or dry by keywords

variable::set_component_entity_hover(variable=`variable`, component="component", name_or_uuid="name_or_uuid");
```

**Arguments:**

| **Name**       | **Type**         | **Description**    |
| -------------- | ---------------- | ------------------ |
| `variable`     | Variable\[Text\] | Variable to set    |
| `component`    | Text             | The Styled Text    |
| `name_or_uuid` | Text             | UUID of the entity |
<h3 id=set_variable_set_component_font>
  <code>variable::set_component_font</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Font\
**Type:** An action that returns a value\
**Description:** Sets the font of the Styled Text.

**Usage example:** 
```ts
`variable` = variable::set_component_font("component", "namespace", "value");

//Or from the object

`variable` = "component".set_component_font("namespace", "value");

//Or dry by positionals

variable::set_component_font(`variable`, "component", "namespace", "value");

//Or dry by keywords

variable::set_component_font(variable=`variable`, component="component", namespace="namespace", value="value");
```

**Arguments:**

| **Name**    | **Type**         | **Description**               |
| ----------- | ---------------- | ----------------------------- |
| `variable`  | Variable\[Text\] | Variable to assign            |
| `component` | Text             | Stylized text                 |
| `namespace` | Text             | Namespace (minecraft\:, etc.) |
| `value`     | Text             | Font ID                       |
<h3 id=set_variable_set_component_hex_color>
  <code>variable::set_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Hex Color\
**Type:** An action that returns a value\
**Description:** Sets the color in hex of a Styled Text.

**Usage example:** 
```ts
`variable` = variable::set_component_hex_color("component", "color");

//Or from the object

`variable` = "component".set_component_hex_color("color");

//Or dry by positionals

variable::set_component_hex_color(`variable`, "component", "color");

//Or dry by keywords

variable::set_component_hex_color(variable=`variable`, component="component", color="color");
```

**Arguments:**

| **Name**    | **Type**         | **Description**    |
| ----------- | ---------------- | ------------------ |
| `variable`  | Variable\[Text\] | Variable to assign |
| `component` | Text             | Stylized text      |
| `color`     | Text             | HEX-color          |
<h3 id=set_variable_set_component_hover>
  <code>variable::set_component_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Hover\
**Type:** An action that returns a value\
**Description:** Sets the hover text of the Styled Text.

**Usage example:** 
```ts
`variable` = variable::set_component_hover("component", "hover");

//Or from the object

`variable` = "component".set_component_hover("hover");

//Or dry by positionals

variable::set_component_hover(`variable`, "component", "hover");

//Or dry by keywords

variable::set_component_hover(variable=`variable`, component="component", hover="hover");
```

**Arguments:**

| **Name**    | **Type**         | **Description**    |
| ----------- | ---------------- | ------------------ |
| `variable`  | Variable\[Text\] | Variable to assign |
| `component` | Text             | Stylized text      |
| `hover`     | Text             | Hover text         |
<h3 id=set_variable_set_component_insertion>
  <code>variable::set_component_insertion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Hover Text\
**Type:** An action that returns a value\
**Description:** Sets the insert text of the Styled Text.

**Usage example:** 
```ts
`variable` = variable::set_component_insertion("component", "insertion");

//Or from the object

`variable` = "component".set_component_insertion("insertion");

//Or dry by positionals

variable::set_component_insertion(`variable`, "component", "insertion");

//Or dry by keywords

variable::set_component_insertion(variable=`variable`, component="component", insertion="insertion");
```

**Arguments:**

| **Name**    | **Type**         | **Description** |
| ----------- | ---------------- | --------------- |
| `variable`  | Variable\[Text\] | Variable to set |
| `component` | Text             | The Styled Text |
| `insertion` | Text             | Text to insert  |
<h3 id=set_variable_set_component_item_hover>
  <code>variable::set_component_item_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Item Hover\
**Type:** An action that returns a value\
**Description:** Sets the hover item of the Styled Text.

**Usage example:** 
```ts
`variable` = variable::set_component_item_hover("component", item("stick"));

//Or from the object

`variable` = "component".set_component_item_hover(item("stick"));

//Or dry by positionals

variable::set_component_item_hover(`variable`, "component", item("stick"));

//Or dry by keywords

variable::set_component_item_hover(variable=`variable`, component="component", hover=item("stick"));
```

**Arguments:**

| **Name**    | **Type**         | **Description**    |
| ----------- | ---------------- | ------------------ |
| `variable`  | Variable\[Text\] | Variable to assign |
| `component` | Text             | Stylized text      |
| `hover`     | Item             | Hover item         |
<h3 id=set_variable_set_component_shadow_color>
  <code>variable::set_component_shadow_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_component_shadow_color("component", "color");

//Or from the object

`variable` = "component".set_component_shadow_color("color");

//Or dry by positionals

variable::set_component_shadow_color(`variable`, "component", "color");

//Or dry by keywords

variable::set_component_shadow_color(variable=`variable`, component="component", color="color");
```

**Arguments:**

| **Name**    | **Type**         | **Description** |
| ----------- | ---------------- | --------------- |
| `variable`  | Variable\[Text\] | None            |
| `component` | Text             | None            |
| `color`     | Text             | None            |
<h3 id=set_variable_set_coordinate>
  <code>variable::set_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Location Coordinate\
**Type:** An action that returns a value\
**Description:** Sets the value of the selected coordinate to a location and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_coordinate(location(0,0,0,0,0), 1, "PITCH");

//Or from the object

`variable` = location(0,0,0,0,0).set_coordinate(1, "PITCH");

//Or dry by positionals

variable::set_coordinate(`variable`, location(0,0,0,0,0), 1, "PITCH");

//Or dry by keywords

variable::set_coordinate(variable=`variable`, location=location(0,0,0,0,0), coordinate=1, type="PITCH");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                         | **Description**    |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable\[Location\]                                                                                                             | Variable to assign |
| `location`   | Location                                                                                                                         | Location to set    |
| `coordinate` | Number                                                                                                                           | Coordinate Value   |
| `type`       | Marker<br/>**PITCH** - Pitch Vertical<br/>**X** - X Axis<br/>**Y** - Y Axis<br/>**YAW** - Horizontal rotation<br/>**Z** - Z Axis | Coordinate Type    |
<h3 id=set_variable_set_item_amount>
  <code>variable::set_item_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Amount\
**Type:** An action that returns a value\
**Description:** Sets the number of items in a stack.

**Usage example:** 
```ts
`variable` = variable::set_item_amount(item("stick"), 1);

//Or from the object

`variable` = item("stick").set_item_amount(1);

//Or dry by positionals

variable::set_item_amount(`variable`, item("stick"), 1);

//Or dry by keywords

variable::set_item_amount(variable=`variable`, item=item("stick"), amount=1);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `item`     | Item             | Item               |
| `amount`   | Number           | Amount             |
<h3 id=set_variable_set_item_attribute>
  <code>variable::set_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Attribute To Item\
**Type:** An action that returns a value\
**Description:** Adds a specific attribute to an item and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_attribute(item("stick"), 1, "name", "ARMOR", "ALL", "ADD_NUMBER");

//Or from the object

`variable` = item("stick").set_item_attribute(1, "name", "ARMOR", "ALL", "ADD_NUMBER");

//Or dry by positionals

variable::set_item_attribute(`variable`, item("stick"), 1, "name", "ARMOR", "ALL", "ADD_NUMBER");

//Or dry by keywords

variable::set_item_attribute(variable=`variable`, item=item("stick"), amount=1, name="name", attribute="ARMOR", slot="ALL", operation="ADD_NUMBER");
```

**Arguments:**

| **Name**    | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Description**     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `variable`  | Variable\[Item\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Variable to assign  |
| `item`      | Item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Item                |
| `amount`    | Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Attribute Value     |
| `name`      | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Attribute Name      |
| `attribute` | Marker<br/>**ARMOR** - Armor<br/>**ARMOR_TOUGHNESS** - Armor Toughness<br/>**ATTACK_DAMAGE** - Attack Damage<br/>**ATTACK_KNOCKBACK** - Attack Knockback<br/>**ATTACK_SPEED** - Attack Speed<br/>**FLYING_SPEED** - Flying Speed<br/>**FOLLOW_RANGE** - Follow Range<br/>**GENERIC_ARMOR** - Protection Points (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Defense Density Points (generic.armor_toughness)<br/>**GENERIC_ATTACK_DAMAGE** - Attack Damage (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Attack Knockback (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Attack Speed (generic.attack_speed)<br/>**GENERIC_BURNING_TIME** - Burning Time<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Explosion Knockback Resistance<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Fall Damage Multiplier<br/>**GENERIC_FLYING_SPEED** - Flying speed (generic.flying_speed)<br/>**GENERIC_FOLLOW_RANGE** - Follow Distance (generic.follow_range)<br/>**GENERIC_GRAVITY** - Gravity<br/>**GENERIC_JUMP_STRENGTH** - Jump Strength<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Knockback Resistance (generic.knockback_resistance)<br/>**GENERIC_LUCK** - Fishing Luck (generic.luck)<br/>**GENERIC_MAX_ABSORPTION** - Max absorption (generic.max_absorption)<br/>**GENERIC_MAX_HEALTH** - Maximum Health (generic.max_health)<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Movement Efficiency<br/>**GENERIC_MOVEMENT_SPEED** - Movement Speed (generic.movement_speed)<br/>**GENERIC_OXYGEN_BONUS** - Oxygen Bonus<br/>**GENERIC_SAFE_FALL_DISTANCE** - Safe Fall Distance<br/>**GENERIC_SCALE** - Scale<br/>**GENERIC_STEP_HEIGHT** - Step Height<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Water Movement Efficiency<br/>**HORSE_JUMP_STRENGTH** - Horse Jump Strength (horse.jump_strength)<br/>**KNOCKBACK_RESISTANCE** - Knockback Resistance<br/>**LUCK** - Luck<br/>**MAX_ABSORPTION** - Max Absorption<br/>**MAX_HEALTH** - Max Health<br/>**MOVEMENT_SPEED** - Movement Speed<br/>**PLAYER_BLOCK_BREAK_SPEED** - Block Breaking Speed<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - Block Interaction Range<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - Entity Interaction Range<br/>**PLAYER_MINING_EFFICIENCY** - Mining Efficiency<br/>**PLAYER_SNEAKING_SPEED** - Sneaking Speed<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Submerged Mining Speed<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - Sweeping Damage Ratio<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Zombie reinforcements (zombie.spawn_reinforcements) | Attribute Type      |
| `slot`      | Marker<br/>**ALL** - All<br/>**ARMOR** - Armor<br/>**BODY** - Body (doesn\'t work with all entities)<br/>**BOOTS** - Boots<br/>**CHEST** - Chest<br/>**HAND** - Hand<br/>**HEAD** - Helmet<br/>**LEGGINGS** - Leggings<br/>**MAIN_HAND** - Main Hand<br/>**OFF_HAND** - Offhand                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Attribute Slot      |
| `operation` | Marker<br/>**ADD_NUMBER** - Amount<br/>**ADD_SCALAR** - Percentage<br/>**MULTIPLY_SCALAR_1** - Product (multiplicative)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Attribute Operation |
<h3 id=set_variable_set_item_break_sound>
  <code>variable::set_item_break_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_item_break_sound(item("stick"), "break_sound");

//Or from the object

`variable` = item("stick").set_item_break_sound("break_sound");

//Or dry by positionals

variable::set_item_break_sound(`variable`, item("stick"), "break_sound");

//Or dry by keywords

variable::set_item_break_sound(variable=`variable`, item=item("stick"), break_sound="break_sound");
```

**Arguments:**

| **Name**      | **Type**         | **Description** |
| ------------- | ---------------- | --------------- |
| `variable`    | Variable\[Item\] | None            |
| `item`        | Item             | None            |
| `break_sound` | Text             | None            |
<h3 id=set_variable_set_item_color>
  <code>variable::set_item_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Color\
**Type:** An action that returns a value\
**Description:** Sets the specified color to an item and assigns the result to a variable.
**Work_with:**\
&nbsp;&nbsp;Leather Armor\
&nbsp;&nbsp;Potions\
&nbsp;&nbsp;Tipped Arrows\
&nbsp;&nbsp;Filled Maps\
&nbsp;&nbsp;Firework Stars

**Usage example:** 
```ts
`variable` = variable::set_item_color(item("stick"), "color");

//Or from the object

`variable` = item("stick").set_item_color("color");

//Or dry by positionals

variable::set_item_color(`variable`, item("stick"), "color");

//Or dry by keywords

variable::set_item_color(variable=`variable`, item=item("stick"), color="color");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `item`     | Item             | Item               |
| `color`    | Text             | Color              |
<h3 id=set_variable_set_item_component>
  <code>variable::set_item_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Component\
**Type:** An action that returns a value\
**Description:** Sets a component to an item with the specified value and assigns the resulting item to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_component(item("stick"), "component", "any value");

//Or from the object

`variable` = item("stick").set_item_component("component", "any value");

//Or dry by positionals

variable::set_item_component(`variable`, item("stick"), "component", "any value");

//Or dry by keywords

variable::set_item_component(variable=`variable`, item=item("stick"), component="component", value="any value");
```

**Arguments:**

| **Name**    | **Type**         | **Description** |
| ----------- | ---------------- | --------------- |
| `variable`  | Variable\[Item\] | Variable        |
| `item`      | Item             | Item            |
| `component` | Text             | Component Key   |
| `value`     | Any Value        | Component Value |
<h3 id=set_variable_set_item_custom_model_data>
  <code>variable::set_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Model Data\
**Type:** An action that returns a value\
**Description:** Sets the item\'s model data (CustomModelData) and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_custom_model_data(item("stick"), 1);

//Or from the object

`variable` = item("stick").set_item_custom_model_data(1);

//Or dry by positionals

variable::set_item_custom_model_data(`variable`, item("stick"), 1);

//Or dry by keywords

variable::set_item_custom_model_data(variable=`variable`, item=item("stick"), model=1);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `item`     | Item             | Item               |
| `model`    | Number           | Model Number       |
<h3 id=set_variable_set_item_custom_tag>
  <code>variable::set_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Custom Item Tag\
**Type:** An action that returns a value\
**Description:** Sets a custom tag for an item and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_custom_tag(item("stick"), "tag_name", "tag_value");

//Or from the object

`variable` = item("stick").set_item_custom_tag("tag_name", "tag_value");

//Or dry by positionals

variable::set_item_custom_tag(`variable`, item("stick"), "tag_name", "tag_value");

//Or dry by keywords

variable::set_item_custom_tag(variable=`variable`, item=item("stick"), tag_name="tag_name", tag_value="tag_value");
```

**Arguments:**

| **Name**    | **Type**         | **Description**    |
| ----------- | ---------------- | ------------------ |
| `variable`  | Variable\[Item\] | Variable to assign |
| `item`      | Item             | Item               |
| `tag_name`  | Text             | Tag Name           |
| `tag_value` | Text             | Tag Value          |
<h3 id=set_variable_set_item_destroyable_blocks>
  <code>variable::set_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Breakeble Blocks\
**Type:** An action that returns a value\
**Description:** Sets an item with the blocks it can break and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_destroyable_blocks([item("stick"), item("stick")], item("stick"));

//Or from the object

`variable` = item("stick").set_item_destroyable_blocks([item("stick"), item("stick")]);

//Or dry by positionals

variable::set_item_destroyable_blocks(`variable`, [item("stick"), item("stick")], item("stick"));

//Or dry by keywords

variable::set_item_destroyable_blocks(variable=`variable`, destroyable=[item("stick"), item("stick")], item=item("stick"));
```

**Arguments:**

| **Name**      | **Type**         | **Description**                 |
| ------------- | ---------------- | ------------------------------- |
| `variable`    | Variable\[Item\] | Variable to assign              |
| `destroyable` | list\[Item\]     | Blocks Can Be Destroyed by Item |
| `item`        | Item             | Item                            |
<h3 id=set_variable_set_item_durability>
  <code>variable::set_item_durability</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Durability\
**Type:** An action that returns a value\
**Description:** Sets an item\'s durability and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_durability(item("stick"), 1, "DAMAGE");

//Or from the object

`variable` = item("stick").set_item_durability(1, "DAMAGE");

//Or dry by positionals

variable::set_item_durability(`variable`, item("stick"), 1, "DAMAGE");

//Or dry by keywords

variable::set_item_durability(variable=`variable`, item=item("stick"), durability=1, durability_type="DAMAGE");
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                                                                                                | **Description**    |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`        | Variable\[Item\]                                                                                                                                                                                                                                                        | Variable to Assign |
| `item`            | Item                                                                                                                                                                                                                                                                    | Item               |
| `durability`      | Number                                                                                                                                                                                                                                                                  | New Durability     |
| `durability_type` | Marker<br/>**DAMAGE** - Current Durability<br/>**DAMAGE_PERCENTAGE** - Current Durability Percentage<br/>**MAXIMUM** - Max Durability<br/>**MAX_DAMAGE** - None<br/>**REMAINING** - Remaining Durability<br/>**REMAINING_PERCENTAGE** - Remaining Durability Percentage | Durability Type    |
<h3 id=set_variable_set_item_enchantments>
  <code>variable::set_item_enchantments</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Enchantments\
**Type:** An action that returns a value\
**Description:** Sets an enchantment on an item and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_enchantments(item("stick"), `enchantments`);

//Or from the object

`variable` = item("stick").set_item_enchantments(`enchantments`);

//Or dry by positionals

variable::set_item_enchantments(`variable`, item("stick"), `enchantments`);

//Or dry by keywords

variable::set_item_enchantments(variable=`variable`, item=item("stick"), enchantments=`enchantments`);
```

**Arguments:**

| **Name**       | **Type**         | **Description**               |
| -------------- | ---------------- | ----------------------------- |
| `variable`     | Variable\[Item\] | Variable to assign            |
| `item`         | Item             | Item                          |
| `enchantments` | Dictionary       | Enchantments and their levels |
<h3 id=set_variable_set_item_food_properties>
  <code>variable::set_item_food_properties</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_item_food_properties(item("stick"), 1, 2, "TRUE");

//Or from the object

`variable` = item("stick").set_item_food_properties(1, 2, "TRUE");

//Or dry by positionals

variable::set_item_food_properties(`variable`, item("stick"), 1, 2, "TRUE");

//Or dry by keywords

variable::set_item_food_properties(variable=`variable`, item=item("stick"), nutrition=1, saturation=2, can_always_eat="TRUE");
```

**Arguments:**

| **Name**         | **Type**                                        | **Description** |
| ---------------- | ----------------------------------------------- | --------------- |
| `variable`       | Variable\[Item\]                                | None            |
| `item`           | Item                                            | None            |
| `nutrition`      | Number                                          | None            |
| `saturation`     | Number                                          | None            |
| `can_always_eat` | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
<h3 id=set_variable_set_item_glider>
  <code>variable::set_item_glider</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
`variable` = variable::set_item_glider(item("stick"), "TRUE");

//Or from the object

`variable` = item("stick").set_item_glider("TRUE");

//Or dry by positionals

variable::set_item_glider(`variable`, item("stick"), "TRUE");

//Or dry by keywords

variable::set_item_glider(variable=`variable`, item=item("stick"), glider="TRUE");
```

**Arguments:**

| **Name**   | **Type**                                        | **Description** |
| ---------- | ----------------------------------------------- | --------------- |
| `variable` | Variable\[Item\]                                | None            |
| `item`     | Item                                            | None            |
| `glider`   | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
<h3 id=set_variable_set_item_glint_override>
  <code>variable::set_item_glint_override</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_item_glint_override(item("stick"), "TRUE");

//Or from the object

`variable` = item("stick").set_item_glint_override("TRUE");

//Or dry by positionals

variable::set_item_glint_override(`variable`, item("stick"), "TRUE");

//Or dry by keywords

variable::set_item_glint_override(variable=`variable`, item=item("stick"), glowing="TRUE");
```

**Arguments:**

| **Name**   | **Type**                                                               | **Description** |
| ---------- | ---------------------------------------------------------------------- | --------------- |
| `variable` | Variable\[Item\]                                                       | None            |
| `item`     | Item                                                                   | None            |
| `glowing`  | Marker<br/>**TRUE** - None<br/>**FALSE** - None<br/>**NOT_SET** - None | None            |
<h3 id=set_variable_set_item_hidden_tooltip>
  <code>variable::set_item_hidden_tooltip</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_item_hidden_tooltip(item("stick"), "TRUE");

//Or from the object

`variable` = item("stick").set_item_hidden_tooltip("TRUE");

//Or dry by positionals

variable::set_item_hidden_tooltip(`variable`, item("stick"), "TRUE");

//Or dry by keywords

variable::set_item_hidden_tooltip(variable=`variable`, item=item("stick"), tooltip_hidden="TRUE");
```

**Arguments:**

| **Name**         | **Type**                                        | **Description** |
| ---------------- | ----------------------------------------------- | --------------- |
| `variable`       | Variable\[Item\]                                | None            |
| `item`           | Item                                            | None            |
| `tooltip_hidden` | Marker<br/>**TRUE** - None<br/>**FALSE** - None | None            |
<h3 id=set_variable_set_item_lore>
  <code>variable::set_item_lore</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Description\
**Type:** An action that returns a value\
**Description:** Sets the item\'s description.\
**Additional info:**\
&nbsp;&nbsp;Clears the description if no new one is specified.

**Usage example:** 
```ts
`variable` = variable::set_item_lore(item("stick"), ["lore", "lore"]);

//Or from the object

`variable` = item("stick").set_item_lore(["lore", "lore"]);

//Or dry by positionals

variable::set_item_lore(`variable`, item("stick"), ["lore", "lore"]);

//Or dry by keywords

variable::set_item_lore(variable=`variable`, item=item("stick"), lore=["lore", "lore"]);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `item`     | Item             | Item               |
| `lore`     | list\[Text\]     | New Description    |
<h3 id=set_variable_set_item_lore_line>
  <code>variable::set_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Description Line\
**Type:** An action that returns a value\
**Description:** Sets the item\'s description line.

**Usage example:** 
```ts
`variable` = variable::set_item_lore_line(item("stick"), "text", 1, "APPEND");

//Or from the object

`variable` = item("stick").set_item_lore_line("text", 1, "APPEND");

//Or dry by positionals

variable::set_item_lore_line(`variable`, item("stick"), "text", 1, "APPEND");

//Or dry by keywords

variable::set_item_lore_line(variable=`variable`, item=item("stick"), text="text", line=1, mode="APPEND");
```

**Arguments:**

| **Name**   | **Type**                                               | **Description**    |
| ---------- | ------------------------------------------------------ | ------------------ |
| `variable` | Variable\[Item\]                                       | Variable to assign |
| `item`     | Item                                                   | Item               |
| `text`     | Text                                                   | New Description    |
| `line`     | Number                                                 | Line Number        |
| `mode`     | Marker<br/>**APPEND** - Append<br/>**MERGE** - Replace | Set Mode           |
<h3 id=set_variable_set_item_max_stack_size>
  <code>variable::set_item_max_stack_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Max Item Amount\
**Type:** Action without value\
**Description:** Sets the max stack size for the specified item and assigns the resulting item to a variable.\
**Additional info:**\
&nbsp;&nbsp;The number of items in a stack can only be between 1 and 99.\
&nbsp;&nbsp;A value of 0 will set the max stack size to the default value.

**Usage example:** 
```ts
variable::set_item_max_stack_size(`variable`, item("stick"), 1);

//Or dry by keywords

variable::set_item_max_stack_size(variable=`variable`, item=item("stick"), size=1);
```

**Arguments:**

| **Name**   | **Type** | **Description**                    |
| ---------- | -------- | ---------------------------------- |
| `variable` | Variable | Variable                           |
| `item`     | Item     | Item                               |
| `size`     | Number   | Number of maximum items in a stack |
<h3 id=set_variable_set_item_model_data>
  <code>variable::set_item_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_item_model_data(item("stick"), "model");

//Or from the object

`variable` = item("stick").set_item_model_data("model");

//Or dry by positionals

variable::set_item_model_data(`variable`, item("stick"), "model");

//Or dry by keywords

variable::set_item_model_data(variable=`variable`, item=item("stick"), model="model");
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Item\] | None            |
| `item`     | Item             | None            |
| `model`    | Text             | None            |
<h3 id=set_variable_set_item_name>
  <code>variable::set_item_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Name\
**Type:** An action that returns a value\
**Description:** Sets the item\'s display name.

**Usage example:** 
```ts
`variable` = variable::set_item_name(item("stick"), "text");

//Or from the object

`variable` = item("stick").set_item_name("text");

//Or dry by positionals

variable::set_item_name(`variable`, item("stick"), "text");

//Or dry by keywords

variable::set_item_name(variable=`variable`, item=item("stick"), text="text");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `item`     | Item             | Item               |
| `text`     | Text             | Name               |
<h3 id=set_variable_set_item_placeable_blocks>
  <code>variable::set_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Placeable Blocks\
**Type:** An action that returns a value\
**Description:** Sets an item to placeable blocks and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_placeable_blocks([item("stick"), item("stick")], item("stick"));

//Or from the object

`variable` = item("stick").set_item_placeable_blocks([item("stick"), item("stick")]);

//Or dry by positionals

variable::set_item_placeable_blocks(`variable`, [item("stick"), item("stick")], item("stick"));

//Or dry by keywords

variable::set_item_placeable_blocks(variable=`variable`, placeable=[item("stick"), item("stick")], item=item("stick"));
```

**Arguments:**

| **Name**    | **Type**         | **Description**    |
| ----------- | ---------------- | ------------------ |
| `variable`  | Variable\[Item\] | Variable to assign |
| `placeable` | list\[Item\]     | Placeable Blocks   |
| `item`      | Item             | Item               |
<h3 id=set_variable_set_item_rarity>
  <code>variable::set_item_rarity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_item_rarity(item("stick"), "NONE");

//Or from the object

`variable` = item("stick").set_item_rarity("NONE");

//Or dry by positionals

variable::set_item_rarity(`variable`, item("stick"), "NONE");

//Or dry by keywords

variable::set_item_rarity(variable=`variable`, item=item("stick"), rarity="NONE");
```

**Arguments:**

| **Name**   | **Type**                                                                                                         | **Description** |
| ---------- | ---------------------------------------------------------------------------------------------------------------- | --------------- |
| `variable` | Variable\[Item\]                                                                                                 | None            |
| `item`     | Item                                                                                                             | None            |
| `rarity`   | Marker<br/>**NONE** - None<br/>**COMMON** - None<br/>**UNCOMMON** - None<br/>**RARE** - None<br/>**EPIC** - None | None            |
<h3 id=set_variable_set_item_tooltip_style>
  <code>variable::set_item_tooltip_style</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_item_tooltip_style(item("stick"), "style");

//Or from the object

`variable` = item("stick").set_item_tooltip_style("style");

//Or dry by positionals

variable::set_item_tooltip_style(`variable`, item("stick"), "style");

//Or dry by keywords

variable::set_item_tooltip_style(variable=`variable`, item=item("stick"), style="style");
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Item\] | None            |
| `item`     | Item             | None            |
| `style`    | Text             | None            |
<h3 id=set_variable_set_item_type>
  <code>variable::set_item_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Type\
**Type:** An action that returns a value\
**Description:** Changes the type of item without changing the other data of the item.

**Usage example:** 
```ts
`variable` = variable::set_item_type(item("stick"), "type");

//Or from the object

`variable` = item("stick").set_item_type("type");

//Or dry by positionals

variable::set_item_type(`variable`, item("stick"), "type");

//Or dry by keywords

variable::set_item_type(variable=`variable`, item=item("stick"), type="type");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `item`     | Item             | Item               |
| `type`     | Text             | Item Type          |
<h3 id=set_variable_set_item_unbreakable>
  <code>variable::set_item_unbreakable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Unbreakable\
**Type:** An action that returns a value\
**Description:** Sets an item\'s unbreakable and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_unbreakable(item("stick"), "FALSE");

//Or from the object

`variable` = item("stick").set_item_unbreakable("FALSE");

//Or dry by positionals

variable::set_item_unbreakable(`variable`, item("stick"), "FALSE");

//Or dry by keywords

variable::set_item_unbreakable(variable=`variable`, item=item("stick"), unbreakable="FALSE");
```

**Arguments:**

| **Name**      | **Type**                                             | **Description**    |
| ------------- | ---------------------------------------------------- | ------------------ |
| `variable`    | Variable\[Item\]                                     | Variable to assign |
| `item`        | Item                                                 | Item               |
| `unbreakable` | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Unbreakable        |
<h3 id=set_variable_set_item_use_remainder>
  <code>variable::set_item_use_remainder</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_item_use_remainder(item("stick"), item("stick"));

//Or from the object

`variable` = item("stick").set_item_use_remainder(item("stick"));

//Or dry by positionals

variable::set_item_use_remainder(`variable`, item("stick"), item("stick"));

//Or dry by keywords

variable::set_item_use_remainder(variable=`variable`, item=item("stick"), remainder=item("stick"));
```

**Arguments:**

| **Name**    | **Type**         | **Description** |
| ----------- | ---------------- | --------------- |
| `variable`  | Variable\[Item\] | None            |
| `item`      | Item             | None            |
| `remainder` | Item             | None            |
<h3 id=set_variable_set_item_visibility_flags>
  <code>variable::set_item_visibility_flags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Visibility Flags\
**Type:** An action that returns a value\
**Description:** Sets certain item visibility flags and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_item_visibility_flags(item("stick"), "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE");

//Or from the object

`variable` = item("stick").set_item_visibility_flags("NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE");

//Or dry by positionals

variable::set_item_visibility_flags(`variable`, item("stick"), "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE");

//Or dry by keywords

variable::set_item_visibility_flags(variable=`variable`, item=item("stick"), hide_dye="NO_CHANGE", hide_enchantments="NO_CHANGE", hide_attributes="NO_CHANGE", hide_unbreakable="NO_CHANGE", hide_place_on="NO_CHANGE", hide_destroys="NO_CHANGE", hide_potion_effects="NO_CHANGE", hide_armor_trim="NO_CHANGE");
```

**Arguments:**

| **Name**              | **Type**                                                                         | **Description**           |
| --------------------- | -------------------------------------------------------------------------------- | ------------------------- |
| `variable`            | Variable\[Item\]                                                                 | Variable to assign        |
| `item`                | Item                                                                             | Item                      |
| `hide_dye`            | Marker<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off<br/>**ON** - Enabled      | Hide color                |
| `hide_enchantments`   | Marker<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off<br/>**ON** - Enabled      | Hide Enchantments         |
| `hide_attributes`     | Marker<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off<br/>**ON** - Enabled      | Hide Attributes           |
| `hide_unbreakable`    | Marker<br/>**NO_CHANGE** - No Change<br/>**OFF** - Disabled<br/>**ON** - Enabled | Hide Unbreakable          |
| `hide_place_on`       | Marker<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off<br/>**ON** - Enabled      | Hide \"Can be placed on\" |
| `hide_destroys`       | Marker<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off<br/>**ON** - Enabled      | Hide \"Can break\"        |
| `hide_potion_effects` | Marker<br/>**NO_CHANGE** - No Change<br/>**OFF** - Disabled<br/>**ON** - Enabled | Hide stats                |
| `hide_armor_trim`     | Marker<br/>**NO_CHANGE** - No Change<br/>**OFF** - Disabled<br/>**ON** - Enabled | Hide Armor Trim           |
<h3 id=set_variable_set_item_weapon>
  <code>variable::set_item_weapon</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::set_item_weapon(item("stick"), 1, 2);

//Or from the object

`variable` = item("stick").set_item_weapon(1, 2);

//Or dry by positionals

variable::set_item_weapon(`variable`, item("stick"), 1, 2);

//Or dry by keywords

variable::set_item_weapon(variable=`variable`, item=item("stick"), item_damage_per_attack=1, disable_blocking=2);
```

**Arguments:**

| **Name**                 | **Type**         | **Description** |
| ------------------------ | ---------------- | --------------- |
| `variable`               | Variable\[Item\] | None            |
| `item`                   | Item             | None            |
| `item_damage_per_attack` | Number           | None            |
| `disable_blocking`       | Number           | None            |
<h3 id=set_variable_set_list_value>
  <code>variable::set_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set List Value\
**Type:** An action that returns a value\
**Description:** Sets the list value at the specified index.

**Usage example:** 
```ts
`variable` = variable::set_list_value(`list`, 1, "any value");

//Or from the object

`variable` = `list`.set_list_value(1, "any value");

//Or dry by positionals

variable::set_list_value(`variable`, `list`, 1, "any value");

//Or dry by keywords

variable::set_list_value(variable=`variable`, list=`list`, number=1, value="any value");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[List\] | Variable to assign |
| `list`     | List             | List               |
| `number`   | Number           | Index              |
| `value`    | Any Value        | Value              |
<h3 id=set_variable_set_location_direction>
  <code>variable::set_location_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Location Direction\
**Type:** An action that returns a value\
**Description:** Sets the location direction and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_location_direction(location(0,0,0,0,0), vector(0,0,0));

//Or from the object

`variable` = location(0,0,0,0,0).set_location_direction(vector(0,0,0));

//Or dry by positionals

variable::set_location_direction(`variable`, location(0,0,0,0,0), vector(0,0,0));

//Or dry by keywords

variable::set_location_direction(variable=`variable`, location=location(0,0,0,0,0), vector=vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type**             | **Description**     |
| ---------- | -------------------- | ------------------- |
| `variable` | Variable\[Location\] | Variable to Assign  |
| `location` | Location             | Location to install |
| `vector`   | Vector               | Direction Vector    |
<h3 id=set_variable_set_map_value>
  <code>variable::set_map_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Dictionary Value\
**Type:** An action that returns a value\
**Description:** Sets a specific dictionary value by key and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_map_value(`map`, ["any value", "any value"], ["any value", "any value"]);

//Or from the object

`variable` = `map`.set_map_value(["any value", "any value"], ["any value", "any value"]);

//Or dry by positionals

variable::set_map_value(`variable`, `map`, ["any value", "any value"], ["any value", "any value"]);

//Or dry by keywords

variable::set_map_value(variable=`variable`, map=`map`, key=["any value", "any value"], value=["any value", "any value"]);
```

**Arguments:**

| **Name**   | **Type**               | **Description**      |
| ---------- | ---------------------- | -------------------- |
| `variable` | Variable\[Dictionary\] | Variable to assign   |
| `map`      | Dictionary             | Dictionary to change |
| `key`      | list\[Any Value\]      | Key                  |
| `value`    | list\[Any Value\]      | New Value            |
<h3 id=set_variable_set_particle_amount>
  <code>variable::set_particle_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Amount\
**Type:** An action that returns a value\
**Description:** Sets the amount of particles and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_particle_amount(particle("fire"), 1);

//Or from the object

`variable` = particle("fire").set_particle_amount(1);

//Or dry by positionals

variable::set_particle_amount(`variable`, particle("fire"), 1);

//Or dry by keywords

variable::set_particle_amount(variable=`variable`, particle=particle("fire"), amount=1);
```

**Arguments:**

| **Name**   | **Type**                    | **Description**    |
| ---------- | --------------------------- | ------------------ |
| `variable` | Variable\[Particle Effect\] | Variable to Assign |
| `particle` | Particle Effect             | Particle to Change |
| `amount`   | Number                      | New Amount         |
<h3 id=set_variable_set_particle_color>
  <code>variable::set_particle_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Color\
**Type:** An action that returns a value\
**Description:** Sets the particle color and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_particle_color(particle("fire"), "hex_color", "COLOR");

//Or from the object

`variable` = particle("fire").set_particle_color("hex_color", "COLOR");

//Or dry by positionals

variable::set_particle_color(`variable`, particle("fire"), "hex_color", "COLOR");

//Or dry by keywords

variable::set_particle_color(variable=`variable`, particle=particle("fire"), hex_color="hex_color", color_type="COLOR");
```

**Arguments:**

| **Name**     | **Type**                                                                | **Description**    |
| ------------ | ----------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable\[Particle Effect\]                                             | Variable to assign |
| `particle`   | Particle Effect                                                         | Particle to change |
| `hex_color`  | Text                                                                    | HEX color          |
| `color_type` | Marker<br/>**COLOR** - Normal color<br/>**TO_COLOR** - Transition color | Color type         |
<h3 id=set_variable_set_particle_material>
  <code>variable::set_particle_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Material\
**Type:** An action that returns a value\
**Description:** Sets the particle material and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_particle_material(particle("fire"), item("stick"));

//Or from the object

`variable` = particle("fire").set_particle_material(item("stick"));

//Or dry by positionals

variable::set_particle_material(`variable`, particle("fire"), item("stick"));

//Or dry by keywords

variable::set_particle_material(variable=`variable`, particle=particle("fire"), material=item("stick"));
```

**Arguments:**

| **Name**   | **Type**                    | **Description**    |
| ---------- | --------------------------- | ------------------ |
| `variable` | Variable\[Particle Effect\] | Variable to assign |
| `particle` | Particle Effect             | Particle to change |
| `material` | Item                        | New Material       |
<h3 id=set_variable_set_particle_offset>
  <code>variable::set_particle_offset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Motion\
**Type:** An action that returns a value\
**Description:** Sets the movement of a particle and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_particle_offset(particle("fire"), vector(0,0,0));

//Or from the object

`variable` = particle("fire").set_particle_offset(vector(0,0,0));

//Or dry by positionals

variable::set_particle_offset(`variable`, particle("fire"), vector(0,0,0));

//Or dry by keywords

variable::set_particle_offset(variable=`variable`, particle=particle("fire"), offset=vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type**                    | **Description**    |
| ---------- | --------------------------- | ------------------ |
| `variable` | Variable\[Particle Effect\] | Variable to assign |
| `particle` | Particle Effect             | Particle to change |
| `offset`   | Vector                      | New Motion         |
<h3 id=set_variable_set_particle_size>
  <code>variable::set_particle_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Size\
**Type:** An action that returns a value\
**Description:** Sets the particle size and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_particle_size(particle("fire"), 1);

//Or from the object

`variable` = particle("fire").set_particle_size(1);

//Or dry by positionals

variable::set_particle_size(`variable`, particle("fire"), 1);

//Or dry by keywords

variable::set_particle_size(variable=`variable`, particle=particle("fire"), size=1);
```

**Arguments:**

| **Name**   | **Type**                    | **Description**    |
| ---------- | --------------------------- | ------------------ |
| `variable` | Variable\[Particle Effect\] | Variable to assign |
| `particle` | Particle Effect             | Particle to change |
| `size`     | Number                      | New Size           |
<h3 id=set_variable_set_particle_spread>
  <code>variable::set_particle_spread</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Spread\
**Type:** An action that returns a value\
**Description:** Sets a particle\'s spread value to a variable.

**Usage example:** 
```ts
`variable` = variable::set_particle_spread(particle("fire"), 1, 2);

//Or from the object

`variable` = particle("fire").set_particle_spread(1, 2);

//Or dry by positionals

variable::set_particle_spread(`variable`, particle("fire"), 1, 2);

//Or dry by keywords

variable::set_particle_spread(variable=`variable`, particle=particle("fire"), horizontal=1, vertical=2);
```

**Arguments:**

| **Name**     | **Type**                    | **Description**    |
| ------------ | --------------------------- | ------------------ |
| `variable`   | Variable\[Particle Effect\] | Variable to assign |
| `particle`   | Particle Effect             | Particle to change |
| `horizontal` | Number                      | Horizontal Plane   |
| `vertical`   | Number                      | Vertical Plane     |
<h3 id=set_variable_set_particle_type>
  <code>variable::set_particle_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Type\
**Type:** An action that returns a value\
**Description:** Sets the particle type and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_particle_type(particle("fire"), "type");

//Or from the object

`variable` = particle("fire").set_particle_type("type");

//Or dry by positionals

variable::set_particle_type(`variable`, particle("fire"), "type");

//Or dry by keywords

variable::set_particle_type(variable=`variable`, particle=particle("fire"), type="type");
```

**Arguments:**

| **Name**   | **Type**                    | **Description**    |
| ---------- | --------------------------- | ------------------ |
| `variable` | Variable\[Particle Effect\] | Variable to assign |
| `particle` | Particle Effect             | Particle to change |
| `type`     | Text                        | New Particle Type  |
<h3 id=set_variable_set_potion_effect_amplifier>
  <code>variable::set_potion_effect_amplifier</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Potion Power\
**Type:** An action that returns a value\
**Description:** Sets the power of a potion and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_potion_effect_amplifier(potion("slow_falling"), 1);

//Or from the object

`variable` = potion("slow_falling").set_potion_effect_amplifier(1);

//Or dry by positionals

variable::set_potion_effect_amplifier(`variable`, potion("slow_falling"), 1);

//Or dry by keywords

variable::set_potion_effect_amplifier(variable=`variable`, potion=potion("slow_falling"), amplifier=1);
```

**Arguments:**

| **Name**    | **Type**           | **Description**    |
| ----------- | ------------------ | ------------------ |
| `variable`  | Variable\[Potion\] | Variable to assign |
| `potion`    | Potion             | Potion             |
| `amplifier` | Number             | Potion Power       |
<h3 id=set_variable_set_potion_effect_duration>
  <code>variable::set_potion_effect_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Potion Duration\
**Type:** An action that returns a value\
**Description:** Sets the duration of a potion and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_potion_effect_duration(potion("slow_falling"), 1);

//Or from the object

`variable` = potion("slow_falling").set_potion_effect_duration(1);

//Or dry by positionals

variable::set_potion_effect_duration(`variable`, potion("slow_falling"), 1);

//Or dry by keywords

variable::set_potion_effect_duration(variable=`variable`, potion=potion("slow_falling"), duration=1);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Potion\] | Variable to assign |
| `potion`   | Potion             | Potion             |
| `duration` | Number             | Duration           |
<h3 id=set_variable_set_potion_effect_type>
  <code>variable::set_potion_effect_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Potion Effect\
**Type:** An action that returns a value\
**Description:** Sets the effect of a potion and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_potion_effect_type(potion("slow_falling"), "effect_type");

//Or from the object

`variable` = potion("slow_falling").set_potion_effect_type("effect_type");

//Or dry by positionals

variable::set_potion_effect_type(`variable`, potion("slow_falling"), "effect_type");

//Or dry by keywords

variable::set_potion_effect_type(variable=`variable`, potion=potion("slow_falling"), effect_type="effect_type");
```

**Arguments:**

| **Name**      | **Type**           | **Description**    |
| ------------- | ------------------ | ------------------ |
| `variable`    | Variable\[Potion\] | Variable to assign |
| `potion`      | Potion             | Potion             |
| `effect_type` | Text               | Effect ID          |
<h3 id=set_variable_set_sound_pitch>
  <code>variable::set_sound_pitch</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Pitch\
**Type:** An action that returns a value\
**Description:** Sets the pitch of a sound and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_sound_pitch(sound("entity.zombie.hurt"), 1);

//Or from the object

`variable` = sound("entity.zombie.hurt").set_sound_pitch(1);

//Or dry by positionals

variable::set_sound_pitch(`variable`, sound("entity.zombie.hurt"), 1);

//Or dry by keywords

variable::set_sound_pitch(variable=`variable`, sound=sound("entity.zombie.hurt"), pitch=1);
```

**Arguments:**

| **Name**   | **Type**          | **Description**    |
| ---------- | ----------------- | ------------------ |
| `variable` | Variable\[Sound\] | Variable to assign |
| `sound`    | Sound             | Sound to change    |
| `pitch`    | Number            | New Pitch Value    |
<h3 id=set_variable_set_sound_source>
  <code>variable::set_sound_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Source\
**Type:** An action that returns a value\
**Description:** Sets the sound source and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_sound_source(sound("entity.zombie.hurt"), "AMBIENT");

//Or from the object

`variable` = sound("entity.zombie.hurt").set_sound_source("AMBIENT");

//Or dry by positionals

variable::set_sound_source(`variable`, sound("entity.zombie.hurt"), "AMBIENT");

//Or dry by keywords

variable::set_sound_source(variable=`variable`, sound=sound("entity.zombie.hurt"), source="AMBIENT");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                                                                                                                                                                                                                                                             | **Description**    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| `variable` | Variable\[Sound\]                                                                                                                                                                                                                                                                                                                                                                    | Variable to assign |
| `sound`    | Sound                                                                                                                                                                                                                                                                                                                                                                                | Sound to change    |
| `source`   | Marker<br/>**AMBIENT** - Environment (ambient)<br/>**BLOCK** - Blocks<br/>**HOSTILE** - Hostile Creatures (hostile)<br/>**MASTER** - General (master)<br/>**MUSIC** - Music (music)<br/>**NEUTRAL** - Friendly Creatures (neutral)<br/>**PLAYER** - Players (player)<br/>**RECORD** - Music Blocks (record)<br/>**VOICE** - Voice/Speech (voice)<br/>**WEATHER** - Weather (weather) | Sound Source       |
<h3 id=set_variable_set_sound_type>
  <code>variable::set_sound_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Type\
**Type:** An action that returns a value\
**Description:** Sets the sound type and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_sound_type(sound("entity.zombie.hurt"), "namespace", "value");

//Or from the object

`variable` = sound("entity.zombie.hurt").set_sound_type("namespace", "value");

//Or dry by positionals

variable::set_sound_type(`variable`, sound("entity.zombie.hurt"), "namespace", "value");

//Or dry by keywords

variable::set_sound_type(variable=`variable`, sound=sound("entity.zombie.hurt"), namespace="namespace", value="value");
```

**Arguments:**

| **Name**    | **Type**          | **Description**             |
| ----------- | ----------------- | --------------------------- |
| `variable`  | Variable\[Sound\] | Variable to assign          |
| `sound`     | Sound             | Sound to set                |
| `namespace` | Text              | Namespace (minecraft\: etc) |
| `value`     | Text              | Sound ID                    |
<h3 id=set_variable_set_sound_variation>
  <code>variable::set_sound_variation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Variation\
**Type:** An action that returns a value\
**Description:** Sets a sound variation and assigns the result to a variable.\
**Additional info:**\
&nbsp;&nbsp;You can set both text variation and numeric seed.\
&nbsp;&nbsp;Random seed if failed to set.

**Usage example:** 
```ts
`variable` = variable::set_sound_variation(sound("entity.zombie.hurt"), "variation");

//Or from the object

`variable` = sound("entity.zombie.hurt").set_sound_variation("variation");

//Or dry by positionals

variable::set_sound_variation(`variable`, sound("entity.zombie.hurt"), "variation");

//Or dry by keywords

variable::set_sound_variation(variable=`variable`, sound=sound("entity.zombie.hurt"), variation="variation");
```

**Arguments:**

| **Name**    | **Type**          | **Description**    |
| ----------- | ----------------- | ------------------ |
| `variable`  | Variable\[Sound\] | Variable to assign |
| `sound`     | Sound             | Sound to change    |
| `variation` | Text              | Variation          |
<h3 id=set_variable_set_sound_volume_action>
  <code>variable::set_sound_volume_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Volume\
**Type:** An action that returns a value\
**Description:** Sets the sound volume and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_sound_volume_action(sound("entity.zombie.hurt"), 1);

//Or from the object

`variable` = sound("entity.zombie.hurt").set_sound_volume_action(1);

//Or dry by positionals

variable::set_sound_volume_action(`variable`, sound("entity.zombie.hurt"), 1);

//Or dry by keywords

variable::set_sound_volume_action(variable=`variable`, sound=sound("entity.zombie.hurt"), volume=1);
```

**Arguments:**

| **Name**   | **Type**          | **Description**    |
| ---------- | ----------------- | ------------------ |
| `variable` | Variable\[Sound\] | Variable to assign |
| `sound`    | Sound             | Sound to change    |
| `volume`   | Number            | New volume value   |
<h3 id=set_variable_set_template_code>
  <code>variable::set_template_code</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Template Code\
**Type:** An action that returns a value\
**Description:** Sets a code to a template and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_template_code(item("stick"), "any value");

//Or from the object

`variable` = item("stick").set_template_code("any value");

//Or dry by positionals

variable::set_template_code(`variable`, item("stick"), "any value");

//Or dry by keywords

variable::set_template_code(variable=`variable`, template=item("stick"), code="any value");
```

**Arguments:**

| **Name**   | **Type**         | **Description**      |
| ---------- | ---------------- | -------------------- |
| `variable` | Variable\[Item\] | Variable to assign   |
| `template` | Item             | Template             |
| `code`     | Any Value        | JSON Text/Dictionary |
<h3 id=set_variable_set_texture_to_map>
  <code>variable::set_texture_to_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Map Image\
**Type:** An action that returns a value\
**Description:** Sets the map image at the given link. When the server is restarted, images may disappear, so it is recommended to re-install it on the same maps when starting the world.

**Usage example:** 
```ts
`variable` = variable::set_texture_to_map(item("stick"), "url");

//Or from the object

`variable` = item("stick").set_texture_to_map("url");

//Or dry by positionals

variable::set_texture_to_map(`variable`, item("stick"), "url");

//Or dry by keywords

variable::set_texture_to_map(variable=`variable`, map=item("stick"), url="url");
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Item\] | Variable to assign |
| `map`      | Item             | Map to Set         |
| `url`      | Text             | Image Link         |
<h3 id=set_variable_set_vector_component>
  <code>variable::set_vector_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Vector Coordinate\
**Type:** An action that returns a value\
**Description:** Sets a specific vector coordinate and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_vector_component(vector(0,0,0), 1, "X");

//Or from the object

`variable` = vector(0,0,0).set_vector_component(1, "X");

//Or dry by positionals

variable::set_vector_component(`variable`, vector(0,0,0), 1, "X");

//Or dry by keywords

variable::set_vector_component(variable=`variable`, vector=vector(0,0,0), value=1, vector_component="X");
```

**Arguments:**

| **Name**           | **Type**                                                                          | **Description**    |
| ------------------ | --------------------------------------------------------------------------------- | ------------------ |
| `variable`         | Variable\[Vector\]                                                                | Variable to assign |
| `vector`           | Vector                                                                            | Vector to change   |
| `value`            | Number                                                                            | New Value          |
| `vector_component` | Marker<br/>**X** - X Coordinate<br/>**Y** - Y Coordinate<br/>**Z** - Z Coordinate | Coordinate Type    |
<h3 id=set_variable_set_vector_length>
  <code>variable::set_vector_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Vector Length\
**Type:** An action that returns a value\
**Description:** Sets the length of a vector and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_vector_length(vector(0,0,0), 1);

//Or from the object

`variable` = vector(0,0,0).set_vector_length(1);

//Or dry by positionals

variable::set_vector_length(`variable`, vector(0,0,0), 1);

//Or dry by keywords

variable::set_vector_length(variable=`variable`, vector=vector(0,0,0), length=1);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Vector\] | Variable to assign |
| `vector`   | Vector             | Vector to change   |
| `length`   | Number             | New Length         |
<h3 id=set_variable_shift_all_coordinates>
  <code>variable::shift_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift All Location Coordinates\
**Type:** An action that returns a value\
**Description:** Shifts all location coordinates by certain values.

**Usage example:** 
```ts
`variable` = variable::shift_all_coordinates(location(0,0,0,0,0), 1, 2, 3, 4, 5);

//Or from the object

`variable` = location(0,0,0,0,0).shift_all_coordinates(1, 2, 3, 4, 5);

//Or dry by positionals

variable::shift_all_coordinates(`variable`, location(0,0,0,0,0), 1, 2, 3, 4, 5);

//Or dry by keywords

variable::shift_all_coordinates(variable=`variable`, location=location(0,0,0,0,0), x=1, y=2, z=3, yaw=4, pitch=5);
```

**Arguments:**

| **Name**   | **Type**             | **Description**    |
| ---------- | -------------------- | ------------------ |
| `variable` | Variable\[Location\] | Variable to assign |
| `location` | Location             | Locations to Shift |
| `x`        | Number               | Shift X            |
| `y`        | Number               | Shift Y            |
| `z`        | Number               | Shift Z            |
| `yaw`      | Number               | Shift Yaw          |
| `pitch`    | Number               | Shift Pitch        |
<h3 id=set_variable_shift_coordinate>
  <code>variable::shift_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift Location Coordinate\
**Type:** An action that returns a value\
**Description:** Shifts a location\'s coordinate by a certain amount.

**Usage example:** 
```ts
`variable` = variable::shift_coordinate(location(0,0,0,0,0), 1, "PITCH");

//Or from the object

`variable` = location(0,0,0,0,0).shift_coordinate(1, "PITCH");

//Or dry by positionals

variable::shift_coordinate(`variable`, location(0,0,0,0,0), 1, "PITCH");

//Or dry by keywords

variable::shift_coordinate(variable=`variable`, location=location(0,0,0,0,0), distance=1, type="PITCH");
```

**Arguments:**

| **Name**   | **Type**                                                                                                             | **Description**    |
| ---------- | -------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable\[Location\]                                                                                                 | Variable to assign |
| `location` | Location                                                                                                             | Locations to Shift |
| `distance` | Number                                                                                                               | Shift Value        |
| `type`     | Marker<br/>**PITCH** - Horizontal Rotation<br/>**X** - X<br/>**Y** - Y<br/>**YAW** - Vertical Rotation<br/>**Z** - Z | Coordinate Type    |
<h3 id=set_variable_shift_location_in_direction>
  <code>variable::shift_location_in_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift Location In Direction\
**Type:** An action that returns a value\
**Description:** Shifts the location in a certain direction by a certain amount.

**Usage example:** 
```ts
`variable` = variable::shift_location_in_direction(location(0,0,0,0,0), 1, "FORWARD");

//Or from the object

`variable` = location(0,0,0,0,0).shift_location_in_direction(1, "FORWARD");

//Or dry by positionals

variable::shift_location_in_direction(`variable`, location(0,0,0,0,0), 1, "FORWARD");

//Or dry by keywords

variable::shift_location_in_direction(variable=`variable`, location=location(0,0,0,0,0), shift=1, direction="FORWARD");
```

**Arguments:**

| **Name**    | **Type**                                                                                         | **Description**    |
| ----------- | ------------------------------------------------------------------------------------------------ | ------------------ |
| `variable`  | Variable\[Location\]                                                                             | Variable to assign |
| `location`  | Location                                                                                         | Location to Shift  |
| `shift`     | Number                                                                                           | Shift Value        |
| `direction` | Marker<br/>**FORWARD** - Forward/Backward<br/>**SIDEWAYS** - Right/Left<br/>**UPWARD** - Up/Down | Direction          |
<h3 id=set_variable_shift_location_on_vector>
  <code>variable::shift_location_on_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift Location By Vector\
**Type:** An action that returns a value\
**Description:** Shifts the specified location along a vector and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::shift_location_on_vector(location(0,0,0,0,0), vector(0,0,0), 1);

//Or from the object

`variable` = location(0,0,0,0,0).shift_location_on_vector(vector(0,0,0), 1);

//Or dry by positionals

variable::shift_location_on_vector(`variable`, location(0,0,0,0,0), vector(0,0,0), 1);

//Or dry by keywords

variable::shift_location_on_vector(variable=`variable`, location=location(0,0,0,0,0), vector=vector(0,0,0), length=1);
```

**Arguments:**

| **Name**   | **Type**             | **Description**    |
| ---------- | -------------------- | ------------------ |
| `variable` | Variable\[Location\] | Variable to assign |
| `location` | Location             | Location to Shift  |
| `vector`   | Vector               | Shift Vector       |
| `length`   | Number               | Shift distance     |
<h3 id=set_variable_shift_location_towards_location>
  <code>variable::shift_location_towards_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift Location Towards Location\
**Type:** An action that returns a value\
**Description:** Shifts a location towards a given location by a certain distance and assigns it to a variable.

**Usage example:** 
```ts
`variable` = variable::shift_location_towards_location(location(0,0,0,0,0), location(0,0,0,0,0), 1);

//Or from the object

`variable` = location(0,0,0,0,0).shift_location_towards_location(location(0,0,0,0,0), 1);

//Or dry by positionals

variable::shift_location_towards_location(`variable`, location(0,0,0,0,0), location(0,0,0,0,0), 1);

//Or dry by keywords

variable::shift_location_towards_location(variable=`variable`, location_from=location(0,0,0,0,0), location_to=location(0,0,0,0,0), distance=1);
```

**Arguments:**

| **Name**        | **Type**             | **Description**            |
| --------------- | -------------------- | -------------------------- |
| `variable`      | Variable\[Location\] | Variable to assign         |
| `location_from` | Location             | Location to Shift          |
| `location_to`   | Location             | Which Location to Shift To |
| `distance`      | Number               | How much to shift location |
<h3 id=set_variable_simplex_noise_3d>
  <code>variable::simplex_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Simplex Noise\
**Type:** An action that returns a value\
**Description:** Sets the value of the Simplex noise at a specific location to a variable. Returns a number, with a value from -1 to 1.

**Usage example:** 
```ts
`variable` = variable::simplex_noise_3d(location(0,0,0,0,0), 1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Or from the object

`variable` = location(0,0,0,0,0).simplex_noise_3d(1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Or dry by positionals

variable::simplex_noise_3d(`variable`, location(0,0,0,0,0), 1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Or dry by keywords

variable::simplex_noise_3d(variable=`variable`, location=location(0,0,0,0,0), seed=1, loc_frequency=2, octaves=3, frequency=4, amplitude=5, range_mode="FULL_RANGE", normalized="FALSE");
```

**Arguments:**

| **Name**        | **Type**                                                                              | **Description**        |
| --------------- | ------------------------------------------------------------------------------------- | ---------------------- |
| `variable`      | Variable\[Number\]                                                                    | Variable to set        |
| `location`      | Location                                                                              | Location to set noise  |
| `seed`          | Number                                                                                | Noise Key              |
| `loc_frequency` | Number                                                                                | Noise Frequency        |
| `octaves`       | Number                                                                                | Noise Octaves          |
| `frequency`     | Number                                                                                | Noise Octave Frequency |
| `amplitude`     | Number                                                                                | Noise Octave Amplitude |
| `range_mode`    | Marker<br/>**FULL_RANGE** - Full Range (-1 to 1 or more)<br/>**ZERO_TO_ONE** - 0 to 1 | Value Range            |
| `normalized`    | Marker<br/>**FALSE** - Don\'t Normalize<br/>**TRUE** - Normalize                      | Normalize Values       |
<h3 id=set_variable_sine>
  <code>variable::sine</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sine\
**Type:** An action that returns a value\
**Description:** Returns the sine of a number.

**Usage example:** 
```ts
`variable` = variable::sine(1, "ARCSINE", "DEGREES");

//Or from the object

`variable` = (1).sine("ARCSINE", "DEGREES");

//Or dry by positionals

variable::sine(`variable`, 1, "ARCSINE", "DEGREES");

//Or dry by keywords

variable::sine(variable=`variable`, number=1, variant="ARCSINE", input="DEGREES");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                       | **Description**    |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable\[Number\]                                                                                                                             | Variable to assign |
| `number`   | Number                                                                                                                                         | Number to get sine |
| `variant`  | Marker<br/>**ARCSINE** - Arcsine<br/>**HYPERBOLIC_ARCSINE** - Hyperbolic Arcsine<br/>**HYPERBOLIC_SINE** - Hyperbolic Sine<br/>**SINE** - Sine | Operation Type     |
| `input`    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                                                                     | Angle Type         |
<h3 id=set_variable_sort_any_list>
  <code>variable::sort_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sort List\
**Type:** An action that returns a value\
**Description:** Sorts the items in a list.
**Work_with:**\
&nbsp;&nbsp;Numbers\
&nbsp;&nbsp;Text\
&nbsp;&nbsp;Lists

**Usage example:** 
```ts
`variable` = variable::sort_list(`list`, "ASCENDING");

//Or from the object

`variable` = `list`.sort_list("ASCENDING");

//Or dry by positionals

variable::sort_list(`variable`, `list`, "ASCENDING");

//Or dry by keywords

variable::sort_list(variable=`variable`, list=`list`, sort_mode="ASCENDING");
```

**Arguments:**

| **Name**    | **Type**                                                             | **Description**    |
| ----------- | -------------------------------------------------------------------- | ------------------ |
| `variable`  | Variable\[List\]                                                     | Variable to assign |
| `list`      | List                                                                 | List               |
| `sort_mode` | Marker<br/>**ASCENDING** - Ascending<br/>**DESCENDING** - Descending | Sort Method        |
<h3 id=set_variable_sort_any_map>
  <code>variable::sort_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sort Dictionary\
**Type:** An action that returns a value\
**Description:** Sorts a dictionary based on the given parameters and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::sort_map(`map`, "ASCENDING", "KEYS");

//Or from the object

`variable` = `map`.sort_map("ASCENDING", "KEYS");

//Or dry by positionals

variable::sort_map(`variable`, `map`, "ASCENDING", "KEYS");

//Or dry by keywords

variable::sort_map(variable=`variable`, map=`map`, sort_order="ASCENDING", sort_type="KEYS");
```

**Arguments:**

| **Name**     | **Type**                                                             | **Description**    |
| ------------ | -------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable\[Dictionary\]                                               | Variable to assign |
| `map`        | Dictionary                                                           | Dictionary to sort |
| `sort_order` | Marker<br/>**ASCENDING** - Ascending<br/>**DESCENDING** - Descending | Sort Order         |
| `sort_type`  | Marker<br/>**KEYS** - By Key<br/>**VALUES** - By Value               | Sort Type          |
<h3 id=set_variable_split_text>
  <code>variable::split_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Split Text Into List\
**Type:** An action that returns a value\
**Description:** Splits text into list items at the given character and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::split_text("text", "delimiter");

//Or from the object

`variable` = "text".split_text("delimiter");

//Or dry by positionals

variable::split_text(`variable`, "text", "delimiter");

//Or dry by keywords

variable::split_text(variable=`variable`, text="text", delimiter="delimiter");
```

**Arguments:**

| **Name**    | **Type**         | **Description**    |
| ----------- | ---------------- | ------------------ |
| `variable`  | Variable\[List\] | Variable to assign |
| `text`      | Text             | Split Text         |
| `delimiter` | Text             | Delimiter          |
<h3 id=set_variable_split_text_by_length>
  <code>variable::split_text_by_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::split_text_by_length("text", 1);

//Or from the object

`variable` = "text".split_text_by_length(1);

//Or dry by positionals

variable::split_text_by_length(`variable`, "text", 1);

//Or dry by keywords

variable::split_text_by_length(variable=`variable`, text="text", max_length=1);
```

**Arguments:**

| **Name**     | **Type**         | **Description** |
| ------------ | ---------------- | --------------- |
| `variable`   | Variable\[List\] | None            |
| `text`       | Text             | None            |
| `max_length` | Number           | None            |
<h3 id=set_variable_strip_text>
  <code>variable::strip_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Spaces\
**Type:** An action that returns a value\
**Description:** Removes spaces from text and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::strip_text("text", "ALL");

//Or from the object

`variable` = "text".strip_text("ALL");

//Or dry by positionals

variable::strip_text(`variable`, "text", "ALL");

//Or dry by keywords

variable::strip_text(variable=`variable`, text="text", strip_type="ALL");
```

**Arguments:**

| **Name**     | **Type**                                                                                                | **Description**    |
| ------------ | ------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable\[Text\]                                                                                        | Variable to assign |
| `text`       | Text                                                                                                    | Text to change     |
| `strip_type` | Marker<br/>**ALL** - Start and End<br/>**END** - End<br/>**INDENT** - Indentation<br/>**START** - Start | Strip Type         |
<h3 id=set_variable_subtract>
  <code>variable::subtract</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Subtraction (-)\
**Type:** An action that returns a value\
**Description:** Assigns a difference of numbers to a variable.

**Usage example:** 
```ts
`variable` = variable::subtract([1, 2]);

//Or dry by positionals

variable::subtract(`variable`, [1, 2]);

//Or dry by keywords

variable::subtract(variable=`variable`, value=[1, 2]);
```

**Arguments:**

| **Name**   | **Type**           | **Description**     |
| ---------- | ------------------ | ------------------- |
| `variable` | Variable\[Number\] | Variable to assign  |
| `value`    | list\[Number\]     | Numbers to Subtract |
<h3 id=set_variable_subtract_vectors>
  <code>variable::subtract_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Vector Difference\
**Type:** An action that returns a value\
**Description:** Sets a vector difference value to a variable.

**Usage example:** 
```ts
`variable` = variable::subtract_vectors([vector(0,0,0), vector(0,0,0)]);

//Or dry by positionals

variable::subtract_vectors(`variable`, [vector(0,0,0), vector(0,0,0)]);

//Or dry by keywords

variable::subtract_vectors(variable=`variable`, vectors=[vector(0,0,0), vector(0,0,0)]);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Vector\] | Variable to assign |
| `vectors`  | list\[Vector\]     | Difference Vectors |
<h3 id=set_variable_tangent>
  <code>variable::tangent</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Tangent\
**Type:** An action that returns a value\
**Description:** Returns the tangent of a number.

**Usage example:** 
```ts
`variable` = variable::tangent(1, "ARCTANGENT", "DEGREES");

//Or from the object

`variable` = (1).tangent("ARCTANGENT", "DEGREES");

//Or dry by positionals

variable::tangent(`variable`, 1, "ARCTANGENT", "DEGREES");

//Or dry by keywords

variable::tangent(variable=`variable`, number=1, variant="ARCTANGENT", input="DEGREES");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                                               | **Description**       |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `variable` | Variable\[Number\]                                                                                                                                                     | Variable to assign    |
| `number`   | Number                                                                                                                                                                 | Number to get tangent |
| `variant`  | Marker<br/>**ARCTANGENT** - Arctangent<br/>**HYPERBOLIC_ARCTANGENT** - Hyperbolic Arctangent<br/>**HYPERBOLIC_TANGENT** - Hyperbolic Tangent<br/>**TANGENT** - Tangent | Operation Type        |
| `input`    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                                                                                             | Angle Type            |
<h3 id=set_variable_text>
  <code>variable::set_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text\
**Type:** An action that returns a value\
**Description:** Concatenates and assigns one or more text values to a variable.

**Usage example:** 
```ts
`variable` = variable::set_text(["text", "text"], "CONCATENATION");

//Or dry by positionals

variable::set_text(`variable`, ["text", "text"], "CONCATENATION");

//Or dry by keywords

variable::set_text(variable=`variable`, text=["text", "text"], merging="CONCATENATION");
```

**Arguments:**

| **Name**   | **Type**                                                                                                       | **Description**    |
| ---------- | -------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable\[Text\]                                                                                               | Variable to assign |
| `text`     | list\[Text\]                                                                                                   | Text to set        |
| `merging`  | Marker<br/>**CONCATENATION** - Merge<br/>**SEPARATE_LINES** - Separate Lines<br/>**SPACES** - Space Separation | Merge Text         |
<h3 id=set_variable_text_case>
  <code>variable::set_text_case</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text Case\
**Type:** An action that returns a value\
**Description:** Sets the text case and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_text_case("text", "INVERT");

//Or from the object

`variable` = "text".set_text_case("INVERT");

//Or dry by positionals

variable::set_text_case(`variable`, "text", "INVERT");

//Or dry by keywords

variable::set_text_case(variable=`variable`, text="text", case_type="INVERT");
```

**Arguments:**

| **Name**    | **Type**                                                                                                                            | **Description**    |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`  | Variable\[Text\]                                                                                                                    | Variable to assign |
| `text`      | Text                                                                                                                                | Text to set        |
| `case_type` | Marker<br/>**INVERT** - Invert<br/>**LOWER** - Lower<br/>**PROPER** - First character<br/>**RANDOM** - Random<br/>**UPPER** - Upper | Case Type          |
<h3 id=set_variable_text_length>
  <code>variable::get_text_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Text Length\
**Type:** An action that returns a value\
**Description:** Sets the number of characters in text to a variable.

**Usage example:** 
```ts
`variable` = variable::get_text_length("text");

//Or from the object

`variable` = "text".get_text_length();

//Or dry by positionals

variable::get_text_length(`variable`, "text");

//Or dry by keywords

variable::get_text_length(variable=`variable`, text="text");
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `text`     | Text               | Text to Get Length |
<h3 id=set_variable_text_to_bytes>
  <code>variable::text_to_bytes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Convert text to bytes\
**Type:** An action that returns a value\
**Description:** Converts the text to bytes and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::text_to_bytes("text", "UTF_8");

//Or from the object

`variable` = "text".text_to_bytes("UTF_8");

//Or dry by positionals

variable::text_to_bytes(`variable`, "text", "UTF_8");

//Or dry by keywords

variable::text_to_bytes(variable=`variable`, text="text", charset="UTF_8");
```

**Arguments:**

| **Name**   | **Type**                                          | **Description**    |
| ---------- | ------------------------------------------------- | ------------------ |
| `variable` | Variable\[List\]                                  | Variable to assign |
| `text`     | Text                                              | Text to convert    |
| `charset`  | Marker<br/>**UTF_8** - None<br/>**ASCII** - ASCII | Encoding           |
<h3 id=set_variable_text_to_chars>
  <code>variable::text_to_chars</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::text_to_chars("text", "CHARS");

//Or from the object

`variable` = "text".text_to_chars("CHARS");

//Or dry by positionals

variable::text_to_chars(`variable`, "text", "CHARS");

//Or dry by keywords

variable::text_to_chars(variable=`variable`, text="text", chars_type="CHARS");
```

**Arguments:**

| **Name**     | **Type**                                                                                                   | **Description** |
| ------------ | ---------------------------------------------------------------------------------------------------------- | --------------- |
| `variable`   | Variable\[Text\]                                                                                           | None            |
| `text`       | Text                                                                                                       | None            |
| `chars_type` | Marker<br/>**CHARS** - None<br/>**CODES** - None<br/>**CODEPOINTS_CHARS** - None<br/>**CODEPOINTS** - None | None            |
<h3 id=set_variable_to_char>
  <code>variable::to_char</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Character By Number\
**Type:** An action that returns a value\
**Description:** Get a specific character from a number and assign the result to a variable.

**Usage example:** 
```ts
`variable` = variable::to_char(1);

//Or from the object

`variable` = (1).to_char();

//Or dry by positionals

variable::to_char(`variable`, 1);

//Or dry by keywords

variable::to_char(variable=`variable`, number=1);
```

**Arguments:**

| **Name**   | **Type**         | **Description**         |
| ---------- | ---------------- | ----------------------- |
| `variable` | Variable\[Text\] | Variable to assign      |
| `number`   | Number           | Number to get character |
<h3 id=set_variable_to_hsb>
  <code>variable::to_hsb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create HSB Color\
**Type:** An action that returns a value\
**Description:** Creates a HEX color based on hue, saturation and lightness.

**Usage example:** 
```ts
`variable` = variable::to_hsb(1, 2, 3);

//Or dry by positionals

variable::to_hsb(`variable`, 1, 2, 3);

//Or dry by keywords

variable::to_hsb(variable=`variable`, hue=1, saturation=2, brightness=3);
```

**Arguments:**

| **Name**     | **Type**         | **Description**      |
| ------------ | ---------------- | -------------------- |
| `variable`   | Variable\[Text\] | Variable to assign   |
| `hue`        | Number           | Hue (0 - 360)        |
| `saturation` | Number           | Saturation (0 - 100) |
| `brightness` | Number           | Brightness (0 - 100) |
<h3 id=set_variable_to_hsl>
  <code>variable::to_hsl</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create HSL Color\
**Type:** An action that returns a value\
**Description:** Creates a HEX color based on Hue, Saturation and Lightness.

**Usage example:** 
```ts
`variable` = variable::to_hsl(1, 2, 3);

//Or dry by positionals

variable::to_hsl(`variable`, 1, 2, 3);

//Or dry by keywords

variable::to_hsl(variable=`variable`, hue=1, saturation=2, lightness=3);
```

**Arguments:**

| **Name**     | **Type**         | **Description**      |
| ------------ | ---------------- | -------------------- |
| `variable`   | Variable\[Text\] | Variable to assign   |
| `hue`        | Number           | Hue (0 - 360)        |
| `saturation` | Number           | Saturation (0 - 100) |
| `lightness`  | Number           | Lightness (0 - 100)  |
<h3 id=set_variable_to_json>
  <code>variable::to_json</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Convert To JSON\
**Type:** An action that returns a value\
**Description:** Converts dictionaries and lists to JSON text.

**Usage example:** 
```ts
`variable` = variable::to_json("any value", "FALSE");

//Or dry by positionals

variable::to_json(`variable`, "any value", "FALSE");

//Or dry by keywords

variable::to_json(variable=`variable`, value="any value", pretty_print="FALSE");
```

**Arguments:**

| **Name**       | **Type**                                             | **Description**             |
| -------------- | ---------------------------------------------------- | --------------------------- |
| `variable`     | Variable\[Any Value\]                                | To write result             |
| `value`        | Any Value                                            | List/Dictionary with values |
| `pretty_print` | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable | Format Pretty Print         |
<h3 id=set_variable_to_rgb>
  <code>variable::to_rgb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create RGB Color\
**Type:** An action that returns a value\
**Description:** Creates a HEX color based on the red, green and blue channels.

**Usage example:** 
```ts
`variable` = variable::to_rgb(1, 2, 3);

//Or dry by positionals

variable::to_rgb(`variable`, 1, 2, 3);

//Or dry by keywords

variable::to_rgb(variable=`variable`, red=1, green=2, blue=3);
```

**Arguments:**

| **Name**   | **Type**         | **Description**         |
| ---------- | ---------------- | ----------------------- |
| `variable` | Variable\[Text\] | Variable to assign      |
| `red`      | Number           | Red Channel (0 - 255)   |
| `green`    | Number           | Green Channel (0 - 255) |
| `blue`     | Number           | Blue channel (0 - 255)  |
<h3 id=set_variable_trim_list>
  <code>variable::trim_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Trim List\
**Type:** An action that returns a value\
**Description:** Returns a list containing the elements of the specified list that start and end at the specified indexes.

**Usage example:** 
```ts
`variable` = variable::trim_list(`list`, 1, 2);

//Or from the object

`variable` = `list`.trim_list(1, 2);

//Or dry by positionals

variable::trim_list(`variable`, `list`, 1, 2);

//Or dry by keywords

variable::trim_list(variable=`variable`, list=`list`, start=1, end=2);
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[List\] | Variable to assign |
| `list`     | List             | List               |
| `start`    | Number           | Start Index        |
| `end`      | Number           | End index          |
<h3 id=set_variable_trim_text>
  <code>variable::trim_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Trim Text\
**Type:** An action that returns a value\
**Description:** Trims text and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::trim_text("text", 1, 2);

//Or from the object

`variable` = "text".trim_text(1, 2);

//Or dry by positionals

variable::trim_text(`variable`, "text", 1, 2);

//Or dry by keywords

variable::trim_text(variable=`variable`, text="text", start=1, end=2);
```

**Arguments:**

| **Name**   | **Type**         | **Description** |
| ---------- | ---------------- | --------------- |
| `variable` | Variable\[Text\] | Variable to set |
| `text`     | Text             | Text to Trim    |
| `start`    | Number           | Start Position  |
| `end`      | Number           | End Position    |
<h3 id=set_variable_unset_item_components>
  <code>variable::unset_item_components</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
`variable` = variable::unset_item_components(item("stick"), ["components", "components"]);

//Or from the object

`variable` = item("stick").unset_item_components(["components", "components"]);

//Or dry by positionals

variable::unset_item_components(`variable`, item("stick"), ["components", "components"]);

//Or dry by keywords

variable::unset_item_components(variable=`variable`, item=item("stick"), components=["components", "components"]);
```

**Arguments:**

| **Name**     | **Type**         | **Description** |
| ------------ | ---------------- | --------------- |
| `variable`   | Variable\[Item\] | None            |
| `item`       | Item             | None            |
| `components` | list\[Text\]     | None            |
<h3 id=set_variable_value>
  <code>variable::set_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Value (=)\
**Type:** An action that returns a value\
**Description:** Assigns a value to a variable.

**Usage example:** 
```ts
`variable` = variable::set_value("any value");

//Or dry by positionals

variable::set_value(`variable`, "any value");

//Or dry by keywords

variable::set_value(variable=`variable`, value="any value");
```

**Arguments:**

| **Name**   | **Type**              | **Description**    |
| ---------- | --------------------- | ------------------ |
| `variable` | Variable\[Any Value\] | Variable to assign |
| `value`    | Any Value             | Value to assign    |
<h3 id=set_variable_vector>
  <code>variable::set_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Vector\
**Type:** An action that returns a value\
**Description:** Creates a vector from the specified coordinates and assigns the result to a variable.

**Usage example:** 
```ts
`variable` = variable::set_vector(1, 2, 3);

//Or dry by positionals

variable::set_vector(`variable`, 1, 2, 3);

//Or dry by keywords

variable::set_vector(variable=`variable`, x=1, y=2, z=3);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Vector\] | Variable to assign |
| `x`        | Number             | X Coordinate       |
| `y`        | Number             | Y Coordinate       |
| `z`        | Number             | Z Coordinate       |
<h3 id=set_variable_vector_cross_product>
  <code>variable::vector_cross_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Vector Product Of Two Vectors\
**Type:** An action that returns a value\
**Description:** Sets the cross product of two vectors to a variable.

**Usage example:** 
```ts
`variable` = variable::vector_cross_product(vector(0,0,0), vector(0,0,0));

//Or dry by positionals

variable::vector_cross_product(`variable`, vector(0,0,0), vector(0,0,0));

//Or dry by keywords

variable::vector_cross_product(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Vector\] | Variable to assign |
| `vector_1` | Vector             | First Vector       |
| `vector_2` | Vector             | Second Vector      |
<h3 id=set_variable_vector_dot_product>
  <code>variable::vector_dot_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dot Product Of Two Vectors\
**Type:** An action that returns a value\
**Description:** Sets the dot product of two vectors to a variable.

**Usage example:** 
```ts
`variable` = variable::vector_dot_product(vector(0,0,0), vector(0,0,0));

//Or dry by positionals

variable::vector_dot_product(`variable`, vector(0,0,0), vector(0,0,0));

//Or dry by keywords

variable::vector_dot_product(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `vector_1` | Vector             | First Vector       |
| `vector_2` | Vector             | Second Vector      |
<h3 id=set_variable_vector_to_direction_name>
  <code>variable::vector_to_direction_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Direction By Vector\
**Type:** An action that returns a value\
**Description:** Sets to variable which direction the vector is pointing.

**Usage example:** 
```ts
`variable` = variable::vector_to_direction_name(vector(0,0,0));

//Or from the object

`variable` = vector(0,0,0).vector_to_direction_name();

//Or dry by positionals

variable::vector_to_direction_name(`variable`, vector(0,0,0));

//Or dry by keywords

variable::vector_to_direction_name(variable=`variable`, vector=vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type**         | **Description**    |
| ---------- | ---------------- | ------------------ |
| `variable` | Variable\[Text\] | Variable to assign |
| `vector`   | Vector           | Vector to get      |
<h3 id=set_variable_voronoi_noise_3d>
  <code>variable::voronoi_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Voronoi Noise\
**Type:** An action that returns a value\
**Description:** Sets the value of the Voronoi noise at a specific location to a variable. Returns a number, with a value between 0 and 1.

**Usage example:** 
```ts
`variable` = variable::voronoi_noise_3d(location(0,0,0,0,0), 1, 2, 3, "FULL_RANGE", "FALSE");

//Or from the object

`variable` = location(0,0,0,0,0).voronoi_noise_3d(1, 2, 3, "FULL_RANGE", "FALSE");

//Or dry by positionals

variable::voronoi_noise_3d(`variable`, location(0,0,0,0,0), 1, 2, 3, "FULL_RANGE", "FALSE");

//Or dry by keywords

variable::voronoi_noise_3d(variable=`variable`, location=location(0,0,0,0,0), seed=1, frequency=2, displacement=3, range_mode="FULL_RANGE", enable_distance="FALSE");
```

**Arguments:**

| **Name**          | **Type**                                                         | **Description**       |
| ----------------- | ---------------------------------------------------------------- | --------------------- |
| `variable`        | Variable\[Number\]                                               | Variable to assign    |
| `location`        | Location                                                         | Location to set noise |
| `seed`            | Number                                                           | Noise Key             |
| `frequency`       | Number                                                           | Noise Frequency       |
| `displacement`    | Number                                                           | Noise Displacement    |
| `range_mode`      | Marker<br/>**FULL_RANGE** - -1 to 1<br/>**ZERO_TO_ONE** - 0 to 1 | Value Range           |
| `enable_distance` | Marker<br/>**FALSE** - Disable<br/>**TRUE** - Enable             | Distance Mode         |
<h3 id=set_variable_warp>
  <code>variable::wrap</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Wrap Number\
**Type:** An action that returns a value\
**Description:** Checks if a number is between two borders, and if not, wraps it around that border.

**Usage example:** 
```ts
`variable` = variable::wrap(1, 2, 3);

//Or from the object

`variable` = (1).wrap(2, 3);

//Or dry by positionals

variable::wrap(`variable`, 1, 2, 3);

//Or dry by keywords

variable::wrap(variable=`variable`, number=1, min=2, max=3);
```

**Arguments:**

| **Name**   | **Type**           | **Description**    |
| ---------- | ------------------ | ------------------ |
| `variable` | Variable\[Number\] | Variable to assign |
| `number`   | Number             | Number to wrap     |
| `min`      | Number             | Minimum Value      |
| `max`      | Number             | Max Value          |
