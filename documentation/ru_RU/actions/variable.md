<h3 id=if_variable_equals>
  <code>variable::equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равна ли переменная хотя бы одному из сравниваемых значений.

**Пример использования:** 
```ts
if(variable::equals("any value",["any value", "any value"]){
    player::message("Условие верно");
}

#Или от объекта

if("any value".equals(["any value", "any value"]){
    player::message("Условие верно");
}
```

<h3 id=if_variable_exists>
  <code>variable::exists</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Переменная существует\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, существует ли выбранная переменная.

**Пример использования:** 
```ts
if(variable::exists(a1){
    player::message("Условие верно");
}

#Или от объекта

if(a1.exists(){
    player::message("Условие верно");
}
```

<h3 id=if_variable_greater>
  <code>variable::greater</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Больше\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, больше ли числовая переменная указанного значения.

**Пример использования:** 
```ts
if(variable::greater(1,2){
    player::message("Условие верно");
}

#Или от объекта

if((1).greater(2){
    player::message("Условие верно");
}
```

<h3 id=if_variable_greater_or_equals>
  <code>variable::greater_or_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Больше или равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, больше или равна ли числовая переменная указанного значения.

**Пример использования:** 
```ts
if(variable::greater_or_equals(1,2){
    player::message("Условие верно");
}

#Или от объекта

if((1).greater_or_equals(2){
    player::message("Условие верно");
}
```

<h3 id=if_variable_in_range>
  <code>variable::in_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** В диапазоне\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли переменная в указанном диапазоне.
**Работает с:**\
&nbsp;&nbsp;Числами\
&nbsp;&nbsp;Местоположениями

