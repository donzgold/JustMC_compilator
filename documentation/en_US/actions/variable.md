<h3 id=if_variable_equals>
  <code>variable::equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a variable is equal to at least one of the compared values.

**Usage example:** 
```ts
if(variable::equals("any value",["any value", "any value"]){
    player::message("Condition is true");
}

#Or from the object

if("any value".equals(["any value", "any value"]){
    player::message("Condition is true");
}
```

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

<h3 id=if_variable_item_has_enchantment>
  <code>variable::item_has_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

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

<h3 id=if_variable_item_has_tag>
  <code>variable::item_has_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Item Has Custom Tag\
**Type:** Action that checks the conditions\
**Description:** Checks if an item variable has the specified tag with the selected value.

**Usage example:** 
```ts
if(variable::item_has_tag(item("stick"),"tag","value"){
    player::message("Condition is true");
}

#Or from the object

if(item("stick").item_has_tag("tag","value"){
    player::message("Condition is true");
}
```

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

<h3 id=if_variable_list_contains_value>
  <code>variable::list_contains_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** List Contains Value\
**Type:** Action that checks the conditions\
**Description:** Checks if a list contains a specific value.

**Usage example:** 
```ts
if(variable::list_contains_value(`list`,["any value", "any value"],"ANY"){
    player::message("Condition is true");
}

#Or from the object

if(`list`.list_contains_value(["any value", "any value"],"ANY"){
    player::message("Condition is true");
}
```

<h3 id=if_variable_list_value_equals>
  <code>variable::list_value_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** List Value Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the value of a list item is equal to at least one value being compared.

**Usage example:** 
```ts
if(variable::list_value_equals(`list`,1,["any value", "any value"]){
    player::message("Condition is true");
}

#Or from the object

if(`list`.list_value_equals(1,["any value", "any value"]){
    player::message("Condition is true");
}
```

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

<h3 id=if_variable_location_is_near>
  <code>variable::location_is_near</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Near Location\
**Type:** Action that checks the conditions\
**Description:** Checks if a location variable is near the specified location.

**Usage example:** 
```ts
if(variable::location_is_near(location(0,0,0,0,0),1,[location(0,0,0,0,0), location(0,0,0,0,0)],"SPHERE"){
    player::message("Condition is true");
}

#Or from the object

if(location(0,0,0,0,0).location_is_near(1,[location(0,0,0,0,0), location(0,0,0,0,0)],"SPHERE"){
    player::message("Condition is true");
}
```

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

<h3 id=if_variable_map_value_equals>
  <code>variable::map_value_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Dictionary Value Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if the value of a dictionary element by key is equal to at least one value being compared.

**Usage example:** 
```ts
if(variable::map_value_equals(`map`,"any value",["any value", "any value"]){
    player::message("Condition is true");
}

#Or from the object

if(`map`.map_value_equals("any value",["any value", "any value"]){
    player::message("Condition is true");
}
```

<h3 id=if_variable_not_equals>
  <code>variable::not_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Not Equals\
**Type:** Action that checks the conditions\
**Description:** Checks if a variable is equal to at least one of the values being compared.

**Usage example:** 
```ts
if(variable::not_equals("any value",["any value", "any value"]){
    player::message("Condition is true");
}

#Or from the object

if("any value".not_equals(["any value", "any value"]){
    player::message("Condition is true");
}
```

<h3 id=if_variable_range_intersects_range>
  <code>variable::range_intersects_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action that checks the conditions\
**Description:** None

**Usage example:** 
```ts
if(variable::range_intersects_range(location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),"OVERLAPS"){
    player::message("Condition is true");
}
```

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

<h3 id=set_variable_add_item_potion_effects>
  <code>variable::add_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Potion Effects\
