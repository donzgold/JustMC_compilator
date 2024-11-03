<h3 id=if_variable_dummy>
  <code>variable::is_dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action that checks the conditions\
**Description:** ...

**Usage example:** 
```ts
if(variable::is_dummy(){
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
if(variable::equals(["any value", "any value"],"any value"){
    player::message("Condition is true");
}

#Or from the object

if("any value".equals(["any value", "any value"]){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type**        | **Description**     |
| --------- | --------------- | ------------------- |
| `compare` | list[Any Value] | Compare Values      |
| `value`   | Any Value       | Comparison Variable |
<h3 id=if_variable_exists>
  <code>variable::exists</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Variable Exists\
**Type:** Action that checks the conditions\
**Description:** Checks if the selected variable exists.

**Usage example:** 
```ts
if(variable::exists(a1){
    player::message("Condition is true");
}

#Or from the object

if(a1.exists(){
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
if(variable::greater(1,2){
    player::message("Condition is true");
}

#Or from the object

if((1).greater(2){
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
if(variable::greater_or_equals(1,2){
    player::message("Condition is true");
}

#Or from the object

if((1).greater_or_equals(2){
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
if(variable::in_range("any value","any value","any value"){
    player::message("Condition is true");
}

#Or from the object

if("any value".in_range("any value","any value"){
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
**Description:** Checks if a variable's value type is equal to the specified one.

**Usage example:** 
```ts
if(variable::is_type("any value","NUMBER"){
    player::message("Condition is true");
}

#Or from the object

if("any value".is_type("NUMBER"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**        | **Type**                                                                                                                                                                                                                                           | **Description**   |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `value`         | Any Value                                                                                                                                                                                                                                          | Variable to check |
| `variable_type` | Marker<br/>**NUMBER** - Number<br/>**TEXT** - Text<br/>**LOCATION** - Location<br/>**ITEM** - Item<br/>**POTION** - Potion<br/>**SOUND** - Sound<br/>**PARTICLE** - Particle<br/>**VECTOR** - Vector<br/>**ARRAY** - List<br/>**MAP** - Dictionary | Variable Type     |
<h3 id=if_variable_item_equals>
  <code>variable::item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if an item variable is equal to at least one of the specified ones.

**Usage example:** 
```ts
if(variable::item_equals(item("stick"),[item("stick"), item("stick")],"EXACTLY"){
    player::message("Condition is true");
}

#Or from the object

if(item("stick").item_equals([item("stick"), item("stick")],"EXACTLY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                          | **Description**          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `value`           | Item                                                                                                                                                                                              | Item Variable to Compare |
| `compare`         | list[Item]                                                                                                                                                                                        | Compare Values           |
| `comparison_mode` | Marker<br/>**EXACTLY** - Full Comparison<br/>**TYPE_ONLY** - Item type only<br/>**IGNORE_STACK_SIZE** - Ignore quantity<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Ignore Quantity and Durability | Comparison Mode          |
<h3 id=if_variable_item_has_enchantment>
  <code>variable::item_has_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Has Enchantment\
**Type:** Action that checks the conditions\
**Description:** Checks whether the subject variable is the specified enchanting of a certain level.

**Usage example:** 
```ts
if(variable::item_has_enchantment(item("stick"),"enchant",1){
    player::message("Condition is true");
}

#Or from the object

if(item("stick").item_has_enchantment("enchant",1){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type** | **Description**  |
| --------- | -------- | ---------------- |
| `item`    | Item     | Subject variable |
| `enchant` | Text     | Furning key      |
| `level`   | Number   | Level            |
<h3 id=if_variable_item_has_tag>
  <code>variable::item_has_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Has Custom Tag\
**Type:** Action that checks the conditions\
**Description:** Checks if an item variable has the specified tag with the selected value.

**Usage example:** 
```ts
if(variable::item_has_tag(item("stick"),"tag","value","EQUALS"){
    player::message("Condition is true");
}

#Or from the object

if(item("stick").item_has_tag("tag","value","EQUALS"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**       | **Type**                                                                                                                                   | **Description**    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| `item`         | Item                                                                                                                                       | Item Variable      |
| `tag`          | Text                                                                                                                                       | Tag name           |
| `value`        | Text                                                                                                                                       | Tag Value          |
| `compare_type` | Marker<br/>**EQUALS** - Accurate correspondence<br/>**CONTAINS** - Contains<br/>**STARTS_WITH** - It begins on<br/>**ENDS_WITH** - Ends on | Type of comparison |
<h3 id=if_variable_less>
  <code>variable::less</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Less\
**Type:** Action that checks the conditions\
**Description:** Checks if a numeric variable is less than the specified value.

**Usage example:** 
```ts
if(variable::less(1,2){
    player::message("Condition is true");
}

#Or from the object

if((1).less(2){
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
if(variable::less_or_equals(1,2){
    player::message("Condition is true");
}

#Or from the object

if((1).less_or_equals(2){
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
if(variable::list_contains_value(["any value", "any value"],`list`,"ANY"){
    player::message("Condition is true");
}

#Or from the object

if(`list`.list_contains_value(["any value", "any value"],"ANY"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                | **Description** |
| ------------ | ------------------------------------------------------- | --------------- |
| `values`     | list[Any Value]                                         | Values to Check |
| `list`       | List                                                    | List to check   |
| `check_mode` | Marker<br/>**ANY** - Any Value<br/>**ALL** - All Values | Check Mode      |
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
&nbsp;&nbsp;Dictionaries

**Usage example:** 
```ts
if(variable::list_is_empty("any value"){
    player::message("Condition is true");
}

#Or from the object

if("any value".list_is_empty(){
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
if(variable::list_value_equals(`list`,["any value", "any value"],1){
    player::message("Condition is true");
}

#Or from the object

if(`list`.list_value_equals(["any value", "any value"],1){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**        | **Description**   |
| -------- | --------------- | ----------------- |
| `list`   | List            | List to check     |
| `values` | list[Any Value] | Comparable Values |
| `index`  | Number          | Value index       |
<h3 id=if_variable_location_in_range>
  <code>variable::location_in_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Location In Range\
**Type:** Action that checks the conditions\
**Description:** Checks if the location is in the specified range.

**Usage example:** 
```ts
if(variable::location_in_range(location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),"EXACT"){
    player::message("Condition is true");
}

#Or from the object

if(location(0,0,0,0,0).location_in_range(location(0,0,0,0,0),location(0,0,0,0,0),"EXACT"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                          | **Description**        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `value`           | Location                                                                                                                                          | Location to check      |
| `min`             | Location                                                                                                                                          | First corner of region |
| `max`             | Location                                                                                                                                          | Second Region Angle    |
| `border_handling` | Marker<br/>**EXACT** - Exact Coordinates<br/>**BLOCK** - Round to Block Coordinates<br/>**FULL_BLOCK_RANGE** - Round to min. and max. block angle | Check Mode             |
<h3 id=if_variable_location_is_near>
  <code>variable::location_is_near</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Near Location\
**Type:** Action that checks the conditions\
**Description:** Checks if a location variable is near the specified location.

**Usage example:** 
```ts
if(variable::location_is_near([location(0,0,0,0,0), location(0,0,0,0,0)],location(0,0,0,0,0),1,"SPHERE"){
    player::message("Condition is true");
}

#Or from the object

if(location(0,0,0,0,0).location_is_near([location(0,0,0,0,0), location(0,0,0,0,0)],1,"SPHERE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**   | **Type**                                                                                           | **Description**       |
| ---------- | -------------------------------------------------------------------------------------------------- | --------------------- |
| `check`    | list[Location]                                                                                     | Shape Center Location |
| `location` | Location                                                                                           | Location to check     |
| `radius`   | Number                                                                                             | Check Radius          |
| `shape`    | Marker<br/>**SPHERE** - Sphere<br/>**CIRCLE** - Circle<br/>**CUBE** - Cube<br/>**SQUARE** - Square | Shape                 |
<h3 id=if_variable_map_has_key>
  <code>variable::map_has_key</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dictionary Has Key\
**Type:** Action that checks the conditions\
**Description:** Checks if a dictionary has a specific key.

**Usage example:** 
```ts
if(variable::map_has_key(`map`,"any value"){
    player::message("Condition is true");
}

#Or from the object

if(`map`.map_has_key("any value"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**   | **Description**     |
| -------- | ---------- | ------------------- |
| `map`    | Dictionary | Dictionary to check |
| `key`    | Any Value  | Key                 |
<h3 id=if_variable_map_value_equals>
  <code>variable::map_value_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dictionary Value Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the value of a dictionary element by key is equal to at least one value being compared.

**Usage example:** 
```ts
if(variable::map_value_equals(`map`,["any value", "any value"],"any value"){
    player::message("Condition is true");
}

#Or from the object

if(`map`.map_value_equals(["any value", "any value"],"any value"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name** | **Type**        | **Description**     |
| -------- | --------------- | ------------------- |
| `map`    | Dictionary      | Dictionary to check |
| `values` | list[Any Value] | Comparable Values   |
| `key`    | Any Value       | Key                 |
<h3 id=if_variable_not_equals>
  <code>variable::not_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Not Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a variable is equal to at least one of the values being compared.

**Usage example:** 
```ts
if(variable::not_equals(["any value", "any value"],"any value"){
    player::message("Condition is true");
}

#Or from the object

if("any value".not_equals(["any value", "any value"]){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**  | **Type**        | **Description**     |
| --------- | --------------- | ------------------- |
| `compare` | list[Any Value] | Compare Values      |
| `value`   | Any Value       | Comparable Variable |
<h3 id=if_variable_range_intersects_range>
  <code>variable::range_intersects_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Range Intersects Range\
**Type:** Action that checks the conditions\
**Description:** Checks whether one region intersects with another.

**Usage example:** 
```ts
if(variable::range_intersects_range(location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),"OVERLAPS"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**     | **Type**                                                         | **Description**                        |
| ------------ | ---------------------------------------------------------------- | -------------------------------------- |
| `min1`       | Location                                                         | The first corner of the first region   |
| `max1`       | Location                                                         | The second corner of the first region  |
| `min2`       | Location                                                         | The first corner of the second region  |
| `max2`       | Location                                                         | The second corner of the second region |
| `check_type` | Marker<br/>**OVERLAPS** - Intersects<br/>**CONTAINS** - Contains | Type of verification                   |
<h3 id=if_variable_text_contains>
  <code>variable::text_contains</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Text Contains\
**Type:** Action that checks the conditions\
**Description:** Checks if a text variable contains the specified text.

**Usage example:** 
```ts
if(variable::text_contains("value",["compare", "compare"],"TRUE"){
    player::message("Condition is true");
}

#Or from the object

if("value".text_contains(["compare", "compare"],"TRUE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**      | **Type**                                       | **Description**   |
| ------------- | ---------------------------------------------- | ----------------- |
| `value`       | Text                                           | Variable to check |
| `compare`     | list[Text]                                     | Text to check     |
| `ignore_case` | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None | Ignore case       |
<h3 id=if_variable_text_ends_with>
  <code>variable::text_ends_with</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Text Ends With\
**Type:** Action that checks the conditions\
**Description:** Checks if a text variable ends with the specified text.

**Usage example:** 
```ts
if(variable::text_ends_with("value",["compare", "compare"],"TRUE"){
    player::message("Condition is true");
}

#Or from the object

if("value".text_ends_with(["compare", "compare"],"TRUE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**      | **Type**                                     | **Description**       |
| ------------- | -------------------------------------------- | --------------------- |
| `value`       | Text                                         | Text variable to test |
| `compare`     | list[Text]                                   | Compare Text          |
| `ignore_case` | Marker<br/>**TRUE** - Yes<br/>**FALSE** - No | Ignore case           |
<h3 id=if_variable_text_matches>
  <code>variable::text_matches</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Text Matches\
**Type:** Action that checks the conditions\
**Description:** Checks if a text variable matches the specified text or regular expression (RegEx).

**Usage example:** 
```ts
if(variable::text_matches("match",["values", "values"],"TRUE","TRUE"){
    player::message("Condition is true");
}

#Or from the object

if("match".text_matches(["values", "values"],"TRUE","TRUE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**              | **Type**                                                      | **Description**            |
| --------------------- | ------------------------------------------------------------- | -------------------------- |
| `match`               | Text                                                          | Text or Regular Expression |
| `values`              | list[Text]                                                    | Text Variables to Validate |
| `regular_expressions` | Marker<br/>**TRUE** - Regular Expression<br/>**FALSE** - Text | Validation Method          |
| `ignore_case`         | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None                | Ignore case                |
<h3 id=if_variable_text_starts_with>
  <code>variable::text_starts_with</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Text Starts With\
**Type:** Action that checks the conditions\
**Description:** Checks if a text variable starts with the specified text.

**Usage example:** 
```ts
if(variable::text_starts_with("value",["compare", "compare"],"TRUE"){
    player::message("Condition is true");
}

#Or from the object

if("value".text_starts_with(["compare", "compare"],"TRUE"){
    player::message("Condition is true");
}
```

**Arguments:**

| **Name**      | **Type**                                     | **Description**       |
| ------------- | -------------------------------------------- | --------------------- |
| `value`       | Text                                         | Text variable to test |
| `compare`     | list[Text]                                   | Compare Text          |
| `ignore_case` | Marker<br/>**TRUE** - Yes<br/>**FALSE** - No | Ignore Case           |
<h3 id=set_variable_absolute>
  <code>variable::absolute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Absolute Value\
**Type:** An action that returns a value\
**Description:** Sets the modulus of the selected number to a variable.

**Usage example:** 
```ts
a1 = variable::absolute(1);

#Or from the object

a1 = (1).absolute();

#Or dry

variable::absolute(a1,1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `number`   | Number   | Module Number      |
<h3 id=set_variable_add>
  <code>variable::add</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Addition (+)\
**Type:** An action that returns a value\
**Description:** Assigns a sum of numbers to a variable.

**Usage example:** 
```ts
a1 = variable::add([1, 2]);

#Or dry

variable::add(a1,[1, 2]);
```

**Arguments:**

| **Name**   | **Type**     | **Description**    |
| ---------- | ------------ | ------------------ |
| `variable` | Variable     | Variable to assign |
| `value`    | list[Number] | Numbers to Add     |
<h3 id=set_variable_add_item_enchantment>
  <code>variable::add_item_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Enchantment To an Item\
**Type:** An action that returns a value\
**Description:** Adds an enchantment to an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::add_item_enchantment(item("stick"),"enchantment",1);

#Or from the object

a1 = item("stick").add_item_enchantment("enchantment",1);

#Or dry

variable::add_item_enchantment(a1,item("stick"),"enchantment",1);
```

**Arguments:**

| **Name**      | **Type** | **Description**    |
| ------------- | -------- | ------------------ |
| `variable`    | Variable | Variable to assign |
| `item`        | Item     | Item               |
| `enchantment` | Text     | Enchant ID         |
| `level`       | Number   | Enchant Level      |
<h3 id=set_variable_add_item_potion_effects>
  <code>variable::add_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Potion Effects\
**Type:** An action that returns a value\
**Description:** Sets the potion effects of an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::add_item_potion_effects([potion("slow_falling"), potion("slow_falling")],item("stick"),"TRUE","TRUE","REGULAR");

#Or from the object

a1 = item("stick").add_item_potion_effects([potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");

#Or dry

variable::add_item_potion_effects(a1,[potion("slow_falling"), potion("slow_falling")],item("stick"),"TRUE","TRUE","REGULAR");
```

**Arguments:**

| **Name**        | **Type**                                                                       | **Description**            |
| --------------- | ------------------------------------------------------------------------------ | -------------------------- |
| `variable`      | Variable                                                                       | Variable to assign         |
| `potions`       | list[Potion]                                                                   | Potion Effects             |
| `item`          | Item                                                                           | Item                       |
| `overwrite`     | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None                                 | Overwrite existing effects |
| `show_icon`     | Marker<br/>**TRUE** - Yes<br/>**FALSE** - None                                 | Show Effect Icon           |
| `particle_mode` | Marker<br/>**REGULAR** - Yes<br/>**AMBIENT** - Transparent<br/>**NONE** - None | Show Particles             |
<h3 id=set_variable_add_vectors>
  <code>variable::add_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sum Of Vectors\
**Type:** An action that returns a value\
**Description:** Sets the sum of vectors value to a variable.

**Usage example:** 
```ts
a1 = variable::add_vectors([vector(0,0,0), vector(0,0,0)]);

#Or dry

variable::add_vectors(a1,[vector(0,0,0), vector(0,0,0)]);
```

**Arguments:**

| **Name**   | **Type**     | **Description**    |
| ---------- | ------------ | ------------------ |
| `variable` | Variable     | Variable to assign |
| `vectors`  | list[Vector] | Vectors to Add     |
<h3 id=set_variable_align_location>
  <code>variable::align_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Round Location\
**Type:** An action that returns a value\
**Description:** Rounds the location to the center or corner of the block and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::align_location(location(0,0,0,0,0),"KEEP","ALL","BLOCK_CENTER");

#Or from the object

a1 = location(0,0,0,0,0).align_location("KEEP","ALL","BLOCK_CENTER");

#Or dry

variable::align_location(a1,location(0,0,0,0,0),"KEEP","ALL","BLOCK_CENTER");
```

**Arguments:**

| **Name**           | **Type**                                                                                        | **Description**    |
| ------------------ | ----------------------------------------------------------------------------------------------- | ------------------ |
| `variable`         | Variable                                                                                        | Variable to assign |
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
a1 = variable::align_to_axis_vector(vector(0,0,0),"TRUE");

#Or from the object

a1 = vector(0,0,0).align_to_axis_vector("TRUE");

#Or dry

variable::align_to_axis_vector(a1,vector(0,0,0),"TRUE");
```

**Arguments:**

| **Name**    | **Type**                                                         | **Description**       |
| ----------- | ---------------------------------------------------------------- | --------------------- |
| `variable`  | Variable                                                         | Variable to assign    |
| `vector`    | Vector                                                           | Vector to align       |
| `normalize` | Marker<br/>**TRUE** - Normalized<br/>**FALSE** - Original Length | Vector type to output |
<h3 id=set_variable_append_component>
  <code>variable::append_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Append Stylized Texts\
**Type:** An action that returns a value\
**Description:** Combines these stylized texts into a single stylized text and assigns the result to the variable.

**Usage example:** 
```ts
a1 = variable::append_component(["components", "components"],"SPACES");

#Or dry

variable::append_component(a1,["components", "components"],"SPACES");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                         | **Description**              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `variable`   | Variable                                                                                                                         | Variable for appropriation   |
| `components` | list[Text]                                                                                                                       | Stylized texts for combining |
| `merging`    | Marker<br/>**SPACES** - Separation with a gap<br/>**CONCATENATION** - Association<br/>**SEPARATE_LINES** - Separation into lines | The combination of the text  |
<h3 id=set_variable_append_list>
  <code>variable::append_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Combine Two Lists\
**Type:** An action that returns a value\
**Description:** Combines two specified lists into one.

**Usage example:** 
```ts
a1 = variable::append_list(`list_1`,`list_2`);

#Or from the object

a1 = `list_1`.append_list(`list_2`);

#Or dry

variable::append_list(a1,`list_1`,`list_2`);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to Assign |
| `list_1`   | List     | First List         |
| `list_2`   | List     | Second List        |
<h3 id=set_variable_append_map>
  <code>variable::append_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Combine Dictionaries\
**Type:** An action that returns a value\
**Description:** Concatenates two dictionaries and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::append_map(`map`,`other_map`);

#Or from the object

a1 = `map`.append_map(`other_map`);

#Or dry

variable::append_map(a1,`map`,`other_map`);
```

**Arguments:**

| **Name**    | **Type**   | **Description**    |
| ----------- | ---------- | ------------------ |
| `variable`  | Variable   | Variable to Assign |
| `map`       | Dictionary | First Dictionary   |
| `other_map` | Dictionary | Second Dictionary  |
<h3 id=set_variable_append_value>
  <code>variable::append_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add List Value\
**Type:** Action without value\
**Description:** Adds the specified values to the end of the list.

**Usage example:** 
```ts
variable::append_value(a1,["any value", "any value"]);

#Or from the object

a1.append_value(["any value", "any value"]);
```

**Arguments:**

| **Name**   | **Type**        | **Description** |
| ---------- | --------------- | --------------- |
| `variable` | Variable        | List            |
| `values`   | list[Any Value] | Values          |
<h3 id=set_variable_average>
  <code>variable::average</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Average\
**Type:** An action that returns a value\
**Description:** Sets the average of numbers to a variable.

**Usage example:** 
```ts
a1 = variable::average([1, 2]);

#Or dry

variable::average(a1,[1, 2]);
```

**Arguments:**

| **Name**   | **Type**     | **Description**      |
| ---------- | ------------ | -------------------- |
| `variable` | Variable     | Variable to assign   |
| `value`    | list[Number] | Numbers to get value |
<h3 id=set_variable_bitwise_operation>
  <code>variable::bitwise_operation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Bitwise Operation on Numbers\
**Type:** An action that returns a value\
**Description:** Sets the result of a bitwise operation on numbers to a variable.

**Usage example:** 
```ts
a1 = variable::bitwise_operation(1,2,"OR");

#Or dry

variable::bitwise_operation(a1,1,2,"OR");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                                                                                                                                                    | **Description**    |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable                                                                                                                                                                                                                                                                    | Variable to assign |
| `operand1` | Number                                                                                                                                                                                                                                                                      | First operand      |
| `operand2` | Number                                                                                                                                                                                                                                                                      | Second Operand     |
| `operator` | Marker<br/>**OR** - OR (or)<br/>**AND** - And (and)<br/>**NOT** - NOT (not)<br/>**XOR** - XOR (xor)<br/>**LEFT_SHIFT** - Shift Left (left_shift)<br/>**RIGHT_SHIFT** - Shift Right (right_shift)<br/>**UNSIGNED_RIGHT_SHIFT** - Unsigned Right Shift (unsigned_right_shift) | Operation Type     |
<h3 id=set_variable_center_location>
  <code>variable::center_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Center Location\
**Type:** An action that returns a value\
**Description:** Sets the location to the center between other locations and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::center_location([location(0,0,0,0,0), location(0,0,0,0,0)]);

#Or dry

variable::center_location(a1,[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

**Arguments:**

| **Name**    | **Type**       | **Description**    |
| ----------- | -------------- | ------------------ |
| `variable`  | Variable       | Variable to assign |
| `locations` | list[Location] | Locations to Set   |
<h3 id=set_variable_change_component_parsing>
  <code>variable::change_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Change Stylized Text Parsing\
**Type:** An action that returns a value\
**Description:** Changes the type of transformation for the specified stylized text.

**Usage example:** 
```ts
a1 = variable::change_component_parsing("component","PLAIN");

#Or from the object

a1 = "component".change_component_parsing("PLAIN");

#Or dry

variable::change_component_parsing(a1,"component","PLAIN");
```

**Arguments:**

| **Name**    | **Type**                                                                                                       | **Description**                |
| ----------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `variable`  | Variable                                                                                                       | Variable for appropriation     |
| `component` | Text                                                                                                           | Stylized text for installation |
| `parsing`   | Marker<br/>**PLAIN** - Ordinary<br/>**LEGACY** - Color (&)<br/>**MINIMESSAGE** - Stylized<br/>**JSON** - Zhnon | Type of transformation         |
<h3 id=set_variable_char_to_number>
  <code>variable::char_to_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number By Character\
**Type:** An action that returns a value\
**Description:** Gets a specific number from a character and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::char_to_number("char");

#Or from the object

a1 = "char".char_to_number();

#Or dry

variable::char_to_number(a1,"char");
```

**Arguments:**

| **Name**   | **Type** | **Description**         |
| ---------- | -------- | ----------------------- |
| `variable` | Variable | Variable to assign      |
| `char`     | Text     | Character to get number |
<h3 id=set_variable_clamp>
  <code>variable::clamp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clamp Number\
**Type:** An action that returns a value\
**Description:** Checks if a number is between the minimum and maximum values, and if not, sets it to the closest.

**Usage example:** 
```ts
a1 = variable::clamp(1,2,3);

#Or from the object

a1 = (1).clamp(2,3);

#Or dry

variable::clamp(a1,1,2,3);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to Assign |
| `number`   | Number   | Number to Clamp    |
| `min`      | Number   | Minimum Value      |
| `max`      | Number   | Max Value          |
<h3 id=set_variable_clear_color_codes>
  <code>variable::clear_color_codes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Text Colors\
**Type:** An action that returns a value\
**Description:** Clears text from color codes and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::clear_color_codes("text");

#Or from the object

a1 = "text".clear_color_codes();

#Or dry

variable::clear_color_codes(a1,"text");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `text`     | Text     | Text to change     |
<h3 id=set_variable_clear_map>
  <code>variable::clear_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Dictionary\
**Type:** Action without value\
**Description:** Clears the dictionary.

**Usage example:** 
```ts
variable::clear_map(a1);

#Or from the object

a1.clear_map();
```

**Arguments:**

| **Name** | **Type** | **Description**     |
| -------- | -------- | ------------------- |
| `map`    | Variable | Dictionary to Clear |
<h3 id=set_variable_compact_component>
  <code>variable::compact_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Compact Stylized Text\
**Type:** An action that returns a value\
**Description:** Assigns to the variable the specified stylized text without elements of style and subsidiaries.

**Usage example:** 
```ts
a1 = variable::compact_component("component");

#Or from the object

a1 = "component".compact_component();

#Or dry

variable::compact_component(a1,"component");
```

**Arguments:**

| **Name**    | **Type** | **Description**            |
| ----------- | -------- | -------------------------- |
| `variable`  | Variable | Variable for appropriation |
| `component` | Text     | Compressed stylized text   |
<h3 id=set_variable_component_of_children>
  <code>variable::component_of_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create a stylized text from subsidiaries\
**Type:** An action that returns a value\
**Description:** Creates a stylized text from these subsidiaries of stylized texts and assigns the result to the variable.

**Usage example:** 
```ts
a1 = variable::component_of_children(["components", "components"]);

#Or dry

variable::component_of_children(a1,["components", "components"]);
```

**Arguments:**

| **Name**     | **Type**   | **Description**            |
| ------------ | ---------- | -------------------------- |
| `variable`   | Variable   | Variable for appropriation |
| `components` | list[Text] | Stylized texts             |
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
a1 = variable::convert_number_to_text(1,2);

#Or from the object

a1 = (1).convert_number_to_text(2);

#Or dry

variable::convert_number_to_text(a1,1,2);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `number`   | Number   | Number to convert  |
| `radix`    | Number   | Number Base        |
<h3 id=set_variable_convert_text_to_number>
  <code>variable::convert_text_to_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Convert Text To Number\
**Type:** An action that returns a value\
**Description:** Sets the result of converting text to number to a variable. Works only with integers.

**Usage example:** 
```ts
a1 = variable::convert_text_to_number("text",1);

#Or from the object

a1 = "text".convert_text_to_number(1);

#Or dry

variable::convert_text_to_number(a1,"text",1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `text`     | Text     | Text to convert    |
| `radix`    | Number   | Number Base        |
<h3 id=set_variable_cosine>
  <code>variable::cosine</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Cosine\
**Type:** An action that returns a value\
**Description:** Returns the cosine of a number.

**Usage example:** 
```ts
a1 = variable::cosine(1,"COSINE","DEGREES");

#Or from the object

a1 = (1).cosine("COSINE","DEGREES");

#Or dry

variable::cosine(a1,1,"COSINE","DEGREES");
```

**Arguments:**

| **Name**   | **Type**                                                                                                   | **Description**      |
| ---------- | ---------------------------------------------------------------------------------------------------------- | -------------------- |
| `variable` | Variable                                                                                                   | Variable to assign   |
| `number`   | Number                                                                                                     | Number to get cosine |
| `variant`  | Marker<br/>**COSINE** - Cosine<br/>**ARCCOSINE** - Arccosine<br/>**HYPERBOLIC_COSINE** - Hyperbolic Cosine | Operation Type       |
| `input`    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                                 | Corner Type          |
<h3 id=set_variable_cotangent>
  <code>variable::cotangent</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Cotangent\
**Type:** An action that returns a value\
**Description:** Returns the cotangent of a number.

**Usage example:** 
```ts
a1 = variable::cotangent(1,"COTANGENT","DEGREES");

#Or from the object

a1 = (1).cotangent("COTANGENT","DEGREES");

#Or dry

variable::cotangent(a1,1,"COTANGENT","DEGREES");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                     | **Description**         |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `variable` | Variable                                                                                                                     | Variable to assign      |
| `number`   | Number                                                                                                                       | Number to get cotangent |
| `variant`  | Marker<br/>**COTANGENT** - Cotangent<br/>**ARCCOTANGENT** - Arccotangent<br/>**HYPERBOLIC_COTANGENT** - Hyperbolic Cotangent | Operation Type          |
| `input`    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                                                   | Angle Type              |
<h3 id=set_variable_create_keybind_component>
  <code>variable::create_keybind_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Stylized Text With Key Binding\
**Type:** An action that returns a value\
**Description:** Assigns to the variable stylized text tied to the client key.

**Usage example:** 
```ts
a1 = variable::create_keybind_component("key");

#Or dry

variable::create_keybind_component(a1,"key");
```

**Arguments:**

| **Name**   | **Type** | **Description**            |
| ---------- | -------- | -------------------------- |
| `variable` | Variable | Variable for appropriation |
| `key`      | Text     | Keybind                    |
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
a1 = variable::create_list(["any value", "any value"]);

#Or dry

variable::create_list(a1,["any value", "any value"]);
```

**Arguments:**

| **Name**   | **Type**        | **Description**    |
| ---------- | --------------- | ------------------ |
| `variable` | Variable        | Variable to assign |
| `values`   | list[Any Value] | Values             |
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
a1 = variable::create_map(`keys`,`values`);

#Or dry

variable::create_map(a1,`keys`,`values`);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `keys`     | List     | List Keys          |
| `values`   | List     | List of Values     |
<h3 id=set_variable_create_map_from_values>
  <code>variable::create_map_from_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create a dictionary of meanings\
**Type:** An action that returns a value\
**Description:** Creates a dictionary from keys and meanings and assigns the result to the variable.\
**Additional info:**\
&nbsp;&nbsp;Cleans the dictionary if it already exists.

**Usage example:** 
```ts
a1 = variable::create_map_from_values(["any value", "any value"],["any value", "any value"]);

#Or dry

variable::create_map_from_values(a1,["any value", "any value"],["any value", "any value"]);
```

**Arguments:**

| **Name**   | **Type**        | **Description**            |
| ---------- | --------------- | -------------------------- |
| `variable` | Variable        | Variable for appropriation |
| `keys`     | list[Any Value] | Keys                       |
| `values`   | list[Any Value] | Meanings                   |
<h3 id=set_variable_create_translatable_component>
  <code>variable::create_translatable_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Translatable Stylized Text\
**Type:** An action that returns a value\
**Description:** Assigns to the variable the translated stylized text with the indicated arguments.

**Usage example:** 
```ts
a1 = variable::create_translatable_component(["args", "args"],"key");

#Or dry

variable::create_translatable_component(a1,["args", "args"],"key");
```

**Arguments:**

| **Name**   | **Type**   | **Description**            |
| ---------- | ---------- | -------------------------- |
| `variable` | Variable   | Variable for appropriation |
| `args`     | list[Text] | Arguments for inserting    |
| `key`      | Text       | Key                        |
<h3 id=set_variable_decrement>
  <code>variable::decrement</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Decrement (-=)\
**Type:** An action that returns a value\
**Description:** Subtracts the selected number from the variable.

**Usage example:** 
```ts
a1 = variable::decrement(1);

#Or dry

variable::decrement(a1,1);
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
a1 = variable::divide([1, 2],"DEFAULT");

#Or dry

variable::divide(a1,[1, 2],"DEFAULT");
```

**Arguments:**

| **Name**        | **Type**                                                                                                                               | **Description**    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`      | Variable                                                                                                                               | Variable to assign |
| `value`         | list[Number]                                                                                                                           | Numbers to Divide  |
| `division_mode` | Marker<br/>**DEFAULT** - Default<br/>**ROUND_TO_INT** - Round To Integer<br/>**FLOOR** - Round to less<br/>**CEIL** - Round up to more | Division Mode      |
<h3 id=set_variable_divide_vector>
  <code>variable::divide_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Vector Divide\
**Type:** An action that returns a value\
**Description:** Sets the result of dividing two vectors to a variable.

**Usage example:** 
```ts
a1 = variable::divide_vector(vector(0,0,0),vector(0,0,0));

#Or dry

variable::divide_vector(a1,vector(0,0,0),vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `vector`   | Vector   | Vector to change   |
| `divider`  | Vector   | Vector Divider     |
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

<h3 id=set_variable_face_location>
  <code>variable::face_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Location Face Another Location\
**Type:** An action that returns a value\
**Description:** Rotates a location in the direction of another location and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::face_location(location(0,0,0,0,0),location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).face_location(location(0,0,0,0,0));

#Or dry

variable::face_location(a1,location(0,0,0,0,0),location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `location` | Location | Locations to Set   |
| `target`   | Location | Target Location    |
<h3 id=set_variable_flatten_list>
  <code>variable::flatten_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Flatten List\
**Type:** An action that returns a value\
**Description:** Splits the sublists of the specified list into separate items.

**Usage example:** 
```ts
a1 = variable::flatten_list(`list`);

#Or from the object

a1 = `list`.flatten_list();

#Or dry

variable::flatten_list(a1,`list`);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `list`     | List     | List               |
<h3 id=set_variable_format_timestamp>
  <code>variable::format_timestamp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Time Format\
**Type:** An action that returns a value\
**Description:** Converts a number (milliseconds) to the specified time format and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::format_timestamp(1,"pattern","zone_id","locale","CUSTOM");

#Or from the object

a1 = (1).format_timestamp("pattern","zone_id","locale","CUSTOM");

#Or dry

variable::format_timestamp(a1,1,"pattern","zone_id","locale","CUSTOM");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Description**                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| `variable` | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Variable to assign                  |
| `time`     | Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Number to convert                   |
| `pattern`  | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Time Pattern (e.g. mm\:ss)          |
| `zone_id`  | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Timezone (GMT+1\.\.13, GMT-1\.\.13) |
| `locale`   | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Language (ru_RU, en_US...)          |
| `format`   | Marker<br/>**CUSTOM** - Custom<br/>**DD_MM_YYYY_HH_MM_S** - 01\/01\/1970 00\:00\:00 (dd_mm_yyyy_hh_mm_s)<br/>**DD_MM_YYYY** - 01\/01\/1970 (dd_mm_yyyy)<br/>**YYYY_MM_DD_HH_MM_S** - 1970\/01\/01 00\:00\:00 (yyyy_mm_dd_hh_mm_s)<br/>**YYYY_MM_DD** - 1970\/01\/01 (yyyy_mm_dd)<br/>**EEE_D_MMMM** - Thu, 01 January (eee_d_mmmm)<br/>**EEE_MMMM_D** - Thu, January 01 (eee_mmmm_d)<br/>**EEEE** - Thursday (eeee)<br/>**HH_MM_SS** - 00\:00\:00 (hh_mm_ss)<br/>**H_MM_A** - 00\:00 AM (h_mm_a)<br/>**H_H_M_M_S_S** - 00h00m00s (h_h_m_m_s_s)<br/>**S_S** - 00.00 (s_s) | Time Format                         |
<h3 id=set_variable_gaussian_distribution>
  <code>variable::gaussian_distribution</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Normally Distributed Random Number\
**Type:** An action that returns a value\
**Description:** Produces a random number close to the mean μ with a standard deviation σ with a chance given by a normal distribution plot.

**Usage example:** 
```ts
a1 = variable::gaussian_distribution(1,2,"NORMAL");

#Or dry

variable::gaussian_distribution(a1,1,2,"NORMAL");
```

**Arguments:**

| **Name**       | **Type**                                                                            | **Description**            |
| -------------- | ----------------------------------------------------------------------------------- | -------------------------- |
| `variable`     | Variable                                                                            | Variable to Assign         |
| `deviant`      | Number                                                                              | Deviation of σ from mean μ |
| `mean`         | Number                                                                              | Mean μ                     |
| `distribution` | Marker<br/>**NORMAL** - Total Deviation<br/>**FOLDER_NORMAL** - Side Deviation >= μ | Type of σ deviation        |
<h3 id=set_variable_get_all_block_data>
  <code>variable::get_all_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get All Block Data\
**Type:** An action that returns a value\
**Description:** Sets all block data at the selected location to a variable.

**Usage example:** 
```ts
a1 = variable::get_all_block_data(location(0,0,0,0,0),"TRUE");

#Or from the object

a1 = location(0,0,0,0,0).get_all_block_data("TRUE");

#Or dry

variable::get_all_block_data(a1,location(0,0,0,0,0),"TRUE");
```

**Arguments:**

| **Name**           | **Type**                                             | **Description**         |
| ------------------ | ---------------------------------------------------- | ----------------------- |
| `variable`         | Variable                                             | Variable to assign      |
| `location`         | Location                                             | Block Location          |
| `hide_unspecified` | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable | Hide Unspecified Values |
<h3 id=set_variable_get_all_coordinates>
  <code>variable::get_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get All Location Coordinates\
**Type:** An action that returns a value\
**Description:** Gets the value of all coordinates from a location and assigns them to variables.

**Usage example:** 
```ts
a1, a2, a3, a4, a5 = variable::get_all_coordinates(location(0,0,0,0,0));

#Or from the object

a1, a2, a3, a4, a5 = location(0,0,0,0,0).get_all_coordinates();

#Or dry

variable::get_all_coordinates(a1,a2,a3,a4,a5,location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**     |
| ---------- | -------- | ------------------- |
| `x`        | Variable | X Coordinate        |
| `y`        | Variable | Y Coordinate        |
| `z`        | Variable | Z Coordinate        |
| `yaw`      | Variable | Horizontal Rotation |
| `pitch`    | Variable | Pitch Vertical      |
| `location` | Location | Location to Get     |
<h3 id=set_variable_get_angle_between_vectors>
  <code>variable::get_angle_between_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Angle Between Two Vectors\
**Type:** An action that returns a value\
**Description:** Sets the angle between two vectors to a variable.

**Usage example:** 
```ts
a1 = variable::get_angle_between_vectors(vector(0,0,0),vector(0,0,0),"DEGREES");

#Or dry

variable::get_angle_between_vectors(a1,vector(0,0,0),vector(0,0,0),"DEGREES");
```

**Arguments:**

| **Name**      | **Type**                                                   | **Description**    |
| ------------- | ---------------------------------------------------------- | ------------------ |
| `variable`    | Variable                                                   | Variable to assign |
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
a1 = variable::get_block_custom_tag(location(0,0,0,0,0),"tag_name","tag_value","any value");

#Or dry

variable::get_block_custom_tag(a1,location(0,0,0,0,0),"tag_name","tag_value","any value");
```

**Arguments:**

| **Name**        | **Type**  | **Description** |
| --------------- | --------- | --------------- |
| `variable`      | Variable  | None            |
| `location`      | Location  | None            |
| `tag_name`      | Text      | None            |
| `tag_value`     | Text      | None            |
| `default_value` | Any Value | None            |
<h3 id=set_variable_get_block_data>
  <code>variable::get_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Block Data\
**Type:** An action that returns a value\
**Description:** Gets the block data and assigns it to a variable.

**Usage example:** 
```ts
a1 = variable::get_block_data(location(0,0,0,0,0),"tag_name");

#Or from the object

a1 = location(0,0,0,0,0).get_block_data("tag_name");

#Or dry

variable::get_block_data(a1,location(0,0,0,0,0),"tag_name");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `location` | Location | Block Location     |
| `tag_name` | Text     | Tag Name           |
<h3 id=set_variable_get_block_growth>
  <code>variable::get_block_growth</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Block Growth Level\
**Type:** An action that returns a value\
**Description:** Sets the block growth level at the specified location to a variable.

**Usage example:** 
```ts
a1 = variable::get_block_growth(location(0,0,0,0,0),"GROWTH_STAGE");

#Or from the object

a1 = location(0,0,0,0,0).get_block_growth("GROWTH_STAGE");

#Or dry

variable::get_block_growth(a1,location(0,0,0,0,0),"GROWTH_STAGE");
```

**Arguments:**

| **Name**      | **Type**                                                                                 | **Description**    |
| ------------- | ---------------------------------------------------------------------------------------- | ------------------ |
| `variable`    | Variable                                                                                 | Variable to assign |
| `location`    | Location                                                                                 | Block Location     |
| `growth_unit` | Marker<br/>**GROWTH_STAGE** - Growth Stage<br/>**GROWTH_PERCENTAGE** - Growth Percentage | Unit               |
<h3 id=set_variable_get_block_material>
  <code>variable::get_block_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Block Type\
**Type:** An action that returns a value\
**Description:** Sets the block type at the selected location to a variable.

**Usage example:** 
```ts
a1 = variable::get_block_material(location(0,0,0,0,0),"ID");

#Or from the object

a1 = location(0,0,0,0,0).get_block_material("ID");

#Or dry

variable::get_block_material(a1,location(0,0,0,0,0),"ID");
```

**Arguments:**

| **Name**     | **Type**                                                                                                               | **Description**    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable                                                                                                               | Variable to assign |
| `location`   | Location                                                                                                               | Block Location     |
| `value_type` | Marker<br/>**ID** - Block ID<br/>**ID_WITH_DATA** - ID and block data<br/>**NAME** - Block Name<br/>**ITEM** - As Item | Value Type         |
<h3 id=set_variable_get_block_material_property>
  <code>variable::get_block_material_property</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Block Property\
**Type:** An action that returns a value\
**Description:** Gets the specific block property and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_block_material_property(item("stone"),"HARDNESS");

#Or from the object

a1 = item("stone").get_block_material_property("HARDNESS");

#Or dry

variable::get_block_material_property(a1,item("stone"),"HARDNESS");
```

**Arguments:**

| **Name**   | **Type**                                                                                                           | **Description**    |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| `variable` | Variable                                                                                                           | Variable to assign |
| `block`    | Block                                                                                                              | Block to Get       |
| `property` | Marker<br/>**HARDNESS** - Hardness<br/>**BLAST_RESISTANCE** - Blast Resistance<br/>**SLIPPERINESS** - Slipperiness | Property           |
<h3 id=set_variable_get_block_power>
  <code>variable::get_block_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Redstone Power\
**Type:** An action that returns a value\
**Description:** Sets the redstone signal strength at the specified location to a variable.

**Usage example:** 
```ts
a1 = variable::get_block_power(location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).get_block_power();

#Or dry

variable::get_block_power(a1,location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `location` | Location | Block Location     |
<h3 id=set_variable_get_book_text>
  <code>variable::get_book_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Book Text\
**Type:** An action that returns a value\
**Description:** Sets the value of the book text on a specific page to a variable.

**Usage example:** 
```ts
a1 = variable::get_book_text(item("stick"),1);

#Or from the object

a1 = item("stick").get_book_text(1);

#Or dry

variable::get_book_text(a1,item("stick"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `book`     | Item     | Book to get value  |
| `page`     | Number   | Page Number        |
<h3 id=set_variable_get_brushable_block_item>
  <code>variable::get_brushable_block_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Suspicious Block Item\
**Type:** An action that returns a value\
**Description:** Get an item from a suspicious block (sand, gravel) and assign the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_brushable_block_item(location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).get_brushable_block_item();

#Or dry

variable::get_brushable_block_item(a1,location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `location` | Location | Block Location     |
<h3 id=set_variable_get_bundle_items>
  <code>variable::get_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Bundle Items\
**Type:** Action without value\
**Description:** He receives the contents of the bag and assigns the result to the variable.

**Usage example:** 
```ts
variable::get_bundle_items(a1,item("stick"));

#Or from the object

item("stick").get_bundle_items(a1);
```

**Arguments:**

| **Name**   | **Type** | **Description**            |
| ---------- | -------- | -------------------------- |
| `variable` | Variable | Variable for appropriation |
| `bundle`   | Item     | Bundle                     |
<h3 id=set_variable_get_char_at>
  <code>variable::get_char_at</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Character By Index\
**Type:** An action that returns a value\
**Description:** Get the character from the text at the specified index and assign the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_char_at("text",1);

#Or from the object

a1 = "text".get_char_at(1);

#Or dry

variable::get_char_at(a1,"text",1);
```

**Arguments:**

| **Name**   | **Type** | **Description**       |
| ---------- | -------- | --------------------- |
| `variable` | Variable | Variable to assign    |
| `text`     | Text     | Text to get character |
| `index`    | Number   | Index                 |
<h3 id=set_variable_get_color_channels>
  <code>variable::get_color_channels</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Color Channels\
**Type:** An action that returns a value\
**Description:** Gets RGB/HSB/HSL color numeric values as a list.

**Usage example:** 
```ts
a1 = variable::get_color_channels("color","RGB");

#Or from the object

a1 = "color".get_color_channels("RGB");

#Or dry

variable::get_color_channels(a1,"color","RGB");
```

**Arguments:**

| **Name**         | **Type**                                                     | **Description**    |
| ---------------- | ------------------------------------------------------------ | ------------------ |
| `variable`       | Variable                                                     | Variable to assign |
| `color`          | Text                                                         | Color to get value |
| `color_channels` | Marker<br/>**RGB** - RGB<br/>**HSB** - HSB<br/>**HSL** - HSL | Color Channel      |
<h3 id=set_variable_get_compass_lodestone>
  <code>variable::get_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Lodestone Location\
**Type:** An action that returns a value\
**Description:** Get the location of lodestone from a magnetized compass and assign the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_compass_lodestone(item("stick"));

#Or from the object

a1 = item("stick").get_compass_lodestone();

#Or dry

variable::get_compass_lodestone(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Magnetized Compass |
<h3 id=set_variable_get_component_children>
  <code>variable::get_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Stylized Text Children Components\
**Type:** An action that returns a value\
**Description:** Assigns to the variable the subsidiaries of the specified stylized text.

**Usage example:** 
```ts
a1 = variable::get_component_children("component");

#Or from the object

a1 = "component".get_component_children();

#Or dry

variable::get_component_children(a1,"component");
```

**Arguments:**

| **Name**    | **Type** | **Description**            |
| ----------- | -------- | -------------------------- |
| `variable`  | Variable | Variable for appropriation |
| `component` | Text     | Stylized text              |
<h3 id=set_variable_get_component_decorations>
  <code>variable::get_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Stylized Text Decorations\
**Type:** An action that returns a value\
**Description:** Assigns to the variable all the scenery (stylization) of the stylized text.

**Usage example:** 
```ts
a1 = variable::get_component_decorations("component");

#Or from the object

a1 = "component".get_component_decorations();

#Or dry

variable::get_component_decorations(a1,"component");
```

**Arguments:**

| **Name**    | **Type** | **Description**            |
| ----------- | -------- | -------------------------- |
| `variable`  | Variable | Variable for appropriation |
| `component` | Text     | Stylized text              |
<h3 id=set_variable_get_component_hex_color>
  <code>variable::get_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Stylized Text Hex Color\
**Type:** An action that returns a value\
**Description:** Assigns to the variable HEX-color of the specified stylized text.

**Usage example:** 
```ts
a1 = variable::get_component_hex_color("component");

#Or from the object

a1 = "component".get_component_hex_color();

#Or dry

variable::get_component_hex_color(a1,"component");
```

**Arguments:**

| **Name**    | **Type** | **Description**            |
| ----------- | -------- | -------------------------- |
| `variable`  | Variable | Variable for appropriation |
| `component` | Text     | Stylized text              |
<h3 id=set_variable_get_component_parsing>
  <code>variable::get_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Type Stylized Text Parsing\
**Type:** An action that returns a value\
**Description:** Assigns to the variable value of the type of transformation of the specified stylized text.

**Usage example:** 
```ts
a1 = variable::get_component_parsing("component");

#Or from the object

a1 = "component".get_component_parsing();

#Or dry

variable::get_component_parsing(a1,"component");
```

**Arguments:**

| **Name**    | **Type** | **Description**            |
| ----------- | -------- | -------------------------- |
| `variable`  | Variable | Variable for appropriation |
| `component` | Text     | The initial stylized text  |
<h3 id=set_variable_get_container_contents>
  <code>variable::get_container_contents</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Container Contents\
**Type:** An action that returns a value\
**Description:** Sets a list of container contents at the selected location to a variable.

**Usage example:** 
```ts
a1 = variable::get_container_contents(location(0,0,0,0,0),"TRUE");

#Or from the object

a1 = location(0,0,0,0,0).get_container_contents("TRUE");

#Or dry

variable::get_container_contents(a1,location(0,0,0,0,0),"TRUE");
```

**Arguments:**

| **Name**             | **Type**                                                  | **Description**    |
| -------------------- | --------------------------------------------------------- | ------------------ |
| `variable`           | Variable                                                  | Variable to assign |
| `location`           | Location                                                  | Container Location |
| `ignore_empty_slots` | Marker<br/>**TRUE** - Ignore<br/>**FALSE** - Don't Ignore | Ignore Empty Slots |
<h3 id=set_variable_get_container_lock>
  <code>variable::get_container_lock</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Container Key\
**Type:** An action that returns a value\
**Description:** Sets a container key item at the specified location to a variable.

**Usage example:** 
```ts
a1 = variable::get_container_lock(location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).get_container_lock();

#Or dry

variable::get_container_lock(a1,location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `location` | Location | Block Location     |
<h3 id=set_variable_get_container_name>
  <code>variable::get_container_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Container Name\
**Type:** An action that returns a value\
**Description:** Sets the variable to the name of the container at the selected location.

**Usage example:** 
```ts
a1 = variable::get_container_name(location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).get_container_name();

#Or dry

variable::get_container_name(a1,location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `location` | Location | Container Location |
<h3 id=set_variable_get_coordinate>
  <code>variable::get_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Location Coordinate\
**Type:** An action that returns a value\
**Description:** Gets the value of the selected coordinate from the location and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_coordinate(location(0,0,0,0,0),"X");

#Or from the object

a1 = location(0,0,0,0,0).get_coordinate("X");

#Or dry

variable::get_coordinate(a1,location(0,0,0,0,0),"X");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                            | **Description**       |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `variable` | Variable                                                                                                                            | Variable to assign    |
| `location` | Location                                                                                                                            | Location to get value |
| `type`     | Marker<br/>**X** - X Axis<br/>**Y** - Y Axis<br/>**Z** - Z Axis<br/>**PITCH** - Horizontal Rotation<br/>**YAW** - Vertical rotation | Coordinate Type       |
<h3 id=set_variable_get_decorate_pot_sherd>
  <code>variable::get_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Decorate Pot Sherd\
**Type:** An action that returns a value\
**Description:** It assigns to the variable material the bar of the selected side of the jug in the indicated location.

**Usage example:** 
```ts
a1 = variable::get_decorate_pot_sherd(location(0,0,0,0,0),"BACK");

#Or from the object

a1 = location(0,0,0,0,0).get_decorate_pot_sherd("BACK");

#Or dry

variable::get_decorate_pot_sherd(a1,location(0,0,0,0,0),"BACK");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                       | **Description**            |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| `variable` | Variable                                                                                                                       | Variable for appropriation |
| `location` | Location                                                                                                                       | The location of the jug    |
| `side`     | Marker<br/>**BACK** - The back side<br/>**LEFT** - The left side<br/>**RIGHT** - The right side<br/>**FRONT** - The front side | Side of the jug            |
<h3 id=set_variable_get_index_of_subtext>
  <code>variable::get_index_of_subtext</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Subtext Index\
**Type:** An action that returns a value\
**Description:** Gets the subtext index from the text and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_index_of_subtext("text","subtext",1,"FIRST");

#Or from the object

a1 = "text".get_index_of_subtext("subtext",1,"FIRST");

#Or dry

variable::get_index_of_subtext(a1,"text","subtext",1,"FIRST");
```

**Arguments:**

| **Name**      | **Type**                                                                                     | **Description**    |
| ------------- | -------------------------------------------------------------------------------------------- | ------------------ |
| `variable`    | Variable                                                                                     | Variable to assign |
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
a1 = variable::get_item_amount(item("stick"));

#Or from the object

a1 = item("stick").get_item_amount();

#Or dry

variable::get_item_amount(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_attribute>
  <code>variable::get_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Attribute\
**Type:** An action that returns a value\
**Description:** Gets the specified attribute from an item as a \"UUID - Value\" dictionary and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_attribute(item("stick"),"name","GENERIC_MAX_HEALTH","ALL","ADD_NUMBER");

#Or from the object

a1 = item("stick").get_item_attribute("name","GENERIC_MAX_HEALTH","ALL","ADD_NUMBER");

#Or dry

variable::get_item_attribute(a1,item("stick"),"name","GENERIC_MAX_HEALTH","ALL","ADD_NUMBER");
```

**Arguments:**

| **Name**    | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Description**     |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `variable`  | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Variable to assign  |
| `item`      | Item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Item                |
| `name`      | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Attribute Name      |
| `attribute` | Marker<br/>**GENERIC_MAX_HEALTH** - Maximum Health (generic.max_health)<br/>**GENERIC_FOLLOW_RANGE** - Follow Distance (generic.follow_range)<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Knockback Resistance (generic.knockback_resistance)<br/>**GENERIC_MOVEMENT_SPEED** - Movement Speed (generic.movement_speed)<br/>**GENERIC_FLYING_SPEED** - Flying speed (generic.flying_speed)<br/>**GENERIC_ATTACK_DAMAGE** - Attack Damage (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Attack Knockback (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Attack Speed (generic.attack_speed)<br/>**GENERIC_ARMOR** - Protection Points (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Defense Density Points (generic.armor_toughness)<br/>**GENERIC_LUCK** - Fishing Luck (generic.luck)<br/>**HORSE_JUMP_STRENGTH** - Horse Jump Strength (horse.jump_strength)<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Zombie reinforcements (zombie.spawn_reinforcements)<br/>**MAX_HEALTH** - Max health<br/>**MAX_ABSORPTION** - Max absorption<br/>**FOLLOW_RANGE** - Follow range<br/>**KNOCKBACK_RESISTANCE** - Knockback resistance<br/>**MOVEMENT_SPEED** - Movement speed<br/>**FLYING_SPEED** - Flying speed<br/>**ATTACK_DAMAGE** - Attack damage<br/>**ATTACK_KNOCKBACK** - Attack knockback<br/>**ATTACK_SPEED** - Attack speed<br/>**ARMOR** - Armor<br/>**ARMOR_TOUGHNESS** - Armor toughness<br/>**LUCK** - Luck<br/>**GENERIC_JUMP_STRENGTH** - Jump strength<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Fall damage multiplier<br/>**GENERIC_SAFE_FALL_DISTANCE** - Safe fall distance<br/>**GENERIC_SCALE** - Scale<br/>**GENERIC_STEP_HEIGHT** - Step height<br/>**GENERIC_GRAVITY** - Gravity<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - The distance of interaction with blocks<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - The distance of interaction with entities<br/>**PLAYER_BLOCK_BREAK_SPEED** - Block breaking speed<br/>**GENERIC_BURNING_TIME** - Burning time<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Explosion knockback resistance<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Movement speed for slowing blocks<br/>**PLAYER_MINING_EFFICIENCY** - Digging speed<br/>**PLAYER_SNEAKING_SPEED** - Movement speed while sneaking<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Digging speed underwater<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - The coefficient of a break in a blow<br/>**GENERIC_OXYGEN_BONUS** - Air underwater<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Movement speed underwater<br/>**GENERIC_MAX_ABSORPTION** - Max absorption (Generic.max_Absorption) | Attribute Type      |
| `slot`      | Marker<br/>**ALL** - All<br/>**MAIN_HAND** - Main Hand<br/>**OFF_HAND** - Offhand<br/>**HEAD** - Helmet<br/>**CHEST** - Chest<br/>**LEGGINGS** - Leggings<br/>**BOOTS** - Boots<br/>**HAND** - Any hand<br/>**ARMOR** - Any armor<br/>**BODY** - Body (does not work with all entities)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Attribute Slot      |
| `operation` | Marker<br/>**ADD_NUMBER** - Amount<br/>**ADD_SCALAR** - Percentage<br/>**MULTIPLY_SCALAR_1** - Product (multiplicative)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Attribute Operation |
<h3 id=set_variable_get_item_color>
  <code>variable::get_item_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Color\
**Type:** An action that returns a value\
**Description:** Sets an item's color value to a variable.
**Work_with:**\
&nbsp;&nbsp;Leather Armor\
&nbsp;&nbsp;Potions\
&nbsp;&nbsp;Tipped Arrows\
&nbsp;&nbsp;Filled Maps

**Usage example:** 
```ts
a1 = variable::get_item_color(item("stick"));

#Or from the object

a1 = item("stick").get_item_color();

#Or dry

variable::get_item_color(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_custom_model_data>
  <code>variable::get_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Model Data\
**Type:** An action that returns a value\
**Description:** Gets the item's model data (CustomModelData) and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_custom_model_data(item("stick"));

#Or from the object

a1 = item("stick").get_item_custom_model_data();

#Or dry

variable::get_item_custom_model_data(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_custom_tag>
  <code>variable::get_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Custom Item Tag\
**Type:** An action that returns a value\
**Description:** Sets the item's custom tag value to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_custom_tag(item("stick"),"tag_name","any value");

#Or from the object

a1 = item("stick").get_item_custom_tag("tag_name","any value");

#Or dry

variable::get_item_custom_tag(a1,item("stick"),"tag_name","any value");
```

**Arguments:**

| **Name**        | **Type**  | **Description**    |
| --------------- | --------- | ------------------ |
| `variable`      | Variable  | Variable to assign |
| `item`          | Item      | Item               |
| `tag_name`      | Text      | Tag Name           |
| `default_value` | Any Value | Default Value      |
<h3 id=set_variable_get_item_custom_tags>
  <code>variable::get_item_custom_tags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Custom Item Tags\
**Type:** An action that returns a value\
**Description:** Sets a dictionary of custom item tags to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_custom_tags(item("stick"));

#Or from the object

a1 = item("stick").get_item_custom_tags();

#Or dry

variable::get_item_custom_tags(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_destroyable_blocks>
  <code>variable::get_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Destroyable Blocks\
**Type:** Action without value\
**Description:** He receives blocks that can break the subject and assigns the result to the variable.

**Usage example:** 
```ts
variable::get_item_destroyable_blocks(a1,item("stick"));

#Or from the object

item("stick").get_item_destroyable_blocks(a1);
```

**Arguments:**

| **Name**   | **Type** | **Description**            |
| ---------- | -------- | -------------------------- |
| `variable` | Variable | Variable for appropriation |
| `item`     | Item     | Item                       |
<h3 id=set_variable_get_item_durability>
  <code>variable::get_item_durability</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Durability\
**Type:** An action that returns a value\
**Description:** Sets the durability of the specified item to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_durability(item("stick"),"DAMAGE");

#Or from the object

a1 = item("stick").get_item_durability("DAMAGE");

#Or dry

variable::get_item_durability(a1,item("stick"),"DAMAGE");
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                                                                      | **Description**    |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`        | Variable                                                                                                                                                                                                                                      | Variable to assign |
| `item`            | Item                                                                                                                                                                                                                                          | Item               |
| `durability_type` | Marker<br/>**DAMAGE** - Current Durability<br/>**DAMAGE_PERCENTAGE** - Current Durability Percentage<br/>**REMAINING** - Remaining Durability<br/>**REMAINING_PERCENTAGE** - Remaining Durability Percentage<br/>**MAXIMUM** - Max Durability | Durability Type    |
<h3 id=set_variable_get_item_enchantments>
  <code>variable::get_item_enchantments</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Enchantments\
**Type:** An action that returns a value\
**Description:** Sets a dictionary of enchantments and their item levels to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_enchantments(item("stick"));

#Or from the object

a1 = item("stick").get_item_enchantments();

#Or dry

variable::get_item_enchantments(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_lore>
  <code>variable::get_item_lore</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Description\
**Type:** An action that returns a value\
**Description:** Sets an item's description text to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_lore(item("stick"));

#Or from the object

a1 = item("stick").get_item_lore();

#Or dry

variable::get_item_lore(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_lore_line>
  <code>variable::get_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Description Line\
**Type:** An action that returns a value\
**Description:** Sets an item's description line to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_lore_line(item("stick"),1);

#Or from the object

a1 = item("stick").get_item_lore_line(1);

#Or dry

variable::get_item_lore_line(a1,item("stick"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
| `line`     | Number   | Line Number        |
<h3 id=set_variable_get_item_max_stack_size>
  <code>variable::get_item_max_stack_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Max Item Amount\
**Type:** An action that returns a value\
**Description:** Sets the maximum number of items in a stack to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_max_stack_size(item("stick"));

#Or from the object

a1 = item("stick").get_item_max_stack_size();

#Or dry

variable::get_item_max_stack_size(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_name>
  <code>variable::get_item_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Name\
**Type:** An action that returns a value\
**Description:** Sets an item's display name to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_name(item("stick"));

#Or from the object

a1 = item("stick").get_item_name();

#Or dry

variable::get_item_name(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_nbt_tags>
  <code>variable::get_item_nbt_tags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get NBT Item Tags\
**Type:** An action that returns a value\
**Description:** Sets the tags of the specified item to an NBT variable.

**Usage example:** 
```ts
a1 = variable::get_item_nbt_tags(item("stick"));

#Or from the object

a1 = item("stick").get_item_nbt_tags();

#Or dry

variable::get_item_nbt_tags(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_placeable_blocks>
  <code>variable::get_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Placeable Blocks\
**Type:** Action without value\
**Description:** He receives blocks on which an object can be installed and assigns the result to the variable.

**Usage example:** 
```ts
variable::get_item_placeable_blocks(a1,item("stick"));

#Or from the object

item("stick").get_item_placeable_blocks(a1);
```

**Arguments:**

| **Name**   | **Type** | **Description**            |
| ---------- | -------- | -------------------------- |
| `variable` | Variable | Variable for appropriation |
| `item`     | Item     | Item                       |
<h3 id=set_variable_get_item_potion_effects>
  <code>variable::get_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Potion Effects From an Item\
**Type:** An action that returns a value\
**Description:** Get the potion effects from an item and assign the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_potion_effects(item("stick"));

#Or from the object

a1 = item("stick").get_item_potion_effects();

#Or dry

variable::get_item_potion_effects(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_rarity>
  <code>variable::get_item_rarity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Rarity\
**Type:** An action that returns a value\
**Description:** Gets the rarity of an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_rarity(item("stick"));

#Or from the object

a1 = item("stick").get_item_rarity();

#Or dry

variable::get_item_rarity(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
<h3 id=set_variable_get_item_type>
  <code>variable::get_item_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Type\
**Type:** An action that returns a value\
**Description:** Sets an item type to a variable, represented as text.

**Usage example:** 
```ts
a1 = variable::get_item_type(item("stick"),"ID");

#Or from the object

a1 = item("stick").get_item_type("ID");

#Or dry

variable::get_item_type(a1,item("stick"),"ID");
```

**Arguments:**

| **Name**   | **Type**                                                                 | **Description**    |
| ---------- | ------------------------------------------------------------------------ | ------------------ |
| `variable` | Variable                                                                 | Variable to assign |
| `type`     | Item                                                                     | Item               |
| `value`    | Marker<br/>**ID** - Item ID<br/>**NAME** - Item Name<br/>**ITEM** - Item | Text View          |
<h3 id=set_variable_get_lectern_book>
  <code>variable::get_lectern_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Lectern Book\
**Type:** An action that returns a value\
**Description:** Assigns the book from the lectern at the specified location to a variable.

**Usage example:** 
```ts
a1 = variable::get_lectern_book(location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).get_lectern_book();

#Or dry

variable::get_lectern_book(a1,location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `location` | Location | Block Location     |
<h3 id=set_variable_get_lectern_page>
  <code>variable::get_lectern_page</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Lectern Book Page\
**Type:** An action that returns a value\
**Description:** Sets a variable to the current page number of the book from the lectern at the specified location.

**Usage example:** 
```ts
a1 = variable::get_lectern_page(location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).get_lectern_page();

#Or dry

variable::get_lectern_page(a1,location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `location` | Location | Block Location     |
<h3 id=set_variable_get_light_level>
  <code>variable::get_light_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Light Level\
**Type:** An action that returns a value\
**Description:** Sets the value of the light level at the specified location to a variable.

**Usage example:** 
```ts
a1 = variable::get_light_level(location(0,0,0,0,0),"TOTAL");

#Or from the object

a1 = location(0,0,0,0,0).get_light_level("TOTAL");

#Or dry

variable::get_light_level(a1,location(0,0,0,0,0),"TOTAL");
```

**Arguments:**

| **Name**     | **Type**                                                                                         | **Description**       |
| ------------ | ------------------------------------------------------------------------------------------------ | --------------------- |
| `variable`   | Variable                                                                                         | Variable to assign    |
| `location`   | Location                                                                                         | Location to get value |
| `value_type` | Marker<br/>**TOTAL** - Total Light<br/>**SKY** - Light from the sky<br/>**BLOCKS** - Block Light | Light Type            |
<h3 id=set_variable_get_list_index_of_value>
  <code>variable::get_list_index_of_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get List Value Index\
**Type:** An action that returns a value\
**Description:** Searchs for a value in a list and gets its index if found. Returns -1 on failure.

**Usage example:** 
```ts
a1 = variable::get_list_index_of_value(`list`,"any value","FIRST");

#Or from the object

a1 = `list`.get_list_index_of_value("any value","FIRST");

#Or dry

variable::get_list_index_of_value(a1,`list`,"any value","FIRST");
```

**Arguments:**

| **Name**      | **Type**                                                                                     | **Description**    |
| ------------- | -------------------------------------------------------------------------------------------- | ------------------ |
| `variable`    | Variable                                                                                     | Variable to assign |
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
a1 = variable::get_list_length(`list`);

#Or from the object

a1 = `list`.get_list_length();

#Or dry

variable::get_list_length(a1,`list`);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `list`     | List     | List               |
<h3 id=set_variable_get_list_random_value>
  <code>variable::get_list_random_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Random List Value\
**Type:** An action that returns a value\
**Description:** Gets a random value from a list.

**Usage example:** 
```ts
a1 = variable::get_list_random_value(`list`);

#Or from the object

a1 = `list`.get_list_random_value();

#Or dry

variable::get_list_random_value(a1,`list`);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `list`     | List     | List               |
<h3 id=set_variable_get_list_value>
  <code>variable::get_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get List Value\
**Type:** An action that returns a value\
**Description:** Get the value from the list at the specified index.

**Usage example:** 
```ts
a1 = variable::get_list_value(`list`,1,"any value");

#Or from the object

a1 = `list`.get_list_value(1,"any value");

#Or dry

variable::get_list_value(a1,`list`,1,"any value");
```

**Arguments:**

| **Name**        | **Type**  | **Description**    |
| --------------- | --------- | ------------------ |
| `variable`      | Variable  | Variable to assign |
| `list`          | List      | List               |
| `number`        | Number    | Index              |
| `default_value` | Any Value | Default value      |
<h3 id=set_variable_get_list_variables>
  <code>variable::get_list_variables</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Variable Names\
**Type:** An action that returns a value\
**Description:** Gets a list of all variable names and assigns the result to the variable.

**Usage example:** 
```ts
a1 = variable::get_list_variables("GAME");

#Or dry

variable::get_list_variables(a1,"GAME");
```

**Arguments:**

| **Name**   | **Type**                                                                                    | **Description**    |
| ---------- | ------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable                                                                                    | Variable to assign |
| `scope`    | Marker<br/>**GAME** - Game<br/>**SAVE** - Saved<br/>**LOCAL** - Local<br/>**LINE** - Little | Variable Type      |
<h3 id=set_variable_get_location_direction>
  <code>variable::get_location_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Location Direction\
**Type:** An action that returns a value\
**Description:** Assigns to a location direction variable.

**Usage example:** 
```ts
a1 = variable::get_location_direction(location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).get_location_direction();

#Or dry

variable::get_location_direction(a1,location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `location` | Location | Location to Get    |
<h3 id=set_variable_get_map_key_by_index>
  <code>variable::get_map_key_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Key By Index\
**Type:** An action that returns a value\
**Description:** He receives the index key and assigns the result to the variable.

**Usage example:** 
```ts
a1 = variable::get_map_key_by_index(`map`,1,"any value");

#Or from the object

a1 = `map`.get_map_key_by_index(1,"any value");

#Or dry

variable::get_map_key_by_index(a1,`map`,1,"any value");
```

**Arguments:**

| **Name**        | **Type**   | **Description**                |
| --------------- | ---------- | ------------------------------ |
| `variable`      | Variable   | Variable for appropriation     |
| `map`           | Dictionary | Dictionary for obtaining a key |
| `index`         | Number     | Key index                      |
| `default_value` | Any Value  | Default value                  |
<h3 id=set_variable_get_map_keys>
  <code>variable::get_map_keys</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get List Of Dictionary Keys\
**Type:** An action that returns a value\
**Description:** Sets a list of dictionary keys to a variable.

**Usage example:** 
```ts
a1 = variable::get_map_keys(`map`);

#Or from the object

a1 = `map`.get_map_keys();

#Or dry

variable::get_map_keys(a1,`map`);
```

**Arguments:**

| **Name**   | **Type**   | **Description**         |
| ---------- | ---------- | ----------------------- |
| `variable` | Variable   | Variable to assign      |
| `map`      | Dictionary | Dictionary to get value |
<h3 id=set_variable_get_map_keys_by_value>
  <code>variable::get_map_keys_by_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Keys By Value\
**Type:** An action that returns a value\
**Description:** Gets the key or list of dictionary keys by value and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_map_keys_by_value(`map`,"any value","any value","FIRST");

#Or from the object

a1 = `map`.get_map_keys_by_value("any value","any value","FIRST");

#Or dry

variable::get_map_keys_by_value(a1,`map`,"any value","any value","FIRST");
```

**Arguments:**

| **Name**        | **Type**                                                                                                                                 | **Description**    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`      | Variable                                                                                                                                 | Variable to assign |
| `map`           | Dictionary                                                                                                                               | Dictionary         |
| `value`         | Any Value                                                                                                                                | Value to get       |
| `default_value` | Any Value                                                                                                                                | Default value      |
| `find_mode`     | Marker<br/>**FIRST** - From Beginning (gets first key)<br/>**LAST** - From the end (gets the last key)<br/>**ALL** - All (gets all keys) | Find Mode          |
<h3 id=set_variable_get_map_size>
  <code>variable::get_map_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Size\
**Type:** An action that returns a value\
**Description:** Sets a dictionary size value to a variable.

**Usage example:** 
```ts
a1 = variable::get_map_size(`map`);

#Or from the object

a1 = `map`.get_map_size();

#Or dry

variable::get_map_size(a1,`map`);
```

**Arguments:**

| **Name**   | **Type**   | **Description**    |
| ---------- | ---------- | ------------------ |
| `variable` | Variable   | Variable to assign |
| `map`      | Dictionary | Dictionary         |
<h3 id=set_variable_get_map_value>
  <code>variable::get_map_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Value\
**Type:** An action that returns a value\
**Description:** Gets the specified dictionary value by key and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_map_value(`map`,"any value","any value");

#Or from the object

a1 = `map`.get_map_value("any value","any value");

#Or dry

variable::get_map_value(a1,`map`,"any value","any value");
```

**Arguments:**

| **Name**        | **Type**   | **Description**      |
| --------------- | ---------- | -------------------- |
| `variable`      | Variable   | Variable to assign   |
| `map`           | Dictionary | Dictionary to change |
| `key`           | Any Value  | Key                  |
| `default_value` | Any Value  | Default Value        |
<h3 id=set_variable_get_map_value_by_index>
  <code>variable::get_map_value_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Dictionary Value By Index\
**Type:** An action that returns a value\
**Description:** He receives a value for the index and assigns the result to the variable.

**Usage example:** 
```ts
a1 = variable::get_map_value_by_index(`map`,1,"any value");

#Or from the object

a1 = `map`.get_map_value_by_index(1,"any value");

#Or dry

variable::get_map_value_by_index(a1,`map`,1,"any value");
```

**Arguments:**

| **Name**        | **Type**   | **Description**                |
| --------------- | ---------- | ------------------------------ |
| `variable`      | Variable   | Variable for appropriation     |
| `map`           | Dictionary | Dictionary for obtaining value |
| `index`         | Number     | The index of value             |
| `default_value` | Any Value  | Default value                  |
<h3 id=set_variable_get_map_values>
  <code>variable::get_map_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get List Of Dictionary Values\
**Type:** An action that returns a value\
**Description:** Sets a list of dictionary values to a variable.

**Usage example:** 
```ts
a1 = variable::get_map_values(`map`);

#Or from the object

a1 = `map`.get_map_values();

#Or dry

variable::get_map_values(a1,`map`);
```

**Arguments:**

| **Name**   | **Type**   | **Description**         |
| ---------- | ---------- | ----------------------- |
| `variable` | Variable   | Variable to assign      |
| `map`      | Dictionary | Dictionary to get value |
<h3 id=set_variable_get_midpoint_between_vectors>
  <code>variable::get_midpoint_between_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Midpoint Between Vectors\
**Type:** An action that returns a value\
**Description:** Sets the midpoint between two vectors to a variable.

**Usage example:** 
```ts
a1 = variable::get_midpoint_between_vectors(vector(0,0,0),vector(0,0,0));

#Or dry

variable::get_midpoint_between_vectors(a1,vector(0,0,0),vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `vector_1` | Vector   | First Vector       |
| `vector_2` | Vector   | Second Vector      |
<h3 id=set_variable_get_particle_amount>
  <code>variable::get_particle_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Amount\
**Type:** An action that returns a value\
**Description:** Sets a particle amount to a variable.

**Usage example:** 
```ts
a1 = variable::get_particle_amount(particle("fire"));

#Or from the object

a1 = particle("fire").get_particle_amount();

#Or dry

variable::get_particle_amount(a1,particle("fire"));
```

**Arguments:**

| **Name**   | **Type**        | **Description**       |
| ---------- | --------------- | --------------------- |
| `variable` | Variable        | Variable to assign    |
| `particle` | Particle Effect | Particle to get value |
<h3 id=set_variable_get_particle_color>
  <code>variable::get_particle_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Color\
**Type:** An action that returns a value\
**Description:** Sets a particle's color value to a variable.

**Usage example:** 
```ts
a1 = variable::get_particle_color(particle("fire"),"COLOR");

#Or from the object

a1 = particle("fire").get_particle_color("COLOR");

#Or dry

variable::get_particle_color(a1,particle("fire"),"COLOR");
```

**Arguments:**

| **Name**     | **Type**                                                                              | **Description**       |
| ------------ | ------------------------------------------------------------------------------------- | --------------------- |
| `variable`   | Variable                                                                              | Variable to assign    |
| `particle`   | Particle Effect                                                                       | Particle to get value |
| `color_type` | Marker<br/>**COLOR** - The usual color<br/>**TO_COLOR** - The color of the transition | Type of color         |
<h3 id=set_variable_get_particle_material>
  <code>variable::get_particle_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Material\
**Type:** An action that returns a value\
**Description:** Sets a particle's material value to a variable.

**Usage example:** 
```ts
a1 = variable::get_particle_material(particle("fire"));

#Or from the object

a1 = particle("fire").get_particle_material();

#Or dry

variable::get_particle_material(a1,particle("fire"));
```

**Arguments:**

| **Name**   | **Type**        | **Description**       |
| ---------- | --------------- | --------------------- |
| `variable` | Variable        | Variable to assign    |
| `particle` | Particle Effect | Particle to get value |
<h3 id=set_variable_get_particle_offset>
  <code>variable::get_particle_offset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Motion\
**Type:** An action that returns a value\
**Description:** Sets a particle's movement value to a variable.

**Usage example:** 
```ts
a1 = variable::get_particle_offset(particle("fire"));

#Or from the object

a1 = particle("fire").get_particle_offset();

#Or dry

variable::get_particle_offset(a1,particle("fire"));
```

**Arguments:**

| **Name**   | **Type**        | **Description**       |
| ---------- | --------------- | --------------------- |
| `variable` | Variable        | Variable to assign    |
| `particle` | Particle Effect | Particle to get value |
<h3 id=set_variable_get_particle_size>
  <code>variable::get_particle_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Size\
**Type:** An action that returns a value\
**Description:** Sets a particle size value to a variable.

**Usage example:** 
```ts
a1 = variable::get_particle_size(particle("fire"));

#Or from the object

a1 = particle("fire").get_particle_size();

#Or dry

variable::get_particle_size(a1,particle("fire"));
```

**Arguments:**

| **Name**   | **Type**        | **Description**       |
| ---------- | --------------- | --------------------- |
| `variable` | Variable        | Variable to assign    |
| `particle` | Particle Effect | Particle to get value |
<h3 id=set_variable_get_particle_spread>
  <code>variable::get_particle_spread</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Spread\
**Type:** An action that returns a value\
**Description:** Sets a particle's spread value to a variable.

**Usage example:** 
```ts
a1 = variable::get_particle_spread(particle("fire"),"VERTICAL");

#Or from the object

a1 = particle("fire").get_particle_spread("VERTICAL");

#Or dry

variable::get_particle_spread(a1,particle("fire"),"VERTICAL");
```

**Arguments:**

| **Name**   | **Type**                                                           | **Description**       |
| ---------- | ------------------------------------------------------------------ | --------------------- |
| `variable` | Variable                                                           | Variable to assign    |
| `particle` | Particle Effect                                                    | Particle to get value |
| `type`     | Marker<br/>**VERTICAL** - Vertical<br/>**HORIZONTAL** - Horizontal | Spread Plane          |
<h3 id=set_variable_get_particle_type>
  <code>variable::get_particle_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Particle Type\
**Type:** An action that returns a value\
**Description:** Sets a particle type to a variable.

**Usage example:** 
```ts
a1 = variable::get_particle_type(particle("fire"));

#Or from the object

a1 = particle("fire").get_particle_type();

#Or dry

variable::get_particle_type(a1,particle("fire"));
```

**Arguments:**

| **Name**   | **Type**        | **Description**       |
| ---------- | --------------- | --------------------- |
| `variable` | Variable        | Variable to assign    |
| `particle` | Particle Effect | Particle to get value |
<h3 id=set_variable_get_player_head>
  <code>variable::get_player_head</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Player Head\
**Type:** An action that returns a value\
**Description:** Gets the player's head as an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_player_head("name_or_uuid","NAME_OR_UUID");

#Or dry

variable::get_player_head(a1,"name_or_uuid","NAME_OR_UUID");
```

**Arguments:**

| **Name**       | **Type**                                                                               | **Description**     |
| -------------- | -------------------------------------------------------------------------------------- | ------------------- |
| `variable`     | Variable                                                                               | Variable to assign  |
| `name_or_uuid` | Text                                                                                   | Player name or UUID |
| `receive_type` | Marker<br/>**NAME_OR_UUID** - Name or uuid player<br/>**VALUE** - Value Skin parameter | Type of value       |
<h3 id=set_variable_get_player_head_owner>
  <code>variable::get_player_head_owner</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Head Owner\
**Type:** An action that returns a value\
**Description:** Get the name or UUID of the owner of the item head and assign the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_player_head_owner(item("stick"),"NAME");

#Or from the object

a1 = item("stick").get_player_head_owner("NAME");

#Or dry

variable::get_player_head_owner(a1,item("stick"),"NAME");
```

**Arguments:**

| **Name**       | **Type**                                                                            | **Description**    |
| -------------- | ----------------------------------------------------------------------------------- | ------------------ |
| `variable`     | Variable                                                                            | Variable to assign |
| `head`         | Item                                                                                | Player Head        |
| `return_value` | Marker<br/>**NAME** - Name<br/>**UUID** - UUID<br/>**VALUE** - Value Skin parameter | Return Value       |
<h3 id=set_variable_get_player_head_value>
  <code>variable::get_player_head_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Player Head At Location\
**Type:** An action that returns a value\
**Description:** He receives the name or UUID of the owner of the head in the location and assigns the result to the variable.

**Usage example:** 
```ts
a1 = variable::get_player_head_value(location(0,0,0,0,0),"NAME");

#Or from the object

a1 = location(0,0,0,0,0).get_player_head_value("NAME");

#Or dry

variable::get_player_head_value(a1,location(0,0,0,0,0),"NAME");
```

**Arguments:**

| **Name**       | **Type**                                                                                                   | **Description**            |
| -------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------- |
| `variable`     | Variable                                                                                                   | Variable for appropriation |
| `location`     | Location                                                                                                   | The location of the head   |
| `return_value` | Marker<br/>**NAME** - The name of the owner<br/>**UUID** - UUID owner<br/>**VALUE** - Value Skin parameter | Returned value             |
<h3 id=set_variable_get_potion_effect_amplifier>
  <code>variable::get_potion_effect_amplifier</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Potion Power\
**Type:** An action that returns a value\
**Description:** Sets a potion's power to a variable.

**Usage example:** 
```ts
a1 = variable::get_potion_effect_amplifier(potion("slow_falling"));

#Or from the object

a1 = potion("slow_falling").get_potion_effect_amplifier();

#Or dry

variable::get_potion_effect_amplifier(a1,potion("slow_falling"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `potion`   | Potion   | Potion             |
<h3 id=set_variable_get_potion_effect_duration>
  <code>variable::get_potion_effect_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Potion Duration\
**Type:** An action that returns a value\
**Description:** Sets the potion's duration to a variable.

**Usage example:** 
```ts
a1 = variable::get_potion_effect_duration(potion("slow_falling"));

#Or from the object

a1 = potion("slow_falling").get_potion_effect_duration();

#Or dry

variable::get_potion_effect_duration(a1,potion("slow_falling"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `potion`   | Potion   | Potion             |
<h3 id=set_variable_get_potion_effect_type>
  <code>variable::get_potion_effect_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Potion Effect\
**Type:** An action that returns a value\
**Description:** Sets a potion type to a variable.

**Usage example:** 
```ts
a1 = variable::get_potion_effect_type(potion("slow_falling"));

#Or from the object

a1 = potion("slow_falling").get_potion_effect_type();

#Or dry

variable::get_potion_effect_type(a1,potion("slow_falling"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `potion`   | Potion   | Potion             |
<h3 id=set_variable_get_sculk_shrieker_warning_level>
  <code>variable::get_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sculk Shrieker Warning Level\
**Type:** An action that returns a value\
**Description:** It assigns to the variable the hazard level of the rock-crkuna in the specified location.

**Usage example:** 
```ts
a1 = variable::get_sculk_shrieker_warning_level(location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).get_sculk_shrieker_warning_level();

#Or dry

variable::get_sculk_shrieker_warning_level(a1,location(0,0,0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**                 |
| ---------- | -------- | ------------------------------- |
| `variable` | Variable | Variable for appropriation      |
| `location` | Location | The location of the rock-crkuna |
<h3 id=set_variable_get_sign_text>
  <code>variable::get_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sign Line Text\
**Type:** An action that returns a value\
**Description:** Sets the text value of the sign line at the selected location to a variable.

**Usage example:** 
```ts
a1 = variable::get_sign_text(location(0,0,0,0,0),"FRONT","FIRST");

#Or from the object

a1 = location(0,0,0,0,0).get_sign_text("FRONT","FIRST");

#Or dry

variable::get_sign_text(a1,location(0,0,0,0,0),"FRONT","FIRST");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                       | **Description**    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable                                                                                                                                       | Variable to assign |
| `location`   | Location                                                                                                                                       | Sign Location      |
| `check_side` | Marker<br/>**FRONT** - Front<br/>**BACK** - Back<br/>**ALL** - All                                                                             | Sign Side          |
| `sign_line`  | Marker<br/>**FIRST** - First Line<br/>**SECOND** - Second Line<br/>**THIRD** - Third line<br/>**FOURTH** - Fourth line<br/>**ALL** - All lines | Line Number        |
<h3 id=set_variable_get_sound_pitch>
  <code>variable::get_sound_pitch</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Pitch\
**Type:** An action that returns a value\
**Description:** Sets the pitch of a sound to a variable.

**Usage example:** 
```ts
a1 = variable::get_sound_pitch(sound("entity.zombie.hurt"));

#Or from the object

a1 = sound("entity.zombie.hurt").get_sound_pitch();

#Or dry

variable::get_sound_pitch(a1,sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `sound`    | Sound    | Sound to get value |
<h3 id=set_variable_get_sound_source>
  <code>variable::get_sound_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Source\
**Type:** An action that returns a value\
**Description:** Get the sound source and assign the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_sound_source(sound("entity.zombie.hurt"));

#Or from the object

a1 = sound("entity.zombie.hurt").get_sound_source();

#Or dry

variable::get_sound_source(a1,sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `sound`    | Sound    | Sound to get value |
<h3 id=set_variable_get_sound_type>
  <code>variable::get_sound_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Type\
**Type:** An action that returns a value\
**Description:** Sets a sound type value to a variable.

**Usage example:** 
```ts
a1 = variable::get_sound_type(sound("entity.zombie.hurt"));

#Or from the object

a1 = sound("entity.zombie.hurt").get_sound_type();

#Or dry

variable::get_sound_type(a1,sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `sound`    | Sound    | Sound to get value |
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
a1 = variable::get_sound_variation(sound("entity.zombie.hurt"));

#Or from the object

a1 = sound("entity.zombie.hurt").get_sound_variation();

#Or dry

variable::get_sound_variation(a1,sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `sound`    | Sound    | Sound to get value |
<h3 id=set_variable_get_sound_variations>
  <code>variable::get_sound_variations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Variations\
**Type:** An action that returns a value\
**Description:** Gets a list of all sound variations and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_sound_variations(sound("entity.zombie.hurt"));

#Or from the object

a1 = sound("entity.zombie.hurt").get_sound_variations();

#Or dry

variable::get_sound_variations(a1,sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type** | **Description**     |
| ---------- | -------- | ------------------- |
| `variable` | Variable | Variable to assign  |
| `sound`    | Sound    | Sound to get values |
<h3 id=set_variable_get_sound_volume_action>
  <code>variable::get_sound_volume_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Sound Volume\
**Type:** An action that returns a value\
**Description:** Sets a sound volume value to a variable.

**Usage example:** 
```ts
a1 = variable::get_sound_volume_action(sound("entity.zombie.hurt"));

#Or from the object

a1 = sound("entity.zombie.hurt").get_sound_volume_action();

#Or dry

variable::get_sound_volume_action(a1,sound("entity.zombie.hurt"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `sound`    | Sound    | Sound to get value |
<h3 id=set_variable_get_template_code>
  <code>variable::get_template_code</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Template Code\
**Type:** An action that returns a value\
**Description:** Assigns a template code to a variable.

**Usage example:** 
```ts
a1 = variable::get_template_code(item("stick"),"TEXT");

#Or from the object

a1 = item("stick").get_template_code("TEXT");

#Or dry

variable::get_template_code(a1,item("stick"),"TEXT");
```

**Arguments:**

| **Name**      | **Type**                                                      | **Description**    |
| ------------- | ------------------------------------------------------------- | ------------------ |
| `variable`    | Variable                                                      | Variable to assign |
| `template`    | Item                                                          | Template           |
| `return_type` | Marker<br/>**TEXT** - JSON Text<br/>**MAP** - JSON Dictionary | Return Value       |
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
a1 = variable::get_text_width("text");

#Or from the object

a1 = "text".get_text_width();

#Or dry

variable::get_text_width(a1,"text");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `text`     | Text     | Original Text      |
<h3 id=set_variable_get_vector_all_components>
  <code>variable::get_vector_all_components</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get All Vector Coordinates\
**Type:** An action that returns a value\
**Description:** He receives all the coordinates of the vector and assigns the result to the alternating.

**Usage example:** 
```ts
a1, a2, a3 = variable::get_vector_all_components(vector(0,0,0));

#Or from the object

a1, a2, a3 = vector(0,0,0).get_vector_all_components();

#Or dry

variable::get_vector_all_components(a1,a2,a3,vector(0,0,0));
```

**Arguments:**

| **Name** | **Type** | **Description**             |
| -------- | -------- | --------------------------- |
| `x`      | Variable | Coordinate x                |
| `y`      | Variable | Coordinate y                |
| `z`      | Variable | Coordinate z                |
| `vector` | Vector   | Vector for obtaining values |
<h3 id=set_variable_get_vector_between_locations>
  <code>variable::get_vector_between_locations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Vector Between Locations\
**Type:** An action that returns a value\
**Description:** Creates a vector between the start and end locations and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_vector_between_locations(location(0,0,0,0,0),location(0,0,0,0,0));

#Or dry

variable::get_vector_between_locations(a1,location(0,0,0,0,0),location(0,0,0,0,0));
```

**Arguments:**

| **Name**         | **Type** | **Description**    |
| ---------------- | -------- | ------------------ |
| `variable`       | Variable | Variable to assign |
| `end_location`   | Location | Starting Location  |
| `start_location` | Location | End Location       |
<h3 id=set_variable_get_vector_component>
  <code>variable::get_vector_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Vector Coordinate\
**Type:** An action that returns a value\
**Description:** Gets the specified vector coordinate and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_vector_component(vector(0,0,0),"X");

#Or from the object

a1 = vector(0,0,0).get_vector_component("X");

#Or dry

variable::get_vector_component(a1,vector(0,0,0),"X");
```

**Arguments:**

| **Name**           | **Type**                                                                          | **Description**     |
| ------------------ | --------------------------------------------------------------------------------- | ------------------- |
| `variable`         | Variable                                                                          | Variable to assign  |
| `vector`           | Vector                                                                            | Vector to get value |
| `vector_component` | Marker<br/>**X** - X Coordinate<br/>**Y** - Y Coordinate<br/>**Z** - Z Coordinate | Coordinate Type     |
<h3 id=set_variable_get_vector_from_block_face>
  <code>variable::get_vector_from_block_face</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Vector From Cardinal Direction\
**Type:** An action that returns a value\
**Description:** Generates a normalized vector based on the specified cardinal direction (\"south\", \"north\", \"east\", \"west\", \"up\", \"down\").

**Usage example:** 
```ts
a1 = variable::get_vector_from_block_face("block_face");

#Or dry

variable::get_vector_from_block_face(a1,"block_face");
```

**Arguments:**

| **Name**     | **Type** | **Description**    |
| ------------ | -------- | ------------------ |
| `variable`   | Variable | Variable to assign |
| `block_face` | Text     | Cardinal Direction |
<h3 id=set_variable_get_vector_length>
  <code>variable::get_vector_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Vector Length\
**Type:** An action that returns a value\
**Description:** Sets the length of a vector to a variable.

**Usage example:** 
```ts
a1 = variable::get_vector_length(vector(0,0,0),"LENGTH");

#Or from the object

a1 = vector(0,0,0).get_vector_length("LENGTH");

#Or dry

variable::get_vector_length(a1,vector(0,0,0),"LENGTH");
```

**Arguments:**

| **Name**      | **Type**                                                                    | **Description**      |
| ------------- | --------------------------------------------------------------------------- | -------------------- |
| `variable`    | Variable                                                                    | Variable to assign   |
| `vector`      | Vector                                                                      | Vector to get length |
| `length_type` | Marker<br/>**LENGTH** - Real Length<br/>**LENGTH_SQUARED** - Length Squared | Value Type           |
<h3 id=set_variable_hash>
  <code>variable::get_text_hash</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Text Hash\
**Type:** An action that returns a value\
**Description:** Sets the text hash value to a variable.

**Usage example:** 
```ts
a1 = variable::get_text_hash("text","MD5");

#Or from the object

a1 = "text".get_text_hash("MD5");

#Or dry

variable::get_text_hash(a1,"text","MD5");
```

**Arguments:**

| **Name**    | **Type**                                                               | **Description**    |
| ----------- | ---------------------------------------------------------------------- | ------------------ |
| `variable`  | Variable                                                               | Variable to assign |
| `text`      | Text                                                                   | Original Text      |
| `algorithm` | Marker<br/>**MD5** - MD5<br/>**SHA1** - SHA-1<br/>**SHA256** - SHA-256 | Algorithm          |
<h3 id=set_variable_increment>
  <code>variable::increment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Increment (+=)\
**Type:** An action that returns a value\
**Description:** Adds the selected number to a variable.

**Usage example:** 
```ts
a1 = variable::increment(1);

#Or from the object

a1 = (1).increment();

#Or dry

variable::increment(a1,1);
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
a1 = variable::insert_list_value(`list`,1,"any value");

#Or from the object

a1 = `list`.insert_list_value(1,"any value");

#Or dry

variable::insert_list_value(a1,`list`,1,"any value");
```

**Arguments:**

| **Name**   | **Type**  | **Description**    |
| ---------- | --------- | ------------------ |
| `variable` | Variable  | Variable to assign |
| `list`     | List      | List               |
| `number`   | Number    | Index              |
| `value`    | Any Value | Value              |
<h3 id=set_variable_join_text>
  <code>variable::join_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Join List To Text\
**Type:** An action that returns a value\
**Description:** Combines list items into a single text and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::join_text(`list`,"separator","prefix","postfix",1,"truncated");

#Or from the object

a1 = `list`.join_text("separator","prefix","postfix",1,"truncated");

#Or dry

variable::join_text(a1,`list`,"separator","prefix","postfix",1,"truncated");
```

**Arguments:**

| **Name**    | **Type** | **Description**                     |
| ----------- | -------- | ----------------------------------- |
| `variable`  | Variable | Variable to assign                  |
| `list`      | List     | List to Join                        |
| `separator` | Text     | Separator                           |
| `prefix`    | Text     | Prefix                              |
| `postfix`   | Text     | Postfix                             |
| `limit`     | Number   | Item Limit (if empty, all items)    |
| `truncated` | Text     | Text after limit (default is "...") |
<h3 id=set_variable_lerp_number>
  <code>variable::lerp_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Lerp Number\
**Type:** An action that returns a value\
**Description:** Calculates the number between two numbers with a certain coefficient and assigns the result to the variable.With a coefficient of 0, the first number will be returned, at 1 - the second, at 0.5 - the average value.

**Usage example:** 
```ts
a1 = variable::lerp_number(1,2,3);

#Or from the object

a1 = (3).lerp_number(1,2);

#Or dry

variable::lerp_number(a1,1,2,3);
```

**Arguments:**

| **Name**   | **Type** | **Description**            |
| ---------- | -------- | -------------------------- |
| `variable` | Variable | Variable for appropriation |
| `start`    | Number   | The first number           |
| `stop`     | Number   | The second                 |
| `amount`   | Number   | Coefficient (from 0 to 1)  |
<h3 id=set_variable_location_relative>
  <code>variable::location_relative</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Relative Location\
**Type:** An action that returns a value\
**Description:** Sets the location relative to the side of the block at a certain distance, assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::location_relative(location(0,0,0,0,0),1,"NORTH");

#Or from the object

a1 = location(0,0,0,0,0).location_relative(1,"NORTH");

#Or dry

variable::location_relative(a1,location(0,0,0,0,0),1,"NORTH");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Description**    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Variable to assign |
| `location`   | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Relative Location  |
| `distance`   | Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Distance           |
| `block_face` | Marker<br/>**NORTH** - North<br/>**EAST** - East<br/>**SOUTH** - South<br/>**WEST** - West<br/>**UP** - Up<br/>**DOWN** - Down<br/>**NORTH_EAST** - Northeast<br/>**NORTH_WEST** - Northwest<br/>**SOUTH_EAST** - Southeast<br/>**SOUTH_WEST** - Southwest<br/>**WEST_NORTH_WEST** - West-north-west (west_north_west)<br/>**NORTH_NORTH_WEST** - North-north-west (north_north_west)<br/>**NORTH_NORTH_EAST** - North-north-east (north_north_east)<br/>**EAST_NORTH_EAST** - East-North-East (east_north_east)<br/>**EAST_SOUTH_EAST** - East Southeast (east_south_east)<br/>**SOUTH_SOUTH_EAST** - South Southeast (south_south_east)<br/>**SOUTH_SOUTH_WEST** - South-South-West (south_south_west)<br/>**WEST_SOUTH_WEST** - West-south-west (west_south_west)<br/>**SELF** - Own (self) | Block Side         |
<h3 id=set_variable_locations_distance>
  <code>variable::locations_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Distance Between Locations\
**Type:** An action that returns a value\
**Description:** Gets the distance between locations and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::locations_distance(location(0,0,0,0,0),location(0,0,0,0,0),"THREE_D");

#Or dry

variable::locations_distance(a1,location(0,0,0,0,0),location(0,0,0,0,0),"THREE_D");
```

**Arguments:**

| **Name**     | **Type**                                                                                                         | **Description**    |
| ------------ | ---------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable                                                                                                         | Variable to assign |
| `location_1` | Location                                                                                                         | First Location     |
| `location_2` | Location                                                                                                         | Second Location    |
| `type`       | Marker<br/>**THREE_D** - Volume<br/>**TWO_D** - In Plane<br/>**ALTITUDE** - Altitude<br/>**Altitude** - Altitude | Distance Type      |
<h3 id=set_variable_log>
  <code>variable::log</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Logarithm (log)\
**Type:** An action that returns a value\
**Description:** Sets a variable to the logarithm value with the selected argument and base.

**Usage example:** 
```ts
a1 = variable::log(1,2);

#Or from the object

a1 = (1).log(2);

#Or dry

variable::log(a1,1,2);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `number`   | Number   | Log Argument       |
| `base`     | Number   | Log Base           |
<h3 id=set_variable_map_range>
  <code>variable::map_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set New Number Range\
**Type:** An action that returns a value\
**Description:** It translates the number from one range to another and assigns the result to the variable.

**Usage example:** 
```ts
a1 = variable::map_range(1,2,3,4,5);

#Or from the object

a1 = (1).map_range(2,3,4,5);

#Or dry

variable::map_range(a1,1,2,3,4,5);
```

**Arguments:**

| **Name**     | **Type** | **Description**                       |
| ------------ | -------- | ------------------------------------- |
| `variable`   | Variable | Variable for appropriation            |
| `number`     | Number   | The number for change                 |
| `from_start` | Number   | The lower limit of the original range |
| `from_stop`  | Number   | The upper limit of the original range |
| `to_start`   | Number   | The lower limit of the new range      |
| `to_stop`    | Number   | The upper limit of the new range      |
<h3 id=set_variable_max>
  <code>variable::max</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Maximum Value\
**Type:** An action that returns a value\
**Description:** Sets the largest number of the selected variable to a variable.

**Usage example:** 
```ts
a1 = variable::max([1, 2]);

#Or dry

variable::max(a1,[1, 2]);
```

**Arguments:**

| **Name**   | **Type**     | **Description**    |
| ---------- | ------------ | ------------------ |
| `variable` | Variable     | Variable to assign |
| `value`    | list[Number] | Numbers to select  |
<h3 id=set_variable_min>
  <code>variable::min</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Minimum Value\
**Type:** An action that returns a value\
**Description:** Sets the variable to the smallest number selected.

**Usage example:** 
```ts
a1 = variable::min([1, 2]);

#Or dry

variable::min(a1,[1, 2]);
```

**Arguments:**

| **Name**   | **Type**     | **Description**    |
| ---------- | ------------ | ------------------ |
| `variable` | Variable     | Variable to assign |
| `value`    | list[Number] | Numbers to select  |
<h3 id=set_variable_multiply>
  <code>variable::multiply</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Multiply (×)\
**Type:** An action that returns a value\
**Description:** Sets a multiplication of numbers to a variable.

**Usage example:** 
```ts
a1 = variable::multiply([1, 2]);

#Or dry

variable::multiply(a1,[1, 2]);
```

**Arguments:**

| **Name**   | **Type**     | **Description**     |
| ---------- | ------------ | ------------------- |
| `variable` | Variable     | Variable to assign  |
| `value`    | list[Number] | Numbers to Multiply |
<h3 id=set_variable_multiply_vector>
  <code>variable::multiply_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Multiply Vector By Number\
**Type:** An action that returns a value\
**Description:** Sets the result of multiplying a vector by a number to a variable.

**Usage example:** 
```ts
a1 = variable::multiply_vector(vector(0,0,0),1);

#Or dry

variable::multiply_vector(a1,vector(0,0,0),1);
```

**Arguments:**

| **Name**     | **Type** | **Description**    |
| ------------ | -------- | ------------------ |
| `variable`   | Variable | Variable to assign |
| `vector`     | Vector   | Vector to change   |
| `multiplier` | Number   | Number to Multiply |
<h3 id=set_variable_parse_json>
  <code>variable::parse_json</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Parse JSON\
**Type:** An action that returns a value\
**Description:** Parses JSON text into elements\: dictionaries (if the text is in curly braces) and lists (if the text is in square brackets) that can be manipulated to get the desired values.

**Usage example:** 
```ts
a1 = variable::parse_json("json");

#Or dry

variable::parse_json(a1,"json");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | For writing result |
| `json`     | Text     | JSON text          |
<h3 id=set_variable_parse_to_component>
  <code>variable::parse_to_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Parse To Stylized Text\
**Type:** An action that returns a value\
**Description:** Converts the usual text into stylized text.

**Usage example:** 
```ts
a1 = variable::parse_to_component("text","PLAIN");

#Or from the object

a1 = "text".parse_to_component("PLAIN");

#Or dry

variable::parse_to_component(a1,"text","PLAIN");
```

**Arguments:**

| **Name**   | **Type**                                                                                                       | **Description**            |
| ---------- | -------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `variable` | Variable                                                                                                       | Variable for appropriation |
| `text`     | Text                                                                                                           | Text for transformation    |
| `parsing`  | Marker<br/>**PLAIN** - Ordinary<br/>**LEGACY** - Color (&)<br/>**MINIMESSAGE** - Stylized<br/>**JSON** - Zhnon | Type of transformation     |
<h3 id=set_variable_perlin_noise_3d>
  <code>variable::perlin_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Perlin Noise\
**Type:** An action that returns a value\
**Description:** Sets the perlin noise value at a specific location to a variable. Returns a number, with a value from -1 to 1.

**Usage example:** 
```ts
a1 = variable::perlin_noise_3d(location(0,0,0,0,0),1,2,3,4,5,"ZERO_TO_ONE","TRUE");

#Or dry

variable::perlin_noise_3d(a1,location(0,0,0,0,0),1,2,3,4,5,"ZERO_TO_ONE","TRUE");
```

**Arguments:**

| **Name**        | **Type**                                                                              | **Description**            |
| --------------- | ------------------------------------------------------------------------------------- | -------------------------- |
| `variable`      | Variable                                                                              | Variable to assign         |
| `location`      | Location                                                                              | Location to set noise      |
| `seed`          | Number                                                                                | Noise Key                  |
| `loc_frequency` | Number                                                                                | Noise Frequency            |
| `octaves`       | Number                                                                                | Number of Noise Octaves    |
| `frequency`     | Number                                                                                | Frequency of Noise Octaves |
| `amplitude`     | Number                                                                                | Noise Octave Amplitude     |
| `range_mode`    | Marker<br/>**ZERO_TO_ONE** - 0 to 1<br/>**FULL_RANGE** - Full Range (-1 to 1 or more) | Value Range                |
| `normalized`    | Marker<br/>**TRUE** - Normalize<br/>**FALSE** - Don't Normalize                       | Normalize Values           |
<h3 id=set_variable_pow>
  <code>variable::pow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Raise To Power (^)\
**Type:** An action that returns a value\
**Description:** Sets a variable to a power value with the selected base and exponent.

**Usage example:** 
```ts
a1 = variable::pow(1,2);

#Or from the object

a1 = (1).pow(2);

#Or dry

variable::pow(a1,1,2);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `base`     | Number   | Power base         |
| `power`    | Number   | Exponent           |
<h3 id=set_variable_purge>
  <code>variable::purge</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Clear Variables\
**Type:** Action without value\
**Description:** Purges all variables matching the selected names.

**Usage example:** 
```ts
variable::purge(["names", "names"],"GAME","EQUALS","TRUE");
```

**Arguments:**

| **Name**      | **Type**                                                                                                                 | **Description**  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| `names`       | list[Text]                                                                                                               | Names to Compare |
| `scope`       | Marker<br/>**GAME** - Gaming<br/>**SAVE** - Saved<br/>**LOCAL** - Local<br/>**LINE** - Line                              | Variable Type    |
| `match`       | Marker<br/>**EQUALS** - Full Match<br/>**NAME_CONTAINS** - Name contains text<br/>**PART_CONTAINS** - Text contains name | Comparison Mode  |
| `ignore_case` | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled                                                                   | Ignore case      |
<h3 id=set_variable_random>
  <code>variable::random</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Random Value\
**Type:** An action that returns a value\
**Description:** Sets a random value to a variable.

**Usage example:** 
```ts
a1 = variable::random(["any value", "any value"]);

#Or dry

variable::random(a1,["any value", "any value"]);
```

**Arguments:**

| **Name**   | **Type**        | **Description**    |
| ---------- | --------------- | ------------------ |
| `variable` | Variable        | Variable to assign |
| `values`   | list[Any Value] | Values to choose   |
<h3 id=set_variable_random_location>
  <code>variable::random_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Random Location\
**Type:** An action that returns a value\
**Description:** Creates a random location in the region between two corners and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::random_location(location(0,0,0,0,0),location(0,0,0,0,0),"TRUE");

#Or dry

variable::random_location(a1,location(0,0,0,0,0),location(0,0,0,0,0),"TRUE");
```

**Arguments:**

| **Name**     | **Type**                                             | **Description**              |
| ------------ | ---------------------------------------------------- | ---------------------------- |
| `variable`   | Variable                                             | Variable to assign           |
| `location_1` | Location                                             | First corner of region       |
| `location_2` | Location                                             | Second Region Corner         |
| `integer`    | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable | Round to Integer Coordinates |
<h3 id=set_variable_random_number>
  <code>variable::random_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Random Number\
**Type:** An action that returns a value\
**Description:** Sets a variable to a random number within the selected range.

**Usage example:** 
```ts
a1 = variable::random_number(1,2,"TRUE");

#Or dry

variable::random_number(a1,1,2,"TRUE");
```

**Arguments:**

| **Name**   | **Type**                                                 | **Description**    |
| ---------- | -------------------------------------------------------- | ------------------ |
| `variable` | Variable                                                 | Variable to assign |
| `min`      | Number                                                   | Minimum Value      |
| `max`      | Number                                                   | Max Value          |
| `integer`  | Marker<br/>**TRUE** - Integer<br/>**FALSE** - Fractional | Number Type        |
<h3 id=set_variable_randomize_list_order>
  <code>variable::randomize_list_order</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Randomize List\
**Type:** An action that returns a value\
**Description:** Sets the order of items randomly.

**Usage example:** 
```ts
a1 = variable::randomize_list_order(`list`);

#Or from the object

a1 = `list`.randomize_list_order();

#Or dry

variable::randomize_list_order(a1,`list`);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `list`     | List     | List               |
<h3 id=set_variable_ray_trace_result>
  <code>variable::ray_trace_result</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Raycast Result\
**Type:** An action that returns a value\
**Description:** Launches a ray with the given parameters. When the ray collides with the specified objects (entity or block), you can get the location of the ray, the location and side of the block, the UUID of the entity, and the side of the hitbox. Beamwidth only works on entities (increases or decreases creature hitboxes).

**Usage example:** 
```ts
a1, a2, a3, a4 = variable::ray_trace_result(location(0,0,0,0,0),"ONLY_BLOCKS",1,`entities`,"TRUE",2,"NEVER");

#Or dry

variable::ray_trace_result(a1,a2,a3,a4,location(0,0,0,0,0),"ONLY_BLOCKS",1,`entities`,"TRUE",2,"NEVER");
```

**Arguments:**

| **Name**                          | **Type**                                                                                                                                   | **Description**                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `variable_for_hit_location`       | Variable                                                                                                                                   | Ray Impact Point                                                                     |
| `variable_for_hit_block_location` | Variable                                                                                                                                   | Block Location                                                                       |
| `variable_for_hit_block_face`     | Variable                                                                                                                                   | Block/Hitbox Side                                                                    |
| `variable_for_hit_entity_uuid`    | Variable                                                                                                                                   | Entity UUID                                                                          |
| `start`                           | Location                                                                                                                                   | Beam Start                                                                           |
| `ray_collision_mode`              | Marker<br/>**ONLY_BLOCKS** - Only with Blocks<br/>**BLOCKS_AND_ENTITIES** - With blocks and entities<br/>**ONLY_ENTITIES** - Entities Only | Object Collision                                                                     |
| `ray_size`                        | Number                                                                                                                                     | Beam Width                                                                           |
| `entities`                        | List                                                                                                                                       | Names or UUIDs of the entities to collide with (default is all players and entities) |
| `ignore_passable_blocks`          | Marker<br/>**TRUE** - Ignore<br/>**FALSE** - Don't Ignore                                                                                  | Ignore Passable Blocks                                                               |
| `max_distance`                    | Number                                                                                                                                     | Beam length                                                                          |
| `fluid_collision_mode`            | Marker<br/>**NEVER** - Ignore Completely<br/>**SOURCE_ONLY** - Consider Fluid Source Only<br/>**ALWAYS** - Don't Ignore                    | Ignore Fluid                                                                         |
<h3 id=set_variable_reflect_vector_product>
  <code>variable::reflect_vector_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reflect Vector By Second Vector\
**Type:** An action that returns a value\
**Description:** Reflects a vector relative to another vector and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::reflect_vector_product(vector(0,0,0),vector(0,0,0),1);

#Or dry

variable::reflect_vector_product(a1,vector(0,0,0),vector(0,0,0),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**                                            |
| ---------- | -------- | ---------------------------------------------------------- |
| `variable` | Variable | Variable to assign                                         |
| `vector_1` | Vector   | Source Vector                                              |
| `vector_2` | Vector   | Reflection Surface Vector                                  |
| `bounce`   | Number   | Multiply the resulting vector by this number (default 1.0) |
<h3 id=set_variable_regex_replace_text>
  <code>variable::regex_replace_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Match With Regular Expression\
**Type:** An action that returns a value\
**Description:** Replaces text matching the specified regular expression and assigns the result to a variable. The "Replacement" argument can contain $\<group name\> to refer to the group. Include only the flags you need!

**Usage example:** 
```ts
a1 = variable::regex_replace_text("text","regex","replacement","ANY","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE");

#Or from the object

a1 = "text".regex_replace_text("regex","replacement","ANY","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE");

#Or dry

variable::regex_replace_text(a1,"text","regex","replacement","ANY","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE");
```

**Arguments:**

| **Name**          | **Type**                                                                          | **Description**                                  |
| ----------------- | --------------------------------------------------------------------------------- | ------------------------------------------------ |
| `variable`        | Variable                                                                          | Variable to assign                               |
| `text`            | Text                                                                              | Original Text                                    |
| `regex`           | Text                                                                              | Regular Expression                               |
| `replacement`     | Text                                                                              | Replacement                                      |
| `first`           | Marker<br/>**ANY** - Replace All Matches<br/>**FIRST** - Replace First Match Only | Number of replacements                           |
| `ignore_case`     | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled                            | Ignore case (ignore_case flag)                   |
| `multiline`       | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled                            | Multiline Mode (multiline flag)                  |
| `literal`         | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled                            | Treat template verbatim (literal flag)           |
| `unix_lines`      | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled                            | UNIX line mode (unix_lines flag)                 |
| `comments`        | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled                            | Allow comments and ignore spaces (comments flag) |
| `dot_matches_all` | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled                            | Dotall Mode (dotall flag)                        |
| `cannon_eq`       | Marker<br/>**TRUE** - Enabled<br/>**FALSE** - Disabled                            | Canonical Equivalence (cannon_eq Flag)           |
<h3 id=set_variable_remainder>
  <code>variable::remainder</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remainder (%)\
**Type:** An action that returns a value\
**Description:** Sets the remainder of the division of two numbers to a variable.

**Usage example:** 
```ts
a1 = variable::remainder(1,2,"REMAINDER");

#Or from the object

a1 = (1).remainder(2,"REMAINDER");

#Or dry

variable::remainder(a1,1,2,"REMAINDER");
```

**Arguments:**

| **Name**         | **Type**                                                                                                                        | **Description**    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`       | Variable                                                                                                                        | Variable to Assign |
| `dividend`       | Number                                                                                                                          | Dividend           |
| `divisor`        | Number                                                                                                                          | Divisor            |
| `remainder_mode` | Marker<br/>**REMAINDER** - Remainder of division (leaves dividend sign)<br/>**MODULO** - Modulo Remainder (leaves divisor sign) | Operation Mode     |
<h3 id=set_variable_remove_compass_lodestone>
  <code>variable::remove_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Lodestone Location\
**Type:** An action that returns a value\
**Description:** Removes a magnetite location from a magnetized compass and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::remove_compass_lodestone(item("stick"));

#Or from the object

a1 = item("stick").remove_compass_lodestone();

#Or dry

variable::remove_compass_lodestone(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to Assign |
| `item`     | Item     | Magnetized Compass |
<h3 id=set_variable_remove_enchantment>
  <code>variable::remove_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Item Enchantment\
**Type:** An action that returns a value\
**Description:** Removes an enchantment from an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::remove_enchantment(item("stick"),"enchantment");

#Or from the object

a1 = item("stick").remove_enchantment("enchantment");

#Or dry

variable::remove_enchantment(a1,item("stick"),"enchantment");
```

**Arguments:**

| **Name**      | **Type** | **Description**    |
| ------------- | -------- | ------------------ |
| `variable`    | Variable | Variable to Assign |
| `item`        | Item     | Item               |
| `enchantment` | Text     | Enchant ID         |
<h3 id=set_variable_remove_item_attribute>
  <code>variable::remove_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Item Attribute\
**Type:** Action without value\
**Description:** Removes the attribute from the subject and assigns the result to the variable.

**Usage example:** 
```ts
variable::remove_item_attribute(a1,item("stick"),"name_or_uuid","GENERIC_MAX_HEALTH");

#Or from the object

item("stick").remove_item_attribute(a1,"name_or_uuid","GENERIC_MAX_HEALTH");
```

**Arguments:**

| **Name**       | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Description**            |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `variable`     | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Variable for appropriation |
| `item`         | Item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Item                       |
| `name_or_uuid` | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Name or uuid attribute     |
| `attribute`    | Marker<br/>**GENERIC_MAX_HEALTH** - Max health (generic.max_health)<br/>**GENERIC_FOLLOW_RANGE** - Distance (generic.follow_range)<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Publishing resistance (Generic.knockback_resistance)<br/>**GENERIC_MOVEMENT_SPEED** - Generic.movement_Speed)<br/>**GENERIC_FLYING_SPEED** - Generic.flying_speed)<br/>**GENERIC_ATTACK_DAMAGE** - Generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Repulsion of the attack (Generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Generic.attack_Speed)<br/>**GENERIC_ARMOR** - Generic.armor glasses)<br/>**GENERIC_ARMOR_TOUGHNESS** - Generic.armor_touchHness density glasses)<br/>**GENERIC_LUCK** - Luck of fishing (Generic.luck)<br/>**HORSE_JUMP_STRENGTH** - Horse jump (horse.jump_strength)<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - The chance of reinforcing the zombie<br/>**MAX_HEALTH** - Max health<br/>**MAX_ABSORPTION** - Max absorption<br/>**FOLLOW_RANGE** - The distance<br/>**KNOCKBACK_RESISTANCE** - Knockback resistance<br/>**MOVEMENT_SPEED** - Movement speed<br/>**FLYING_SPEED** - Flight speed<br/>**ATTACK_DAMAGE** - Attack damage<br/>**ATTACK_KNOCKBACK** - Attack knockback<br/>**ATTACK_SPEED** - Attack speed<br/>**ARMOR** - Armor<br/>**ARMOR_TOUGHNESS** - Armor toughness<br/>**LUCK** - Luck<br/>**GENERIC_JUMP_STRENGTH** - Jump strength<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Fall damage multiplier<br/>**GENERIC_SAFE_FALL_DISTANCE** - Safe fall distance<br/>**GENERIC_SCALE** - Scale<br/>**GENERIC_STEP_HEIGHT** - Step height<br/>**GENERIC_GRAVITY** - Gravity<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - The distance of interaction with blocks<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - The distance of interaction with entities<br/>**PLAYER_BLOCK_BREAK_SPEED** - Block breaking speed<br/>**GENERIC_BURNING_TIME** - Burning time<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Explosion knockback resistance<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Movement speed for slowing blocks<br/>**PLAYER_MINING_EFFICIENCY** - Digging speed<br/>**PLAYER_SNEAKING_SPEED** - Movement speed while sneaking<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Digging speed underwater<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - The coefficient of a break in a blow<br/>**GENERIC_OXYGEN_BONUS** - Air underwater<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Movement speed underwater<br/>**GENERIC_MAX_ABSORPTION** - Max absorption (Generic.max_Absorption) | Type of attribute          |
<h3 id=set_variable_remove_item_custom_model_data>
  <code>variable::remove_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Item Model Data\
**Type:** An action that returns a value\
**Description:** Removes item model data (CustomModelData) and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::remove_item_custom_model_data(item("stick"));

#Or from the object

a1 = item("stick").remove_item_custom_model_data();

#Or dry

variable::remove_item_custom_model_data(a1,item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `variable` | Variable | Variable to set |
| `item`     | Item     | Item            |
<h3 id=set_variable_remove_item_custom_tag>
  <code>variable::remove_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Custom Item Tag\
**Type:** An action that returns a value\
**Description:** Removes a custom item tag and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::remove_item_custom_tag(item("stick"),"tag_name");

#Or from the object

a1 = item("stick").remove_item_custom_tag("tag_name");

#Or dry

variable::remove_item_custom_tag(a1,item("stick"),"tag_name");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
| `tag_name` | Text     | Tag Name           |
<h3 id=set_variable_remove_item_lore_line>
  <code>variable::remove_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Item Description Line\
**Type:** An action that returns a value\
**Description:** Removes an item's description line and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::remove_item_lore_line(item("stick"),1);

#Or from the object

a1 = item("stick").remove_item_lore_line(1);

#Or dry

variable::remove_item_lore_line(a1,item("stick"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
| `line`     | Number   | Line Number        |
<h3 id=set_variable_remove_item_potion_effects>
  <code>variable::remove_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Potion Effects From an Item\
**Type:** An action that returns a value\
**Description:** Removes potion effects from an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::remove_item_potion_effects([potion("slow_falling"), potion("slow_falling")],item("stick"));

#Or from the object

a1 = item("stick").remove_item_potion_effects([potion("slow_falling"), potion("slow_falling")]);

#Or dry

variable::remove_item_potion_effects(a1,[potion("slow_falling"), potion("slow_falling")],item("stick"));
```

**Arguments:**

| **Name**   | **Type**     | **Description**    |
| ---------- | ------------ | ------------------ |
| `variable` | Variable     | Variable to assign |
| `effects`  | list[Potion] | Potion Effects     |
| `item`     | Item         | Item               |
<h3 id=set_variable_remove_list_duplicates>
  <code>variable::remove_list_duplicates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Duplicate Values\
**Type:** An action that returns a value\
**Description:** Removes all values that appear more than once in the list.

**Usage example:** 
```ts
a1 = variable::remove_list_duplicates(`list`);

#Or from the object

a1 = `list`.remove_list_duplicates();

#Or dry

variable::remove_list_duplicates(a1,`list`);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to Assign |
| `list`     | List     | List               |
<h3 id=set_variable_remove_list_value>
  <code>variable::remove_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Value From List\
**Type:** An action that returns a value\
**Description:** Removes the specified value from the list.

**Usage example:** 
```ts
a1 = variable::remove_list_value(`list`,"any value","FIRST");

#Or from the object

a1 = `list`.remove_list_value("any value","FIRST");

#Or dry

variable::remove_list_value(a1,`list`,"any value","FIRST");
```

**Arguments:**

| **Name**      | **Type**                                                                                                        | **Description**    |
| ------------- | --------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`    | Variable                                                                                                        | Variable to Assign |
| `list`        | List                                                                                                            | List               |
| `value`       | Any Value                                                                                                       | Value              |
| `remove_mode` | Marker<br/>**FIRST** - The first coincidence<br/>**LAST** - The last coincidence<br/>**ALL** - All coincidences | Removal mode       |
<h3 id=set_variable_remove_list_value_at_index>
  <code>variable::remove_list_value_at_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Value From List By Index\
**Type:** An action that returns a value\
**Description:** Removes the value at the specified index from the list.

**Usage example:** 
```ts
a2, a1 = variable::remove_list_value_at_index(`list`,1);

#Or from the object

a2, a1 = `list`.remove_list_value_at_index(1);

#Or dry

variable::remove_list_value_at_index(a1,a2,`list`,1);
```

**Arguments:**

| **Name**        | **Type** | **Description**    |
| --------------- | -------- | ------------------ |
| `removed_value` | Variable | Removed Value      |
| `variable`      | Variable | Variable to Assign |
| `list`          | List     | List               |
| `index`         | Number   | Index              |
<h3 id=set_variable_remove_map_entry>
  <code>variable::remove_map_entry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Dictionary Entry\
**Type:** An action that returns a value\
**Description:** Removes a dictionary entry and assigns the result to a variable.

**Usage example:** 
```ts
a2, a1 = variable::remove_map_entry(["any value", "any value"],`map`,"any value");

#Or from the object

a2, a1 = `map`.remove_map_entry(["any value", "any value"],"any value");

#Or dry

variable::remove_map_entry(a1,a2,["any value", "any value"],`map`,"any value");
```

**Arguments:**

| **Name**        | **Type**        | **Description**      |
| --------------- | --------------- | -------------------- |
| `removed_value` | Variable        | Removed Value        |
| `variable`      | Variable        | Variable to assign   |
| `values`        | list[Any Value] | Values               |
| `map`           | Dictionary      | Dictionary to change |
| `key`           | Any Value       | Key                  |
<h3 id=set_variable_remove_text>
  <code>variable::remove_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Text\
**Type:** An action that returns a value\
**Description:** Removes all or part of the text and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::remove_text(["remove", "remove"],"text","TRUE");

#Or from the object

a1 = "text".remove_text(["remove", "remove"],"TRUE");

#Or dry

variable::remove_text(a1,["remove", "remove"],"text","TRUE");
```

**Arguments:**

| **Name**   | **Type**                                             | **Description**     |
| ---------- | ---------------------------------------------------- | ------------------- |
| `variable` | Variable                                             | Variable to assign  |
| `remove`   | list[Text]                                           | Text to Remove      |
| `text`     | Text                                                 | Original Text       |
| `regex`    | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable | Regular Expressions |
<h3 id=set_variable_repeat_text>
  <code>variable::repeat_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat Text\
**Type:** An action that returns a value\
**Description:** Sets a variable to text repeated a specified number of times.

**Usage example:** 
```ts
a1 = variable::repeat_text("text",1);

#Or from the object

a1 = "text".repeat_text(1);

#Or dry

variable::repeat_text(a1,"text",1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `text`     | Text     | Text to repeat     |
| `repeat`   | Number   | Number of Repeats  |
<h3 id=set_variable_replace_text>
  <code>variable::replace_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Text\
**Type:** An action that returns a value\
**Description:** Replaces all or part of the text and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::replace_text("text","replace","replacement","ANY","TRUE");

#Or from the object

a1 = "text".replace_text("replace","replacement","ANY","TRUE");

#Or dry

variable::replace_text(a1,"text","replace","replacement","ANY","TRUE");
```

**Arguments:**

| **Name**      | **Type**                                                                          | **Description**        |
| ------------- | --------------------------------------------------------------------------------- | ---------------------- |
| `variable`    | Variable                                                                          | Variable to assign     |
| `text`        | Text                                                                              | Original Text          |
| `replace`     | Text                                                                              | Text to Replace        |
| `replacement` | Text                                                                              | Replacement            |
| `first`       | Marker<br/>**ANY** - Replace All Matches<br/>**FIRST** - Replace First Match Only | Number of replacements |
| `ignore_case` | Marker<br/>**TRUE** - Ignore<br/>**FALSE** - Don't ignore                         | Ignore case            |
<h3 id=set_variable_reverse_list>
  <code>variable::reverse_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Reverse List\
**Type:** An action that returns a value\
**Description:** Reverses the order of items.

**Usage example:** 
```ts
a1 = variable::reverse_list(`list`);

#Or from the object

a1 = `list`.reverse_list();

#Or dry

variable::reverse_list(a1,`list`);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `list`     | List     | List               |
<h3 id=set_variable_root>
  <code>variable::root</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Root (√)\
**Type:** An action that returns a value\
**Description:** Sets a variable to a root value with the selected root number and exponent.

**Usage example:** 
```ts
a1 = variable::root(1,2);

#Or dry

variable::root(a1,1,2);
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `variable` | Variable | Variable to set |
| `base`     | Number   | Root Root       |
| `root`     | Number   | Root Index      |
<h3 id=set_variable_rotate_vector_around_axis>
  <code>variable::rotate_vector_around_axis</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Rotate Vector Around an Axis\
**Type:** An action that returns a value\
**Description:** Rotates a vector around an axis by the specified amount and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::rotate_vector_around_axis(vector(0,0,0),1,"X","DEGREES");

#Or from the object

a1 = vector(0,0,0).rotate_vector_around_axis(1,"X","DEGREES");

#Or dry

variable::rotate_vector_around_axis(a1,vector(0,0,0),1,"X","DEGREES");
```

**Arguments:**

| **Name**      | **Type**                                                                          | **Description**    |
| ------------- | --------------------------------------------------------------------------------- | ------------------ |
| `variable`    | Variable                                                                          | Variable to assign |
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
a1 = variable::rotate_vector_around_vector(vector(0,0,0),vector(0,0,0),1,"DEGREES");

#Or from the object

a1 = vector(0,0,0).rotate_vector_around_vector(vector(0,0,0),1,"DEGREES");

#Or dry

variable::rotate_vector_around_vector(a1,vector(0,0,0),vector(0,0,0),1,"DEGREES");
```

**Arguments:**

| **Name**          | **Type**                                                   | **Description**    |
| ----------------- | ---------------------------------------------------------- | ------------------ |
| `variable`        | Variable                                                   | Variable to assign |
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
a1 = variable::round(1,2,"ROUND");

#Or from the object

a1 = (1).round(2,"ROUND");

#Or dry

variable::round(a1,1,2,"ROUND");
```

**Arguments:**

| **Name**     | **Type**                                                                                  | **Description**                     |
| ------------ | ----------------------------------------------------------------------------------------- | ----------------------------------- |
| `variable`   | Variable                                                                                  | Variable to assign                  |
| `number`     | Number                                                                                    | Number to Round                     |
| `precision`  | Number                                                                                    | Number of digits after integer part |
| `round_type` | Marker<br/>**ROUND** - Normal Rounding<br/>**FLOOR** - Round Down<br/>**CEIL** - Round Up | Rounding Method                     |
<h3 id=set_variable_set_all_coordinates>
  <code>variable::set_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set All Location Coordinates\
**Type:** An action that returns a value\
**Description:** Sets the values of all coordinates to a location.

**Usage example:** 
```ts
a1 = variable::set_all_coordinates(1,2,3,4,5);

#Or dry

variable::set_all_coordinates(a1,1,2,3,4,5);
```

**Arguments:**

| **Name**   | **Type** | **Description**     |
| ---------- | -------- | ------------------- |
| `variable` | Variable | Variable to assign  |
| `x`        | Number   | X Coordinate        |
| `y`        | Number   | Y Coordinate        |
| `z`        | Number   | Z Coordinate        |
| `yaw`      | Number   | Horizontal Rotation |
| `pitch`    | Number   | Pitch Vertical      |
<h3 id=set_variable_set_armor_trim>
  <code>variable::set_armor_trim</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Armor Trim\
**Type:** Action without value\
**Description:** The armor sets the specified template and assigns the result to the variable.

**Usage example:** 
```ts
variable::set_armor_trim(a1,item("stick"),item("stick"),item("stick"));

#Or from the object

item("stick").set_armor_trim(a1,item("stick"),item("stick"));
```

**Arguments:**

| **Name**   | **Type** | **Description**              |
| ---------- | -------- | ---------------------------- |
| `variable` | Variable | Variable for appropriation   |
| `armor`    | Item     | Armor                        |
| `material` | Item     | The material of the template |
| `pattern`  | Item     | Pattern                      |
<h3 id=set_variable_set_book_page>
  <code>variable::set_book_page</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Book Text On Page\
**Type:** An action that returns a value\
**Description:** Sets the book text on a specific page and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_book_page(item("stick"),"text",1,"MERGE");

#Or from the object

a1 = item("stick").set_book_page("text",1,"MERGE");

#Or dry

variable::set_book_page(a1,item("stick"),"text",1,"MERGE");
```

**Arguments:**

| **Name**   | **Type**                                               | **Description**    |
| ---------- | ------------------------------------------------------ | ------------------ |
| `variable` | Variable                                               | Variable to assign |
| `book`     | Item                                                   | Book to change     |
| `text`     | Text                                                   | New Text           |
| `page`     | Number                                                 | Page Number        |
| `mode`     | Marker<br/>**MERGE** - Replace<br/>**APPEND** - Append | Set Mode           |
<h3 id=set_variable_set_book_pages>
  <code>variable::set_book_pages</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Book Text\
**Type:** An action that returns a value\
**Description:** Sets the book text and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_book_pages(["text", "text"],item("stick"));

#Or from the object

a1 = item("stick").set_book_pages(["text", "text"]);

#Or dry

variable::set_book_pages(a1,["text", "text"],item("stick"));
```

**Arguments:**

| **Name**   | **Type**   | **Description**    |
| ---------- | ---------- | ------------------ |
| `variable` | Variable   | Variable to assign |
| `text`     | list[Text] | New Text           |
| `book`     | Item       | Book to change     |
<h3 id=set_variable_set_bundle_items>
  <code>variable::set_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Bundle Items\
**Type:** Action without value\
**Description:** Changes the contents of the bag and assigns the result to the variable.

**Usage example:** 
```ts
variable::set_bundle_items(a1,[item("stick"), item("stick")],item("stick"),"ADD");

#Or from the object

item("stick").set_bundle_items(a1,[item("stick"), item("stick")],"ADD");
```

**Arguments:**

| **Name**       | **Type**                                                           | **Description**            |
| -------------- | ------------------------------------------------------------------ | -------------------------- |
| `variable`     | Variable                                                           | Variable for appropriation |
| `items`        | list[Item]                                                         | Change items               |
| `bundle`       | Item                                                               | Bundle                     |
| `setting_mode` | Marker<br/>**ADD** - Add<br/>**SET** - Set<br/>**REMOVE** - Delete | Type of change             |
<h3 id=set_variable_set_compass_lodestone>
  <code>variable::set_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Lodestone Location\
**Type:** An action that returns a value\
**Description:** Sets the compass to the location of the magnetite and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_compass_lodestone(item("stick"),location(0,0,0,0,0),"TRUE");

#Or from the object

a1 = item("stick").set_compass_lodestone(location(0,0,0,0,0),"TRUE");

#Or dry

variable::set_compass_lodestone(a1,item("stick"),location(0,0,0,0,0),"TRUE");
```

**Arguments:**

| **Name**   | **Type**                                                | **Description**             |
| ---------- | ------------------------------------------------------- | --------------------------- |
| `variable` | Variable                                                | Variable to Assign          |
| `item`     | Item                                                    | Compass                     |
| `location` | Location                                                | Magnetite Location          |
| `tracked`  | Marker<br/>**TRUE** - Track<br/>**FALSE** - Don't check | Location Magnetite Presence |
<h3 id=set_variable_set_component_children>
  <code>variable::set_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set the subsidiaries to the stylized text\
**Type:** An action that returns a value\
**Description:** Assigns to the variable stylized text with the specified daughter parts.

**Usage example:** 
```ts
a1 = variable::set_component_children(["children", "children"],"component");

#Or from the object

a1 = "component".set_component_children(["children", "children"]);

#Or dry

variable::set_component_children(a1,["children", "children"],"component");
```

**Arguments:**

| **Name**    | **Type**   | **Description**            |
| ----------- | ---------- | -------------------------- |
| `variable`  | Variable   | Variable for appropriation |
| `children`  | list[Text] | Dummies stylized texts     |
| `component` | Text       | The main stylized text     |
<h3 id=set_variable_set_component_click>
  <code>variable::set_component_click</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Click Action\
**Type:** An action that returns a value\
**Description:** It sets the action indicated by the stylized text when pressing and assigns it to the variable.

**Usage example:** 
```ts
a1 = variable::set_component_click("component","value","COPY_TO_CLIPBORD");

#Or from the object

a1 = "component".set_component_click("value","COPY_TO_CLIPBORD");

#Or dry

variable::set_component_click(a1,"component","value","COPY_TO_CLIPBORD");
```

**Arguments:**

| **Name**       | **Type**                                                                                                                                                                                                                               | **Description**            |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `variable`     | Variable                                                                                                                                                                                                                               | Variable for appropriation |
| `component`    | Text                                                                                                                                                                                                                                   | Stylized text              |
| `value`        | Text                                                                                                                                                                                                                                   | The value of the action    |
| `click_action` | Marker<br/>**COPY_TO_CLIPBORD** - Copy to the clipboard<br/>**SUGGEST_COMMAND** - Offer a message<br/>**OPEN_URL** - Open the link<br/>**CHANGE_PAGE** - Change the page of the book<br/>**COPY_TO_CLIPBOARD** - Copy to the clipboard | Action when pressing       |
<h3 id=set_variable_set_component_decorations>
  <code>variable::set_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Decorations\
**Type:** An action that returns a value\
**Description:** It sets the scenery of the specified stylized text and assigns it to the variable.

**Usage example:** 
```ts
a1 = variable::set_component_decorations("component","NOT_SET","NOT_SET","NOT_SET","NOT_SET","NOT_SET");

#Or from the object

a1 = "component".set_component_decorations("NOT_SET","NOT_SET","NOT_SET","NOT_SET","NOT_SET");

#Or dry

variable::set_component_decorations(a1,"component","NOT_SET","NOT_SET","NOT_SET","NOT_SET","NOT_SET");
```

**Arguments:**

| **Name**        | **Type**                                                                     | **Description**            |
| --------------- | ---------------------------------------------------------------------------- | -------------------------- |
| `variable`      | Variable                                                                     | Variable for appropriation |
| `component`     | Text                                                                         | Stylized text              |
| `bold`          | Marker<br/>**NOT_SET** - Not installed<br/>**FALSE** - No<br/>**TRUE** - Yes | Bold                       |
| `italic`        | Marker<br/>**NOT_SET** - Not installed<br/>**FALSE** - No<br/>**TRUE** - Yes | Italic                     |
| `underlined`    | Marker<br/>**NOT_SET** - Not installed<br/>**FALSE** - No<br/>**TRUE** - Yes | Undrelined                 |
| `strikethrough` | Marker<br/>**NOT_SET** - Not installed<br/>**FALSE** - No<br/>**TRUE** - Yes | Strikethrough              |
| `obfuscated`    | Marker<br/>**NOT_SET** - Not installed<br/>**FALSE** - No<br/>**TRUE** - Yes | Obfuscated                 |
<h3 id=set_variable_set_component_entity_hover>
  <code>variable::set_component_entity_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Entity Hover\
**Type:** An action that returns a value\
**Description:** It sets the entity displayed by the specified stylized text when hovering and assigns it to the variable.

**Usage example:** 
```ts
a1 = variable::set_component_entity_hover("component","name_or_uuid");

#Or from the object

a1 = "component".set_component_entity_hover("name_or_uuid");

#Or dry

variable::set_component_entity_hover(a1,"component","name_or_uuid");
```

**Arguments:**

| **Name**       | **Type** | **Description**            |
| -------------- | -------- | -------------------------- |
| `variable`     | Variable | Variable for appropriation |
| `component`    | Text     | Stylized text              |
| `name_or_uuid` | Text     | Name or uuid entity        |
<h3 id=set_variable_set_component_font>
  <code>variable::set_component_font</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Font\
**Type:** An action that returns a value\
**Description:** It sets the font to the specified stylized text and assigns it to the variable.

**Usage example:** 
```ts
a1 = variable::set_component_font("component","namespace","value");

#Or from the object

a1 = "component".set_component_font("namespace","value");

#Or dry

variable::set_component_font(a1,"component","namespace","value");
```

**Arguments:**

| **Name**    | **Type** | **Description**                        |
| ----------- | -------- | -------------------------------------- |
| `variable`  | Variable | Variable for appropriation             |
| `component` | Text     | Stylized text                          |
| `namespace` | Text     | The space of names (minecraft \: etc.) |
| `value`     | Text     | Font ID                                |
<h3 id=set_variable_set_component_hex_color>
  <code>variable::set_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Hex Color\
**Type:** An action that returns a value\
**Description:** Sets HEX-color with the specified stylized text and assigns it to the variable.

**Usage example:** 
```ts
a1 = variable::set_component_hex_color("component","color");

#Or from the object

a1 = "component".set_component_hex_color("color");

#Or dry

variable::set_component_hex_color(a1,"component","color");
```

**Arguments:**

| **Name**    | **Type** | **Description**            |
| ----------- | -------- | -------------------------- |
| `variable`  | Variable | Variable for appropriation |
| `component` | Text     | Stylized text              |
| `color`     | Text     | HEX-color                  |
<h3 id=set_variable_set_component_hover>
  <code>variable::set_component_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Text Hover\
**Type:** An action that returns a value\
**Description:** It sets the text displayed by indicated by the stylized text and assigns it to the variable.

**Usage example:** 
```ts
a1 = variable::set_component_hover("component","hover");

#Or from the object

a1 = "component".set_component_hover("hover");

#Or dry

variable::set_component_hover(a1,"component","hover");
```

**Arguments:**

| **Name**    | **Type** | **Description**                       |
| ----------- | -------- | ------------------------------------- |
| `variable`  | Variable | Variable for appropriation            |
| `component` | Text     | Stylized text                         |
| `hover`     | Text     | Stylized text displayed when entering |
<h3 id=set_variable_set_component_insertion>
  <code>variable::set_component_insertion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Hover Text\
**Type:** An action that returns a value\
**Description:** It sets the proposed message to the specified stylized text when pressing with Shift and appropriates it to the variable.

**Usage example:** 
```ts
a1 = variable::set_component_insertion("component","insertion");

#Or from the object

a1 = "component".set_component_insertion("insertion");

#Or dry

variable::set_component_insertion(a1,"component","insertion");
```

**Arguments:**

| **Name**    | **Type** | **Description**            |
| ----------- | -------- | -------------------------- |
| `variable`  | Variable | Variable for appropriation |
| `component` | Text     | Stylized text              |
| `insertion` | Text     | The proposed message       |
<h3 id=set_variable_set_component_item_hover>
  <code>variable::set_component_item_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Stylized Text Item Hover\
**Type:** An action that returns a value\
**Description:** It sets an object displayed by the indicated stylized text and assigns it to the variable.

**Usage example:** 
```ts
a1 = variable::set_component_item_hover("component",item("stick"));

#Or from the object

a1 = "component".set_component_item_hover(item("stick"));

#Or dry

variable::set_component_item_hover(a1,"component",item("stick"));
```

**Arguments:**

| **Name**    | **Type** | **Description**            |
| ----------- | -------- | -------------------------- |
| `variable`  | Variable | Variable for appropriation |
| `component` | Text     | Stylized text              |
| `hover`     | Item     | A subject displayed when   |
<h3 id=set_variable_set_coordinate>
  <code>variable::set_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Location Coordinate\
**Type:** An action that returns a value\
**Description:** Sets the value of the selected coordinate to a location and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_coordinate(location(0,0,0,0,0),1,"X");

#Or from the object

a1 = location(0,0,0,0,0).set_coordinate(1,"X");

#Or dry

variable::set_coordinate(a1,location(0,0,0,0,0),1,"X");
```

**Arguments:**

| **Name**     | **Type**                                                                                                                         | **Description**    |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable                                                                                                                         | Variable to assign |
| `location`   | Location                                                                                                                         | Location to set    |
| `coordinate` | Number                                                                                                                           | Coordinate Value   |
| `type`       | Marker<br/>**X** - X Axis<br/>**Y** - Y Axis<br/>**Z** - Z Axis<br/>**YAW** - Horizontal rotation<br/>**PITCH** - Pitch Vertical | Coordinate Type    |
<h3 id=set_variable_set_item_amount>
  <code>variable::set_item_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Amount\
**Type:** An action that returns a value\
**Description:** Sets the number of items in a stack.

**Usage example:** 
```ts
a1 = variable::set_item_amount(item("stick"),1);

#Or from the object

a1 = item("stick").set_item_amount(1);

#Or dry

variable::set_item_amount(a1,item("stick"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
| `amount`   | Number   | Amount             |
<h3 id=set_variable_set_item_attribute>
  <code>variable::set_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Attribute To Item\
**Type:** An action that returns a value\
**Description:** Adds a specific attribute to an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_attribute(item("stick"),1,"name","GENERIC_MAX_HEALTH","ALL","ADD_NUMBER");

#Or from the object

a1 = item("stick").set_item_attribute(1,"name","GENERIC_MAX_HEALTH","ALL","ADD_NUMBER");

#Or dry

variable::set_item_attribute(a1,item("stick"),1,"name","GENERIC_MAX_HEALTH","ALL","ADD_NUMBER");
```

**Arguments:**

| **Name**    | **Type**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Description**     |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `variable`  | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Variable to assign  |
| `item`      | Item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Item                |
| `amount`    | Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Attribute Value     |
| `name`      | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Attribute Name      |
| `attribute` | Marker<br/>**GENERIC_MAX_HEALTH** - Maximum Health (generic.max_health)<br/>**GENERIC_FOLLOW_RANGE** - Follow Distance (generic.follow_range)<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Knockback Resistance (generic.knockback_resistance)<br/>**GENERIC_MOVEMENT_SPEED** - Movement Speed (generic.movement_speed)<br/>**GENERIC_FLYING_SPEED** - Flying speed (generic.flying_speed)<br/>**GENERIC_ATTACK_DAMAGE** - Attack Damage (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Attack Knockback (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Attack Speed (generic.attack_speed)<br/>**GENERIC_ARMOR** - Protection Points (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Defense Density Points (generic.armor_toughness)<br/>**GENERIC_LUCK** - Fishing Luck (generic.luck)<br/>**HORSE_JUMP_STRENGTH** - Horse Jump Strength (horse.jump_strength)<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Zombie reinforcements (zombie.spawn_reinforcements)<br/>**MAX_HEALTH** - Max health<br/>**MAX_ABSORPTION** - Max absorption<br/>**FOLLOW_RANGE** - Follow range<br/>**KNOCKBACK_RESISTANCE** - Knockback resistance<br/>**MOVEMENT_SPEED** - Movement speed<br/>**FLYING_SPEED** - Flight speed<br/>**ATTACK_DAMAGE** - Attack damage<br/>**ATTACK_KNOCKBACK** - Attack knockback<br/>**ATTACK_SPEED** - Attack speed<br/>**ARMOR** - Armor<br/>**ARMOR_TOUGHNESS** - Armor toughness<br/>**LUCK** - Luck<br/>**GENERIC_JUMP_STRENGTH** - Jump strength<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Fall damage multiplier<br/>**GENERIC_SAFE_FALL_DISTANCE** - Safe fall distance<br/>**GENERIC_SCALE** - Scale<br/>**GENERIC_STEP_HEIGHT** - Step height<br/>**GENERIC_GRAVITY** - Gravity<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - The distance of interaction with blocks<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - The distance of interaction with entities<br/>**PLAYER_BLOCK_BREAK_SPEED** - Block breaking speed<br/>**GENERIC_BURNING_TIME** - Burning time<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Explosion knockback resistance<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Movement speed for slowing blocks<br/>**PLAYER_MINING_EFFICIENCY** - Digging speed<br/>**PLAYER_SNEAKING_SPEED** - Movement speed while sneaking<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Digging speed underwater<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - The coefficient of a break in a blow<br/>**GENERIC_OXYGEN_BONUS** - Air underwater<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Movement speed underwater<br/>**GENERIC_MAX_ABSORPTION** - Max absorption (Generic.max_Absorption) | Attribute Type      |
| `slot`      | Marker<br/>**ALL** - All<br/>**MAIN_HAND** - Main Hand<br/>**OFF_HAND** - Offhand<br/>**HEAD** - Helmet<br/>**CHEST** - Chest<br/>**LEGGINGS** - Leggings<br/>**BOOTS** - Boots<br/>**HAND** - Any hand<br/>**ARMOR** - Any armor<br/>**BODY** - Body (does not work with all entities)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Attribute Slot      |
| `operation` | Marker<br/>**ADD_NUMBER** - Amount<br/>**ADD_SCALAR** - Percentage<br/>**MULTIPLY_SCALAR_1** - Product (multiplicative)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Attribute Operation |
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
a1 = variable::set_item_color(item("stick"),"color");

#Or from the object

a1 = item("stick").set_item_color("color");

#Or dry

variable::set_item_color(a1,item("stick"),"color");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
| `color`    | Text     | Color              |
<h3 id=set_variable_set_item_component>
  <code>variable::set_item_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set the item component\
**Type:** An action that returns a value\
**Description:** It sets the subject with the component with the specified value and assigns the subject to the variable.

**Usage example:** 
```ts
a1 = variable::set_item_component(item("stick"),"component","any value");

#Or from the object

a1 = item("stick").set_item_component("component","any value");

#Or dry

variable::set_item_component(a1,item("stick"),"component","any value");
```

**Arguments:**

| **Name**    | **Type**  | **Description** |
| ----------- | --------- | --------------- |
| `variable`  | Variable  | Variable        |
| `item`      | Item      | Item            |
| `component` | Text      | Component key   |
| `value`     | Any Value | Meaning         |
<h3 id=set_variable_set_item_custom_model_data>
  <code>variable::set_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Model Data\
**Type:** An action that returns a value\
**Description:** Sets the item's model data (CustomModelData) and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_custom_model_data(item("stick"),1);

#Or from the object

a1 = item("stick").set_item_custom_model_data(1);

#Or dry

variable::set_item_custom_model_data(a1,item("stick"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
| `model`    | Number   | Model Number       |
<h3 id=set_variable_set_item_custom_tag>
  <code>variable::set_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Custom Item Tag\
**Type:** An action that returns a value\
**Description:** Sets a custom tag for an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_custom_tag(item("stick"),"tag_name","tag_value");

#Or from the object

a1 = item("stick").set_item_custom_tag("tag_name","tag_value");

#Or dry

variable::set_item_custom_tag(a1,item("stick"),"tag_name","tag_value");
```

**Arguments:**

| **Name**    | **Type** | **Description**    |
| ----------- | -------- | ------------------ |
| `variable`  | Variable | Variable to assign |
| `item`      | Item     | Item               |
| `tag_name`  | Text     | Tag Name           |
| `tag_value` | Text     | Tag Value          |
<h3 id=set_variable_set_item_destroyable_blocks>
  <code>variable::set_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Breakeble Blocks\
**Type:** An action that returns a value\
**Description:** Sets an item with the blocks it can break and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_destroyable_blocks([item("stick"), item("stick")],item("stick"));

#Or from the object

a1 = item("stick").set_item_destroyable_blocks([item("stick"), item("stick")]);

#Or dry

variable::set_item_destroyable_blocks(a1,[item("stick"), item("stick")],item("stick"));
```

**Arguments:**

| **Name**      | **Type**   | **Description**                 |
| ------------- | ---------- | ------------------------------- |
| `variable`    | Variable   | Variable to assign              |
| `destroyable` | list[Item] | Blocks Can Be Destroyed by Item |
| `item`        | Item       | Item                            |
<h3 id=set_variable_set_item_durability>
  <code>variable::set_item_durability</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Durability\
**Type:** An action that returns a value\
**Description:** Sets an item's durability and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_durability(item("stick"),1,"DAMAGE");

#Or from the object

a1 = item("stick").set_item_durability(1,"DAMAGE");

#Or dry

variable::set_item_durability(a1,item("stick"),1,"DAMAGE");
```

**Arguments:**

| **Name**          | **Type**                                                                                                                                                                                                                                      | **Description**    |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`        | Variable                                                                                                                                                                                                                                      | Variable to Assign |
| `item`            | Item                                                                                                                                                                                                                                          | Item               |
| `durability`      | Number                                                                                                                                                                                                                                        | New Durability     |
| `durability_type` | Marker<br/>**DAMAGE** - Current Durability<br/>**DAMAGE_PERCENTAGE** - Current Durability Percentage<br/>**REMAINING** - Remaining Durability<br/>**REMAINING_PERCENTAGE** - Remaining Durability Percentage<br/>**MAXIMUM** - Max Durability | Durability Type    |
<h3 id=set_variable_set_item_enchantments>
  <code>variable::set_item_enchantments</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Enchantments\
**Type:** An action that returns a value\
**Description:** Sets an enchantment on an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_enchantments(item("stick"),`enchantments`);

#Or from the object

a1 = item("stick").set_item_enchantments(`enchantments`);

#Or dry

variable::set_item_enchantments(a1,item("stick"),`enchantments`);
```

**Arguments:**

| **Name**       | **Type**   | **Description**               |
| -------------- | ---------- | ----------------------------- |
| `variable`     | Variable   | Variable to assign            |
| `item`         | Item       | Item                          |
| `enchantments` | Dictionary | Enchantments and their levels |
<h3 id=set_variable_set_item_lore>
  <code>variable::set_item_lore</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Description\
**Type:** An action that returns a value\
**Description:** Sets the item's description.\
**Additional info:**\
&nbsp;&nbsp;Clears the description if no new one is specified.

**Usage example:** 
```ts
a1 = variable::set_item_lore(["lore", "lore"],item("stick"));

#Or from the object

a1 = item("stick").set_item_lore(["lore", "lore"]);

#Or dry

variable::set_item_lore(a1,["lore", "lore"],item("stick"));
```

**Arguments:**

| **Name**   | **Type**   | **Description**    |
| ---------- | ---------- | ------------------ |
| `variable` | Variable   | Variable to assign |
| `lore`     | list[Text] | New Description    |
| `item`     | Item       | Item               |
<h3 id=set_variable_set_item_lore_line>
  <code>variable::set_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Description Line\
**Type:** An action that returns a value\
**Description:** Sets the item's description line.

**Usage example:** 
```ts
a1 = variable::set_item_lore_line(item("stick"),"text",1,"MERGE");

#Or from the object

a1 = item("stick").set_item_lore_line("text",1,"MERGE");

#Or dry

variable::set_item_lore_line(a1,item("stick"),"text",1,"MERGE");
```

**Arguments:**

| **Name**   | **Type**                                               | **Description**    |
| ---------- | ------------------------------------------------------ | ------------------ |
| `variable` | Variable                                               | Variable to assign |
| `item`     | Item                                                   | Item               |
| `text`     | Text                                                   | New Description    |
| `line`     | Number                                                 | Line Number        |
| `mode`     | Marker<br/>**MERGE** - Replace<br/>**APPEND** - Append | Set Mode           |
<h3 id=set_variable_set_item_max_stack_size>
  <code>variable::set_item_max_stack_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set the maximum number of items\
**Type:** Action without value\
**Description:** Sets the maximum number of items in a glass for the specified item and assigns it to the variable.\
**Additional info:**\
&nbsp;&nbsp;The number of items in a glass can only be from 1 to 99.\
&nbsp;&nbsp;The value 0 will return the maximum amount to the default value.

**Usage example:** 
```ts
variable::set_item_max_stack_size(a1,item("stick"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**                    |
| ---------- | -------- | ---------------------------------- |
| `variable` | Variable | Variable                           |
| `item`     | Item     | Item                               |
| `size`     | Number   | The number of objects in the glass |
<h3 id=set_variable_set_item_name>
  <code>variable::set_item_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Name\
**Type:** An action that returns a value\
**Description:** Sets the item's display name.

**Usage example:** 
```ts
a1 = variable::set_item_name(item("stick"),"text");

#Or from the object

a1 = item("stick").set_item_name("text");

#Or dry

variable::set_item_name(a1,item("stick"),"text");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
| `text`     | Text     | Name               |
<h3 id=set_variable_set_item_placeable_blocks>
  <code>variable::set_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Placeable Blocks\
**Type:** An action that returns a value\
**Description:** Sets an item to placeable blocks and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_placeable_blocks([item("stick"), item("stick")],item("stick"));

#Or from the object

a1 = item("stick").set_item_placeable_blocks([item("stick"), item("stick")]);

#Or dry

variable::set_item_placeable_blocks(a1,[item("stick"), item("stick")],item("stick"));
```

**Arguments:**

| **Name**    | **Type**   | **Description**    |
| ----------- | ---------- | ------------------ |
| `variable`  | Variable   | Variable to assign |
| `placeable` | list[Item] | Placeable Blocks   |
| `item`      | Item       | Item               |
<h3 id=set_variable_set_item_type>
  <code>variable::set_item_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Type\
**Type:** An action that returns a value\
**Description:** Changes the type of item without changing the other data of the item.

**Usage example:** 
```ts
a1 = variable::set_item_type(item("stick"),"type");

#Or from the object

a1 = item("stick").set_item_type("type");

#Or dry

variable::set_item_type(a1,item("stick"),"type");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `item`     | Item     | Item               |
| `type`     | Text     | Item Type          |
<h3 id=set_variable_set_item_unbreakable>
  <code>variable::set_item_unbreakable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Unbreakable\
**Type:** An action that returns a value\
**Description:** Sets an item's unbreakable and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_unbreakable(item("stick"),"TRUE");

#Or from the object

a1 = item("stick").set_item_unbreakable("TRUE");

#Or dry

variable::set_item_unbreakable(a1,item("stick"),"TRUE");
```

**Arguments:**

| **Name**      | **Type**                                             | **Description**    |
| ------------- | ---------------------------------------------------- | ------------------ |
| `variable`    | Variable                                             | Variable to assign |
| `item`        | Item                                                 | Item               |
| `unbreakable` | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable | Unbreakable        |
<h3 id=set_variable_set_item_visibility_flags>
  <code>variable::set_item_visibility_flags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Visibility Flags\
**Type:** An action that returns a value\
**Description:** Sets certain item visibility flags and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_visibility_flags(item("stick"),"ON","ON","ON","ON","ON","ON","ON","ON");

#Or from the object

a1 = item("stick").set_item_visibility_flags("ON","ON","ON","ON","ON","ON","ON","ON");

#Or dry

variable::set_item_visibility_flags(a1,item("stick"),"ON","ON","ON","ON","ON","ON","ON","ON");
```

**Arguments:**

| **Name**              | **Type**                                                                         | **Description**           |
| --------------------- | -------------------------------------------------------------------------------- | ------------------------- |
| `variable`            | Variable                                                                         | Variable to assign        |
| `item`                | Item                                                                             | Item                      |
| `hide_dye`            | Marker<br/>**ON** - Enabled<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off      | Hide color                |
| `hide_enchantments`   | Marker<br/>**ON** - Enabled<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off      | Hide Enchantments         |
| `hide_attributes`     | Marker<br/>**ON** - Enabled<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off      | Hide Attributes           |
| `hide_unbreakable`    | Marker<br/>**ON** - Enabled<br/>**NO_CHANGE** - No Change<br/>**OFF** - Disabled | Hide Unbreakable          |
| `hide_place_on`       | Marker<br/>**ON** - Enabled<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off      | Hide \"Can be placed on\" |
| `hide_destroys`       | Marker<br/>**ON** - Enabled<br/>**NO_CHANGE** - No Change<br/>**OFF** - Off      | Hide \"Can break\"        |
| `hide_potion_effects` | Marker<br/>**ON** - Enabled<br/>**NO_CHANGE** - No Change<br/>**OFF** - Disabled | Hide stats                |
| `hide_armor_trim`     | Marker<br/>**ON** - Enabled<br/>**NO_CHANGE** - No Change<br/>**OFF** - Disabled | Hide Armor Trim           |
<h3 id=set_variable_set_list_value>
  <code>variable::set_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set List Value\
**Type:** An action that returns a value\
**Description:** Sets the list value at the specified index.

**Usage example:** 
```ts
a1 = variable::set_list_value(`list`,1,"any value");

#Or from the object

a1 = `list`.set_list_value(1,"any value");

#Or dry

variable::set_list_value(a1,`list`,1,"any value");
```

**Arguments:**

| **Name**   | **Type**  | **Description**    |
| ---------- | --------- | ------------------ |
| `variable` | Variable  | Variable to assign |
| `list`     | List      | List               |
| `number`   | Number    | Index              |
| `value`    | Any Value | Value              |
<h3 id=set_variable_set_location_direction>
  <code>variable::set_location_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Location Direction\
**Type:** An action that returns a value\
**Description:** Sets the location direction and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_location_direction(location(0,0,0,0,0),vector(0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).set_location_direction(vector(0,0,0));

#Or dry

variable::set_location_direction(a1,location(0,0,0,0,0),vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**     |
| ---------- | -------- | ------------------- |
| `variable` | Variable | Variable to Assign  |
| `location` | Location | Location to install |
| `vector`   | Vector   | Direction Vector    |
<h3 id=set_variable_set_map_value>
  <code>variable::set_map_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Dictionary Value\
**Type:** An action that returns a value\
**Description:** Sets a specific dictionary value by key and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_map_value(`map`,"any value","any value");

#Or from the object

a1 = `map`.set_map_value("any value","any value");

#Or dry

variable::set_map_value(a1,`map`,"any value","any value");
```

**Arguments:**

| **Name**   | **Type**   | **Description**      |
| ---------- | ---------- | -------------------- |
| `variable` | Variable   | Variable to assign   |
| `map`      | Dictionary | Dictionary to change |
| `key`      | Any Value  | Key                  |
| `value`    | Any Value  | New Value            |
<h3 id=set_variable_set_particle_amount>
  <code>variable::set_particle_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Amount\
**Type:** An action that returns a value\
**Description:** Sets the amount of particles and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_particle_amount(particle("fire"),1);

#Or from the object

a1 = particle("fire").set_particle_amount(1);

#Or dry

variable::set_particle_amount(a1,particle("fire"),1);
```

**Arguments:**

| **Name**   | **Type**        | **Description**    |
| ---------- | --------------- | ------------------ |
| `variable` | Variable        | Variable to Assign |
| `particle` | Particle Effect | Particle to Change |
| `amount`   | Number          | New Amount         |
<h3 id=set_variable_set_particle_color>
  <code>variable::set_particle_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Color\
**Type:** An action that returns a value\
**Description:** Sets the particle color and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_particle_color(particle("fire"),"hex_color","COLOR");

#Or from the object

a1 = particle("fire").set_particle_color("hex_color","COLOR");

#Or dry

variable::set_particle_color(a1,particle("fire"),"hex_color","COLOR");
```

**Arguments:**

| **Name**     | **Type**                                                                              | **Description**    |
| ------------ | ------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable                                                                              | Variable to assign |
| `particle`   | Particle Effect                                                                       | Particle to change |
| `hex_color`  | Text                                                                                  | HEX color          |
| `color_type` | Marker<br/>**COLOR** - The usual color<br/>**TO_COLOR** - The color of the transition | Type of color      |
<h3 id=set_variable_set_particle_material>
  <code>variable::set_particle_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Material\
**Type:** An action that returns a value\
**Description:** Sets the particle material and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_particle_material(particle("fire"),item("stick"));

#Or from the object

a1 = particle("fire").set_particle_material(item("stick"));

#Or dry

variable::set_particle_material(a1,particle("fire"),item("stick"));
```

**Arguments:**

| **Name**   | **Type**        | **Description**    |
| ---------- | --------------- | ------------------ |
| `variable` | Variable        | Variable to assign |
| `particle` | Particle Effect | Particle to change |
| `material` | Item            | New Material       |
<h3 id=set_variable_set_particle_offset>
  <code>variable::set_particle_offset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Motion\
**Type:** An action that returns a value\
**Description:** Sets the movement of a particle and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_particle_offset(particle("fire"),vector(0,0,0));

#Or from the object

a1 = particle("fire").set_particle_offset(vector(0,0,0));

#Or dry

variable::set_particle_offset(a1,particle("fire"),vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type**        | **Description**    |
| ---------- | --------------- | ------------------ |
| `variable` | Variable        | Variable to assign |
| `particle` | Particle Effect | Particle to change |
| `offset`   | Vector          | New Motion         |
<h3 id=set_variable_set_particle_size>
  <code>variable::set_particle_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Size\
**Type:** An action that returns a value\
**Description:** Sets the particle size and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_particle_size(particle("fire"),1);

#Or from the object

a1 = particle("fire").set_particle_size(1);

#Or dry

variable::set_particle_size(a1,particle("fire"),1);
```

**Arguments:**

| **Name**   | **Type**        | **Description**    |
| ---------- | --------------- | ------------------ |
| `variable` | Variable        | Variable to assign |
| `particle` | Particle Effect | Particle to change |
| `size`     | Number          | New Size           |
<h3 id=set_variable_set_particle_spread>
  <code>variable::set_particle_spread</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Spread\
**Type:** An action that returns a value\
**Description:** Sets a particle's spread value to a variable.

**Usage example:** 
```ts
a1 = variable::set_particle_spread(particle("fire"),1,2);

#Or from the object

a1 = particle("fire").set_particle_spread(1,2);

#Or dry

variable::set_particle_spread(a1,particle("fire"),1,2);
```

**Arguments:**

| **Name**     | **Type**        | **Description**    |
| ------------ | --------------- | ------------------ |
| `variable`   | Variable        | Variable to assign |
| `particle`   | Particle Effect | Particle to change |
| `horizontal` | Number          | Horizontal Plane   |
| `vertical`   | Number          | Vertical Plane     |
<h3 id=set_variable_set_particle_type>
  <code>variable::set_particle_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Particle Type\
**Type:** An action that returns a value\
**Description:** Sets the particle type and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_particle_type(particle("fire"),"type");

#Or from the object

a1 = particle("fire").set_particle_type("type");

#Or dry

variable::set_particle_type(a1,particle("fire"),"type");
```

**Arguments:**

| **Name**   | **Type**        | **Description**    |
| ---------- | --------------- | ------------------ |
| `variable` | Variable        | Variable to assign |
| `particle` | Particle Effect | Particle to change |
| `type`     | Text            | New Particle Type  |
<h3 id=set_variable_set_potion_effect_amplifier>
  <code>variable::set_potion_effect_amplifier</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Potion Power\
**Type:** An action that returns a value\
**Description:** Sets the power of a potion and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_potion_effect_amplifier(potion("slow_falling"),1);

#Or from the object

a1 = potion("slow_falling").set_potion_effect_amplifier(1);

#Or dry

variable::set_potion_effect_amplifier(a1,potion("slow_falling"),1);
```

**Arguments:**

| **Name**    | **Type** | **Description**    |
| ----------- | -------- | ------------------ |
| `variable`  | Variable | Variable to assign |
| `potion`    | Potion   | Potion             |
| `amplifier` | Number   | Potion Power       |
<h3 id=set_variable_set_potion_effect_duration>
  <code>variable::set_potion_effect_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Potion Duration\
**Type:** An action that returns a value\
**Description:** Sets the duration of a potion and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_potion_effect_duration(potion("slow_falling"),1);

#Or from the object

a1 = potion("slow_falling").set_potion_effect_duration(1);

#Or dry

variable::set_potion_effect_duration(a1,potion("slow_falling"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `potion`   | Potion   | Potion             |
| `duration` | Number   | Duration           |
<h3 id=set_variable_set_potion_effect_type>
  <code>variable::set_potion_effect_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Potion Effect\
**Type:** An action that returns a value\
**Description:** Sets the effect of a potion and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_potion_effect_type(potion("slow_falling"),"effect_type");

#Or from the object

a1 = potion("slow_falling").set_potion_effect_type("effect_type");

#Or dry

variable::set_potion_effect_type(a1,potion("slow_falling"),"effect_type");
```

**Arguments:**

| **Name**      | **Type** | **Description**    |
| ------------- | -------- | ------------------ |
| `variable`    | Variable | Variable to assign |
| `potion`      | Potion   | Potion             |
| `effect_type` | Text     | Effect ID          |
<h3 id=set_variable_set_sound_pitch>
  <code>variable::set_sound_pitch</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Pitch\
**Type:** An action that returns a value\
**Description:** Sets the pitch of a sound and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_sound_pitch(sound("entity.zombie.hurt"),1);

#Or from the object

a1 = sound("entity.zombie.hurt").set_sound_pitch(1);

#Or dry

variable::set_sound_pitch(a1,sound("entity.zombie.hurt"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `sound`    | Sound    | Sound to change    |
| `pitch`    | Number   | New Pitch Value    |
<h3 id=set_variable_set_sound_source>
  <code>variable::set_sound_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Source\
**Type:** An action that returns a value\
**Description:** Sets the sound source and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_sound_source(sound("entity.zombie.hurt"),"MASTER");

#Or from the object

a1 = sound("entity.zombie.hurt").set_sound_source("MASTER");

#Or dry

variable::set_sound_source(a1,sound("entity.zombie.hurt"),"MASTER");
```

**Arguments:**

| **Name**   | **Type**                                                                                                                                                                                                                                                                                                                                                                             | **Description**    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| `variable` | Variable                                                                                                                                                                                                                                                                                                                                                                             | Variable to assign |
| `sound`    | Sound                                                                                                                                                                                                                                                                                                                                                                                | Sound to change    |
| `source`   | Marker<br/>**MASTER** - General (master)<br/>**MUSIC** - Music (music)<br/>**RECORD** - Music Blocks (record)<br/>**WEATHER** - Weather (weather)<br/>**BLOCK** - Blocks<br/>**HOSTILE** - Hostile Creatures (hostile)<br/>**NEUTRAL** - Friendly Creatures (neutral)<br/>**PLAYER** - Players (player)<br/>**AMBIENT** - Environment (ambient)<br/>**VOICE** - Voice/Speech (voice) | Sound Source       |
<h3 id=set_variable_set_sound_type>
  <code>variable::set_sound_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Type\
**Type:** An action that returns a value\
**Description:** Sets the sound type and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_sound_type(sound("entity.zombie.hurt"),"namespace","value");

#Or from the object

a1 = sound("entity.zombie.hurt").set_sound_type("namespace","value");

#Or dry

variable::set_sound_type(a1,sound("entity.zombie.hurt"),"namespace","value");
```

**Arguments:**

| **Name**    | **Type** | **Description**             |
| ----------- | -------- | --------------------------- |
| `variable`  | Variable | Variable to assign          |
| `sound`     | Sound    | Sound to set                |
| `namespace` | Text     | Namespace (minecraft\: etc) |
| `value`     | Text     | Sound ID                    |
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
a1 = variable::set_sound_variation(sound("entity.zombie.hurt"),"variation");

#Or from the object

a1 = sound("entity.zombie.hurt").set_sound_variation("variation");

#Or dry

variable::set_sound_variation(a1,sound("entity.zombie.hurt"),"variation");
```

**Arguments:**

| **Name**    | **Type** | **Description**    |
| ----------- | -------- | ------------------ |
| `variable`  | Variable | Variable to assign |
| `sound`     | Sound    | Sound to change    |
| `variation` | Text     | Variation          |
<h3 id=set_variable_set_sound_volume_action>
  <code>variable::set_sound_volume_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Volume\
**Type:** An action that returns a value\
**Description:** Sets the sound volume and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_sound_volume_action(sound("entity.zombie.hurt"),1);

#Or from the object

a1 = sound("entity.zombie.hurt").set_sound_volume_action(1);

#Or dry

variable::set_sound_volume_action(a1,sound("entity.zombie.hurt"),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `sound`    | Sound    | Sound to change    |
| `volume`   | Number   | New volume value   |
<h3 id=set_variable_set_template_code>
  <code>variable::set_template_code</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Template Code\
**Type:** An action that returns a value\
**Description:** Sets a code to a template and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_template_code(item("stick"),"any value");

#Or from the object

a1 = item("stick").set_template_code("any value");

#Or dry

variable::set_template_code(a1,item("stick"),"any value");
```

**Arguments:**

| **Name**   | **Type**  | **Description**      |
| ---------- | --------- | -------------------- |
| `variable` | Variable  | Variable to assign   |
| `template` | Item      | Template             |
| `code`     | Any Value | JSON Text/Dictionary |
<h3 id=set_variable_set_texture_to_map>
  <code>variable::set_texture_to_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Map Image\
**Type:** An action that returns a value\
**Description:** Sets the map image at the given link. When the server is restarted, images may disappear, so it is recommended to re-install it on the same maps when starting the world.

**Usage example:** 
```ts
a1 = variable::set_texture_to_map(item("stick"),"url");

#Or from the object

a1 = item("stick").set_texture_to_map("url");

#Or dry

variable::set_texture_to_map(a1,item("stick"),"url");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `map`      | Item     | Map to Set         |
| `url`      | Text     | Image Link         |
<h3 id=set_variable_set_vector_component>
  <code>variable::set_vector_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Vector Coordinate\
**Type:** An action that returns a value\
**Description:** Sets a specific vector coordinate and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_vector_component(vector(0,0,0),1,"X");

#Or from the object

a1 = vector(0,0,0).set_vector_component(1,"X");

#Or dry

variable::set_vector_component(a1,vector(0,0,0),1,"X");
```

**Arguments:**

| **Name**           | **Type**                                                                          | **Description**    |
| ------------------ | --------------------------------------------------------------------------------- | ------------------ |
| `variable`         | Variable                                                                          | Variable to assign |
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
a1 = variable::set_vector_length(vector(0,0,0),1);

#Or from the object

a1 = vector(0,0,0).set_vector_length(1);

#Or dry

variable::set_vector_length(a1,vector(0,0,0),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `vector`   | Vector   | Vector to change   |
| `length`   | Number   | New Length         |
<h3 id=set_variable_shift_all_coordinates>
  <code>variable::shift_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift All Location Coordinates\
**Type:** An action that returns a value\
**Description:** Shifts all location coordinates by certain values.

**Usage example:** 
```ts
a1 = variable::shift_all_coordinates(location(0,0,0,0,0),1,2,3,4,5);

#Or from the object

a1 = location(0,0,0,0,0).shift_all_coordinates(1,2,3,4,5);

#Or dry

variable::shift_all_coordinates(a1,location(0,0,0,0,0),1,2,3,4,5);
```

**Arguments:**

| **Name**   | **Type** | **Description**              |
| ---------- | -------- | ---------------------------- |
| `variable` | Variable | Variable to assign           |
| `location` | Location | Locations to Shift           |
| `x`        | Number   | Shift X                      |
| `y`        | Number   | Shift Y                      |
| `z`        | Number   | Shift Z                      |
| `yaw`      | Number   | Shift by Horizontal Rotation |
| `pitch`    | Number   | Pitch Shift                  |
<h3 id=set_variable_shift_coordinate>
  <code>variable::shift_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift Location Coordinate\
**Type:** An action that returns a value\
**Description:** Shifts a location's coordinate by a certain amount.

**Usage example:** 
```ts
a1 = variable::shift_coordinate(location(0,0,0,0,0),1,"X");

#Or from the object

a1 = location(0,0,0,0,0).shift_coordinate(1,"X");

#Or dry

variable::shift_coordinate(a1,location(0,0,0,0,0),1,"X");
```

**Arguments:**

| **Name**   | **Type**                                                                                                             | **Description**    |
| ---------- | -------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable                                                                                                             | Variable to assign |
| `location` | Location                                                                                                             | Locations to Shift |
| `distance` | Number                                                                                                               | Shift Value        |
| `type`     | Marker<br/>**X** - X<br/>**Y** - Y<br/>**Z** - Z<br/>**PITCH** - Horizontal Rotation<br/>**YAW** - Vertical Rotation | Coordinate Type    |
<h3 id=set_variable_shift_location_in_direction>
  <code>variable::shift_location_in_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift Location In Direction\
**Type:** An action that returns a value\
**Description:** Shifts the location in a certain direction by a certain amount.

**Usage example:** 
```ts
a1 = variable::shift_location_in_direction(location(0,0,0,0,0),1,"FORWARD");

#Or from the object

a1 = location(0,0,0,0,0).shift_location_in_direction(1,"FORWARD");

#Or dry

variable::shift_location_in_direction(a1,location(0,0,0,0,0),1,"FORWARD");
```

**Arguments:**

| **Name**    | **Type**                                                                                         | **Description**    |
| ----------- | ------------------------------------------------------------------------------------------------ | ------------------ |
| `variable`  | Variable                                                                                         | Variable to assign |
| `location`  | Location                                                                                         | Location to Shift  |
| `shift`     | Number                                                                                           | Shift Value        |
| `direction` | Marker<br/>**FORWARD** - Forward/Backward<br/>**UPWARD** - Up/Down<br/>**SIDEWAYS** - Left/Right | Direction          |
<h3 id=set_variable_shift_location_on_vector>
  <code>variable::shift_location_on_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift Location By Vector\
**Type:** An action that returns a value\
**Description:** Shifts the specified location along a vector and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::shift_location_on_vector(location(0,0,0,0,0),vector(0,0,0),1);

#Or from the object

a1 = location(0,0,0,0,0).shift_location_on_vector(vector(0,0,0),1);

#Or dry

variable::shift_location_on_vector(a1,location(0,0,0,0,0),vector(0,0,0),1);
```

**Arguments:**

| **Name**   | **Type** | **Description**           |
| ---------- | -------- | ------------------------- |
| `variable` | Variable | Variable to assign        |
| `location` | Location | Location to Shift         |
| `vector`   | Vector   | Shift Vector              |
| `length`   | Number   | The distance of the shift |
<h3 id=set_variable_shift_location_towards_location>
  <code>variable::shift_location_towards_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Shift Location Towards Location\
**Type:** An action that returns a value\
**Description:** Shifts a location towards a given location by a certain distance and assigns it to a variable.

**Usage example:** 
```ts
a1 = variable::shift_location_towards_location(location(0,0,0,0,0),location(0,0,0,0,0),1);

#Or from the object

a1 = location(0,0,0,0,0).shift_location_towards_location(location(0,0,0,0,0),1);

#Or dry

variable::shift_location_towards_location(a1,location(0,0,0,0,0),location(0,0,0,0,0),1);
```

**Arguments:**

| **Name**        | **Type** | **Description**            |
| --------------- | -------- | -------------------------- |
| `variable`      | Variable | Variable to assign         |
| `location_from` | Location | Location to Shift          |
| `location_to`   | Location | Which Location to Shift To |
| `distance`      | Number   | How much to shift location |
<h3 id=set_variable_simplex_noise_3d>
  <code>variable::simplex_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Simplex Noise\
**Type:** An action that returns a value\
**Description:** Sets the value of the Simplex noise at a specific location to a variable. Returns a number, with a value from -1 to 1.

**Usage example:** 
```ts
a1 = variable::simplex_noise_3d(location(0,0,0,0,0),1,2,3,4,5,"ZERO_TO_ONE","TRUE");

#Or from the object

a1 = location(0,0,0,0,0).simplex_noise_3d(1,2,3,4,5,"ZERO_TO_ONE","TRUE");

#Or dry

variable::simplex_noise_3d(a1,location(0,0,0,0,0),1,2,3,4,5,"ZERO_TO_ONE","TRUE");
```

**Arguments:**

| **Name**        | **Type**                                                                              | **Description**        |
| --------------- | ------------------------------------------------------------------------------------- | ---------------------- |
| `variable`      | Variable                                                                              | Variable to set        |
| `location`      | Location                                                                              | Location to set noise  |
| `seed`          | Number                                                                                | Noise Key              |
| `loc_frequency` | Number                                                                                | Noise Frequency        |
| `octaves`       | Number                                                                                | Noise Octaves          |
| `frequency`     | Number                                                                                | Noise Octave Frequency |
| `amplitude`     | Number                                                                                | Noise Octave Amplitude |
| `range_mode`    | Marker<br/>**ZERO_TO_ONE** - 0 to 1<br/>**FULL_RANGE** - Full Range (-1 to 1 or more) | Value Range            |
| `normalized`    | Marker<br/>**TRUE** - Normalize<br/>**FALSE** - Don't Normalize                       | Normalize Values       |
<h3 id=set_variable_sine>
  <code>variable::sine</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Sine\
**Type:** An action that returns a value\
**Description:** Returns the sine of a number.

**Usage example:** 
```ts
a1 = variable::sine(1,"SINE","DEGREES");

#Or from the object

a1 = (1).sine("SINE","DEGREES");

#Or dry

variable::sine(a1,1,"SINE","DEGREES");
```

**Arguments:**

| **Name**   | **Type**                                                                                       | **Description**    |
| ---------- | ---------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable                                                                                       | Variable to assign |
| `number`   | Number                                                                                         | Number to get sine |
| `variant`  | Marker<br/>**SINE** - Sine<br/>**ARCSINE** - Arcsine<br/>**HYPERBOLIC_SINE** - Hyperbolic Sine | Operation Type     |
| `input`    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                     | Angle Type         |
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
a1 = variable::sort_list(`list`,"ASCENDING");

#Or from the object

a1 = `list`.sort_list("ASCENDING");

#Or dry

variable::sort_list(a1,`list`,"ASCENDING");
```

**Arguments:**

| **Name**    | **Type**                                                             | **Description**    |
| ----------- | -------------------------------------------------------------------- | ------------------ |
| `variable`  | Variable                                                             | Variable to assign |
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
a1 = variable::sort_map(`map`,"ASCENDING","KEYS");

#Or from the object

a1 = `map`.sort_map("ASCENDING","KEYS");

#Or dry

variable::sort_map(a1,`map`,"ASCENDING","KEYS");
```

**Arguments:**

| **Name**     | **Type**                                                             | **Description**    |
| ------------ | -------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable                                                             | Variable to assign |
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
a1 = variable::split_text("text","delimiter");

#Or from the object

a1 = "text".split_text("delimiter");

#Or dry

variable::split_text(a1,"text","delimiter");
```

**Arguments:**

| **Name**    | **Type** | **Description**    |
| ----------- | -------- | ------------------ |
| `variable`  | Variable | Variable to assign |
| `text`      | Text     | Split Text         |
| `delimiter` | Text     | Delimiter          |
<h3 id=set_variable_strip_text>
  <code>variable::strip_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Spaces\
**Type:** An action that returns a value\
**Description:** Removes spaces from text and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::strip_text("text","ALL");

#Or from the object

a1 = "text".strip_text("ALL");

#Or dry

variable::strip_text(a1,"text","ALL");
```

**Arguments:**

| **Name**     | **Type**                                                                                                | **Description**    |
| ------------ | ------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`   | Variable                                                                                                | Variable to assign |
| `text`       | Text                                                                                                    | Text to change     |
| `strip_type` | Marker<br/>**ALL** - Start and End<br/>**START** - Start<br/>**END** - End<br/>**INDENT** - Indentation | Strip Type         |
<h3 id=set_variable_subtract>
  <code>variable::subtract</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Number Subtraction (-)\
**Type:** An action that returns a value\
**Description:** Assigns a difference of numbers to a variable.

**Usage example:** 
```ts
a1 = variable::subtract([1, 2]);

#Or dry

variable::subtract(a1,[1, 2]);
```

**Arguments:**

| **Name**   | **Type**     | **Description**     |
| ---------- | ------------ | ------------------- |
| `variable` | Variable     | Variable to assign  |
| `value`    | list[Number] | Numbers to Subtract |
<h3 id=set_variable_subtract_vectors>
  <code>variable::subtract_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Vector Difference\
**Type:** An action that returns a value\
**Description:** Sets a vector difference value to a variable.

**Usage example:** 
```ts
a1 = variable::subtract_vectors([vector(0,0,0), vector(0,0,0)]);

#Or dry

variable::subtract_vectors(a1,[vector(0,0,0), vector(0,0,0)]);
```

**Arguments:**

| **Name**   | **Type**     | **Description**    |
| ---------- | ------------ | ------------------ |
| `variable` | Variable     | Variable to assign |
| `vectors`  | list[Vector] | Difference Vectors |
<h3 id=set_variable_tangent>
  <code>variable::tangent</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Tangent\
**Type:** An action that returns a value\
**Description:** Returns the tangent of a number.

**Usage example:** 
```ts
a1 = variable::tangent(1,"TANGENT","DEGREES");

#Or from the object

a1 = (1).tangent("TANGENT","DEGREES");

#Or dry

variable::tangent(a1,1,"TANGENT","DEGREES");
```

**Arguments:**

| **Name**   | **Type**                                                                                                         | **Description**       |
| ---------- | ---------------------------------------------------------------------------------------------------------------- | --------------------- |
| `variable` | Variable                                                                                                         | Variable to assign    |
| `number`   | Number                                                                                                           | Number to get tangent |
| `variant`  | Marker<br/>**TANGENT** - Tangent<br/>**ARCTANGENT** - Arctangent<br/>**HYPERBOLIC_TANGENT** - Hyperbolic Tangent | Operation Type        |
| `input`    | Marker<br/>**DEGREES** - Degrees<br/>**RADIANS** - Radians                                                       | Angle Type            |
<h3 id=set_variable_text>
  <code>variable::set_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text\
**Type:** An action that returns a value\
**Description:** Concatenates and assigns one or more text values to a variable.

**Usage example:** 
```ts
a1 = variable::set_text(["text", "text"],"SPACES");

#Or dry

variable::set_text(a1,["text", "text"],"SPACES");
```

**Arguments:**

| **Name**   | **Type**                                                                                                       | **Description**    |
| ---------- | -------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable                                                                                                       | Variable to assign |
| `text`     | list[Text]                                                                                                     | Text to set        |
| `merging`  | Marker<br/>**SPACES** - Space Separation<br/>**CONCATENATION** - Merge<br/>**SEPARATE_LINES** - Separate Lines | Merge Text         |
<h3 id=set_variable_text_case>
  <code>variable::set_text_case</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Text Case\
**Type:** An action that returns a value\
**Description:** Sets the text case and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_text_case("text","UPPER");

#Or from the object

a1 = "text".set_text_case("UPPER");

#Or dry

variable::set_text_case(a1,"text","UPPER");
```

**Arguments:**

| **Name**    | **Type**                                                                                                                            | **Description**    |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable`  | Variable                                                                                                                            | Variable to assign |
| `text`      | Text                                                                                                                                | Text to set        |
| `case_type` | Marker<br/>**UPPER** - Upper<br/>**LOWER** - Lower<br/>**PROPER** - First character<br/>**INVERT** - Invert<br/>**RANDOM** - Random | Case Type          |
<h3 id=set_variable_text_length>
  <code>variable::get_text_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Text Length\
**Type:** An action that returns a value\
**Description:** Sets the number of characters in text to a variable.

**Usage example:** 
```ts
a1 = variable::get_text_length("text");

#Or from the object

a1 = "text".get_text_length();

#Or dry

variable::get_text_length(a1,"text");
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `text`     | Text     | Text to Get Length |
<h3 id=set_variable_to_char>
  <code>variable::to_char</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Character By Number\
**Type:** An action that returns a value\
**Description:** Get a specific character from a number and assign the result to a variable.

**Usage example:** 
```ts
a1 = variable::to_char(1);

#Or from the object

a1 = (1).to_char();

#Or dry

variable::to_char(a1,1);
```

**Arguments:**

| **Name**   | **Type** | **Description**         |
| ---------- | -------- | ----------------------- |
| `variable` | Variable | Variable to assign      |
| `number`   | Number   | Number to get character |
<h3 id=set_variable_to_hsb>
  <code>variable::to_hsb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create HSB Color\
**Type:** An action that returns a value\
**Description:** Creates a HEX color based on hue, saturation and lightness.

**Usage example:** 
```ts
a1 = variable::to_hsb(1,2,3);

#Or dry

variable::to_hsb(a1,1,2,3);
```

**Arguments:**

| **Name**     | **Type** | **Description**      |
| ------------ | -------- | -------------------- |
| `variable`   | Variable | Variable to assign   |
| `hue`        | Number   | Hue (0 - 360)        |
| `saturation` | Number   | Saturation (0 - 100) |
| `brightness` | Number   | Brightness (0 - 100) |
<h3 id=set_variable_to_hsl>
  <code>variable::to_hsl</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create HSL Color\
**Type:** An action that returns a value\
**Description:** Creates a HEX color based on Hue, Saturation and Lightness.

**Usage example:** 
```ts
a1 = variable::to_hsl(1,2,3);

#Or dry

variable::to_hsl(a1,1,2,3);
```

**Arguments:**

| **Name**     | **Type** | **Description**      |
| ------------ | -------- | -------------------- |
| `variable`   | Variable | Variable to assign   |
| `hue`        | Number   | Hue (0 - 360)        |
| `saturation` | Number   | Saturation (0 - 100) |
| `lightness`  | Number   | Lightness (0 - 100)  |
<h3 id=set_variable_to_json>
  <code>variable::to_json</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Convert To JSON\
**Type:** An action that returns a value\
**Description:** Converts dictionaries and lists to JSON text.

**Usage example:** 
```ts
a1 = variable::to_json("any value","TRUE");

#Or dry

variable::to_json(a1,"any value","TRUE");
```

**Arguments:**

| **Name**       | **Type**                                             | **Description**             |
| -------------- | ---------------------------------------------------- | --------------------------- |
| `variable`     | Variable                                             | To write result             |
| `value`        | Any Value                                            | List/Dictionary with values |
| `pretty_print` | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable | Format Pretty Print         |
<h3 id=set_variable_to_rgb>
  <code>variable::to_rgb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create RGB Color\
**Type:** An action that returns a value\
**Description:** Creates a HEX color based on the red, green and blue channels.

**Usage example:** 
```ts
a1 = variable::to_rgb(1,2,3);

#Or dry

variable::to_rgb(a1,1,2,3);
```

**Arguments:**

| **Name**   | **Type** | **Description**         |
| ---------- | -------- | ----------------------- |
| `variable` | Variable | Variable to assign      |
| `red`      | Number   | Red Channel (0 - 255)   |
| `green`    | Number   | Green Channel (0 - 255) |
| `blue`     | Number   | Blue channel (0 - 255)  |
<h3 id=set_variable_trim_list>
  <code>variable::trim_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Trim List\
**Type:** An action that returns a value\
**Description:** Returns a list containing the elements of the specified list that start and end at the specified indexes.

**Usage example:** 
```ts
a1 = variable::trim_list(`list`,1,2);

#Or from the object

a1 = `list`.trim_list(1,2);

#Or dry

variable::trim_list(a1,`list`,1,2);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `list`     | List     | List               |
| `start`    | Number   | Start Index        |
| `end`      | Number   | End index          |
<h3 id=set_variable_trim_text>
  <code>variable::trim_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Trim Text\
**Type:** An action that returns a value\
**Description:** Trims text and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::trim_text("text",1,2);

#Or from the object

a1 = "text".trim_text(1,2);

#Or dry

variable::trim_text(a1,"text",1,2);
```

**Arguments:**

| **Name**   | **Type** | **Description** |
| ---------- | -------- | --------------- |
| `variable` | Variable | Variable to set |
| `text`     | Text     | Text to Trim    |
| `start`    | Number   | Start Position  |
| `end`      | Number   | End Position    |
<h3 id=set_variable_value>
  <code>variable::set_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Value (=)\
**Type:** An action that returns a value\
**Description:** Assigns a value to a variable.

**Usage example:** 
```ts
a1 = variable::set_value("any value");

#Or dry

variable::set_value(a1,"any value");
```

**Arguments:**

| **Name**   | **Type**  | **Description**    |
| ---------- | --------- | ------------------ |
| `variable` | Variable  | Variable to assign |
| `value`    | Any Value | Value to assign    |
<h3 id=set_variable_vector>
  <code>variable::set_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Vector\
**Type:** An action that returns a value\
**Description:** Creates a vector from the specified coordinates and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_vector(1,2,3);

#Or dry

variable::set_vector(a1,1,2,3);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `x`        | Number   | X Coordinate       |
| `y`        | Number   | Y Coordinate       |
| `z`        | Number   | Z Coordinate       |
<h3 id=set_variable_vector_cross_product>
  <code>variable::vector_cross_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Vector Product Of Two Vectors\
**Type:** An action that returns a value\
**Description:** Sets the cross product of two vectors to a variable.

**Usage example:** 
```ts
a1 = variable::vector_cross_product(vector(0,0,0),vector(0,0,0));

#Or dry

variable::vector_cross_product(a1,vector(0,0,0),vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `vector_1` | Vector   | First Vector       |
| `vector_2` | Vector   | Second Vector      |
<h3 id=set_variable_vector_dot_product>
  <code>variable::vector_dot_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dot Product Of Two Vectors\
**Type:** An action that returns a value\
**Description:** Sets the dot product of two vectors to a variable.

**Usage example:** 
```ts
a1 = variable::vector_dot_product(vector(0,0,0),vector(0,0,0));

#Or dry

variable::vector_dot_product(a1,vector(0,0,0),vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `vector_1` | Vector   | First Vector       |
| `vector_2` | Vector   | Second Vector      |
<h3 id=set_variable_vector_to_direction_name>
  <code>variable::vector_to_direction_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Direction By Vector\
**Type:** An action that returns a value\
**Description:** Sets to variable which direction the vector is pointing.

**Usage example:** 
```ts
a1 = variable::vector_to_direction_name(vector(0,0,0));

#Or from the object

a1 = vector(0,0,0).vector_to_direction_name();

#Or dry

variable::vector_to_direction_name(a1,vector(0,0,0));
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `vector`   | Vector   | Vector to get      |
<h3 id=set_variable_voronoi_noise_3d>
  <code>variable::voronoi_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Voronoi Noise\
**Type:** An action that returns a value\
**Description:** Sets the value of the Voronoi noise at a specific location to a variable. Returns a number, with a value between 0 and 1.

**Usage example:** 
```ts
a1 = variable::voronoi_noise_3d(location(0,0,0,0,0),1,2,3,"ZERO_TO_ONE","TRUE");

#Or from the object

a1 = location(0,0,0,0,0).voronoi_noise_3d(1,2,3,"ZERO_TO_ONE","TRUE");

#Or dry

variable::voronoi_noise_3d(a1,location(0,0,0,0,0),1,2,3,"ZERO_TO_ONE","TRUE");
```

**Arguments:**

| **Name**          | **Type**                                                         | **Description**       |
| ----------------- | ---------------------------------------------------------------- | --------------------- |
| `variable`        | Variable                                                         | Variable to assign    |
| `location`        | Location                                                         | Location to set noise |
| `seed`            | Number                                                           | Noise Key             |
| `frequency`       | Number                                                           | Noise Frequency       |
| `displacement`    | Number                                                           | Noise Displacement    |
| `range_mode`      | Marker<br/>**ZERO_TO_ONE** - 0 to 1<br/>**FULL_RANGE** - -1 to 1 | Value Range           |
| `enable_distance` | Marker<br/>**TRUE** - Enable<br/>**FALSE** - Disable             | Distance Mode         |
<h3 id=set_variable_warp>
  <code>variable::warp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Wrap Number\
**Type:** An action that returns a value\
**Description:** Checks if a number is between two borders, and if not, wraps it around that border.

**Usage example:** 
```ts
a1 = variable::warp(1,2,3);

#Or from the object

a1 = (1).warp(2,3);

#Or dry

variable::warp(a1,1,2,3);
```

**Arguments:**

| **Name**   | **Type** | **Description**    |
| ---------- | -------- | ------------------ |
| `variable` | Variable | Variable to assign |
| `number`   | Number   | Number to wrap     |
| `min`      | Number   | Minimum Value      |
| `max`      | Number   | Max Value          |
