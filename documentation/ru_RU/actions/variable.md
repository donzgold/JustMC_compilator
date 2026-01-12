<h2 id=variable>
  <code>variable</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

<h3 id=if_variable_block_is_minecraft_tagged>
  <code>variable::block_is_minecraft_tagged</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Блок имеет Minecraft-тег\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли блок указанный Minecraft-тег (например, "mineable/shovel").\
**Дополнительная информация:**\
&nbsp;&nbsp;Minecraft-тег должен начинаться с "#minecraft:"

**Пример использования:**
```ts
if(variable::block_is_minecraft_tagged("minecraft:oak_log[axis=x]", "namespace")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::block_is_minecraft_tagged(block="minecraft:oak_log[axis=x]", namespace="namespace")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID        | Тип   | Описание          |
|-----------|-------|-------------------|
| block     | Блок  | Блок для проверки |
| namespace | Текст | Minecraft-тег     |

<h3 id=if_variable_block_is_solid>
  <code>variable::block_is_solid</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Блок является полным\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, является ли указанный блок полным.

**Пример использования:**
```ts
if(variable::block_is_solid("minecraft:oak_log[axis=x]")){
    player::message("Условие верно");
}

//Или от объекта

if("minecraft:oak_log[axis=x]".block_is_solid()){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::block_is_solid(block="minecraft:oak_log[axis=x]")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID    | Тип  | Описание          |
|-------|------|-------------------|
| block | Блок | Блок для проверки |

<h3 id=if_variable_dummy>
  <code>variable::is_dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** ...\
**Тип:** Действие, проверяющее условие\
**Описание:** ...

**Пример использования:**
```ts
if(variable::is_dummy()){
    player::message("Условие верно");
}
```

<h3 id=if_variable_equals>
  <code>variable::equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равна ли переменная хотя бы одному из сравниваемых значений.

**Пример использования:**
```ts
if(variable::equals("any value", ["any value", "any value"])){
    player::message("Условие верно");
}

//Или от объекта

if("any value".equals(["any value", "any value"])){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::equals(value="any value", compare=["any value", "any value"])){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID      | Тип                                                            | Описание                 |
|---------|----------------------------------------------------------------|--------------------------|
| value   | Любое значение                                                 | Переменная для сравнения |
| compare | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Сравниваемые значения    |

<h3 id=if_variable_exists>
  <code>variable::exists</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Переменная существует\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, существует ли выбранная переменная.

**Пример использования:**
```ts
if(variable::exists(`variable`)){
    player::message("Условие верно");
}

//Или от объекта

if(`variable`.exists()){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::exists(variable=`variable`)){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID       | Тип        | Описание                |
|----------|------------|-------------------------|
| variable | Переменная | Переменная для проверки |

<h3 id=if_variable_greater>
  <code>variable::greater</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Больше\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, больше ли числовая переменная указанного значения.

**Пример использования:**
```ts
if(variable::greater(1, 2)){
    player::message("Условие верно");
}

//Или от объекта

if((1).greater(2)){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::greater(value=1, compare=2)){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID      | Тип   | Описание                |
|---------|-------|-------------------------|
| value   | Число | Сравниваемая переменная |
| compare | Число | Сравниваемое значение   |

<h3 id=if_variable_greater_or_equals>
  <code>variable::greater_or_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Больше или равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, больше или равна ли числовая переменная указанного значения.

**Пример использования:**
```ts
if(variable::greater_or_equals(1, 2)){
    player::message("Условие верно");
}

//Или от объекта

if((1).greater_or_equals(2)){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::greater_or_equals(value=1, compare=2)){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID      | Тип   | Описание                |
|---------|-------|-------------------------|
| value   | Число | Сравниваемая переменная |
| compare | Число | Сравниваемое значение   |

<h3 id=if_variable_in_range>
  <code>variable::in_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** В диапазоне\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли переменная в указанном диапазоне.\
**Работает с:**\
&nbsp;&nbsp;Числами\
&nbsp;&nbsp;Местоположениями

**Пример использования:**
```ts
if(variable::in_range("any value", "any value", "any value")){
    player::message("Условие верно");
}

//Или от объекта

if("any value".in_range("any value", "any value")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::in_range(value="any value", min="any value", max="any value")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID    | Тип            | Описание                |
|-------|----------------|-------------------------|
| value | Любое значение | Сравниваемая переменная |
| min   | Любое значение | Минимальное значение    |
| max   | Любое значение | Максимальное значение   |

<h3 id=if_variable_is_type>
  <code>variable::is_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Тип переменной равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли тип значения переменной указанному.

**Пример использования:**
```ts
if(variable::is_type("any value", "ARRAY")){
    player::message("Условие верно");
}

//Или от объекта

if("any value".is_type("ARRAY")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::is_type(value="any value", variable_type="ARRAY")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID            | Тип                                                                                                                                                                                                                                                     | Описание                |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| value         | Любое значение                                                                                                                                                                                                                                          | Переменная для проверки |
| variable_type | Маркер<br/>**ARRAY** - Список<br/>**ITEM** - Предмет<br/>**LOCATION** - Местоположение<br/>**MAP** - Словарь<br/>**NUMBER** - Число<br/>**PARTICLE** - Частица<br/>**POTION** - Зелье<br/>**SOUND** - Звук<br/>**TEXT** - Текст<br/>**VECTOR** - Вектор | Тип переменной          |

<h3 id=if_variable_item_equals>
  <code>variable::item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равна ли предметная переменная хотя бы одной из указанных.

**Пример использования:**
```ts
if(variable::item_equals(item("stick"), [item("stick"), item("stick")], "EXACTLY")){
    player::message("Условие верно");
}

//Или от объекта

if(item("stick").item_equals([item("stick"), item("stick")], "EXACTLY")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::item_equals(value=item("stick"), compare=[item("stick"), item("stick")], comparison_mode="EXACTLY")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID              | Тип                                                                                                                                                                                                                  | Описание                         |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| value           | Предмет                                                                                                                                                                                                              | Сравниваемая переменная предмета |
| compare         | Message 'actions.array' not found in 'ru_RU'\[Предмет\]                                                                                                                                                              | Сравниваемые значения            |
| comparison_mode | Маркер<br/>**EXACTLY** - Полное сравнение<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Игнорировать количество и прочность<br/>**IGNORE_STACK_SIZE** - Игнорировать количество<br/>**TYPE_ONLY** - Только тип предмета | Режим сравнения                  |

<h3 id=if_variable_item_has_enchantment>
  <code>variable::item_has_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет имеет зачарование\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли предметная переменная указанное зачарование определённого уровня.

**Пример использования:**
```ts
if(variable::item_has_enchantment(item("stick"), "enchant", 1)){
    player::message("Условие верно");
}

//Или от объекта

if(item("stick").item_has_enchantment("enchant", 1)){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::item_has_enchantment(item=item("stick"), enchant="enchant", level=1)){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID      | Тип     | Описание              |
|---------|---------|-----------------------|
| item    | Предмет | Предметная переменная |
| enchant | Текст   | Ключ зачарования      |
| level   | Число   | Уровень               |

<h3 id=if_variable_item_has_tag>
  <code>variable::item_has_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет имеет тег\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли предметная переменная указанный тег с выбранным значением.

**Пример использования:**
```ts
if(variable::item_has_tag(item("stick"), "tag", ["value", "value"], "CONTAINS")){
    player::message("Условие верно");
}

//Или от объекта

if(item("stick").item_has_tag("tag", ["value", "value"], "CONTAINS")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::item_has_tag(item=item("stick"), tag="tag", value=["value", "value"], compare_type="CONTAINS")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID           | Тип                                                                                                                                              | Описание              |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| item         | Предмет                                                                                                                                          | Предметная переменная |
| tag          | Текст                                                                                                                                            | Имя тега              |
| value        | Message 'actions.array' not found in 'ru_RU'\[Текст\]                                                                                            | Значение тега         |
| compare_type | Маркер<br/>**CONTAINS** - Содержит<br/>**ENDS_WITH** - Заканчивается на<br/>**EQUALS** - Точное соответствие<br/>**STARTS_WITH** - Начинается на | Тип сравнения         |

<h3 id=if_variable_item_is_block>
  <code>variable::item_is_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет является блоком\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, является ли указанный предмет блоком.

**Пример использования:**
```ts
if(variable::item_is_block(item("stick"))){
    player::message("Условие верно");
}

//Или от объекта

if(item("stick").item_is_block()){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::item_is_block(item=item("stick"))){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID   | Тип     | Описание             |
|------|---------|----------------------|
| item | Предмет | Предмет для проверки |

<h3 id=if_variable_item_is_minecraft_tagged>
  <code>variable::item_is_minecraft_tagged</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет имеет Minecraft-тег\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли предмет указанный Minecraft-тег (например, "swords").\
**Дополнительная информация:**\
&nbsp;&nbsp;Minecraft-тег должен начинаться с "#minecraft:"

**Пример использования:**
```ts
if(variable::item_is_minecraft_tagged(item("stick"), "namespace")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::item_is_minecraft_tagged(item=item("stick"), namespace="namespace")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID        | Тип     | Описание             |
|-----------|---------|----------------------|
| item      | Предмет | Предмет для проверки |
| namespace | Текст   | Minecraft-тег        |

<h3 id=if_variable_less>
  <code>variable::less</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Меньше\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, меньше ли числовая переменная указанного значения.

**Пример использования:**
```ts
if(variable::less(1, 2)){
    player::message("Условие верно");
}

//Или от объекта

if((1).less(2)){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::less(value=1, compare=2)){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID      | Тип   | Описание                |
|---------|-------|-------------------------|
| value   | Число | Сравниваемая переменная |
| compare | Число | Сравниваемое значение   |

<h3 id=if_variable_less_or_equals>
  <code>variable::less_or_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Меньше или равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, меньше или равна ли числовая переменная указанного значения.

**Пример использования:**
```ts
if(variable::less_or_equals(1, 2)){
    player::message("Условие верно");
}

//Или от объекта

if((1).less_or_equals(2)){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::less_or_equals(value=1, compare=2)){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID      | Тип   | Описание                |
|---------|-------|-------------------------|
| value   | Число | Сравниваемая переменная |
| compare | Число | Сравниваемое значение   |

<h3 id=if_variable_list_contains_value>
  <code>variable::list_contains_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Список содержит значение\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, содержит ли список определённое значение.

**Пример использования:**
```ts
if(variable::list_contains_value([`list`, `list`], ["any value", "any value"], "ALL")){
    player::message("Условие верно");
}

//Или от объекта

if([`list`, `list`].list_contains_value(["any value", "any value"], "ALL")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::list_contains_value(list=[`list`, `list`], values=["any value", "any value"], check_mode="ALL")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID         | Тип                                                            | Описание              |
|------------|----------------------------------------------------------------|-----------------------|
| list       | Список                                                         | Список для проверки   |
| values     | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Значения для проверки |
| check_mode | Маркер<br/>**ALL** - Все значения<br/>**ANY** - Любое значение | Режим проверки        |

<h3 id=if_variable_list_is_empty>
  <code>variable::list_is_empty</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Значение пустое\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли размер значения нулю.\
**Работает с:**\
&nbsp;&nbsp;Текстом\
&nbsp;&nbsp;Списками\
&nbsp;&nbsp;Словарями\
&nbsp;&nbsp;Предметами\
&nbsp;&nbsp;Несуществующими переменными\
&nbsp;&nbsp;Пустыми значениями

**Пример использования:**
```ts
if(variable::list_is_empty("any value")){
    player::message("Условие верно");
}

//Или от объекта

if("any value".list_is_empty()){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::list_is_empty(list="any value")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID   | Тип            | Описание              |
|------|----------------|-----------------------|
| list | Любое значение | Значение для проверки |

<h3 id=if_variable_list_value_equals>
  <code>variable::list_value_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Значение элемента списка равно\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равно ли значение элемента списка хотя бы одному сравниваемому значению.

**Пример использования:**
```ts
if(variable::list_value_equals([`list`, `list`], 1, ["any value", "any value"])){
    player::message("Условие верно");
}

//Или от объекта

if([`list`, `list`].list_value_equals(1, ["any value", "any value"])){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::list_value_equals(list=[`list`, `list`], index=1, values=["any value", "any value"])){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID     | Тип                                                            | Описание              |
|--------|----------------------------------------------------------------|-----------------------|
| list   | Список                                                         | Список для проверки   |
| index  | Число                                                          | Индекс значения       |
| values | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Сравниваемые значения |

<h3 id=if_variable_location_in_range>
  <code>variable::location_in_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Местоположение в диапазоне\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли местоположение в указанном диапазоне.

**Пример использования:**
```ts
if(variable::location_in_range(location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "BLOCK")){
    player::message("Условие верно");
}

//Или от объекта

if(location(0,0,0,0,0).location_in_range(location(0,0,0,0,0), location(0,0,0,0,0), "BLOCK")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::location_in_range(value=location(0,0,0,0,0), min=location(0,0,0,0,0), max=location(0,0,0,0,0), border_handling="BLOCK")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID              | Тип                                                                                                                                                      | Описание                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| value           | Местоположение                                                                                                                                           | Местоположение для проверки |
| min             | Местоположение                                                                                                                                           | Первый угол региона         |
| max             | Местоположение                                                                                                                                           | Второй угол региона         |
| border_handling | Маркер<br/>**BLOCK** - Округление до координат блока<br/>**EXACT** - Точные координаты<br/>**FULL_BLOCK_RANGE** - Округление до мин. и макс. угла блоков | Режим проверки              |

<h3 id=if_variable_location_is_near>
  <code>variable::location_is_near</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Рядом с местоположением\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли переменная местоположения рядом с указанным местоположением.

**Пример использования:**
```ts
if(variable::location_is_near(location(0,0,0,0,0), 1, [location(0,0,0,0,0), location(0,0,0,0,0)], "CIRCLE")){
    player::message("Условие верно");
}

//Или от объекта

if(location(0,0,0,0,0).location_is_near(1, [location(0,0,0,0,0), location(0,0,0,0,0)], "CIRCLE")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::location_is_near(location=location(0,0,0,0,0), radius=1, check=[location(0,0,0,0,0), location(0,0,0,0,0)], shape="CIRCLE")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID       | Тип                                                                                             | Описание                     |
|----------|-------------------------------------------------------------------------------------------------|------------------------------|
| location | Местоположение                                                                                  | Местоположение для проверки  |
| radius   | Число                                                                                           | Радиус проверки              |
| check    | Message 'actions.array' not found in 'ru_RU'\[Местоположение\]                                  | Местоположение центра фигуры |
| shape    | Маркер<br/>**CIRCLE** - Круг<br/>**CUBE** - Куб<br/>**SPHERE** - Сфера<br/>**SQUARE** - Квадрат | Фигура                       |

<h3 id=if_variable_map_has_key>
  <code>variable::map_has_key</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Словарь имеет ключ\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли словарь определённый ключ.

**Пример использования:**
```ts
if(variable::map_has_key({"map":`map`}, ["any value", "any value"], "ALL")){
    player::message("Условие верно");
}

//Или от объекта

if({"map":`map`}.map_has_key(["any value", "any value"], "ALL")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::map_has_key(map={"map":`map`}, key=["any value", "any value"], check_mode="ALL")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID         | Тип                                                                              | Описание             |
|------------|----------------------------------------------------------------------------------|----------------------|
| map        | Словарь                                                                          | Словарь для проверки |
| key        | Message 'actions.array' not found in 'ru_RU'\[Любое значение\]                   | Ключ                 |
| check_mode | Маркер<br/>**ALL** - Все указанные ключи<br/>**ANY** - Любой из указанных ключей | Тип проверки         |

<h3 id=if_variable_map_value_equals>
  <code>variable::map_value_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Значение элемента словаря равно\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равно ли значение элемента словаря по ключу хотя бы одному сравниваемому значению.

**Пример использования:**
```ts
if(variable::map_value_equals({"map":`map`}, "any value", ["any value", "any value"])){
    player::message("Условие верно");
}

//Или от объекта

if({"map":`map`}.map_value_equals("any value", ["any value", "any value"])){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::map_value_equals(map={"map":`map`}, key="any value", values=["any value", "any value"])){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID     | Тип                                                            | Описание              |
|--------|----------------------------------------------------------------|-----------------------|
| map    | Словарь                                                        | Словарь для проверки  |
| key    | Любое значение                                                 | Ключ                  |
| values | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Сравниваемые значения |

<h3 id=if_variable_not_equals>
  <code>variable::not_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Не равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, не равна ли переменная всем сравниваемым значениям.

**Пример использования:**
```ts
if(variable::not_equals("any value", ["any value", "any value"])){
    player::message("Условие верно");
}

//Или от объекта

if("any value".not_equals(["any value", "any value"])){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::not_equals(value="any value", compare=["any value", "any value"])){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID      | Тип                                                            | Описание                |
|---------|----------------------------------------------------------------|-------------------------|
| value   | Любое значение                                                 | Сравниваемая переменная |
| compare | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Сравниваемые значения   |

<h3 id=if_variable_number_in_range>
  <code>variable::number_in_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** В диапазоне\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, в указанном диапазоне ли числовая переменная указанного значения.

**Пример использования:**
```ts
if(variable::number_in_range(1, 2, 3, "NOT_INCLUDE")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::number_in_range(value=1, min=2, max=3, including="NOT_INCLUDE")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID        | Тип                                                                                                                                                                            | Описание             |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| value     | Число                                                                                                                                                                          | Значение             |
| min       | Число                                                                                                                                                                          | От                   |
| max       | Число                                                                                                                                                                          | До                   |
| including | Маркер<br/>**NOT_INCLUDE** - Не учитывать "от" и "до"<br/>**INCLUDE_FIRST** - Учитывать "от"<br/>**INCLUDE_LAST** - Учитывать "до"<br/>**INCLUDE_ALL** - Учитывать "от" и "до" | Тип границ диапазона |

<h3 id=if_variable_range_intersects_range>
  <code>variable::range_intersects_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Регион пересекается с регионом\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, пересекается ли один регион с другим.

**Пример использования:**
```ts
if(variable::range_intersects_range(location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "CONTAINS")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::range_intersects_range(min1=location(0,0,0,0,0), max1=location(0,0,0,0,0), min2=location(0,0,0,0,0), max2=location(0,0,0,0,0), check_type="CONTAINS")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID         | Тип                                                                | Описание                    |
|------------|--------------------------------------------------------------------|-----------------------------|
| min1       | Местоположение                                                     | Первый угол первого региона |
| max1       | Местоположение                                                     | Второй угол первого региона |
| min2       | Местоположение                                                     | Первый угол второго региона |
| max2       | Местоположение                                                     | Второй угол второго региона |
| check_type | Маркер<br/>**CONTAINS** - Содержит<br/>**OVERLAPS** - Пересекается | Тип проверки                |

<h3 id=if_variable_text_contains>
  <code>variable::text_contains</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Текст содержит\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, содержит ли текстовая переменная указанный текст.

**Пример использования:**
```ts
if(variable::text_contains("value", ["compare", "compare"], "FALSE")){
    player::message("Условие верно");
}

//Или от объекта

if("value".text_contains(["compare", "compare"], "FALSE")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::text_contains(value="value", compare=["compare", "compare"], ignore_case="FALSE")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID          | Тип                                                   | Описание                |
|-------------|-------------------------------------------------------|-------------------------|
| value       | Текст                                                 | Переменная для проверки |
| compare     | Message 'actions.array' not found in 'ru_RU'\[Текст\] | Текст для проверки      |
| ignore_case | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да          | Игнорировать регистр    |

<h3 id=if_variable_text_ends_with>
  <code>variable::text_ends_with</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Текст заканчивается на\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, заканчивается ли текстовая переменная на указанный текст.

**Пример использования:**
```ts
if(variable::text_ends_with("value", ["compare", "compare"], "FALSE")){
    player::message("Условие верно");
}

//Или от объекта

if("value".text_ends_with(["compare", "compare"], "FALSE")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::text_ends_with(value="value", compare=["compare", "compare"], ignore_case="FALSE")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID          | Тип                                                   | Описание                          |
|-------------|-------------------------------------------------------|-----------------------------------|
| value       | Текст                                                 | Текстовая переменная для проверки |
| compare     | Message 'actions.array' not found in 'ru_RU'\[Текст\] | Текст для сравнения               |
| ignore_case | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да          | Игнорировать регистр              |

<h3 id=if_variable_text_matches>
  <code>variable::text_matches</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Текст совпадает\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, совпадает ли текстовая переменная с указанным текстом или регулярным выражением (RegEx).

**Пример использования:**
```ts
if(variable::text_matches("match", ["values", "values"], "FALSE", "FALSE")){
    player::message("Условие верно");
}

//Или от объекта

if("match".text_matches(["values", "values"], "FALSE", "FALSE")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::text_matches(match="match", values=["values", "values"], regular_expressions="FALSE", ignore_case="FALSE")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID                  | Тип                                                              | Описание                          |
|---------------------|------------------------------------------------------------------|-----------------------------------|
| match               | Текст                                                            | Текст или регулярное выражение    |
| values              | Message 'actions.array' not found in 'ru_RU'\[Текст\]            | Текстовые переменные для проверки |
| regular_expressions | Маркер<br/>**FALSE** - Текст<br/>**TRUE** - Регулярное выражение | Способ проверки                   |
| ignore_case         | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да                     | Игнорировать регистр              |

<h3 id=if_variable_text_starts_with>
  <code>variable::text_starts_with</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Текст начинается с\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, начинается ли текстовая переменная с указанного текста.

**Пример использования:**
```ts
if(variable::text_starts_with("value", ["compare", "compare"], "FALSE")){
    player::message("Условие верно");
}

//Или от объекта

if("value".text_starts_with(["compare", "compare"], "FALSE")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(variable::text_starts_with(value="value", compare=["compare", "compare"], ignore_case="FALSE")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID          | Тип                                                   | Описание                          |
|-------------|-------------------------------------------------------|-----------------------------------|
| value       | Текст                                                 | Текстовая переменная для проверки |
| compare     | Message 'actions.array' not found in 'ru_RU'\[Текст\] | Текст для сравнения               |
| ignore_case | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да          | Игнорировать регистр              |

<h3 id=set_variable_absolute>
  <code>variable::absolute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Модуль числа\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение модуля выбранного числа.

**Пример использования:**
```ts
`variable` = variable::absolute(1);

//Или от объекта

`variable` = (1).absolute();

//Или в сухую позиционно

variable::absolute(`variable`, 1);

//Или в сухую по ключам

variable::absolute(variable=`variable`, number=1);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| number   | Число               | Число в модуле            |

<h3 id=set_variable_add>
  <code>variable::add</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сложение чисел (+)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной сумму чисел.

**Пример использования:**
```ts
`variable` = variable::add([1, 2]);

//Или в сухую позиционно

variable::add(`variable`, [1, 2]);

//Или в сухую по ключам

variable::add(variable=`variable`, value=[1, 2]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                   | Переменная для присвоения |
| value    | Message 'actions.array' not found in 'ru_RU'\[Число\] | Числа для суммирования    |

<h3 id=set_variable_add_item_enchantment>
  <code>variable::add_item_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить зачарование предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Добавляет зачарование предмету и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::add_item_enchantment(item("stick"), "enchantment", 1);

//Или от объекта

`variable` = item("stick").add_item_enchantment("enchantment", 1);

//Или в сухую позиционно

variable::add_item_enchantment(`variable`, item("stick"), "enchantment", 1);

//Или в сухую по ключам

variable::add_item_enchantment(variable=`variable`, item=item("stick"), enchantment="enchantment", level=1);
```

**Аргументы:**

| ID          | Тип                   | Описание                  |
|-------------|-----------------------|---------------------------|
| variable    | Переменная\[Предмет\] | Переменная для присвоения |
| item        | Предмет               | Предмет                   |
| enchantment | Текст                 | ID зачарования            |
| level       | Число                 | Уровень зачарования       |

<h3 id=set_variable_add_item_potion_effects>
  <code>variable::add_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить эффекты зелий предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает эффекты зелий предмету и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::add_item_potion_effects([potion("slow_falling"), potion("slow_falling")], item("stick"), "FALSE", "FALSE", "AMBIENT");

//Или от объекта

`variable` = item("stick").add_item_potion_effects([potion("slow_falling"), potion("slow_falling")], "FALSE", "FALSE", "AMBIENT");

//Или в сухую позиционно

variable::add_item_potion_effects(`variable`, [potion("slow_falling"), potion("slow_falling")], item("stick"), "FALSE", "FALSE", "AMBIENT");

//Или в сухую по ключам

variable::add_item_potion_effects(variable=`variable`, potions=[potion("slow_falling"), potion("slow_falling")], item=item("stick"), overwrite="FALSE", show_icon="FALSE", particle_mode="AMBIENT");
```

**Аргументы:**

| ID            | Тип                                                                          | Описание                            |
|---------------|------------------------------------------------------------------------------|-------------------------------------|
| variable      | Переменная\[Предмет\]                                                        | Переменная для присвоения           |
| potions       | Message 'actions.array' not found in 'ru_RU'\[Зелье\]                        | Эффекты зелий                       |
| item          | Предмет                                                                      | Предмет                             |
| overwrite     | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да                                 | Перезаписывать существующие эффекты |
| show_icon     | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да                                 | Показывать иконку эффекта           |
| particle_mode | Маркер<br/>**AMBIENT** - Прозрачными<br/>**NONE** - Нет<br/>**REGULAR** - Да | Показывать частицы                  |

<h3 id=set_variable_add_vectors>
  <code>variable::add_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сумма векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение суммы векторов.

**Пример использования:**
```ts
`variable` = variable::add_vectors([vector(0,0,0), vector(0,0,0)]);

//Или в сухую позиционно

variable::add_vectors(`variable`, [vector(0,0,0), vector(0,0,0)]);

//Или в сухую по ключам

variable::add_vectors(variable=`variable`, vectors=[vector(0,0,0), vector(0,0,0)]);
```

**Аргументы:**

| ID       | Тип                                                    | Описание                  |
|----------|--------------------------------------------------------|---------------------------|
| variable | Переменная\[Вектор\]                                   | Переменная для присвоения |
| vectors  | Message 'actions.array' not found in 'ru_RU'\[Вектор\] | Вектора для суммирования  |

<h3 id=set_variable_align_location>
  <code>variable::align_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Округлить местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Округляет местоположение к центру или углу блока и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::align_location(location(0,0,0,0,0), "KEEP", "ALL", "BLOCK_CENTER");

//Или от объекта

`variable` = location(0,0,0,0,0).align_location("KEEP", "ALL", "BLOCK_CENTER");

//Или в сухую позиционно

variable::align_location(`variable`, location(0,0,0,0,0), "KEEP", "ALL", "BLOCK_CENTER");

//Или в сухую по ключам

variable::align_location(variable=`variable`, location=location(0,0,0,0,0), rotation_mode="KEEP", coordinates_mode="ALL", align_mode="BLOCK_CENTER");
```

**Аргументы:**

| ID               | Тип                                                                                         | Описание                  |
|------------------|---------------------------------------------------------------------------------------------|---------------------------|
| variable         | Переменная\[Местоположение\]                                                                | Переменная для присвоения |
| location         | Местоположение                                                                              | Местоположение            |
| rotation_mode    | Маркер<br/>**KEEP** - Включить<br/>**REMOVE** - Выключить                                   | Сохранение поворота       |
| coordinates_mode | Маркер<br/>**ALL** - Все координаты<br/>**X_Z** - Координаты X и Z<br/>**Y** - Координата Y | Тип координаты            |
| align_mode       | Маркер<br/>**BLOCK_CENTER** - К центру блока<br/>**CORNER** - К углу блока                  | Режим округления          |

<h3 id=set_variable_align_to_axis_vector>
  <code>variable::align_to_axis_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выровнять вектор\
**Тип:** Действие, возращающее значение\
**Описание:** Выравнивает вектор к ближайшей оси и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::align_to_axis_vector(vector(0,0,0), "FALSE");

//Или от объекта

`variable` = vector(0,0,0).align_to_axis_vector("FALSE");

//Или в сухую позиционно

variable::align_to_axis_vector(`variable`, vector(0,0,0), "FALSE");

//Или в сухую по ключам

variable::align_to_axis_vector(variable=`variable`, vector=vector(0,0,0), normalize="FALSE");
```

**Аргументы:**

| ID        | Тип                                                                  | Описание                  |
|-----------|----------------------------------------------------------------------|---------------------------|
| variable  | Переменная\[Вектор\]                                                 | Переменная для присвоения |
| vector    | Вектор                                                               | Вектор для выравнивания   |
| normalize | Маркер<br/>**FALSE** - Исходной длины<br/>**TRUE** - Нормализованный | Тип выдаваемого вектора   |

<h3 id=set_variable_append_component>
  <code>variable::append_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Объединить стилизуемые тексты\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет указанные стилизуемые тексты в единый стилизуемый текст и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::append_component(["components", "components"], "CONCATENATION");

//Или в сухую позиционно

variable::append_component(`variable`, ["components", "components"], "CONCATENATION");

//Или в сухую по ключам

variable::append_component(variable=`variable`, components=["components", "components"], merging="CONCATENATION");
```

**Аргументы:**

| ID         | Тип                                                                                                                           | Описание                           |
|------------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| variable   | Переменная\[Текст\]                                                                                                           | Переменная для присвоения          |
| components | Message 'actions.array' not found in 'ru_RU'\[Текст\]                                                                         | Стилизуемые тексты для объединения |
| merging    | Маркер<br/>**CONCATENATION** - Объединение<br/>**SEPARATE_LINES** - Разделение на строки<br/>**SPACES** - Разделение пробелом | Объединение текста                 |

<h3 id=set_variable_append_list>
  <code>variable::append_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Объединить два списка\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет два указанных списка в один.

**Пример использования:**
```ts
`variable` = variable::append_list([`list_1`, `list_1`], [`list_2`, `list_2`]);

//Или от объекта

`variable` = [`list_1`, `list_1`].append_list([`list_2`, `list_2`]);

//Или в сухую позиционно

variable::append_list(`variable`, [`list_1`, `list_1`], [`list_2`, `list_2`]);

//Или в сухую по ключам

variable::append_list(variable=`variable`, list_1=[`list_1`, `list_1`], list_2=[`list_2`, `list_2`]);
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| list_1   | Список               | Первый список             |
| list_2   | Список               | Второй список             |

<h3 id=set_variable_append_map>
  <code>variable::append_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Объединить словари\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет два словаря и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::append_map({"map":`map`}, {"other_map":`other_map`});

//Или от объекта

`variable` = {"map":`map`}.append_map({"other_map":`other_map`});

//Или в сухую позиционно

variable::append_map(`variable`, {"map":`map`}, {"other_map":`other_map`});

//Или в сухую по ключам

variable::append_map(variable=`variable`, map={"map":`map`}, other_map={"other_map":`other_map`});
```

**Аргументы:**

| ID        | Тип                   | Описание                  |
|-----------|-----------------------|---------------------------|
| variable  | Переменная\[Словарь\] | Переменная для присвоения |
| map       | Словарь               | Первый словарь            |
| other_map | Словарь               | Второй словарь            |

<h3 id=set_variable_append_value>
  <code>variable::append_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить значение\
**Тип:** Действие без значения\
**Описание:** Добавляет указанные значения в конец списка.

**Пример использования:**
```ts
variable::append_value(`variable`, ["any value", "any value"]);

//Или от объекта

`variable`.append_value(["any value", "any value"]);

//Или в сухую по ключам

variable::append_value(variable=`variable`, values=["any value", "any value"]);
```

**Аргументы:**

| ID       | Тип                                                            | Описание |
|----------|----------------------------------------------------------------|----------|
| variable | Переменная                                                     | Список   |
| values   | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Значения |

<h3 id=set_variable_atan2>
  <code>variable::atan2</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Арктангенс значений (atan2)\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает арктангенс от двух указанных чисел.

**Пример использования:**
```ts
`variable` = variable::atan2(1, 2);

//Или в сухую позиционно

variable::atan2(`variable`, 1, 2);

//Или в сухую по ключам

variable::atan2(variable=`variable`, y=1, x=2);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| y        | Число               | Первое число (y)          |
| x        | Число               | Второе число (x)          |

<h3 id=set_variable_average>
  <code>variable::average</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Среднее значение\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной среднее значение чисел.

**Пример использования:**
```ts
`variable` = variable::average([1, 2], "ARITHMETIC");

//Или в сухую позиционно

variable::average(`variable`, [1, 2], "ARITHMETIC");

//Или в сухую по ключам

variable::average(variable=`variable`, value=[1, 2], type="ARITHMETIC");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                               | Описание                     |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| variable | Переменная\[Число\]                                                                                                                                                               | Переменная для присвоения    |
| value    | Message 'actions.array' not found in 'ru_RU'\[Число\]                                                                                                                             | Числа для получения значения |
| type     | Маркер<br/>**ARITHMETIC** - Среднее арифметическое<br/>**GEOMETRIC** - Среднее геометрическое<br/>**HARMONIC** - Среднее гармоническое<br/>**QUADRATIC** - Среднее квадратическое | Тип значения                 |

<h3 id=set_variable_bitwise_operation>
  <code>variable::bitwise_operation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Побитовая операция над числами\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат побитовой операции над числами.

**Пример использования:**
```ts
`variable` = variable::bitwise_operation(1, 2, "AND");

//Или в сухую позиционно

variable::bitwise_operation(`variable`, 1, 2, "AND");

//Или в сухую по ключам

variable::bitwise_operation(variable=`variable`, operand1=1, operand2=2, operator="AND");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                                                                                                                                                                                                                                                  | Описание                  |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                                                                                                                                                                                                                                                                                                                                                                  | Переменная для присвоения |
| operand1 | Число                                                                                                                                                                                                                                                                                                                                                                                                | Первый операнд            |
| operand2 | Число                                                                                                                                                                                                                                                                                                                                                                                                | Второй операнд            |
| operator | Маркер<br/>**AND** - И (and)<br/>**LEFT_ROTATE** - Левое вращение (left_rotate)<br/>**LEFT_SHIFT** - Сдвиг влево (left_shift)<br/>**NOT** - НЕ (not)<br/>**OR** - ИЛИ (or)<br/>**RIGHT_ROTATE** - Правое вращение (right_rotate)<br/>**RIGHT_SHIFT** - Сдвиг вправо (right_shift)<br/>**UNSIGNED_RIGHT_SHIFT** - Беззнаковый сдвиг вправо (unsigned_right_shift)<br/>**XOR** - Исключающее ИЛИ (xor) | Тип операции              |

<h3 id=set_variable_bytes_to_text>
  <code>variable::bytes_to_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать байты в текст\
**Тип:** Действие, возращающее значение\
**Описание:** Преобразовывает байты в текст и присваивает результат в переменную.

**Пример использования:**
```ts
`variable` = variable::bytes_to_text([1, 2], "UTF_16");

//Или в сухую позиционно

variable::bytes_to_text(`variable`, [1, 2], "UTF_16");

//Или в сухую по ключам

variable::bytes_to_text(variable=`variable`, bytes=[1, 2], charset="UTF_16");
```

**Аргументы:**

| ID       | Тип                                                                        | Описание                  |
|----------|----------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Текст\]                                                        | Переменная для присвоения |
| bytes    | Message 'actions.array' not found in 'ru_RU'\[Число\]                      | Байты для преобразования  |
| charset  | Маркер<br/>**UTF_16** - UTF-16<br/>**UTF_8** - UTF-8<br/>**ASCII** - ASCII | Кодировка                 |

<h3 id=set_variable_center_location>
  <code>variable::center_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить центральное местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Находит местоположение равное центру между несколькими местоположениями и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::center_location([location(0,0,0,0,0), location(0,0,0,0,0)]);

//Или в сухую позиционно

variable::center_location(`variable`, [location(0,0,0,0,0), location(0,0,0,0,0)]);

//Или в сухую по ключам

variable::center_location(variable=`variable`, locations=[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

**Аргументы:**

| ID        | Тип                                                            | Описание                     |
|-----------|----------------------------------------------------------------|------------------------------|
| variable  | Переменная\[Местоположение\]                                   | Переменная для присвоения    |
| locations | Message 'actions.array' not found in 'ru_RU'\[Местоположение\] | Местоположения для установки |

<h3 id=set_variable_change_component_parsing>
  <code>variable::change_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Изменить тип стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Изменяет тип стилизуемого текста, преобразуя его стили из одного формата в другой, и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::change_component_parsing("component", "JSON");

//Или от объекта

`variable` = "component".change_component_parsing("JSON");

//Или в сухую позиционно

variable::change_component_parsing(`variable`, "component", "JSON");

//Или в сухую по ключам

variable::change_component_parsing(variable=`variable`, component="component", parsing="JSON");
```

**Аргументы:**

| ID        | Тип                                                                                                               | Описание                  |
|-----------|-------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable  | Переменная\[Текст\]                                                                                               | Переменная для присвоения |
| component | Текст                                                                                                             | Стилизуемый текст         |
| parsing   | Маркер<br/>**JSON** - JSON<br/>**LEGACY** - Цветной (&)<br/>**MINIMESSAGE** - Стилизуемый<br/>**PLAIN** - Обычный | Тип стилизуемого текста   |

<h3 id=set_variable_char_to_number>
  <code>variable::char_to_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить число по символу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённое число из символа и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::char_to_number("char");

//Или от объекта

`variable` = "char".char_to_number();

//Или в сухую позиционно

variable::char_to_number(`variable`, "char");

//Или в сухую по ключам

variable::char_to_number(variable=`variable`, char="char");
```

**Аргументы:**

| ID       | Тип                 | Описание                   |
|----------|---------------------|----------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения  |
| char     | Текст               | Символ для получения числа |

<h3 id=set_variable_chunk_text>
  <code>variable::chunk_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Фрагментировать текст\
**Тип:** Действие, возращающее значение\
**Описание:** Фрагментирует текст по указанному числу символов на список строк и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::chunk_text("text", 1);

//Или от объекта

`variable` = "text".chunk_text(1);

//Или в сухую позиционно

variable::chunk_text(`variable`, "text", 1);

//Или в сухую по ключам

variable::chunk_text(variable=`variable`, text="text", size=1);
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| text     | Текст                | Фрагментируемый текст     |
| size     | Число                | Размер фрагмента          |

<h3 id=set_variable_clamp>
  <code>variable::clamp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Ограничить число\
**Тип:** Действие, возращающее значение\
**Описание:** Проверяет, находится ли число между минимальным и максимальным значением, и если нет, устанавливает его на ближайшее.

**Пример использования:**
```ts
`variable` = variable::clamp(1, 2, 3);

//Или от объекта

`variable` = (1).clamp(2, 3);

//Или в сухую позиционно

variable::clamp(`variable`, 1, 2, 3);

//Или в сухую по ключам

variable::clamp(variable=`variable`, number=1, min=2, max=3);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| number   | Число               | Число для ограничения     |
| min      | Число               | Минимальное значение      |
| max      | Число               | Максимальное значение     |

<h3 id=set_variable_clamp_location>
  <code>variable::clamp_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Ограничить местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Проверяет, находится ли местоположение внутри региона, и если нет, устанавливает ближайшее к нему местоположение в регионе.

**Пример использования:**
```ts
`variable` = variable::clamp_location(location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "XYZ");

//Или от объекта

`variable` = location(0,0,0,0,0).clamp_location(location(0,0,0,0,0), location(0,0,0,0,0), "XYZ");

//Или в сухую позиционно

variable::clamp_location(`variable`, location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "XYZ");

//Или в сухую по ключам

variable::clamp_location(variable=`variable`, location=location(0,0,0,0,0), corner_1=location(0,0,0,0,0), corner_2=location(0,0,0,0,0), coordinates_mode="XYZ");
```

**Аргументы:**

| ID               | Тип                                                                                        | Описание                  |
|------------------|--------------------------------------------------------------------------------------------|---------------------------|
| variable         | Переменная\[Местоположение\]                                                               | Переменная для присвоения |
| location         | Местоположение                                                                             | Местоположение            |
| corner_1         | Местоположение                                                                             | Первый угол региона       |
| corner_2         | Местоположение                                                                             | Второй угол региона       |
| coordinates_mode | Маркер<br/>**XYZ** - Все координаты<br/>**XZ** - Координаты X и Z<br/>**Y** - Координата Y | Тип координат             |

<h3 id=set_variable_clear_color_codes>
  <code>variable::clear_color_codes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить цвета текста\
**Тип:** Действие, возращающее значение\
**Описание:** Очищает текст от цветовых кодов и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::clear_color_codes("text");

//Или от объекта

`variable` = "text".clear_color_codes();

//Или в сухую позиционно

variable::clear_color_codes(`variable`, "text");

//Или в сухую по ключам

variable::clear_color_codes(variable=`variable`, text="text");
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| text     | Текст               | Текст для изменения       |

<h3 id=set_variable_clear_map>
  <code>variable::clear_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить словарь\
**Тип:** Действие без значения\
**Описание:** Очищает словарь.

**Пример использования:**
```ts
variable::clear_map(`map`);

//Или от объекта

`map`.clear_map();

//Или в сухую по ключам

variable::clear_map(map=`map`);
```

**Аргументы:**

| ID  | Тип        | Описание            |
|-----|------------|---------------------|
| map | Переменная | Словарь для очистки |

<h3 id=set_variable_code_bytes>
  <code>variable::code_bytes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Закодировать байты\
**Тип:** Действие, возращающее значение\
**Описание:** Кодирует/раскодирует входящие байты выбранным методом и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::code_bytes([1, 2], "BASE64_ENCODE");

//Или в сухую позиционно

variable::code_bytes(`variable`, [1, 2], "BASE64_ENCODE");

//Или в сухую по ключам

variable::code_bytes(variable=`variable`, input=[1, 2], codec="BASE64_ENCODE");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                                   | Описание                  |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Список\]                                                                                                                                                                  | Переменная для присвоения |
| input    | Message 'actions.array' not found in 'ru_RU'\[Число\]                                                                                                                                 | Входящие байты            |
| codec    | Маркер<br/>**BASE64_ENCODE** - Кодирование в Base64<br/>**BASE64_DECODE** - Раскодирование из Base64<br/>**ZLIB_COMPRESS** - Сжатие в zlib<br/>**ZLIB_DECOMPRESS** - Разжатие из zlib | Метод                     |

<h3 id=set_variable_compact_component>
  <code>variable::compact_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сжать стилизуемый текст\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной указанный стилизуемый текст без элементов стиля и дочерних частей.

**Пример использования:**
```ts
`variable` = variable::compact_component("component");

//Или от объекта

`variable` = "component".compact_component();

//Или в сухую позиционно

variable::compact_component(`variable`, "component");

//Или в сухую по ключам

variable::compact_component(variable=`variable`, component="component");
```

**Аргументы:**

| ID        | Тип                 | Описание                    |
|-----------|---------------------|-----------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения   |
| component | Текст               | Сжимаемый стилизуемый текст |

<h3 id=set_variable_component_of_children>
  <code>variable::component_of_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать стилизуемый текст из дочерних частей\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт стилизуемый текст из указанных дочерних стилизуемых текстов и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::component_of_children(["components", "components"]);

//Или в сухую позиционно

variable::component_of_children(`variable`, ["components", "components"]);

//Или в сухую по ключам

variable::component_of_children(variable=`variable`, components=["components", "components"]);
```

**Аргументы:**

| ID         | Тип                                                   | Описание                  |
|------------|-------------------------------------------------------|---------------------------|
| variable   | Переменная\[Текст\]                                   | Переменная для присвоения |
| components | Message 'actions.array' not found in 'ru_RU'\[Текст\] | Стилизуемые тексты        |

<h3 id=set_variable_convert_number_to_text>
  <code>variable::convert_number_to_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать число в текст\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат преобразования числа в текст.\
**Дополнительная информация:**\
&nbsp;&nbsp;Работает только с целыми числами.\
&nbsp;&nbsp;Основание системы счисления должно находиться в диапазоне от 2 до 36 включительно.

**Пример использования:**
```ts
`variable` = variable::convert_number_to_text(1, 2);

//Или от объекта

`variable` = (1).convert_number_to_text(2);

//Или в сухую позиционно

variable::convert_number_to_text(`variable`, 1, 2);

//Или в сухую по ключам

variable::convert_number_to_text(variable=`variable`, number=1, radix=2);
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения   |
| number   | Число               | Число для преобразования    |
| radix    | Число               | Основание системы счисления |

<h3 id=set_variable_convert_text_to_number>
  <code>variable::convert_text_to_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать текст в число\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат преобразования числа в виде текста другой системы счисления в число десятичной системы счисления. Работает только с целыми числами.

**Пример использования:**
```ts
`variable` = variable::convert_text_to_number("text", 1);

//Или от объекта

`variable` = "text".convert_text_to_number(1);

//Или в сухую позиционно

variable::convert_text_to_number(`variable`, "text", 1);

//Или в сухую по ключам

variable::convert_text_to_number(variable=`variable`, text="text", radix=1);
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения   |
| text     | Текст               | Текст для преобразования    |
| radix    | Число               | Основание системы счисления |

<h3 id=set_variable_cosine>
  <code>variable::cosine</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Косинус числа\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает косинус от числа.

**Пример использования:**
```ts
`variable` = variable::cosine(1, "ARCCOSINE", "DEGREES");

//Или от объекта

`variable` = (1).cosine("ARCCOSINE", "DEGREES");

//Или в сухую позиционно

variable::cosine(`variable`, 1, "ARCCOSINE", "DEGREES");

//Или в сухую по ключам

variable::cosine(variable=`variable`, number=1, variant="ARCCOSINE", input="DEGREES");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                          | Описание                     |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| variable | Переменная\[Число\]                                                                                                                                                          | Переменная для присвоения    |
| number   | Число                                                                                                                                                                        | Число для получения косинуса |
| variant  | Маркер<br/>**ARCCOSINE** - Арккосинус<br/>**COSINE** - Косинус<br/>**HYPERBOLIC_ARCCOSINE** - Гиперболический арккосинус<br/>**HYPERBOLIC_COSINE** - Гиперболический косинус | Тип операции                 |
| input    | Маркер<br/>**DEGREES** - Градусы<br/>**RADIANS** - Радианы                                                                                                                   | Тип угла                     |

<h3 id=set_variable_cotangent>
  <code>variable::cotangent</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Котангенс числа\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает котангенс от числа.

**Пример использования:**
```ts
`variable` = variable::cotangent(1, "ARCCOTANGENT", "DEGREES");

//Или от объекта

`variable` = (1).cotangent("ARCCOTANGENT", "DEGREES");

//Или в сухую позиционно

variable::cotangent(`variable`, 1, "ARCCOTANGENT", "DEGREES");

//Или в сухую по ключам

variable::cotangent(variable=`variable`, number=1, variant="ARCCOTANGENT", input="DEGREES");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                                              | Описание                       |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| variable | Переменная\[Число\]                                                                                                                                                                              | Переменная для присвоения      |
| number   | Число                                                                                                                                                                                            | Число для получения котангенса |
| variant  | Маркер<br/>**ARCCOTANGENT** - Арккотангенс<br/>**COTANGENT** - Котангенс<br/>**HYPERBOLIC_ARCCOTANGENT** - Гиперболический арккотангенс<br/>**HYPERBOLIC_COTANGENT** - Гиперболический котангенс | Тип операции                   |
| input    | Маркер<br/>**DEGREES** - Градусы<br/>**RADIANS** - Радианы                                                                                                                                       | Тип угла                       |

<h3 id=set_variable_create_keybind_component>
  <code>variable::create_keybind_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать стилизуемый текст с привязкой к клавише\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной стилизуемый текст, привязанный к клавише клиента.

**Пример использования:**
```ts
`variable` = variable::create_keybind_component("key");

//Или в сухую позиционно

variable::create_keybind_component(`variable`, "key");

//Или в сухую по ключам

variable::create_keybind_component(variable=`variable`, key="key");
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| key      | Текст               | Ключ клавиши              |

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
`variable` = variable::create_list(["any value", "any value"]);

//Или в сухую позиционно

variable::create_list(`variable`, ["any value", "any value"]);

//Или в сухую по ключам

variable::create_list(variable=`variable`, values=["any value", "any value"]);
```

**Аргументы:**

| ID       | Тип                                                            | Описание                  |
|----------|----------------------------------------------------------------|---------------------------|
| variable | Переменная\[Список\]                                           | Переменная для присвоения |
| values   | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Значения                  |

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
`variable` = variable::create_map([`keys`, `keys`], [`values`, `values`]);

//Или в сухую позиционно

variable::create_map(`variable`, [`keys`, `keys`], [`values`, `values`]);

//Или в сухую по ключам

variable::create_map(variable=`variable`, keys=[`keys`, `keys`], values=[`values`, `values`]);
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Словарь\] | Переменная для присвоения |
| keys     | Список                | Список ключей             |
| values   | Список                | Список значений           |

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
`variable` = variable::create_map_from_values(["any value", "any value"], ["any value", "any value"]);

//Или в сухую позиционно

variable::create_map_from_values(`variable`, ["any value", "any value"], ["any value", "any value"]);

//Или в сухую по ключам

variable::create_map_from_values(variable=`variable`, keys=["any value", "any value"], values=["any value", "any value"]);
```

**Аргументы:**

| ID       | Тип                                                            | Описание                  |
|----------|----------------------------------------------------------------|---------------------------|
| variable | Переменная\[Словарь\]                                          | Переменная для присвоения |
| keys     | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Ключи                     |
| values   | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Значения                  |

<h3 id=set_variable_create_translatable_component>
  <code>variable::create_translatable_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать переводимый стилизуемый текст\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной переводимый стилизуемый текст с указанными аргументами.\
**Дополнительная информация:**\
&nbsp;&nbsp;Если запасное сообщение не задано и указанный ключ не имеет перевода, конечное сообщение будет равно указанному ключу.

**Пример использования:**
```ts
`variable` = variable::create_translatable_component("key", "fallback", ["args", "args"]);

//Или в сухую позиционно

variable::create_translatable_component(`variable`, "key", "fallback", ["args", "args"]);

//Или в сухую по ключам

variable::create_translatable_component(variable=`variable`, key="key", fallback="fallback", args=["args", "args"]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Текст\]                                   | Переменная для присвоения |
| key      | Текст                                                 | Ключ                      |
| fallback | Текст                                                 | Запасное сообщение        |
| args     | Message 'actions.array' not found in 'ru_RU'\[Текст\] | Аргументы для вставки     |

<h3 id=set_variable_decrement>
  <code>variable::decrement</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отнимание (-=)\
**Тип:** Действие без значения\
**Описание:** Отнимает от переменной выбранное число.

**Пример использования:**
```ts
variable::decrement(`variable`, 1);

//Или от объекта

`variable`.decrement(1);

//Или в сухую по ключам

variable::decrement(variable=`variable`, number=1);
```

**Аргументы:**

| ID       | Тип        | Описание                  |
|----------|------------|---------------------------|
| variable | Переменная | Переменная для присвоения |
| number   | Число      | Число для отнимания       |

<h3 id=set_variable_divide>
  <code>variable::divide</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Деление чисел (÷)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной частное чисел.

**Пример использования:**
```ts
`variable` = variable::divide([1, 2], "CEIL");

//Или в сухую позиционно

variable::divide(`variable`, [1, 2], "CEIL");

//Или в сухую по ключам

variable::divide(variable=`variable`, value=[1, 2], division_mode="CEIL");
```

**Аргументы:**

| ID            | Тип                                                                                                                                                          | Описание                  |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable      | Переменная\[Число\]                                                                                                                                          | Переменная для присвоения |
| value         | Message 'actions.array' not found in 'ru_RU'\[Число\]                                                                                                        | Числа для деления         |
| division_mode | Маркер<br/>**CEIL** - Округлить до большего<br/>**DEFAULT** - Без округления<br/>**FLOOR** - Округлить до меньшего<br/>**ROUND_TO_INT** - Обычное округление | Режим деления             |

<h3 id=set_variable_divide_vector>
  <code>variable::divide_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Деление векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат деления двух векторов.

**Пример использования:**
```ts
`variable` = variable::divide_vector(vector(0,0,0), vector(0,0,0));

//Или в сухую позиционно

variable::divide_vector(`variable`, vector(0,0,0), vector(0,0,0));

//Или в сухую по ключам

variable::divide_vector(variable=`variable`, vector=vector(0,0,0), divider=vector(0,0,0));
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Вектор\] | Переменная для присвоения |
| vector   | Вектор               | Вектор для изменения      |
| divider  | Вектор               | Вектор-делитель           |

<h3 id=set_variable_dummy>
  <code>variable::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** ...\
**Тип:** Действие без значения\
**Описание:** ...

**Пример использования:**
```ts
variable::dummy();
```

<h3 id=set_variable_edit_item_custom_model_data>
  <code>variable::edit_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Изменить данные о модели предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Изменяет данные о модели предмета (CustomModelData) и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::edit_item_custom_model_data(item("stick"), ["any value", "any value"], "FLOATS", "SET");

//Или от объекта

`variable` = item("stick").edit_item_custom_model_data(["any value", "any value"], "FLOATS", "SET");

//Или в сухую позиционно

variable::edit_item_custom_model_data(`variable`, item("stick"), ["any value", "any value"], "FLOATS", "SET");

//Или в сухую по ключам

variable::edit_item_custom_model_data(variable=`variable`, item=item("stick"), data=["any value", "any value"], value_type="FLOATS", setup_mode="SET");
```

**Аргументы:**

| ID         | Тип                                                                                                                                                                                      | Описание                  |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Предмет\]                                                                                                                                                                    | Переменная для присвоения |
| item       | Предмет                                                                                                                                                                                  | Предмет                   |
| data       | Message 'actions.array' not found in 'ru_RU'\[Любое значение\]                                                                                                                           | Данные                    |
| value_type | Маркер<br/>**FLOATS** - Плавающие значения (floats)<br/>**BOOLEANS** - Булевые значения (booleans)<br/>**STRINGS** - Строчные значения (strings)<br/>**COLORS** - Список цветов (colors) | Тип данных                |
| setup_mode | Маркер<br/>**SET** - Установка<br/>**ADD** - Добавление<br/>**REMOVE_ALL** - Удалить все<br/>**REMOVE_FIRST** - Удалить первую запись<br/>**REMOVE_LAST** - Удалить последнюю запись     | Действие                  |

<h3 id=set_variable_face_location>
  <code>variable::face_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Направить местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Поворачивает местоположение в направлении другого местоположения и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::face_location(location(0,0,0,0,0), location(0,0,0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).face_location(location(0,0,0,0,0));

//Или в сухую позиционно

variable::face_location(`variable`, location(0,0,0,0,0), location(0,0,0,0,0));

//Или в сухую по ключам

variable::face_location(variable=`variable`, location=location(0,0,0,0,0), target=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                          | Описание                     |
|----------|------------------------------|------------------------------|
| variable | Переменная\[Местоположение\] | Переменная для присвоения    |
| location | Местоположение               | Местоположения для установки |
| target   | Местоположение               | Целевое местоположение       |

<h3 id=set_variable_find_nearest_location>
  <code>variable::find_nearest_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить ближайшее местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Ищет в перечисленных местоположениях ближайшее к указанному и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::find_nearest_location(location(0,0,0,0,0), [location(0,0,0,0,0), location(0,0,0,0,0)], "XYZ");

//Или от объекта

`variable` = location(0,0,0,0,0).find_nearest_location([location(0,0,0,0,0), location(0,0,0,0,0)], "XYZ");

//Или в сухую позиционно

variable::find_nearest_location(`variable`, location(0,0,0,0,0), [location(0,0,0,0,0), location(0,0,0,0,0)], "XYZ");

//Или в сухую по ключам

variable::find_nearest_location(variable=`variable`, location=location(0,0,0,0,0), locations=[location(0,0,0,0,0), location(0,0,0,0,0)], distance_type="XYZ");
```

**Аргументы:**

| ID            | Тип                                                                          | Описание                  |
|---------------|------------------------------------------------------------------------------|---------------------------|
| variable      | Переменная\[Местоположение\]                                                 | Переменная для присвоения |
| location      | Местоположение                                                               | Местоположение            |
| locations     | Message 'actions.array' not found in 'ru_RU'\[Местоположение\]               | Местоположения для поиска |
| distance_type | Маркер<br/>**XYZ** - В объёме<br/>**XZ** - В плоскости<br/>**Y** - По высоте | Тип расстояния            |

<h3 id=set_variable_find_nearest_number>
  <code>variable::find_nearest_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Ближайшее число\
**Тип:** Действие, возращающее значение\
**Описание:** Ищет в перечисленных числах ближайшее к указанному числу и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::find_nearest_number(1, [2, 3]);

//Или от объекта

`variable` = (1).find_nearest_number([2, 3]);

//Или в сухую позиционно

variable::find_nearest_number(`variable`, 1, [2, 3]);

//Или в сухую по ключам

variable::find_nearest_number(variable=`variable`, number=1, numbers=[2, 3]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                   | Переменная для присвоения |
| number   | Число                                                 | Число                     |
| numbers  | Message 'actions.array' not found in 'ru_RU'\[Число\] | Числа для поиска          |

<h3 id=set_variable_flatten_list>
  <code>variable::flatten_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сгладить список\
**Тип:** Действие, возращающее значение\
**Описание:** Разделяет подсписки указанного списка на отдельные элементы.

**Пример использования:**
```ts
`variable` = variable::flatten_list([`list`, `list`], "FALSE");

//Или от объекта

`variable` = [`list`, `list`].flatten_list("FALSE");

//Или в сухую позиционно

variable::flatten_list(`variable`, [`list`, `list`], "FALSE");

//Или в сухую по ключам

variable::flatten_list(variable=`variable`, list=[`list`, `list`], deep="FALSE");
```

**Аргументы:**

| ID       | Тип                                          | Описание                  |
|----------|----------------------------------------------|---------------------------|
| variable | Переменная\[Список\]                         | Переменная для присвоения |
| list     | Список                                       | Список                    |
| deep     | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да | Глубокое сглаживание      |

<h3 id=set_variable_format_timestamp>
  <code>variable::format_timestamp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать формат времени\
**Тип:** Действие, возращающее значение\
**Описание:** Преобразовывает число (миллисекунды) в указанный формат времени и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::format_timestamp(1, "pattern", "zone_id", "locale", "CUSTOM");

//Или от объекта

`variable` = (1).format_timestamp("pattern", "zone_id", "locale", "CUSTOM");

//Или в сухую позиционно

variable::format_timestamp(`variable`, 1, "pattern", "zone_id", "locale", "CUSTOM");

//Или в сухую по ключам

variable::format_timestamp(variable=`variable`, time=1, pattern="pattern", zone_id="zone_id", locale="locale", format="CUSTOM");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Описание                          |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| variable | Переменная\[Текст\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Переменная для присвоения         |
| time     | Число                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Число для преобразования          |
| pattern  | Текст                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Шаблон времени (например, mm\:ss) |
| zone_id  | Текст                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Часовой пояс (GMT±1\.\.13)        |
| locale   | Текст                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Язык (ru_RU, en_US...)            |
| format   | Маркер<br/>**CUSTOM** - Настраиваемое<br/>**DD_MM_YYYY** - 01\/01\/1970 (dd_mm_yyyy)<br/>**DD_MM_YYYY_HH_MM_S** - 01\/01\/1970 00\:00\:00 (dd_mm_yyyy_hh_mm_s)<br/>**EEEE** - Thursday (eeee)<br/>**EEE_D_MMMM** - Thu, 01 January (eee_d_mmmm)<br/>**EEE_MMMM_D** - Thu, January 01 (eee_mmmm_d)<br/>**HH_MM_SS** - 00\:00\:00 (hh_mm_ss)<br/>**H_H_M_M_S_S** - 00h00m00s (h_h_m_m_s_s)<br/>**H_MM_A** - 00\:00 AM (h_mm_a)<br/>**S_S** - 00.00 (s_s)<br/>**YYYY_MM_DD** - 1970\/01\/01 (yyyy_mm_dd)<br/>**YYYY_MM_DD_HH_MM_S** - 1970\/01\/01 00\:00\:00 (yyyy_mm_dd_hh_mm_s) | Формат времени                    |

<h3 id=set_variable_gamma_function>
  <code>variable::gamma_function</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Гамма-функция\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает гамма-функцию числа и присваивает к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Является обобщением факториала.\
&nbsp;&nbsp;Гамма-функция может быть представлена как (n-1)!, где n - заданное число.

**Пример использования:**
```ts
`variable` = variable::gamma_function(1);

//Или от объекта

`variable` = (1).gamma_function();

//Или в сухую позиционно

variable::gamma_function(`variable`, 1);

//Или в сухую по ключам

variable::gamma_function(variable=`variable`, number=1);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| number   | Число               | Число                     |

<h3 id=set_variable_gaussian_distribution>
  <code>variable::gaussian_distribution</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Нормально распределённое случайное число\
**Тип:** Действие, возращающее значение\
**Описание:** Выдаёт случайное число близкое к среднему значению μ со стандартным отклонением σ с шансом, заданным графиком нормального распределения.

**Пример использования:**
```ts
`variable` = variable::gaussian_distribution(1, 2, "FOLDER_NORMAL");

//Или в сухую позиционно

variable::gaussian_distribution(`variable`, 1, 2, "FOLDER_NORMAL");

//Или в сухую по ключам

variable::gaussian_distribution(variable=`variable`, deviant=1, mean=2, distribution="FOLDER_NORMAL");
```

**Аргументы:**

| ID           | Тип                                                                                         | Описание                            |
|--------------|---------------------------------------------------------------------------------------------|-------------------------------------|
| variable     | Переменная\[Число\]                                                                         | Переменная для присвоения           |
| deviant      | Число                                                                                       | Отклонение σ от среднего значения μ |
| mean         | Число                                                                                       | Среднее значение μ                  |
| distribution | Маркер<br/>**FOLDER_NORMAL** - Отклонение в сторону >= μ<br/>**NORMAL** - Полное отклонение | Тип σ отклонения                    |

<h3 id=set_variable_get_all_block_data>
  <code>variable::get_all_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить все данные блока\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной все данные блока на выбранном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_all_block_data(location(0,0,0,0,0), "FALSE");

//Или от объекта

`variable` = location(0,0,0,0,0).get_all_block_data("FALSE");

//Или в сухую позиционно

variable::get_all_block_data(`variable`, location(0,0,0,0,0), "FALSE");

//Или в сухую по ключам

variable::get_all_block_data(variable=`variable`, location=location(0,0,0,0,0), hide_unspecified="FALSE");
```

**Аргументы:**

| ID               | Тип                                                      | Описание                         |
|------------------|----------------------------------------------------------|----------------------------------|
| variable         | Переменная\[Текст\]                                      | Переменная для присвоения        |
| location         | Местоположение                                           | Местоположение блока             |
| hide_unspecified | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Скрытие неустановленных значений |

<h3 id=set_variable_get_all_coordinates>
  <code>variable::get_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить все координаты местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение всех координат с местоположения и присваивает их в переменные.

**Пример использования:**
```ts
`x`, `y`, `z`, `yaw`, `pitch` = variable::get_all_coordinates(location(0,0,0,0,0));

//Или от объекта

`x`, `y`, `z`, `yaw`, `pitch` = location(0,0,0,0,0).get_all_coordinates();

//Или в сухую позиционно

variable::get_all_coordinates(`x`, `y`, `z`, `yaw`, `pitch`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_all_coordinates(x=`x`, y=`y`, z=`z`, yaw=`yaw`, pitch=`pitch`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                 | Описание                     |
|----------|---------------------|------------------------------|
| x        | Переменная\[Число\] | Координата X                 |
| y        | Переменная\[Число\] | Координата Y                 |
| z        | Переменная\[Число\] | Координата Z                 |
| yaw      | Переменная\[Число\] | Горизонтальный поворот       |
| pitch    | Переменная\[Число\] | Вертикальный поворот         |
| location | Местоположение      | Местоположение для получения |

<h3 id=set_variable_get_angle_between_vectors>
  <code>variable::get_angle_between_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить угол между двумя векторами\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение угла между двумя векторами.

**Пример использования:**
```ts
`variable` = variable::get_angle_between_vectors(vector(0,0,0), vector(0,0,0), "DEGREES");

//Или в сухую позиционно

variable::get_angle_between_vectors(`variable`, vector(0,0,0), vector(0,0,0), "DEGREES");

//Или в сухую по ключам

variable::get_angle_between_vectors(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0), angle_units="DEGREES");
```

**Аргументы:**

| ID          | Тип                                                        | Описание                  |
|-------------|------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Число\]                                        | Переменная для присвоения |
| vector_1    | Вектор                                                     | Первый вектор             |
| vector_2    | Вектор                                                     | Второй вектор             |
| angle_units | Маркер<br/>**DEGREES** - Градусы<br/>**RADIANS** - Радианы | Тип угла                  |

<h3 id=set_variable_get_block_custom_tag>
  <code>variable::get_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** creative_plus.action.set_variable_get_block_custom_tag.name\
**Тип:** Действие, возращающее значение\
**Описание:** creative_plus.action.set_variable_get_block_custom_tag.description

**Пример использования:**
```ts
`variable` = variable::get_block_custom_tag(location(0,0,0,0,0), "tag_name", "tag_value", "any value");

//Или в сухую позиционно

variable::get_block_custom_tag(`variable`, location(0,0,0,0,0), "tag_name", "tag_value", "any value");

//Или в сухую по ключам

variable::get_block_custom_tag(variable=`variable`, location=location(0,0,0,0,0), tag_name="tag_name", tag_value="tag_value", default_value="any value");
```

**Аргументы:**

| ID            | Тип                          | Описание                                                                           |
|---------------|------------------------------|------------------------------------------------------------------------------------|
| variable      | Переменная\[Любое значение\] | creative_plus.action.set_variable_get_block_custom_tag.argument.variable.name      |
| location      | Местоположение               | creative_plus.action.set_variable_get_block_custom_tag.argument.location.name      |
| tag_name      | Текст                        | creative_plus.action.set_variable_get_block_custom_tag.argument.tag_name.name      |
| tag_value     | Текст                        | creative_plus.action.set_variable_get_block_custom_tag.argument.tag_value.name     |
| default_value | Любое значение               | creative_plus.action.set_variable_get_block_custom_tag.argument.default_value.name |

<h3 id=set_variable_get_block_data>
  <code>variable::get_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить данные блока\
**Тип:** Действие, возращающее значение\
**Описание:** Получает данные блока и присваивает его в переменную.\
**Работает с:**\
&nbsp;&nbsp;Блоками-сущностями (сундуки, таблички, бочки и т.д.)

**Пример использования:**
```ts
`variable` = variable::get_block_data(location(0,0,0,0,0), "tag_name");

//Или от объекта

`variable` = location(0,0,0,0,0).get_block_data("tag_name");

//Или в сухую позиционно

variable::get_block_data(`variable`, location(0,0,0,0,0), "tag_name");

//Или в сухую по ключам

variable::get_block_data(variable=`variable`, location=location(0,0,0,0,0), tag_name="tag_name");
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| location | Местоположение      | Местоположение блока      |
| tag_name | Текст               | Название тега             |

<h3 id=set_variable_get_block_growth>
  <code>variable::get_block_growth</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить уровень роста блока\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение уровня роста блока на указанном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_block_growth(location(0,0,0,0,0), "GROWTH_PERCENTAGE");

//Или от объекта

`variable` = location(0,0,0,0,0).get_block_growth("GROWTH_PERCENTAGE");

//Или в сухую позиционно

variable::get_block_growth(`variable`, location(0,0,0,0,0), "GROWTH_PERCENTAGE");

//Или в сухую по ключам

variable::get_block_growth(variable=`variable`, location=location(0,0,0,0,0), growth_unit="GROWTH_PERCENTAGE");
```

**Аргументы:**

| ID          | Тип                                                                                  | Описание                  |
|-------------|--------------------------------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Число\]                                                                  | Переменная для присвоения |
| location    | Местоположение                                                                       | Местоположение блока      |
| growth_unit | Маркер<br/>**GROWTH_PERCENTAGE** - Процент роста<br/>**GROWTH_STAGE** - Стадия роста | Единица измерения         |

<h3 id=set_variable_get_block_material>
  <code>variable::get_block_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип блока\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной тип блока на выбранном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_block_material(location(0,0,0,0,0), "ID");

//Или от объекта

`variable` = location(0,0,0,0,0).get_block_material("ID");

//Или в сухую позиционно

variable::get_block_material(`variable`, location(0,0,0,0,0), "ID");

//Или в сухую по ключам

variable::get_block_material(variable=`variable`, location=location(0,0,0,0,0), value_type="ID");
```

**Аргументы:**

| ID         | Тип                                                                                                                       | Описание                  |
|------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Текст\]                                                                                                       | Переменная для присвоения |
| location   | Местоположение                                                                                                            | Местоположение блока      |
| value_type | Маркер<br/>**ID** - ID блока<br/>**ID_WITH_DATA** - ID и данные блока<br/>**ITEM** - Как предмет<br/>**NAME** - Имя блока | Тип значения              |

<h3 id=set_variable_get_block_material_property>
  <code>variable::get_block_material_property</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить свойство блока\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённое свойство блока и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_block_material_property("minecraft:oak_log[axis=x]", "BLAST_RESISTANCE");

//Или от объекта

`variable` = "minecraft:oak_log[axis=x]".get_block_material_property("BLAST_RESISTANCE");

//Или в сухую позиционно

variable::get_block_material_property(`variable`, "minecraft:oak_log[axis=x]", "BLAST_RESISTANCE");

//Или в сухую по ключам

variable::get_block_material_property(variable=`variable`, block="minecraft:oak_log[axis=x]", property="BLAST_RESISTANCE");
```

**Аргументы:**

| ID       | Тип                                                                                                                     | Описание                  |
|----------|-------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                                                                                     | Переменная для присвоения |
| block    | Блок                                                                                                                    | Блок для получения        |
| property | Маркер<br/>**BLAST_RESISTANCE** - Устойчивость к взрыву<br/>**HARDNESS** - Прочность<br/>**SLIPPERINESS** - Скользкость | Свойство                  |

<h3 id=set_variable_get_block_power>
  <code>variable::get_block_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить силу редстоуна\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение силы сигнала редстоуна на указанном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_block_power(location(0,0,0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).get_block_power();

//Или в сухую позиционно

variable::get_block_power(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_block_power(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| location | Местоположение      | Местоположение блока      |

<h3 id=set_variable_get_block_sound>
  <code>variable::get_block_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить звук блока\
**Тип:** Действие, возращающее значение\
**Описание:** Получает звук указанного блока и присваивает его к переменной.

**Пример использования:**
```ts
`variable` = variable::get_block_sound("minecraft:oak_log[axis=x]", "BREAK");

//Или от объекта

`variable` = "minecraft:oak_log[axis=x]".get_block_sound("BREAK");

//Или в сухую позиционно

variable::get_block_sound(`variable`, "minecraft:oak_log[axis=x]", "BREAK");

//Или в сухую по ключам

variable::get_block_sound(variable=`variable`, block="minecraft:oak_log[axis=x]", source="BREAK");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                        | Описание                  |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Звук\]                                                                                                                                         | Переменная для присвоения |
| block    | Блок                                                                                                                                                       | Блок                      |
| source   | Маркер<br/>**BREAK** - Ломание<br/>**PLACE** - Установка<br/>**HIT** - Процесс ломания<br/>**FALL** - Падение на блок<br/>**STEP** - Передвижение по блоку | Источник звука            |

<h3 id=set_variable_get_blocks_by_tag>
  <code>variable::get_blocks_by_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить блоки по Minecraft-тегу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает блоки по Minecraft-тегу (например, "mineable/shovel") и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_blocks_by_tag("namespace", "ID");

//Или в сухую позиционно

variable::get_blocks_by_tag(`variable`, "namespace", "ID");

//Или в сухую по ключам

variable::get_blocks_by_tag(variable=`variable`, namespace="namespace", result_type="ID");
```

**Аргументы:**

| ID          | Тип                                                                                                            | Описание                  |
|-------------|----------------------------------------------------------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Список\]                                                                                           | Переменная для присвоения |
| namespace   | Текст                                                                                                          | Minecraft-тег             |
| result_type | Маркер<br/>**ID** - ID блока<br/>**TRANSLATION_KEY** - Переводимое название блока<br/>**ITEM** - Предмет блока | Тип результата            |

<h3 id=set_variable_get_book_text>
  <code>variable::get_book_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить текст книги\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение текста книги на определённой странице.

**Пример использования:**
```ts
`variable` = variable::get_book_text(item("stick"), 1);

//Или от объекта

`variable` = item("stick").get_book_text(1);

//Или в сухую позиционно

variable::get_book_text(`variable`, item("stick"), 1);

//Или в сухую по ключам

variable::get_book_text(variable=`variable`, book=item("stick"), page=1);
```

**Аргументы:**

| ID       | Тип                 | Описание                     |
|----------|---------------------|------------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения    |
| book     | Предмет             | Книга для получения значения |
| page     | Число               | Номер страницы               |

<h3 id=set_variable_get_brushable_block_item>
  <code>variable::get_brushable_block_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить предмет из подозрительного блока\
**Тип:** Действие, возращающее значение\
**Описание:** Получить предмет из подозрительного блока (песка, гравия) и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_brushable_block_item(location(0,0,0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).get_brushable_block_item();

//Или в сухую позиционно

variable::get_brushable_block_item(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_brushable_block_item(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| location | Местоположение        | Местоположение блока      |

<h3 id=set_variable_get_bundle_items>
  <code>variable::get_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить содержимое мешка\
**Тип:** Действие, возращающее значение\
**Описание:** Получает содержимое мешка и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_bundle_items(item("stick"));

//Или от объекта

`variable` = item("stick").get_bundle_items();

//Или в сухую позиционно

variable::get_bundle_items(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_bundle_items(variable=`variable`, bundle=item("stick"));
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| bundle   | Предмет              | Мешок                     |

<h3 id=set_variable_get_char_at>
  <code>variable::get_char_at</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить символ по индексу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает символ из текста по указанному индексу и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_char_at("text", 1);

//Или от объекта

`variable` = "text".get_char_at(1);

//Или в сухую позиционно

variable::get_char_at(`variable`, "text", 1);

//Или в сухую по ключам

variable::get_char_at(variable=`variable`, text="text", index=1);
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения   |
| text     | Текст               | Текст для получения символа |
| index    | Число               | Индекс                      |

<h3 id=set_variable_get_color_channels>
  <code>variable::get_color_channels</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить цветовые каналы\
**Тип:** Действие, возращающее значение\
**Описание:** Получает числовые значения RGB/HSB/HSL цвета в виде списка.

**Пример использования:**
```ts
`variable` = variable::get_color_channels("color", "HSB");

//Или от объекта

`variable` = "color".get_color_channels("HSB");

//Или в сухую позиционно

variable::get_color_channels(`variable`, "color", "HSB");

//Или в сухую по ключам

variable::get_color_channels(variable=`variable`, color="color", color_channels="HSB");
```

**Аргументы:**

| ID             | Тип                                                          | Описание                    |
|----------------|--------------------------------------------------------------|-----------------------------|
| variable       | Переменная\[Список\]                                         | Переменная для присвоения   |
| color          | Текст                                                        | Цвет для получения значения |
| color_channels | Маркер<br/>**HSB** - HSB<br/>**HSL** - HSL<br/>**RGB** - RGB | Цветовой канал              |

<h3 id=set_variable_get_compass_lodestone>
  <code>variable::get_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить местоположение магнетита\
**Тип:** Действие, возращающее значение\
**Описание:** Получает с намагниченного компаса местоположение магнетита и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_compass_lodestone(item("stick"));

//Или от объекта

`variable` = item("stick").get_compass_lodestone();

//Или в сухую позиционно

variable::get_compass_lodestone(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_compass_lodestone(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                          | Описание                  |
|----------|------------------------------|---------------------------|
| variable | Переменная\[Местоположение\] | Переменная для присвоения |
| item     | Предмет                      | Намагниченный компас      |

<h3 id=set_variable_get_component_children>
  <code>variable::get_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить дочерние части стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной дочерние части указанного стилизуемого текста.

**Пример использования:**
```ts
`variable` = variable::get_component_children("component");

//Или от объекта

`variable` = "component".get_component_children();

//Или в сухую позиционно

variable::get_component_children(`variable`, "component");

//Или в сухую по ключам

variable::get_component_children(variable=`variable`, component="component");
```

**Аргументы:**

| ID        | Тип                  | Описание                  |
|-----------|----------------------|---------------------------|
| variable  | Переменная\[Список\] | Переменная для присвоения |
| component | Текст                | Стилизуемый текст         |

<h3 id=set_variable_get_component_decorations>
  <code>variable::get_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить декорации стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной все декорации (стилизацию) стилизуемого текста.

**Пример использования:**
```ts
`variable` = variable::get_component_decorations("component");

//Или от объекта

`variable` = "component".get_component_decorations();

//Или в сухую позиционно

variable::get_component_decorations(`variable`, "component");

//Или в сухую по ключам

variable::get_component_decorations(variable=`variable`, component="component");
```

**Аргументы:**

| ID        | Тип                  | Описание                  |
|-----------|----------------------|---------------------------|
| variable  | Переменная\[Список\] | Переменная для присвоения |
| component | Текст                | Стилизуемый текст         |

<h3 id=set_variable_get_component_hex_color>
  <code>variable::get_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить HEX-цвет стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной HEX-цвет указанного стилизуемого текста.

**Пример использования:**
```ts
`variable` = variable::get_component_hex_color("component");

//Или от объекта

`variable` = "component".get_component_hex_color();

//Или в сухую позиционно

variable::get_component_hex_color(`variable`, "component");

//Или в сухую по ключам

variable::get_component_hex_color(variable=`variable`, component="component");
```

**Аргументы:**

| ID        | Тип                 | Описание                  |
|-----------|---------------------|---------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения |
| component | Текст               | Стилизуемый текст         |

<h3 id=set_variable_get_component_parsing>
  <code>variable::get_component_parsing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип преобразования стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение типа преобразования указанного стилизуемого текста.

**Пример использования:**
```ts
`variable` = variable::get_component_parsing("component");

//Или от объекта

`variable` = "component".get_component_parsing();

//Или в сухую позиционно

variable::get_component_parsing(`variable`, "component");

//Или в сухую по ключам

variable::get_component_parsing(variable=`variable`, component="component");
```

**Аргументы:**

| ID        | Тип                 | Описание                   |
|-----------|---------------------|----------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения  |
| component | Текст               | Исходный стилизуемый текст |

<h3 id=set_variable_get_container_contents>
  <code>variable::get_container_contents</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить содержимое контейнера\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной список содержимого контейнера на выбранном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_container_contents(location(0,0,0,0,0), "FALSE");

//Или от объекта

`variable` = location(0,0,0,0,0).get_container_contents("FALSE");

//Или в сухую позиционно

variable::get_container_contents(`variable`, location(0,0,0,0,0), "FALSE");

//Или в сухую по ключам

variable::get_container_contents(variable=`variable`, location=location(0,0,0,0,0), ignore_empty_slots="FALSE");
```

**Аргументы:**

| ID                 | Тип                                                                | Описание                    |
|--------------------|--------------------------------------------------------------------|-----------------------------|
| variable           | Переменная\[Список\]                                               | Переменная для присвоения   |
| location           | Местоположение                                                     | Местоположение контейнера   |
| ignore_empty_slots | Маркер<br/>**FALSE** - Не игнорировать<br/>**TRUE** - Игнорировать | Игнорирование пустых слотов |

<h3 id=set_variable_get_container_lock>
  <code>variable::get_container_lock</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить ключ контейнера\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной предмет ключа контейнера на указанном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_container_lock(location(0,0,0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).get_container_lock();

//Или в сухую позиционно

variable::get_container_lock(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_container_lock(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| location | Местоположение      | Местоположение блока      |

<h3 id=set_variable_get_container_name>
  <code>variable::get_container_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить имя контейнера\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной имя контейнера на выбранном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_container_name(location(0,0,0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).get_container_name();

//Или в сухую позиционно

variable::get_container_name(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_container_name(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| location | Местоположение      | Местоположение контейнера |

<h3 id=set_variable_get_coordinate>
  <code>variable::get_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить координату местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение выбранной координаты с местоположения и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_coordinate(location(0,0,0,0,0), "PITCH");

//Или от объекта

`variable` = location(0,0,0,0,0).get_coordinate("PITCH");

//Или в сухую позиционно

variable::get_coordinate(`variable`, location(0,0,0,0,0), "PITCH");

//Или в сухую по ключам

variable::get_coordinate(variable=`variable`, location=location(0,0,0,0,0), type="PITCH");
```

**Аргументы:**

| ID       | Тип                                                                                                                                    | Описание                              |
|----------|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| variable | Переменная\[Число\]                                                                                                                    | Переменная для присвоения             |
| location | Местоположение                                                                                                                         | Местоположение для получения значения |
| type     | Маркер<br/>**PITCH** - Вертикальный поворот<br/>**X** - Ось X<br/>**Y** - Ось Y<br/>**YAW** - Горизонтальный поворот<br/>**Z** - Ось Z | Тип координаты                        |

<h3 id=set_variable_get_decorate_pot_sherd>
  <code>variable::get_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить украшение вазы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной материал черепка выбранной стороны вазы на указанном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_decorate_pot_sherd(location(0,0,0,0,0), "BACK");

//Или от объекта

`variable` = location(0,0,0,0,0).get_decorate_pot_sherd("BACK");

//Или в сухую позиционно

variable::get_decorate_pot_sherd(`variable`, location(0,0,0,0,0), "BACK");

//Или в сухую по ключам

variable::get_decorate_pot_sherd(variable=`variable`, location=location(0,0,0,0,0), side="BACK");
```

**Аргументы:**

| ID       | Тип                                                                                                                               | Описание                  |
|----------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Предмет\]                                                                                                             | Переменная для присвоения |
| location | Местоположение                                                                                                                    | Местоположение вазы       |
| side     | Маркер<br/>**BACK** - Задняя сторона<br/>**FRONT** - Передняя сторона<br/>**LEFT** - Левая сторона<br/>**RIGHT** - Правая сторона | Сторона вазы              |

<h3 id=set_variable_get_entity_types_by_tag>
  <code>variable::get_entity_types_by_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить сущностей по Minecraft-тегу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает сущностей по Minecraft-тегу (например, "aquatic") и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_entity_types_by_tag("namespace", "ID");

//Или в сухую позиционно

variable::get_entity_types_by_tag(`variable`, "namespace", "ID");

//Или в сухую по ключам

variable::get_entity_types_by_tag(variable=`variable`, namespace="namespace", result_type="ID");
```

**Аргументы:**

| ID          | Тип                                                                                     | Описание                  |
|-------------|-----------------------------------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Список\]                                                                    | Переменная для присвоения |
| namespace   | Текст                                                                                   | Minecraft-тег             |
| result_type | Маркер<br/>**ID** - ID сущности<br/>**TRANSLATION_KEY** - Переводимое название сущности | Тип результата            |

<h3 id=set_variable_get_index_of_subtext>
  <code>variable::get_index_of_subtext</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить индекс подтекста\
**Тип:** Действие, возращающее значение\
**Описание:** Получает индекс подтекста из текста и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_index_of_subtext("text", "subtext", 1, "FIRST");

//Или от объекта

`variable` = "text".get_index_of_subtext("subtext", 1, "FIRST");

//Или в сухую позиционно

variable::get_index_of_subtext(`variable`, "text", "subtext", 1, "FIRST");

//Или в сухую по ключам

variable::get_index_of_subtext(variable=`variable`, text="text", subtext="subtext", start_index=1, search_mode="FIRST");
```

**Аргументы:**

| ID          | Тип                                                                                                         | Описание                    |
|-------------|-------------------------------------------------------------------------------------------------------------|-----------------------------|
| variable    | Переменная\[Число\]                                                                                         | Переменная для присвоения   |
| text        | Текст                                                                                                       | Текст для получения индекса |
| subtext     | Текст                                                                                                       | Подтекст                    |
| start_index | Число                                                                                                       | Начальный индекс            |
| search_mode | Маркер<br/>**FIRST** - С начала (получить первый индекс)<br/>**LAST** - С конца (получить последний индекс) | Режим поиска                |

<h3 id=set_variable_get_item_amount>
  <code>variable::get_item_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить количество предметов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной количество предметов в стаке.

**Пример использования:**
```ts
`variable` = variable::get_item_amount(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_amount();

//Или в сухую позиционно

variable::get_item_amount(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_amount(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_attribute>
  <code>variable::get_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить атрибут предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённый атрибут с предмета в виде словаря "UUID - Значение" и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_attribute(item("stick"), "name", "ARMOR", "ALL", "ADD_NUMBER");

//Или от объекта

`variable` = item("stick").get_item_attribute("name", "ARMOR", "ALL", "ADD_NUMBER");

//Или в сухую позиционно

variable::get_item_attribute(`variable`, item("stick"), "name", "ARMOR", "ALL", "ADD_NUMBER");

//Или в сухую по ключам

variable::get_item_attribute(variable=`variable`, item=item("stick"), name="name", attribute="ARMOR", slot="ALL", operation="ADD_NUMBER");
```

**Аргументы:**

| ID        | Тип                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Описание                  |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable  | Переменная\[Словарь\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Переменная для присвоения |
| item      | Предмет                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Предмет                   |
| name      | Текст                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Имя атрибута              |
| attribute | Маркер<br/>**ARMOR** - Броня<br/>**ARMOR_TOUGHNESS** - Плотность защиты<br/>**ATTACK_DAMAGE** - Урон атаки<br/>**ATTACK_KNOCKBACK** - Отталкивание от атаки<br/>**ATTACK_SPEED** - Скорость атаки<br/>**FLYING_SPEED** - Скорость полёта<br/>**FOLLOW_RANGE** - Расстояние следования<br/>**GENERIC_ARMOR** - Очки защиты (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Очки плотности защиты (generic.armor_toughness)<br/>**GENERIC_ATTACK_DAMAGE** - Урон атаки (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Отталкивание атаки (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Скорость атаки (generic.attack_speed)<br/>**GENERIC_BURNING_TIME** - Время горения<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Сопротивление отбрасыванию от взрыва<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Множитель урона от падения<br/>**GENERIC_FLYING_SPEED** - Скорость полёта (generic.flying_speed)<br/>**GENERIC_FOLLOW_RANGE** - Расстояние следования (generic.follow_range)<br/>**GENERIC_GRAVITY** - Гравитация<br/>**GENERIC_JUMP_STRENGTH** - Сила прыжка<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Сопротивление отталкиванию (generic.knockback_resistance)<br/>**GENERIC_LUCK** - Удача рыбалки (generic.luck)<br/>**GENERIC_MAX_ABSORPTION** - Максимальное поглощение (generic.max_absorption)<br/>**GENERIC_MAX_HEALTH** - Максимальное здоровье (generic.max_health)<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Скорость передвижения по замедляющим блокам<br/>**GENERIC_MOVEMENT_SPEED** - Скорость передвижения (generic.movement_speed)<br/>**GENERIC_OXYGEN_BONUS** - Воздух под водой<br/>**GENERIC_SAFE_FALL_DISTANCE** - Безопасная высота падения<br/>**GENERIC_SCALE** - Масштаб<br/>**GENERIC_STEP_HEIGHT** - Высота шага<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Скорость передвижения под водой<br/>**HORSE_JUMP_STRENGTH** - Сила прыжка лошади (horse.jump_strength)<br/>**KNOCKBACK_RESISTANCE** - Сопротивление отталкиванию<br/>**LUCK** - Удача<br/>**MAX_ABSORPTION** - Максимальное поглощение<br/>**MAX_HEALTH** - Максимальное здоровье<br/>**MOVEMENT_SPEED** - Скорость передвижения<br/>**PLAYER_BLOCK_BREAK_SPEED** - Скорость ломания блока<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - Расстояние взаимодействия с блоками<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - Расстояние взаимодействия с сущностями<br/>**PLAYER_MINING_EFFICIENCY** - Скорость копания<br/>**PLAYER_SNEAKING_SPEED** - Скорость передвижения крадясь<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Скорость копания под водой<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - Коэффициент разящего удара<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Шанс подкрепления зомби (zombie.spawn_reinforcements) | Тип атрибута              |
| slot      | Маркер<br/>**ALL** - Все<br/>**ARMOR** - Любая броня<br/>**BODY** - Тело (работает не со всеми сущностями)<br/>**BOOTS** - Ботинки<br/>**CHEST** - Нагрудник<br/>**HAND** - Любая рука<br/>**HEAD** - Шлем<br/>**LEGGINGS** - Поножи<br/>**MAIN_HAND** - Основная рука<br/>**OFF_HAND** - Второстепенная рука                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Слот атрибута             |
| operation | Маркер<br/>**ADD_NUMBER** - Количество (amount)<br/>**ADD_SCALAR** - Процент (percentage)<br/>**MULTIPLY_SCALAR_1** - Произведение (multiplicative)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Операция атрибута         |

<h3 id=set_variable_get_item_break_sound>
  <code>variable::get_item_break_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить звук ломания предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает звук, воспроизводимый при поломке указанного предмета, и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_break_sound(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_break_sound();

//Или в сухую позиционно

variable::get_item_break_sound(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_break_sound(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_color>
  <code>variable::get_item_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить цвет предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение цвета предмета.\
**Работает с:**\
&nbsp;&nbsp;Кожаной бронёй\
&nbsp;&nbsp;Зельями\
&nbsp;&nbsp;Стрелами с эффектом\
&nbsp;&nbsp;Заполненными картами

**Пример использования:**
```ts
`variable` = variable::get_item_color(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_color();

//Или в сухую позиционно

variable::get_item_color(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_color(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_component>
  <code>variable::get_item_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить компонент предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение компонента предмета и присваивает значение к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_component(item("stick"), "component");

//Или от объекта

`variable` = item("stick").get_item_component("component");

//Или в сухую позиционно

variable::get_item_component(`variable`, item("stick"), "component");

//Или в сухую по ключам

variable::get_item_component(variable=`variable`, item=item("stick"), component="component");
```

**Аргументы:**

| ID        | Тип                          | Описание                  |
|-----------|------------------------------|---------------------------|
| variable  | Переменная\[Любое значение\] | Переменная для присвоения |
| item      | Предмет                      | Предмет                   |
| component | Текст                        | Ключ компонента           |

<h3 id=set_variable_get_item_custom_model_data>
  <code>variable::get_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить данные модели предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает данные модели предмета (CustomModelData) и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_custom_model_data(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_custom_model_data();

//Или в сухую позиционно

variable::get_item_custom_model_data(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_custom_model_data(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_custom_tag>
  <code>variable::get_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить кастомный тег предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение кастомного тега предмета.

**Пример использования:**
```ts
`variable` = variable::get_item_custom_tag(item("stick"), "tag_name", "any value");

//Или от объекта

`variable` = item("stick").get_item_custom_tag("tag_name", "any value");

//Или в сухую позиционно

variable::get_item_custom_tag(`variable`, item("stick"), "tag_name", "any value");

//Или в сухую по ключам

variable::get_item_custom_tag(variable=`variable`, item=item("stick"), tag_name="tag_name", default_value="any value");
```

**Аргументы:**

| ID            | Тип                          | Описание                  |
|---------------|------------------------------|---------------------------|
| variable      | Переменная\[Любое значение\] | Переменная для присвоения |
| item          | Предмет                      | Предмет                   |
| tag_name      | Текст                        | Имя тега                  |
| default_value | Любое значение               | Значение по умолчанию     |

<h3 id=set_variable_get_item_custom_tags>
  <code>variable::get_item_custom_tags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить кастомные теги предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной словарь кастомных тегов предмета.

**Пример использования:**
```ts
`variable` = variable::get_item_custom_tags(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_custom_tags();

//Или в сухую позиционно

variable::get_item_custom_tags(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_custom_tags(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Словарь\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |

<h3 id=set_variable_get_item_destroyable_blocks>
  <code>variable::get_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить блоки для ломания предметом\
**Тип:** Действие, возращающее значение\
**Описание:** Получает блоки, которые может ломать предмет и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_destroyable_blocks(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_destroyable_blocks();

//Или в сухую позиционно

variable::get_item_destroyable_blocks(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_destroyable_blocks(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| item     | Предмет              | Предмет                   |

<h3 id=set_variable_get_item_durability>
  <code>variable::get_item_durability</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить прочность предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной прочность указанного предмета.

**Пример использования:**
```ts
`variable` = variable::get_item_durability(item("stick"), "DAMAGE");

//Или от объекта

`variable` = item("stick").get_item_durability("DAMAGE");

//Или в сухую позиционно

variable::get_item_durability(`variable`, item("stick"), "DAMAGE");

//Или в сухую по ключам

variable::get_item_durability(variable=`variable`, item=item("stick"), durability_type="DAMAGE");
```

**Аргументы:**

| ID              | Тип                                                                                                                                                                                                                                           | Описание                  |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable        | Переменная\[Число\]                                                                                                                                                                                                                           | Переменная для присвоения |
| item            | Предмет                                                                                                                                                                                                                                       | Предмет                   |
| durability_type | Маркер<br/>**DAMAGE** - Текущая прочность<br/>**DAMAGE_PERCENTAGE** - Текущий процент прочности<br/>**MAXIMUM** - Максимальная прочность<br/>**REMAINING** - Остаточная прочность<br/>**REMAINING_PERCENTAGE** - Остаточный процент прочности | Тип прочности             |

<h3 id=set_variable_get_item_effective_name>
  <code>variable::get_item_effective_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить отображаемое в инвентаре имя предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает имя предмета, в том виде, в котором оно отображается в инвентаре, и присваивает его к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Возвращаемый текст создается из нескольких частей, которые влияют на отображаемое имя, в том числе из редкости и переводимого имени предмета.

**Пример использования:**
```ts
`variable` = variable::get_item_effective_name(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_effective_name();

//Или в сухую позиционно

variable::get_item_effective_name(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_effective_name(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_enchantments>
  <code>variable::get_item_enchantments</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить зачарования предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной словарь зачарований и их уровней предмета.

**Пример использования:**
```ts
`variable` = variable::get_item_enchantments(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_enchantments();

//Или в сухую позиционно

variable::get_item_enchantments(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_enchantments(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Словарь\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |

<h3 id=set_variable_get_item_food_properties>
  <code>variable::get_item_food_properties</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить значение компонента еды предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение компонента еды предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_food_properties(item("stick"), "");

//Или от объекта

`variable` = item("stick").get_item_food_properties("");

//Или в сухую позиционно

variable::get_item_food_properties(`variable`, item("stick"), "");

//Или в сухую по ключам

variable::get_item_food_properties(variable=`variable`, item=item("stick"), property="");
```

**Аргументы:**

| ID       | Тип                                                                                                       | Описание                  |
|----------|-----------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                                                                       | Переменная для присвоения |
| item     | Предмет                                                                                                   | Предмет                   |
| property | Маркер<br/>**** - creative_plus.action.set_variable_get_item_food_properties.argument.property.enum..name | Значение                  |

<h3 id=set_variable_get_item_lore>
  <code>variable::get_item_lore</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить описание предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной текст описания предмета.

**Пример использования:**
```ts
`variable` = variable::get_item_lore(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_lore();

//Или в сухую позиционно

variable::get_item_lore(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_lore(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| item     | Предмет              | Предмет                   |

<h3 id=set_variable_get_item_lore_line>
  <code>variable::get_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить строку описания предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной строку описания предмета.

**Пример использования:**
```ts
`variable` = variable::get_item_lore_line(item("stick"), 1);

//Или от объекта

`variable` = item("stick").get_item_lore_line(1);

//Или в сухую позиционно

variable::get_item_lore_line(`variable`, item("stick"), 1);

//Или в сухую по ключам

variable::get_item_lore_line(variable=`variable`, item=item("stick"), line=1);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |
| line     | Число               | Номер строки              |

<h3 id=set_variable_get_item_max_stack_size>
  <code>variable::get_item_max_stack_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить максимальное количество предметов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной максимально возможное количество предметов в стаке.

**Пример использования:**
```ts
`variable` = variable::get_item_max_stack_size(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_max_stack_size();

//Или в сухую позиционно

variable::get_item_max_stack_size(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_max_stack_size(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_model_data>
  <code>variable::get_item_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить модель предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает модель указанного предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_model_data(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_model_data();

//Или в сухую позиционно

variable::get_item_model_data(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_model_data(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_name>
  <code>variable::get_item_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить имя предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной отображаемое имя предмета.

**Пример использования:**
```ts
`variable` = variable::get_item_name(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_name();

//Или в сухую позиционно

variable::get_item_name(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_name(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_nbt_tags>
  <code>variable::get_item_nbt_tags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить данные о предмете\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной данные об указанном предмете.

**Пример использования:**
```ts
`variable` = variable::get_item_nbt_tags(item("stick"), "ALL");

//Или от объекта

`variable` = item("stick").get_item_nbt_tags("ALL");

//Или в сухую позиционно

variable::get_item_nbt_tags(`variable`, item("stick"), "ALL");

//Или в сухую по ключам

variable::get_item_nbt_tags(variable=`variable`, item=item("stick"), fetch_mode="ALL");
```

**Аргументы:**

| ID         | Тип                                                           | Описание                  |
|------------|---------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Словарь\]                                         | Переменная для присвоения |
| item       | Предмет                                                       | Предмет                   |
| fetch_mode | Маркер<br/>**ALL** - Все<br/>**CUSTOM_DATA** - Кастомные теги | Тип данных                |

<h3 id=set_variable_get_item_placeable_blocks>
  <code>variable::get_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить блоки для установки предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает блоки, на которые может быть установлен предмет и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_placeable_blocks(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_placeable_blocks();

//Или в сухую позиционно

variable::get_item_placeable_blocks(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_placeable_blocks(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| item     | Предмет              | Предмет                   |

<h3 id=set_variable_get_item_potion_effects>
  <code>variable::get_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить эффекты зелий из предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает эффекты зелий из предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_potion_effects(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_potion_effects();

//Или в сухую позиционно

variable::get_item_potion_effects(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_potion_effects(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| item     | Предмет              | Предмет                   |

<h3 id=set_variable_get_item_rarity>
  <code>variable::get_item_rarity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить редкость предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает редкость предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_rarity(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_rarity();

//Или в сухую позиционно

variable::get_item_rarity(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_rarity(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_tooltip_style>
  <code>variable::get_item_tooltip_style</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить стиль всплывающей подсказки предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает стиль всплывающей подсказки предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_tooltip_style(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_tooltip_style();

//Или в сухую позиционно

variable::get_item_tooltip_style(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_tooltip_style(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| item     | Предмет             | Предмет                   |

<h3 id=set_variable_get_item_type>
  <code>variable::get_item_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной тип предмета, представленный в виде текста.

**Пример использования:**
```ts
`variable` = variable::get_item_type(item("stick"), "ID");

//Или от объекта

`variable` = item("stick").get_item_type("ID");

//Или в сухую позиционно

variable::get_item_type(`variable`, item("stick"), "ID");

//Или в сухую по ключам

variable::get_item_type(variable=`variable`, type=item("stick"), value="ID");
```

**Аргументы:**

| ID       | Тип                                                                                | Описание                  |
|----------|------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Текст\]                                                                | Переменная для присвоения |
| type     | Предмет                                                                            | Предмет                   |
| value    | Маркер<br/>**ID** - ID предмета<br/>**ITEM** - Предмет<br/>**NAME** - Имя предмета | Текстовое представление   |

<h3 id=set_variable_get_item_use_remainder>
  <code>variable::get_item_use_remainder</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить превращение предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает предмет, в который превратится указанный предмет после использования и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_use_remainder(item("stick"));

//Или от объекта

`variable` = item("stick").get_item_use_remainder();

//Или в сухую позиционно

variable::get_item_use_remainder(`variable`, item("stick"));

//Или в сухую по ключам

variable::get_item_use_remainder(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |

<h3 id=set_variable_get_item_weapon>
  <code>variable::get_item_weapon</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить значение компонента оружия предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение компонента оружия предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_item_weapon(item("stick"), "ITEM_DAMAGE_PER_ATTACK");

//Или от объекта

`variable` = item("stick").get_item_weapon("ITEM_DAMAGE_PER_ATTACK");

//Или в сухую позиционно

variable::get_item_weapon(`variable`, item("stick"), "ITEM_DAMAGE_PER_ATTACK");

//Или в сухую по ключам

variable::get_item_weapon(variable=`variable`, item=item("stick"), property="ITEM_DAMAGE_PER_ATTACK");
```

**Аргументы:**

| ID       | Тип                                                                                                        | Описание                  |
|----------|------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                                                                        | Переменная для присвоения |
| item     | Предмет                                                                                                    | Предмет                   |
| property | Маркер<br/>**ITEM_DAMAGE_PER_ATTACK** - Урон от атаки<br/>**DISABLE_BLOCKING** - Задержка щита после удара | Значение                  |

<h3 id=set_variable_get_items_by_tag>
  <code>variable::get_items_by_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить предметы по Minecraft-тегу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает предметы по Minecraft-тегу (например, "swords") и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_items_by_tag("namespace", "ID");

//Или в сухую позиционно

variable::get_items_by_tag(`variable`, "namespace", "ID");

//Или в сухую по ключам

variable::get_items_by_tag(variable=`variable`, namespace="namespace", result_type="ID");
```

**Аргументы:**

| ID          | Тип                                                                                                            | Описание                  |
|-------------|----------------------------------------------------------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Список\]                                                                                           | Переменная для присвоения |
| namespace   | Текст                                                                                                          | Minecraft-тег             |
| result_type | Маркер<br/>**ID** - ID предмета<br/>**TRANSLATION_KEY** - Переводимое название предмета<br/>**ITEM** - Предмет | Тип результата            |

<h3 id=set_variable_get_lectern_book>
  <code>variable::get_lectern_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить книгу с кафедры\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной книгу с кафедры на указанном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_lectern_book(location(0,0,0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).get_lectern_book();

//Или в сухую позиционно

variable::get_lectern_book(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_lectern_book(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| location | Местоположение        | Местоположение блока      |

<h3 id=set_variable_get_lectern_page>
  <code>variable::get_lectern_page</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить страницу книги с кафедры\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной номер текущей страницы книги с кафедры на указанном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_lectern_page(location(0,0,0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).get_lectern_page();

//Или в сухую позиционно

variable::get_lectern_page(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_lectern_page(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| location | Местоположение      | Местоположение блока      |

<h3 id=set_variable_get_light_level>
  <code>variable::get_light_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить уровень освещения\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение уровня освещения на указанном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_light_level(location(0,0,0,0,0), "BLOCKS");

//Или от объекта

`variable` = location(0,0,0,0,0).get_light_level("BLOCKS");

//Или в сухую позиционно

variable::get_light_level(`variable`, location(0,0,0,0,0), "BLOCKS");

//Или в сухую по ключам

variable::get_light_level(variable=`variable`, location=location(0,0,0,0,0), value_type="BLOCKS");
```

**Аргументы:**

| ID         | Тип                                                                                                | Описание                          |
|------------|----------------------------------------------------------------------------------------------------|-----------------------------------|
| variable   | Переменная\[Число\]                                                                                | Переменная для присвоения         |
| location   | Местоположение                                                                                     | Местоположение получения значения |
| value_type | Маркер<br/>**BLOCKS** - Свет от блоков<br/>**SKY** - Свет от неба<br/>**TOTAL** - Полное освещение | Тип освещения                     |

<h3 id=set_variable_get_list_index_of_value>
  <code>variable::get_list_index_of_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить индекс значения списка\
**Тип:** Действие, возращающее значение\
**Описание:** Выполняет поиск значения в списке и получает его индекс, если он найден. В случае неудачи возвращает -1.

**Пример использования:**
```ts
`variable` = variable::get_list_index_of_value([`list`, `list`], "any value", "FIRST");

//Или от объекта

`variable` = [`list`, `list`].get_list_index_of_value("any value", "FIRST");

//Или в сухую позиционно

variable::get_list_index_of_value(`variable`, [`list`, `list`], "any value", "FIRST");

//Или в сухую по ключам

variable::get_list_index_of_value(variable=`variable`, list=[`list`, `list`], value="any value", search_mode="FIRST");
```

**Аргументы:**

| ID          | Тип                                                                                                         | Описание                  |
|-------------|-------------------------------------------------------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Число\]                                                                                         | Переменная для присвоения |
| list        | Список                                                                                                      | Список                    |
| value       | Любое значение                                                                                              | Значение                  |
| search_mode | Маркер<br/>**FIRST** - С начала (получить первый индекс)<br/>**LAST** - С конца (получить последний индекс) | Режим поиска              |

<h3 id=set_variable_get_list_length>
  <code>variable::get_list_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить размер списка\
**Тип:** Действие, возращающее значение\
**Описание:** Получает количество элементов, содержащихся в указанном списке.

**Пример использования:**
```ts
`variable` = variable::get_list_length([`list`, `list`]);

//Или от объекта

`variable` = [`list`, `list`].get_list_length();

//Или в сухую позиционно

variable::get_list_length(`variable`, [`list`, `list`]);

//Или в сухую по ключам

variable::get_list_length(variable=`variable`, list=[`list`, `list`]);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| list     | Список              | Список                    |

<h3 id=set_variable_get_list_random_value>
  <code>variable::get_list_random_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить случайное значение списка\
**Тип:** Действие, возращающее значение\
**Описание:** Получает случайное значение из списка.

**Пример использования:**
```ts
`variable` = variable::get_list_random_value([`list`, `list`]);

//Или от объекта

`variable` = [`list`, `list`].get_list_random_value();

//Или в сухую позиционно

variable::get_list_random_value(`variable`, [`list`, `list`]);

//Или в сухую по ключам

variable::get_list_random_value(variable=`variable`, list=[`list`, `list`]);
```

**Аргументы:**

| ID       | Тип                          | Описание                  |
|----------|------------------------------|---------------------------|
| variable | Переменная\[Любое значение\] | Переменная для присвоения |
| list     | Список                       | Список                    |

<h3 id=set_variable_get_list_value>
  <code>variable::get_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить значение из списка\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение из списка по указанному индексу.

**Пример использования:**
```ts
`variable` = variable::get_list_value([`list`, `list`], 1, "any value");

//Или от объекта

`variable` = [`list`, `list`].get_list_value(1, "any value");

//Или в сухую позиционно

variable::get_list_value(`variable`, [`list`, `list`], 1, "any value");

//Или в сухую по ключам

variable::get_list_value(variable=`variable`, list=[`list`, `list`], number=1, default_value="any value");
```

**Аргументы:**

| ID            | Тип                          | Описание                  |
|---------------|------------------------------|---------------------------|
| variable      | Переменная\[Любое значение\] | Переменная для присвоения |
| list          | Список                       | Список                    |
| number        | Число                        | Индекс                    |
| default_value | Любое значение               | Значение по умолчанию     |

<h3 id=set_variable_get_list_variables>
  <code>variable::get_list_variables</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить имена переменных\
**Тип:** Действие, возращающее значение\
**Описание:** Получает список имён всех переменных и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_list_variables(["names", "names"], "GAME", "EQUALS", "TRUE");

//Или в сухую позиционно

variable::get_list_variables(`variable`, ["names", "names"], "GAME", "EQUALS", "TRUE");

//Или в сухую по ключам

variable::get_list_variables(variable=`variable`, names=["names", "names"], scope="GAME", match="EQUALS", ignore_case="TRUE");
```

**Аргументы:**

| ID          | Тип                                                                                                                                                                                          | Описание                  |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Список\]                                                                                                                                                                         | Переменная для присвоения |
| names       | Message 'actions.array' not found in 'ru_RU'\[Текст\]                                                                                                                                        | Имена переменных          |
| scope       | Маркер<br/>**GAME** - Игровые<br/>**SAVE** - Сохранённые<br/>**LOCAL** - Локальные                                                                                                           | Тип переменных            |
| match       | Маркер<br/>**EQUALS** - Точное соответствие<br/>**NAME_CONTAINS** - Содержит<br/>**PART_CONTAINS** - Содержит часть<br/>**STARTS_WITH** - Начинается на<br/>**ENDS_WITH** - Заканчивается на | Вид сравнения             |
| ignore_case | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет                                                                                                                                                 | Игнорировать регистр      |

<h3 id=set_variable_get_location_direction>
  <code>variable::get_location_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить направление местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной направления местоположения.

**Пример использования:**
```ts
`variable` = variable::get_location_direction(location(0,0,0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).get_location_direction();

//Или в сухую позиционно

variable::get_location_direction(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_location_direction(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                  | Описание                     |
|----------|----------------------|------------------------------|
| variable | Переменная\[Вектор\] | Переменная для присвоения    |
| location | Местоположение       | Местоположение для получения |

<h3 id=set_variable_get_map_key_by_index>
  <code>variable::get_map_key_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить ключ словаря по индексу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает ключ по индексу и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_map_key_by_index({"map":`map`}, 1, "any value");

//Или от объекта

`variable` = {"map":`map`}.get_map_key_by_index(1, "any value");

//Или в сухую позиционно

variable::get_map_key_by_index(`variable`, {"map":`map`}, 1, "any value");

//Или в сухую по ключам

variable::get_map_key_by_index(variable=`variable`, map={"map":`map`}, index=1, default_value="any value");
```

**Аргументы:**

| ID            | Тип                          | Описание                    |
|---------------|------------------------------|-----------------------------|
| variable      | Переменная\[Любое значение\] | Переменная для присвоения   |
| map           | Словарь                      | Словарь для получения ключа |
| index         | Число                        | Индекс ключа                |
| default_value | Любое значение               | Значение по умолчанию       |

<h3 id=set_variable_get_map_keys>
  <code>variable::get_map_keys</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить список ключей словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной список ключей словаря.

**Пример использования:**
```ts
`variable` = variable::get_map_keys({"map":`map`});

//Или от объекта

`variable` = {"map":`map`}.get_map_keys();

//Или в сухую позиционно

variable::get_map_keys(`variable`, {"map":`map`});

//Или в сухую по ключам

variable::get_map_keys(variable=`variable`, map={"map":`map`});
```

**Аргументы:**

| ID       | Тип                  | Описание                       |
|----------|----------------------|--------------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения      |
| map      | Словарь              | Словарь для получения значения |

<h3 id=set_variable_get_map_keys_by_value>
  <code>variable::get_map_keys_by_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить ключи словаря по значению\
**Тип:** Действие, возращающее значение\
**Описание:** Получает ключ либо список ключей словаря по значению и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_map_keys_by_value({"map":`map`}, "any value", "any value", "ALL");

//Или от объекта

`variable` = {"map":`map`}.get_map_keys_by_value("any value", "any value", "ALL");

//Или в сухую позиционно

variable::get_map_keys_by_value(`variable`, {"map":`map`}, "any value", "any value", "ALL");

//Или в сухую по ключам

variable::get_map_keys_by_value(variable=`variable`, map={"map":`map`}, value="any value", default_value="any value", find_mode="ALL");
```

**Аргументы:**

| ID            | Тип                                                                                                                                            | Описание                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable      | Переменная\[Список\]                                                                                                                           | Переменная для присвоения |
| map           | Словарь                                                                                                                                        | Словарь                   |
| value         | Любое значение                                                                                                                                 | Значение для получения    |
| default_value | Любое значение                                                                                                                                 | Значение по умолчанию     |
| find_mode     | Маркер<br/>**ALL** - Все (получает все ключи)<br/>**FIRST** - С начала (получает первый ключ)<br/>**LAST** - С конца (получает последний ключ) | Режим поиска              |

<h3 id=set_variable_get_map_size>
  <code>variable::get_map_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить размер словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение размера словаря.

**Пример использования:**
```ts
`variable` = variable::get_map_size({"map":`map`});

//Или от объекта

`variable` = {"map":`map`}.get_map_size();

//Или в сухую позиционно

variable::get_map_size(`variable`, {"map":`map`});

//Или в сухую по ключам

variable::get_map_size(variable=`variable`, map={"map":`map`});
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| map      | Словарь             | Словарь                   |

<h3 id=set_variable_get_map_value>
  <code>variable::get_map_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить значение словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённое значение словаря по ключу и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_map_value({"map":`map`}, "any value", "any value");

//Или от объекта

`variable` = {"map":`map`}.get_map_value("any value", "any value");

//Или в сухую позиционно

variable::get_map_value(`variable`, {"map":`map`}, "any value", "any value");

//Или в сухую по ключам

variable::get_map_value(variable=`variable`, map={"map":`map`}, key="any value", default_value="any value");
```

**Аргументы:**

| ID            | Тип                          | Описание                  |
|---------------|------------------------------|---------------------------|
| variable      | Переменная\[Любое значение\] | Переменная для присвоения |
| map           | Словарь                      | Словарь для изменения     |
| key           | Любое значение               | Ключ                      |
| default_value | Любое значение               | Значение по умолчанию     |

<h3 id=set_variable_get_map_value_by_index>
  <code>variable::get_map_value_by_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить значение словаря по индексу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает значение по индексу и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_map_value_by_index({"map":`map`}, 1, "any value");

//Или от объекта

`variable` = {"map":`map`}.get_map_value_by_index(1, "any value");

//Или в сухую позиционно

variable::get_map_value_by_index(`variable`, {"map":`map`}, 1, "any value");

//Или в сухую по ключам

variable::get_map_value_by_index(variable=`variable`, map={"map":`map`}, index=1, default_value="any value");
```

**Аргументы:**

| ID            | Тип                          | Описание                       |
|---------------|------------------------------|--------------------------------|
| variable      | Переменная\[Любое значение\] | Переменная для присвоения      |
| map           | Словарь                      | Словарь для получения значения |
| index         | Число                        | Индекс значения                |
| default_value | Любое значение               | Значение по умолчанию          |

<h3 id=set_variable_get_map_values>
  <code>variable::get_map_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить список значений словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной список значений словаря.

**Пример использования:**
```ts
`variable` = variable::get_map_values({"map":`map`});

//Или от объекта

`variable` = {"map":`map`}.get_map_values();

//Или в сухую позиционно

variable::get_map_values(`variable`, {"map":`map`});

//Или в сухую по ключам

variable::get_map_values(variable=`variable`, map={"map":`map`});
```

**Аргументы:**

| ID       | Тип                  | Описание                       |
|----------|----------------------|--------------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения      |
| map      | Словарь              | Словарь для получения значения |

<h3 id=set_variable_get_midpoint_between_vectors>
  <code>variable::get_midpoint_between_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить центральное значение между векторами\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной центральное значение между двумя векторами.

**Пример использования:**
```ts
`variable` = variable::get_midpoint_between_vectors(vector(0,0,0), vector(0,0,0));

//Или в сухую позиционно

variable::get_midpoint_between_vectors(`variable`, vector(0,0,0), vector(0,0,0));

//Или в сухую по ключам

variable::get_midpoint_between_vectors(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0));
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Вектор\] | Переменная для присвоения |
| vector_1 | Вектор               | Первый вектор             |
| vector_2 | Вектор               | Второй вектор             |

<h3 id=set_variable_get_particle_amount>
  <code>variable::get_particle_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить количество частиц\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение количества частиц.

**Пример использования:**
```ts
`variable` = variable::get_particle_amount(particle("fire"));

//Или от объекта

`variable` = particle("fire").get_particle_amount();

//Или в сухую позиционно

variable::get_particle_amount(`variable`, particle("fire"));

//Или в сухую по ключам

variable::get_particle_amount(variable=`variable`, particle=particle("fire"));
```

**Аргументы:**

| ID       | Тип                 | Описание                       |
|----------|---------------------|--------------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения      |
| particle | Эффект частиц       | Частица для получения значения |

<h3 id=set_variable_get_particle_color>
  <code>variable::get_particle_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить цвет частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение цвета частицы.

**Пример использования:**
```ts
`variable` = variable::get_particle_color(particle("fire"), "COLOR");

//Или от объекта

`variable` = particle("fire").get_particle_color("COLOR");

//Или в сухую позиционно

variable::get_particle_color(`variable`, particle("fire"), "COLOR");

//Или в сухую по ключам

variable::get_particle_color(variable=`variable`, particle=particle("fire"), color_type="COLOR");
```

**Аргументы:**

| ID         | Тип                                                                  | Описание                       |
|------------|----------------------------------------------------------------------|--------------------------------|
| variable   | Переменная\[Текст\]                                                  | Переменная для присвоения      |
| particle   | Эффект частиц                                                        | Частица для получения значения |
| color_type | Маркер<br/>**COLOR** - Обычный цвет<br/>**TO_COLOR** - Цвет перехода | Тип цвета                      |

<h3 id=set_variable_get_particle_material>
  <code>variable::get_particle_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить материал частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение материала частицы.

**Пример использования:**
```ts
`variable` = variable::get_particle_material(particle("fire"));

//Или от объекта

`variable` = particle("fire").get_particle_material();

//Или в сухую позиционно

variable::get_particle_material(`variable`, particle("fire"));

//Или в сухую по ключам

variable::get_particle_material(variable=`variable`, particle=particle("fire"));
```

**Аргументы:**

| ID       | Тип                 | Описание                       |
|----------|---------------------|--------------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения      |
| particle | Эффект частиц       | Частица для получения значения |

<h3 id=set_variable_get_particle_offset>
  <code>variable::get_particle_offset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить движение частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение движения частицы.

**Пример использования:**
```ts
`variable` = variable::get_particle_offset(particle("fire"));

//Или от объекта

`variable` = particle("fire").get_particle_offset();

//Или в сухую позиционно

variable::get_particle_offset(`variable`, particle("fire"));

//Или в сухую по ключам

variable::get_particle_offset(variable=`variable`, particle=particle("fire"));
```

**Аргументы:**

| ID       | Тип                  | Описание                       |
|----------|----------------------|--------------------------------|
| variable | Переменная\[Вектор\] | Переменная для присвоения      |
| particle | Эффект частиц        | Частица для получения значения |

<h3 id=set_variable_get_particle_size>
  <code>variable::get_particle_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить размер частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение размера частицы.

**Пример использования:**
```ts
`variable` = variable::get_particle_size(particle("fire"));

//Или от объекта

`variable` = particle("fire").get_particle_size();

//Или в сухую позиционно

variable::get_particle_size(`variable`, particle("fire"));

//Или в сухую по ключам

variable::get_particle_size(variable=`variable`, particle=particle("fire"));
```

**Аргументы:**

| ID       | Тип                 | Описание                       |
|----------|---------------------|--------------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения      |
| particle | Эффект частиц       | Частица для получения значения |

<h3 id=set_variable_get_particle_spread>
  <code>variable::get_particle_spread</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить разброс частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение разброса частицы.

**Пример использования:**
```ts
`variable` = variable::get_particle_spread(particle("fire"), "HORIZONTAL");

//Или от объекта

`variable` = particle("fire").get_particle_spread("HORIZONTAL");

//Или в сухую позиционно

variable::get_particle_spread(`variable`, particle("fire"), "HORIZONTAL");

//Или в сухую по ключам

variable::get_particle_spread(variable=`variable`, particle=particle("fire"), type="HORIZONTAL");
```

**Аргументы:**

| ID       | Тип                                                                        | Описание                       |
|----------|----------------------------------------------------------------------------|--------------------------------|
| variable | Переменная\[Число\]                                                        | Переменная для присвоения      |
| particle | Эффект частиц                                                              | Частица для получения значения |
| type     | Маркер<br/>**HORIZONTAL** - Горизонтальная<br/>**VERTICAL** - Вертикальная | Плоскость разброса             |

<h3 id=set_variable_get_particle_type>
  <code>variable::get_particle_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение типа частицы.

**Пример использования:**
```ts
`variable` = variable::get_particle_type(particle("fire"));

//Или от объекта

`variable` = particle("fire").get_particle_type();

//Или в сухую позиционно

variable::get_particle_type(`variable`, particle("fire"));

//Или в сухую по ключам

variable::get_particle_type(variable=`variable`, particle=particle("fire"));
```

**Аргументы:**

| ID       | Тип                 | Описание                       |
|----------|---------------------|--------------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения      |
| particle | Эффект частиц       | Частица для получения значения |

<h3 id=set_variable_get_player_head>
  <code>variable::get_player_head</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить голову игрока\
**Тип:** Действие, возращающее значение\
**Описание:** Получает голову игрока в виде предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_player_head("name_or_uuid", "NAME_OR_UUID");

//Или в сухую позиционно

variable::get_player_head(`variable`, "name_or_uuid", "NAME_OR_UUID");

//Или в сухую по ключам

variable::get_player_head(variable=`variable`, name_or_uuid="name_or_uuid", receive_type="NAME_OR_UUID");
```

**Аргументы:**

| ID           | Тип                                                                                    | Описание                  |
|--------------|----------------------------------------------------------------------------------------|---------------------------|
| variable     | Переменная\[Предмет\]                                                                  | Переменная для присвоения |
| name_or_uuid | Текст                                                                                  | Значение                  |
| receive_type | Маркер<br/>**NAME_OR_UUID** - Имя или UUID игрока<br/>**VALUE** - Параметр value скина | Тип значения              |

<h3 id=set_variable_get_player_head_owner>
  <code>variable::get_player_head_owner</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить владельца головы\
**Тип:** Действие, возращающее значение\
**Описание:** Получает имя или UUID владельца головы и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_player_head_owner(item("stick"), "NAME");

//Или от объекта

`variable` = item("stick").get_player_head_owner("NAME");

//Или в сухую позиционно

variable::get_player_head_owner(`variable`, item("stick"), "NAME");

//Или в сухую по ключам

variable::get_player_head_owner(variable=`variable`, head=item("stick"), return_value="NAME");
```

**Аргументы:**

| ID           | Тип                                                                                                    | Описание                  |
|--------------|--------------------------------------------------------------------------------------------------------|---------------------------|
| variable     | Переменная\[Текст\]                                                                                    | Переменная для присвоения |
| head         | Предмет                                                                                                | Голова игрока             |
| return_value | Маркер<br/>**NAME** - Имя владельца<br/>**UUID** - UUID владельца<br/>**VALUE** - Параметр value скина | Возвращаемое значение     |

<h3 id=set_variable_get_player_head_value>
  <code>variable::get_player_head_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить владельца головы на местоположении\
**Тип:** Действие, возращающее значение\
**Описание:** Получает имя или UUID владельца головы на местоположении и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_player_head_value(location(0,0,0,0,0), "NAME");

//Или от объекта

`variable` = location(0,0,0,0,0).get_player_head_value("NAME");

//Или в сухую позиционно

variable::get_player_head_value(`variable`, location(0,0,0,0,0), "NAME");

//Или в сухую по ключам

variable::get_player_head_value(variable=`variable`, location=location(0,0,0,0,0), return_value="NAME");
```

**Аргументы:**

| ID           | Тип                                                                                                    | Описание                  |
|--------------|--------------------------------------------------------------------------------------------------------|---------------------------|
| variable     | Переменная\[Текст\]                                                                                    | Переменная для присвоения |
| location     | Местоположение                                                                                         | Местоположение головы     |
| return_value | Маркер<br/>**NAME** - Имя владельца<br/>**UUID** - UUID владельца<br/>**VALUE** - Параметр value скина | Возвращаемое значение     |

<h3 id=set_variable_get_potion_effect_amplifier>
  <code>variable::get_potion_effect_amplifier</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить силу зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение силы зелья.

**Пример использования:**
```ts
`variable` = variable::get_potion_effect_amplifier(potion("slow_falling"));

//Или от объекта

`variable` = potion("slow_falling").get_potion_effect_amplifier();

//Или в сухую позиционно

variable::get_potion_effect_amplifier(`variable`, potion("slow_falling"));

//Или в сухую по ключам

variable::get_potion_effect_amplifier(variable=`variable`, potion=potion("slow_falling"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| potion   | Зелье               | Зелье                     |

<h3 id=set_variable_get_potion_effect_duration>
  <code>variable::get_potion_effect_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить длительность зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение длительности зелья.

**Пример использования:**
```ts
`variable` = variable::get_potion_effect_duration(potion("slow_falling"));

//Или от объекта

`variable` = potion("slow_falling").get_potion_effect_duration();

//Или в сухую позиционно

variable::get_potion_effect_duration(`variable`, potion("slow_falling"));

//Или в сухую по ключам

variable::get_potion_effect_duration(variable=`variable`, potion=potion("slow_falling"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| potion   | Зелье               | Зелье                     |

<h3 id=set_variable_get_potion_effect_type>
  <code>variable::get_potion_effect_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение типа зелья.

**Пример использования:**
```ts
`variable` = variable::get_potion_effect_type(potion("slow_falling"));

//Или от объекта

`variable` = potion("slow_falling").get_potion_effect_type();

//Или в сухую позиционно

variable::get_potion_effect_type(`variable`, potion("slow_falling"));

//Или в сухую по ключам

variable::get_potion_effect_type(variable=`variable`, potion=potion("slow_falling"));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| potion   | Зелье               | Зелье                     |

<h3 id=set_variable_get_sculk_shrieker_warning_level>
  <code>variable::get_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить уровень опасности скалк-крикуна\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной уровень опасности скалк-крикуна на указанном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_sculk_shrieker_warning_level(location(0,0,0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).get_sculk_shrieker_warning_level();

//Или в сухую позиционно

variable::get_sculk_shrieker_warning_level(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_sculk_shrieker_warning_level(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                 | Описание                     |
|----------|---------------------|------------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения    |
| location | Местоположение      | Местоположение скалк-крикуна |

<h3 id=set_variable_get_sign_text>
  <code>variable::get_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить текст строки таблички\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение текста строки таблички на выбранном местоположении.

**Пример использования:**
```ts
`variable` = variable::get_sign_text(location(0,0,0,0,0), "ALL", "ALL");

//Или от объекта

`variable` = location(0,0,0,0,0).get_sign_text("ALL", "ALL");

//Или в сухую позиционно

variable::get_sign_text(`variable`, location(0,0,0,0,0), "ALL", "ALL");

//Или в сухую по ключам

variable::get_sign_text(variable=`variable`, location=location(0,0,0,0,0), check_side="ALL", sign_line="ALL");
```

**Аргументы:**

| ID         | Тип                                                                                                                                                          | Описание                  |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Текст\]                                                                                                                                          | Переменная для присвоения |
| location   | Местоположение                                                                                                                                               | Местоположение таблички   |
| check_side | Маркер<br/>**ALL** - Все<br/>**BACK** - Задняя<br/>**FRONT** - Передняя                                                                                      | Сторона таблички          |
| sign_line  | Маркер<br/>**ALL** - Все строки<br/>**FIRST** - Первая строка<br/>**FOURTH** - Четвёртая строка<br/>**SECOND** - Вторая строка<br/>**THIRD** - Третья строка | Номер строки              |

<h3 id=set_variable_get_sound_pitch>
  <code>variable::get_sound_pitch</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить высоту звука\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение высоты звука.

**Пример использования:**
```ts
`variable` = variable::get_sound_pitch(sound("entity.zombie.hurt"));

//Или от объекта

`variable` = sound("entity.zombie.hurt").get_sound_pitch();

//Или в сухую позиционно

variable::get_sound_pitch(`variable`, sound("entity.zombie.hurt"));

//Или в сухую по ключам

variable::get_sound_pitch(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения   |
| sound    | Звук                | Звук для получения значения |

<h3 id=set_variable_get_sound_source>
  <code>variable::get_sound_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить источник звука\
**Тип:** Действие, возращающее значение\
**Описание:** Получает источник звука и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_sound_source(sound("entity.zombie.hurt"));

//Или от объекта

`variable` = sound("entity.zombie.hurt").get_sound_source();

//Или в сухую позиционно

variable::get_sound_source(`variable`, sound("entity.zombie.hurt"));

//Или в сухую по ключам

variable::get_sound_source(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения   |
| sound    | Звук                | Звук для получения значения |

<h3 id=set_variable_get_sound_type>
  <code>variable::get_sound_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить тип звука\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение типа звука.

**Пример использования:**
```ts
`variable` = variable::get_sound_type(sound("entity.zombie.hurt"));

//Или от объекта

`variable` = sound("entity.zombie.hurt").get_sound_type();

//Или в сухую позиционно

variable::get_sound_type(`variable`, sound("entity.zombie.hurt"));

//Или в сухую по ключам

variable::get_sound_type(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения   |
| sound    | Звук                | Звук для получения значения |

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
`variable` = variable::get_sound_variation(sound("entity.zombie.hurt"));

//Или от объекта

`variable` = sound("entity.zombie.hurt").get_sound_variation();

//Или в сухую позиционно

variable::get_sound_variation(`variable`, sound("entity.zombie.hurt"));

//Или в сухую по ключам

variable::get_sound_variation(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения   |
| sound    | Звук                | Звук для получения значения |

<h3 id=set_variable_get_sound_variations>
  <code>variable::get_sound_variations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить вариации звука\
**Тип:** Действие, возращающее значение\
**Описание:** Получает список всех вариаций звука и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_sound_variations(sound("entity.zombie.hurt"));

//Или от объекта

`variable` = sound("entity.zombie.hurt").get_sound_variations();

//Или в сухую позиционно

variable::get_sound_variations(`variable`, sound("entity.zombie.hurt"));

//Или в сухую по ключам

variable::get_sound_variations(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Аргументы:**

| ID       | Тип                  | Описание                    |
|----------|----------------------|-----------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения   |
| sound    | Звук                 | Звук для получения значений |

<h3 id=set_variable_get_sound_volume_action>
  <code>variable::get_sound_volume_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить громкость звука\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение громкости звука.

**Пример использования:**
```ts
`variable` = variable::get_sound_volume_action(sound("entity.zombie.hurt"));

//Или от объекта

`variable` = sound("entity.zombie.hurt").get_sound_volume_action();

//Или в сухую позиционно

variable::get_sound_volume_action(`variable`, sound("entity.zombie.hurt"));

//Или в сухую по ключам

variable::get_sound_volume_action(variable=`variable`, sound=sound("entity.zombie.hurt"));
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения   |
| sound    | Звук                | Звук для получения значения |

<h3 id=set_variable_get_template_code>
  <code>variable::get_template_code</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить код из шаблона\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной код из шаблона.

**Пример использования:**
```ts
`variable` = variable::get_template_code(item("stick"), "MAP");

//Или от объекта

`variable` = item("stick").get_template_code("MAP");

//Или в сухую позиционно

variable::get_template_code(`variable`, item("stick"), "MAP");

//Или в сухую по ключам

variable::get_template_code(variable=`variable`, template=item("stick"), return_type="MAP");
```

**Аргументы:**

| ID          | Тип                                                    | Описание                  |
|-------------|--------------------------------------------------------|---------------------------|
| variable    | Переменная\[Любое значение\]                           | Переменная для присвоения |
| template    | Предмет                                                | Шаблон                    |
| return_type | Маркер<br/>**MAP** - Словарь<br/>**TEXT** - Текст JSON | Возвращаемое значение     |

<h3 id=set_variable_get_text_regex_groups>
  <code>variable::get_text_regex_groups</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Разобрать по регулярному выражению\
**Тип:** Действие, возращающее значение\
**Описание:** Разбирает текст по регулярному выражению и присваивает к переменной нахождения с содержимым всех групп захвата или содержимое определённых групп.

**Пример использования:**
```ts
`variable` = variable::get_text_regex_groups("text", "regex", "group", "ALL", "INDEX", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE");

//Или от объекта

`variable` = "text".get_text_regex_groups("regex", "group", "ALL", "INDEX", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE");

//Или в сухую позиционно

variable::get_text_regex_groups(`variable`, "text", "regex", "group", "ALL", "INDEX", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE");

//Или в сухую по ключам

variable::get_text_regex_groups(variable=`variable`, text="text", regex="regex", group="group", match_mode="ALL", get_group_by="INDEX", ignore_case="TRUE", multiline="TRUE", literal="TRUE", unix_lines="TRUE", comments="TRUE", dot_matches_all="TRUE", cannon_eq="TRUE");
```

**Аргументы:**

| ID              | Тип                                                                          | Описание                                                       |
|-----------------|------------------------------------------------------------------------------|----------------------------------------------------------------|
| variable        | Переменная\[Список\]                                                         | Переменная для присвоения                                      |
| text            | Текст                                                                        | Текст                                                          |
| regex           | Текст                                                                        | Регулярное выражение                                           |
| group           | Текст                                                                        | Группа                                                         |
| match_mode      | Маркер<br/>**ALL** - Все совпадения<br/>**FIRST** - Только первое совпадение | Количество совпадений                                          |
| get_group_by    | Маркер<br/>**INDEX** - Номеру<br/>**NAME** - Имени                           | Получить группу по                                             |
| ignore_case     | Маркер<br/>**TRUE** - Включено<br/>**FALSE** - Выключено                     | Игнорировать регистр (флаг ignore_case)                        |
| multiline       | Маркер<br/>**TRUE** - Включён<br/>**FALSE** - Выключен                       | Многострочный режим (флаг multiline)                           |
| literal         | Маркер<br/>**TRUE** - Включено<br/>**FALSE** - Выключено                     | Воспринимать шаблон дословно (флаг literal)                    |
| unix_lines      | Маркер<br/>**TRUE** - Включён<br/>**FALSE** - Выключен                       | Режим UNIX строк (флаг unix_lines)                             |
| comments        | Маркер<br/>**TRUE** - Включено<br/>**FALSE** - Выключено                     | Разрешить комментарии и игнорирование пробелов (флаг comments) |
| dot_matches_all | Маркер<br/>**TRUE** - Включён<br/>**FALSE** - Выключен                       | Режим dotall (флаг dotall)                                     |
| cannon_eq       | Маркер<br/>**TRUE** - Включено<br/>**FALSE** - Выключено                     | Каноническая эквивалентность (флаг cannon_eq)                  |

<h3 id=set_variable_get_text_similarity>
  <code>variable::get_text_similarity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить схожесть текстов\
**Тип:** Действие, возращающее значение\
**Описание:** Получает коэффициент схожести текстов и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_text_similarity("text_1", "text_2", "SIMILARITY");

//Или от объекта

`variable` = "text_1".get_text_similarity("text_2", "SIMILARITY");

//Или в сухую позиционно

variable::get_text_similarity(`variable`, "text_1", "text_2", "SIMILARITY");

//Или в сухую по ключам

variable::get_text_similarity(variable=`variable`, text_1="text_1", text_2="text_2", value_type="SIMILARITY");
```

**Аргументы:**

| ID         | Тип                                                                                                | Описание                  |
|------------|----------------------------------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Число\]                                                                                | Переменная для присвоения |
| text_1     | Текст                                                                                              | Первый текст              |
| text_2     | Текст                                                                                              | Второй текст              |
| value_type | Маркер<br/>**SIMILARITY** - Процент схожести<br/>**LEVENSHTEIN_DISTANCE** - Расстояние Левенштейна | Тип значения              |

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
`variable` = variable::get_text_width("text");

//Или от объекта

`variable` = "text".get_text_width();

//Или в сухую позиционно

variable::get_text_width(`variable`, "text");

//Или в сухую по ключам

variable::get_text_width(variable=`variable`, text="text");
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| text     | Текст               | Исходный текст            |

<h3 id=set_variable_get_tile_block_custom_tag>
  <code>variable::get_tile_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить кастомный тег блока-сущности\
**Тип:** Действие, возращающее значение\
**Описание:** Получает данные о кастомном теге блока-сущности и присваивает результат к переменной.\
**Работает с:**\
&nbsp;&nbsp;Блоками-сущностями (сундуки, таблички, бочки и т.д.)

**Пример использования:**
```ts
`variable` = variable::get_tile_block_custom_tag(location(0,0,0,0,0), "tag_name", "any value");

//Или в сухую позиционно

variable::get_tile_block_custom_tag(`variable`, location(0,0,0,0,0), "tag_name", "any value");

//Или в сухую по ключам

variable::get_tile_block_custom_tag(variable=`variable`, location=location(0,0,0,0,0), tag_name="tag_name", default_value="any value");
```

**Аргументы:**

| ID            | Тип                 | Описание                      |
|---------------|---------------------|-------------------------------|
| variable      | Переменная\[Текст\] | Переменная для присвоения     |
| location      | Местоположение      | Местоположение блока-сущности |
| tag_name      | Текст               | Имя кастомного тега           |
| default_value | Любое значение      | Значение по умолчанию         |

<h3 id=set_variable_get_tile_block_nbt>
  <code>variable::get_tile_block_nbt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить NBT-теги блока-сущности\
**Тип:** Действие, возращающее значение\
**Описание:** Получает данные о NBT-тегах блока-сущности и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_tile_block_nbt(location(0,0,0,0,0), "path", "ANY_VALUE");

//Или в сухую позиционно

variable::get_tile_block_nbt(`variable`, location(0,0,0,0,0), "path", "ANY_VALUE");

//Или в сухую по ключам

variable::get_tile_block_nbt(variable=`variable`, location=location(0,0,0,0,0), path="path", value_type="ANY_VALUE");
```

**Аргументы:**

| ID         | Тип                                                                       | Описание                      |
|------------|---------------------------------------------------------------------------|-------------------------------|
| variable   | Переменная\[Любое значение\]                                              | Переменная для присвоения     |
| location   | Местоположение                                                            | Местоположение блока-сущности |
| path       | Текст                                                                     | Путь                          |
| value_type | Маркер<br/>**ANY_VALUE** - Любое значение<br/>**NBT_STRING** - NBT-строка | Тип данных                    |

<h3 id=set_variable_get_vault_displayed_item>
  <code>variable::get_vault_displayed_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить отображаемый предмет сокровищницы\
**Тип:** Действие, возращающее значение\
**Описание:** Получает отображаемый предмет сокровищницы и присваивает его к переменной.\
**Работает с:**\
&nbsp;&nbsp;Сокровищницами

**Пример использования:**
```ts
`variable` = variable::get_vault_displayed_item(location(0,0,0,0,0));

//Или в сухую позиционно

variable::get_vault_displayed_item(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_vault_displayed_item(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                   | Описание                    |
|----------|-----------------------|-----------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения   |
| location | Местоположение        | Местоположение сокровищницы |

<h3 id=set_variable_get_vault_next_state_update_time>
  <code>variable::get_vault_next_state_update_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить время следующего обновления состояния сокровищницы\
**Тип:** Действие, возращающее значение\
**Описание:** Получает время следующего обновления состояния сокровищницы и присваивает его к переменной.\
**Работает с:**\
&nbsp;&nbsp;Сокровищницами

**Пример использования:**
```ts
`variable` = variable::get_vault_next_state_update_time(location(0,0,0,0,0));

//Или в сухую позиционно

variable::get_vault_next_state_update_time(`variable`, location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_vault_next_state_update_time(variable=`variable`, location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения   |
| location | Местоположение      | Местоположение сокровищницы |

<h3 id=set_variable_get_vector_all_components>
  <code>variable::get_vector_all_components</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить все координаты вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Получает все координаты вектора и присваивает результат к переменным.

**Пример использования:**
```ts
`x`, `y`, `z` = variable::get_vector_all_components(vector(0,0,0));

//Или от объекта

`x`, `y`, `z` = vector(0,0,0).get_vector_all_components();

//Или в сухую позиционно

variable::get_vector_all_components(`x`, `y`, `z`, vector(0,0,0));

//Или в сухую по ключам

variable::get_vector_all_components(x=`x`, y=`y`, z=`z`, vector=vector(0,0,0));
```

**Аргументы:**

| ID     | Тип                 | Описание                      |
|--------|---------------------|-------------------------------|
| x      | Переменная\[Число\] | Координата X                  |
| y      | Переменная\[Число\] | Координата Y                  |
| z      | Переменная\[Число\] | Координата Z                  |
| vector | Вектор              | Вектор для получения значений |

<h3 id=set_variable_get_vector_between_locations>
  <code>variable::get_vector_between_locations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать вектор между местоположениями\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт вектор между начальным и конечным местоположениями и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_vector_between_locations(location(0,0,0,0,0), location(0,0,0,0,0));

//Или в сухую позиционно

variable::get_vector_between_locations(`variable`, location(0,0,0,0,0), location(0,0,0,0,0));

//Или в сухую по ключам

variable::get_vector_between_locations(variable=`variable`, end_location=location(0,0,0,0,0), start_location=location(0,0,0,0,0));
```

**Аргументы:**

| ID             | Тип                  | Описание                  |
|----------------|----------------------|---------------------------|
| variable       | Переменная\[Вектор\] | Переменная для присвоения |
| end_location   | Местоположение       | Начальное местоположение  |
| start_location | Местоположение       | Конечное местоположение   |

<h3 id=set_variable_get_vector_component>
  <code>variable::get_vector_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить координату вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённую координату вектора и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::get_vector_component(vector(0,0,0), "X");

//Или от объекта

`variable` = vector(0,0,0).get_vector_component("X");

//Или в сухую позиционно

variable::get_vector_component(`variable`, vector(0,0,0), "X");

//Или в сухую по ключам

variable::get_vector_component(variable=`variable`, vector=vector(0,0,0), vector_component="X");
```

**Аргументы:**

| ID               | Тип                                                                               | Описание                      |
|------------------|-----------------------------------------------------------------------------------|-------------------------------|
| variable         | Переменная\[Число\]                                                               | Переменная для присвоения     |
| vector           | Вектор                                                                            | Вектор для получения значения |
| vector_component | Маркер<br/>**X** - Координата X<br/>**Y** - Координата Y<br/>**Z** - Координата Z | Тип координаты                |

<h3 id=set_variable_get_vector_from_block_face>
  <code>variable::get_vector_from_block_face</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать вектор из кардинального направления\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт нормализированный вектор в зависимости от указанного кардинального направления ("south", "north", "east", "west", "up", "down").

**Пример использования:**
```ts
`variable` = variable::get_vector_from_block_face("block_face");

//Или в сухую позиционно

variable::get_vector_from_block_face(`variable`, "block_face");

//Или в сухую по ключам

variable::get_vector_from_block_face(variable=`variable`, block_face="block_face");
```

**Аргументы:**

| ID         | Тип                  | Описание                  |
|------------|----------------------|---------------------------|
| variable   | Переменная\[Вектор\] | Переменная для присвоения |
| block_face | Текст                | Кардинальное направление  |

<h3 id=set_variable_get_vector_length>
  <code>variable::get_vector_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить длину вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение длины вектора.

**Пример использования:**
```ts
`variable` = variable::get_vector_length(vector(0,0,0), "LENGTH");

//Или от объекта

`variable` = vector(0,0,0).get_vector_length("LENGTH");

//Или в сухую позиционно

variable::get_vector_length(`variable`, vector(0,0,0), "LENGTH");

//Или в сухую по ключам

variable::get_vector_length(variable=`variable`, vector=vector(0,0,0), length_type="LENGTH");
```

**Аргументы:**

| ID          | Тип                                                                              | Описание                   |
|-------------|----------------------------------------------------------------------------------|----------------------------|
| variable    | Переменная\[Число\]                                                              | Переменная для присвоения  |
| vector      | Вектор                                                                           | Вектор для получения длины |
| length_type | Маркер<br/>**LENGTH** - Реальная длина<br/>**LENGTH_SQUARED** - Длина в квадрате | Тип значения               |

<h3 id=set_variable_hadamard_vector_product>
  <code>variable::hadamard_vector_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Адамарово произведение векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной адамарово произведение двух векторов.

**Пример использования:**
```ts
`variable` = variable::hadamard_vector_product(vector(0,0,0), vector(0,0,0));

//Или от объекта

`variable` = vector(0,0,0).hadamard_vector_product(vector(0,0,0));

//Или в сухую позиционно

variable::hadamard_vector_product(`variable`, vector(0,0,0), vector(0,0,0));

//Или в сухую по ключам

variable::hadamard_vector_product(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0));
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Вектор\] | Переменная для присвоения |
| vector_1 | Вектор               | Первый вектор             |
| vector_2 | Вектор               | Второй вектор             |

<h3 id=set_variable_hash>
  <code>variable::get_text_hash</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить хеш текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение хеша текста.

**Пример использования:**
```ts
`variable` = variable::get_text_hash("text", "MD5");

//Или от объекта

`variable` = "text".get_text_hash("MD5");

//Или в сухую позиционно

variable::get_text_hash(`variable`, "text", "MD5");

//Или в сухую по ключам

variable::get_text_hash(variable=`variable`, text="text", algorithm="MD5");
```

**Аргументы:**

| ID        | Тип                                                                    | Описание                  |
|-----------|------------------------------------------------------------------------|---------------------------|
| variable  | Переменная\[Текст\]                                                    | Переменная для присвоения |
| text      | Текст                                                                  | Исходный текст            |
| algorithm | Маркер<br/>**MD5** - MD5<br/>**SHA1** - SHA-1<br/>**SHA256** - SHA-256 | Aлгоритм                  |

<h3 id=set_variable_hide_item_components>
  <code>variable::hide_item_components</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Скрыть компоненты предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Скрывает указанные компоненты предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::hide_item_components(item("stick"), ["components", "components"], "SET");

//Или от объекта

`variable` = item("stick").hide_item_components(["components", "components"], "SET");

//Или в сухую позиционно

variable::hide_item_components(`variable`, item("stick"), ["components", "components"], "SET");

//Или в сухую по ключам

variable::hide_item_components(variable=`variable`, item=item("stick"), components=["components", "components"], mode="SET");
```

**Аргументы:**

| ID         | Тип                                                                               | Описание                  |
|------------|-----------------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Предмет\]                                                             | Переменная для присвоения |
| item       | Предмет                                                                           | Предмет                   |
| components | Message 'actions.array' not found in 'ru_RU'\[Текст\]                             | Ключи компонентов         |
| mode       | Маркер<br/>**SET** - Установка<br/>**ADD** - Добавление<br/>**REMOVE** - Удаление | Режим установки           |

<h3 id=set_variable_increment>
  <code>variable::increment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Прибавление (+=)\
**Тип:** Действие без значения\
**Описание:** Прибавляет к переменной выбранное число.

**Пример использования:**
```ts
variable::increment(`variable`, 1);

//Или от объекта

`variable`.increment(1);

//Или в сухую по ключам

variable::increment(variable=`variable`, number=1);
```

**Аргументы:**

| ID       | Тип        | Описание                  |
|----------|------------|---------------------------|
| variable | Переменная | Переменная для присвоения |
| number   | Число      | Число для прибавления     |

<h3 id=set_variable_insert_list_value>
  <code>variable::insert_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Вставить значение в список\
**Тип:** Действие, возращающее значение\
**Описание:** Вставляет значение в список по указанному индексу, сдвигая все значения в нём после него вправо.

**Пример использования:**
```ts
`variable` = variable::insert_list_value([`list`, `list`], 1, "any value");

//Или от объекта

`variable` = [`list`, `list`].insert_list_value(1, "any value");

//Или в сухую позиционно

variable::insert_list_value(`variable`, [`list`, `list`], 1, "any value");

//Или в сухую по ключам

variable::insert_list_value(variable=`variable`, list=[`list`, `list`], number=1, value="any value");
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| list     | Список               | Список                    |
| number   | Число                | Индекс                    |
| value    | Любое значение       | Значение                  |

<h3 id=set_variable_join_text>
  <code>variable::join_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Объединить список в текст\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет элементы списка в единый текст и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::join_text([`list`, `list`], "separator", "prefix", "postfix", 1, "truncated");

//Или от объекта

`variable` = [`list`, `list`].join_text("separator", "prefix", "postfix", 1, "truncated");

//Или в сухую позиционно

variable::join_text(`variable`, [`list`, `list`], "separator", "prefix", "postfix", 1, "truncated");

//Или в сухую по ключам

variable::join_text(variable=`variable`, list=[`list`, `list`], separator="separator", prefix="prefix", postfix="postfix", limit=1, truncated="truncated");
```

**Аргументы:**

| ID        | Тип                 | Описание                                      |
|-----------|---------------------|-----------------------------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения                     |
| list      | Список              | Список для объединения                        |
| separator | Текст               | Разделитель                                   |
| prefix    | Текст               | Префикс                                       |
| postfix   | Текст               | Постфикс                                      |
| limit     | Число               | Лимит элементов (если пусто, то все элементы) |
| truncated | Текст               | Текст после лимита (по умолчанию - "...")     |

<h3 id=set_variable_lerp_number>
  <code>variable::lerp_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Интерполировать число\
**Тип:** Действие, возращающее значение\
**Описание:** Вычисляет число между двумя числами с определённым коэффициентом и присваивает результат к переменной. При коэффициенте 0 будет возвращено первое число, при 1 - второе, при 0.5 - среднее значение.

**Пример использования:**
```ts
`variable` = variable::lerp_number(1, 2, 3);

//Или от объекта

`variable` = (3).lerp_number(1, 2);

//Или в сухую позиционно

variable::lerp_number(`variable`, 1, 2, 3);

//Или в сухую по ключам

variable::lerp_number(variable=`variable`, start=1, stop=2, amount=3);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| start    | Число               | Первое число              |
| stop     | Число               | Второе число              |
| amount   | Число               | Коэффициент (от 0 до 1)   |

<h3 id=set_variable_location_relative>
  <code>variable::location_relative</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить относительное местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает местоположение относительно стороны блока на определённом расстоянии, присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::location_relative(location(0,0,0,0,0), 1, "DOWN");

//Или от объекта

`variable` = location(0,0,0,0,0).location_relative(1, "DOWN");

//Или в сухую позиционно

variable::location_relative(`variable`, location(0,0,0,0,0), 1, "DOWN");

//Или в сухую по ключам

variable::location_relative(variable=`variable`, location=location(0,0,0,0,0), distance=1, block_face="DOWN");
```

**Аргументы:**

| ID         | Тип                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Описание                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| variable   | Переменная\[Местоположение\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Переменная для присвоения    |
| location   | Местоположение                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Относительное местоположение |
| distance   | Число                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Расстояние                   |
| block_face | Маркер<br/>**DOWN** - Низ<br/>**EAST** - Восток<br/>**EAST_NORTH_EAST** - Восток-север-восток (east_north_east)<br/>**EAST_SOUTH_EAST** - Восток-юг-восток (east_south_east)<br/>**NORTH** - Север<br/>**NORTH_EAST** - Северо-восток<br/>**NORTH_NORTH_EAST** - Север-север-восток (north_north_east)<br/>**NORTH_NORTH_WEST** - Север-север-запад (north_north_west)<br/>**NORTH_WEST** - Северо-запад<br/>**SELF** - Собственная (self)<br/>**SOUTH** - Юг<br/>**SOUTH_EAST** - Юго-восток<br/>**SOUTH_SOUTH_EAST** - Юг-юг-восток (south_south_east)<br/>**SOUTH_SOUTH_WEST** - Юг-юг-запад (south_south_west)<br/>**SOUTH_WEST** - Юго-запад<br/>**UP** - Верх<br/>**WEST** - Запад<br/>**WEST_NORTH_WEST** - Запад-север-запад (west_north_west)<br/>**WEST_SOUTH_WEST** - Запад-юг-запад (west_south_west) | Сторона блока                |

<h3 id=set_variable_locations_distance>
  <code>variable::locations_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить расстояние между местоположениями\
**Тип:** Действие, возращающее значение\
**Описание:** Получает расстояние между местоположениями и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::locations_distance(location(0,0,0,0,0), location(0,0,0,0,0), "ALTITUDE");

//Или в сухую позиционно

variable::locations_distance(`variable`, location(0,0,0,0,0), location(0,0,0,0,0), "ALTITUDE");

//Или в сухую по ключам

variable::locations_distance(variable=`variable`, location_1=location(0,0,0,0,0), location_2=location(0,0,0,0,0), type="ALTITUDE");
```

**Аргументы:**

| ID         | Тип                                                                                                                                                                    | Описание                  |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Число\]                                                                                                                                                    | Переменная для присвоения |
| location_1 | Местоположение                                                                                                                                                         | Первое местоположение     |
| location_2 | Местоположение                                                                                                                                                         | Второе местоположение     |
| type       | Маркер<br/>**ALTITUDE** - По высоте<br/>**SQUARED_2D** - Округленное в 2D<br/>**SQUARED_3D** - Округленное в 3D<br/>**THREE_D** - В объёме<br/>**TWO_D** - В плоскости | Тип расстояния            |

<h3 id=set_variable_log>
  <code>variable::log</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Логарифм числа (log)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение логарифма с выбранным аргументом и основанием.

**Пример использования:**
```ts
`variable` = variable::log(1, 2);

//Или от объекта

`variable` = (1).log(2);

//Или в сухую позиционно

variable::log(`variable`, 1, 2);

//Или в сухую по ключам

variable::log(variable=`variable`, number=1, base=2);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| number   | Число               | Аргумент логарифма        |
| base     | Число               | Основание логарифма       |

<h3 id=set_variable_map_range>
  <code>variable::map_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Перевести число в другой диапазон\
**Тип:** Действие, возращающее значение\
**Описание:** Переводит число с одного диапазона в другой и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::map_range(1, 2, 3, 4, 5);

//Или от объекта

`variable` = (1).map_range(2, 3, 4, 5);

//Или в сухую позиционно

variable::map_range(`variable`, 1, 2, 3, 4, 5);

//Или в сухую по ключам

variable::map_range(variable=`variable`, number=1, from_start=2, from_stop=3, to_start=4, to_stop=5);
```

**Аргументы:**

| ID         | Тип                 | Описание                              |
|------------|---------------------|---------------------------------------|
| variable   | Переменная\[Число\] | Переменная для присвоения             |
| number     | Число               | Число для изменения                   |
| from_start | Число               | Нижний предел изначального диапазона  |
| from_stop  | Число               | Верхний предел изначального диапазона |
| to_start   | Число               | Нижний предел нового диапазона        |
| to_stop    | Число               | Верхний предел нового диапазона       |

<h3 id=set_variable_mathematical_expectation>
  <code>variable::mathematical_expectation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Математическое ожидание\
**Тип:** Действие, возращающее значение\
**Описание:** Вычисляет математическое ожидание, то есть средневзвешенное значение всех возможных исходов случайной величины. Может быть представлено как Σ nᵢ * pᵢ, где n - исход, p - вероятность

**Пример использования:**
```ts
`variable` = variable::mathematical_expectation([1, 2], [3, 4]);

//Или в сухую позиционно

variable::mathematical_expectation(`variable`, [1, 2], [3, 4]);

//Или в сухую по ключам

variable::mathematical_expectation(variable=`variable`, values=[1, 2], probabilities=[3, 4]);
```

**Аргументы:**

| ID            | Тип                                                   | Описание                  |
|---------------|-------------------------------------------------------|---------------------------|
| variable      | Переменная\[Число\]                                   | Переменная для присвоения |
| values        | Message 'actions.array' not found in 'ru_RU'\[Число\] | Исходы                    |
| probabilities | Message 'actions.array' not found in 'ru_RU'\[Число\] | Вероятности               |

<h3 id=set_variable_max>
  <code>variable::max</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Максимальное значение\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной наибольшее число из выбранных.

**Пример использования:**
```ts
`variable` = variable::max([1, 2]);

//Или в сухую позиционно

variable::max(`variable`, [1, 2]);

//Или в сухую по ключам

variable::max(variable=`variable`, value=[1, 2]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                   | Переменная для присвоения |
| value    | Message 'actions.array' not found in 'ru_RU'\[Число\] | Числа для выбора          |

<h3 id=set_variable_median>
  <code>variable::median</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Медианное значение\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной медианное (серединное) значение чисел.

**Пример использования:**
```ts
`variable` = variable::median([1, 2]);

//Или в сухую позиционно

variable::median(`variable`, [1, 2]);

//Или в сухую по ключам

variable::median(variable=`variable`, value=[1, 2]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                     |
|----------|-------------------------------------------------------|------------------------------|
| variable | Переменная\[Число\]                                   | Переменная для присвоения    |
| value    | Message 'actions.array' not found in 'ru_RU'\[Число\] | Числа для получения значения |

<h3 id=set_variable_min>
  <code>variable::min</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Минимальное значение\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной наименьшее число из выбранных.

**Пример использования:**
```ts
`variable` = variable::min([1, 2]);

//Или в сухую позиционно

variable::min(`variable`, [1, 2]);

//Или в сухую по ключам

variable::min(variable=`variable`, value=[1, 2]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                   | Переменная для присвоения |
| value    | Message 'actions.array' not found in 'ru_RU'\[Число\] | Числа для выбора          |

<h3 id=set_variable_multiple>
  <code>variable::set_values</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить значения нескольких переменных (=)\
**Тип:** Действие без значения\
**Описание:** Присваивает указанные значения к указанным переменным.

**Пример использования:**
```ts
variable::set_values([`variables`, `variables`], ["any value", "any value"]);

//Или в сухую по ключам

variable::set_values(variables=[`variables`, `variables`], values=["any value", "any value"]);
```

**Аргументы:**

| ID        | Тип                                                            | Описание                  |
|-----------|----------------------------------------------------------------|---------------------------|
| variables | Message 'actions.array' not found in 'ru_RU'\[Переменная\]     | Переменные для присвоения |
| values    | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Значения для присвоения   |

<h3 id=set_variable_multiply>
  <code>variable::multiply</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Умножение чисел (×)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной произведение чисел.

**Пример использования:**
```ts
`variable` = variable::multiply([1, 2]);

//Или в сухую позиционно

variable::multiply(`variable`, [1, 2]);

//Или в сухую по ключам

variable::multiply(variable=`variable`, value=[1, 2]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                   | Переменная для присвоения |
| value    | Message 'actions.array' not found in 'ru_RU'\[Число\] | Числа для умножения       |

<h3 id=set_variable_multiply_vector>
  <code>variable::multiply_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Умножить вектор на число\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной результат умножения вектора на число.

**Пример использования:**
```ts
`variable` = variable::multiply_vector(vector(0,0,0), 1);

//Или от объекта

`variable` = vector(0,0,0).multiply_vector(1);

//Или в сухую позиционно

variable::multiply_vector(`variable`, vector(0,0,0), 1);

//Или в сухую по ключам

variable::multiply_vector(variable=`variable`, vector=vector(0,0,0), multiplier=1);
```

**Аргументы:**

| ID         | Тип                  | Описание                  |
|------------|----------------------|---------------------------|
| variable   | Переменная\[Вектор\] | Переменная для присвоения |
| vector     | Вектор               | Вектор для изменения      |
| multiplier | Число                | Число для умножения       |

<h3 id=set_variable_obtain_item_custom_model_data>
  <code>variable::obtain_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить данные о модели предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Получает список данных о модели предмета (CustomModelData) и присваивает его к переменной.

**Пример использования:**
```ts
`variable` = variable::obtain_item_custom_model_data(item("stick"), "FLOATS");

//Или от объекта

`variable` = item("stick").obtain_item_custom_model_data("FLOATS");

//Или в сухую позиционно

variable::obtain_item_custom_model_data(`variable`, item("stick"), "FLOATS");

//Или в сухую по ключам

variable::obtain_item_custom_model_data(variable=`variable`, item=item("stick"), value_type="FLOATS");
```

**Аргументы:**

| ID         | Тип                                                                                                                                                                                      | Описание                  |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Список\]                                                                                                                                                                     | Переменная для присвоения |
| item       | Предмет                                                                                                                                                                                  | Предмет                   |
| value_type | Маркер<br/>**FLOATS** - Плавающие значения (floats)<br/>**BOOLEANS** - Булевые значения (booleans)<br/>**STRINGS** - Строчные значения (strings)<br/>**COLORS** - Список цветов (colors) | Тип данных                |

<h3 id=set_variable_parse_json>
  <code>variable::parse_json</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Разобрать JSON\
**Тип:** Действие, возращающее значение\
**Описание:** Разбирает текст JSON на элементы\: словари (если текст заключен в фигурные скобки) и списки (если текст заключен в квадратные скобки), с которыми можно работать, чтобы получить нужные значения.

**Пример использования:**
```ts
`variable` = variable::parse_json("json");

//Или в сухую позиционно

variable::parse_json(`variable`, "json");

//Или в сухую по ключам

variable::parse_json(variable=`variable`, json="json");
```

**Аргументы:**

| ID       | Тип                 | Описание              |
|----------|---------------------|-----------------------|
| variable | Переменная\[Текст\] | Для записи результата |
| json     | Текст               | JSON текст            |

<h3 id=set_variable_parse_to_component>
  <code>variable::parse_to_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает тип стилизуемого текста, не меняя его содержимое, и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::parse_to_component("text", "JSON");

//Или от объекта

`variable` = "text".parse_to_component("JSON");

//Или в сухую позиционно

variable::parse_to_component(`variable`, "text", "JSON");

//Или в сухую по ключам

variable::parse_to_component(variable=`variable`, text="text", parsing="JSON");
```

**Аргументы:**

| ID       | Тип                                                                                                               | Описание                  |
|----------|-------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Текст\]                                                                                               | Переменная для присвоения |
| text     | Текст                                                                                                             | Текст для установки       |
| parsing  | Маркер<br/>**JSON** - JSON<br/>**LEGACY** - Цветной (&)<br/>**MINIMESSAGE** - Стилизуемый<br/>**PLAIN** - Обычный | Тип стилизуемого текста   |

<h3 id=set_variable_perlin_noise_3d>
  <code>variable::perlin_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Шум Перлина\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение шума Перлина в определённом местоположении. Возвращает число, со значением от -1 до 1.

**Пример использования:**
```ts
`variable` = variable::perlin_noise_3d(location(0,0,0,0,0), 1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Или в сухую позиционно

variable::perlin_noise_3d(`variable`, location(0,0,0,0,0), 1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Или в сухую по ключам

variable::perlin_noise_3d(variable=`variable`, location=location(0,0,0,0,0), seed=1, loc_frequency=2, octaves=3, frequency=4, amplitude=5, range_mode="FULL_RANGE", normalized="FALSE");
```

**Аргументы:**

| ID            | Тип                                                                                                 | Описание                          |
|---------------|-----------------------------------------------------------------------------------------------------|-----------------------------------|
| variable      | Переменная\[Число\]                                                                                 | Переменная для присвоения         |
| location      | Местоположение                                                                                      | Местоположение для установки шума |
| seed          | Число                                                                                               | Ключ шума                         |
| loc_frequency | Число                                                                                               | Частота шума                      |
| octaves       | Число                                                                                               | Количество октав шума (1-8)       |
| frequency     | Число                                                                                               | Частота октав шума                |
| amplitude     | Число                                                                                               | Амплитуда октав шума              |
| range_mode    | Маркер<br/>**FULL_RANGE** - Полный диапазон (от -1 до 1 или больше)<br/>**ZERO_TO_ONE** - От 0 до 1 | Диапазон значений                 |
| normalized    | Маркер<br/>**FALSE** - Не нормализировать<br/>**TRUE** - Нормализировать                            | Нормализация значений             |

<h3 id=set_variable_pow>
  <code>variable::pow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Степень числа (^)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение степени с выбранным основанием и показателем.

**Пример использования:**
```ts
`variable` = variable::pow(1, 2);

//Или от объекта

`variable` = (1).pow(2);

//Или в сухую позиционно

variable::pow(`variable`, 1, 2);

//Или в сухую по ключам

variable::pow(variable=`variable`, base=1, power=2);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| base     | Число               | Основание степени         |
| power    | Число               | Показатель степени        |

<h3 id=set_variable_purge>
  <code>variable::purge</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить переменные\
**Тип:** Действие без значения\
**Описание:** Очищает все переменные, подходящие под выбранные имена.

**Пример использования:**
```ts
variable::purge(["names", "names"], "GAME", "ENDS_WITH", "FALSE");

//Или в сухую по ключам

variable::purge(names=["names", "names"], scope="GAME", match="ENDS_WITH", ignore_case="FALSE");
```

**Аргументы:**

| ID          | Тип                                                                                                                                                                                                               | Описание               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| names       | Message 'actions.array' not found in 'ru_RU'\[Текст\]                                                                                                                                                             | Имена для сравнения    |
| scope       | Маркер<br/>**GAME** - Игровая<br/>**LOCAL** - Локальная<br/>**SAVE** - Сохранённая                                                                                                                                | Тип переменной         |
| match       | Маркер<br/>**ENDS_WITH** - Имя заканчивается на<br/>**EQUALS** - Полное соответствие<br/>**NAME_CONTAINS** - Имя содержит текст<br/>**PART_CONTAINS** - Текст содержит имя<br/>**STARTS_WITH** - Имя начинается с | Режим сравнения        |
| ignore_case | Маркер<br/>**FALSE** - Выключено<br/>**TRUE** - Включено                                                                                                                                                          | Игнорирование регистра |

<h3 id=set_variable_random>
  <code>variable::random</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить случайное значение\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает случайное значение к переменной.

**Пример использования:**
```ts
`variable` = variable::random(["any value", "any value"]);

//Или в сухую позиционно

variable::random(`variable`, ["any value", "any value"]);

//Или в сухую по ключам

variable::random(variable=`variable`, values=["any value", "any value"]);
```

**Аргументы:**

| ID       | Тип                                                            | Описание                  |
|----------|----------------------------------------------------------------|---------------------------|
| variable | Переменная\[Любое значение\]                                   | Переменная для присвоения |
| values   | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Значения для выбора       |

<h3 id=set_variable_random_location>
  <code>variable::random_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать случайное местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт случайное местоположение в регионе между двумя углами и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::random_location(location(0,0,0,0,0), location(0,0,0,0,0), "FALSE");

//Или в сухую позиционно

variable::random_location(`variable`, location(0,0,0,0,0), location(0,0,0,0,0), "FALSE");

//Или в сухую по ключам

variable::random_location(variable=`variable`, location_1=location(0,0,0,0,0), location_2=location(0,0,0,0,0), integer="FALSE");
```

**Аргументы:**

| ID         | Тип                                                      | Описание                      |
|------------|----------------------------------------------------------|-------------------------------|
| variable   | Переменная\[Местоположение\]                             | Переменная для присвоения     |
| location_1 | Местоположение                                           | Первый угол региона           |
| location_2 | Местоположение                                           | Второй угол региона           |
| integer    | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Округление до целых координат |

<h3 id=set_variable_random_number>
  <code>variable::random_number</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Случайное число\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной случайное число в выбранном диапазоне.

**Пример использования:**
```ts
`variable` = variable::random_number(1, 2, "FALSE");

//Или в сухую позиционно

variable::random_number(`variable`, 1, 2, "FALSE");

//Или в сухую по ключам

variable::random_number(variable=`variable`, min=1, max=2, integer="FALSE");
```

**Аргументы:**

| ID       | Тип                                                 | Описание                  |
|----------|-----------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                 | Переменная для присвоения |
| min      | Число                                               | Минимальное значение      |
| max      | Число                                               | Максимальное значение     |
| integer  | Маркер<br/>**FALSE** - Дробное<br/>**TRUE** - Целое | Тип числа                 |

<h3 id=set_variable_randomize_list_order>
  <code>variable::randomize_list_order</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Рандомизировать список\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает порядок элементов случайным образом.

**Пример использования:**
```ts
`variable` = variable::randomize_list_order([`list`, `list`]);

//Или от объекта

`variable` = [`list`, `list`].randomize_list_order();

//Или в сухую позиционно

variable::randomize_list_order(`variable`, [`list`, `list`]);

//Или в сухую по ключам

variable::randomize_list_order(variable=`variable`, list=[`list`, `list`]);
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| list     | Список               | Список                    |

<h3 id=set_variable_ray_trace_result>
  <code>variable::ray_trace_result</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить результат рейкаста\
**Тип:** Действие, возращающее значение\
**Описание:** Запускает луч с заданными параметрами. При столкновении луча с указанными объектами (с сущностью или блоком) можно получить местоположение падения луча, местоположение и сторону блока, UUID сущности и сторону хитбокса. Ширина луча работает только на сущностей (увеличивает или уменьшает хитбоксы существ).

**Пример использования:**
```ts
`variable_for_hit_location`, `variable_for_hit_block_location`, `variable_for_hit_block_face`, `variable_for_hit_entity_uuid` = variable::ray_trace_result(location(0,0,0,0,0), 1, 2, [`entities`, `entities`], "BLOCKS_AND_ENTITIES", "FALSE", "ALWAYS");

//Или в сухую позиционно

variable::ray_trace_result(`variable_for_hit_location`, `variable_for_hit_block_location`, `variable_for_hit_block_face`, `variable_for_hit_entity_uuid`, location(0,0,0,0,0), 1, 2, [`entities`, `entities`], "BLOCKS_AND_ENTITIES", "FALSE", "ALWAYS");

//Или в сухую по ключам

variable::ray_trace_result(variable_for_hit_location=`variable_for_hit_location`, variable_for_hit_block_location=`variable_for_hit_block_location`, variable_for_hit_block_face=`variable_for_hit_block_face`, variable_for_hit_entity_uuid=`variable_for_hit_entity_uuid`, start=location(0,0,0,0,0), ray_size=1, max_distance=2, entities=[`entities`, `entities`], ray_collision_mode="BLOCKS_AND_ENTITIES", ignore_passable_blocks="FALSE", fluid_collision_mode="ALWAYS");
```

**Аргументы:**

| ID                              | Тип                                                                                                                                            | Описание                                                                         |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| variable_for_hit_location       | Переменная\[Местоположение\]                                                                                                                   | Точка падения луча                                                               |
| variable_for_hit_block_location | Переменная\[Местоположение\]                                                                                                                   | Местоположение блока                                                             |
| variable_for_hit_block_face     | Переменная\[Текст\]                                                                                                                            | Сторона блока/хитбокса                                                           |
| variable_for_hit_entity_uuid    | Переменная\[Список\]                                                                                                                           | UUID сущности                                                                    |
| start                           | Местоположение                                                                                                                                 | Начало луча                                                                      |
| ray_size                        | Число                                                                                                                                          | Ширина луча                                                                      |
| max_distance                    | Число                                                                                                                                          | Длина луча                                                                       |
| entities                        | Список                                                                                                                                         | Имена или UUID сущностей для столкновения (по умолчанию - все игроки и сущности) |
| ray_collision_mode              | Маркер<br/>**BLOCKS_AND_ENTITIES** - С блоками и сущностями<br/>**ONLY_BLOCKS** - Только с блоками<br/>**ONLY_ENTITIES** - Только с сущностями | Столкновение с объектами                                                         |
| ignore_passable_blocks          | Маркер<br/>**FALSE** - Не игнорировать<br/>**TRUE** - Игнорировать                                                                             | Игнорировать проходимые блоки                                                    |
| fluid_collision_mode            | Маркер<br/>**ALWAYS** - Не игнорировать<br/>**NEVER** - Полностью игнорировать<br/>**SOURCE_ONLY** - Учитывать только источник жидкости        | Игнорировать жидкость                                                            |

<h3 id=set_variable_reflect_vector_product>
  <code>variable::reflect_vector_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отразить вектор относительно второго вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Отражает вектор относительно другого вектора и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::reflect_vector_product(vector(0,0,0), vector(0,0,0), 1);

//Или в сухую позиционно

variable::reflect_vector_product(`variable`, vector(0,0,0), vector(0,0,0), 1);

//Или в сухую по ключам

variable::reflect_vector_product(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0), bounce=1);
```

**Аргументы:**

| ID       | Тип                  | Описание                                                     |
|----------|----------------------|--------------------------------------------------------------|
| variable | Переменная\[Вектор\] | Переменная для присвоения                                    |
| vector_1 | Вектор               | Исходный вектор                                              |
| vector_2 | Вектор               | Вектор поверхности отражения                                 |
| bounce   | Число                | Домножение итогового вектора на это число (по умолчанию 1.0) |

<h3 id=set_variable_regex_replace_text>
  <code>variable::regex_replace_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заменить совпадение с регулярным выражением\
**Тип:** Действие, возращающее значение\
**Описание:** Заменяет текст, соответствующий указанному регулярному выражению, и присваивает результат к переменной. Аргумент "Замена" может содержать $\<название группы\> для ссылки на группу. Включайте только те флаги, которые вам нужны!

**Пример использования:**
```ts
`variable` = variable::regex_replace_text("text", "regex", "replacement", "ANY", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Или от объекта

`variable` = "text".regex_replace_text("regex", "replacement", "ANY", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Или в сухую позиционно

variable::regex_replace_text(`variable`, "text", "regex", "replacement", "ANY", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Или в сухую по ключам

variable::regex_replace_text(variable=`variable`, text="text", regex="regex", replacement="replacement", first="ANY", ignore_case="FALSE", multiline="FALSE", literal="FALSE", unix_lines="FALSE", comments="FALSE", dot_matches_all="FALSE", cannon_eq="FALSE");
```

**Аргументы:**

| ID              | Тип                                                                                            | Описание                                                       |
|-----------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| variable        | Переменная\[Текст\]                                                                            | Переменная для присвоения                                      |
| text            | Текст                                                                                          | Исходный текст                                                 |
| regex           | Текст                                                                                          | Регулярное выражение                                           |
| replacement     | Текст                                                                                          | Замена                                                         |
| first           | Маркер<br/>**ANY** - Заменить все совпадения<br/>**FIRST** - Заменить только первое совпадение | Количество замен                                               |
| ignore_case     | Маркер<br/>**FALSE** - Выключено<br/>**TRUE** - Включено                                       | Игнорировать регистр (флаг ignore_case)                        |
| multiline       | Маркер<br/>**FALSE** - Выключен<br/>**TRUE** - Включён                                         | Многострочный режим (флаг multiline)                           |
| literal         | Маркер<br/>**FALSE** - Выключено<br/>**TRUE** - Включено                                       | Воспринимать шаблон дословно (флаг literal)                    |
| unix_lines      | Маркер<br/>**FALSE** - Выключен<br/>**TRUE** - Включён                                         | Режим UNIX строк (флаг unix_lines)                             |
| comments        | Маркер<br/>**FALSE** - Выключено<br/>**TRUE** - Включено                                       | Разрешить комментарии и игнорирование пробелов (флаг comments) |
| dot_matches_all | Маркер<br/>**FALSE** - Выключен<br/>**TRUE** - Включён                                         | Режим dotall (флаг dotall)                                     |
| cannon_eq       | Маркер<br/>**FALSE** - Выключено<br/>**TRUE** - Включено                                       | Каноническая эквивалентность (флаг cannon_eq)                  |

<h3 id=set_variable_remainder>
  <code>variable::remainder</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Остаток от деления (%)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной остаток от деления двух чисел.

**Пример использования:**
```ts
`variable` = variable::remainder(1, 2, "MODULO");

//Или от объекта

`variable` = (1).remainder(2, "MODULO");

//Или в сухую позиционно

variable::remainder(`variable`, 1, 2, "MODULO");

//Или в сухую по ключам

variable::remainder(variable=`variable`, dividend=1, divisor=2, remainder_mode="MODULO");
```

**Аргументы:**

| ID             | Тип                                                                                                                                  | Описание                  |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable       | Переменная\[Число\]                                                                                                                  | Переменная для присвоения |
| dividend       | Число                                                                                                                                | Делимое                   |
| divisor        | Число                                                                                                                                | Делитель                  |
| remainder_mode | Маркер<br/>**MODULO** - Остаток по модулю (оставляет знак делителя)<br/>**REMAINDER** - Остаток от деления (оставляет знак делимого) | Режим работы              |

<h3 id=set_variable_remove_compass_lodestone>
  <code>variable::remove_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить местоположение магнетита\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет с намагниченного компаса местоположение магнетита и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::remove_compass_lodestone(item("stick"));

//Или от объекта

`variable` = item("stick").remove_compass_lodestone();

//Или в сухую позиционно

variable::remove_compass_lodestone(`variable`, item("stick"));

//Или в сухую по ключам

variable::remove_compass_lodestone(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Намагниченный компас      |

<h3 id=set_variable_remove_enchantment>
  <code>variable::remove_enchantment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить зачарование предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет зачарование с предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::remove_enchantment(item("stick"), "enchantment");

//Или от объекта

`variable` = item("stick").remove_enchantment("enchantment");

//Или в сухую позиционно

variable::remove_enchantment(`variable`, item("stick"), "enchantment");

//Или в сухую по ключам

variable::remove_enchantment(variable=`variable`, item=item("stick"), enchantment="enchantment");
```

**Аргументы:**

| ID          | Тип                   | Описание                  |
|-------------|-----------------------|---------------------------|
| variable    | Переменная\[Предмет\] | Переменная для присвоения |
| item        | Предмет               | Предмет                   |
| enchantment | Текст                 | ID зачарования            |

<h3 id=set_variable_remove_item_attribute>
  <code>variable::remove_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить атрибут у предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет атрибут у предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::remove_item_attribute(item("stick"), "name_or_uuid", "ARMOR");

//Или от объекта

`variable` = item("stick").remove_item_attribute("name_or_uuid", "ARMOR");

//Или в сухую позиционно

variable::remove_item_attribute(`variable`, item("stick"), "name_or_uuid", "ARMOR");

//Или в сухую по ключам

variable::remove_item_attribute(variable=`variable`, item=item("stick"), name_or_uuid="name_or_uuid", attribute="ARMOR");
```

**Аргументы:**

| ID           | Тип                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Описание                  |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable     | Переменная\[Предмет\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Переменная для присвоения |
| item         | Предмет                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Предмет                   |
| name_or_uuid | Текст                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Имя или UUID атрибута     |
| attribute    | Маркер<br/>**ARMOR** - Броня<br/>**ARMOR_TOUGHNESS** - Плотность защиты<br/>**ATTACK_DAMAGE** - Урон атаки<br/>**ATTACK_KNOCKBACK** - Отталкивание от атаки<br/>**ATTACK_SPEED** - Скорость атаки<br/>**FLYING_SPEED** - Скорость полёта<br/>**FOLLOW_RANGE** - Расстояние следования<br/>**GENERIC_ARMOR** - Очки защиты (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Очки плотности защиты (generic.armor_toughness)<br/>**GENERIC_ATTACK_DAMAGE** - Урон атаки (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Отталкивание атаки (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Скорость атаки (generic.attack_speed)<br/>**GENERIC_BURNING_TIME** - Время горения<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Сопротивление отбрасыванию от взрыва<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Множитель урона от падения<br/>**GENERIC_FLYING_SPEED** - Скорость полёта (generic.flying_speed)<br/>**GENERIC_FOLLOW_RANGE** - Расстояние следования (generic.follow_range)<br/>**GENERIC_GRAVITY** - Гравитация<br/>**GENERIC_JUMP_STRENGTH** - Сила прыжка<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Сопротивление отталкиванию (generic.knockback_resistance)<br/>**GENERIC_LUCK** - Удача рыбалки (generic.luck)<br/>**GENERIC_MAX_ABSORPTION** - Максимальное поглощение (generic.max_absorption)<br/>**GENERIC_MAX_HEALTH** - Максимальное здоровье (generic.max_health)<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Скорость передвижения по замедляющим блокам<br/>**GENERIC_MOVEMENT_SPEED** - Скорость передвижения (generic.movement_speed)<br/>**GENERIC_OXYGEN_BONUS** - Воздух под водой<br/>**GENERIC_SAFE_FALL_DISTANCE** - Безопасная высота падения<br/>**GENERIC_SCALE** - Масштаб<br/>**GENERIC_STEP_HEIGHT** - Высота шага<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Скорость передвижения под водой<br/>**HORSE_JUMP_STRENGTH** - Сила прыжка лошади (horse.jump_strength)<br/>**KNOCKBACK_RESISTANCE** - Сопротивление отталкиванию<br/>**LUCK** - Удача<br/>**MAX_ABSORPTION** - Максимальное поглощение<br/>**MAX_HEALTH** - Максимальное здоровье<br/>**MOVEMENT_SPEED** - Скорость передвижения<br/>**PLAYER_BLOCK_BREAK_SPEED** - Скорость ломания блока<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - Расстояние взаимодействия с блоками<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - Расстояние взаимодействия с сущностями<br/>**PLAYER_MINING_EFFICIENCY** - Скорость копания<br/>**PLAYER_SNEAKING_SPEED** - Скорость передвижения крадясь<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Скорость копания под водой<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - Коэффициент разящего удара<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Шанс подкрепления зомби (zombie.spawn_reinforcements) | Тип атрибута              |

<h3 id=set_variable_remove_item_custom_model_data>
  <code>variable::remove_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить данные модели предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет данные модели предмета (CustomModelData) и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::remove_item_custom_model_data(item("stick"));

//Или от объекта

`variable` = item("stick").remove_item_custom_model_data();

//Или в сухую позиционно

variable::remove_item_custom_model_data(`variable`, item("stick"));

//Или в сухую по ключам

variable::remove_item_custom_model_data(variable=`variable`, item=item("stick"));
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |

<h3 id=set_variable_remove_item_custom_tag>
  <code>variable::remove_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить кастомный тег предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет кастомный тег предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::remove_item_custom_tag(item("stick"), "tag_name");

//Или от объекта

`variable` = item("stick").remove_item_custom_tag("tag_name");

//Или в сухую позиционно

variable::remove_item_custom_tag(`variable`, item("stick"), "tag_name");

//Или в сухую по ключам

variable::remove_item_custom_tag(variable=`variable`, item=item("stick"), tag_name="tag_name");
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |
| tag_name | Текст                 | Имя тега                  |

<h3 id=set_variable_remove_item_lore_line>
  <code>variable::remove_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить строку описания предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет строку описания предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::remove_item_lore_line(item("stick"), 1);

//Или от объекта

`variable` = item("stick").remove_item_lore_line(1);

//Или в сухую позиционно

variable::remove_item_lore_line(`variable`, item("stick"), 1);

//Или в сухую по ключам

variable::remove_item_lore_line(variable=`variable`, item=item("stick"), line=1);
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |
| line     | Число                 | Номер строки              |

<h3 id=set_variable_remove_item_potion_effects>
  <code>variable::remove_item_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить эффекты зелий из предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет эффекты зелий из предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::remove_item_potion_effects([potion("slow_falling"), potion("slow_falling")], item("stick"));

//Или от объекта

`variable` = item("stick").remove_item_potion_effects([potion("slow_falling"), potion("slow_falling")]);

//Или в сухую позиционно

variable::remove_item_potion_effects(`variable`, [potion("slow_falling"), potion("slow_falling")], item("stick"));

//Или в сухую по ключам

variable::remove_item_potion_effects(variable=`variable`, effects=[potion("slow_falling"), potion("slow_falling")], item=item("stick"));
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Предмет\]                                 | Переменная для присвоения |
| effects  | Message 'actions.array' not found in 'ru_RU'\[Зелье\] | Эффекты зелий             |
| item     | Предмет                                               | Предмет                   |

<h3 id=set_variable_remove_list_duplicates>
  <code>variable::remove_list_duplicates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить повторяющиеся значения\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет все значения, которые попадаются в списке больше одного раза.

**Пример использования:**
```ts
`variable` = variable::remove_list_duplicates([`list`, `list`]);

//Или от объекта

`variable` = [`list`, `list`].remove_list_duplicates();

//Или в сухую позиционно

variable::remove_list_duplicates(`variable`, [`list`, `list`]);

//Или в сухую по ключам

variable::remove_list_duplicates(variable=`variable`, list=[`list`, `list`]);
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| list     | Список               | Список                    |

<h3 id=set_variable_remove_list_value>
  <code>variable::remove_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить значение из списка\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет указанное значение из списка.

**Пример использования:**
```ts
`variable` = variable::remove_list_value([`list`, `list`], "any value", "ALL");

//Или от объекта

`variable` = [`list`, `list`].remove_list_value("any value", "ALL");

//Или в сухую позиционно

variable::remove_list_value(`variable`, [`list`, `list`], "any value", "ALL");

//Или в сухую по ключам

variable::remove_list_value(variable=`variable`, list=[`list`, `list`], value="any value", remove_mode="ALL");
```

**Аргументы:**

| ID          | Тип                                                                                                       | Описание                  |
|-------------|-----------------------------------------------------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Список\]                                                                                      | Переменная для присвоения |
| list        | Список                                                                                                    | Список                    |
| value       | Любое значение                                                                                            | Значение                  |
| remove_mode | Маркер<br/>**ALL** - Все совпадения<br/>**FIRST** - Первое совпадение<br/>**LAST** - Последнее совпадение | Режим удаления            |

<h3 id=set_variable_remove_list_value_at_index>
  <code>variable::remove_list_value_at_index</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить значение из списка по индексу\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет значение из списка, которое находится по указанному индексу.

**Пример использования:**
```ts
`variable`, `removed_value` = variable::remove_list_value_at_index([`list`, `list`], 1);

//Или от объекта

`variable`, `removed_value` = [`list`, `list`].remove_list_value_at_index(1);

//Или в сухую позиционно

variable::remove_list_value_at_index(`removed_value`, `variable`, [`list`, `list`], 1);

//Или в сухую по ключам

variable::remove_list_value_at_index(removed_value=`removed_value`, variable=`variable`, list=[`list`, `list`], index=1);
```

**Аргументы:**

| ID            | Тип                          | Описание                  |
|---------------|------------------------------|---------------------------|
| removed_value | Переменная\[Любое значение\] | Удалённое значение        |
| variable      | Переменная\[Список\]         | Переменная для присвоения |
| list          | Список                       | Список                    |
| index         | Число                        | Индекс                    |

<h3 id=set_variable_remove_map_entry>
  <code>variable::remove_map_entry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить элемент словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет элемент словаря и присваивает результат к переменной.

**Пример использования:**
```ts
`variable`, `removed_value` = variable::remove_map_entry({"map":`map`}, "any value", ["any value", "any value"]);

//Или от объекта

`variable`, `removed_value` = {"map":`map`}.remove_map_entry("any value", ["any value", "any value"]);

//Или в сухую позиционно

variable::remove_map_entry(`removed_value`, `variable`, {"map":`map`}, "any value", ["any value", "any value"]);

//Или в сухую по ключам

variable::remove_map_entry(removed_value=`removed_value`, variable=`variable`, map={"map":`map`}, key="any value", values=["any value", "any value"]);
```

**Аргументы:**

| ID            | Тип                                                            | Описание                  |
|---------------|----------------------------------------------------------------|---------------------------|
| removed_value | Переменная\[Любое значение\]                                   | Удалённое значение        |
| variable      | Переменная\[Словарь\]                                          | Переменная для присвоения |
| map           | Словарь                                                        | Словарь для изменения     |
| key           | Любое значение                                                 | Ключ                      |
| values        | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Значения                  |

<h3 id=set_variable_remove_text>
  <code>variable::remove_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить текст\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет весь текст или его часть и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::remove_text(["remove", "remove"], "text", "FALSE");

//Или от объекта

`variable` = "text".remove_text(["remove", "remove"], "FALSE");

//Или в сухую позиционно

variable::remove_text(`variable`, ["remove", "remove"], "text", "FALSE");

//Или в сухую по ключам

variable::remove_text(variable=`variable`, remove=["remove", "remove"], text="text", regex="FALSE");
```

**Аргументы:**

| ID       | Тип                                                      | Описание                  |
|----------|----------------------------------------------------------|---------------------------|
| variable | Переменная\[Текст\]                                      | Переменная для присвоения |
| remove   | Message 'actions.array' not found in 'ru_RU'\[Текст\]    | Текст для удаления        |
| text     | Текст                                                    | Исходный текст            |
| regex    | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Регулярные выражения      |

<h3 id=set_variable_repeat_text>
  <code>variable::repeat_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Повторить текст\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной текст, повторённый определённое количество раз.

**Пример использования:**
```ts
`variable` = variable::repeat_text("text", 1);

//Или от объекта

`variable` = "text".repeat_text(1);

//Или в сухую позиционно

variable::repeat_text(`variable`, "text", 1);

//Или в сухую по ключам

variable::repeat_text(variable=`variable`, text="text", repeat=1);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| text     | Текст               | Текст для повторения      |
| repeat   | Число               | Количество повторений     |

<h3 id=set_variable_replace_text>
  <code>variable::replace_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заменить текст\
**Тип:** Действие, возращающее значение\
**Описание:** Заменяет весь текст или его часть и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::replace_text("text", "replace", "replacement", "ANY", "FALSE");

//Или от объекта

`variable` = "text".replace_text("replace", "replacement", "ANY", "FALSE");

//Или в сухую позиционно

variable::replace_text(`variable`, "text", "replace", "replacement", "ANY", "FALSE");

//Или в сухую по ключам

variable::replace_text(variable=`variable`, text="text", replace="replace", replacement="replacement", first="ANY", ignore_case="FALSE");
```

**Аргументы:**

| ID          | Тип                                                                                            | Описание                  |
|-------------|------------------------------------------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Текст\]                                                                            | Переменная для присвоения |
| text        | Текст                                                                                          | Исходный текст            |
| replace     | Текст                                                                                          | Текст для замены          |
| replacement | Текст                                                                                          | Замена                    |
| first       | Маркер<br/>**ANY** - Заменить все совпадения<br/>**FIRST** - Заменить только первое совпадение | Количество замен          |
| ignore_case | Маркер<br/>**FALSE** - Не игнорировать<br/>**TRUE** - Игнорировать                             | Игнорировать регистр      |

<h3 id=set_variable_reverse_list>
  <code>variable::reverse_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Перевернуть список\
**Тип:** Действие, возращающее значение\
**Описание:** Меняет порядок следования элементов на обратный.

**Пример использования:**
```ts
`variable` = variable::reverse_list([`list`, `list`]);

//Или от объекта

`variable` = [`list`, `list`].reverse_list();

//Или в сухую позиционно

variable::reverse_list(`variable`, [`list`, `list`]);

//Или в сухую по ключам

variable::reverse_list(variable=`variable`, list=[`list`, `list`]);
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| list     | Список               | Список                    |

<h3 id=set_variable_root>
  <code>variable::root</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Корень числа (√)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение корня с выбранным подкоренным числом и показателем.

**Пример использования:**
```ts
`variable` = variable::root(1, 2);

//Или в сухую позиционно

variable::root(`variable`, 1, 2);

//Или в сухую по ключам

variable::root(variable=`variable`, base=1, root=2);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| base     | Число               | Подкоренное число         |
| root     | Число               | Показатель корня          |

<h3 id=set_variable_rotate_vector_around_axis>
  <code>variable::rotate_vector_around_axis</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Повернуть вектор вокруг оси\
**Тип:** Действие, возращающее значение\
**Описание:** Поворачивает вектор вокруг оси на определённое значение и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::rotate_vector_around_axis(vector(0,0,0), 1, "X", "DEGREES");

//Или от объекта

`variable` = vector(0,0,0).rotate_vector_around_axis(1, "X", "DEGREES");

//Или в сухую позиционно

variable::rotate_vector_around_axis(`variable`, vector(0,0,0), 1, "X", "DEGREES");

//Или в сухую по ключам

variable::rotate_vector_around_axis(variable=`variable`, vector=vector(0,0,0), angle=1, axis="X", angle_units="DEGREES");
```

**Аргументы:**

| ID          | Тип                                                                               | Описание                  |
|-------------|-----------------------------------------------------------------------------------|---------------------------|
| variable    | Переменная\[Вектор\]                                                              | Переменная для присвоения |
| vector      | Вектор                                                                            | Вектор для изменения      |
| angle       | Число                                                                             | Угол поворота             |
| axis        | Маркер<br/>**X** - Координата X<br/>**Y** - Координата Y<br/>**Z** - Координата Z | Тип координаты            |
| angle_units | Маркер<br/>**DEGREES** - Градусы<br/>**RADIANS** - Радианы                        | Тип угла                  |

<h3 id=set_variable_rotate_vector_around_vector>
  <code>variable::rotate_vector_around_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Повернуть вектор вокруг другого вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Поворачивает вектор вокруг другого вектора на определённое значение и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::rotate_vector_around_vector(vector(0,0,0), vector(0,0,0), 1, "DEGREES");

//Или от объекта

`variable` = vector(0,0,0).rotate_vector_around_vector(vector(0,0,0), 1, "DEGREES");

//Или в сухую позиционно

variable::rotate_vector_around_vector(`variable`, vector(0,0,0), vector(0,0,0), 1, "DEGREES");

//Или в сухую по ключам

variable::rotate_vector_around_vector(variable=`variable`, rotating_vector=vector(0,0,0), axis_vector=vector(0,0,0), angle=1, angle_units="DEGREES");
```

**Аргументы:**

| ID              | Тип                                                        | Описание                  |
|-----------------|------------------------------------------------------------|---------------------------|
| variable        | Переменная\[Вектор\]                                       | Переменная для присвоения |
| rotating_vector | Вектор                                                     | Вектор для изменения      |
| axis_vector     | Вектор                                                     | Осевой вектор             |
| angle           | Число                                                      | Угол поворота             |
| angle_units     | Маркер<br/>**DEGREES** - Градусы<br/>**RADIANS** - Радианы | Тип угла                  |

<h3 id=set_variable_round>
  <code>variable::round</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Округлить число\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной округлённое выбранным способом число.

**Пример использования:**
```ts
`variable` = variable::round(1, 2, "CEIL");

//Или от объекта

`variable` = (1).round(2, "CEIL");

//Или в сухую позиционно

variable::round(`variable`, 1, 2, "CEIL");

//Или в сухую по ключам

variable::round(variable=`variable`, number=1, precision=2, round_type="CEIL");
```

**Аргументы:**

| ID         | Тип                                                                                                                    | Описание                          |
|------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| variable   | Переменная\[Число\]                                                                                                    | Переменная для присвоения         |
| number     | Число                                                                                                                  | Число для округления              |
| precision  | Число                                                                                                                  | Количество цифр после целой части |
| round_type | Маркер<br/>**CEIL** - Округление до большего<br/>**FLOOR** - Округление до меньшего<br/>**ROUND** - Обычное округление | Способ округления                 |

<h3 id=set_variable_set_all_coordinates>
  <code>variable::set_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать местоположение\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт местоположение из указанных координат.

**Пример использования:**
```ts
`variable` = variable::set_all_coordinates(1, 2, 3, 4, 5);

//Или в сухую позиционно

variable::set_all_coordinates(`variable`, 1, 2, 3, 4, 5);

//Или в сухую по ключам

variable::set_all_coordinates(variable=`variable`, x=1, y=2, z=3, yaw=4, pitch=5);
```

**Аргументы:**

| ID       | Тип                          | Описание                  |
|----------|------------------------------|---------------------------|
| variable | Переменная\[Местоположение\] | Переменная для присвоения |
| x        | Число                        | Координата X              |
| y        | Число                        | Координата Y              |
| z        | Число                        | Координата Z              |
| yaw      | Число                        | Горизонтальный поворот    |
| pitch    | Число                        | Вертикальный поворот      |

<h3 id=set_variable_set_armor_trim>
  <code>variable::set_armor_trim</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить броне шаблон\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает броне указанный шаблон и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_armor_trim(item("stick"), item("stick"), item("stick"));

//Или от объекта

`variable` = item("stick").set_armor_trim(item("stick"), item("stick"));

//Или в сухую позиционно

variable::set_armor_trim(`variable`, item("stick"), item("stick"), item("stick"));

//Или в сухую по ключам

variable::set_armor_trim(variable=`variable`, armor=item("stick"), material=item("stick"), pattern=item("stick"));
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| armor    | Предмет               | Броня                     |
| material | Предмет               | Материал шаблона          |
| pattern  | Предмет               | Шаблон                    |

<h3 id=set_variable_set_book_page>
  <code>variable::set_book_page</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить текст книги на странице\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает текст книги на определённой странице и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_book_page(item("stick"), "text", 1, "APPEND");

//Или от объекта

`variable` = item("stick").set_book_page("text", 1, "APPEND");

//Или в сухую позиционно

variable::set_book_page(`variable`, item("stick"), "text", 1, "APPEND");

//Или в сухую по ключам

variable::set_book_page(variable=`variable`, book=item("stick"), text="text", page=1, mode="APPEND");
```

**Аргументы:**

| ID       | Тип                                                       | Описание                  |
|----------|-----------------------------------------------------------|---------------------------|
| variable | Переменная\[Предмет\]                                     | Переменная для присвоения |
| book     | Предмет                                                   | Книга для изменения       |
| text     | Текст                                                     | Новый текст               |
| page     | Число                                                     | Номер страницы            |
| mode     | Маркер<br/>**APPEND** - Добавление<br/>**MERGE** - Замена | Режим установки           |

<h3 id=set_variable_set_book_pages>
  <code>variable::set_book_pages</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить текст книги\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает текст книги и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_book_pages(item("stick"), ["text", "text"]);

//Или от объекта

`variable` = item("stick").set_book_pages(["text", "text"]);

//Или в сухую позиционно

variable::set_book_pages(`variable`, item("stick"), ["text", "text"]);

//Или в сухую по ключам

variable::set_book_pages(variable=`variable`, book=item("stick"), text=["text", "text"]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Предмет\]                                 | Переменная для присвоения |
| book     | Предмет                                               | Книга для изменения       |
| text     | Message 'actions.array' not found in 'ru_RU'\[Текст\] | Новый текст               |

<h3 id=set_variable_set_bundle_items>
  <code>variable::set_bundle_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Изменить содержимое мешка\
**Тип:** Действие, возращающее значение\
**Описание:** Изменяет содержимое мешка и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_bundle_items(item("stick"), [item("stick"), item("stick")], "ADD");

//Или от объекта

`variable` = item("stick").set_bundle_items([item("stick"), item("stick")], "ADD");

//Или в сухую позиционно

variable::set_bundle_items(`variable`, item("stick"), [item("stick"), item("stick")], "ADD");

//Или в сухую по ключам

variable::set_bundle_items(variable=`variable`, bundle=item("stick"), items=[item("stick"), item("stick")], setting_mode="ADD");
```

**Аргументы:**

| ID           | Тип                                                                             | Описание                  |
|--------------|---------------------------------------------------------------------------------|---------------------------|
| variable     | Переменная\[Предмет\]                                                           | Переменная для присвоения |
| bundle       | Предмет                                                                         | Мешок                     |
| items        | Message 'actions.array' not found in 'ru_RU'\[Предмет\]                         | Предметы для изменения    |
| setting_mode | Маркер<br/>**ADD** - Добавить<br/>**REMOVE** - Удалить<br/>**SET** - Установить | Тип изменения             |

<h3 id=set_variable_set_compass_lodestone>
  <code>variable::set_compass_lodestone</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить местоположение магнетита\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает компасу местоположение магнетита и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_compass_lodestone(item("stick"), location(0,0,0,0,0), "FALSE");

//Или от объекта

`variable` = item("stick").set_compass_lodestone(location(0,0,0,0,0), "FALSE");

//Или в сухую позиционно

variable::set_compass_lodestone(`variable`, item("stick"), location(0,0,0,0,0), "FALSE");

//Или в сухую по ключам

variable::set_compass_lodestone(variable=`variable`, item=item("stick"), location=location(0,0,0,0,0), tracked="FALSE");
```

**Аргументы:**

| ID       | Тип                                                          | Описание                            |
|----------|--------------------------------------------------------------|-------------------------------------|
| variable | Переменная\[Предмет\]                                        | Переменная для присвоения           |
| item     | Предмет                                                      | Компас                              |
| location | Местоположение                                               | Местоположение магнетита            |
| tracked  | Маркер<br/>**FALSE** - Не проверять<br/>**TRUE** - Проверять | Наличие магнетита на местоположении |

<h3 id=set_variable_set_component_children>
  <code>variable::set_component_children</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дочерние части стилизуемому тексту\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной стилизуемый текст с указанными дочерними частями.

**Пример использования:**
```ts
`variable` = variable::set_component_children("component", ["children", "children"]);

//Или от объекта

`variable` = "component".set_component_children(["children", "children"]);

//Или в сухую позиционно

variable::set_component_children(`variable`, "component", ["children", "children"]);

//Или в сухую по ключам

variable::set_component_children(variable=`variable`, component="component", children=["children", "children"]);
```

**Аргументы:**

| ID        | Тип                                                   | Описание                    |
|-----------|-------------------------------------------------------|-----------------------------|
| variable  | Переменная\[Текст\]                                   | Переменная для присвоения   |
| component | Текст                                                 | Основный стилизуемый текст  |
| children  | Message 'actions.array' not found in 'ru_RU'\[Текст\] | Дочерние стилизуемые тексты |

<h3 id=set_variable_set_component_click>
  <code>variable::set_component_click</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту действие при нажатии\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту действие при нажатии и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_component_click("component", "value", "CHANGE_PAGE");

//Или от объекта

`variable` = "component".set_component_click("value", "CHANGE_PAGE");

//Или в сухую позиционно

variable::set_component_click(`variable`, "component", "value", "CHANGE_PAGE");

//Или в сухую по ключам

variable::set_component_click(variable=`variable`, component="component", value="value", click_action="CHANGE_PAGE");
```

**Аргументы:**

| ID           | Тип                                                                                                                                                                                                                                                | Описание                  |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable     | Переменная\[Текст\]                                                                                                                                                                                                                                | Переменная для присвоения |
| component    | Текст                                                                                                                                                                                                                                              | Стилизуемый текст         |
| value        | Текст                                                                                                                                                                                                                                              | Значение действия         |
| click_action | Маркер<br/>**CHANGE_PAGE** - Изменить страницу книги<br/>**COPY_TO_CLIPBOARD** - Скопировать в буфер обмена<br/>**COPY_TO_CLIPBORD** - Скопировать в буфер обмена<br/>**OPEN_URL** - Открыть ссылку<br/>**SUGGEST_COMMAND** - Предложить сообщение | Действие при нажатии      |

<h3 id=set_variable_set_component_decorations>
  <code>variable::set_component_decorations</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить декорации стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает декорации указанному стилизуемому тексту и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_component_decorations("component", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Или от объекта

`variable` = "component".set_component_decorations("FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Или в сухую позиционно

variable::set_component_decorations(`variable`, "component", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Или в сухую по ключам

variable::set_component_decorations(variable=`variable`, component="component", bold="FALSE", italic="FALSE", underlined="FALSE", strikethrough="FALSE", obfuscated="FALSE");
```

**Аргументы:**

| ID            | Тип                                                                           | Описание                  |
|---------------|-------------------------------------------------------------------------------|---------------------------|
| variable      | Переменная\[Текст\]                                                           | Переменная для присвоения |
| component     | Текст                                                                         | Стилизуемый текст         |
| bold          | Маркер<br/>**FALSE** - Нет<br/>**NOT_SET** - Не установлено<br/>**TRUE** - Да | Жирный текст              |
| italic        | Маркер<br/>**FALSE** - Нет<br/>**NOT_SET** - Не установлено<br/>**TRUE** - Да | Наклоненный текст         |
| underlined    | Маркер<br/>**FALSE** - Нет<br/>**NOT_SET** - Не установлено<br/>**TRUE** - Да | Подчёркнутый текст        |
| strikethrough | Маркер<br/>**FALSE** - Нет<br/>**NOT_SET** - Не установлено<br/>**TRUE** - Да | Перечёркнутый текст       |
| obfuscated    | Маркер<br/>**FALSE** - Нет<br/>**NOT_SET** - Не установлено<br/>**TRUE** - Да | Зашифрованный текст       |

<h3 id=set_variable_set_component_entity_hover>
  <code>variable::set_component_entity_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту сущность при наведении\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту сущность, отображаемую при наведении, и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_component_entity_hover("component", "name_or_uuid");

//Или от объекта

`variable` = "component".set_component_entity_hover("name_or_uuid");

//Или в сухую позиционно

variable::set_component_entity_hover(`variable`, "component", "name_or_uuid");

//Или в сухую по ключам

variable::set_component_entity_hover(variable=`variable`, component="component", name_or_uuid="name_or_uuid");
```

**Аргументы:**

| ID           | Тип                 | Описание                  |
|--------------|---------------------|---------------------------|
| variable     | Переменная\[Текст\] | Переменная для присвоения |
| component    | Текст               | Стилизуемый текст         |
| name_or_uuid | Текст               | Имя или UUID сущности     |

<h3 id=set_variable_set_component_font>
  <code>variable::set_component_font</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить шрифт стилизуемому тексту\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает шрифт указанному стилизуемому тексту и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_component_font("component", "namespace", "value");

//Или от объекта

`variable` = "component".set_component_font("namespace", "value");

//Или в сухую позиционно

variable::set_component_font(`variable`, "component", "namespace", "value");

//Или в сухую по ключам

variable::set_component_font(variable=`variable`, component="component", namespace="namespace", value="value");
```

**Аргументы:**

| ID        | Тип                 | Описание                             |
|-----------|---------------------|--------------------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения            |
| component | Текст               | Стилизуемый текст                    |
| namespace | Текст               | Пространство имён (minecraft и т.п.) |
| value     | Текст               | ID шрифта                            |

<h3 id=set_variable_set_component_hex_color>
  <code>variable::set_component_hex_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить HEX-цвет стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает HEX-цвет указанному стилизуемому тексту и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_component_hex_color("component", "color");

//Или от объекта

`variable` = "component".set_component_hex_color("color");

//Или в сухую позиционно

variable::set_component_hex_color(`variable`, "component", "color");

//Или в сухую по ключам

variable::set_component_hex_color(variable=`variable`, component="component", color="color");
```

**Аргументы:**

| ID        | Тип                 | Описание                  |
|-----------|---------------------|---------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения |
| component | Текст               | Стилизуемый текст         |
| color     | Текст               | HEX-цвет                  |

<h3 id=set_variable_set_component_hover>
  <code>variable::set_component_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту текст при наведении\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту текст, отображаемый при наведении, и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_component_hover("component", "hover");

//Или от объекта

`variable` = "component".set_component_hover("hover");

//Или в сухую позиционно

variable::set_component_hover(`variable`, "component", "hover");

//Или в сухую по ключам

variable::set_component_hover(variable=`variable`, component="component", hover="hover");
```

**Аргументы:**

| ID        | Тип                 | Описание                                      |
|-----------|---------------------|-----------------------------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения                     |
| component | Текст               | Стилизуемый текст                             |
| hover     | Текст               | Стилизуемый текст, отображаемый при наведении |

<h3 id=set_variable_set_component_insertion>
  <code>variable::set_component_insertion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту предлагаемое сообщение\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту предлагаемое сообщение при нажатии с Shift и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_component_insertion("component", "insertion");

//Или от объекта

`variable` = "component".set_component_insertion("insertion");

//Или в сухую позиционно

variable::set_component_insertion(`variable`, "component", "insertion");

//Или в сухую по ключам

variable::set_component_insertion(variable=`variable`, component="component", insertion="insertion");
```

**Аргументы:**

| ID        | Тип                 | Описание                  |
|-----------|---------------------|---------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения |
| component | Текст               | Стилизуемый текст         |
| insertion | Текст               | Предлагаемое сообщение    |

<h3 id=set_variable_set_component_item_hover>
  <code>variable::set_component_item_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стилизуемому тексту предмет при наведении\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанному стилизуемому тексту предмет, отображаемый при наведении, и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_component_item_hover("component", item("stick"));

//Или от объекта

`variable` = "component".set_component_item_hover(item("stick"));

//Или в сухую позиционно

variable::set_component_item_hover(`variable`, "component", item("stick"));

//Или в сухую по ключам

variable::set_component_item_hover(variable=`variable`, component="component", hover=item("stick"));
```

**Аргументы:**

| ID        | Тип                 | Описание                            |
|-----------|---------------------|-------------------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения           |
| component | Текст               | Стилизуемый текст                   |
| hover     | Предмет             | Предмет, отображаемый при наведении |

<h3 id=set_variable_set_component_shadow_color>
  <code>variable::set_component_shadow_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет тени стилизуемого текста\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает цвет тени указанному стилизуемому тексту и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_component_shadow_color("component", "color");

//Или от объекта

`variable` = "component".set_component_shadow_color("color");

//Или в сухую позиционно

variable::set_component_shadow_color(`variable`, "component", "color");

//Или в сухую по ключам

variable::set_component_shadow_color(variable=`variable`, component="component", color="color");
```

**Аргументы:**

| ID        | Тип                 | Описание                  |
|-----------|---------------------|---------------------------|
| variable  | Переменная\[Текст\] | Переменная для присвоения |
| component | Текст               | Стилизуемый текст         |
| color     | Текст               | HEX цвет                  |

<h3 id=set_variable_set_coordinate>
  <code>variable::set_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить координату местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает значение выбранной координаты в местоположение и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_coordinate(location(0,0,0,0,0), 1, "PITCH");

//Или от объекта

`variable` = location(0,0,0,0,0).set_coordinate(1, "PITCH");

//Или в сухую позиционно

variable::set_coordinate(`variable`, location(0,0,0,0,0), 1, "PITCH");

//Или в сухую по ключам

variable::set_coordinate(variable=`variable`, location=location(0,0,0,0,0), coordinate=1, type="PITCH");
```

**Аргументы:**

| ID         | Тип                                                                                                                                    | Описание                     |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| variable   | Переменная\[Местоположение\]                                                                                                           | Переменная для присвоения    |
| location   | Местоположение                                                                                                                         | Местоположение для установки |
| coordinate | Число                                                                                                                                  | Значение координаты          |
| type       | Маркер<br/>**PITCH** - Вертикальный поворот<br/>**X** - Ось X<br/>**Y** - Ось Y<br/>**YAW** - Горизонтальный поворот<br/>**Z** - Ось Z | Тип координаты               |

<h3 id=set_variable_set_item_amount>
  <code>variable::set_item_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить количество предметов\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает количество предметов в стаке.

**Пример использования:**
```ts
`variable` = variable::set_item_amount(item("stick"), 1);

//Или от объекта

`variable` = item("stick").set_item_amount(1);

//Или в сухую позиционно

variable::set_item_amount(`variable`, item("stick"), 1);

//Или в сухую по ключам

variable::set_item_amount(variable=`variable`, item=item("stick"), amount=1);
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |
| amount   | Число                 | Количество                |

<h3 id=set_variable_set_item_attribute>
  <code>variable::set_item_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить атрибут предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Добавляет определённый атрибут предмету и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_attribute(item("stick"), 1, "name", "ARMOR", "ALL", "ADD_NUMBER");

//Или от объекта

`variable` = item("stick").set_item_attribute(1, "name", "ARMOR", "ALL", "ADD_NUMBER");

//Или в сухую позиционно

variable::set_item_attribute(`variable`, item("stick"), 1, "name", "ARMOR", "ALL", "ADD_NUMBER");

//Или в сухую по ключам

variable::set_item_attribute(variable=`variable`, item=item("stick"), amount=1, name="name", attribute="ARMOR", slot="ALL", operation="ADD_NUMBER");
```

**Аргументы:**

| ID        | Тип                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Описание                  |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable  | Переменная\[Предмет\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Переменная для присвоения |
| item      | Предмет                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Предмет                   |
| amount    | Число                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Значение атрибута         |
| name      | Текст                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Имя атрибута              |
| attribute | Маркер<br/>**ARMOR** - Броня<br/>**ARMOR_TOUGHNESS** - Плотность защиты<br/>**ATTACK_DAMAGE** - Урон атаки<br/>**ATTACK_KNOCKBACK** - Отталкивание от атаки<br/>**ATTACK_SPEED** - Скорость атаки<br/>**FLYING_SPEED** - Скорость полёта<br/>**FOLLOW_RANGE** - Расстояние следования<br/>**GENERIC_ARMOR** - Очки защиты (generic.armor)<br/>**GENERIC_ARMOR_TOUGHNESS** - Очки плотности защиты (generic.armor_toughness)<br/>**GENERIC_ATTACK_DAMAGE** - Урон атаки (generic.attack_damage)<br/>**GENERIC_ATTACK_KNOCKBACK** - Отталкивание атаки (generic.attack_knockback)<br/>**GENERIC_ATTACK_SPEED** - Скорость атаки (generic.attack_speed)<br/>**GENERIC_BURNING_TIME** - Время горения<br/>**GENERIC_EXPLOSION_KNOCKBACK_RESISTANCE** - Сопротивление отбрасыванию от взрыва<br/>**GENERIC_FALL_DAMAGE_MULTIPLIER** - Множитель урона от падения<br/>**GENERIC_FLYING_SPEED** - Скорость полёта (generic.flying_speed)<br/>**GENERIC_FOLLOW_RANGE** - Расстояние следования (generic.follow_range)<br/>**GENERIC_GRAVITY** - Гравитация<br/>**GENERIC_JUMP_STRENGTH** - Сила прыжка<br/>**GENERIC_KNOCKBACK_RESISTANCE** - Сопротивление отталкиванию (generic.knockback_resistance)<br/>**GENERIC_LUCK** - Удача рыбалки (generic.luck)<br/>**GENERIC_MAX_ABSORPTION** - Максимальное поглощение (generic.max_absorption)<br/>**GENERIC_MAX_HEALTH** - Максимальное здоровье (generic.max_health)<br/>**GENERIC_MOVEMENT_EFFICIENCY** - Скорость передвижения по замедляющим блокам<br/>**GENERIC_MOVEMENT_SPEED** - Скорость передвижения (generic.movement_speed)<br/>**GENERIC_OXYGEN_BONUS** - Воздух под водой<br/>**GENERIC_SAFE_FALL_DISTANCE** - Безопасная высота падения<br/>**GENERIC_SCALE** - Масштаб<br/>**GENERIC_STEP_HEIGHT** - Высота шага<br/>**GENERIC_WATER_MOVEMENT_EFFICIENCY** - Скорость передвижения под водой<br/>**HORSE_JUMP_STRENGTH** - Сила прыжка лошади (horse.jump_strength)<br/>**KNOCKBACK_RESISTANCE** - Сопротивление отталкиванию<br/>**LUCK** - Удача<br/>**MAX_ABSORPTION** - Максимальное поглощение<br/>**MAX_HEALTH** - Максимальное здоровье<br/>**MOVEMENT_SPEED** - Скорость передвижения<br/>**PLAYER_BLOCK_BREAK_SPEED** - Скорость ломания блока<br/>**PLAYER_BLOCK_INTERACTION_RANGE** - Расстояние взаимодействия с блоками<br/>**PLAYER_ENTITY_INTERACTION_RANGE** - Расстояние взаимодействия с сущностями<br/>**PLAYER_MINING_EFFICIENCY** - Скорость копания<br/>**PLAYER_SNEAKING_SPEED** - Скорость передвижения крадясь<br/>**PLAYER_SUBMERGED_MINING_SPEED** - Скорость копания под водой<br/>**PLAYER_SWEEPING_DAMAGE_RATIO** - Коэффициент разящего удара<br/>**ZOMBIE_SPAWN_REINFORCEMENTS** - Шанс подкрепления зомби (zombie.spawn_reinforcements) | Тип атрибута              |
| slot      | Маркер<br/>**ALL** - Все<br/>**ARMOR** - Любая броня<br/>**BODY** - Тело (работает не со всеми сущностями)<br/>**BOOTS** - Ботинки<br/>**CHEST** - Нагрудник<br/>**HAND** - Любая рука<br/>**HEAD** - Шлем<br/>**LEGGINGS** - Поножи<br/>**MAIN_HAND** - Основная рука<br/>**OFF_HAND** - Второстепенная рука                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Слот атрибута             |
| operation | Маркер<br/>**ADD_NUMBER** - Количество (amount)<br/>**ADD_SCALAR** - Процент (percentage)<br/>**MULTIPLY_SCALAR_1** - Произведение (multiplicative)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Операция атрибута         |

<h3 id=set_variable_set_item_break_sound>
  <code>variable::set_item_break_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить звук ломания предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает звук, воспроизводимый при поломке указанного предмета, и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_break_sound(item("stick"), "break_sound");

//Или от объекта

`variable` = item("stick").set_item_break_sound("break_sound");

//Или в сухую позиционно

variable::set_item_break_sound(`variable`, item("stick"), "break_sound");

//Или в сухую по ключам

variable::set_item_break_sound(variable=`variable`, item=item("stick"), break_sound="break_sound");
```

**Аргументы:**

| ID          | Тип                   | Описание                  |
|-------------|-----------------------|---------------------------|
| variable    | Переменная\[Предмет\] | Переменная для присвоения |
| item        | Предмет               | Предмет                   |
| break_sound | Текст                 | Звук поломки              |

<h3 id=set_variable_set_item_color>
  <code>variable::set_item_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает указанный цвет предмету и присваивает результат к переменной.\
**Работает с:**\
&nbsp;&nbsp;Кожаной бронёй\
&nbsp;&nbsp;Зельями\
&nbsp;&nbsp;Стрелами с эффектом\
&nbsp;&nbsp;Заполненными картами\
&nbsp;&nbsp;Звёздочками фейерверков

**Пример использования:**
```ts
`variable` = variable::set_item_color(item("stick"), "color");

//Или от объекта

`variable` = item("stick").set_item_color("color");

//Или в сухую позиционно

variable::set_item_color(`variable`, item("stick"), "color");

//Или в сухую по ключам

variable::set_item_color(variable=`variable`, item=item("stick"), color="color");
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |
| color    | Текст                 | Цвет                      |

<h3 id=set_variable_set_item_component>
  <code>variable::set_item_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмету компонент\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает предмету компонент с указанным значением и присваивает предмет к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_component(item("stick"), "component", "any value");

//Или от объекта

`variable` = item("stick").set_item_component("component", "any value");

//Или в сухую позиционно

variable::set_item_component(`variable`, item("stick"), "component", "any value");

//Или в сухую по ключам

variable::set_item_component(variable=`variable`, item=item("stick"), component="component", value="any value");
```

**Аргументы:**

| ID        | Тип                   | Описание        |
|-----------|-----------------------|-----------------|
| variable  | Переменная\[Предмет\] | Переменная      |
| item      | Предмет               | Предмет         |
| component | Текст                 | Ключ компонента |
| value     | Любое значение        | Значение        |

<h3 id=set_variable_set_item_custom_model_data>
  <code>variable::set_item_custom_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить данные модели предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает данные модели предмета (CustomModelData) и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_custom_model_data(item("stick"), 1);

//Или от объекта

`variable` = item("stick").set_item_custom_model_data(1);

//Или в сухую позиционно

variable::set_item_custom_model_data(`variable`, item("stick"), 1);

//Или в сухую по ключам

variable::set_item_custom_model_data(variable=`variable`, item=item("stick"), model=1);
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |
| model    | Число                 | Номер модели              |

<h3 id=set_variable_set_item_custom_tag>
  <code>variable::set_item_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить кастомный тег предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает кастомный тег предмету и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_custom_tag(item("stick"), "tag_name", "tag_value");

//Или от объекта

`variable` = item("stick").set_item_custom_tag("tag_name", "tag_value");

//Или в сухую позиционно

variable::set_item_custom_tag(`variable`, item("stick"), "tag_name", "tag_value");

//Или в сухую по ключам

variable::set_item_custom_tag(variable=`variable`, item=item("stick"), tag_name="tag_name", tag_value="tag_value");
```

**Аргументы:**

| ID        | Тип                   | Описание                  |
|-----------|-----------------------|---------------------------|
| variable  | Переменная\[Предмет\] | Переменная для присвоения |
| item      | Предмет               | Предмет                   |
| tag_name  | Текст                 | Имя тега                  |
| tag_value | Текст                 | Значение тега             |

<h3 id=set_variable_set_item_destroyable_blocks>
  <code>variable::set_item_destroyable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмету блоки для ломания\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает предмету блоки, которые можно им ломать и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_destroyable_blocks([item("stick"), item("stick")], item("stick"));

//Или от объекта

`variable` = item("stick").set_item_destroyable_blocks([item("stick"), item("stick")]);

//Или в сухую позиционно

variable::set_item_destroyable_blocks(`variable`, [item("stick"), item("stick")], item("stick"));

//Или в сухую по ключам

variable::set_item_destroyable_blocks(variable=`variable`, destroyable=[item("stick"), item("stick")], item=item("stick"));
```

**Аргументы:**

| ID          | Тип                                                     | Описание                              |
|-------------|---------------------------------------------------------|---------------------------------------|
| variable    | Переменная\[Предмет\]                                   | Переменная для присвоения             |
| destroyable | Message 'actions.array' not found in 'ru_RU'\[Предмет\] | Блоки, которые можно ломать предметом |
| item        | Предмет                                                 | Предмет                               |

<h3 id=set_variable_set_item_durability>
  <code>variable::set_item_durability</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить прочность предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает прочность предмету и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_durability(item("stick"), 1, "DAMAGE");

//Или от объекта

`variable` = item("stick").set_item_durability(1, "DAMAGE");

//Или в сухую позиционно

variable::set_item_durability(`variable`, item("stick"), 1, "DAMAGE");

//Или в сухую по ключам

variable::set_item_durability(variable=`variable`, item=item("stick"), durability=1, durability_type="DAMAGE");
```

**Аргументы:**

| ID              | Тип                                                                                                                                                                                                                                                                                       | Описание                  |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable        | Переменная\[Предмет\]                                                                                                                                                                                                                                                                     | Переменная для присвоения |
| item            | Предмет                                                                                                                                                                                                                                                                                   | Предмет                   |
| durability      | Число                                                                                                                                                                                                                                                                                     | Новая прочность           |
| durability_type | Маркер<br/>**DAMAGE** - Текущая прочность<br/>**DAMAGE_PERCENTAGE** - Текущий процент прочности<br/>**MAXIMUM** - Максимальная прочность<br/>**MAX_DAMAGE** - Максимальная прочность<br/>**REMAINING** - Остаточная прочность<br/>**REMAINING_PERCENTAGE** - Остаточный процент прочности | Тип прочности             |

<h3 id=set_variable_set_item_enchantments>
  <code>variable::set_item_enchantments</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить зачарования предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает зачарования предмету и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_enchantments(item("stick"), {"enchantments":`enchantments`});

//Или от объекта

`variable` = item("stick").set_item_enchantments({"enchantments":`enchantments`});

//Или в сухую позиционно

variable::set_item_enchantments(`variable`, item("stick"), {"enchantments":`enchantments`});

//Или в сухую по ключам

variable::set_item_enchantments(variable=`variable`, item=item("stick"), enchantments={"enchantments":`enchantments`});
```

**Аргументы:**

| ID           | Тип                   | Описание                  |
|--------------|-----------------------|---------------------------|
| variable     | Переменная\[Предмет\] | Переменная для присвоения |
| item         | Предмет               | Предмет                   |
| enchantments | Словарь               | Зачарования и их уровни   |

<h3 id=set_variable_set_item_food_properties>
  <code>variable::set_item_food_properties</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмету данные компонента еды\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает предмету данные компонента еды и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_food_properties(item("stick"), 1, 2, "TRUE");

//Или от объекта

`variable` = item("stick").set_item_food_properties(1, 2, "TRUE");

//Или в сухую позиционно

variable::set_item_food_properties(`variable`, item("stick"), 1, 2, "TRUE");

//Или в сухую по ключам

variable::set_item_food_properties(variable=`variable`, item=item("stick"), nutrition=1, saturation=2, can_always_eat="TRUE");
```

**Аргументы:**

| ID             | Тип                                          | Описание                      |
|----------------|----------------------------------------------|-------------------------------|
| variable       | Переменная\[Предмет\]                        | Переменная для присвоения     |
| item           | Предмет                                      | Предмет                       |
| nutrition      | Число                                        | Питательность                 |
| saturation     | Число                                        | Насыщение                     |
| can_always_eat | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет | Возможность сьесть без голода |

<h3 id=set_variable_set_item_glider>
  <code>variable::set_item_glider</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмету скольжение\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает предмету скольжение и присваивает результат к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Экипировав предмет, имеющий скольжение, игрок сможет скользить по земле и летать, как если бы на нём были надеты элитры.

**Пример использования:**
```ts
`variable` = variable::set_item_glider(item("stick"), "TRUE");

//Или от объекта

`variable` = item("stick").set_item_glider("TRUE");

//Или в сухую позиционно

variable::set_item_glider(`variable`, item("stick"), "TRUE");

//Или в сухую по ключам

variable::set_item_glider(variable=`variable`, item=item("stick"), glider="TRUE");
```

**Аргументы:**

| ID       | Тип                                          | Описание                  |
|----------|----------------------------------------------|---------------------------|
| variable | Переменная\[Предмет\]                        | Переменная для присвоения |
| item     | Предмет                                      | Предмет                   |
| glider   | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет | Скольжение                |

<h3 id=set_variable_set_item_glint_override>
  <code>variable::set_item_glint_override</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Переопределить свечение предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Переопределяет свечение предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_glint_override(item("stick"), "TRUE");

//Или от объекта

`variable` = item("stick").set_item_glint_override("TRUE");

//Или в сухую позиционно

variable::set_item_glint_override(`variable`, item("stick"), "TRUE");

//Или в сухую по ключам

variable::set_item_glint_override(variable=`variable`, item=item("stick"), glowing="TRUE");
```

**Аргументы:**

| ID       | Тип                                                                         | Описание                  |
|----------|-----------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Предмет\]                                                       | Переменная для присвоения |
| item     | Предмет                                                                     | Предмет                   |
| glowing  | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет<br/>**NOT_SET** - По умолчанию | Свечение                  |

<h3 id=set_variable_set_item_hidden_tooltip>
  <code>variable::set_item_hidden_tooltip</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Скрыть всплывающую подсказку предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Скрывает всплывающую подсказку предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_hidden_tooltip(item("stick"), "TRUE");

//Или от объекта

`variable` = item("stick").set_item_hidden_tooltip("TRUE");

//Или в сухую позиционно

variable::set_item_hidden_tooltip(`variable`, item("stick"), "TRUE");

//Или в сухую по ключам

variable::set_item_hidden_tooltip(variable=`variable`, item=item("stick"), tooltip_hidden="TRUE");
```

**Аргументы:**

| ID             | Тип                                          | Описание                      |
|----------------|----------------------------------------------|-------------------------------|
| variable       | Переменная\[Предмет\]                        | Переменная для присвоения     |
| item           | Предмет                                      | Предмет                       |
| tooltip_hidden | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет | Скрытие всплывающей подсказки |

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
`variable` = variable::set_item_lore(item("stick"), ["lore", "lore"]);

//Или от объекта

`variable` = item("stick").set_item_lore(["lore", "lore"]);

//Или в сухую позиционно

variable::set_item_lore(`variable`, item("stick"), ["lore", "lore"]);

//Или в сухую по ключам

variable::set_item_lore(variable=`variable`, item=item("stick"), lore=["lore", "lore"]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Предмет\]                                 | Переменная для присвоения |
| item     | Предмет                                               | Предмет                   |
| lore     | Message 'actions.array' not found in 'ru_RU'\[Текст\] | Новое описание            |

<h3 id=set_variable_set_item_lore_line>
  <code>variable::set_item_lore_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить строку описания предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает строку описания предмета.

**Пример использования:**
```ts
`variable` = variable::set_item_lore_line(item("stick"), "text", 1, "APPEND");

//Или от объекта

`variable` = item("stick").set_item_lore_line("text", 1, "APPEND");

//Или в сухую позиционно

variable::set_item_lore_line(`variable`, item("stick"), "text", 1, "APPEND");

//Или в сухую по ключам

variable::set_item_lore_line(variable=`variable`, item=item("stick"), text="text", line=1, mode="APPEND");
```

**Аргументы:**

| ID       | Тип                                                       | Описание                  |
|----------|-----------------------------------------------------------|---------------------------|
| variable | Переменная\[Предмет\]                                     | Переменная для присвоения |
| item     | Предмет                                                   | Предмет                   |
| text     | Текст                                                     | Новое описание            |
| line     | Число                                                     | Номер строки              |
| mode     | Маркер<br/>**APPEND** - Добавление<br/>**MERGE** - Замена | Режим установки           |

<h3 id=set_variable_set_item_max_stack_size>
  <code>variable::set_item_max_stack_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить максимальное количество предметов\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает максимальное количество предметов в стаке для указанного предмета и присваивает его к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Количество предметов в стаке может быть лишь от 1 до 99.\
&nbsp;&nbsp;Значение 0 вернёт максимальное количество к значению по умолчанию.

**Пример использования:**
```ts
`variable` = variable::set_item_max_stack_size(item("stick"), 1);

//Или от объекта

`variable` = item("stick").set_item_max_stack_size(1);

//Или в сухую позиционно

variable::set_item_max_stack_size(`variable`, item("stick"), 1);

//Или в сухую по ключам

variable::set_item_max_stack_size(variable=`variable`, item=item("stick"), size=1);
```

**Аргументы:**

| ID       | Тип                   | Описание                     |
|----------|-----------------------|------------------------------|
| variable | Переменная\[Предмет\] | Переменная                   |
| item     | Предмет               | Предмет                      |
| size     | Число                 | Количество предметов в стаке |

<h3 id=set_variable_set_item_model_data>
  <code>variable::set_item_model_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить модель предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает модель указанному предмету и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_model_data(item("stick"), "model");

//Или от объекта

`variable` = item("stick").set_item_model_data("model");

//Или в сухую позиционно

variable::set_item_model_data(`variable`, item("stick"), "model");

//Или в сухую по ключам

variable::set_item_model_data(variable=`variable`, item=item("stick"), model="model");
```

**Аргументы:**

| ID       | Тип                   | Описание                                            |
|----------|-----------------------|-----------------------------------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения                           |
| item     | Предмет               | Предмет                                             |
| model    | Текст                 | Модель предмета (пример: "minecraft:diamond_sword") |

<h3 id=set_variable_set_item_name>
  <code>variable::set_item_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить имя предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает отображаемое имя предмета.

**Пример использования:**
```ts
`variable` = variable::set_item_name(item("stick"), "text");

//Или от объекта

`variable` = item("stick").set_item_name("text");

//Или в сухую позиционно

variable::set_item_name(`variable`, item("stick"), "text");

//Или в сухую по ключам

variable::set_item_name(variable=`variable`, item=item("stick"), text="text");
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |
| text     | Текст                 | Имя                       |

<h3 id=set_variable_set_item_placeable_blocks>
  <code>variable::set_item_placeable_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмету блоки для установки\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает предмету блоки, на которые его можно поставить и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_placeable_blocks([item("stick"), item("stick")], item("stick"));

//Или от объекта

`variable` = item("stick").set_item_placeable_blocks([item("stick"), item("stick")]);

//Или в сухую позиционно

variable::set_item_placeable_blocks(`variable`, [item("stick"), item("stick")], item("stick"));

//Или в сухую по ключам

variable::set_item_placeable_blocks(variable=`variable`, placeable=[item("stick"), item("stick")], item=item("stick"));
```

**Аргументы:**

| ID        | Тип                                                     | Описание                                  |
|-----------|---------------------------------------------------------|-------------------------------------------|
| variable  | Переменная\[Предмет\]                                   | Переменная для присвоения                 |
| placeable | Message 'actions.array' not found in 'ru_RU'\[Предмет\] | Блоки, на которые можно поставить предмет |
| item      | Предмет                                                 | Предмет                                   |

<h3 id=set_variable_set_item_rarity>
  <code>variable::set_item_rarity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить редкость предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает редкость предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_rarity(item("stick"), "NONE");

//Или от объекта

`variable` = item("stick").set_item_rarity("NONE");

//Или в сухую позиционно

variable::set_item_rarity(`variable`, item("stick"), "NONE");

//Или в сухую по ключам

variable::set_item_rarity(variable=`variable`, item=item("stick"), rarity="NONE");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                         | Описание                  |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Предмет\]                                                                                                                                                       | Переменная для присвоения |
| item     | Предмет                                                                                                                                                                     | Предмет                   |
| rarity   | Маркер<br/>**NONE** - Никакая (none)<br/>**COMMON** - Обычная (common)<br/>**UNCOMMON** - Необычная (uncommon)<br/>**RARE** - Редкая (rare)<br/>**EPIC** - Эпическая (epic) | Редкость                  |

<h3 id=set_variable_set_item_tooltip_style>
  <code>variable::set_item_tooltip_style</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стиль всплывающей подсказки предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает стиль всплывающей подсказки предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_tooltip_style(item("stick"), "style");

//Или от объекта

`variable` = item("stick").set_item_tooltip_style("style");

//Или в сухую позиционно

variable::set_item_tooltip_style(`variable`, item("stick"), "style");

//Или в сухую по ключам

variable::set_item_tooltip_style(variable=`variable`, item=item("stick"), style="style");
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |
| style    | Текст                 | Ключ стиля подсказки      |

<h3 id=set_variable_set_item_type>
  <code>variable::set_item_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Меняет тип предмета, не изменяя другие данные предмета.

**Пример использования:**
```ts
`variable` = variable::set_item_type(item("stick"), "type");

//Или от объекта

`variable` = item("stick").set_item_type("type");

//Или в сухую позиционно

variable::set_item_type(`variable`, item("stick"), "type");

//Или в сухую по ключам

variable::set_item_type(variable=`variable`, item=item("stick"), type="type");
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| item     | Предмет               | Предмет                   |
| type     | Текст                 | Тип предмета              |

<h3 id=set_variable_set_item_unbreakable>
  <code>variable::set_item_unbreakable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить неломаемость предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает неломаемость предмету и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_unbreakable(item("stick"), "FALSE");

//Или от объекта

`variable` = item("stick").set_item_unbreakable("FALSE");

//Или в сухую позиционно

variable::set_item_unbreakable(`variable`, item("stick"), "FALSE");

//Или в сухую по ключам

variable::set_item_unbreakable(variable=`variable`, item=item("stick"), unbreakable="FALSE");
```

**Аргументы:**

| ID          | Тип                                                      | Описание                  |
|-------------|----------------------------------------------------------|---------------------------|
| variable    | Переменная\[Предмет\]                                    | Переменная для присвоения |
| item        | Предмет                                                  | Предмет                   |
| unbreakable | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Неломаемость              |

<h3 id=set_variable_set_item_use_remainder>
  <code>variable::set_item_use_remainder</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить превращение предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает предмет, в который превратится указанный предмет после использования и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_use_remainder(item("stick"), item("stick"));

//Или от объекта

`variable` = item("stick").set_item_use_remainder(item("stick"));

//Или в сухую позиционно

variable::set_item_use_remainder(`variable`, item("stick"), item("stick"));

//Или в сухую по ключам

variable::set_item_use_remainder(variable=`variable`, item=item("stick"), remainder=item("stick"));
```

**Аргументы:**

| ID        | Тип                   | Описание                       |
|-----------|-----------------------|--------------------------------|
| variable  | Переменная\[Предмет\] | Переменная для присвоения      |
| item      | Предмет               | Предмет                        |
| remainder | Предмет               | Предмет, в который превратится |

<h3 id=set_variable_set_item_visibility_flags>
  <code>variable::set_item_visibility_flags</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить флаги видимости предмету\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает определённые флаги видимости предмету и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_visibility_flags(item("stick"), "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE");

//Или от объекта

`variable` = item("stick").set_item_visibility_flags("NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE");

//Или в сухую позиционно

variable::set_item_visibility_flags(`variable`, item("stick"), "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE", "NO_CHANGE");

//Или в сухую по ключам

variable::set_item_visibility_flags(variable=`variable`, item=item("stick"), hide_dye="NO_CHANGE", hide_enchantments="NO_CHANGE", hide_attributes="NO_CHANGE", hide_unbreakable="NO_CHANGE", hide_place_on="NO_CHANGE", hide_destroys="NO_CHANGE", hide_potion_effects="NO_CHANGE", hide_armor_trim="NO_CHANGE");
```

**Аргументы:**

| ID                  | Тип                                                                                    | Описание                   |
|---------------------|----------------------------------------------------------------------------------------|----------------------------|
| variable            | Переменная\[Предмет\]                                                                  | Переменная для присвоения  |
| item                | Предмет                                                                                | Предмет                    |
| hide_dye            | Маркер<br/>**NO_CHANGE** - Без изменений<br/>**OFF** - Выключено<br/>**ON** - Включено | Скрытие цвета              |
| hide_enchantments   | Маркер<br/>**NO_CHANGE** - Без изменений<br/>**OFF** - Выключено<br/>**ON** - Включено | Скрытие зачарований        |
| hide_attributes     | Маркер<br/>**NO_CHANGE** - Без изменений<br/>**OFF** - Выключено<br/>**ON** - Включено | Скрытие атрибутов          |
| hide_unbreakable    | Маркер<br/>**NO_CHANGE** - Без изменений<br/>**OFF** - Выключено<br/>**ON** - Включено | Скрытие неразрушимости     |
| hide_place_on       | Маркер<br/>**NO_CHANGE** - Без изменений<br/>**OFF** - Выключено<br/>**ON** - Включено | Скрытие "Можно ставить на" |
| hide_destroys       | Маркер<br/>**NO_CHANGE** - Без изменений<br/>**OFF** - Выключено<br/>**ON** - Включено | Скрытие "Может ломать"     |
| hide_potion_effects | Маркер<br/>**NO_CHANGE** - Без изменений<br/>**OFF** - Выключено<br/>**ON** - Включено | Скрытие характеристик      |
| hide_armor_trim     | Маркер<br/>**NO_CHANGE** - Без изменений<br/>**OFF** - Выключено<br/>**ON** - Включено | Скрытие отделки брони      |

<h3 id=set_variable_set_item_weapon>
  <code>variable::set_item_weapon</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмету данные компонента оружия\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает предмету данные компонента оружия и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_item_weapon(item("stick"), 1, 2);

//Или от объекта

`variable` = item("stick").set_item_weapon(1, 2);

//Или в сухую позиционно

variable::set_item_weapon(`variable`, item("stick"), 1, 2);

//Или в сухую по ключам

variable::set_item_weapon(variable=`variable`, item=item("stick"), item_damage_per_attack=1, disable_blocking=2);
```

**Аргументы:**

| ID                     | Тип                   | Описание                  |
|------------------------|-----------------------|---------------------------|
| variable               | Переменная\[Предмет\] | Переменная для присвоения |
| item                   | Предмет               | Предмет                   |
| item_damage_per_attack | Число                 | Урон от атаки             |
| disable_blocking       | Число                 | Задержка щита после удара |

<h3 id=set_variable_set_list_value>
  <code>variable::set_list_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить значение списка\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает значение списка по указанному индексу.

**Пример использования:**
```ts
`variable` = variable::set_list_value([`list`, `list`], 1, "any value");

//Или от объекта

`variable` = [`list`, `list`].set_list_value(1, "any value");

//Или в сухую позиционно

variable::set_list_value(`variable`, [`list`, `list`], 1, "any value");

//Или в сухую по ключам

variable::set_list_value(variable=`variable`, list=[`list`, `list`], number=1, value="any value");
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| list     | Список               | Список                    |
| number   | Число                | Индекс                    |
| value    | Любое значение       | Значение                  |

<h3 id=set_variable_set_location_direction>
  <code>variable::set_location_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить направление местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает направление местоположения и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_location_direction(location(0,0,0,0,0), vector(0,0,0));

//Или от объекта

`variable` = location(0,0,0,0,0).set_location_direction(vector(0,0,0));

//Или в сухую позиционно

variable::set_location_direction(`variable`, location(0,0,0,0,0), vector(0,0,0));

//Или в сухую по ключам

variable::set_location_direction(variable=`variable`, location=location(0,0,0,0,0), vector=vector(0,0,0));
```

**Аргументы:**

| ID       | Тип                          | Описание                     |
|----------|------------------------------|------------------------------|
| variable | Переменная\[Местоположение\] | Переменная для присвоения    |
| location | Местоположение               | Местоположение для установки |
| vector   | Вектор                       | Вектор направления           |

<h3 id=set_variable_set_map_value>
  <code>variable::set_map_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить значение словаря\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает определённое значение словаря по ключу и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_map_value({"map":`map`}, ["any value", "any value"], ["any value", "any value"]);

//Или от объекта

`variable` = {"map":`map`}.set_map_value(["any value", "any value"], ["any value", "any value"]);

//Или в сухую позиционно

variable::set_map_value(`variable`, {"map":`map`}, ["any value", "any value"], ["any value", "any value"]);

//Или в сухую по ключам

variable::set_map_value(variable=`variable`, map={"map":`map`}, key=["any value", "any value"], value=["any value", "any value"]);
```

**Аргументы:**

| ID       | Тип                                                            | Описание                  |
|----------|----------------------------------------------------------------|---------------------------|
| variable | Переменная\[Словарь\]                                          | Переменная для присвоения |
| map      | Словарь                                                        | Словарь для изменения     |
| key      | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Ключ                      |
| value    | Message 'actions.array' not found in 'ru_RU'\[Любое значение\] | Новое значение            |

<h3 id=set_variable_set_particle_amount>
  <code>variable::set_particle_amount</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить количество частиц\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает количество частиц и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_particle_amount(particle("fire"), 1);

//Или от объекта

`variable` = particle("fire").set_particle_amount(1);

//Или в сухую позиционно

variable::set_particle_amount(`variable`, particle("fire"), 1);

//Или в сухую по ключам

variable::set_particle_amount(variable=`variable`, particle=particle("fire"), amount=1);
```

**Аргументы:**

| ID       | Тип                         | Описание                  |
|----------|-----------------------------|---------------------------|
| variable | Переменная\[Эффект частиц\] | Переменная для присвоения |
| particle | Эффект частиц               | Частица для изменения     |
| amount   | Число                       | Новое количество          |

<h3 id=set_variable_set_particle_color>
  <code>variable::set_particle_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает цвет частицы и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_particle_color(particle("fire"), "hex_color", "COLOR");

//Или от объекта

`variable` = particle("fire").set_particle_color("hex_color", "COLOR");

//Или в сухую позиционно

variable::set_particle_color(`variable`, particle("fire"), "hex_color", "COLOR");

//Или в сухую по ключам

variable::set_particle_color(variable=`variable`, particle=particle("fire"), hex_color="hex_color", color_type="COLOR");
```

**Аргументы:**

| ID         | Тип                                                                  | Описание                  |
|------------|----------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Эффект частиц\]                                          | Переменная для присвоения |
| particle   | Эффект частиц                                                        | Частица для изменения     |
| hex_color  | Текст                                                                | HEX цвет                  |
| color_type | Маркер<br/>**COLOR** - Обычный цвет<br/>**TO_COLOR** - Цвет перехода | Тип цвета                 |

<h3 id=set_variable_set_particle_material>
  <code>variable::set_particle_material</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить материал частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает материал частицы и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_particle_material(particle("fire"), item("stick"));

//Или от объекта

`variable` = particle("fire").set_particle_material(item("stick"));

//Или в сухую позиционно

variable::set_particle_material(`variable`, particle("fire"), item("stick"));

//Или в сухую по ключам

variable::set_particle_material(variable=`variable`, particle=particle("fire"), material=item("stick"));
```

**Аргументы:**

| ID       | Тип                         | Описание                  |
|----------|-----------------------------|---------------------------|
| variable | Переменная\[Эффект частиц\] | Переменная для присвоения |
| particle | Эффект частиц               | Частица для изменения     |
| material | Предмет                     | Новый материал            |

<h3 id=set_variable_set_particle_offset>
  <code>variable::set_particle_offset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить движение частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает движение частицы и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_particle_offset(particle("fire"), vector(0,0,0));

//Или от объекта

`variable` = particle("fire").set_particle_offset(vector(0,0,0));

//Или в сухую позиционно

variable::set_particle_offset(`variable`, particle("fire"), vector(0,0,0));

//Или в сухую по ключам

variable::set_particle_offset(variable=`variable`, particle=particle("fire"), offset=vector(0,0,0));
```

**Аргументы:**

| ID       | Тип                         | Описание                  |
|----------|-----------------------------|---------------------------|
| variable | Переменная\[Эффект частиц\] | Переменная для присвоения |
| particle | Эффект частиц               | Частица для изменения     |
| offset   | Вектор                      | Новое движение            |

<h3 id=set_variable_set_particle_size>
  <code>variable::set_particle_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить размер частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает размер частицы и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_particle_size(particle("fire"), 1);

//Или от объекта

`variable` = particle("fire").set_particle_size(1);

//Или в сухую позиционно

variable::set_particle_size(`variable`, particle("fire"), 1);

//Или в сухую по ключам

variable::set_particle_size(variable=`variable`, particle=particle("fire"), size=1);
```

**Аргументы:**

| ID       | Тип                         | Описание                  |
|----------|-----------------------------|---------------------------|
| variable | Переменная\[Эффект частиц\] | Переменная для присвоения |
| particle | Эффект частиц               | Частица для изменения     |
| size     | Число                       | Новый размер              |

<h3 id=set_variable_set_particle_spread>
  <code>variable::set_particle_spread</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить разброс частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение разброса частицы.

**Пример использования:**
```ts
`variable` = variable::set_particle_spread(particle("fire"), 1, 2);

//Или от объекта

`variable` = particle("fire").set_particle_spread(1, 2);

//Или в сухую позиционно

variable::set_particle_spread(`variable`, particle("fire"), 1, 2);

//Или в сухую по ключам

variable::set_particle_spread(variable=`variable`, particle=particle("fire"), horizontal=1, vertical=2);
```

**Аргументы:**

| ID         | Тип                         | Описание                  |
|------------|-----------------------------|---------------------------|
| variable   | Переменная\[Эффект частиц\] | Переменная для присвоения |
| particle   | Эффект частиц               | Частица для изменения     |
| horizontal | Число                       | Горизонтальная плоскость  |
| vertical   | Число                       | Вертикальная плоскость    |

<h3 id=set_variable_set_particle_type>
  <code>variable::set_particle_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип частицы\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает тип частицы и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_particle_type(particle("fire"), "type");

//Или от объекта

`variable` = particle("fire").set_particle_type("type");

//Или в сухую позиционно

variable::set_particle_type(`variable`, particle("fire"), "type");

//Или в сухую по ключам

variable::set_particle_type(variable=`variable`, particle=particle("fire"), type="type");
```

**Аргументы:**

| ID       | Тип                         | Описание                  |
|----------|-----------------------------|---------------------------|
| variable | Переменная\[Эффект частиц\] | Переменная для присвоения |
| particle | Эффект частиц               | Частица для изменения     |
| type     | Текст                       | Новый тип частицы         |

<h3 id=set_variable_set_potion_effect_amplifier>
  <code>variable::set_potion_effect_amplifier</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить силу зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает силу зелью и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_potion_effect_amplifier(potion("slow_falling"), 1);

//Или от объекта

`variable` = potion("slow_falling").set_potion_effect_amplifier(1);

//Или в сухую позиционно

variable::set_potion_effect_amplifier(`variable`, potion("slow_falling"), 1);

//Или в сухую по ключам

variable::set_potion_effect_amplifier(variable=`variable`, potion=potion("slow_falling"), amplifier=1);
```

**Аргументы:**

| ID        | Тип                 | Описание                  |
|-----------|---------------------|---------------------------|
| variable  | Переменная\[Зелье\] | Переменная для присвоения |
| potion    | Зелье               | Зелье                     |
| amplifier | Число               | Сила зелья                |

<h3 id=set_variable_set_potion_effect_duration>
  <code>variable::set_potion_effect_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить длительность зелья\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает длительность зелью и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_potion_effect_duration(potion("slow_falling"), 1);

//Или от объекта

`variable` = potion("slow_falling").set_potion_effect_duration(1);

//Или в сухую позиционно

variable::set_potion_effect_duration(`variable`, potion("slow_falling"), 1);

//Или в сухую по ключам

variable::set_potion_effect_duration(variable=`variable`, potion=potion("slow_falling"), duration=1);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Зелье\] | Переменная для присвоения |
| potion   | Зелье               | Зелье                     |
| duration | Число               | Длительность              |

<h3 id=set_variable_set_potion_effect_type>
  <code>variable::set_potion_effect_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить эффект зелью\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает эффект зелью и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_potion_effect_type(potion("slow_falling"), "effect_type");

//Или от объекта

`variable` = potion("slow_falling").set_potion_effect_type("effect_type");

//Или в сухую позиционно

variable::set_potion_effect_type(`variable`, potion("slow_falling"), "effect_type");

//Или в сухую по ключам

variable::set_potion_effect_type(variable=`variable`, potion=potion("slow_falling"), effect_type="effect_type");
```

**Аргументы:**

| ID          | Тип                 | Описание                  |
|-------------|---------------------|---------------------------|
| variable    | Переменная\[Зелье\] | Переменная для присвоения |
| potion      | Зелье               | Зелье                     |
| effect_type | Текст               | ID эффекта                |

<h3 id=set_variable_set_sound_pitch>
  <code>variable::set_sound_pitch</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить высоту звука\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает высоту звука и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_sound_pitch(sound("entity.zombie.hurt"), 1);

//Или от объекта

`variable` = sound("entity.zombie.hurt").set_sound_pitch(1);

//Или в сухую позиционно

variable::set_sound_pitch(`variable`, sound("entity.zombie.hurt"), 1);

//Или в сухую по ключам

variable::set_sound_pitch(variable=`variable`, sound=sound("entity.zombie.hurt"), pitch=1);
```

**Аргументы:**

| ID       | Тип                | Описание                  |
|----------|--------------------|---------------------------|
| variable | Переменная\[Звук\] | Переменная для присвоения |
| sound    | Звук               | Звук для изменения        |
| pitch    | Число              | Новое значение высоты     |

<h3 id=set_variable_set_sound_source>
  <code>variable::set_sound_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить источник звука\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает источник звука и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_sound_source(sound("entity.zombie.hurt"), "AMBIENT");

//Или от объекта

`variable` = sound("entity.zombie.hurt").set_sound_source("AMBIENT");

//Или в сухую позиционно

variable::set_sound_source(`variable`, sound("entity.zombie.hurt"), "AMBIENT");

//Или в сухую по ключам

variable::set_sound_source(variable=`variable`, sound=sound("entity.zombie.hurt"), source="AMBIENT");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                                                                                                                                                                                                                                           | Описание                  |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Звук\]                                                                                                                                                                                                                                                                                                                                                                            | Переменная для присвоения |
| sound    | Звук                                                                                                                                                                                                                                                                                                                                                                                          | Звук для изменения        |
| source   | Маркер<br/>**AMBIENT** - Окружение (ambient)<br/>**BLOCK** - Блоки (block)<br/>**HOSTILE** - Враждебные существа (hostile)<br/>**MASTER** - Общий (master)<br/>**MUSIC** - Музыка (music)<br/>**NEUTRAL** - Дружелюбные существа (neutral)<br/>**PLAYER** - Игроки (player)<br/>**RECORD** - Музыкальные блоки (record)<br/>**VOICE** - Голос/Речь (voice)<br/>**WEATHER** - Погода (weather) | Источник звука            |

<h3 id=set_variable_set_sound_type>
  <code>variable::set_sound_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип звука\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает тип звуку и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_sound_type(sound("entity.zombie.hurt"), "namespace", "value");

//Или от объекта

`variable` = sound("entity.zombie.hurt").set_sound_type("namespace", "value");

//Или в сухую позиционно

variable::set_sound_type(`variable`, sound("entity.zombie.hurt"), "namespace", "value");

//Или в сухую по ключам

variable::set_sound_type(variable=`variable`, sound=sound("entity.zombie.hurt"), namespace="namespace", value="value");
```

**Аргументы:**

| ID        | Тип                | Описание                             |
|-----------|--------------------|--------------------------------------|
| variable  | Переменная\[Звук\] | Переменная для присвоения            |
| sound     | Звук               | Звук для установки                   |
| namespace | Текст              | Пространство имён (minecraft и т.п.) |
| value     | Текст              | ID звука                             |

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
`variable` = variable::set_sound_variation(sound("entity.zombie.hurt"), "variation");

//Или от объекта

`variable` = sound("entity.zombie.hurt").set_sound_variation("variation");

//Или в сухую позиционно

variable::set_sound_variation(`variable`, sound("entity.zombie.hurt"), "variation");

//Или в сухую по ключам

variable::set_sound_variation(variable=`variable`, sound=sound("entity.zombie.hurt"), variation="variation");
```

**Аргументы:**

| ID        | Тип                | Описание                  |
|-----------|--------------------|---------------------------|
| variable  | Переменная\[Звук\] | Переменная для присвоения |
| sound     | Звук               | Звук для изменения        |
| variation | Текст              | Вариация                  |

<h3 id=set_variable_set_sound_volume_action>
  <code>variable::set_sound_volume_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить громкость звука\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает громкость звука и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_sound_volume_action(sound("entity.zombie.hurt"), 1);

//Или от объекта

`variable` = sound("entity.zombie.hurt").set_sound_volume_action(1);

//Или в сухую позиционно

variable::set_sound_volume_action(`variable`, sound("entity.zombie.hurt"), 1);

//Или в сухую по ключам

variable::set_sound_volume_action(variable=`variable`, sound=sound("entity.zombie.hurt"), volume=1);
```

**Аргументы:**

| ID       | Тип                | Описание                  |
|----------|--------------------|---------------------------|
| variable | Переменная\[Звук\] | Переменная для присвоения |
| sound    | Звук               | Звук для изменения        |
| volume   | Число              | Новое значение громкости  |

<h3 id=set_variable_set_template_code>
  <code>variable::set_template_code</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить код в шаблон\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает код в шаблон и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_template_code(item("stick"), "any value");

//Или от объекта

`variable` = item("stick").set_template_code("any value");

//Или в сухую позиционно

variable::set_template_code(`variable`, item("stick"), "any value");

//Или в сухую по ключам

variable::set_template_code(variable=`variable`, template=item("stick"), code="any value");
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| template | Предмет               | Шаблон                    |
| code     | Любое значение        | Словарь/текст JSON        |

<h3 id=set_variable_set_texture_to_map>
  <code>variable::set_texture_to_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить изображение карте\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает изображение карте по указанной ссылке. При перезагрузке сервера изображения могут пропасть, поэтому рекомендуется повторно устанавливать его тем же картам при запуске мира.

**Пример использования:**
```ts
`variable` = variable::set_texture_to_map(item("stick"), "url");

//Или от объекта

`variable` = item("stick").set_texture_to_map("url");

//Или в сухую позиционно

variable::set_texture_to_map(`variable`, item("stick"), "url");

//Или в сухую по ключам

variable::set_texture_to_map(variable=`variable`, map=item("stick"), url="url");
```

**Аргументы:**

| ID       | Тип                   | Описание                  |
|----------|-----------------------|---------------------------|
| variable | Переменная\[Предмет\] | Переменная для присвоения |
| map      | Предмет               | Карта для установки       |
| url      | Текст                 | Ссылка на изображение     |

<h3 id=set_variable_set_vector_component>
  <code>variable::set_vector_component</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить координату вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает определённую координату вектора и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_vector_component(vector(0,0,0), 1, "X");

//Или от объекта

`variable` = vector(0,0,0).set_vector_component(1, "X");

//Или в сухую позиционно

variable::set_vector_component(`variable`, vector(0,0,0), 1, "X");

//Или в сухую по ключам

variable::set_vector_component(variable=`variable`, vector=vector(0,0,0), value=1, vector_component="X");
```

**Аргументы:**

| ID               | Тип                                                                               | Описание                  |
|------------------|-----------------------------------------------------------------------------------|---------------------------|
| variable         | Переменная\[Вектор\]                                                              | Переменная для присвоения |
| vector           | Вектор                                                                            | Вектор для изменения      |
| value            | Число                                                                             | Новое значение            |
| vector_component | Маркер<br/>**X** - Координата X<br/>**Y** - Координата Y<br/>**Z** - Координата Z | Тип координаты            |

<h3 id=set_variable_set_vector_length>
  <code>variable::set_vector_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить длину вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает длину вектора и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_vector_length(vector(0,0,0), 1);

//Или от объекта

`variable` = vector(0,0,0).set_vector_length(1);

//Или в сухую позиционно

variable::set_vector_length(`variable`, vector(0,0,0), 1);

//Или в сухую по ключам

variable::set_vector_length(variable=`variable`, vector=vector(0,0,0), length=1);
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Вектор\] | Переменная для присвоения |
| vector   | Вектор               | Вектор для изменения      |
| length   | Число                | Новая длина               |

<h3 id=set_variable_shift_all_coordinates>
  <code>variable::shift_all_coordinates</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сдвинуть все координаты местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Сдвигает все координаты местоположения на определённые значения.

**Пример использования:**
```ts
`variable` = variable::shift_all_coordinates(location(0,0,0,0,0), 1, 2, 3, 4, 5);

//Или от объекта

`variable` = location(0,0,0,0,0).shift_all_coordinates(1, 2, 3, 4, 5);

//Или в сухую позиционно

variable::shift_all_coordinates(`variable`, location(0,0,0,0,0), 1, 2, 3, 4, 5);

//Или в сухую по ключам

variable::shift_all_coordinates(variable=`variable`, location=location(0,0,0,0,0), x=1, y=2, z=3, yaw=4, pitch=5);
```

**Аргументы:**

| ID       | Тип                          | Описание                          |
|----------|------------------------------|-----------------------------------|
| variable | Переменная\[Местоположение\] | Переменная для присвоения         |
| location | Местоположение               | Местоположение для сдвига         |
| x        | Число                        | Сдвиг по оси X                    |
| y        | Число                        | Сдвиг по оси Y                    |
| z        | Число                        | Сдвиг по оси Z                    |
| yaw      | Число                        | Сдвиг по горизонтальному повороту |
| pitch    | Число                        | Сдвиг по вертикальному повороту   |

<h3 id=set_variable_shift_coordinate>
  <code>variable::shift_coordinate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сдвинуть координату местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Сдвигает координату местоположения на определённое значение.

**Пример использования:**
```ts
`variable` = variable::shift_coordinate(location(0,0,0,0,0), 1, "PITCH");

//Или от объекта

`variable` = location(0,0,0,0,0).shift_coordinate(1, "PITCH");

//Или в сухую позиционно

variable::shift_coordinate(`variable`, location(0,0,0,0,0), 1, "PITCH");

//Или в сухую по ключам

variable::shift_coordinate(variable=`variable`, location=location(0,0,0,0,0), distance=1, type="PITCH");
```

**Аргументы:**

| ID       | Тип                                                                                                                        | Описание                  |
|----------|----------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Местоположение\]                                                                                               | Переменная для присвоения |
| location | Местоположение                                                                                                             | Местоположение для сдвига |
| distance | Число                                                                                                                      | Значение сдвига           |
| type     | Маркер<br/>**PITCH** - Вертикальный поворот<br/>**X** - X<br/>**Y** - Y<br/>**YAW** - Горизонтальный поворот<br/>**Z** - Z | Тип координаты            |

<h3 id=set_variable_shift_location_in_direction>
  <code>variable::shift_location_in_direction</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сдвинуть местоположение в направлении\
**Тип:** Действие, возращающее значение\
**Описание:** Сдвигает местоположение в определённом направлении на определённое значение.

**Пример использования:**
```ts
`variable` = variable::shift_location_in_direction(location(0,0,0,0,0), 1, "FORWARD");

//Или от объекта

`variable` = location(0,0,0,0,0).shift_location_in_direction(1, "FORWARD");

//Или в сухую позиционно

variable::shift_location_in_direction(`variable`, location(0,0,0,0,0), 1, "FORWARD");

//Или в сухую по ключам

variable::shift_location_in_direction(variable=`variable`, location=location(0,0,0,0,0), shift=1, direction="FORWARD");
```

**Аргументы:**

| ID        | Тип                                                                                               | Описание                  |
|-----------|---------------------------------------------------------------------------------------------------|---------------------------|
| variable  | Переменная\[Местоположение\]                                                                      | Переменная для присвоения |
| location  | Местоположение                                                                                    | Местоположение для сдвига |
| shift     | Число                                                                                             | Значение сдвига           |
| direction | Маркер<br/>**FORWARD** - Вперёд/Назад<br/>**SIDEWAYS** - Вправо/Влево<br/>**UPWARD** - Вверх/Вниз | Направление               |

<h3 id=set_variable_shift_location_on_vector>
  <code>variable::shift_location_on_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сдвинуть местоположение по вектору\
**Тип:** Действие, возращающее значение\
**Описание:** Сдвигает указанное местоположение по вектору и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::shift_location_on_vector(location(0,0,0,0,0), vector(0,0,0), 1);

//Или от объекта

`variable` = location(0,0,0,0,0).shift_location_on_vector(vector(0,0,0), 1);

//Или в сухую позиционно

variable::shift_location_on_vector(`variable`, location(0,0,0,0,0), vector(0,0,0), 1);

//Или в сухую по ключам

variable::shift_location_on_vector(variable=`variable`, location=location(0,0,0,0,0), vector=vector(0,0,0), length=1);
```

**Аргументы:**

| ID       | Тип                          | Описание                  |
|----------|------------------------------|---------------------------|
| variable | Переменная\[Местоположение\] | Переменная для присвоения |
| location | Местоположение               | Местоположение для сдвига |
| vector   | Вектор                       | Вектор сдвига             |
| length   | Число                        | Расстояние сдвига         |

<h3 id=set_variable_shift_location_towards_location>
  <code>variable::shift_location_towards_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сместить местоположение в сторону местоположения\
**Тип:** Действие, возращающее значение\
**Описание:** Смещает местоположение в сторону заданного местоположения на определённое расстояние и присваивает его в переменную.

**Пример использования:**
```ts
`variable` = variable::shift_location_towards_location(location(0,0,0,0,0), location(0,0,0,0,0), 1);

//Или от объекта

`variable` = location(0,0,0,0,0).shift_location_towards_location(location(0,0,0,0,0), 1);

//Или в сухую позиционно

variable::shift_location_towards_location(`variable`, location(0,0,0,0,0), location(0,0,0,0,0), 1);

//Или в сухую по ключам

variable::shift_location_towards_location(variable=`variable`, location_from=location(0,0,0,0,0), location_to=location(0,0,0,0,0), distance=1);
```

**Аргументы:**

| ID            | Тип                          | Описание                          |
|---------------|------------------------------|-----------------------------------|
| variable      | Переменная\[Местоположение\] | Переменная для присвоения         |
| location_from | Местоположение               | Местоположение для сдвига         |
| location_to   | Местоположение               | К какому местоположению смещать   |
| distance      | Число                        | На сколько смещать местоположение |

<h3 id=set_variable_simplex_noise_3d>
  <code>variable::simplex_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Шум Симплекс\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение шума Симплекс в определённом местоположении. Возвращает число, со значением от -1 до 1.

**Пример использования:**
```ts
`variable` = variable::simplex_noise_3d(location(0,0,0,0,0), 1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Или от объекта

`variable` = location(0,0,0,0,0).simplex_noise_3d(1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Или в сухую позиционно

variable::simplex_noise_3d(`variable`, location(0,0,0,0,0), 1, 2, 3, 4, 5, "FULL_RANGE", "FALSE");

//Или в сухую по ключам

variable::simplex_noise_3d(variable=`variable`, location=location(0,0,0,0,0), seed=1, loc_frequency=2, octaves=3, frequency=4, amplitude=5, range_mode="FULL_RANGE", normalized="FALSE");
```

**Аргументы:**

| ID            | Тип                                                                                                 | Описание                          |
|---------------|-----------------------------------------------------------------------------------------------------|-----------------------------------|
| variable      | Переменная\[Число\]                                                                                 | Переменная для присвоения         |
| location      | Местоположение                                                                                      | Местоположение для установки шума |
| seed          | Число                                                                                               | Ключ шума                         |
| loc_frequency | Число                                                                                               | Частота шума                      |
| octaves       | Число                                                                                               | Количество октав шума             |
| frequency     | Число                                                                                               | Частота октав шума                |
| amplitude     | Число                                                                                               | Амплитуда октав шума              |
| range_mode    | Маркер<br/>**FULL_RANGE** - Полный диапазон (от -1 до 1 или больше)<br/>**ZERO_TO_ONE** - От 0 до 1 | Диапазон значений                 |
| normalized    | Маркер<br/>**FALSE** - Не нормализировать<br/>**TRUE** - Нормализировать                            | Нормализация значений             |

<h3 id=set_variable_sine>
  <code>variable::sine</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Синус числа\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает синус от числа.

**Пример использования:**
```ts
`variable` = variable::sine(1, "ARCSINE", "DEGREES");

//Или от объекта

`variable` = (1).sine("ARCSINE", "DEGREES");

//Или в сухую позиционно

variable::sine(`variable`, 1, "ARCSINE", "DEGREES");

//Или в сухую по ключам

variable::sine(variable=`variable`, number=1, variant="ARCSINE", input="DEGREES");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                          | Описание                   |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| variable | Переменная\[Число\]                                                                                                                                          | Переменная для присвоения  |
| number   | Число                                                                                                                                                        | Число для получения синуса |
| variant  | Маркер<br/>**ARCSINE** - Арксинус<br/>**HYPERBOLIC_ARCSINE** - Гиперболический арксинус<br/>**HYPERBOLIC_SINE** - Гиперболический синус<br/>**SINE** - Синус | Тип операции               |
| input    | Маркер<br/>**DEGREES** - Градусы<br/>**RADIANS** - Радианы                                                                                                   | Тип угла                   |

<h3 id=set_variable_sort_any_list>
  <code>variable::sort_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отсортировать список\
**Тип:** Действие, возращающее значение\
**Описание:** Сортирует элементы списка.\
**Работает с:**\
&nbsp;&nbsp;Числами\
&nbsp;&nbsp;Текстом\
&nbsp;&nbsp;Списками

**Пример использования:**
```ts
`variable` = variable::sort_list([`list`, `list`], "ASCENDING");

//Или от объекта

`variable` = [`list`, `list`].sort_list("ASCENDING");

//Или в сухую позиционно

variable::sort_list(`variable`, [`list`, `list`], "ASCENDING");

//Или в сухую по ключам

variable::sort_list(variable=`variable`, list=[`list`, `list`], sort_mode="ASCENDING");
```

**Аргументы:**

| ID        | Тип                                                                        | Описание                  |
|-----------|----------------------------------------------------------------------------|---------------------------|
| variable  | Переменная\[Список\]                                                       | Переменная для присвоения |
| list      | Список                                                                     | Список                    |
| sort_mode | Маркер<br/>**ASCENDING** - По возрастанию<br/>**DESCENDING** - По убыванию | Способ сортировки         |

<h3 id=set_variable_sort_any_map>
  <code>variable::sort_map</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сортировать словарь\
**Тип:** Действие, возращающее значение\
**Описание:** Сортирует словарь по заданным параметрам и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::sort_map({"map":`map`}, "ASCENDING", "KEYS");

//Или от объекта

`variable` = {"map":`map`}.sort_map("ASCENDING", "KEYS");

//Или в сухую позиционно

variable::sort_map(`variable`, {"map":`map`}, "ASCENDING", "KEYS");

//Или в сухую по ключам

variable::sort_map(variable=`variable`, map={"map":`map`}, sort_order="ASCENDING", sort_type="KEYS");
```

**Аргументы:**

| ID         | Тип                                                                        | Описание                  |
|------------|----------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Словарь\]                                                      | Переменная для присвоения |
| map        | Словарь                                                                    | Словарь для сортировки    |
| sort_order | Маркер<br/>**ASCENDING** - По возрастанию<br/>**DESCENDING** - По убыванию | Порядок сортировки        |
| sort_type  | Маркер<br/>**KEYS** - По ключу<br/>**VALUES** - По значению                | Тип сортировки            |

<h3 id=set_variable_split_text>
  <code>variable::split_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Разделить текст на элементы\
**Тип:** Действие, возращающее значение\
**Описание:** Разделяет текст на элементы списка по заданному символу и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::split_text("text", "delimiter");

//Или от объекта

`variable` = "text".split_text("delimiter");

//Или в сухую позиционно

variable::split_text(`variable`, "text", "delimiter");

//Или в сухую по ключам

variable::split_text(variable=`variable`, text="text", delimiter="delimiter");
```

**Аргументы:**

| ID        | Тип                  | Описание                  |
|-----------|----------------------|---------------------------|
| variable  | Переменная\[Список\] | Переменная для присвоения |
| text      | Текст                | Текст для разделения      |
| delimiter | Текст                | Разделитель               |

<h3 id=set_variable_split_text_by_length>
  <code>variable::split_text_by_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Перенос по словам\
**Тип:** Действие, возращающее значение\
**Описание:** Разделяет текст по словам на список строк и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::split_text_by_length("text", 1);

//Или от объекта

`variable` = "text".split_text_by_length(1);

//Или в сухую позиционно

variable::split_text_by_length(`variable`, "text", 1);

//Или в сухую по ключам

variable::split_text_by_length(variable=`variable`, text="text", max_length=1);
```

**Аргументы:**

| ID         | Тип                  | Описание                  |
|------------|----------------------|---------------------------|
| variable   | Переменная\[Список\] | Переменная для присвоения |
| text       | Текст                | Текст для разделения      |
| max_length | Число                | Длина строки              |

<h3 id=set_variable_strip_text>
  <code>variable::strip_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить пробелы\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет пробелы в тексте и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::strip_text("text", "ALL");

//Или от объекта

`variable` = "text".strip_text("ALL");

//Или в сухую позиционно

variable::strip_text(`variable`, "text", "ALL");

//Или в сухую по ключам

variable::strip_text(variable=`variable`, text="text", strip_type="ALL");
```

**Аргументы:**

| ID         | Тип                                                                                                           | Описание                  |
|------------|---------------------------------------------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Текст\]                                                                                           | Переменная для присвоения |
| text       | Текст                                                                                                         | Текст для изменения       |
| strip_type | Маркер<br/>**ALL** - В начале и конце<br/>**END** - В конце<br/>**INDENT** - Отступы<br/>**START** - В начале | Тип удаления              |

<h3 id=set_variable_subtract>
  <code>variable::subtract</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Вычитание чисел (-)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной разницу чисел.

**Пример использования:**
```ts
`variable` = variable::subtract([1, 2]);

//Или в сухую позиционно

variable::subtract(`variable`, [1, 2]);

//Или в сухую по ключам

variable::subtract(variable=`variable`, value=[1, 2]);
```

**Аргументы:**

| ID       | Тип                                                   | Описание                  |
|----------|-------------------------------------------------------|---------------------------|
| variable | Переменная\[Число\]                                   | Переменная для присвоения |
| value    | Message 'actions.array' not found in 'ru_RU'\[Число\] | Числа для вычитания       |

<h3 id=set_variable_subtract_vectors>
  <code>variable::subtract_vectors</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Разница векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение разницы векторов.

**Пример использования:**
```ts
`variable` = variable::subtract_vectors([vector(0,0,0), vector(0,0,0)]);

//Или в сухую позиционно

variable::subtract_vectors(`variable`, [vector(0,0,0), vector(0,0,0)]);

//Или в сухую по ключам

variable::subtract_vectors(variable=`variable`, vectors=[vector(0,0,0), vector(0,0,0)]);
```

**Аргументы:**

| ID       | Тип                                                    | Описание                      |
|----------|--------------------------------------------------------|-------------------------------|
| variable | Переменная\[Вектор\]                                   | Переменная для присвоения     |
| vectors  | Message 'actions.array' not found in 'ru_RU'\[Вектор\] | Вектора для получения разницы |

<h3 id=set_variable_tangent>
  <code>variable::tangent</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Тангенс числа\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает тангенс от числа.

**Пример использования:**
```ts
`variable` = variable::tangent(1, "ARCTANGENT", "DEGREES");

//Или от объекта

`variable` = (1).tangent("ARCTANGENT", "DEGREES");

//Или в сухую позиционно

variable::tangent(`variable`, 1, "ARCTANGENT", "DEGREES");

//Или в сухую по ключам

variable::tangent(variable=`variable`, number=1, variant="ARCTANGENT", input="DEGREES");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                              | Описание                     |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| variable | Переменная\[Число\]                                                                                                                                                              | Переменная для присвоения    |
| number   | Число                                                                                                                                                                            | Число для получения тангенса |
| variant  | Маркер<br/>**ARCTANGENT** - Арктангенс<br/>**HYPERBOLIC_ARCTANGENT** - Гиперболический арктангенс<br/>**HYPERBOLIC_TANGENT** - Гиперболический тангенс<br/>**TANGENT** - Тангенс | Тип операции                 |
| input    | Маркер<br/>**DEGREES** - Градусы<br/>**RADIANS** - Радианы                                                                                                                       | Тип угла                     |

<h3 id=set_variable_text>
  <code>variable::set_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить текст в переменную\
**Тип:** Действие, возращающее значение\
**Описание:** Объединяет и присваивает к переменной одно или несколько значений текста.

**Пример использования:**
```ts
`variable` = variable::set_text(["text", "text"], "CONCATENATION");

//Или в сухую позиционно

variable::set_text(`variable`, ["text", "text"], "CONCATENATION");

//Или в сухую по ключам

variable::set_text(variable=`variable`, text=["text", "text"], merging="CONCATENATION");
```

**Аргументы:**

| ID       | Тип                                                                                                                           | Описание                  |
|----------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Текст\]                                                                                                           | Переменная для присвоения |
| text     | Message 'actions.array' not found in 'ru_RU'\[Текст\]                                                                         | Текст для установки       |
| merging  | Маркер<br/>**CONCATENATION** - Объединение<br/>**SEPARATE_LINES** - Разделение на строки<br/>**SPACES** - Разделение пробелом | Объединение текста        |

<h3 id=set_variable_text_case>
  <code>variable::set_text_case</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить регистр текста\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает регистр текста и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_text_case("text", "INVERT");

//Или от объекта

`variable` = "text".set_text_case("INVERT");

//Или в сухую позиционно

variable::set_text_case(`variable`, "text", "INVERT");

//Или в сухую по ключам

variable::set_text_case(variable=`variable`, text="text", case_type="INVERT");
```

**Аргументы:**

| ID        | Тип                                                                                                                                            | Описание                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable  | Переменная\[Текст\]                                                                                                                            | Переменная для присвоения |
| text      | Текст                                                                                                                                          | Текст для установки       |
| case_type | Маркер<br/>**INVERT** - Инвертировать<br/>**LOWER** - Нижний<br/>**PROPER** - Первый символ<br/>**RANDOM** - Случайный<br/>**UPPER** - Верхний | Тип регистра              |

<h3 id=set_variable_text_length>
  <code>variable::get_text_length</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить длину текста\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение количества символов в тексте.

**Пример использования:**
```ts
`variable` = variable::get_text_length("text");

//Или от объекта

`variable` = "text".get_text_length();

//Или в сухую позиционно

variable::get_text_length(`variable`, "text");

//Или в сухую по ключам

variable::get_text_length(variable=`variable`, text="text");
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| text     | Текст               | Текст для получения длины |

<h3 id=set_variable_text_to_bytes>
  <code>variable::text_to_bytes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать текст в байты\
**Тип:** Действие, возращающее значение\
**Описание:** Преобразовывает текст в байты и присваивает результат в переменную.

**Пример использования:**
```ts
`variable` = variable::text_to_bytes("text", "UTF_16");

//Или от объекта

`variable` = "text".text_to_bytes("UTF_16");

//Или в сухую позиционно

variable::text_to_bytes(`variable`, "text", "UTF_16");

//Или в сухую по ключам

variable::text_to_bytes(variable=`variable`, text="text", charset="UTF_16");
```

**Аргументы:**

| ID       | Тип                                                                        | Описание                  |
|----------|----------------------------------------------------------------------------|---------------------------|
| variable | Переменная\[Список\]                                                       | Переменная для присвоения |
| text     | Текст                                                                      | Текст для преобразования  |
| charset  | Маркер<br/>**UTF_16** - UTF-16<br/>**UTF_8** - UTF-8<br/>**ASCII** - ASCII | Кодировка                 |

<h3 id=set_variable_text_to_chars>
  <code>variable::text_to_chars</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать текст в символы\
**Тип:** Действие, возращающее значение\
**Описание:** Преобразовывает текст в символы выбранного типа и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::text_to_chars("text", "CHARS");

//Или от объекта

`variable` = "text".text_to_chars("CHARS");

//Или в сухую позиционно

variable::text_to_chars(`variable`, "text", "CHARS");

//Или в сухую по ключам

variable::text_to_chars(variable=`variable`, text="text", chars_type="CHARS");
```

**Аргументы:**

| ID         | Тип                                                                                                                                                                      | Описание                  |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| variable   | Переменная\[Текст\]                                                                                                                                                      | Переменная для присвоения |
| text       | Текст                                                                                                                                                                    | Преобразовываемый текст   |
| chars_type | Маркер<br/>**CHARS** - Символы (UTF-16)<br/>**CODES** - Коды символов (UTF-16)<br/>**CODEPOINTS_CHARS** - Символы (Unicode)<br/>**CODEPOINTS** - Кодовые точки (Unicode) | Тип символов              |

<h3 id=set_variable_to_char>
  <code>variable::to_char</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить символ по числу\
**Тип:** Действие, возращающее значение\
**Описание:** Получает определённый символ по числу и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::to_char(1);

//Или от объекта

`variable` = (1).to_char();

//Или в сухую позиционно

variable::to_char(`variable`, 1);

//Или в сухую по ключам

variable::to_char(variable=`variable`, number=1);
```

**Аргументы:**

| ID       | Тип                 | Описание                    |
|----------|---------------------|-----------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения   |
| number   | Число               | Число для получения символа |

<h3 id=set_variable_to_hsb>
  <code>variable::to_hsb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать HSB цвет\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт HEX цвет на основе оттенка, насыщенности и яркости.

**Пример использования:**
```ts
`variable` = variable::to_hsb(1, 2, 3);

//Или в сухую позиционно

variable::to_hsb(`variable`, 1, 2, 3);

//Или в сухую по ключам

variable::to_hsb(variable=`variable`, hue=1, saturation=2, brightness=3);
```

**Аргументы:**

| ID         | Тип                 | Описание                  |
|------------|---------------------|---------------------------|
| variable   | Переменная\[Текст\] | Переменная для присвоения |
| hue        | Число               | Оттенок (0 - 360)         |
| saturation | Число               | Насыщенность (0 - 100)    |
| brightness | Число               | Яркость (0 - 100)         |

<h3 id=set_variable_to_hsl>
  <code>variable::to_hsl</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать HSL цвет\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт HEX цвет на основе оттенка, насыщенности и светлоты.

**Пример использования:**
```ts
`variable` = variable::to_hsl(1, 2, 3);

//Или в сухую позиционно

variable::to_hsl(`variable`, 1, 2, 3);

//Или в сухую по ключам

variable::to_hsl(variable=`variable`, hue=1, saturation=2, lightness=3);
```

**Аргументы:**

| ID         | Тип                 | Описание                  |
|------------|---------------------|---------------------------|
| variable   | Переменная\[Текст\] | Переменная для присвоения |
| hue        | Число               | Оттенок (0 - 360)         |
| saturation | Число               | Насыщенность (0 - 100)    |
| lightness  | Число               | Светлота (0 - 100)        |

<h3 id=set_variable_to_json>
  <code>variable::to_json</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Преобразовать в JSON\
**Тип:** Действие, возращающее значение\
**Описание:** Преобразует словари и списки в JSON текст.

**Пример использования:**
```ts
`variable` = variable::to_json("any value", "FALSE");

//Или в сухую позиционно

variable::to_json(`variable`, "any value", "FALSE");

//Или в сухую по ключам

variable::to_json(variable=`variable`, value="any value", pretty_print="FALSE");
```

**Аргументы:**

| ID           | Тип                                                      | Описание                     |
|--------------|----------------------------------------------------------|------------------------------|
| variable     | Переменная\[Любое значение\]                             | Для записи результата        |
| value        | Любое значение                                           | Список/Словарь со значениями |
| pretty_print | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Форматирование Pretty Print  |

<h3 id=set_variable_to_rgb>
  <code>variable::to_rgb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать RGB цвет\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт HEX цвет в зависимости от красного, зелёного и синего каналов.

**Пример использования:**
```ts
`variable` = variable::to_rgb(1, 2, 3);

//Или в сухую позиционно

variable::to_rgb(`variable`, 1, 2, 3);

//Или в сухую по ключам

variable::to_rgb(variable=`variable`, red=1, green=2, blue=3);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| red      | Число               | Красный канал (0 - 255)   |
| green    | Число               | Зелёный канал (0 - 255)   |
| blue     | Число               | Синий канал (0 - 255)     |

<h3 id=set_variable_trim_list>
  <code>variable::trim_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Обрезать список\
**Тип:** Действие, возращающее значение\
**Описание:** Возвращает список, содержащий элементы указанного списка, которые находятся начиная и заканчивая на указанных индексах.

**Пример использования:**
```ts
`variable` = variable::trim_list([`list`, `list`], 1, 2);

//Или от объекта

`variable` = [`list`, `list`].trim_list(1, 2);

//Или в сухую позиционно

variable::trim_list(`variable`, [`list`, `list`], 1, 2);

//Или в сухую по ключам

variable::trim_list(variable=`variable`, list=[`list`, `list`], start=1, end=2);
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Список\] | Переменная для присвоения |
| list     | Список               | Список                    |
| start    | Число                | Индекс начала             |
| end      | Число                | Индекс конца              |

<h3 id=set_variable_trim_text>
  <code>variable::trim_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Обрезать текст\
**Тип:** Действие, возращающее значение\
**Описание:** Обрезает текст и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::trim_text("text", 1, 2);

//Или от объекта

`variable` = "text".trim_text(1, 2);

//Или в сухую позиционно

variable::trim_text(`variable`, "text", 1, 2);

//Или в сухую по ключам

variable::trim_text(variable=`variable`, text="text", start=1, end=2);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| text     | Текст               | Текст для обрезки         |
| start    | Число               | Начальная позиция         |
| end      | Число               | Конечная позиция          |

<h3 id=set_variable_unset_item_components>
  <code>variable::unset_item_components</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить компоненты предмета\
**Тип:** Действие, возращающее значение\
**Описание:** Удаляет указанные компоненты предмета и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::unset_item_components(item("stick"), ["components", "components"]);

//Или от объекта

`variable` = item("stick").unset_item_components(["components", "components"]);

//Или в сухую позиционно

variable::unset_item_components(`variable`, item("stick"), ["components", "components"]);

//Или в сухую по ключам

variable::unset_item_components(variable=`variable`, item=item("stick"), components=["components", "components"]);
```

**Аргументы:**

| ID         | Тип                                                   | Описание                    |
|------------|-------------------------------------------------------|-----------------------------|
| variable   | Переменная\[Предмет\]                                 | Переменная для присвоения   |
| item       | Предмет                                               | Предмет                     |
| components | Message 'actions.array' not found in 'ru_RU'\[Текст\] | Ключи удаляемых компонентов |

<h3 id=set_variable_value>
  <code>variable::set_value</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить значение (=)\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает значение к переменной.

**Пример использования:**
```ts
`variable` = variable::set_value("any value");

//Или в сухую позиционно

variable::set_value(`variable`, "any value");

//Или в сухую по ключам

variable::set_value(variable=`variable`, value="any value");
```

**Аргументы:**

| ID       | Тип                          | Описание                  |
|----------|------------------------------|---------------------------|
| variable | Переменная\[Любое значение\] | Переменная для присвоения |
| value    | Любое значение               | Значение для присвоения   |

<h3 id=set_variable_vector>
  <code>variable::set_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать вектор\
**Тип:** Действие, возращающее значение\
**Описание:** Создаёт вектор из указанных координат и присваивает результат к переменной.

**Пример использования:**
```ts
`variable` = variable::set_vector(1, 2, 3);

//Или в сухую позиционно

variable::set_vector(`variable`, 1, 2, 3);

//Или в сухую по ключам

variable::set_vector(variable=`variable`, x=1, y=2, z=3);
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Вектор\] | Переменная для присвоения |
| x        | Число                | Координата X              |
| y        | Число                | Координата Y              |
| z        | Число                | Координата Z              |

<h3 id=set_variable_vector_cross_product>
  <code>variable::vector_cross_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Векторное произведение двух векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение векторного произведения двух векторов.

**Пример использования:**
```ts
`variable` = variable::vector_cross_product(vector(0,0,0), vector(0,0,0));

//Или в сухую позиционно

variable::vector_cross_product(`variable`, vector(0,0,0), vector(0,0,0));

//Или в сухую по ключам

variable::vector_cross_product(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0));
```

**Аргументы:**

| ID       | Тип                  | Описание                  |
|----------|----------------------|---------------------------|
| variable | Переменная\[Вектор\] | Переменная для присвоения |
| vector_1 | Вектор               | Первый вектор             |
| vector_2 | Вектор               | Второй вектор             |

<h3 id=set_variable_vector_dot_product>
  <code>variable::vector_dot_product</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Скалярное произведение двух векторов\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение скалярного произведения двух векторов.

**Пример использования:**
```ts
`variable` = variable::vector_dot_product(vector(0,0,0), vector(0,0,0));

//Или в сухую позиционно

variable::vector_dot_product(`variable`, vector(0,0,0), vector(0,0,0));

//Или в сухую по ключам

variable::vector_dot_product(variable=`variable`, vector_1=vector(0,0,0), vector_2=vector(0,0,0));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| vector_1 | Вектор              | Первый вектор             |
| vector_2 | Вектор              | Второй вектор             |

<h3 id=set_variable_vector_to_direction_name>
  <code>variable::vector_to_direction_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить сторону света вектора\
**Тип:** Действие, возращающее значение\
**Описание:** Устанавливает в переменную сторону света, в которую направлен вектор.

**Пример использования:**
```ts
`variable` = variable::vector_to_direction_name(vector(0,0,0));

//Или от объекта

`variable` = vector(0,0,0).vector_to_direction_name();

//Или в сухую позиционно

variable::vector_to_direction_name(`variable`, vector(0,0,0));

//Или в сухую по ключам

variable::vector_to_direction_name(variable=`variable`, vector=vector(0,0,0));
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Текст\] | Переменная для присвоения |
| vector   | Вектор              | Вектор для получения      |

<h3 id=set_variable_voronoi_noise_3d>
  <code>variable::voronoi_noise_3d</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Шум Вороного\
**Тип:** Действие, возращающее значение\
**Описание:** Присваивает к переменной значение шума Вороного в определённом местоположении. Возвращает число, со значением от 0 до 1.

**Пример использования:**
```ts
`variable` = variable::voronoi_noise_3d(location(0,0,0,0,0), 1, 2, 3, "FULL_RANGE", "FALSE");

//Или от объекта

`variable` = location(0,0,0,0,0).voronoi_noise_3d(1, 2, 3, "FULL_RANGE", "FALSE");

//Или в сухую позиционно

variable::voronoi_noise_3d(`variable`, location(0,0,0,0,0), 1, 2, 3, "FULL_RANGE", "FALSE");

//Или в сухую по ключам

variable::voronoi_noise_3d(variable=`variable`, location=location(0,0,0,0,0), seed=1, frequency=2, displacement=3, range_mode="FULL_RANGE", enable_distance="FALSE");
```

**Аргументы:**

| ID              | Тип                                                                    | Описание                          |
|-----------------|------------------------------------------------------------------------|-----------------------------------|
| variable        | Переменная\[Число\]                                                    | Переменная для присвоения         |
| location        | Местоположение                                                         | Местоположение для установки шума |
| seed            | Число                                                                  | Ключ шума                         |
| frequency       | Число                                                                  | Частота шума                      |
| displacement    | Число                                                                  | Смещение шума                     |
| range_mode      | Маркер<br/>**FULL_RANGE** - От -1 до 1<br/>**ZERO_TO_ONE** - От 0 до 1 | Диапазон значений                 |
| enable_distance | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить               | Режим расстояния                  |

<h3 id=set_variable_warp>
  <code>variable::wrap</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Обернуть число\
**Тип:** Действие, возращающее значение\
**Описание:** Проверяет, находится ли число между двумя границами, и если нет, оборачивает его вокруг этой границы.

**Пример использования:**
```ts
`variable` = variable::wrap(1, 2, 3);

//Или от объекта

`variable` = (1).wrap(2, 3);

//Или в сухую позиционно

variable::wrap(`variable`, 1, 2, 3);

//Или в сухую по ключам

variable::wrap(variable=`variable`, number=1, min=2, max=3);
```

**Аргументы:**

| ID       | Тип                 | Описание                  |
|----------|---------------------|---------------------------|
| variable | Переменная\[Число\] | Переменная для присвоения |
| number   | Число               | Число для оборачивания    |
| min      | Число               | Минимальное значение      |
| max      | Число               | Максимальное значение     |