**Type:** An action that returns a value\
**Description:** Sets the potion effects of an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::add_item_potion_effects(item("stick"),[potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");

#Or from the object

a1 = item("stick").add_item_potion_effects([potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");

#Or dry

variable::add_item_potion_effects(a1,item("stick"),[potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");
```

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

<h3 id=set_variable_append_component>
  <code>variable::append_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::append_component(["components", "components"],"SPACES");

#Or dry

variable::append_component(a1,["components", "components"],"SPACES");
```

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

<h3 id=set_variable_change_component_parsing>
  <code>variable::change_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::change_component_parsing("component","PLAIN");

#Or from the object

a1 = "component".change_component_parsing("PLAIN");

#Or dry

variable::change_component_parsing(a1,"component","PLAIN");
```

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

#Or dry

variable::clamp(a1,1,2,3);
```

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

<h3 id=set_variable_compact_component>
  <code>variable::compact_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::compact_component("component");

#Or from the object

a1 = "component".compact_component();

#Or dry

variable::compact_component(a1,"component");
```

<h3 id=set_variable_component_of_children>
  <code>variable::component_of_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::component_of_children(["components", "components"]);

#Or dry

variable::component_of_children(a1,["components", "components"]);
```

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

<h3 id=set_variable_create_keybind_component>
  <code>variable::create_keybind_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::create_keybind_component("key");

#Or dry

variable::create_keybind_component(a1,"key");
```

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

<h3 id=set_variable_create_map_from_values>
  <code>variable::create_map_from_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None\
**Additional info:**\
&nbsp;&nbsp;None

**Usage example:** 
```ts
a1 = variable::create_map_from_values(["any value", "any value"],["any value", "any value"]);

#Or dry

variable::create_map_from_values(a1,["any value", "any value"],["any value", "any value"]);
```

<h3 id=set_variable_create_translatable_component>
  <code>variable::create_translatable_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::create_translatable_component("key",["args", "args"]);

#Or dry

variable::create_translatable_component(a1,"key",["args", "args"]);
```

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

variable::get_all_coordinates(location(0,0,0,0,0),a1,a2,a3,a4,a5);
```

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

<h3 id=set_variable_get_bundle_items>
  <code>variable::get_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
variable::get_bundle_items(a1,item("stick"));

#Or from the object

item("stick").get_bundle_items(a1);
```

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

<h3 id=set_variable_get_component_children>
  <code>variable::get_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::get_component_children("component");

#Or from the object

a1 = "component".get_component_children();

#Or dry

variable::get_component_children(a1,"component");
```

<h3 id=set_variable_get_component_decorations>
  <code>variable::get_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::get_component_decorations("component");

#Or from the object

a1 = "component".get_component_decorations();

#Or dry

variable::get_component_decorations(a1,"component");
```

<h3 id=set_variable_get_component_hex_color>
  <code>variable::get_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::get_component_hex_color("component");

#Or from the object

a1 = "component".get_component_hex_color();

#Or dry

variable::get_component_hex_color(a1,"component");
```

<h3 id=set_variable_get_component_parsing>
  <code>variable::get_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::get_component_parsing("component");

#Or from the object

a1 = "component".get_component_parsing();

#Or dry

variable::get_component_parsing(a1,"component");
```

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

<h3 id=set_variable_get_decorate_pot_sherd>
  <code>variable::get_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::get_decorate_pot_sherd(location(0,0,0,0,0),"BACK");

#Or from the object

a1 = location(0,0,0,0,0).get_decorate_pot_sherd("BACK");

#Or dry

variable::get_decorate_pot_sherd(a1,location(0,0,0,0,0),"BACK");
```

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

<h3 id=set_variable_get_item_attribute>
  <code>variable::get_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Attribute\
**Type:** An action that returns a value\
**Description:** Gets the specified attribute from an item as a "UUID - Value" dictionary and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_attribute(item("stick"),"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");

#Or from the object

a1 = item("stick").get_item_attribute("name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");

#Or dry

variable::get_item_attribute(a1,item("stick"),"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");
```

<h3 id=set_variable_get_item_color>
  <code>variable::get_item_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Item Color\
**Type:** An action that returns a value\
**Description:** Sets an item's color value to a variable.

**Usage example:** 
```ts
a1 = variable::get_item_color(item("stick"));

#Or from the object

a1 = item("stick").get_item_color();

#Or dry

variable::get_item_color(a1,item("stick"));
```

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

<h3 id=set_variable_get_item_destroyable_blocks>
  <code>variable::get_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
variable::get_item_destroyable_blocks(a1,item("stick"));

#Or from the object

item("stick").get_item_destroyable_blocks(a1);
```

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

<h3 id=set_variable_get_item_placeable_blocks>
  <code>variable::get_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
variable::get_item_placeable_blocks(a1,item("stick"));

#Or from the object

item("stick").get_item_placeable_blocks(a1);
```

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

<h3 id=set_variable_get_map_key_by_index>
  <code>variable::get_map_key_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::get_map_key_by_index(`map`,1,"any value");

#Or from the object

a1 = `map`.get_map_key_by_index(1,"any value");

#Or dry

variable::get_map_key_by_index(a1,`map`,1,"any value");
```

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

<h3 id=set_variable_get_map_value_by_index>
  <code>variable::get_map_value_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::get_map_value_by_index(`map`,1,"any value");

#Or from the object

a1 = `map`.get_map_value_by_index(1,"any value");

#Or dry

variable::get_map_value_by_index(a1,`map`,1,"any value");
```

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

<h3 id=set_variable_get_player_head_value>
  <code>variable::get_player_head_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::get_player_head_value(location(0,0,0,0,0),"NAME");

#Or from the object

a1 = location(0,0,0,0,0).get_player_head_value("NAME");

#Or dry

variable::get_player_head_value(a1,location(0,0,0,0,0),"NAME");
```

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

<h3 id=set_variable_get_sculk_shrieker_warning_level>
  <code>variable::get_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::get_sculk_shrieker_warning_level(location(0,0,0,0,0));

#Or from the object

a1 = location(0,0,0,0,0).get_sculk_shrieker_warning_level();

#Or dry

variable::get_sculk_shrieker_warning_level(a1,location(0,0,0,0,0));
```

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

<h3 id=set_variable_get_vector_all_components>
  <code>variable::get_vector_all_components</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1, a2, a3 = variable::get_vector_all_components(vector(0,0,0));

#Or from the object

a1, a2, a3 = vector(0,0,0).get_vector_all_components();

#Or dry

variable::get_vector_all_components(vector(0,0,0),a1,a2,a3);
```

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

<h3 id=set_variable_get_vector_from_block_face>
  <code>variable::get_vector_from_block_face</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Create Vector From Cardinal Direction\
**Type:** An action that returns a value\
**Description:** Generates a normalized vector based on the specified cardinal direction ("south", "north", "east", "west", "up", " down").

**Usage example:** 
```ts
a1 = variable::get_vector_from_block_face("block_face");

#Or dry

variable::get_vector_from_block_face(a1,"block_face");
```

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

<h3 id=set_variable_lerp_number>
  <code>variable::lerp_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::lerp_number(1,2,3);

#Or from the object

a1 = (3).lerp_number(1,2);

#Or dry

variable::lerp_number(a1,1,2,3);
```

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

<h3 id=set_variable_map_range>
  <code>variable::map_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::map_range(1,2,3,4,5);

#Or from the object

a1 = (1).map_range(2,3,4,5);

#Or dry

variable::map_range(a1,1,2,3,4,5);
```

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

<h3 id=set_variable_parse_json>
  <code>variable::parse_json</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Parse JSON\
**Type:** An action that returns a value\
**Description:** Parses JSON text into elements: dictionaries (if the text is in curly braces) and lists (if the text is in square brackets) that can be manipulated to get the desired values.

**Usage example:** 
```ts
a1 = variable::parse_json("json");

#Or dry

variable::parse_json(a1,"json");
```

<h3 id=set_variable_parse_to_component>
  <code>variable::parse_to_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::parse_to_component("text","PLAIN");

#Or from the object

a1 = "text".parse_to_component("PLAIN");

#Or dry

variable::parse_to_component(a1,"text","PLAIN");
```

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

<h3 id=set_variable_ray_trace_result>
  <code>variable::ray_trace_result</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Get Raycast Result\
**Type:** An action that returns a value\
**Description:** Launches a ray with the given parameters. When the ray collides with the specified objects (entity or block), you can get the location of the ray, the location and side of the block, the UUID of the entity, and the side of the hitbox. Beamwidth only works on entities (increases or decreases creature hitboxes).

**Usage example:** 
```ts
a1, a2, a3, a4 = variable::ray_trace_result(location(0,0,0,0,0),1,2,"ONLY_BLOCKS","TRUE","NEVER",`entities`);

#Or dry

variable::ray_trace_result(location(0,0,0,0,0),1,2,"ONLY_BLOCKS","TRUE","NEVER",a1,a2,a3,a4,`entities`);
```

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

<h3 id=set_variable_regex_replace_text>
  <code>variable::regex_replace_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Replace Match With Regular Expression\
**Type:** An action that returns a value\
**Description:** Replaces text matching the specified regular expression and assigns the result to a variable. The "Replacement" argument can contain $<group name> to refer to the group. Include only the flags you need!

**Usage example:** 
```ts
a1 = variable::regex_replace_text("text","regex","replacement","ANY","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE");

#Or from the object

a1 = "text".regex_replace_text("regex","replacement","ANY","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE");

#Or dry

variable::regex_replace_text(a1,"text","regex","replacement","ANY","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE");
```

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

<h3 id=set_variable_remove_item_attribute>
  <code>variable::remove_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
variable::remove_item_attribute(a1,item("stick"),"name_or_uuid","GENERIC_ARMOR");

#Or from the object

item("stick").remove_item_attribute(a1,"name_or_uuid","GENERIC_ARMOR");
```

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

<h3 id=set_variable_remove_item_potion_effects>
  <code>variable::remove_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Potion Effects From an Item\
**Type:** An action that returns a value\
**Description:** Removes potion effects from an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::remove_item_potion_effects(item("stick"),[potion("slow_falling"), potion("slow_falling")]);

#Or from the object

a1 = item("stick").remove_item_potion_effects([potion("slow_falling"), potion("slow_falling")]);

#Or dry

variable::remove_item_potion_effects(a1,item("stick"),[potion("slow_falling"), potion("slow_falling")]);
```

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

<h3 id=set_variable_remove_map_entry>
  <code>variable::remove_map_entry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Dictionary Entry\
**Type:** An action that returns a value\
**Description:** Removes a dictionary entry and assigns the result to a variable.

**Usage example:** 
```ts
a2, a1 = variable::remove_map_entry(`map`,"any value",["any value", "any value"]);

#Or from the object

a2, a1 = `map`.remove_map_entry("any value",["any value", "any value"]);

#Or dry

variable::remove_map_entry(a1,a2,`map`,"any value",["any value", "any value"]);
```

<h3 id=set_variable_remove_text>
  <code>variable::remove_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Remove Text\
**Type:** An action that returns a value\
**Description:** Removes all or part of the text and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::remove_text("text","TRUE",["remove", "remove"]);

#Or from the object

a1 = "text".remove_text("TRUE",["remove", "remove"]);

#Or dry

variable::remove_text(a1,"text","TRUE",["remove", "remove"]);
```

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

<h3 id=set_variable_set_armor_trim>
  <code>variable::set_armor_trim</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
variable::set_armor_trim(a1,item("stick"),item("stick"),item("stick"));

#Or from the object

item("stick").set_armor_trim(a1,item("stick"),item("stick"));
```

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

<h3 id=set_variable_set_book_pages>
  <code>variable::set_book_pages</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Book Text\
**Type:** An action that returns a value\
**Description:** Sets the book text and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_book_pages(item("stick"),["text", "text"]);

#Or from the object

a1 = item("stick").set_book_pages(["text", "text"]);

#Or dry

variable::set_book_pages(a1,item("stick"),["text", "text"]);
```

<h3 id=set_variable_set_bundle_items>
  <code>variable::set_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** Action without value\
**Description:** None

**Usage example:** 
```ts
variable::set_bundle_items(a1,item("stick"),[item("stick"), item("stick")],"ADD");

#Or from the object

item("stick").set_bundle_items(a1,[item("stick"), item("stick")],"ADD");
```

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

<h3 id=set_variable_set_component_children>
  <code>variable::set_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::set_component_children("component",["children", "children"]);

#Or from the object

a1 = "component".set_component_children(["children", "children"]);

#Or dry

variable::set_component_children(a1,"component",["children", "children"]);
```

<h3 id=set_variable_set_component_click>
  <code>variable::set_component_click</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::set_component_click("component","value","COPY_TO_CLIPBOARD");

#Or from the object

a1 = "component".set_component_click("value","COPY_TO_CLIPBOARD");

#Or dry

variable::set_component_click(a1,"component","value","COPY_TO_CLIPBOARD");
```

<h3 id=set_variable_set_component_decorations>
  <code>variable::set_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::set_component_decorations("component","FALSE","FALSE","FALSE","FALSE","FALSE");

#Or from the object

a1 = "component".set_component_decorations("FALSE","FALSE","FALSE","FALSE","FALSE");

#Or dry

variable::set_component_decorations(a1,"component","FALSE","FALSE","FALSE","FALSE","FALSE");
```

<h3 id=set_variable_set_component_entity_hover>
  <code>variable::set_component_entity_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::set_component_entity_hover("component","name_or_uuid");

#Or from the object

a1 = "component".set_component_entity_hover("name_or_uuid");

#Or dry

variable::set_component_entity_hover(a1,"component","name_or_uuid");
```

<h3 id=set_variable_set_component_font>
  <code>variable::set_component_font</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::set_component_font("component","namespace","value");

#Or from the object

a1 = "component".set_component_font("namespace","value");

#Or dry

variable::set_component_font(a1,"component","namespace","value");
```

<h3 id=set_variable_set_component_hex_color>
  <code>variable::set_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::set_component_hex_color("component","color");

#Or from the object

a1 = "component".set_component_hex_color("color");

#Or dry

variable::set_component_hex_color(a1,"component","color");
```

<h3 id=set_variable_set_component_hover>
  <code>variable::set_component_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::set_component_hover("component","hover");

#Or from the object

a1 = "component".set_component_hover("hover");

#Or dry

variable::set_component_hover(a1,"component","hover");
```

<h3 id=set_variable_set_component_insertion>
  <code>variable::set_component_insertion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::set_component_insertion("component","insertion");

#Or from the object

a1 = "component".set_component_insertion("insertion");

#Or dry

variable::set_component_insertion(a1,"component","insertion");
```

<h3 id=set_variable_set_component_item_hover>
  <code>variable::set_component_item_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** None\
**Type:** An action that returns a value\
**Description:** None

**Usage example:** 
```ts
a1 = variable::set_component_item_hover("component",item("stick"));

#Or from the object

a1 = "component".set_component_item_hover(item("stick"));

#Or dry

variable::set_component_item_hover(a1,"component",item("stick"));
```

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

<h3 id=set_variable_set_item_attribute>
  <code>variable::set_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Add Attribute To Item\
**Type:** An action that returns a value\
**Description:** Adds a specific attribute to an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_attribute(item("stick"),1,"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");

#Or from the object

a1 = item("stick").set_item_attribute(1,"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");

#Or dry

variable::set_item_attribute(a1,item("stick"),1,"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");
```

<h3 id=set_variable_set_item_color>
  <code>variable::set_item_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Color\
**Type:** An action that returns a value\
**Description:** Sets the specified color to an item and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_color(item("stick"),"color");

#Or from the object

a1 = item("stick").set_item_color("color");

#Or dry

variable::set_item_color(a1,item("stick"),"color");
```

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

<h3 id=set_variable_set_item_destroyable_blocks>
  <code>variable::set_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Breakeble Blocks\
**Type:** An action that returns a value\
**Description:** Sets an item with the blocks it can break and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_destroyable_blocks(item("stick"),[item("stick"), item("stick")]);

#Or from the object

a1 = item("stick").set_item_destroyable_blocks([item("stick"), item("stick")]);

#Or dry

variable::set_item_destroyable_blocks(a1,item("stick"),[item("stick"), item("stick")]);
```

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

<h3 id=set_variable_set_item_type>
  <code>variable::set_item_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Type\
**Type:** An action that returns a value\
**Description:** Changes the type of an item without changing the other data of the item.

**Usage example:** 
```ts
a1 = variable::set_item_type(item("stick"),"type");

#Or from the object

a1 = item("stick").set_item_type("type");

#Or dry

variable::set_item_type(a1,item("stick"),"type");
```

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

<h3 id=set_variable_set_item_placeable_blocks>
  <code>variable::set_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Item Placeable Blocks\
**Type:** An action that returns a value\
**Description:** Sets an item to placeable blocks and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_item_placeable_blocks(item("stick"),[item("stick"), item("stick")]);

#Or from the object

a1 = item("stick").set_item_placeable_blocks([item("stick"), item("stick")]);

#Or dry

variable::set_item_placeable_blocks(a1,item("stick"),[item("stick"), item("stick")]);
```

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

<h3 id=set_variable_set_sound_source>
  <code>variable::set_sound_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Set Sound Source\
**Type:** An action that returns a value\
**Description:** Sets the sound source and assigns the result to a variable.

**Usage example:** 
```ts
a1 = variable::set_sound_source(sound("entity.zombie.hurt"),"AMBIENT");

#Or from the object

a1 = sound("entity.zombie.hurt").set_sound_source("AMBIENT");

#Or dry

variable::set_sound_source(a1,sound("entity.zombie.hurt"),"AMBIENT");
```

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