**Пример использования:** 
```ts
if(variable::in_range("any value","any value","any value"){
    player::message("Условие верно");
}

#Или от объекта

if("any value".in_range("any value","any value"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_is_type>
  <code>variable::is_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Тип переменной равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли тип значения переменной указанному.

**Пример использования:** 
```ts
if(variable::is_type("any value","NUMBER"){
    player::message("Условие верно");
}

#Или от объекта

if("any value".is_type("NUMBER"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_item_equals>
  <code>variable::item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равна ли предметная переменная хотя бы одной из указанных.

**Пример использования:** 
```ts
if(variable::item_equals(item("stick"),[item("stick"), item("stick")],"EXACTLY"){
    player::message("Условие верно");
}

#Или от объекта

if(item("stick").item_equals([item("stick"), item("stick")],"EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_item_has_enchantment>
  <code>variable::item_has_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет имеет зачарование\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли предметная переменная указанное зачарование определенного уровня.

**Пример использования:** 
```ts
if(variable::item_has_enchantment(item("stick"),"enchant",1){
    player::message("Условие верно");
}

#Или от объекта

if(item("stick").item_has_enchantment("enchant",1){
    player::message("Условие верно");
}
```

<h3 id=if_variable_item_has_tag>
  <code>variable::item_has_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет имеет тег\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли предметная переменная указанный тег с выбранным значением.

**Пример использования:** 
```ts
if(variable::item_has_tag(item("stick"),"tag","value"){
    player::message("Условие верно");
}

#Или от объекта

if(item("stick").item_has_tag("tag","value"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_less>
  <code>variable::less</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Меньше\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, меньше ли числовая переменная указанного значения.

**Пример использования:** 
```ts
if(variable::less(1,2){
    player::message("Условие верно");
}

#Или от объекта

if((1).less(2){
    player::message("Условие верно");
}
```

<h3 id=if_variable_less_or_equals>
  <code>variable::less_or_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Меньше или равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, меньше или равна ли числовая переменная указанного значения.

**Пример использования:** 
```ts
if(variable::less_or_equals(1,2){
    player::message("Условие верно");
}

#Или от объекта

if((1).less_or_equals(2){
    player::message("Условие верно");
}
```

<h3 id=if_variable_list_contains_value>
  <code>variable::list_contains_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Список содержит значение\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, содержит ли список определённое значение.

**Пример использования:** 
```ts
if(variable::list_contains_value(`list`,["any value", "any value"],"ANY"){
    player::message("Условие верно");
}

#Или от объекта

if(`list`.list_contains_value(["any value", "any value"],"ANY"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_list_value_equals>
  <code>variable::list_value_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Значение элемента списка равно\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равно ли значение элемента списка хотя бы одному сравниваемому значению.

**Пример использования:** 
```ts
if(variable::list_value_equals(`list`,1,["any value", "any value"]){
    player::message("Условие верно");
}

#Или от объекта

if(`list`.list_value_equals(1,["any value", "any value"]){
    player::message("Условие верно");
}
```

<h3 id=if_variable_location_in_range>
  <code>variable::location_in_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Местоположение в диапазоне\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли местоположение в указанном диапазоне.

**Пример использования:** 
```ts
if(variable::location_in_range(location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),"EXACT"){
    player::message("Условие верно");
}

#Или от объекта

if(location(0,0,0,0,0).location_in_range(location(0,0,0,0,0),location(0,0,0,0,0),"EXACT"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_location_is_near>
  <code>variable::location_is_near</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Рядом с местоположением\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли переменная местоположения рядом с указанным местоположением.

**Пример использования:** 
```ts
if(variable::location_is_near(location(0,0,0,0,0),1,[location(0,0,0,0,0), location(0,0,0,0,0)],"SPHERE"){
    player::message("Условие верно");
}

#Или от объекта

if(location(0,0,0,0,0).location_is_near(1,[location(0,0,0,0,0), location(0,0,0,0,0)],"SPHERE"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_map_has_key>
  <code>variable::map_has_key</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Словарь имеет ключ\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли словарь определённый ключ.

**Пример использования:** 
```ts
if(variable::map_has_key(`map`,"any value"){
    player::message("Условие верно");
}

#Или от объекта

if(`map`.map_has_key("any value"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_map_value_equals>
  <code>variable::map_value_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Значение элемента словаря равно\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равно ли значение элемента словаря по ключу хотя бы одному сравниваемому значению.

**Пример использования:** 
```ts
if(variable::map_value_equals(`map`,"any value",["any value", "any value"]){
    player::message("Условие верно");
}

#Или от объекта

if(`map`.map_value_equals("any value",["any value", "any value"]){
    player::message("Условие верно");
}
```

<h3 id=if_variable_not_equals>
  <code>variable::not_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Не равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, не равна ли переменная хотя бы одному сравниваемых значений.

**Пример использования:** 
```ts
if(variable::not_equals("any value",["any value", "any value"]){
    player::message("Условие верно");
}

#Или от объекта

if("any value".not_equals(["any value", "any value"]){
    player::message("Условие верно");
}
```

<h3 id=if_variable_range_intersects_range>
  <code>variable::range_intersects_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Регион пересекается с регионом\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, пересекается ли один регион с другим.

**Пример использования:** 
```ts
if(variable::range_intersects_range(location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),"OVERLAPS"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_text_contains>
  <code>variable::text_contains</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Текст содержит\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, содержит ли текстовая переменная указанный текст.

**Пример использования:** 
```ts
if(variable::text_contains("value",["compare", "compare"],"TRUE"){
    player::message("Условие верно");
}

#Или от объекта

if("value".text_contains(["compare", "compare"],"TRUE"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_text_ends_with>
  <code>variable::text_ends_with</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Текст заканчивается на\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, заканчивается ли текстовая переменная на указанный текст.

**Пример использования:** 
```ts
if(variable::text_ends_with("value",["compare", "compare"],"TRUE"){
    player::message("Условие верно");
}

#Или от объекта

if("value".text_ends_with(["compare", "compare"],"TRUE"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_text_matches>
  <code>variable::text_matches</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Текст совпадает\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, совпадает ли текстовая переменная с указанным текстом или регулярным выражением (RegEx).

**Пример использования:** 
```ts
if(variable::text_matches("match",["values", "values"],"TRUE","TRUE"){
    player::message("Условие верно");
}

#Или от объекта

if("match".text_matches(["values", "values"],"TRUE","TRUE"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_text_starts_with>
  <code>variable::text_starts_with</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Текст начинается с\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, начинается ли текстовая переменная с указанного текста.

**Пример использования:** 
```ts
if(variable::text_starts_with("value",["compare", "compare"],"TRUE"){
    player::message("Условие верно");
}

#Или от объекта

if("value".text_starts_with(["compare", "compare"],"TRUE"){
    player::message("Условие верно");
}
```

<h3 id=if_variable_list_is_empty>
  <code>variable::list_is_empty</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Размер значения равен нулю\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли размер значения нулю.
**Работает с:**\
&nbsp;&nbsp;Текстом\
&nbsp;&nbsp;Списками\
&nbsp;&nbsp;Словарями

**Пример использования:** 
```ts
if(variable::list_is_empty("any value"){
    player::message("Условие верно");
}

#Или от объекта

if("any value".list_is_empty(){
    player::message("Условие верно");
}
```

<h3 id=set_variable_absolute>
  <code>variable::absolute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Модуль числа\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение модуля выбранного числа.

**Пример использования:** 
```ts
a1 = variable::absolute(1);

#Или от объекта

a1 = (1).absolute();

#Или в сухую

variable::absolute(a1,1);
```

<h3 id=set_variable_value>
  <code>variable::set_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить значение (=)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает значение к переменной.

**Пример использования:** 
```ts
a1 = variable::set_value("any value");

#Или в сухую

variable::set_value(a1,"any value");
```

<h3 id=set_variable_add>
  <code>variable::add</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сложение чисел (+)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной сумму чисел.

**Пример использования:** 
```ts
a1 = variable::add([1, 2]);

#Или в сухую

variable::add(a1,[1, 2]);
```

<h3 id=set_variable_add_item_enchantment>
  <code>variable::add_item_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить зачарование предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Добавляет зачарование предмету и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::add_item_enchantment(item("stick"),"enchantment",1);

#Или от объекта

a1 = item("stick").add_item_enchantment("enchantment",1);

#Или в сухую

variable::add_item_enchantment(a1,item("stick"),"enchantment",1);
```

<h3 id=set_variable_add_item_potion_effects>
  <code>variable::add_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить эффекты зелий предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает эффекты зелий предмету и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::add_item_potion_effects(item("stick"),[potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");

#Или от объекта

a1 = item("stick").add_item_potion_effects([potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");

#Или в сухую

variable::add_item_potion_effects(a1,item("stick"),[potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");
```

<h3 id=set_variable_add_vectors>
  <code>variable::add_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сумма векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение суммы векторов.

**Пример использования:** 
```ts
a1 = variable::add_vectors([vector(0,0,0), vector(0,0,0)]);

#Или в сухую

variable::add_vectors(a1,[vector(0,0,0), vector(0,0,0)]);
```

<h3 id=set_variable_align_location>
  <code>variable::align_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Округлить местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Округляет местоположение к центру или углу блока и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::align_location(location(0,0,0,0,0),"KEEP","ALL","BLOCK_CENTER");

#Или от объекта

a1 = location(0,0,0,0,0).align_location("KEEP","ALL","BLOCK_CENTER");

#Или в сухую

variable::align_location(a1,location(0,0,0,0,0),"KEEP","ALL","BLOCK_CENTER");
```

<h3 id=set_variable_align_to_axis_vector>
  <code>variable::align_to_axis_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выровнять вектор\
**Тип:** Действие, возращающее значение\
**Описание:** Выравнивает вектор к ближайшей оси и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::align_to_axis_vector(vector(0,0,0),"TRUE");

#Или от объекта

a1 = vector(0,0,0).align_to_axis_vector("TRUE");

#Или в сухую

variable::align_to_axis_vector(a1,vector(0,0,0),"TRUE");
```

<h3 id=set_variable_append_component>
  <code>variable::append_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Объединить стилизуемые тексты\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет указанные стилизуемые тексты в единый стилизуемый текст и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::append_component(["components", "components"],"SPACES");

#Или в сухую

variable::append_component(a1,["components", "components"],"SPACES");
```

<h3 id=set_variable_append_list>
  <code>variable::append_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Объединить два списка\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет два указанных списка в один.

**Пример использования:** 
```ts
a1 = variable::append_list(`list_1`,`list_2`);

#Или от объекта

a1 = `list_1`.append_list(`list_2`);

#Или в сухую

variable::append_list(a1,`list_1`,`list_2`);
```

<h3 id=set_variable_append_map>
  <code>variable::append_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Объединить словари\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет два словаря и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::append_map(`map`,`other_map`);

#Или от объекта

a1 = `map`.append_map(`other_map`);

#Или в сухую

variable::append_map(a1,`map`,`other_map`);
```

<h3 id=set_variable_append_value>
  <code>variable::append_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить значение\
**Тип:** Действие без значения\
**Описание:** Добавляет указанные значения в конец списка.

**Пример использования:** 
```ts
variable::append_value(a1,["any value", "any value"]);

#Или от объекта

a1.append_value(["any value", "any value"]);
```

<h3 id=set_variable_average>
  <code>variable::average</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Среднее значение\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной среднее значение чисел.

**Пример использования:** 
```ts
a1 = variable::average([1, 2]);

#Или в сухую

variable::average(a1,[1, 2]);
```

<h3 id=set_variable_bitwise_operation>
  <code>variable::bitwise_operation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Побитовая операция над числами\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат побитовой операции над числами.

**Пример использования:** 
```ts
a1 = variable::bitwise_operation(1,2,"OR");

#Или в сухую

variable::bitwise_operation(a1,1,2,"OR");
```

<h3 id=set_variable_center_location>
  <code>variable::center_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить центральное местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Находит местоположение равное центру между двумя местоположениями и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::center_location([location(0,0,0,0,0), location(0,0,0,0,0)]);

#Или в сухую

variable::center_location(a1,[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

<h3 id=set_variable_change_component_parsing>
  <code>variable::change_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Изменить тип преобразования стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Изменяет тип преобразования для указанного стилизуемого текста.

**Пример использования:** 
```ts
a1 = variable::change_component_parsing("component","PLAIN");

#Или от объекта

a1 = "component".change_component_parsing("PLAIN");

#Или в сухую

variable::change_component_parsing(a1,"component","PLAIN");
```

<h3 id=set_variable_char_to_number>
  <code>variable::char_to_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить число по символу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённое число из символа и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::char_to_number("char");

#Или от объекта

a1 = "char".char_to_number();

#Или в сухую

variable::char_to_number(a1,"char");
```

<h3 id=set_variable_clamp>
  <code>variable::clamp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Ограничить число\
**Тип:** Действие, возращающее значение\
**Описание:** Проверяет, находится ли число между минимальным и максимальным значением, и если нет, устанавливает его на ближайшее.

**Пример использования:** 
```ts
a1 = variable::clamp(1,2,3);

#Или в сухую

variable::clamp(a1,1,2,3);
```

<h3 id=set_variable_clear_color_codes>
  <code>variable::clear_color_codes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить цвета текста\
**Тип:** Действие, возращающее значение\
**Описание:** Очищает текст от цветовых кодов и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::clear_color_codes("text");

#Или от объекта

a1 = "text".clear_color_codes();

#Или в сухую

variable::clear_color_codes(a1,"text");
```

<h3 id=set_variable_clear_map>
  <code>variable::clear_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить словарь\
**Тип:** Действие без значения\
**Описание:** Очищает словарь.

**Пример использования:** 
```ts
variable::clear_map(a1);

#Или от объекта

a1.clear_map();
```

<h3 id=set_variable_compact_component>
  <code>variable::compact_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сжать стилизуемый текст\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной указанный стилизуемый текст без элементов стиля и дочерних частей.

**Пример использования:** 
```ts
a1 = variable::compact_component("component");

#Или от объекта

a1 = "component".compact_component();

#Или в сухую

variable::compact_component(a1,"component");
```

<h3 id=set_variable_component_of_children>
  <code>variable::component_of_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать стилизуемый текст из дочерних частей\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт стилизуемый текст из указанных дочерних стилизуемых текстов и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::component_of_children(["components", "components"]);

#Или в сухую

variable::component_of_children(a1,["components", "components"]);
```

<h3 id=set_variable_convert_number_to_text>
  <code>variable::convert_number_to_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать число в текст\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат преобразования числа в текст.\
**Дополнительная информация:**\
&nbsp;&nbsp;Работает только с целыми числами.\
&nbsp;&nbsp;Основание системы счисления должно находится в диапазоне от 2 до 36 включительно.

**Пример использования:** 
```ts
a1 = variable::convert_number_to_text(1,2);

#Или от объекта

a1 = (1).convert_number_to_text(2);

#Или в сухую

variable::convert_number_to_text(a1,1,2);
```

<h3 id=set_variable_convert_text_to_number>
  <code>variable::convert_text_to_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать текст в число\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат преобразования числа в виде текста другой системы счисления в число десятичной системы счисления. Работает только с целыми числами.

**Пример использования:** 
```ts
a1 = variable::convert_text_to_number("text",1);

#Или от объекта

a1 = "text".convert_text_to_number(1);

#Или в сухую

variable::convert_text_to_number(a1,"text",1);
```

<h3 id=set_variable_cosine>
  <code>variable::cosine</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Косинус числа\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает косинус от числа.

**Пример использования:** 
```ts
a1 = variable::cosine(1,"COSINE","DEGREES");

#Или от объекта

a1 = (1).cosine("COSINE","DEGREES");

#Или в сухую

variable::cosine(a1,1,"COSINE","DEGREES");
```

<h3 id=set_variable_cotangent>
  <code>variable::cotangent</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Котангенс числа\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает котангенс от числа.

**Пример использования:** 
```ts
a1 = variable::cotangent(1,"COTANGENT","DEGREES");

#Или от объекта

a1 = (1).cotangent("COTANGENT","DEGREES");

#Или в сухую

variable::cotangent(a1,1,"COTANGENT","DEGREES");
```

<h3 id=set_variable_create_keybind_component>
  <code>variable::create_keybind_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать стилизуемый текст с привязкой к клавише\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной стилизуемый текст, привязанный к клавише клиента.

**Пример использования:** 
```ts
a1 = variable::create_keybind_component("key");

#Или в сухую

variable::create_keybind_component(a1,"key");
```

<h3 id=set_variable_create_list>
  <code>variable::create_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать список\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт список, содержащий указанные значения.\
**Дополнительная информация:**\
&nbsp;&nbsp;Очищает список если он уже существует.

**Пример использования:** 
```ts
a1 = variable::create_list(["any value", "any value"]);

#Или в сухую

variable::create_list(a1,["any value", "any value"]);
```

<h3 id=set_variable_create_map>
  <code>variable::create_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать словарь\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт словарь из списка ключей и значений и присваивает результат к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Очищает словарь, если он уже существует.

**Пример использования:** 
```ts
a1 = variable::create_map(`keys`,`values`);

#Или в сухую

variable::create_map(a1,`keys`,`values`);
```

<h3 id=set_variable_create_map_from_values>
  <code>variable::create_map_from_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать словарь из значений\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт словарь из ключей и значений и присваивает результат к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Очищает словарь, если он уже существует.

**Пример использования:** 
```ts
a1 = variable::create_map_from_values(["any value", "any value"],["any value", "any value"]);

#Или в сухую

variable::create_map_from_values(a1,["any value", "any value"],["any value", "any value"]);
```

<h3 id=set_variable_create_translatable_component>
  <code>variable::create_translatable_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать переводимый стилизуемый текст\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной переводимый стилизуемый текст с указанными аргументами.

**Пример использования:** 
```ts
a1 = variable::create_translatable_component("key",["args", "args"]);

#Или в сухую

variable::create_translatable_component(a1,"key",["args", "args"]);
```

<h3 id=set_variable_vector_cross_product>
  <code>variable::vector_cross_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Векторное произведение двух векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение векторного произведения двух векторов.

**Пример использования:** 
```ts
a1 = variable::vector_cross_product(vector(0,0,0),vector(0,0,0));

#Или в сухую

variable::vector_cross_product(a1,vector(0,0,0),vector(0,0,0));
```

<h3 id=set_variable_decrement>
  <code>variable::decrement</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отнимание (-=)\
**Тип:** Действие, возращающее значение\
**Описание:** Отнимает от переменной выбранное число.

**Пример использования:** 
```ts
a1 = variable::decrement(1);

#Или в сухую

variable::decrement(a1,1);
```

<h3 id=set_variable_divide>
  <code>variable::divide</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Деление чисел (÷)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной частное чисел.

**Пример использования:** 
```ts
a1 = variable::divide([1, 2],"DEFAULT");

#Или в сухую

variable::divide(a1,[1, 2],"DEFAULT");
```

<h3 id=set_variable_divide_vector>
  <code>variable::divide_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Деление векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат деления двух векторов.

**Пример использования:** 
```ts
a1 = variable::divide_vector(vector(0,0,0),vector(0,0,0));

#Или в сухую

variable::divide_vector(a1,vector(0,0,0),vector(0,0,0));
```

<h3 id=set_variable_vector_dot_product>
  <code>variable::vector_dot_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Скалярное произведение двух векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение скалярного произведения двух векторов.

**Пример использования:** 
```ts
a1 = variable::vector_dot_product(vector(0,0,0),vector(0,0,0));

#Или в сухую

variable::vector_dot_product(a1,vector(0,0,0),vector(0,0,0));
```

<h3 id=set_variable_face_location>
  <code>variable::face_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Направить местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Поворачивает местоположение в направлении другого местоположения и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::face_location(location(0,0,0,0,0),location(0,0,0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).face_location(location(0,0,0,0,0));

#Или в сухую

variable::face_location(a1,location(0,0,0,0,0),location(0,0,0,0,0));
```

<h3 id=set_variable_flatten_list>
  <code>variable::flatten_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сгладить список\
**Тип:** Действие, возращающее значение\
**Описание:** Разделяет подсписки указанного списка на отдельные элементы.

**Пример использования:** 
```ts
a1 = variable::flatten_list(`list`);

#Или от объекта

a1 = `list`.flatten_list();

#Или в сухую

variable::flatten_list(a1,`list`);
```

<h3 id=set_variable_format_timestamp>
  <code>variable::format_timestamp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать формат времени\
**Тип:** Действие, возращающее значение\
**Описание:** Преобразовывает число (миллисекунды) в указанный формат времени и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::format_timestamp(1,"pattern","zone_id","locale","CUSTOM");

#Или от объекта

a1 = (1).format_timestamp("pattern","zone_id","locale","CUSTOM");

#Или в сухую

variable::format_timestamp(a1,1,"pattern","zone_id","locale","CUSTOM");
```

<h3 id=set_variable_gaussian_distribution>
  <code>variable::gaussian_distribution</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Нормально распределенное случайное число\
**Тип:** Действие, возращающее значение\
**Описание:** Выдаёт случайное число близкое к среднему значению μ со стандартным отклонением σ с шансом, заданным графиком нормального распределения.

**Пример использования:** 
```ts
a1 = variable::gaussian_distribution(1,2,"NORMAL");

#Или в сухую

variable::gaussian_distribution(a1,1,2,"NORMAL");
```

<h3 id=set_variable_get_all_block_data>
  <code>variable::get_all_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить все данные блока\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной все данные блока на выбранном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_all_block_data(location(0,0,0,0,0),"TRUE");

#Или от объекта

a1 = location(0,0,0,0,0).get_all_block_data("TRUE");

#Или в сухую

variable::get_all_block_data(a1,location(0,0,0,0,0),"TRUE");
```

<h3 id=set_variable_get_all_coordinates>
  <code>variable::get_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить все координаты местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение всех координат с местоположения и присваивает их в переменные.

**Пример использования:** 
```ts
a1, a2, a3, a4, a5 = variable::get_all_coordinates(location(0,0,0,0,0));

#Или от объекта

a1, a2, a3, a4, a5 = location(0,0,0,0,0).get_all_coordinates();

#Или в сухую

variable::get_all_coordinates(location(0,0,0,0,0),a1,a2,a3,a4,a5);
```

<h3 id=set_variable_get_angle_between_vectors>
  <code>variable::get_angle_between_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить угол между двумя векторами\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение угла между двумя векторами.

**Пример использования:** 
```ts
a1 = variable::get_angle_between_vectors(vector(0,0,0),vector(0,0,0),"DEGREES");

#Или в сухую

variable::get_angle_between_vectors(a1,vector(0,0,0),vector(0,0,0),"DEGREES");
```

<h3 id=set_variable_get_block_custom_tag>
  <code>variable::get_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** None\
**Тип:** Действие, возращающее значение\
**Описание:** None

**Пример использования:** 
```ts
a1 = variable::get_block_custom_tag(location(0,0,0,0,0),"tag_name","tag_value","any value");

#Или в сухую

variable::get_block_custom_tag(a1,location(0,0,0,0,0),"tag_name","tag_value","any value");
```

<h3 id=set_variable_get_block_data>
  <code>variable::get_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить данные блока\
**Тип:** Действие, возращающее значение\
**Описание:** Получает данные блока и присваивает его в переменную.

**Пример использования:** 
```ts
a1 = variable::get_block_data(location(0,0,0,0,0),"tag_name");

#Или от объекта

a1 = location(0,0,0,0,0).get_block_data("tag_name");

#Или в сухую

variable::get_block_data(a1,location(0,0,0,0,0),"tag_name");
```

<h3 id=set_variable_get_block_growth>
  <code>variable::get_block_growth</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить уровень роста блока\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение уровня роста блока на указанном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_block_growth(location(0,0,0,0,0),"GROWTH_STAGE");

#Или от объекта

a1 = location(0,0,0,0,0).get_block_growth("GROWTH_STAGE");

#Или в сухую

variable::get_block_growth(a1,location(0,0,0,0,0),"GROWTH_STAGE");
```

<h3 id=set_variable_get_block_material>
  <code>variable::get_block_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип блока\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной тип блока на выбранном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_block_material(location(0,0,0,0,0),"ID");

#Или от объекта

a1 = location(0,0,0,0,0).get_block_material("ID");

#Или в сухую

variable::get_block_material(a1,location(0,0,0,0,0),"ID");
```

<h3 id=set_variable_get_block_material_property>
  <code>variable::get_block_material_property</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить свойство блока\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённое свойство блока и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_block_material_property(item("stone"),"HARDNESS");

#Или от объекта

a1 = item("stone").get_block_material_property("HARDNESS");

#Или в сухую

variable::get_block_material_property(a1,item("stone"),"HARDNESS");
```

<h3 id=set_variable_get_block_power>
  <code>variable::get_block_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить силу редстоуна\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение силы сигнала редстоуна на указанном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_block_power(location(0,0,0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).get_block_power();

#Или в сухую

variable::get_block_power(a1,location(0,0,0,0,0));
```

<h3 id=set_variable_get_book_text>
  <code>variable::get_book_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить текст книги\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение текста книги на определённой странице.

**Пример использования:** 
```ts
a1 = variable::get_book_text(item("stick"),1);

#Или от объекта

a1 = item("stick").get_book_text(1);

#Или в сухую

variable::get_book_text(a1,item("stick"),1);
```

<h3 id=set_variable_get_brushable_block_item>
  <code>variable::get_brushable_block_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить предмет из подозрительного блока\
**Тип:** Действие, возращающее значение\
**Описание:** Получить предмет из подозрительного блока (песка, гравия) и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_brushable_block_item(location(0,0,0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).get_brushable_block_item();

#Или в сухую

variable::get_brushable_block_item(a1,location(0,0,0,0,0));
```

<h3 id=set_variable_get_bundle_items>
  <code>variable::get_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить содержимое мешка\
**Тип:** Действие без значения\
**Описание:** Получает содержимое мешка и присваивает результат к переменной.

**Пример использования:** 
```ts
variable::get_bundle_items(a1,item("stick"));

#Или от объекта

item("stick").get_bundle_items(a1);
```

<h3 id=set_variable_get_char_at>
  <code>variable::get_char_at</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить символ по индексу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает символ из текста по указанному индексу и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_char_at("text",1);

#Или от объекта

a1 = "text".get_char_at(1);

#Или в сухую

variable::get_char_at(a1,"text",1);
```

<h3 id=set_variable_get_color_channels>
  <code>variable::get_color_channels</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить цветовые каналы\
**Тип:** Действие, возращающее значение\
**Описание:** Получает числовые значения RGB/HSB/HSL цвета в виде списка.

**Пример использования:** 
```ts
a1 = variable::get_color_channels("color","RGB");

#Или от объекта

a1 = "color".get_color_channels("RGB");

#Или в сухую

variable::get_color_channels(a1,"color","RGB");
```

<h3 id=set_variable_get_compass_lodestone>
  <code>variable::get_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить местоположение магнетита\
**Тип:** Действие, возращающее значение\
**Описание:** Получает с намагниченного компаса местоположение магнетита и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_compass_lodestone(item("stick"));

#Или от объекта

a1 = item("stick").get_compass_lodestone();

#Или в сухую

variable::get_compass_lodestone(a1,item("stick"));
```

<h3 id=set_variable_get_component_children>
  <code>variable::get_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить дочерние части стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной дочерние части указанного стилизуемого текста.

**Пример использования:** 
```ts
a1 = variable::get_component_children("component");

#Или от объекта

a1 = "component".get_component_children();

#Или в сухую

variable::get_component_children(a1,"component");
```

<h3 id=set_variable_get_component_decorations>
  <code>variable::get_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить декорации стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной все декорации (стилизацию) стилизуемого текста.

**Пример использования:** 
```ts
a1 = variable::get_component_decorations("component");

#Или от объекта

a1 = "component".get_component_decorations();

#Или в сухую

variable::get_component_decorations(a1,"component");
```

<h3 id=set_variable_get_component_hex_color>
  <code>variable::get_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить HEX-цвет стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной HEX-цвет указанного стилизуемого текста.

**Пример использования:** 
```ts
a1 = variable::get_component_hex_color("component");

#Или от объекта

a1 = "component".get_component_hex_color();

#Или в сухую

variable::get_component_hex_color(a1,"component");
```

<h3 id=set_variable_get_component_parsing>
  <code>variable::get_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип преобразования стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение типа преобразования указанного стилизуемого текста.

**Пример использования:** 
```ts
a1 = variable::get_component_parsing("component");

#Или от объекта

a1 = "component".get_component_parsing();

#Или в сухую

variable::get_component_parsing(a1,"component");
```

<h3 id=set_variable_get_container_contents>
  <code>variable::get_container_contents</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить содержимое контейнера\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной список содержимого контейнера на выбранном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_container_contents(location(0,0,0,0,0),"TRUE");

#Или от объекта

a1 = location(0,0,0,0,0).get_container_contents("TRUE");

#Или в сухую

variable::get_container_contents(a1,location(0,0,0,0,0),"TRUE");
```

<h3 id=set_variable_get_container_lock>
  <code>variable::get_container_lock</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить ключ контейнера\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной предмет ключа контейнера на указанном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_container_lock(location(0,0,0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).get_container_lock();

#Или в сухую

variable::get_container_lock(a1,location(0,0,0,0,0));
```

<h3 id=set_variable_get_container_name>
  <code>variable::get_container_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить имя контейнера\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной имя контейнера на выбранном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_container_name(location(0,0,0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).get_container_name();

#Или в сухую

variable::get_container_name(a1,location(0,0,0,0,0));
```

<h3 id=set_variable_get_coordinate>
  <code>variable::get_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить координату местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение выбранной координаты с местоположения и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_coordinate(location(0,0,0,0,0),"X");

#Или от объекта

a1 = location(0,0,0,0,0).get_coordinate("X");

#Или в сухую

variable::get_coordinate(a1,location(0,0,0,0,0),"X");
```

<h3 id=set_variable_get_decorate_pot_sherd>
  <code>variable::get_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить украшение кувшина\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной материал черепка выбранной стороны кувшина на указанном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_decorate_pot_sherd(location(0,0,0,0,0),"BACK");

#Или от объекта

a1 = location(0,0,0,0,0).get_decorate_pot_sherd("BACK");

#Или в сухую

variable::get_decorate_pot_sherd(a1,location(0,0,0,0,0),"BACK");
```

<h3 id=set_variable_get_index_of_subtext>
  <code>variable::get_index_of_subtext</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить индекс подтекста\
**Тип:** Действие, возращающее значение\
**Описание:** Получает индекс подтекста из текста и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_index_of_subtext("text","subtext",1,"FIRST");

#Или от объекта

a1 = "text".get_index_of_subtext("subtext",1,"FIRST");

#Или в сухую

variable::get_index_of_subtext(a1,"text","subtext",1,"FIRST");
```

<h3 id=set_variable_get_item_amount>
  <code>variable::get_item_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить количество предметов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной количество предметов в стаке.

**Пример использования:** 
```ts
a1 = variable::get_item_amount(item("stick"));

#Или от объекта

a1 = item("stick").get_item_amount();

#Или в сухую

variable::get_item_amount(a1,item("stick"));
```

<h3 id=set_variable_get_item_attribute>
  <code>variable::get_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить атрибут предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённый атрибут с предмета в виде словаря "UUID - Значение", и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_item_attribute(item("stick"),"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");

#Или от объекта

a1 = item("stick").get_item_attribute("name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");

#Или в сухую

variable::get_item_attribute(a1,item("stick"),"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");
```

<h3 id=set_variable_get_item_color>
  <code>variable::get_item_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить цвет предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение цвета предмета.

**Пример использования:** 
```ts
a1 = variable::get_item_color(item("stick"));

#Или от объекта

a1 = item("stick").get_item_color();

#Или в сухую

variable::get_item_color(a1,item("stick"));
```

<h3 id=set_variable_get_item_custom_model_data>
  <code>variable::get_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить данные модели предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает данные модели предмета (CustomModelData) и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_item_custom_model_data(item("stick"));

#Или от объекта

a1 = item("stick").get_item_custom_model_data();

#Или в сухую

variable::get_item_custom_model_data(a1,item("stick"));
```

<h3 id=set_variable_get_item_custom_tag>
  <code>variable::get_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить кастомный тег предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение кастомного тега предмета.

**Пример использования:** 
```ts
a1 = variable::get_item_custom_tag(item("stick"),"tag_name","any value");

#Или от объекта

a1 = item("stick").get_item_custom_tag("tag_name","any value");

#Или в сухую

variable::get_item_custom_tag(a1,item("stick"),"tag_name","any value");
```

<h3 id=set_variable_get_item_custom_tags>
  <code>variable::get_item_custom_tags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить кастомные теги предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной словарь кастомных тегов предмета.

**Пример использования:** 
```ts
a1 = variable::get_item_custom_tags(item("stick"));

#Или от объекта

a1 = item("stick").get_item_custom_tags();

#Или в сухую

variable::get_item_custom_tags(a1,item("stick"));
```

<h3 id=set_variable_get_item_destroyable_blocks>
  <code>variable::get_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить блоки для ломания предметом\
**Тип:** Действие без значения\
**Описание:** Получает блоки которые может ломать предмет и присваивает результат к переменной.

**Пример использования:** 
```ts
variable::get_item_destroyable_blocks(a1,item("stick"));

#Или от объекта

item("stick").get_item_destroyable_blocks(a1);
```

<h3 id=set_variable_get_item_durability>
  <code>variable::get_item_durability</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить прочность предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной прочность указанного предмета.

**Пример использования:** 
```ts
a1 = variable::get_item_durability(item("stick"),"DAMAGE");

#Или от объекта

a1 = item("stick").get_item_durability("DAMAGE");

#Или в сухую

variable::get_item_durability(a1,item("stick"),"DAMAGE");
```

<h3 id=set_variable_get_item_enchantments>
  <code>variable::get_item_enchantments</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить зачарования предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной словарь зачарований и их уровней предмета.

**Пример использования:** 
```ts
a1 = variable::get_item_enchantments(item("stick"));

#Или от объекта

a1 = item("stick").get_item_enchantments();

#Или в сухую

variable::get_item_enchantments(a1,item("stick"));
```

<h3 id=set_variable_get_item_lore>
  <code>variable::get_item_lore</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить описание предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной текст описания предмета.

**Пример использования:** 
```ts
a1 = variable::get_item_lore(item("stick"));

#Или от объекта

a1 = item("stick").get_item_lore();

#Или в сухую

variable::get_item_lore(a1,item("stick"));
```

<h3 id=set_variable_get_item_lore_line>
  <code>variable::get_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить строку описания предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной строку описания предмета.

**Пример использования:** 
```ts
a1 = variable::get_item_lore_line(item("stick"),1);

#Или от объекта

a1 = item("stick").get_item_lore_line(1);

#Или в сухую

variable::get_item_lore_line(a1,item("stick"),1);
```

<h3 id=set_variable_get_item_type>
  <code>variable::get_item_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной тип предмета, представленный в виде текста.

**Пример использования:** 
```ts
a1 = variable::get_item_type(item("stick"),"ID");

#Или от объекта

a1 = item("stick").get_item_type("ID");

#Или в сухую

variable::get_item_type(a1,item("stick"),"ID");
```

<h3 id=set_variable_get_item_max_stack_size>
  <code>variable::get_item_max_stack_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить максимальное количество предметов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной максимально возможное количество предметов в стаке.

**Пример использования:** 
```ts
a1 = variable::get_item_max_stack_size(item("stick"));

#Или от объекта

a1 = item("stick").get_item_max_stack_size();

#Или в сухую

variable::get_item_max_stack_size(a1,item("stick"));
```

<h3 id=set_variable_get_item_name>
  <code>variable::get_item_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить имя предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной отображаемое имя предмета.

**Пример использования:** 
```ts
a1 = variable::get_item_name(item("stick"));

#Или от объекта

a1 = item("stick").get_item_name();

#Или в сухую

variable::get_item_name(a1,item("stick"));
```

<h3 id=set_variable_get_item_nbt_tags>
  <code>variable::get_item_nbt_tags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить NBT тег предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной NBT теги указанного предмета.

**Пример использования:** 
```ts
a1 = variable::get_item_nbt_tags(item("stick"));

#Или от объекта

a1 = item("stick").get_item_nbt_tags();

#Или в сухую

variable::get_item_nbt_tags(a1,item("stick"));
```

<h3 id=set_variable_get_item_placeable_blocks>
  <code>variable::get_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить блоки для установки предмета\
**Тип:** Действие без значения\
**Описание:** Получает блоки на которые может быть установлен предмет и присваивает результат к переменной.

**Пример использования:** 
```ts
variable::get_item_placeable_blocks(a1,item("stick"));

#Или от объекта

item("stick").get_item_placeable_blocks(a1);
```

<h3 id=set_variable_get_item_potion_effects>
  <code>variable::get_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить эффекты зелий из предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает эффекты зелий из предмета и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_item_potion_effects(item("stick"));

#Или от объекта

a1 = item("stick").get_item_potion_effects();

#Или в сухую

variable::get_item_potion_effects(a1,item("stick"));
```

<h3 id=set_variable_get_item_rarity>
  <code>variable::get_item_rarity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить редкость предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает редкость предмета и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_item_rarity(item("stick"));

#Или от объекта

a1 = item("stick").get_item_rarity();

#Или в сухую

variable::get_item_rarity(a1,item("stick"));
```

<h3 id=set_variable_get_lectern_book>
  <code>variable::get_lectern_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить книгу с кафедры\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной книгу с кафедры на указанном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_lectern_book(location(0,0,0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).get_lectern_book();

#Или в сухую

variable::get_lectern_book(a1,location(0,0,0,0,0));
```

<h3 id=set_variable_get_lectern_page>
  <code>variable::get_lectern_page</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить страницу книги с кафедры\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной номер текущей страницы книги с кафедры на указанном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_lectern_page(location(0,0,0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).get_lectern_page();

#Или в сухую

variable::get_lectern_page(a1,location(0,0,0,0,0));
```

<h3 id=set_variable_get_light_level>
  <code>variable::get_light_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить уровень освещения\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение уровня освещения на указанном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_light_level(location(0,0,0,0,0),"TOTAL");

#Или от объекта

a1 = location(0,0,0,0,0).get_light_level("TOTAL");

#Или в сухую

variable::get_light_level(a1,location(0,0,0,0,0),"TOTAL");
```

<h3 id=set_variable_get_list_index_of_value>
  <code>variable::get_list_index_of_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить индекс значения списка\
**Тип:** Действие, возращающее значение\
**Описание:** Выполняет поиск значения в списке и получает его индекс, если он найден. В случае неудачи возвращает -1.

**Пример использования:** 
```ts
a1 = variable::get_list_index_of_value(`list`,"any value","FIRST");

#Или от объекта

a1 = `list`.get_list_index_of_value("any value","FIRST");

#Или в сухую

variable::get_list_index_of_value(a1,`list`,"any value","FIRST");
```

<h3 id=set_variable_get_list_length>
  <code>variable::get_list_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить размер списка\
**Тип:** Действие, возращающее значение\
**Описание:** Получает количество элементов, содержащихся в указанном списке.

**Пример использования:** 
```ts
a1 = variable::get_list_length(`list`);

#Или от объекта

a1 = `list`.get_list_length();

#Или в сухую

variable::get_list_length(a1,`list`);
```

<h3 id=set_variable_get_list_random_value>
  <code>variable::get_list_random_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить случайное значение списка\
**Тип:** Действие, возращающее значение\
**Описание:** Получает случайное значение из списка.

**Пример использования:** 
```ts
a1 = variable::get_list_random_value(`list`);

#Или от объекта

a1 = `list`.get_list_random_value();

#Или в сухую

variable::get_list_random_value(a1,`list`);
```

<h3 id=set_variable_get_list_value>
  <code>variable::get_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить значение из списка\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение из списка по указанному индексу.

**Пример использования:** 
```ts
a1 = variable::get_list_value(`list`,1,"any value");

#Или от объекта

a1 = `list`.get_list_value(1,"any value");

#Или в сухую

variable::get_list_value(a1,`list`,1,"any value");
```

<h3 id=set_variable_get_list_variables>
  <code>variable::get_list_variables</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить имена переменных\
**Тип:** Действие, возращающее значение\
**Описание:** Получает список имён всех переменных, и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_list_variables("GAME");

#Или в сухую

variable::get_list_variables(a1,"GAME");
```

<h3 id=set_variable_get_location_direction>
  <code>variable::get_location_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить направление местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной направления местоположения.

**Пример использования:** 
```ts
a1 = variable::get_location_direction(location(0,0,0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).get_location_direction();

#Или в сухую

variable::get_location_direction(a1,location(0,0,0,0,0));
```

<h3 id=set_variable_get_map_key_by_index>
  <code>variable::get_map_key_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить ключ словаря по индексу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает ключ по индексу и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_map_key_by_index(`map`,1,"any value");

#Или от объекта

a1 = `map`.get_map_key_by_index(1,"any value");

#Или в сухую

variable::get_map_key_by_index(a1,`map`,1,"any value");
```

<h3 id=set_variable_get_map_keys>
  <code>variable::get_map_keys</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить список ключей словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной список ключей словаря.

**Пример использования:** 
```ts
a1 = variable::get_map_keys(`map`);

#Или от объекта

a1 = `map`.get_map_keys();

#Или в сухую

variable::get_map_keys(a1,`map`);
```

<h3 id=set_variable_get_map_keys_by_value>
  <code>variable::get_map_keys_by_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить ключи словаря по значению\
**Тип:** Действие, возращающее значение\
**Описание:** Получает ключ либо список ключей словаря по значению и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_map_keys_by_value(`map`,"any value","any value","FIRST");

#Или от объекта

a1 = `map`.get_map_keys_by_value("any value","any value","FIRST");

#Или в сухую

variable::get_map_keys_by_value(a1,`map`,"any value","any value","FIRST");
```

<h3 id=set_variable_get_map_size>
  <code>variable::get_map_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить размер словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение размера словаря.

**Пример использования:** 
```ts
a1 = variable::get_map_size(`map`);

#Или от объекта

a1 = `map`.get_map_size();

#Или в сухую

variable::get_map_size(a1,`map`);
```

<h3 id=set_variable_get_map_value>
  <code>variable::get_map_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить значение словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённое значение словаря по ключу и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_map_value(`map`,"any value","any value");

#Или от объекта

a1 = `map`.get_map_value("any value","any value");

#Или в сухую

variable::get_map_value(a1,`map`,"any value","any value");
```

<h3 id=set_variable_get_map_value_by_index>
  <code>variable::get_map_value_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить значение словаря по индексу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение по индексу и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_map_value_by_index(`map`,1,"any value");

#Или от объекта

a1 = `map`.get_map_value_by_index(1,"any value");

#Или в сухую

variable::get_map_value_by_index(a1,`map`,1,"any value");
```

<h3 id=set_variable_get_map_values>
  <code>variable::get_map_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить список значений словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной список значений словаря.

**Пример использования:** 
```ts
a1 = variable::get_map_values(`map`);

#Или от объекта

a1 = `map`.get_map_values();

#Или в сухую

variable::get_map_values(a1,`map`);
```

<h3 id=set_variable_get_midpoint_between_vectors>
  <code>variable::get_midpoint_between_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить центральное значение между векторами\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной центральное значение между двумя векторами.

**Пример использования:** 
```ts
a1 = variable::get_midpoint_between_vectors(vector(0,0,0),vector(0,0,0));

#Или в сухую

variable::get_midpoint_between_vectors(a1,vector(0,0,0),vector(0,0,0));
```

<h3 id=set_variable_get_particle_amount>
  <code>variable::get_particle_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить количество частиц\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение количества частиц.

**Пример использования:** 
```ts
a1 = variable::get_particle_amount(particle("fire"));

#Или от объекта

a1 = particle("fire").get_particle_amount();

#Или в сухую

variable::get_particle_amount(a1,particle("fire"));
```

<h3 id=set_variable_get_particle_color>
  <code>variable::get_particle_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить цвет частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение цвета частицы.

**Пример использования:** 
```ts
a1 = variable::get_particle_color(particle("fire"),"COLOR");

#Или от объекта

a1 = particle("fire").get_particle_color("COLOR");

#Или в сухую

variable::get_particle_color(a1,particle("fire"),"COLOR");
```

<h3 id=set_variable_get_particle_material>
  <code>variable::get_particle_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить материал частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение материала частицы.

**Пример использования:** 
```ts
a1 = variable::get_particle_material(particle("fire"));

#Или от объекта

a1 = particle("fire").get_particle_material();

#Или в сухую

variable::get_particle_material(a1,particle("fire"));
```

<h3 id=set_variable_get_particle_offset>
  <code>variable::get_particle_offset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить движение частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение движения частицы.

**Пример использования:** 
```ts
a1 = variable::get_particle_offset(particle("fire"));

#Или от объекта

a1 = particle("fire").get_particle_offset();

#Или в сухую

variable::get_particle_offset(a1,particle("fire"));
```

<h3 id=set_variable_get_particle_size>
  <code>variable::get_particle_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить размер частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение размера частицы.

**Пример использования:** 
```ts
a1 = variable::get_particle_size(particle("fire"));

#Или от объекта

a1 = particle("fire").get_particle_size();

#Или в сухую

variable::get_particle_size(a1,particle("fire"));
```

<h3 id=set_variable_get_particle_spread>
  <code>variable::get_particle_spread</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить разброс частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение разброса частицы.

**Пример использования:** 
```ts
a1 = variable::get_particle_spread(particle("fire"),"VERTICAL");

#Или от объекта

a1 = particle("fire").get_particle_spread("VERTICAL");

#Или в сухую

variable::get_particle_spread(a1,particle("fire"),"VERTICAL");
```

<h3 id=set_variable_get_particle_type>
  <code>variable::get_particle_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение типа частицы.

**Пример использования:** 
```ts
a1 = variable::get_particle_type(particle("fire"));

#Или от объекта

a1 = particle("fire").get_particle_type();

#Или в сухую

variable::get_particle_type(a1,particle("fire"));
```

<h3 id=set_variable_get_player_head>
  <code>variable::get_player_head</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить голову игрока\
**Тип:** Действие, возращающее значение\
**Описание:** Получает голову игрока в виде предмета и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_player_head("name_or_uuid","NAME_OR_UUID");

#Или в сухую

variable::get_player_head(a1,"name_or_uuid","NAME_OR_UUID");
```

<h3 id=set_variable_get_player_head_owner>
  <code>variable::get_player_head_owner</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить владельца головы\
**Тип:** Действие, возращающее значение\
**Описание:** Получает имя или UUID владельца головы и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_player_head_owner(item("stick"),"NAME");

#Или от объекта

a1 = item("stick").get_player_head_owner("NAME");

#Или в сухую

variable::get_player_head_owner(a1,item("stick"),"NAME");
```

<h3 id=set_variable_get_player_head_value>
  <code>variable::get_player_head_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить владельца головы на местоположении\
**Тип:** Действие, возращающее значение\
**Описание:** Получает имя или UUID владельца головы на местоположении и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_player_head_value(location(0,0,0,0,0),"NAME");

#Или от объекта

a1 = location(0,0,0,0,0).get_player_head_value("NAME");

#Или в сухую

variable::get_player_head_value(a1,location(0,0,0,0,0),"NAME");
```

<h3 id=set_variable_get_potion_effect_amplifier>
  <code>variable::get_potion_effect_amplifier</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить силу зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение силы зелья.

**Пример использования:** 
```ts
a1 = variable::get_potion_effect_amplifier(potion("slow_falling"));

#Или от объекта

a1 = potion("slow_falling").get_potion_effect_amplifier();

#Или в сухую

variable::get_potion_effect_amplifier(a1,potion("slow_falling"));
```

<h3 id=set_variable_get_potion_effect_duration>
  <code>variable::get_potion_effect_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить длительность зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение длительности зелья.

**Пример использования:** 
```ts
a1 = variable::get_potion_effect_duration(potion("slow_falling"));

#Или от объекта

a1 = potion("slow_falling").get_potion_effect_duration();

#Или в сухую

variable::get_potion_effect_duration(a1,potion("slow_falling"));
```

<h3 id=set_variable_get_potion_effect_type>
  <code>variable::get_potion_effect_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение типа зелья.

**Пример использования:** 
```ts
a1 = variable::get_potion_effect_type(potion("slow_falling"));

#Или от объекта

a1 = potion("slow_falling").get_potion_effect_type();

#Или в сухую

variable::get_potion_effect_type(a1,potion("slow_falling"));
```

<h3 id=set_variable_get_sculk_shrieker_warning_level>
  <code>variable::get_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить уровень опасности скалк-крикуна\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной уровень опасности скалк-крикуна на указанном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_sculk_shrieker_warning_level(location(0,0,0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).get_sculk_shrieker_warning_level();

#Или в сухую

variable::get_sculk_shrieker_warning_level(a1,location(0,0,0,0,0));
```

<h3 id=set_variable_get_sign_text>
  <code>variable::get_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить текст строки таблички\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение текста строки таблички на выбранном местоположении.

**Пример использования:** 
```ts
a1 = variable::get_sign_text(location(0,0,0,0,0),"FRONT","FIRST");

#Или от объекта

a1 = location(0,0,0,0,0).get_sign_text("FRONT","FIRST");

#Или в сухую

variable::get_sign_text(a1,location(0,0,0,0,0),"FRONT","FIRST");
```

<h3 id=set_variable_get_sound_pitch>
  <code>variable::get_sound_pitch</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить высоту звука\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение высоты звука.

**Пример использования:** 
```ts
a1 = variable::get_sound_pitch(sound("entity.zombie.hurt"));

#Или от объекта

a1 = sound("entity.zombie.hurt").get_sound_pitch();

#Или в сухую

variable::get_sound_pitch(a1,sound("entity.zombie.hurt"));
```

<h3 id=set_variable_get_sound_source>
  <code>variable::get_sound_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить источник звука\
**Тип:** Действие, возращающее значение\
**Описание:** Получить источник звука и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_sound_source(sound("entity.zombie.hurt"));

#Или от объекта

a1 = sound("entity.zombie.hurt").get_sound_source();

#Или в сухую

variable::get_sound_source(a1,sound("entity.zombie.hurt"));
```

<h3 id=set_variable_get_sound_type>
  <code>variable::get_sound_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип звука\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение типа звука.

**Пример использования:** 
```ts
a1 = variable::get_sound_type(sound("entity.zombie.hurt"));

#Или от объекта

a1 = sound("entity.zombie.hurt").get_sound_type();

#Или в сухую

variable::get_sound_type(a1,sound("entity.zombie.hurt"));
```

<h3 id=set_variable_get_sound_variation>
  <code>variable::get_sound_variation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить вариацию звука\
**Тип:** Действие, возращающее значение\
**Описание:** Получает вариацию звука и присваивает результат к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Возвращает пустой текст, если используется случайный сид.

**Пример использования:** 
```ts
a1 = variable::get_sound_variation(sound("entity.zombie.hurt"));

#Или от объекта

a1 = sound("entity.zombie.hurt").get_sound_variation();

#Или в сухую

variable::get_sound_variation(a1,sound("entity.zombie.hurt"));
```

<h3 id=set_variable_get_sound_variations>
  <code>variable::get_sound_variations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить вариации звука\
**Тип:** Действие, возращающее значение\
**Описание:** Получает список всех вариаций звука и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_sound_variations(sound("entity.zombie.hurt"));

#Или от объекта

a1 = sound("entity.zombie.hurt").get_sound_variations();

#Или в сухую

variable::get_sound_variations(a1,sound("entity.zombie.hurt"));
```

<h3 id=set_variable_get_sound_volume_action>
  <code>variable::get_sound_volume_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить громкость звука\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение громкости звука.

**Пример использования:** 
```ts
a1 = variable::get_sound_volume_action(sound("entity.zombie.hurt"));

#Или от объекта

a1 = sound("entity.zombie.hurt").get_sound_volume_action();

#Или в сухую

variable::get_sound_volume_action(a1,sound("entity.zombie.hurt"));
```

<h3 id=set_variable_get_template_code>
  <code>variable::get_template_code</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить код из шаблона\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной код из шаблона.

**Пример использования:** 
```ts
a1 = variable::get_template_code(item("stick"),"TEXT");

#Или от объекта

a1 = item("stick").get_template_code("TEXT");

#Или в сухую

variable::get_template_code(a1,item("stick"),"TEXT");
```

<h3 id=set_variable_text_length>
  <code>variable::get_text_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить длину текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение количества символов в тексте.

**Пример использования:** 
```ts
a1 = variable::get_text_length("text");

#Или от объекта

a1 = "text".get_text_length();

#Или в сухую

variable::get_text_length(a1,"text");
```

<h3 id=set_variable_get_text_width>
  <code>variable::get_text_width</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить ширину текста в пикселях\
**Тип:** Действие, возращающее значение\
**Описание:** Получает размер каждого символа в тексте, суммирует их и присваивает результат к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Значения могут быть не актуальными, если используется ресурспак со своими символами.

**Пример использования:** 
```ts
a1 = variable::get_text_width("text");

#Или от объекта

a1 = "text".get_text_width();

#Или в сухую

variable::get_text_width(a1,"text");
```

<h3 id=set_variable_get_vector_all_components>
  <code>variable::get_vector_all_components</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить все координаты вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Получает все координаты вектора и присваивает результат к переменным.

**Пример использования:** 
```ts
a1, a2, a3 = variable::get_vector_all_components(vector(0,0,0));

#Или от объекта

a1, a2, a3 = vector(0,0,0).get_vector_all_components();

#Или в сухую

variable::get_vector_all_components(vector(0,0,0),a1,a2,a3);
```

<h3 id=set_variable_get_vector_between_locations>
  <code>variable::get_vector_between_locations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать вектор между местоположениями\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт вектор между начальным и конечным местоположениями и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_vector_between_locations(location(0,0,0,0,0),location(0,0,0,0,0));

#Или в сухую

variable::get_vector_between_locations(a1,location(0,0,0,0,0),location(0,0,0,0,0));
```

<h3 id=set_variable_get_vector_component>
  <code>variable::get_vector_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить координату вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённую координату вектора и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::get_vector_component(vector(0,0,0),"X");

#Или от объекта

a1 = vector(0,0,0).get_vector_component("X");

#Или в сухую

variable::get_vector_component(a1,vector(0,0,0),"X");
```

<h3 id=set_variable_get_vector_from_block_face>
  <code>variable::get_vector_from_block_face</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать вектор из кардинального направления\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт нормализированный вектор в зависимости от указанного кардинального направления ("south", "north", "east", "west", "up", "down").

**Пример использования:** 
```ts
a1 = variable::get_vector_from_block_face("block_face");

#Или в сухую

variable::get_vector_from_block_face(a1,"block_face");
```

<h3 id=set_variable_get_vector_length>
  <code>variable::get_vector_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить длину вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение длины вектора.

**Пример использования:** 
```ts
a1 = variable::get_vector_length(vector(0,0,0),"LENGTH");

#Или от объекта

a1 = vector(0,0,0).get_vector_length("LENGTH");

#Или в сухую

variable::get_vector_length(a1,vector(0,0,0),"LENGTH");
```

<h3 id=set_variable_hash>
  <code>variable::get_text_hash</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить хеш текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение хеша текста.

**Пример использования:** 
```ts
a1 = variable::get_text_hash("text","MD5");

#Или от объекта

a1 = "text".get_text_hash("MD5");

#Или в сухую

variable::get_text_hash(a1,"text","MD5");
```

<h3 id=set_variable_increment>
  <code>variable::increment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Прибавление (+=)\
**Тип:** Действие, возращающее значение\
**Описание:** Прибавляет к переменной выбранное число.

**Пример использования:** 
```ts
a1 = variable::increment(1);

#Или от объекта

a1 = (1).increment();

#Или в сухую

variable::increment(a1,1);
```

<h3 id=set_variable_insert_list_value>
  <code>variable::insert_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Вставить значение в список\
**Тип:** Действие, возращающее значение\
**Описание:** Вставляет значение в список по указанному индексу, сдвигая все значения в нем после него вправо.

**Пример использования:** 
```ts
a1 = variable::insert_list_value(`list`,1,"any value");

#Или от объекта

a1 = `list`.insert_list_value(1,"any value");

#Или в сухую

variable::insert_list_value(a1,`list`,1,"any value");
```

<h3 id=set_variable_join_text>
  <code>variable::join_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Объединить список в текст\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет элементы списка в единый текст и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::join_text(`list`,"separator","prefix","postfix",1,"truncated");

#Или от объекта

a1 = `list`.join_text("separator","prefix","postfix",1,"truncated");

#Или в сухую

variable::join_text(a1,`list`,"separator","prefix","postfix",1,"truncated");
```

<h3 id=set_variable_lerp_number>
  <code>variable::lerp_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Интерполировать число\
**Тип:** Действие, возращающее значение\
**Описание:** Вычисляет число между двумя числами с определённым коэффициентом и присваивает результат к переменной. При коэффициенте 0 будет возвращено первое число, при 1 - второе, при 0.5 - среднее значение.

**Пример использования:** 
```ts
a1 = variable::lerp_number(1,2,3);

#Или от объекта

a1 = (3).lerp_number(1,2);

#Или в сухую

variable::lerp_number(a1,1,2,3);
```

<h3 id=set_variable_location_relative>
  <code>variable::location_relative</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить относительное местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает местоположение относительно стороны блока на определённом расстоянии, присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::location_relative(location(0,0,0,0,0),1,"NORTH");

#Или от объекта

a1 = location(0,0,0,0,0).location_relative(1,"NORTH");

#Или в сухую

variable::location_relative(a1,location(0,0,0,0,0),1,"NORTH");
```

<h3 id=set_variable_locations_distance>
  <code>variable::locations_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить расстояние между местоположениями\
**Тип:** Действие, возращающее значение\
**Описание:** Получает расстояние между местоположениями и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::locations_distance(location(0,0,0,0,0),location(0,0,0,0,0),"THREE_D");

#Или в сухую

variable::locations_distance(a1,location(0,0,0,0,0),location(0,0,0,0,0),"THREE_D");
```

<h3 id=set_variable_log>
  <code>variable::log</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Логарифм числа (log)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение логарифма с выбранным аргументом и основанием.

**Пример использования:** 
```ts
a1 = variable::log(1,2);

#Или от объекта

a1 = (1).log(2);

#Или в сухую

variable::log(a1,1,2);
```

<h3 id=set_variable_map_range>
  <code>variable::map_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Перевести число в другой диапазон\
**Тип:** Действие, возращающее значение\
**Описание:** Переводит число с одного диапазона в другой и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::map_range(1,2,3,4,5);

#Или от объекта

a1 = (1).map_range(2,3,4,5);

#Или в сухую

variable::map_range(a1,1,2,3,4,5);
```

<h3 id=set_variable_max>
  <code>variable::max</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Максимальное значение\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной наибольшее число из выбранных.

**Пример использования:** 
```ts
a1 = variable::max([1, 2]);

#Или в сухую

variable::max(a1,[1, 2]);
```

<h3 id=set_variable_min>
  <code>variable::min</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Минимальное значение\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной наименьшее число из выбранных.

**Пример использования:** 
```ts
a1 = variable::min([1, 2]);

#Или в сухую

variable::min(a1,[1, 2]);
```

<h3 id=set_variable_multiply>
  <code>variable::multiply</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Умножение чисел (×)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной произведение чисел.

**Пример использования:** 
```ts
a1 = variable::multiply([1, 2]);

#Или в сухую

variable::multiply(a1,[1, 2]);
```

<h3 id=set_variable_multiply_vector>
  <code>variable::multiply_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Умножить вектор на число\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат умножения вектора на число.

**Пример использования:** 
```ts
a1 = variable::multiply_vector(vector(0,0,0),1);

#Или в сухую

variable::multiply_vector(a1,vector(0,0,0),1);
```

<h3 id=set_variable_parse_json>
  <code>variable::parse_json</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Разобрать JSON\
**Тип:** Действие, возращающее значение\
**Описание:** Разбирает текст JSON на элементы: словари (если текст заключен в фигурные скобки) и списки (если текст заключен в квадратные скобки), с которыми можно работать, чтобы получить нужные значения.

**Пример использования:** 
```ts
a1 = variable::parse_json("json");

#Или в сухую

variable::parse_json(a1,"json");
```

<h3 id=set_variable_parse_to_component>
  <code>variable::parse_to_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать в стилизуемый текст\
**Тип:** Действие, возращающее значение\
**Описание:** Преобразует обычный текст в стилизуемый текст.

**Пример использования:** 
```ts
a1 = variable::parse_to_component("text","PLAIN");

#Или от объекта

a1 = "text".parse_to_component("PLAIN");

#Или в сухую

variable::parse_to_component(a1,"text","PLAIN");
```

<h3 id=set_variable_perlin_noise_3d>
  <code>variable::perlin_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Шум Перлина\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение шума Перлина в определённом местоположении. Возвращает число, со значением от -1 до 1.

**Пример использования:** 
```ts
a1 = variable::perlin_noise_3d(location(0,0,0,0,0),1,2,3,4,5,"ZERO_TO_ONE","TRUE");

#Или в сухую

variable::perlin_noise_3d(a1,location(0,0,0,0,0),1,2,3,4,5,"ZERO_TO_ONE","TRUE");
```

<h3 id=set_variable_pow>
  <code>variable::pow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Степень числа (^)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение степени с выбранным основанием и показателем.

**Пример использования:** 
```ts
a1 = variable::pow(1,2);

#Или от объекта

a1 = (1).pow(2);

#Или в сухую

variable::pow(a1,1,2);
```

<h3 id=set_variable_purge>
  <code>variable::purge</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить переменные\
**Тип:** Действие без значения\
**Описание:** Очищает все переменные, подходящие под выбранные имена.

**Пример использования:** 
```ts
variable::purge(["names", "names"],"GAME","EQUALS","TRUE");
```

<h3 id=set_variable_random>
  <code>variable::random</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить случайное значение\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает случайное значение к переменной.

**Пример использования:** 
```ts
a1 = variable::random(["any value", "any value"]);

#Или в сухую

variable::random(a1,["any value", "any value"]);
```

<h3 id=set_variable_randomize_list_order>
  <code>variable::randomize_list_order</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Рандомизировать список\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает порядок элементов случайным образом.

**Пример использования:** 
```ts
a1 = variable::randomize_list_order(`list`);

#Или от объекта

a1 = `list`.randomize_list_order();

#Или в сухую

variable::randomize_list_order(a1,`list`);
```

<h3 id=set_variable_random_location>
  <code>variable::random_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать случайное местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт случайное местоположение в регионе между двумя углами и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::random_location(location(0,0,0,0,0),location(0,0,0,0,0),"TRUE");

#Или в сухую

variable::random_location(a1,location(0,0,0,0,0),location(0,0,0,0,0),"TRUE");
```

<h3 id=set_variable_random_number>
  <code>variable::random_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Случайное число\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной случайное число в выбранном диапазоне.

**Пример использования:** 
```ts
a1 = variable::random_number(1,2,"TRUE");

#Или в сухую

variable::random_number(a1,1,2,"TRUE");
```

<h3 id=set_variable_ray_trace_result>
  <code>variable::ray_trace_result</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить результат рейкаста\
**Тип:** Действие, возращающее значение\
**Описание:** Запускает луч с заданными параметрами. При столкновении луча с указанными объектами (с сущностью или блоком) можно получить местоположение падения луча, местоположение и сторону блока, UUID сущности и сторону хитбокса. Ширина луча работает только на сущностей (увеличивает или уменьшает хитбоксы существ).

**Пример использования:** 
```ts
a1, a2, a3, a4 = variable::ray_trace_result(location(0,0,0,0,0),1,2,"ONLY_BLOCKS","TRUE","NEVER",`entities`);

#Или в сухую

variable::ray_trace_result(location(0,0,0,0,0),1,2,"ONLY_BLOCKS","TRUE","NEVER",a1,a2,a3,a4,`entities`);
```

<h3 id=set_variable_reflect_vector_product>
  <code>variable::reflect_vector_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отразить вектор относительно второго вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Отражает вектор относительно другого вектора и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::reflect_vector_product(vector(0,0,0),vector(0,0,0),1);

#Или в сухую

variable::reflect_vector_product(a1,vector(0,0,0),vector(0,0,0),1);
```

<h3 id=set_variable_regex_replace_text>
  <code>variable::regex_replace_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заменить совпадение с регулярным выражением\
**Тип:** Действие, возращающее значение\
**Описание:** Заменяет текст, соответствующий указанному регулярному выражению, и присваивает результат к переменной. Аргумент "Замена" может содержать $<название группы> для ссылки на группу. Включайте только те флаги, которые вам нужны!

**Пример использования:** 
```ts
a1 = variable::regex_replace_text("text","regex","replacement","ANY","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE");

#Или от объекта

a1 = "text".regex_replace_text("regex","replacement","ANY","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE");

#Или в сухую

variable::regex_replace_text(a1,"text","regex","replacement","ANY","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE","TRUE");
```

<h3 id=set_variable_remainder>
  <code>variable::remainder</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Остаток от деления (%)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной остаток от деления двух чисел.

**Пример использования:** 
```ts
a1 = variable::remainder(1,2,"REMAINDER");

#Или от объекта

a1 = (1).remainder(2,"REMAINDER");

#Или в сухую

variable::remainder(a1,1,2,"REMAINDER");
```

<h3 id=set_variable_remove_compass_lodestone>
  <code>variable::remove_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить местоположение магнетита\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет с намагниченного компаса местоположение магнетита и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::remove_compass_lodestone(item("stick"));

#Или от объекта

a1 = item("stick").remove_compass_lodestone();

#Или в сухую

variable::remove_compass_lodestone(a1,item("stick"));
```

<h3 id=set_variable_remove_item_attribute>
  <code>variable::remove_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить атрибут у предмета\
**Тип:** Действие без значения\
**Описание:** Удаляет атрибут у предмета и присваивает результат к переменной.

**Пример использования:** 
```ts
variable::remove_item_attribute(a1,item("stick"),"name_or_uuid","GENERIC_ARMOR");

#Или от объекта

item("stick").remove_item_attribute(a1,"name_or_uuid","GENERIC_ARMOR");
```

<h3 id=set_variable_remove_item_custom_model_data>
  <code>variable::remove_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить данные модели предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет данные модели предмета (CustomModelData) и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::remove_item_custom_model_data(item("stick"));

#Или от объекта

a1 = item("stick").remove_item_custom_model_data();

#Или в сухую

variable::remove_item_custom_model_data(a1,item("stick"));
```

<h3 id=set_variable_remove_item_custom_tag>
  <code>variable::remove_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить кастомный тег предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет кастомный тег предмета и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::remove_item_custom_tag(item("stick"),"tag_name");

#Или от объекта

a1 = item("stick").remove_item_custom_tag("tag_name");

#Или в сухую

variable::remove_item_custom_tag(a1,item("stick"),"tag_name");
```

<h3 id=set_variable_remove_enchantment>
  <code>variable::remove_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить зачарование предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет зачарование с предмета и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::remove_enchantment(item("stick"),"enchantment");

#Или от объекта

a1 = item("stick").remove_enchantment("enchantment");

#Или в сухую

variable::remove_enchantment(a1,item("stick"),"enchantment");
```

<h3 id=set_variable_remove_item_lore_line>
  <code>variable::remove_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить строку описания предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет строку описания предмета и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::remove_item_lore_line(item("stick"),1);

#Или от объекта

a1 = item("stick").remove_item_lore_line(1);

#Или в сухую

variable::remove_item_lore_line(a1,item("stick"),1);
```

<h3 id=set_variable_remove_item_potion_effects>
  <code>variable::remove_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить эффекты зелий из предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет эффекты зелий из предмета и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::remove_item_potion_effects(item("stick"),[potion("slow_falling"), potion("slow_falling")]);

#Или от объекта

a1 = item("stick").remove_item_potion_effects([potion("slow_falling"), potion("slow_falling")]);

#Или в сухую

variable::remove_item_potion_effects(a1,item("stick"),[potion("slow_falling"), potion("slow_falling")]);
```

<h3 id=set_variable_remove_list_duplicates>
  <code>variable::remove_list_duplicates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить повторяющиеся значения\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет все значения, которые попадаются в списке больше одного раза.

**Пример использования:** 
```ts
a1 = variable::remove_list_duplicates(`list`);

#Или от объекта

a1 = `list`.remove_list_duplicates();

#Или в сухую

variable::remove_list_duplicates(a1,`list`);
```

<h3 id=set_variable_remove_list_value>
  <code>variable::remove_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить значение из списка\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет указанное значение из списка.

**Пример использования:** 
```ts
a1 = variable::remove_list_value(`list`,"any value","FIRST");

#Или от объекта

a1 = `list`.remove_list_value("any value","FIRST");

#Или в сухую

variable::remove_list_value(a1,`list`,"any value","FIRST");
```

<h3 id=set_variable_remove_list_value_at_index>
  <code>variable::remove_list_value_at_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить значение из списка по индексу\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет значение из списка, которое находится по указанному индексу.

**Пример использования:** 
```ts
a2, a1 = variable::remove_list_value_at_index(`list`,1);

#Или от объекта

a2, a1 = `list`.remove_list_value_at_index(1);

#Или в сухую

variable::remove_list_value_at_index(a1,a2,`list`,1);
```

<h3 id=set_variable_remove_map_entry>
  <code>variable::remove_map_entry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить элемент словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет элемент словаря и присваивает результат к переменной.

**Пример использования:** 
```ts
a2, a1 = variable::remove_map_entry(`map`,"any value",["any value", "any value"]);

#Или от объекта

a2, a1 = `map`.remove_map_entry("any value",["any value", "any value"]);

#Или в сухую

variable::remove_map_entry(a1,a2,`map`,"any value",["any value", "any value"]);
```

<h3 id=set_variable_remove_text>
  <code>variable::remove_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить текст\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет весь текст или его часть и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::remove_text("text","TRUE",["remove", "remove"]);

#Или от объекта

a1 = "text".remove_text("TRUE",["remove", "remove"]);

#Или в сухую

variable::remove_text(a1,"text","TRUE",["remove", "remove"]);
```

<h3 id=set_variable_repeat_text>
  <code>variable::repeat_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Повторить текст\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной текст, повторённый определённое количество раз.

**Пример использования:** 
```ts
a1 = variable::repeat_text("text",1);

#Или от объекта

a1 = "text".repeat_text(1);

#Или в сухую

variable::repeat_text(a1,"text",1);
```

<h3 id=set_variable_replace_text>
  <code>variable::replace_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заменить текст\
**Тип:** Действие, возращающее значение\
**Описание:** Заменяет весь текст или его часть и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::replace_text("text","replace","replacement","ANY","TRUE");

#Или от объекта

a1 = "text".replace_text("replace","replacement","ANY","TRUE");

#Или в сухую

variable::replace_text(a1,"text","replace","replacement","ANY","TRUE");
```

<h3 id=set_variable_reverse_list>
  <code>variable::reverse_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Перевернуть список\
**Тип:** Действие, возращающее значение\
**Описание:** Меняет порядок следования элементов на обратный.

**Пример использования:** 
```ts
a1 = variable::reverse_list(`list`);

#Или от объекта

a1 = `list`.reverse_list();

#Или в сухую

variable::reverse_list(a1,`list`);
```

<h3 id=set_variable_root>
  <code>variable::root</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Корень числа (√)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение корня с выбранным подкоренным числом и показателем.

**Пример использования:** 
```ts
a1 = variable::root(1,2);

#Или в сухую

variable::root(a1,1,2);
```

<h3 id=set_variable_rotate_vector_around_axis>
  <code>variable::rotate_vector_around_axis</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Повернуть вектор вокруг оси\
**Тип:** Действие, возращающее значение\
**Описание:** Поворачивает вектор вокруг оси на определённое значение и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::rotate_vector_around_axis(vector(0,0,0),1,"X","DEGREES");

#Или от объекта

a1 = vector(0,0,0).rotate_vector_around_axis(1,"X","DEGREES");

#Или в сухую

variable::rotate_vector_around_axis(a1,vector(0,0,0),1,"X","DEGREES");
```

<h3 id=set_variable_rotate_vector_around_vector>
  <code>variable::rotate_vector_around_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Повернуть вектор вокруг другого вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Поворачивает вектор вокруг другого вектора на определённое значение и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::rotate_vector_around_vector(vector(0,0,0),vector(0,0,0),1,"DEGREES");

#Или от объекта

a1 = vector(0,0,0).rotate_vector_around_vector(vector(0,0,0),1,"DEGREES");

#Или в сухую

variable::rotate_vector_around_vector(a1,vector(0,0,0),vector(0,0,0),1,"DEGREES");
```

<h3 id=set_variable_round>
  <code>variable::round</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Округлить число\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной округлённое выбранным способом число.

**Пример использования:** 
```ts
a1 = variable::round(1,2,"ROUND");

#Или от объекта

a1 = (1).round(2,"ROUND");

#Или в сухую

variable::round(a1,1,2,"ROUND");
```

<h3 id=set_variable_set_all_coordinates>
  <code>variable::set_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Создает местоположение из указанных координат.

**Пример использования:** 
```ts
a1 = variable::set_all_coordinates(1,2,3,4,5);

#Или в сухую

variable::set_all_coordinates(a1,1,2,3,4,5);
```

<h3 id=set_variable_set_armor_trim>
  <code>variable::set_armor_trim</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить броне шаблон\
**Тип:** Действие без значения\
**Описание:** Устанавливает броне указанный шаблон и присваивает результат к переменной.

**Пример использования:** 
```ts
variable::set_armor_trim(a1,item("stick"),item("stick"),item("stick"));

#Или от объекта

item("stick").set_armor_trim(a1,item("stick"),item("stick"));
```

<h3 id=set_variable_set_book_page>
  <code>variable::set_book_page</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить текст книги на странице\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает текст книги на определённой странице и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_book_page(item("stick"),"text",1,"MERGE");

#Или от объекта

a1 = item("stick").set_book_page("text",1,"MERGE");

#Или в сухую

variable::set_book_page(a1,item("stick"),"text",1,"MERGE");
```

<h3 id=set_variable_set_book_pages>
  <code>variable::set_book_pages</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить текст книги\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает текст книги и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_book_pages(item("stick"),["text", "text"]);

#Или от объекта

a1 = item("stick").set_book_pages(["text", "text"]);

#Или в сухую

variable::set_book_pages(a1,item("stick"),["text", "text"]);
```

<h3 id=set_variable_set_bundle_items>
  <code>variable::set_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Изменить содержимое мешка\
**Тип:** Действие без значения\
**Описание:** Изменяет содержимое мешка и присваивает результат к переменной.

**Пример использования:** 
```ts
variable::set_bundle_items(a1,item("stick"),[item("stick"), item("stick")],"ADD");

#Или от объекта

item("stick").set_bundle_items(a1,[item("stick"), item("stick")],"ADD");
```

<h3 id=set_variable_set_compass_lodestone>
  <code>variable::set_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить местоположение магнетита\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает компасу местоположение магнетита и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_compass_lodestone(item("stick"),location(0,0,0,0,0),"TRUE");

#Или от объекта

a1 = item("stick").set_compass_lodestone(location(0,0,0,0,0),"TRUE");

#Или в сухую

variable::set_compass_lodestone(a1,item("stick"),location(0,0,0,0,0),"TRUE");
```

<h3 id=set_variable_set_component_children>
  <code>variable::set_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дочерние части стилизуемому тексту\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной стилизуемый текст с указанными дочерними частями.

**Пример использования:** 
```ts
a1 = variable::set_component_children("component",["children", "children"]);

#Или от объекта

a1 = "component".set_component_children(["children", "children"]);

#Или в сухую

variable::set_component_children(a1,"component",["children", "children"]);
```

<h3 id=set_variable_set_component_click>
  <code>variable::set_component_click</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту действие при нажатии\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту действие при нажатии и присваивает его к переменной.

**Пример использования:** 
```ts
a1 = variable::set_component_click("component","value","COPY_TO_CLIPBOARD");

#Или от объекта

a1 = "component".set_component_click("value","COPY_TO_CLIPBOARD");

#Или в сухую

variable::set_component_click(a1,"component","value","COPY_TO_CLIPBOARD");
```

<h3 id=set_variable_set_component_decorations>
  <code>variable::set_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить декорации стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает декорации указанному стилизуемому тексту и присваивает его к переменной.

**Пример использования:** 
```ts
a1 = variable::set_component_decorations("component","FALSE","FALSE","FALSE","FALSE","FALSE");

#Или от объекта

a1 = "component".set_component_decorations("FALSE","FALSE","FALSE","FALSE","FALSE");

#Или в сухую

variable::set_component_decorations(a1,"component","FALSE","FALSE","FALSE","FALSE","FALSE");
```

<h3 id=set_variable_set_component_entity_hover>
  <code>variable::set_component_entity_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту сущность при наведении\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту сущность, отображаемую при наведении и присваивает его к переменной.

**Пример использования:** 
```ts
a1 = variable::set_component_entity_hover("component","name_or_uuid");

#Или от объекта

a1 = "component".set_component_entity_hover("name_or_uuid");

#Или в сухую

variable::set_component_entity_hover(a1,"component","name_or_uuid");
```

<h3 id=set_variable_set_component_font>
  <code>variable::set_component_font</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить шрифт стилизуемому тексту\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает шрифт указанному стилизуемому тексту и присваивает его к переменной.

**Пример использования:** 
```ts
a1 = variable::set_component_font("component","namespace","value");

#Или от объекта

a1 = "component".set_component_font("namespace","value");

#Или в сухую

variable::set_component_font(a1,"component","namespace","value");
```

<h3 id=set_variable_set_component_hex_color>
  <code>variable::set_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить HEX-цвет стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает HEX-цвет указанному стилизуемому тексту и присваивает его к переменной.

**Пример использования:** 
```ts
a1 = variable::set_component_hex_color("component","color");

#Или от объекта

a1 = "component".set_component_hex_color("color");

#Или в сухую

variable::set_component_hex_color(a1,"component","color");
```

<h3 id=set_variable_set_component_hover>
  <code>variable::set_component_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту текст при наведении\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту текст, отображаемый при наведении и присваивает его к переменной.

**Пример использования:** 
```ts
a1 = variable::set_component_hover("component","hover");

#Или от объекта

a1 = "component".set_component_hover("hover");

#Или в сухую

variable::set_component_hover(a1,"component","hover");
```

<h3 id=set_variable_set_component_insertion>
  <code>variable::set_component_insertion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту предлагаемое сообщение\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту предлагаемое сообщение при нажатии с Shift и присваивает его к переменной.

**Пример использования:** 
```ts
a1 = variable::set_component_insertion("component","insertion");

#Или от объекта

a1 = "component".set_component_insertion("insertion");

#Или в сухую

variable::set_component_insertion(a1,"component","insertion");
```

<h3 id=set_variable_set_component_item_hover>
  <code>variable::set_component_item_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту предмет при наведении\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту предмет, отображаемый при наведении и присваивает его к переменной.

**Пример использования:** 
```ts
a1 = variable::set_component_item_hover("component",item("stick"));

#Или от объекта

a1 = "component".set_component_item_hover(item("stick"));

#Или в сухую

variable::set_component_item_hover(a1,"component",item("stick"));
```

<h3 id=set_variable_set_coordinate>
  <code>variable::set_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить координату местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает значение выбранной координаты в местоположение и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_coordinate(location(0,0,0,0,0),1,"X");

#Или от объекта

a1 = location(0,0,0,0,0).set_coordinate(1,"X");

#Или в сухую

variable::set_coordinate(a1,location(0,0,0,0,0),1,"X");
```

<h3 id=set_variable_set_item_amount>
  <code>variable::set_item_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить количество предметов\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает количество предметов в стаке.

**Пример использования:** 
```ts
a1 = variable::set_item_amount(item("stick"),1);

#Или от объекта

a1 = item("stick").set_item_amount(1);

#Или в сухую

variable::set_item_amount(a1,item("stick"),1);
```

<h3 id=set_variable_set_item_attribute>
  <code>variable::set_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить атрибут предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Добавляет определённый атрибут предмету и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_attribute(item("stick"),1,"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");

#Или от объекта

a1 = item("stick").set_item_attribute(1,"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");

#Или в сухую

variable::set_item_attribute(a1,item("stick"),1,"name","GENERIC_ARMOR","ALL","MULTIPLY_SCALAR_1");
```

<h3 id=set_variable_set_item_color>
  <code>variable::set_item_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанный цвет предмету и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_color(item("stick"),"color");

#Или от объекта

a1 = item("stick").set_item_color("color");

#Или в сухую

variable::set_item_color(a1,item("stick"),"color");
```

<h3 id=set_variable_set_item_custom_model_data>
  <code>variable::set_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить данные модели предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает данные модели предмета (CustomModelData) и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_custom_model_data(item("stick"),1);

#Или от объекта

a1 = item("stick").set_item_custom_model_data(1);

#Или в сухую

variable::set_item_custom_model_data(a1,item("stick"),1);
```

<h3 id=set_variable_set_item_custom_tag>
  <code>variable::set_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить кастомный тег предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает кастомный тег предмету и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_custom_tag(item("stick"),"tag_name","tag_value");

#Или от объекта

a1 = item("stick").set_item_custom_tag("tag_name","tag_value");

#Или в сухую

variable::set_item_custom_tag(a1,item("stick"),"tag_name","tag_value");
```

<h3 id=set_variable_set_item_destroyable_blocks>
  <code>variable::set_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмету блоки для ломания\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает предмету блоки, которые можно им ломать, и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_destroyable_blocks(item("stick"),[item("stick"), item("stick")]);

#Или от объекта

a1 = item("stick").set_item_destroyable_blocks([item("stick"), item("stick")]);

#Или в сухую

variable::set_item_destroyable_blocks(a1,item("stick"),[item("stick"), item("stick")]);
```

<h3 id=set_variable_set_item_durability>
  <code>variable::set_item_durability</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить прочность предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает прочность предмету и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_durability(item("stick"),1,"DAMAGE");

#Или от объекта

a1 = item("stick").set_item_durability(1,"DAMAGE");

#Или в сухую

variable::set_item_durability(a1,item("stick"),1,"DAMAGE");
```

<h3 id=set_variable_set_item_enchantments>
  <code>variable::set_item_enchantments</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить зачарования предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает зачарования предмету и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_enchantments(item("stick"),`enchantments`);

#Или от объекта

a1 = item("stick").set_item_enchantments(`enchantments`);

#Или в сухую

variable::set_item_enchantments(a1,item("stick"),`enchantments`);
```

<h3 id=set_variable_set_item_lore>
  <code>variable::set_item_lore</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить описание предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает описание предмета.\
**Дополнительная информация:**\
&nbsp;&nbsp;Очищает описание если не указано новое.

**Пример использования:** 
```ts
a1 = variable::set_item_lore(["lore", "lore"],item("stick"));

#Или от объекта

a1 = item("stick").set_item_lore(["lore", "lore"]);

#Или в сухую

variable::set_item_lore(a1,["lore", "lore"],item("stick"));
```

<h3 id=set_variable_set_item_lore_line>
  <code>variable::set_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить строку описания предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает строку описания предмета.

**Пример использования:** 
```ts
a1 = variable::set_item_lore_line(item("stick"),"text",1,"MERGE");

#Или от объекта

a1 = item("stick").set_item_lore_line("text",1,"MERGE");

#Или в сухую

variable::set_item_lore_line(a1,item("stick"),"text",1,"MERGE");
```

<h3 id=set_variable_set_item_type>
  <code>variable::set_item_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Меняет тип предмета, не изменяя другие данные предмета.

**Пример использования:** 
```ts
a1 = variable::set_item_type(item("stick"),"type");

#Или от объекта

a1 = item("stick").set_item_type("type");

#Или в сухую

variable::set_item_type(a1,item("stick"),"type");
```

<h3 id=set_variable_set_item_name>
  <code>variable::set_item_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить имя предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает отображаемое имя предмета.

**Пример использования:** 
```ts
a1 = variable::set_item_name(item("stick"),"text");

#Или от объекта

a1 = item("stick").set_item_name("text");

#Или в сухую

variable::set_item_name(a1,item("stick"),"text");
```

<h3 id=set_variable_set_item_placeable_blocks>
  <code>variable::set_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмету блоки для установки\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает предмету блоки, на который его можно поставить, и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_placeable_blocks(item("stick"),[item("stick"), item("stick")]);

#Или от объекта

a1 = item("stick").set_item_placeable_blocks([item("stick"), item("stick")]);

#Или в сухую

variable::set_item_placeable_blocks(a1,item("stick"),[item("stick"), item("stick")]);
```

<h3 id=set_variable_set_item_unbreakable>
  <code>variable::set_item_unbreakable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить неломаемость предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает неломаемость предмету и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_unbreakable(item("stick"),"TRUE");

#Или от объекта

a1 = item("stick").set_item_unbreakable("TRUE");

#Или в сухую

variable::set_item_unbreakable(a1,item("stick"),"TRUE");
```

<h3 id=set_variable_set_item_visibility_flags>
  <code>variable::set_item_visibility_flags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить флаги видимости предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает определённые флаги видимости предмету и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_item_visibility_flags(item("stick"),"ON","ON","ON","ON","ON","ON","ON","ON");

#Или от объекта

a1 = item("stick").set_item_visibility_flags("ON","ON","ON","ON","ON","ON","ON","ON");

#Или в сухую

variable::set_item_visibility_flags(a1,item("stick"),"ON","ON","ON","ON","ON","ON","ON","ON");
```

<h3 id=set_variable_set_list_value>
  <code>variable::set_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить значение списка\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает значение списка по указанному индексу.

**Пример использования:** 
```ts
a1 = variable::set_list_value(`list`,1,"any value");

#Или от объекта

a1 = `list`.set_list_value(1,"any value");

#Или в сухую

variable::set_list_value(a1,`list`,1,"any value");
```

<h3 id=set_variable_set_location_direction>
  <code>variable::set_location_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить направление местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает направление местоположения и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_location_direction(location(0,0,0,0,0),vector(0,0,0));

#Или от объекта

a1 = location(0,0,0,0,0).set_location_direction(vector(0,0,0));

#Или в сухую

variable::set_location_direction(a1,location(0,0,0,0,0),vector(0,0,0));
```

<h3 id=set_variable_set_map_value>
  <code>variable::set_map_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить значение словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает определённое значение словаря по ключу и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_map_value(`map`,"any value","any value");

#Или от объекта

a1 = `map`.set_map_value("any value","any value");

#Или в сухую

variable::set_map_value(a1,`map`,"any value","any value");
```

<h3 id=set_variable_set_particle_amount>
  <code>variable::set_particle_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить количество частиц\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает количество частиц и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_particle_amount(particle("fire"),1);

#Или от объекта

a1 = particle("fire").set_particle_amount(1);

#Или в сухую

variable::set_particle_amount(a1,particle("fire"),1);
```

<h3 id=set_variable_set_particle_color>
  <code>variable::set_particle_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает цвет частицы и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_particle_color(particle("fire"),"hex_color","COLOR");

#Или от объекта

a1 = particle("fire").set_particle_color("hex_color","COLOR");

#Или в сухую

variable::set_particle_color(a1,particle("fire"),"hex_color","COLOR");
```

<h3 id=set_variable_set_particle_material>
  <code>variable::set_particle_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить материал частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает материал частицы и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_particle_material(particle("fire"),item("stick"));

#Или от объекта

a1 = particle("fire").set_particle_material(item("stick"));

#Или в сухую

variable::set_particle_material(a1,particle("fire"),item("stick"));
```

<h3 id=set_variable_set_particle_offset>
  <code>variable::set_particle_offset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить движение частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает движение частицы и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_particle_offset(particle("fire"),vector(0,0,0));

#Или от объекта

a1 = particle("fire").set_particle_offset(vector(0,0,0));

#Или в сухую

variable::set_particle_offset(a1,particle("fire"),vector(0,0,0));
```

<h3 id=set_variable_set_particle_size>
  <code>variable::set_particle_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить размер частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает размер частицы и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_particle_size(particle("fire"),1);

#Или от объекта

a1 = particle("fire").set_particle_size(1);

#Или в сухую

variable::set_particle_size(a1,particle("fire"),1);
```

<h3 id=set_variable_set_particle_spread>
  <code>variable::set_particle_spread</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить разброс частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение разброса частицы.

**Пример использования:** 
```ts
a1 = variable::set_particle_spread(particle("fire"),1,2);

#Или от объекта

a1 = particle("fire").set_particle_spread(1,2);

#Или в сухую

variable::set_particle_spread(a1,particle("fire"),1,2);
```

<h3 id=set_variable_set_particle_type>
  <code>variable::set_particle_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает тип частицы и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_particle_type(particle("fire"),"type");

#Или от объекта

a1 = particle("fire").set_particle_type("type");

#Или в сухую

variable::set_particle_type(a1,particle("fire"),"type");
```

<h3 id=set_variable_set_potion_effect_amplifier>
  <code>variable::set_potion_effect_amplifier</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить силу зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает силу зелью и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_potion_effect_amplifier(potion("slow_falling"),1);

#Или от объекта

a1 = potion("slow_falling").set_potion_effect_amplifier(1);

#Или в сухую

variable::set_potion_effect_amplifier(a1,potion("slow_falling"),1);
```

<h3 id=set_variable_set_potion_effect_duration>
  <code>variable::set_potion_effect_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить длительность зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает длительность зелью и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_potion_effect_duration(potion("slow_falling"),1);

#Или от объекта

a1 = potion("slow_falling").set_potion_effect_duration(1);

#Или в сухую

variable::set_potion_effect_duration(a1,potion("slow_falling"),1);
```

<h3 id=set_variable_set_potion_effect_type>
  <code>variable::set_potion_effect_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить эффект зелью\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает эффект зелью и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_potion_effect_type(potion("slow_falling"),"effect_type");

#Или от объекта

a1 = potion("slow_falling").set_potion_effect_type("effect_type");

#Или в сухую

variable::set_potion_effect_type(a1,potion("slow_falling"),"effect_type");
```

<h3 id=set_variable_set_sound_pitch>
  <code>variable::set_sound_pitch</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить высоту звука\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает высоту звука и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_sound_pitch(sound("entity.zombie.hurt"),1);

#Или от объекта

a1 = sound("entity.zombie.hurt").set_sound_pitch(1);

#Или в сухую

variable::set_sound_pitch(a1,sound("entity.zombie.hurt"),1);
```

<h3 id=set_variable_set_sound_source>
  <code>variable::set_sound_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить источник звука\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает источник звука и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_sound_source(sound("entity.zombie.hurt"),"AMBIENT");

#Или от объекта

a1 = sound("entity.zombie.hurt").set_sound_source("AMBIENT");

#Или в сухую

variable::set_sound_source(a1,sound("entity.zombie.hurt"),"AMBIENT");
```

<h3 id=set_variable_set_sound_type>
  <code>variable::set_sound_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип звука\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает тип звуку и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_sound_type(sound("entity.zombie.hurt"),"namespace","value");

#Или от объекта

a1 = sound("entity.zombie.hurt").set_sound_type("namespace","value");

#Или в сухую

variable::set_sound_type(a1,sound("entity.zombie.hurt"),"namespace","value");
```

<h3 id=set_variable_set_sound_variation>
  <code>variable::set_sound_variation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить вариацию звука\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает вариацию звука и присваивает результат к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Можно установить как текстовую вариацию, так и числовой сид.\
&nbsp;&nbsp;Случайный сид если не удалось установить.

**Пример использования:** 
```ts
a1 = variable::set_sound_variation(sound("entity.zombie.hurt"),"variation");

#Или от объекта

a1 = sound("entity.zombie.hurt").set_sound_variation("variation");

#Или в сухую

variable::set_sound_variation(a1,sound("entity.zombie.hurt"),"variation");
```

<h3 id=set_variable_set_sound_volume_action>
  <code>variable::set_sound_volume_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить громкость звука\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает громкость звука и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_sound_volume_action(sound("entity.zombie.hurt"),1);

#Или от объекта

a1 = sound("entity.zombie.hurt").set_sound_volume_action(1);

#Или в сухую

variable::set_sound_volume_action(a1,sound("entity.zombie.hurt"),1);
```

<h3 id=set_variable_set_template_code>
  <code>variable::set_template_code</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить код в шаблон\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает код в шаблон и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_template_code(item("stick"),"any value");

#Или от объекта

a1 = item("stick").set_template_code("any value");

#Или в сухую

variable::set_template_code(a1,item("stick"),"any value");
```

<h3 id=set_variable_set_texture_to_map>
  <code>variable::set_texture_to_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить изображение карте\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает изображение карте по указанной ссылке. При перезагрузке сервера изображения могут пропасть, по этому рекомендуется повторно устанавливать его тем же картам при запуске мира.

**Пример использования:** 
```ts
a1 = variable::set_texture_to_map(item("stick"),"url");

#Или от объекта

a1 = item("stick").set_texture_to_map("url");

#Или в сухую

variable::set_texture_to_map(a1,item("stick"),"url");
```

<h3 id=set_variable_set_vector_component>
  <code>variable::set_vector_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить координату вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает определённую координату вектора и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_vector_component(vector(0,0,0),1,"X");

#Или от объекта

a1 = vector(0,0,0).set_vector_component(1,"X");

#Или в сухую

variable::set_vector_component(a1,vector(0,0,0),1,"X");
```

<h3 id=set_variable_set_vector_length>
  <code>variable::set_vector_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить длину вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает длину вектора и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_vector_length(vector(0,0,0),1);

#Или от объекта

a1 = vector(0,0,0).set_vector_length(1);

#Или в сухую

variable::set_vector_length(a1,vector(0,0,0),1);
```

<h3 id=set_variable_shift_all_coordinates>
  <code>variable::shift_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сдвинуть все координаты местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Сдвигает все координаты местоположения на определённые значения.

**Пример использования:** 
```ts
a1 = variable::shift_all_coordinates(location(0,0,0,0,0),1,2,3,4,5);

#Или от объекта

a1 = location(0,0,0,0,0).shift_all_coordinates(1,2,3,4,5);

#Или в сухую

variable::shift_all_coordinates(a1,location(0,0,0,0,0),1,2,3,4,5);
```

<h3 id=set_variable_shift_coordinate>
  <code>variable::shift_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сдвинуть координату местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Сдвигает координату местоположения на определённое значение.

**Пример использования:** 
```ts
a1 = variable::shift_coordinate(location(0,0,0,0,0),1,"X");

#Или от объекта

a1 = location(0,0,0,0,0).shift_coordinate(1,"X");

#Или в сухую

variable::shift_coordinate(a1,location(0,0,0,0,0),1,"X");
```

<h3 id=set_variable_shift_location_in_direction>
  <code>variable::shift_location_in_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сдвинуть местоположение в направлении\
**Тип:** Действие, возращающее значение\
**Описание:** Сдвигает местоположение в определённом направлении на определённое значение.

**Пример использования:** 
```ts
a1 = variable::shift_location_in_direction(location(0,0,0,0,0),1,"FORWARD");

#Или от объекта

a1 = location(0,0,0,0,0).shift_location_in_direction(1,"FORWARD");

#Или в сухую

variable::shift_location_in_direction(a1,location(0,0,0,0,0),1,"FORWARD");
```

<h3 id=set_variable_shift_location_on_vector>
  <code>variable::shift_location_on_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сдвинуть местоположение по вектору\
**Тип:** Действие, возращающее значение\
**Описание:** Сдвигает указанное местоположение по вектору и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::shift_location_on_vector(location(0,0,0,0,0),vector(0,0,0),1);

#Или от объекта

a1 = location(0,0,0,0,0).shift_location_on_vector(vector(0,0,0),1);

#Или в сухую

variable::shift_location_on_vector(a1,location(0,0,0,0,0),vector(0,0,0),1);
```

<h3 id=set_variable_shift_location_towards_location>
  <code>variable::shift_location_towards_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сместить местоположение в сторону местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Смещает местоположение в сторону заданного местоположения на определенное расстояние и присваивает его в переменную.

**Пример использования:** 
```ts
a1 = variable::shift_location_towards_location(location(0,0,0,0,0),location(0,0,0,0,0),1);

#Или от объекта

a1 = location(0,0,0,0,0).shift_location_towards_location(location(0,0,0,0,0),1);

#Или в сухую

variable::shift_location_towards_location(a1,location(0,0,0,0,0),location(0,0,0,0,0),1);
```

<h3 id=set_variable_simplex_noise_3d>
  <code>variable::simplex_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Шум Симплекс\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение шума Симплекс в определённом местоположении. Возвращает число, со значением от -1 до 1.

**Пример использования:** 
```ts
a1 = variable::simplex_noise_3d(location(0,0,0,0,0),1,2,3,4,5,"ZERO_TO_ONE","TRUE");

#Или от объекта

a1 = location(0,0,0,0,0).simplex_noise_3d(1,2,3,4,5,"ZERO_TO_ONE","TRUE");

#Или в сухую

variable::simplex_noise_3d(a1,location(0,0,0,0,0),1,2,3,4,5,"ZERO_TO_ONE","TRUE");
```

<h3 id=set_variable_sine>
  <code>variable::sine</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Синус числа\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает синус от числа.

**Пример использования:** 
```ts
a1 = variable::sine(1,"SINE","DEGREES");

#Или от объекта

a1 = (1).sine("SINE","DEGREES");

#Или в сухую

variable::sine(a1,1,"SINE","DEGREES");
```

<h3 id=set_variable_sort_any_list>
  <code>variable::sort_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отсортировать список\
**Тип:** Действие, возращающее значение\
**Описание:** Сортирует элементы списка.
**Работает с:**\
&nbsp;&nbsp;Числами\
&nbsp;&nbsp;Текстом\
&nbsp;&nbsp;Списками

**Пример использования:** 
```ts
a1 = variable::sort_list(`list`,"ASCENDING");

#Или от объекта

a1 = `list`.sort_list("ASCENDING");

#Или в сухую

variable::sort_list(a1,`list`,"ASCENDING");
```

<h3 id=set_variable_sort_any_map>
  <code>variable::sort_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сортировать словарь\
**Тип:** Действие, возращающее значение\
**Описание:** Сортирует словарь по заданным параметрам и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::sort_map(`map`,"ASCENDING","KEYS");

#Или от объекта

a1 = `map`.sort_map("ASCENDING","KEYS");

#Или в сухую

variable::sort_map(a1,`map`,"ASCENDING","KEYS");
```

<h3 id=set_variable_split_text>
  <code>variable::split_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Разделить текст на элементы\
**Тип:** Действие, возращающее значение\
**Описание:** Разделяет текст на элементы списка по заданному символу и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::split_text("text","delimiter");

#Или от объекта

a1 = "text".split_text("delimiter");

#Или в сухую

variable::split_text(a1,"text","delimiter");
```

<h3 id=set_variable_strip_text>
  <code>variable::strip_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить пробелы\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет пробелы в тексте и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::strip_text("text","ALL");

#Или от объекта

a1 = "text".strip_text("ALL");

#Или в сухую

variable::strip_text(a1,"text","ALL");
```

<h3 id=set_variable_subtract>
  <code>variable::subtract</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Вычитание чисел (-)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной разницу чисел.

**Пример использования:** 
```ts
a1 = variable::subtract([1, 2]);

#Или в сухую

variable::subtract(a1,[1, 2]);
```

<h3 id=set_variable_subtract_vectors>
  <code>variable::subtract_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Разница векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение разницы векторов.

**Пример использования:** 
```ts
a1 = variable::subtract_vectors([vector(0,0,0), vector(0,0,0)]);

#Или в сухую

variable::subtract_vectors(a1,[vector(0,0,0), vector(0,0,0)]);
```

<h3 id=set_variable_tangent>
  <code>variable::tangent</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Тангенс числа\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает тангенс от числа.

**Пример использования:** 
```ts
a1 = variable::tangent(1,"TANGENT","DEGREES");

#Или от объекта

a1 = (1).tangent("TANGENT","DEGREES");

#Или в сухую

variable::tangent(a1,1,"TANGENT","DEGREES");
```

<h3 id=set_variable_text>
  <code>variable::set_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить текст в переменную\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет и присваивает к переменной одно или несколько значений текста.

**Пример использования:** 
```ts
a1 = variable::set_text(["text", "text"],"SPACES");

#Или в сухую

variable::set_text(a1,["text", "text"],"SPACES");
```

<h3 id=set_variable_text_case>
  <code>variable::set_text_case</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить регистр текста\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает регистр текста и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_text_case("text","UPPER");

#Или от объекта

a1 = "text".set_text_case("UPPER");

#Или в сухую

variable::set_text_case(a1,"text","UPPER");
```

<h3 id=set_variable_to_char>
  <code>variable::to_char</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить символ по числу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённый символ по числу и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::to_char(1);

#Или от объекта

a1 = (1).to_char();

#Или в сухую

variable::to_char(a1,1);
```

<h3 id=set_variable_to_hsb>
  <code>variable::to_hsb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать HSB цвет\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт HEX цвет на основе оттенка, насыщенности и яркости.

**Пример использования:** 
```ts
a1 = variable::to_hsb(1,2,3);

#Или в сухую

variable::to_hsb(a1,1,2,3);
```

<h3 id=set_variable_to_hsl>
  <code>variable::to_hsl</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать HSL цвет\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт HEX цвет на основе оттенка, насыщенности и светлоты.

**Пример использования:** 
```ts
a1 = variable::to_hsl(1,2,3);

#Или в сухую

variable::to_hsl(a1,1,2,3);
```

<h3 id=set_variable_to_json>
  <code>variable::to_json</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать в JSON\
**Тип:** Действие, возращающее значение\
**Описание:** Преобразует словари и списки в JSON текст.

**Пример использования:** 
```ts
a1 = variable::to_json("any value","TRUE");

#Или в сухую

variable::to_json(a1,"any value","TRUE");
```

<h3 id=set_variable_to_rgb>
  <code>variable::to_rgb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать RGB цвет\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт HEX цвет в зависимости от красного, зелёного и синего каналов.

**Пример использования:** 
```ts
a1 = variable::to_rgb(1,2,3);

#Или в сухую

variable::to_rgb(a1,1,2,3);
```

<h3 id=set_variable_trim_list>
  <code>variable::trim_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Обрезать список\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает список, содержащий элементы указанного списка, которые находятся начиная и заканчивая на указанных индексах.

**Пример использования:** 
```ts
a1 = variable::trim_list(`list`,1,2);

#Или от объекта

a1 = `list`.trim_list(1,2);

#Или в сухую

variable::trim_list(a1,`list`,1,2);
```

<h3 id=set_variable_trim_text>
  <code>variable::trim_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Обрезать текст\
**Тип:** Действие, возращающее значение\
**Описание:** Обрезает текст и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::trim_text("text",1,2);

#Или от объекта

a1 = "text".trim_text(1,2);

#Или в сухую

variable::trim_text(a1,"text",1,2);
```

<h3 id=set_variable_vector>
  <code>variable::set_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать вектор\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт вектор из указанных координат и присваивает результат к переменной.

**Пример использования:** 
```ts
a1 = variable::set_vector(1,2,3);

#Или в сухую

variable::set_vector(a1,1,2,3);
```

<h3 id=set_variable_vector_to_direction_name>
  <code>variable::vector_to_direction_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить сторону света вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает в переменную сторону света, в которую направлен вектор.

**Пример использования:** 
```ts
a1 = variable::vector_to_direction_name(vector(0,0,0));

#Или от объекта

a1 = vector(0,0,0).vector_to_direction_name();

#Или в сухую

variable::vector_to_direction_name(a1,vector(0,0,0));
```

<h3 id=set_variable_voronoi_noise_3d>
  <code>variable::voronoi_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Шум Вороного\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение шума Вороного в определённом местоположении. Возвращает число, со значением от 0 до 1.

**Пример использования:** 
```ts
a1 = variable::voronoi_noise_3d(location(0,0,0,0,0),1,2,3,"ZERO_TO_ONE","TRUE");

#Или от объекта

a1 = location(0,0,0,0,0).voronoi_noise_3d(1,2,3,"ZERO_TO_ONE","TRUE");

#Или в сухую

variable::voronoi_noise_3d(a1,location(0,0,0,0,0),1,2,3,"ZERO_TO_ONE","TRUE");
```

<h3 id=set_variable_warp>
  <code>variable::warp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Обернуть число\
**Тип:** Действие, возращающее значение\
**Описание:** Проверяет, находится ли число между двумя границами, и если нет, оборачивает его вокруг этой границы.

**Пример использования:** 
```ts
a1 = variable::warp(1,2,3);

#Или от объекта

a1 = (1).warp(2,3);

#Или в сухую

variable::warp(a1,1,2,3);
```
