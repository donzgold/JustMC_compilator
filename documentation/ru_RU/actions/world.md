<h2 id=world>
  <code>world</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

<h3 id=game_block_growth>
  <code>world::block_growth</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стадию роста блока\
**Тип:** Действие без значения\
**Описание:** Устанавливает стадию роста для блока на выбранном местоположении.

**Пример использования:**
```ts
world::block_growth(location(0,0,0,0,0), 1, "PERCENTAGE");

//Или в сухую по ключам

world::block_growth(location=location(0,0,0,0,0), growth_stage=1, growth_type="PERCENTAGE");
```

**Аргументы:**

| ID           | Тип                                                                                 | Описание             |
|--------------|-------------------------------------------------------------------------------------|----------------------|
| location     | Местоположение                                                                      | Местоположение блока |
| growth_stage | Число                                                                               | Стадия роста         |
| growth_type  | Маркер<br/>**PERCENTAGE** - Процент роста<br/>**STAGE_NUMBER** - Номер стадии роста | Тип роста            |

<h3 id=game_bloom_skulk_catalyst>
  <code>world::bloom_skulk_catalyst</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Продлить скалк-заражение к местоположению\
**Тип:** Действие без значения\
**Описание:** Продлевает скалк-заражение к местоположению.\
**Работает с:**\
&nbsp;&nbsp;Скалк-катализаторами

**Пример использования:**
```ts
world::bloom_skulk_catalyst(location(0,0,0,0,0), location(0,0,0,0,0), 1);

//Или в сухую по ключам

world::bloom_skulk_catalyst(location=location(0,0,0,0,0), bloom_location=location(0,0,0,0,0), charge=1);
```

**Аргументы:**

| ID             | Тип            | Описание                               |
|----------------|----------------|----------------------------------------|
| location       | Местоположение | Местоположение скалкового катализатора |
| bloom_location | Местоположение | Конечное местоположение                |
| charge         | Число          | Сила заражения                         |

<h3 id=game_bone_meal_block>
  <code>world::bone_meal_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удобрить блок\
**Тип:** Действие без значения\
**Описание:** Удобряет блок на выбранном местоположении.

**Пример использования:**
```ts
world::bone_meal_block(location(0,0,0,0,0), 1);

//Или в сухую по ключам

world::bone_meal_block(location=location(0,0,0,0,0), count=1);
```

**Аргументы:**

| ID       | Тип            | Описание                    |
|----------|----------------|-----------------------------|
| location | Местоположение | Местоположение блока        |
| count    | Число          | Количество попыток удобрить |

<h3 id=game_break_block>
  <code>world::break_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сломать блок\
**Тип:** Действие без значения\
**Описание:** Разрушает блоки на указанных местоположениях, как если бы это сделал игрок в режиме выживания нужным инструментом.

**Пример использования:**
```ts
world::break_block([location(0,0,0,0,0), location(0,0,0,0,0)], item("stick"), "FALSE");

//Или в сухую по ключам

world::break_block(locations=[location(0,0,0,0,0), location(0,0,0,0,0)], tool=item("stick"), drop_exp="FALSE");
```

**Аргументы:**

| ID        | Тип                                                      | Описание              |
|-----------|----------------------------------------------------------|-----------------------|
| locations | Список\[Местоположение\]                                 | Местоположения блоков |
| tool      | Предмет                                                  | Инструмент            |
| drop_exp  | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Выпадение опыта       |

<h3 id=game_cancel_event>
  <code>world::cancel_event</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отмена события\
**Тип:** Действие без значения\
**Описание:** Отменяет начальное событие, которое вызвало этот код.

**Пример использования:**
```ts
world::cancel_event();
```

<h3 id=game_clear_container>
  <code>world::clear_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить контейнер\
**Тип:** Действие без значения\
**Описание:** Удаляет все предметы из контейнера на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:**
```ts
world::clear_container(location(0,0,0,0,0));

//Или в сухую по ключам

world::clear_container(location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип            | Описание                  |
|----------|----------------|---------------------------|
| location | Местоположение | Местоположение контейнера |

<h3 id=game_clear_container_items>
  <code>world::clear_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить предметы в контейнере\
**Тип:** Действие без значения\
**Описание:** Очищает указанные предметы из контейнера.\
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:**
```ts
world::clear_container_items([item("stick"), item("stick")], location(0,0,0,0,0));

//Или в сухую по ключам

world::clear_container_items(items=[item("stick"), item("stick")], location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип               | Описание                  |
|----------|-------------------|---------------------------|
| items    | Список\[Предмет\] | Предметы                  |
| location | Местоположение    | Местоположение контейнера |

<h3 id=game_clear_exploded_blocks>
  <code>world::clear_exploded_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить взорванные блоки\
**Тип:** Действие без значения\
**Описание:** Возвращает взорванные блоки в исходное положение.\
**Работает с:**\
&nbsp;&nbsp;Событием "Сущность взрывается"\
&nbsp;&nbsp;Событием "Блок взрывается"

**Пример использования:**
```ts
world::clear_exploded_blocks([location(0,0,0,0,0), location(0,0,0,0,0)]);

//Или в сухую по ключам

world::clear_exploded_blocks(location=[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

**Аргументы:**

| ID       | Тип                      | Описание              |
|----------|--------------------------|-----------------------|
| location | Список\[Местоположение\] | Местоположения блоков |

<h3 id=game_clear_region>
  <code>world::clear_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить регион\
**Тип:** Действие без значения\
**Описание:** Удаляет все блоки в регионе.

**Пример использования:**
```ts
world::clear_region(location(0,0,0,0,0), location(0,0,0,0,0));

//Или в сухую по ключам

world::clear_region(pos_1=location(0,0,0,0,0), pos_2=location(0,0,0,0,0));
```

**Аргументы:**

| ID    | Тип            | Описание                     |
|-------|----------------|------------------------------|
| pos_1 | Местоположение | Угол региона                 |
| pos_2 | Местоположение | Противоположный угол региона |

<h3 id=game_clear_scoreboard_scores>
  <code>world::clear_scoreboard_scores</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить значения скорборда\
**Тип:** Действие без значения\
**Описание:** Очищает все значения указанного скорборда.

**Пример использования:**
```ts
world::clear_scoreboard_scores("id");

//Или в сухую по ключам

world::clear_scoreboard_scores(id="id");
```

**Аргументы:**

| ID | Тип   | Описание     |
|----|-------|--------------|
| id | Текст | ID скорборда |

<h3 id=game_clone_region>
  <code>world::clone_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Клонировать блоки региона\
**Тип:** Действие без значения\
**Описание:** Клонирует регион на выбраное местоположение.

**Пример использования:**
```ts
world::clone_region(location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), location(0,0,0,0,0), "FALSE", "FALSE");

//Или в сухую по ключам

world::clone_region(pos_1=location(0,0,0,0,0), pos_2=location(0,0,0,0,0), target_pos=location(0,0,0,0,0), paste_pos=location(0,0,0,0,0), ignore_air="FALSE", copy_entity="FALSE");
```

**Аргументы:**

| ID          | Тип                                                                | Описание                     |
|-------------|--------------------------------------------------------------------|------------------------------|
| pos_1       | Местоположение                                                     | Угол региона                 |
| pos_2       | Местоположение                                                     | Противоположный угол региона |
| target_pos  | Местоположение                                                     | Местоположение копирования   |
| paste_pos   | Местоположение                                                     | Местоположение для вставки   |
| ignore_air  | Маркер<br/>**FALSE** - Не игнорировать<br/>**TRUE** - Игнорировать | Игнорировать воздух          |
| copy_entity | Маркер<br/>**FALSE** - Не клонировать<br/>**TRUE** - Клонировать   | Клонировать существ          |

<h3 id=game_create_explosion>
  <code>world::create_explosion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать взрыв\
**Тип:** Действие без значения\
**Описание:** Создаёт взрыв в указанном местоположении.

**Пример использования:**
```ts
world::create_explosion(location(0,0,0,0,0), 1, "name_or_uuid", "FALSE", "FALSE");

//Или в сухую по ключам

world::create_explosion(location=location(0,0,0,0,0), power=1, name_or_uuid="name_or_uuid", fire="FALSE", break_blocks="FALSE");
```

**Аргументы:**

| ID           | Тип                                                      | Описание                      |
|--------------|----------------------------------------------------------|-------------------------------|
| location     | Местоположение                                           | Место создания                |
| power        | Число                                                    | Сила взрыва (от 0 до 4)       |
| name_or_uuid | Текст                                                    | Имя или UUID источника взрыва |
| fire         | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Появление огня                |
| break_blocks | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Разрушение блоков             |

<h3 id=game_create_scoreboard>
  <code>world::create_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать скорборд\
**Тип:** Действие без значения\
**Описание:** Создаёт скорборд с определённым ID. Чтобы отобразить скорборд игроку, используйте действие "Показать скорборд".

**Пример использования:**
```ts
world::create_scoreboard("id", "display_name");

//Или в сухую по ключам

world::create_scoreboard(id="id", display_name="display_name");
```

**Аргументы:**

| ID           | Тип   | Описание     |
|--------------|-------|--------------|
| id           | Текст | ID скорборда |
| display_name | Текст | Заголовок    |

<h3 id=game_dummy>
  <code>world::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** ...\
**Тип:** Действие без значения\
**Описание:** ...

**Пример использования:**
```ts
world::dummy();
```

<h3 id=game_fill_container>
  <code>world::fill_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заполнить контейнер\
**Тип:** Действие без значения\
**Описание:** Заполняет контейнер на выбранном местоположении указанными предметами.\
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:**
```ts
world::fill_container([item("stick"), item("stick")], location(0,0,0,0,0));

//Или в сухую по ключам

world::fill_container(items=[item("stick"), item("stick")], location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип               | Описание                  |
|----------|-------------------|---------------------------|
| items    | Список\[Предмет\] | Предметы для заполнения   |
| location | Местоположение    | Местоположение контейнера |

<h3 id=game_generate_tree>
  <code>world::generate_tree</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать дерево\
**Тип:** Действие без значения\
**Описание:** Создаёт дерево на выбранном местоположении.

**Пример использования:**
```ts
world::generate_tree(location(0,0,0,0,0), "ACACIA");

//Или в сухую по ключам

world::generate_tree(location=location(0,0,0,0,0), tree_type="ACACIA");
```

**Аргументы:**

| ID        | Тип                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Описание              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| location  | Местоположение                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Местоположение дерева |
| tree_type | Маркер<br/>**ACACIA** - Акация<br/>**AZALEA** - Азалия<br/>**BIG_TREE** - Большое дерево<br/>**BIRCH** - Обычная берёза<br/>**BROWN_MUSHROOM** - Коричневый гриб<br/>**CHERRY** - Вишня<br/>**CHORUS_PLANT** - Дерево хоруса<br/>**COCOA_TREE** - Дерево джунглей с какао-бобами<br/>**CRIMSON_FUNGUS** - Багровый гриб<br/>**DARK_OAK** - Тёмный дуб<br/>**JUNGLE** - Дерево джунглей<br/>**JUNGLE_BUSH** - Куст джунглей<br/>**MANGROVE** - Мангровое дерево<br/>**MEGA_PINE** - Огромная сосна<br/>**MEGA_REDWOOD** - Огромная секвойя<br/>**REDWOOD** - Обычная ель<br/>**RED_MUSHROOM** - Красный гриб<br/>**SMALL_JUNGLE** - Маленькое дерево джунглей<br/>**SWAMP** - Болотное дерево<br/>**TALL_BIRCH** - Высокая берёза<br/>**TALL_MANGROVE** - Высокое мангровое дерево<br/>**TALL_REDWOOD** - Высокая ель<br/>**TREE** - Обычное дерево<br/>**WARPED_FUNGUS** - Искажённый гриб | Тип дерева            |

<h3 id=game_hide_event_message>
  <code>world::hide_event_message</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Убрать сообщение события\
**Тип:** Действие без значения\
**Описание:** Убирает отправку сообщения события, которое вызвало этот код.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок зашёл в мир"\
&nbsp;&nbsp;Событием "Игрок вышел из мира"\
&nbsp;&nbsp;Событием "Игрок умирает"

**Пример использования:**
```ts
world::hide_event_message("FALSE");

//Или в сухую по ключам

world::hide_event_message(hide="FALSE");
```

**Аргументы:**

| ID   | Тип                                          | Описание         |
|------|----------------------------------------------|------------------|
| hide | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да | Убрать сообщение |

<h3 id=game_launch_firework>
  <code>world::launch_firework</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать фейерверк\
**Тип:** Действие без значения\
**Описание:** Запускает фейерверк в указанном местоположении.

**Пример использования:**
```ts
world::launch_firework(item("stick"), location(0,0,0,0,0), "DIRECTIONAL", "FALSE");

//Или в сухую по ключам

world::launch_firework(firework=item("stick"), location=location(0,0,0,0,0), movement="DIRECTIONAL", instant="FALSE");
```

**Аргументы:**

| ID       | Тип                                                               | Описание               |
|----------|-------------------------------------------------------------------|------------------------|
| firework | Предмет                                                           | Фейерверк для создания |
| location | Местоположение                                                    | Место создания         |
| movement | Маркер<br/>**DIRECTIONAL** - Направленное<br/>**UPWARDS** - Вверх | Движение               |
| instant  | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да                      | Мгновенный взрыв       |

<h3 id=game_launch_projectile>
  <code>world::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить снаряд\
**Тип:** Действие без значения\
**Описание:** Запускает снаряд в указанном местоположении.

**Пример использования:**
```ts
world::launch_projectile(item("stick"), location(0,0,0,0,0), 1, 2, "custom_name", particle("fire"));

//Или в сухую по ключам

world::launch_projectile(projectile=item("stick"), location=location(0,0,0,0,0), speed=1, inaccuracy=2, custom_name="custom_name", trail=particle("fire"));
```

**Аргументы:**

| ID          | Тип            | Описание                                         |
|-------------|----------------|--------------------------------------------------|
| projectile  | Предмет        | Снаряд для запуска                               |
| location    | Местоположение | Место запуска                                    |
| speed       | Число          | Скорость снаряда                                 |
| inaccuracy  | Число          | Отклонение снаряда (0, чтобы снаряд летел ровно) |
| custom_name | Текст          | Имя снаряда                                      |
| trail       | Эффект частиц  | След, который будет оставаться за снарядом       |

<h3 id=game_random_tick_block>
  <code>world::random_tick_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Вызвать случайный тик\
**Тип:** Действие без значения\
**Описание:** Вызывает случайный тик на выбранном местоположении.

**Пример использования:**
```ts
world::random_tick_block(location(0,0,0,0,0), 1);

//Или в сухую по ключам

world::random_tick_block(location=location(0,0,0,0,0), times=1);
```

**Аргументы:**

| ID       | Тип            | Описание         |
|----------|----------------|------------------|
| location | Местоположение | Местоположение   |
| times    | Число          | Количество тиков |

<h3 id=game_remove_container_items>
  <code>world::remove_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить предметы из контейнера\
**Тип:** Действие без значения\
**Описание:** Удаляет из контейнера на выбранном местоположении указанные предметы.\
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:**
```ts
world::remove_container_items([item("stick"), item("stick")], location(0,0,0,0,0));

//Или в сухую по ключам

world::remove_container_items(items=[item("stick"), item("stick")], location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип               | Описание                  |
|----------|-------------------|---------------------------|
| items    | Список\[Предмет\] | Предметы                  |
| location | Местоположение    | Местоположение контейнера |

<h3 id=game_remove_scoreboard>
  <code>world::remove_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить скорборд\
**Тип:** Действие без значения\
**Описание:** Удаляет указанный скорборд.

**Пример использования:**
```ts
world::remove_scoreboard("id");

//Или в сухую по ключам

world::remove_scoreboard(id="id");
```

**Аргументы:**

| ID | Тип   | Описание     |
|----|-------|--------------|
| id | Текст | ID скорборда |

<h3 id=game_remove_scoreboard_score_by_name>
  <code>world::remove_scoreboard_score_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить значение скорборда по тексту\
**Тип:** Действие без значения\
**Описание:** Удаляет значение указанной строки в скорборде.

**Пример использования:**
```ts
world::remove_scoreboard_score_by_name("id", "text");

//Или в сухую по ключам

world::remove_scoreboard_score_by_name(id="id", text="text");
```

**Аргументы:**

| ID   | Тип   | Описание     |
|------|-------|--------------|
| id   | Текст | ID скорборда |
| text | Текст | ID линии     |

<h3 id=game_remove_scoreboard_score_by_score>
  <code>world::remove_scoreboard_score_by_score</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить значение скорборда по счёту\
**Тип:** Действие без значения\
**Описание:** Удаляет значение указанного скорборда по счёту.

**Пример использования:**
```ts
world::remove_scoreboard_score_by_score("id", 1);

//Или в сухую по ключам

world::remove_scoreboard_score_by_score(id="id", score=1);
```

**Аргументы:**

| ID    | Тип   | Описание                   |
|-------|-------|----------------------------|
| id    | Текст | ID скорборда               |
| score | Число | Счёт значения для удаления |

<h3 id=game_remove_tile_block_custom_tag>
  <code>world::remove_tile_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить кастомный тег блока-сущности\
**Тип:** Действие без значения\
**Описание:** Удаляет указанный кастомный тег блока-сущности на местоположении.\
**Работает с:**\
&nbsp;&nbsp;Блоками-сущностями (сундуки, таблички, бочки и т.д.)

**Пример использования:**
```ts
world::remove_tile_block_custom_tag(location(0,0,0,0,0), "tag_name");

//Или в сухую по ключам

world::remove_tile_block_custom_tag(location=location(0,0,0,0,0), tag_name="tag_name");
```

**Аргументы:**

| ID       | Тип            | Описание                      |
|----------|----------------|-------------------------------|
| location | Местоположение | Местоположение блока-сущности |
| tag_name | Текст          | Имя кастомного тега           |

<h3 id=game_replace_blocks_in_region>
  <code>world::replace_blocks_in_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заменить блоки в регионе\
**Тип:** Действие без значения\
**Описание:** Заменяет одни блоки на другие в выбранном регионе.

**Пример использования:**
```ts
world::replace_blocks_in_region(["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], location(0,0,0,0,0), location(0,0,0,0,0), "minecraft:oak_log[axis=x]");

//Или в сухую по ключам

world::replace_blocks_in_region(old_block=["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], pos_1=location(0,0,0,0,0), pos_2=location(0,0,0,0,0), new_block="minecraft:oak_log[axis=x]");
```

**Аргументы:**

| ID        | Тип            | Описание                     |
|-----------|----------------|------------------------------|
| old_block | Список\[Блок\] | Блоки для замены             |
| pos_1     | Местоположение | Угол региона                 |
| pos_2     | Местоположение | Противоположный угол региона |
| new_block | Блок           | Новый блок                   |

<h3 id=game_replace_container_items>
  <code>world::replace_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заменить предметы в контейнере\
**Тип:** Действие без значения\
**Описание:** Заменяет указанные предметы в контейнере на выбранном местоположении на определённый предмет.\
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:**
```ts
world::replace_container_items([item("stick"), item("stick")], location(0,0,0,0,0), item("stick"), 1);

//Или в сухую по ключам

world::replace_container_items(items=[item("stick"), item("stick")], location=location(0,0,0,0,0), replace=item("stick"), count=1);
```

**Аргументы:**

| ID       | Тип               | Описание                        |
|----------|-------------------|---------------------------------|
| items    | Список\[Предмет\] | Заменяемые предметы             |
| location | Местоположение    | Местоположение контейнера       |
| replace  | Предмет           | Заменяющий предмет              |
| count    | Число             | Количество предметов для замены |

<h3 id=game_send_web_request>
  <code>world::send_web_request</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отправить веб-запрос\
**Тип:** Действие без значения\
**Описание:** Отправляет веб-запрос с выбранным методом и телом на выбранный URL.

**Пример использования:**
```ts
world::send_web_request("url", "content_body", {"headers":`headers`}, "DELETE", "APPLICATION_JSON");

//Или в сухую по ключам

world::send_web_request(url="url", content_body="content_body", headers={"headers":`headers`}, request_type="DELETE", content_type="APPLICATION_JSON");
```

**Аргументы:**

| ID           | Тип                                                                                                                              | Описание          |
|--------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------|
| url          | Текст                                                                                                                            | URL               |
| content_body | Текст                                                                                                                            | Тело запроса      |
| headers      | Словарь                                                                                                                          | Заголовки запроса |
| request_type | Маркер<br/>**DELETE** - DELETE<br/>**GET** - GET<br/>**HEAD** - HEAD<br/>**PATCH** - PATCH<br/>**POST** - POST<br/>**PUT** - PUT | Тип запроса       |
| content_type | Маркер<br/>**APPLICATION_JSON** - JSON (application/json)<br/>**TEXT_PLAIN** - Обычный текст (text/plain)                        | Медиа тип запроса |

<h3 id=game_set_age>
  <code>world::set_age</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить возраст\
**Тип:** Действие без значения\
**Описание:** Устанавливает возраст блока на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Любыми блоками, которые могут иметь возраст

**Пример использования:**
```ts
world::set_age(location(0,0,0,0,0), 1);

//Или в сухую по ключам

world::set_age(location=location(0,0,0,0,0), tick=1);
```

**Аргументы:**

| ID       | Тип            | Описание             |
|----------|----------------|----------------------|
| location | Местоположение | Местоположение блока |
| tick     | Число          | Тики                 |

<h3 id=game_set_block>
  <code>world::set_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить блок\
**Тип:** Действие без значения\
**Описание:** Устанавливает выбранный тип блока на выбранных местоположениях.

**Пример использования:**
```ts
world::set_block([location(0,0,0,0,0), location(0,0,0,0,0)], "minecraft:oak_log[axis=x]", "FALSE");

//Или в сухую по ключам

world::set_block(locations=[location(0,0,0,0,0), location(0,0,0,0,0)], block="minecraft:oak_log[axis=x]", update_blocks="FALSE");
```

**Аргументы:**

| ID            | Тип                                                          | Описание                       |
|---------------|--------------------------------------------------------------|--------------------------------|
| locations     | Список\[Местоположение\]                                     | Местоположения установки блока |
| block         | Блок                                                         | Блок                           |
| update_blocks | Маркер<br/>**FALSE** - Не обновлять<br/>**TRUE** - Обновлять | Обновлять блоки вокруг         |

<h3 id=game_set_block_analogue_power>
  <code>world::set_block_analogue_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить силу редстоун-сигнала\
**Тип:** Действие без значения\
**Описание:** Устанавливает на выбранном местоположении определённую силу сигнала.\
**Работает с:**\
&nbsp;&nbsp;Активируемыми блоками

**Пример использования:**
```ts
world::set_block_analogue_power(location(0,0,0,0,0), 1);

//Или в сухую по ключам

world::set_block_analogue_power(location=location(0,0,0,0,0), power_level=1);
```

**Аргументы:**

| ID          | Тип            | Описание             |
|-------------|----------------|----------------------|
| location    | Местоположение | Местоположение блока |
| power_level | Число          | Новая сила сигнала   |

<h3 id=game_set_block_custom_tag>
  <code>world::set_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** creative_plus.action.game_set_block_custom_tag.name\
**Тип:** Действие без значения\
**Описание:** creative_plus.action.game_set_block_custom_tag.description

**Пример использования:**
```ts
world::set_block_custom_tag(location(0,0,0,0,0), "tag_name", "tag_value");

//Или в сухую по ключам

world::set_block_custom_tag(location=location(0,0,0,0,0), tag_name="tag_name", tag_value="tag_value");
```

**Аргументы:**

| ID        | Тип            | Описание                                                               |
|-----------|----------------|------------------------------------------------------------------------|
| location  | Местоположение | creative_plus.action.game_set_block_custom_tag.argument.location.name  |
| tag_name  | Текст          | creative_plus.action.game_set_block_custom_tag.argument.tag_name.name  |
| tag_value | Текст          | creative_plus.action.game_set_block_custom_tag.argument.tag_value.name |

<h3 id=game_set_block_data>
  <code>world::set_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить параметры блоку\
**Тип:** Действие без значения\
**Описание:** Устанавливает параметры блоку на определённом местоположении.

**Пример использования:**
```ts
world::set_block_data(location(0,0,0,0,0), "block_data");

//Или в сухую по ключам

world::set_block_data(location=location(0,0,0,0,0), block_data="block_data");
```

**Аргументы:**

| ID         | Тип            | Описание              |
|------------|----------------|-----------------------|
| location   | Местоположение | Местоположение блока  |
| block_data | Текст          | Новые параметры блока |

<h3 id=game_set_block_drops_enabled>
  <code>world::set_block_drops_enabled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить выпадение блоков\
**Тип:** Действие без значения\
**Описание:** Устанавливает правило в мире на выпадение блоков при их разрушении.

**Пример использования:**
```ts
world::set_block_drops_enabled("FALSE");

//Или в сухую по ключам

world::set_block_drops_enabled(enable="FALSE");
```

**Аргументы:**

| ID     | Тип                                                      | Описание         |
|--------|----------------------------------------------------------|------------------|
| enable | Маркер<br/>**FALSE** - Выключено<br/>**TRUE** - Включено | Выпадение блоков |

<h3 id=game_set_block_powered>
  <code>world::set_block_powered</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Активировать блок\
**Тип:** Действие без значения\
**Описание:** Активирует блок на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Активируемыми блоками

**Пример использования:**
```ts
world::set_block_powered(location(0,0,0,0,0), "FALSE");

//Или в сухую по ключам

world::set_block_powered(location=location(0,0,0,0,0), powered="FALSE");
```

**Аргументы:**

| ID       | Тип                                                      | Описание             |
|----------|----------------------------------------------------------|----------------------|
| location | Местоположение                                           | Местоположение блока |
| powered  | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Активация            |

<h3 id=game_set_block_single_data>
  <code>world::set_block_single_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить параметр блоку\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанный параметр блоку на местоположении на заданое значение.

**Пример использования:**
```ts
world::set_block_single_data(location(0,0,0,0,0), "data", "value");

//Или в сухую по ключам

world::set_block_single_data(location=location(0,0,0,0,0), data="data", value="value");
```

**Аргументы:**

| ID       | Тип            | Описание             |
|----------|----------------|----------------------|
| location | Местоположение | Местоположение блока |
| data     | Текст          | Изменяемый параметр  |
| value    | Текст          | Новое значение       |

<h3 id=game_set_brushable_block_item>
  <code>world::set_brushable_block_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет в подозрительный блок\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет в подозрительный блок (песок, гравий) на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Подозрительным песком\
&nbsp;&nbsp;Подозрительным гравием

**Пример использования:**
```ts
world::set_brushable_block_item(location(0,0,0,0,0), item("stick"));

//Или в сухую по ключам

world::set_brushable_block_item(location=location(0,0,0,0,0), item=item("stick"));
```

**Аргументы:**

| ID       | Тип            | Описание             |
|----------|----------------|----------------------|
| location | Местоположение | Местоположение блока |
| item     | Предмет        | Предмет              |

<h3 id=game_set_campfire_item>
  <code>world::set_campfire_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет в костёр\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет в костёр на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Кострами

**Пример использования:**
```ts
world::set_campfire_item(location(0,0,0,0,0), item("stick"), 1, "FIRST");

//Или в сухую по ключам

world::set_campfire_item(location=location(0,0,0,0,0), item=item("stick"), cooking_time=1, slot="FIRST");
```

**Аргументы:**

| ID           | Тип                                                                                                     | Описание              |
|--------------|---------------------------------------------------------------------------------------------------------|-----------------------|
| location     | Местоположение                                                                                          | Местоположение костра |
| item         | Предмет                                                                                                 | Предмет               |
| cooking_time | Число                                                                                                   | Время готовки         |
| slot         | Маркер<br/>**FIRST** - Первый<br/>**FOURTH** - Четвёртый<br/>**SECOND** - Второй<br/>**THIRD** - Третий | Слот                  |

<h3 id=game_set_container>
  <code>world::set_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предметы в контейнере\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанные предметы в контейнер на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:**
```ts
world::set_container([item("stick"), item("stick")], [location(0,0,0,0,0), location(0,0,0,0,0)]);

//Или в сухую по ключам

world::set_container(items=[item("stick"), item("stick")], location=[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

**Аргументы:**

| ID       | Тип                      | Описание                  |
|----------|--------------------------|---------------------------|
| items    | Список\[Предмет\]        | Предметы для установки    |
| location | Список\[Местоположение\] | Местоположение контейнера |

<h3 id=game_set_container_lock>
  <code>world::set_container_lock</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить ключ контейнера\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённый ключ контейнеру на выбранном местоположении.\
**Дополнительная информация:**\
&nbsp;&nbsp;В качестве ключа контейнера служит любой предмет с определённым именем.

**Пример использования:**
```ts
world::set_container_lock(location(0,0,0,0,0), "container_key");

//Или в сухую по ключам

world::set_container_lock(location=location(0,0,0,0,0), container_key="container_key");
```

**Аргументы:**

| ID            | Тип            | Описание                  |
|---------------|----------------|---------------------------|
| location      | Местоположение | Местоположение контейнера |
| container_key | Текст          | Имя ключа контейнера      |

<h3 id=game_set_container_name>
  <code>world::set_container_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить имя контейнеру\
**Тип:** Действие без значения\
**Описание:** Устанавливает имя контейнеру на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:**
```ts
world::set_container_name(location(0,0,0,0,0), "name");

//Или в сухую по ключам

world::set_container_name(location=location(0,0,0,0,0), name="name");
```

**Аргументы:**

| ID       | Тип            | Описание                  |
|----------|----------------|---------------------------|
| location | Местоположение | Местоположение контейнера |
| name     | Текст          | Имя контейнера            |

<h3 id=game_set_creaking_heart_natural>
  <code>world::set_creaking_heart_natural</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить натуральность скрипцевины\
**Тип:** Действие без значения\
**Описание:** Устанавливает натуральность скрипцевины, находящейся на указанном местоположении.\
**Дополнительная информация:**\
&nbsp;&nbsp;Натуральность скрипцевины определяет выпадет ли опыт при её разрушении.\
**Работает с:**\
&nbsp;&nbsp;Скрипцевинами

**Пример использования:**
```ts
world::set_creaking_heart_natural(location(0,0,0,0,0), "TRUE");

//Или в сухую по ключам

world::set_creaking_heart_natural(location=location(0,0,0,0,0), natural="TRUE");
```

**Аргументы:**

| ID       | Тип                                          | Описание       |
|----------|----------------------------------------------|----------------|
| location | Местоположение                               | Местоположение |
| natural  | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет | Натуральность  |

<h3 id=game_set_creaking_heart_state>
  <code>world::set_creaking_heart_state</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить состояние скрипцевине\
**Тип:** Действие без значения\
**Описание:** Устанавливает состояние скрипцевине, находящейся на указанном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Скрипцевинами

**Пример использования:**
```ts
world::set_creaking_heart_state(location(0,0,0,0,0), "UPROOTED");

//Или в сухую по ключам

world::set_creaking_heart_state(location=location(0,0,0,0,0), heart_state="UPROOTED");
```

**Аргументы:**

| ID          | Тип                                                                                    | Описание       |
|-------------|----------------------------------------------------------------------------------------|----------------|
| location    | Местоположение                                                                         | Местоположение |
| heart_state | Маркер<br/>**UPROOTED** - Неактивная<br/>**DORMANT** - Спящая<br/>**AWAKE** - Активная | Состояние      |

<h3 id=game_set_decorate_pot_sherd>
  <code>world::set_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить украшение вазы\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанный черепок выбранной стороне вазы на указанном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Вазами

**Пример использования:**
```ts
world::set_decorate_pot_sherd(location(0,0,0,0,0), item("stick"), "BACK");

//Или в сухую по ключам

world::set_decorate_pot_sherd(location=location(0,0,0,0,0), item=item("stick"), side="BACK");
```

**Аргументы:**

| ID       | Тип                                                                                                                               | Описание              |
|----------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| location | Местоположение                                                                                                                    | Местоположение вазы   |
| item     | Предмет                                                                                                                           | Черепок для установки |
| side     | Маркер<br/>**BACK** - Задняя сторона<br/>**FRONT** - Передняя сторона<br/>**LEFT** - Левая сторона<br/>**RIGHT** - Правая сторона | Сторона вазы          |

<h3 id=game_set_dried_ghast_hydration>
  <code>world::set_dried_ghast_hydration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить влажность Высушенному гасту\
**Тип:** Действие без значения\
**Описание:** Устанавливает влажность Высушенному гасту, который находится на указанном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Высушенными гастами

**Пример использования:**
```ts
world::set_dried_ghast_hydration(location(0,0,0,0,0), 1);

//Или в сухую по ключам

world::set_dried_ghast_hydration(location=location(0,0,0,0,0), hydration=1);
```

**Аргументы:**

| ID        | Тип            | Описание       |
|-----------|----------------|----------------|
| location  | Местоположение | Местоположение |
| hydration | Число          | Влажность      |

<h3 id=game_set_event_anvil_repair_cost>
  <code>world::set_event_anvil_repair_cost</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стоимость действия наковальни\
**Тип:** Действие без значения\
**Описание:** Устанавливает стоимость совершаемого действия в наковальне.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок получает результат"

**Пример использования:**
```ts
world::set_event_anvil_repair_cost(1, "REPAIR_COST", "TRUE");

//Или в сухую по ключам

world::set_event_anvil_repair_cost(repair_cost=1, repair_cost_type="REPAIR_COST", bypass_cost="TRUE");
```

**Аргументы:**

| ID               | Тип                                                                                                                                                               | Описание                |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| repair_cost      | Число                                                                                                                                                             | Стоимость               |
| repair_cost_type | Маркер<br/>**REPAIR_COST** - Конечная стоимость<br/>**REPAIR_ITEM_COUNT_COST** - Стоимость за каждый предмет<br/>**MAXIMUM_REPAIR_COST** - Максимальная стоимость | Тип стоимости           |
| bypass_cost      | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет                                                                                                                      | Игнорирование стоимости |

<h3 id=game_set_event_combust_duration>
  <code>world::set_event_combust_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время горения события\
**Тип:** Действие без значения\
**Описание:** Устанавливает время горения, связанное с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок загорелся"\
&nbsp;&nbsp;Событием "Сущность загорелась"

**Пример использования:**
```ts
world::set_event_combust_duration(1);

//Или в сухую по ключам

world::set_event_combust_duration(duration=1);
```

**Аргументы:**

| ID       | Тип   | Описание      |
|----------|-------|---------------|
| duration | Число | Время горения |

<h3 id=game_set_event_damage>
  <code>world::set_event_damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить урон события\
**Тип:** Действие без значения\
**Описание:** Устанавливает урон, связанный с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событиями урона

**Пример использования:**
```ts
world::set_event_damage(1);

//Или в сухую по ключам

world::set_event_damage(damage=1);
```

**Аргументы:**

| ID     | Тип   | Описание         |
|--------|-------|------------------|
| damage | Число | Количество урона |

<h3 id=game_set_event_death_screen_message>
  <code>world::set_event_death_screen_message</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить сообщение при смерти\
**Тип:** Действие без значения\
**Описание:** Устанавливает сообщение при смерти, отображаемое на экране смерти, связанное с этим событием.\
**Дополнительная информация:**\
&nbsp;&nbsp;Если передаваемое значение пустое, устанавливается сообщение по умолчанию.\
&nbsp;&nbsp;Устанавливаемое сообщение ограничено 256 символами.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок умирает"

**Пример использования:**
```ts
world::set_event_death_screen_message("message");

//Или в сухую по ключам

world::set_event_death_screen_message(message="message");
```

**Аргументы:**

| ID      | Тип   | Описание  |
|---------|-------|-----------|
| message | Текст | Сообщение |

<h3 id=game_set_event_enchantment_offers>
  <code>world::set_event_enchantment_offers</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предлагаемые зачарования события\
**Тип:** Действие без значения\
**Описание:** Устанавливает предлагаемые зачарования события.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок выбирает зачарование"

**Пример использования:**
```ts
world::set_event_enchantment_offers(["enchantments", "enchantments"], ["levels", "levels"], ["costs", "costs"]);

//Или в сухую по ключам

world::set_event_enchantment_offers(enchantments=["enchantments", "enchantments"], levels=["levels", "levels"], costs=["costs", "costs"]);
```

**Аргументы:**

| ID           | Тип             | Описание                 |
|--------------|-----------------|--------------------------|
| enchantments | Список\[Текст\] | Предлагаемые зачарования |
| levels       | Список\[Текст\] | Уровни зачарований       |
| costs        | Список\[Текст\] | Стоимость зачарований    |

<h3 id=game_set_event_exhaustion>
  <code>world::set_event_exhaustion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить истощение события\
**Тип:** Действие без значения\
**Описание:** Устанавливает значение истощения, связанное с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок истощается"

**Пример использования:**
```ts
world::set_event_exhaustion(1);

//Или в сухую по ключам

world::set_event_exhaustion(exhaustion=1);
```

**Аргументы:**

| ID         | Тип   | Описание             |
|------------|-------|----------------------|
| exhaustion | Число | Количество истощения |

<h3 id=game_set_event_experience>
  <code>world::set_event_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить опыт события\
**Тип:** Действие без значения\
**Описание:** Устанавливает значение опыта, связанное с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок рыбачит"\
&nbsp;&nbsp;Событием "Игрок поднял сферу опыта"\
&nbsp;&nbsp;Событиями убийства

**Пример использования:**
```ts
world::set_event_experience(1);

//Или в сухую по ключам

world::set_event_experience(experience=1);
```

**Аргументы:**

| ID         | Тип   | Описание         |
|------------|-------|------------------|
| experience | Число | Количество опыта |

<h3 id=game_set_event_gamemode>
  <code>world::set_event_gamemode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим игры события\
**Тип:** Действие без значения\
**Описание:** Устанавливает режим игры, связанный с событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок запросил меню смены режима игры"

**Пример использования:**
```ts
world::set_event_gamemode("CREATIVE");

//Или в сухую по ключам

world::set_event_gamemode(gamemode="CREATIVE");
```

**Аргументы:**

| ID       | Тип                                                                                                                               | Описание   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------|------------|
| gamemode | Маркер<br/>**CREATIVE** - Творческий<br/>**SURVIVAL** - Выживание<br/>**ADVENTURE** - Приключение<br/>**SPECTATOR** - Наблюдатель | Режим игры |

<h3 id=game_set_event_heal>
  <code>world::set_event_heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить лечение события\
**Тип:** Действие без значения\
**Описание:** Устанавливает значение лечения, связанное с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок восстанавливает здоровье"\
&nbsp;&nbsp;Событием "Сущность исцеляется"

**Пример использования:**
```ts
world::set_event_heal(1);

//Или в сухую по ключам

world::set_event_heal(heal=1);
```

**Аргументы:**

| ID   | Тип   | Описание           |
|------|-------|--------------------|
| heal | Число | Количество лечения |

<h3 id=game_set_event_item>
  <code>world::set_event_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет события\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет, связанный с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Раздатчик надевает броню"\
&nbsp;&nbsp;Событием "Блок выбрасывает предмет"\
&nbsp;&nbsp;Событием "Игрок употребляет предмет"\
&nbsp;&nbsp;Событием "Игрок крафтит предмет"\
&nbsp;&nbsp;Событием "Игрок выбрасывает предмет"\
&nbsp;&nbsp;Событием "Существо выбрасывает предмет"\
&nbsp;&nbsp;Событием "Существо поднимает предмет"\
&nbsp;&nbsp;Событием "Игрок кликает в своём инвентаре"\
&nbsp;&nbsp;Событием "Игрок кликает в инвентаре"\
&nbsp;&nbsp;Событием "Игрок изменяет книгу"\
&nbsp;&nbsp;Событием "Игрок поднял снаряд"\
&nbsp;&nbsp;Событием "Ведьма кидает зелье"\
&nbsp;&nbsp;Событием "Игрок получает результат"

**Пример использования:**
```ts
world::set_event_item(item("stick"));

//Или в сухую по ключам

world::set_event_item(item=item("stick"));
```

**Аргументы:**

| ID   | Тип     | Описание              |
|------|---------|-----------------------|
| item | Предмет | Новый предмет события |

<h3 id=game_set_event_item_cooldown>
  <code>world::set_event_item_cooldown</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить задержку предмета события\
**Тип:** Действие без значения\
**Описание:** Устанавливает задержку предмета, связанную с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок использует предмет с задержкой"\
&nbsp;&nbsp;Событием "Игрок получает задержку для группы предметов"

**Пример использования:**
```ts
world::set_event_item_cooldown(1);

//Или в сухую по ключам

world::set_event_item_cooldown(cooldown=1);
```

**Аргументы:**

| ID       | Тип   | Описание         |
|----------|-------|------------------|
| cooldown | Число | Задержка в тиках |

<h3 id=game_set_event_items>
  <code>world::set_event_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предметы события\
**Тип:** Действие без значения\
**Описание:** Устанавливает предметы, связанные с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок находит предмет в инвентаре"

**Пример использования:**
```ts
world::set_event_items([item("stick"), item("stick")]);

//Или в сухую по ключам

world::set_event_items(items=[item("stick"), item("stick")]);
```

**Аргументы:**

| ID    | Тип               | Описание               |
|-------|-------------------|------------------------|
| items | Список\[Предмет\] | Предметы для установки |

<h3 id=game_set_event_knockback_vector>
  <code>world::set_event_knockback_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить вектор отталкивания события\
**Тип:** Действие без значения\
**Описание:** Устанавливает вектор отталкивания, связанный с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок отталкивается"\
&nbsp;&nbsp;Событием "Сущность отталкивается"

**Пример использования:**
```ts
world::set_event_knockback_vector(vector(0,0,0));

//Или в сухую по ключам

world::set_event_knockback_vector(knockback=vector(0,0,0));
```

**Аргументы:**

| ID        | Тип    | Описание            |
|-----------|--------|---------------------|
| knockback | Вектор | Вектор отталкивания |

<h3 id=game_set_event_move_allowed>
  <code>world::set_event_move_allowed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Разрешить передвижение\
**Тип:** Действие без значения\
**Описание:** Разрешает передвижение, если оно не удалось.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игроку не удалось передвинуться"

**Пример использования:**
```ts
world::set_event_move_allowed("FALSE");

//Или в сухую по ключам

world::set_event_move_allowed(allowed="FALSE");
```

**Аргументы:**

| ID      | Тип                                          | Описание               |
|---------|----------------------------------------------|------------------------|
| allowed | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да | Разрешить передвижение |

<h3 id=game_set_event_projectile>
  <code>world::set_event_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить снаряд события\
**Тип:** Действие без значения\
**Описание:** Заменяет снаряд, который связан с этим событием.

**Пример использования:**
```ts
world::set_event_projectile(item("stick"), "name");

//Или в сухую по ключам

world::set_event_projectile(projectile=item("stick"), name="name");
```

**Аргументы:**

| ID         | Тип     | Описание                 |
|------------|---------|--------------------------|
| projectile | Предмет | Снаряд                   |
| name       | Текст   | Отображаемое имя снаряда |

<h3 id=game_set_event_sound>
  <code>world::set_event_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить звук события\
**Тип:** Действие без значения\
**Описание:** Устанавливает звук для проигрывания, связанный с этим событием, заменяя изначальный.

**Пример использования:**
```ts
world::set_event_sound(sound("entity.zombie.hurt"));

//Или в сухую по ключам

world::set_event_sound(sound=sound("entity.zombie.hurt"));
```

**Аргументы:**

| ID    | Тип  | Описание           |
|-------|------|--------------------|
| sound | Звук | Проигрываемый звук |

<h3 id=game_set_event_source_slot>
  <code>world::set_event_source_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить начальный слот события\
**Тип:** Действие без значения\
**Описание:** Устанавливает начальный слот, связанный с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок находит предмет в инвентаре"

**Пример использования:**
```ts
world::set_event_source_slot(1);

//Или в сухую по ключам

world::set_event_source_slot(source_slot=1);
```

**Аргументы:**

| ID          | Тип   | Описание           |
|-------------|-------|--------------------|
| source_slot | Число | Слот для установки |

<h3 id=game_set_event_target_slot>
  <code>world::set_event_target_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить конечный слот события\
**Тип:** Действие без значения\
**Описание:** Устанавливает конечный слот, связанный с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок находит предмет в инвентаре"

**Пример использования:**
```ts
world::set_event_target_slot(1);

//Или в сухую по ключам

world::set_event_target_slot(target=1);
```

**Аргументы:**

| ID     | Тип   | Описание           |
|--------|-------|--------------------|
| target | Число | Слот для установки |

<h3 id=game_set_event_uery_info>
  <code>world::set_event_uery_info</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить теги в полученную информацию\
**Тип:** Действие без значения\
**Описание:** Устанавливает дополнительные теги в полученную отладочную информацию, которые скопируются в буфер обмена, если событие не отменено.\
**Дополнительная информация:**\
&nbsp;&nbsp;Изменения касаются только дополнительной информации.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок получает информацию о блоке"\
&nbsp;&nbsp;Событием "Игрок получает информацию о сущности"

**Пример использования:**
```ts
world::set_event_uery_info("information");

//Или в сухую по ключам

world::set_event_uery_info(information="information");
```

**Аргументы:**

| ID          | Тип   | Описание            |
|-------------|-------|---------------------|
| information | Текст | Дополнительные теги |

<h3 id=game_set_event_velocity>
  <code>world::set_event_velocity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить вектор скорости события\
**Тип:** Действие без значения\
**Описание:** Устанавливает вектор скорости, связанный с этим событием.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок изменил вектор скорости"

**Пример использования:**
```ts
world::set_event_velocity(vector(0,0,0));

//Или в сухую по ключам

world::set_event_velocity(velocity=vector(0,0,0));
```

**Аргументы:**

| ID       | Тип    | Описание        |
|----------|--------|-----------------|
| velocity | Вектор | Вектор скорости |

<h3 id=game_set_furnace_cook_time>
  <code>world::set_furnace_cook_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время готовки печи\
**Тип:** Действие без значения\
**Описание:** Устанавливает время готовки печи на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Печками\
&nbsp;&nbsp;Плавильнями\
&nbsp;&nbsp;Коптильнями

**Пример использования:**
```ts
world::set_furnace_cook_time(location(0,0,0,0,0), 1);

//Или в сухую по ключам

world::set_furnace_cook_time(location=location(0,0,0,0,0), time=1);
```

**Аргументы:**

| ID       | Тип            | Описание            |
|----------|----------------|---------------------|
| location | Местоположение | Местоположение печи |
| time     | Число          | Время готовки       |

<h3 id=game_set_item_in_container_slot>
  <code>world::set_item_in_container_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет в слот контейнера\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет в указанный слот контейнера на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:**
```ts
world::set_item_in_container_slot(location(0,0,0,0,0), item("stick"), 1);

//Или в сухую по ключам

world::set_item_in_container_slot(location=location(0,0,0,0,0), item=item("stick"), slot=1);
```

**Аргументы:**

| ID       | Тип            | Описание                  |
|----------|----------------|---------------------------|
| location | Местоположение | Местоположение контейнера |
| item     | Предмет        | Предмет                   |
| slot     | Число          | Номер слота               |

<h3 id=game_set_lectern_book>
  <code>world::set_lectern_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить книгу в кафедру\
**Тип:** Действие без значения\
**Описание:** Устанавливает книгу в кафедру на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Кафедрами

**Пример использования:**
```ts
world::set_lectern_book(location(0,0,0,0,0), item("stick"), 1);

//Или в сухую по ключам

world::set_lectern_book(location=location(0,0,0,0,0), item=item("stick"), page=1);
```

**Аргументы:**

| ID       | Тип            | Описание               |
|----------|----------------|------------------------|
| location | Местоположение | Местоположение кафедры |
| item     | Предмет        | Книга для установки    |
| page     | Число          | Страница               |

<h3 id=game_set_player_head>
  <code>world::set_player_head</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить голову игрока\
**Тип:** Действие без значения\
**Описание:** Устанавливает голову игрока на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Головами игроков

**Пример использования:**
```ts
world::set_player_head(location(0,0,0,0,0), "name_or_uuid", "NAME_OR_UUID");

//Или в сухую по ключам

world::set_player_head(location=location(0,0,0,0,0), name_or_uuid="name_or_uuid", receive_type="NAME_OR_UUID");
```

**Аргументы:**

| ID           | Тип                                                                                      | Описание              |
|--------------|------------------------------------------------------------------------------------------|-----------------------|
| location     | Местоположение                                                                           | Местоположение головы |
| name_or_uuid | Текст                                                                                    | Значение              |
| receive_type | Маркер<br/>**NAME_OR_UUID** - Имя или UUID игрока<br/>**VALUE** - Параметр "value" скина | Тип значения          |

<h3 id=game_set_region>
  <code>world::set_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить блоки в регионе\
**Тип:** Действие без значения\
**Описание:** Устанавливает выбранный тип блока на весь выбранный регион.

**Пример использования:**
```ts
world::set_region("minecraft:oak_log[axis=x]", location(0,0,0,0,0), location(0,0,0,0,0));

//Или в сухую по ключам

world::set_region(block="minecraft:oak_log[axis=x]", pos_1=location(0,0,0,0,0), pos_2=location(0,0,0,0,0));
```

**Аргументы:**

| ID    | Тип            | Описание                     |
|-------|----------------|------------------------------|
| block | Блок           | Блок                         |
| pos_1 | Местоположение | Угол региона                 |
| pos_2 | Местоположение | Противоположный угол региона |

<h3 id=game_set_scoreboard_line>
  <code>world::set_scoreboard_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить линию в скорборде\
**Тип:** Действие без значения\
**Описание:** Устанавливает линию в скорборде.

**Пример использования:**
```ts
world::set_scoreboard_line("id", "line", "display", 1, "format_content", "BLANK");

//Или от объекта

"id".set_scoreboard_line("line", "display", 1, "format_content", "BLANK");

//Или в сухую по ключам

world::set_scoreboard_line(id="id", line="line", display="display", score=1, format_content="format_content", format="BLANK");
```

**Аргументы:**

| ID             | Тип                                                                                                    | Описание           |
|----------------|--------------------------------------------------------------------------------------------------------|--------------------|
| id             | Текст                                                                                                  | ID скорборда       |
| line           | Текст                                                                                                  | ID линии           |
| display        | Текст                                                                                                  | Отображаемый текст |
| score          | Число                                                                                                  | Значение           |
| format_content | Текст                                                                                                  | Формат текста      |
| format         | Маркер<br/>**BLANK** - Пустое<br/>**FIXED** - Текстовое<br/>**RESET** - Обычное<br/>**STYLED** - Стиль | Тип формата        |

<h3 id=game_set_scoreboard_line_display>
  <code>world::set_scoreboard_line_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить отображаемый текст линии скорборда\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанной линии скорборда отображаемый текст.

**Пример использования:**
```ts
world::set_scoreboard_line_display("id", "line", "display");

//Или от объекта

"id".set_scoreboard_line_display("line", "display");

//Или в сухую по ключам

world::set_scoreboard_line_display(id="id", line="line", display="display");
```

**Аргументы:**

| ID      | Тип   | Описание           |
|---------|-------|--------------------|
| id      | Текст | ID скорборда       |
| line    | Текст | ID линии           |
| display | Текст | Отображаемый текст |

<h3 id=game_set_scoreboard_line_format>
  <code>world::set_scoreboard_line_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить формат текста линии скорборда\
**Тип:** Действие без значения\
**Описание:** Устанавливает форматирование текста указанной линии скорборда.

**Пример использования:**
```ts
world::set_scoreboard_line_format("id", "line", "format_content", "BLANK");

//Или от объекта

"id".set_scoreboard_line_format("line", "format_content", "BLANK");

//Или в сухую по ключам

world::set_scoreboard_line_format(id="id", line="line", format_content="format_content", format="BLANK");
```

**Аргументы:**

| ID             | Тип                                                                                                    | Описание      |
|----------------|--------------------------------------------------------------------------------------------------------|---------------|
| id             | Текст                                                                                                  | ID скорборда  |
| line           | Текст                                                                                                  | ID линии      |
| format_content | Текст                                                                                                  | Формат текста |
| format         | Маркер<br/>**BLANK** - Пустое<br/>**FIXED** - Текстовое<br/>**RESET** - Обычное<br/>**STYLED** - Стиль | Тип формата   |

<h3 id=game_set_scoreboard_number_format>
  <code>world::set_scoreboard_number_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить форматирование значений скорборда\
**Тип:** Действие без значения\
**Описание:** Устанавливает форматирование значений для скорборда.

**Пример использования:**
```ts
world::set_scoreboard_number_format("id", "format_content", "BLANK");

//Или от объекта

"id".set_scoreboard_number_format("format_content", "BLANK");

//Или в сухую по ключам

world::set_scoreboard_number_format(id="id", format_content="format_content", format="BLANK");
```

**Аргументы:**

| ID             | Тип                                                                                                    | Описание      |
|----------------|--------------------------------------------------------------------------------------------------------|---------------|
| id             | Текст                                                                                                  | ID скорборда  |
| format_content | Текст                                                                                                  | Формат текста |
| format         | Маркер<br/>**BLANK** - Пустое<br/>**FIXED** - Текстовое<br/>**RESET** - Обычное<br/>**STYLED** - Стиль | Тип формата   |

<h3 id=game_set_scoreboard_score>
  <code>world::set_scoreboard_score</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить значение скорборда\
**Тип:** Действие без значения\
**Описание:** Устанавливает значение указанной строке в скорборде.

**Пример использования:**
```ts
world::set_scoreboard_score("id", "text", 1);

//Или в сухую по ключам

world::set_scoreboard_score(id="id", text="text", score=1);
```

**Аргументы:**

| ID    | Тип   | Описание     |
|-------|-------|--------------|
| id    | Текст | ID скорборда |
| text  | Текст | ID линии     |
| score | Число | Счёт         |

<h3 id=game_set_scoreboard_title>
  <code>world::set_scoreboard_title</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Изменить заголовок скорборда\
**Тип:** Действие без значения\
**Описание:** Изменяет заголовок указанного скорборда.

**Пример использования:**
```ts
world::set_scoreboard_title("id", "title");

//Или в сухую по ключам

world::set_scoreboard_title(id="id", title="title");
```

**Аргументы:**

| ID    | Тип   | Описание        |
|-------|-------|-----------------|
| id    | Текст | ID скорборда    |
| title | Текст | Новый заголовок |

<h3 id=game_set_sculk_shrieker_can_summon>
  <code>world::set_sculk_shrieker_can_summon</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить скалк-крикуну возможность призыва\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанному скалк-крикуну возможность призыва Вардена.\
**Работает с:**\
&nbsp;&nbsp;Скалк-крикунами

**Пример использования:**
```ts
world::set_sculk_shrieker_can_summon(location(0,0,0,0,0), "FALSE");

//Или в сухую по ключам

world::set_sculk_shrieker_can_summon(location=location(0,0,0,0,0), can_summon="FALSE");
```

**Аргументы:**

| ID         | Тип                                                                      | Описание                     |
|------------|--------------------------------------------------------------------------|------------------------------|
| location   | Местоположение                                                           | Местоположение скалк-крикуна |
| can_summon | Маркер<br/>**FALSE** - Не может призывать<br/>**TRUE** - Может призывать | Возможность призыва          |

<h3 id=game_set_sculk_shrieker_shrieking>
  <code>world::set_sculk_shrieker_shrieking</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить состояние скалк-крикуну\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанному скалк-крикуну состояние.\
**Работает с:**\
&nbsp;&nbsp;Скалк-крикунами

**Пример использования:**
```ts
world::set_sculk_shrieker_shrieking(location(0,0,0,0,0), "FALSE");

//Или в сухую по ключам

world::set_sculk_shrieker_shrieking(location=location(0,0,0,0,0), shrieking="FALSE");
```

**Аргументы:**

| ID        | Тип                                                        | Описание                     |
|-----------|------------------------------------------------------------|------------------------------|
| location  | Местоположение                                             | Местоположение скалк-крикуна |
| shrieking | Маркер<br/>**FALSE** - Не кричащий<br/>**TRUE** - Кричащий | Состояние                    |

<h3 id=game_set_sculk_shrieker_warning_level>
  <code>world::set_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить скалк-крикуну уровень опасности\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанному скалк-крикуну уровень опасности.\
**Работает с:**\
&nbsp;&nbsp;Скалк-крикунами

**Пример использования:**
```ts
world::set_sculk_shrieker_warning_level(location(0,0,0,0,0), 1);

//Или в сухую по ключам

world::set_sculk_shrieker_warning_level(location=location(0,0,0,0,0), warning_level=1);
```

**Аргументы:**

| ID            | Тип            | Описание                     |
|---------------|----------------|------------------------------|
| location      | Местоположение | Местоположение скалк-крикуна |
| warning_level | Число          | Уровень опасности            |

<h3 id=game_set_sign_text>
  <code>world::set_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить текст таблички\
**Тип:** Действие без значения\
**Описание:** Устанавливает текст таблички на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Табличками

**Пример использования:**
```ts
world::set_sign_text(location(0,0,0,0,0), "text", 1, "ALL");

//Или в сухую по ключам

world::set_sign_text(location=location(0,0,0,0,0), text="text", line=1, side="ALL");
```

**Аргументы:**

| ID       | Тип                                                                     | Описание                |
|----------|-------------------------------------------------------------------------|-------------------------|
| location | Местоположение                                                          | Местоположение таблички |
| text     | Текст                                                                   | Текст для установки     |
| line     | Число                                                                   | Строка                  |
| side     | Маркер<br/>**ALL** - Все<br/>**BACK** - Задняя<br/>**FRONT** - Передняя | Сторона таблички        |

<h3 id=game_set_sign_text_color>
  <code>world::set_sign_text_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет текста таблички\
**Тип:** Действие без значения\
**Описание:** Устанавливает цвет текста таблички на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Табличками

**Пример использования:**
```ts
world::set_sign_text_color(location(0,0,0,0,0), "ALL", "BLACK", "FALSE");

//Или в сухую по ключам

world::set_sign_text_color(location=location(0,0,0,0,0), side="ALL", sign_text_color="BLACK", glowing="FALSE");
```

**Аргументы:**

| ID              | Тип                                                                                                                                                                                                                                                                                                                                                                                                                      | Описание                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| location        | Местоположение                                                                                                                                                                                                                                                                                                                                                                                                           | Местоположение таблички |
| side            | Маркер<br/>**ALL** - Все<br/>**BACK** - Задняя<br/>**FRONT** - Передняя                                                                                                                                                                                                                                                                                                                                                  | Сторона таблички        |
| sign_text_color | Маркер<br/>**BLACK** - Чёрный<br/>**BLUE** - Синий<br/>**BROWN** - Коричневый<br/>**CYAN** - Бирюзовый<br/>**GRAY** - Серый<br/>**GREEN** - Зелёный<br/>**LIGHT_BLUE** - Голубой<br/>**LIGHT_GRAY** - Светло-серый<br/>**LIME** - Лаймовый<br/>**MAGENTA** - Пурпурный<br/>**ORANGE** - Оранжевый<br/>**PINK** - Розовый<br/>**PURPLE** - Фиолетовый<br/>**RED** - Красный<br/>**WHITE** - Белый<br/>**YELLOW** - Жёлтый | Цвет текста             |
| glowing         | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить                                                                                                                                                                                                                                                                                                                                                                 | Свечение текста         |

<h3 id=game_set_sign_waxed>
  <code>world::set_sign_waxed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить вощённость таблички\
**Тип:** Действие без значения\
**Описание:** Устанавливает вощённость таблички на выбранном местоположении.\
**Работает с:**\
&nbsp;&nbsp;Табличками

**Пример использования:**
```ts
world::set_sign_waxed(location(0,0,0,0,0), "FALSE");

//Или в сухую по ключам

world::set_sign_waxed(location=location(0,0,0,0,0), waxed="FALSE");
```

**Аргументы:**

| ID       | Тип                                                      | Описание                |
|----------|----------------------------------------------------------|-------------------------|
| location | Местоположение                                           | Местоположение таблички |
| waxed    | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Вощённость              |

<h3 id=game_set_spawner_entity>
  <code>world::set_spawner_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить сущность в спавнере\
**Тип:** Действие без значения\
**Описание:** Устанавливает спавнеру на выбранном местоположении сущность внутри.\
**Работает с:**\
&nbsp;&nbsp;Спавнерами

**Пример использования:**
```ts
world::set_spawner_entity(location(0,0,0,0,0), item("stick"));

//Или от объекта

location(0,0,0,0,0).set_spawner_entity(item("stick"));

//Или в сухую по ключам

world::set_spawner_entity(location=location(0,0,0,0,0), entity=item("stick"));
```

**Аргументы:**

| ID       | Тип            | Описание                |
|----------|----------------|-------------------------|
| location | Местоположение | Местоположение спавнера |
| entity   | Предмет        | Яйцо призыва сущности   |

<h3 id=game_set_tile_block_custom_tag>
  <code>world::set_tile_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить кастомный тег блоку-сущности\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанный кастомный тег блоку-сущности на местоположении.\
**Работает с:**\
&nbsp;&nbsp;Блоками-сущностями (сундуки, таблички, бочки и т.д.)

**Пример использования:**
```ts
world::set_tile_block_custom_tag(location(0,0,0,0,0), "tag_name", "tag_value");

//Или в сухую по ключам

world::set_tile_block_custom_tag(location=location(0,0,0,0,0), tag_name="tag_name", tag_value="tag_value");
```

**Аргументы:**

| ID        | Тип            | Описание                      |
|-----------|----------------|-------------------------------|
| location  | Местоположение | Местоположение блока-сущности |
| tag_name  | Текст          | Имя кастомного тега           |
| tag_value | Текст          | Значение кастомного тега      |

<h3 id=game_set_vault_displayed_item>
  <code>world::set_vault_displayed_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить отображаемый предмет сокровищнице\
**Тип:** Действие без значения\
**Описание:** Устанавливает отображаемый предмет сокровищнице, находящейся на указанном местоположении.\
**Дополнительная информация:**\
&nbsp;&nbsp;Повторный вызов действия, перезаписывает отображаемый предмет.\
**Работает с:**\
&nbsp;&nbsp;Сокровищницами

**Пример использования:**
```ts
world::set_vault_displayed_item(location(0,0,0,0,0), item("stick"));

//Или в сухую по ключам

world::set_vault_displayed_item(location=location(0,0,0,0,0), item=item("stick"));
```

**Аргументы:**

| ID       | Тип            | Описание                    |
|----------|----------------|-----------------------------|
| location | Местоположение | Местоположение сокровищницы |
| item     | Предмет        | Отображаемый предмет        |

<h3 id=game_set_vault_next_state_update_time>
  <code>world::set_vault_next_state_update_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время до следующего состояния сокровищнице\
**Тип:** Действие без значения\
**Описание:** Устанавливает время до перехода в следующее состоянии сокровищнице, находящейся на указанном местоположении.\
**Дополнительная информация:**\
&nbsp;&nbsp;Необходимо установить точное время, когда сокровищница перейдёт в следующее состояние.\
&nbsp;&nbsp;По умолчанию выбирает максимальное возможное значение.\
**Работает с:**\
&nbsp;&nbsp;Сокровищницами

**Пример использования:**
```ts
world::set_vault_next_state_update_time(location(0,0,0,0,0), 1);

//Или в сухую по ключам

world::set_vault_next_state_update_time(location=location(0,0,0,0,0), time=1);
```

**Аргументы:**

| ID       | Тип            | Описание                    |
|----------|----------------|-----------------------------|
| location | Местоположение | Местоположение сокровищницы |
| time     | Число          | Время                       |

<h3 id=game_set_world_difficulty>
  <code>world::set_world_difficulty</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить сложность мира\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённую сложность в мире.

**Пример использования:**
```ts
world::set_world_difficulty("EASY");

//Или в сухую по ключам

world::set_world_difficulty(difficulty="EASY");
```

**Аргументы:**

| ID         | Тип                                                                                                       | Описание  |
|------------|-----------------------------------------------------------------------------------------------------------|-----------|
| difficulty | Маркер<br/>**EASY** - Лёгкая<br/>**HARD** - Сложная<br/>**NORMAL** - Нормальная<br/>**PEACEFUL** - Мирная | Сложность |

<h3 id=game_set_world_gamerule>
  <code>world::set_gamerule</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить игровое правило мира\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённое игровое правило (gamerule) мира.\
**Дополнительная информация:**\
&nbsp;&nbsp;Оставьте аргумент "Значение"\ пустым, чтобы сбросить его на состояние по умолчанию.

**Пример использования:**
```ts
world::set_gamerule("DISABLE_RAIDS", "value");

//Или в сухую по ключам

world::set_gamerule(gamerule="DISABLE_RAIDS", value="value");
```

**Аргументы:**

| ID       | Тип                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Описание        |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| gamerule | Маркер<br/>**DISABLE_RAIDS** - Отключение рейдов (disableRaids)<br/>**DO_DAYLIGHT_CYCLE** - Смена дня и ночи (doDaylightCycle)<br/>**DO_ENTITY_DROPS** - Выпадение экипировки сущностей (doEntityDrops)<br/>**DO_FIRE_TICK** - Распространение огня (doFireTick)<br/>**DO_IMMEDIATE_RESPAWN** - Мгновенное возрождение (doImmediateRespawn)<br/>**DO_INSOMNIA** - Появление фантомов (doInsomnia)<br/>**DO_MOB_LOOT** - Выпадение добычи с мобов (doMobLoot)<br/>**DO_MOB_SPAWNING** - Появление мобов (doMobSpawning)<br/>**DO_PATROL_SPAWNING** - Патрули Разбойников (doPatrolSpawning)<br/>**DO_TILE_DROPS** - Выпадение блоков (doTileDrops)<br/>**DO_TRADER_SPAWNING** - Странствующие торговцы (doTraderSpawning)<br/>**DO_WEATHER_CYCLE** - Изменения погоды (doWeatherCycle)<br/>**DROWNING_DAMAGE** - Урон от утопления (drowningDamage)<br/>**FALL_DAMAGE** - Урон от падения (fallDamage)<br/>**FIRE_DAMAGE** - Урон от огня (fireDamage)<br/>**FORGIVE_DEAD_PLAYERS** - Прощение умерших игроков (forgiveDeadPlayers)<br/>**KEEP_INVENTORY** - Сохранение инвентаря при смерти (keepInventory)<br/>**MOB_GRIEFING** - Разрушительные действия мобов (mobGriefing)<br/>**PROJECTILES_CAN_BREAK_BLOCKS** - Снаряды могут разрушать блоки (projectilesCanBreakBlocks)<br/>**SHOW_DEATH_MESSAGES** - Сообщения о смерти (showDeathMessages)<br/>**NATURAL_REGENERATION** - Регенерация здоровья (naturalRegeneration)<br/>**UNIVERSAL_ANGER** - Слепая ярость (universalAnger)<br/>**PLAYERS_SLEEPING_PERCENTAGE** - Процент спящих (playersSleepingPercentage)<br/>**REDUCED_DEBUG_INFO** - Малый экран отладки (reducedDebugInfo)<br/>**FREEZE_DAMAGE** - Урон от замерзания (freezeDamage)<br/>**RANDOM_TICK_SPEED** - Частота случайных тиков (randomTickSpeed)<br/>**MAX_ENTITY_CRAMMING** - Предел сущностей в одном блоке (maxEntityCramming)<br/>**SPAWN_RADIUS** - Радиус области возрождения (spawnRadius)<br/>**LAVA_SOURCE_CONVERSION** - Возобновление источников лавы (lavaSourceConversion)<br/>**WATER_SOURCE_CONVERSION** - Возобновление источников воды (waterSourceConversion)<br/>**TNT_EXPLOSION_DROP_DECAY** - Потеря части добычи при взрыве динамита (tntExplosionDropDecay)<br/>**BLOCK_EXPLOSION_DROP_DECAY** - Потеря части добычи при взрыве от взаимодействия с блоком (blockExplosionDropDecay)<br/>**MOB_EXPLOSION_DROP_DECAY** - Потеря части добычи при взрыве моба (mobExplosionDropDecay)<br/>**DO_LIMITED_CRAFTING** - Создание только по рецепту (doLimitedCrafting)<br/>**PLAYERS_NETHER_PORTAL_DEFAULT_DELAY** - Время прохождения портала Незера вне творческого режима (playersNetherPortalDefaultDelay)<br/>**PLAYERS_NETHER_PORTAL_CREATIVE_DELAY** - Время прохождения портала Незера в творческом режиме (playersNetherPortalCreativeDelay)<br/>**SNOW_ACCUMULATION_HEIGHT** - Высота снежного покрова (showAccumulationHeight)<br/>**SPAWN_CHUNK_RADIUS** - Радиус чанков возрождения (shawnChunkRadius)<br/>**DO_WARDEN_SPAWNING** - Появление Хранителей (doWardenSpawning)<br/>**ENDER_PEARLS_VANISH_ON_DEATH** - Исчезновение брошенного эндер-жемчуга при смерти (enderPearlsVanishOnDeath)<br/>**DO_VINES_SPREAD** - Распространение лозы (doVinesSpread)<br/>**ALLOW_FIRE_TICKS_AWAY_FROM_PLAYER** - Обновление огня вдали от игроков<br/>**TNT_EXPLODER** - Активация и взрыв динамита<br/>**LOCATOR_BAR** - Видимость локатора игроков | Игровое правило |
| value    | Текст                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Значение        |

<h3 id=game_set_world_simulation_distance>
  <code>world::set_world_simulation_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дистанцию симуляции мира\
**Тип:** Действие без значения\
**Описание:** Устанавливает дистанцию симуляции чанков для мира.

**Пример использования:**
```ts
world::set_world_simulation_distance(1);

//Или в сухую по ключам

world::set_world_simulation_distance(distance=1);
```

**Аргументы:**

| ID       | Тип   | Описание                            |
|----------|-------|-------------------------------------|
| distance | Число | Дистанция симуляции в чанках (2-32) |

<h3 id=game_set_world_time>
  <code>world::set_world_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время мира\
**Тип:** Действие без значения\
**Описание:** Устанавливает время мира в тиках.

**Пример использования:**
```ts
world::set_world_time(1);

//Или в сухую по ключам

world::set_world_time(time=1);
```

**Аргументы:**

| ID   | Тип   | Описание      |
|------|-------|---------------|
| time | Число | Время в тиках |

<h3 id=game_set_world_weather>
  <code>world::set_world_weather</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить погоду мира\
**Тип:** Действие без значения\
**Описание:** Устанавливает погоду мира на определённое время.\
**Дополнительная информация:**\
&nbsp;&nbsp;По умолчанию, если не указать длительность, погода не будет изменяться.

**Пример использования:**
```ts
world::set_world_weather(1, "CLEAR");

//Или в сухую по ключам

world::set_world_weather(weather_duration=1, weather_type="CLEAR");
```

**Аргументы:**

| ID               | Тип                                                                              | Описание     |
|------------------|----------------------------------------------------------------------------------|--------------|
| weather_duration | Число                                                                            | Длительность |
| weather_type     | Маркер<br/>**CLEAR** - Ясная<br/>**RAINING** - Дождливая<br/>**THUNDER** - Гроза | Тип погоды   |

<h3 id=game_spawn_armor_stand>
  <code>world::spawn_armor_stand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать стойку для брони\
**Тип:** Действие без значения\
**Описание:** Создаёт стойку для брони в указанном местоположении.

**Пример использования:**
```ts
world::spawn_armor_stand(item("stick"), item("stick"), item("stick"), item("stick"), item("stick"), item("stick"), location(0,0,0,0,0), "custom_name", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE");

//Или в сухую по ключам

world::spawn_armor_stand(helmet=item("stick"), chestplate=item("stick"), leggings=item("stick"), boots=item("stick"), right_hand=item("stick"), left_hand=item("stick"), location=location(0,0,0,0,0), custom_name="custom_name", gravity="FALSE", marker="FALSE", small="FALSE", show_arms="FALSE", base_plate="FALSE", invisible="FALSE");
```

**Аргументы:**

| ID          | Тип                                                      | Описание              |
|-------------|----------------------------------------------------------|-----------------------|
| helmet      | Предмет                                                  | Головной убор         |
| chestplate  | Предмет                                                  | Нагрудник             |
| leggings    | Предмет                                                  | Поножи                |
| boots       | Предмет                                                  | Ботинки               |
| right_hand  | Предмет                                                  | Предмет в правой руке |
| left_hand   | Предмет                                                  | Предмет в левой руке  |
| location    | Местоположение                                           | Место создания        |
| custom_name | Текст                                                    | Имя стойки            |
| gravity     | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Установить гравитацию |
| marker      | Маркер<br/>**FALSE** - Выключен<br/>**TRUE** - Включён   | Режим маркера         |
| small       | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Сделать маленьким     |
| show_arms   | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Отображение рук       |
| base_plate  | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Отображение плиты     |
| invisible   | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Невидимость           |

<h3 id=game_spawn_block_display>
  <code>world::spawn_block_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать визуализатор блока\
**Тип:** Действие без значения\
**Описание:** Создаёт визуализатор блока на указанном местоположении.

**Пример использования:**
```ts
world::spawn_block_display(location(0,0,0,0,0), "custom_name", "minecraft:oak_log[axis=x]");

//Или в сухую по ключам

world::spawn_block_display(spawn_location=location(0,0,0,0,0), custom_name="custom_name", block="minecraft:oak_log[axis=x]");
```

**Аргументы:**

| ID             | Тип            | Описание          |
|----------------|----------------|-------------------|
| spawn_location | Местоположение | Место создания    |
| custom_name    | Текст          | Имя               |
| block          | Блок           | Отображаемый блок |

<h3 id=game_spawn_effect_cloud>
  <code>world::spawn_effect_cloud</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать облако туманного зелья\
**Тип:** Действие без значения\
**Описание:** Создаёт облако туманного зелья, которое пропитывает эффектами сущностей в нём.

**Пример использования:**
```ts
world::spawn_effect_cloud(location(0,0,0,0,0), 1, 2, [potion("slow_falling"), potion("slow_falling")], particle("fire"), "custom_name");

//Или в сухую по ключам

world::spawn_effect_cloud(location=location(0,0,0,0,0), duration=1, radius=2, effects=[potion("slow_falling"), potion("slow_falling")], particle=particle("fire"), custom_name="custom_name");
```

**Аргументы:**

| ID          | Тип             | Описание       |
|-------------|-----------------|----------------|
| location    | Местоположение  | Место создания |
| duration    | Число           | Длительность   |
| radius      | Число           | Радиус облака  |
| effects     | Список\[Зелье\] | Эффекты зелья  |
| particle    | Эффект частиц   | Частицы облака |
| custom_name | Текст           | Имя            |

<h3 id=game_spawn_end_crystal>
  <code>world::spawn_end_crystal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать кристалл Энда\
**Тип:** Действие без значения\
**Описание:** Создаёт кристалл Энда в указанном местоположении.

**Пример использования:**
```ts
world::spawn_end_crystal(location(0,0,0,0,0), "custom_name", "FALSE");

//Или в сухую по ключам

world::spawn_end_crystal(location=location(0,0,0,0,0), custom_name="custom_name", show_bottom="FALSE");
```

**Аргументы:**

| ID          | Тип                                          | Описание            |
|-------------|----------------------------------------------|---------------------|
| location    | Местоположение                               | Место создания      |
| custom_name | Текст                                        | Имя                 |
| show_bottom | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да | Создание фундамента |

<h3 id=game_spawn_evoker_fangs>
  <code>world::spawn_evoker_fangs</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать челюсти заклинателя\
**Тип:** Действие без значения\
**Описание:** Создаёт челюсти заклинателя в указанном местоположении.

**Пример использования:**
```ts
world::spawn_evoker_fangs(location(0,0,0,0,0), "custom_name");

//Или в сухую по ключам

world::spawn_evoker_fangs(location=location(0,0,0,0,0), custom_name="custom_name");
```

**Аргументы:**

| ID          | Тип            | Описание       |
|-------------|----------------|----------------|
| location    | Местоположение | Место создания |
| custom_name | Текст          | Имя            |

<h3 id=game_spawn_experience_orb>
  <code>world::spawn_experience_orb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать сферу опыта\
**Тип:** Действие без значения\
**Описание:** Создаёт сферу опыта в указанном местоположении с выбранными параметрами.

**Пример использования:**
```ts
world::spawn_experience_orb(location(0,0,0,0,0), 1, "custom_name");

//Или в сухую по ключам

world::spawn_experience_orb(location=location(0,0,0,0,0), experience_amount=1, custom_name="custom_name");
```

**Аргументы:**

| ID                | Тип            | Описание         |
|-------------------|----------------|------------------|
| location          | Местоположение | Место создания   |
| experience_amount | Число          | Количество опыта |
| custom_name       | Текст          | Имя              |

<h3 id=game_spawn_eye_of_ender>
  <code>world::spawn_eye_of_ender</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать око Энда\
**Тип:** Действие без значения\
**Описание:** Создаёт в указанном местоположении око Энда, которое будет двигаться в сторону цели.

**Пример использования:**
```ts
world::spawn_eye_of_ender(location(0,0,0,0,0), location(0,0,0,0,0), 1, "custom_name", "DROP");

//Или в сухую по ключам

world::spawn_eye_of_ender(location=location(0,0,0,0,0), destination=location(0,0,0,0,0), lifespan=1, custom_name="custom_name", end_of_lifespan="DROP");
```

**Аргументы:**

| ID              | Тип                                                                                             | Описание           |
|-----------------|-------------------------------------------------------------------------------------------------|--------------------|
| location        | Местоположение                                                                                  | Место создания     |
| destination     | Местоположение                                                                                  | Цель               |
| lifespan        | Число                                                                                           | Длительность жизни |
| custom_name     | Текст                                                                                           | Имя                |
| end_of_lifespan | Маркер<br/>**DROP** - Выпасть предметом<br/>**RANDOM** - Случайно<br/>**SHATTER** - Расколоться | По окончанию       |

<h3 id=game_spawn_falling_block>
  <code>world::spawn_falling_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать падающий блок\
**Тип:** Действие без значения\
**Описание:** Создаёт падающий блок в указанном местоположении.

**Пример использования:**
```ts
world::spawn_falling_block("minecraft:oak_log[axis=x]", location(0,0,0,0,0), "name", "FALSE");

//Или в сухую по ключам

world::spawn_falling_block(block="minecraft:oak_log[axis=x]", location=location(0,0,0,0,0), name="name", should_expire="FALSE");
```

**Аргументы:**

| ID            | Тип                                          | Описание          |
|---------------|----------------------------------------------|-------------------|
| block         | Блок                                         | Блок для создания |
| location      | Местоположение                               | Место создания    |
| name          | Текст                                        | Имя               |
| should_expire | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да | Должен исчезать   |

<h3 id=game_spawn_interaction_entity>
  <code>world::spawn_interaction_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать сущность взаимодействия\
**Тип:** Действие без значения\
**Описание:** Создаёт сущность взаимодействия на указанном местоположении.\
**Дополнительная информация:**\
&nbsp;&nbsp;Определяйте взаимодействие при помощи событий атаки и клика по сущности.

**Пример использования:**
```ts
world::spawn_interaction_entity(location(0,0,0,0,0), "custom_name", 1, 2, "FALSE");

//Или в сухую по ключам

world::spawn_interaction_entity(location=location(0,0,0,0,0), custom_name="custom_name", width=1, height=2, responsive="FALSE");
```

**Аргументы:**

| ID          | Тип                                                      | Описание              |
|-------------|----------------------------------------------------------|-----------------------|
| location    | Местоположение                                           | Место создания        |
| custom_name | Текст                                                    | Имя                   |
| width       | Число                                                    | Горизонтальный размер |
| height      | Число                                                    | Вертикальный размер   |
| responsive  | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Отзывчивость          |

<h3 id=game_spawn_item>
  <code>world::spawn_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать предмет\
**Тип:** Действие без значения\
**Описание:** Создаёт предмет в указанном местоположении с выбранными параметрами.

**Пример использования:**
```ts
world::spawn_item(location(0,0,0,0,0), item("stick"), "custom_name", "FALSE", "FALSE", "FALSE");

//Или в сухую по ключам

world::spawn_item(location=location(0,0,0,0,0), item=item("stick"), custom_name="custom_name", can_mob_pickup="FALSE", can_player_pickup="FALSE", apply_motion="FALSE");
```

**Аргументы:**

| ID                | Тип                                          | Описание                              |
|-------------------|----------------------------------------------|---------------------------------------|
| location          | Местоположение                               | Место создания                        |
| item              | Предмет                                      | Предмет для создания                  |
| custom_name       | Текст                                        | Имя                                   |
| can_mob_pickup    | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да | Смогут ли подбирать предмет мобы      |
| can_player_pickup | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да | Смогут ли подбирать предмет игроки    |
| apply_motion      | Маркер<br/>**FALSE** - Нет<br/>**TRUE** - Да | Задать движение предмета при создании |

<h3 id=game_spawn_item_display>
  <code>world::spawn_item_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать визуализатор предмета\
**Тип:** Действие без значения\
**Описание:** Создаёт визуализатор предмета на указанном местоположении.

**Пример использования:**
```ts
world::spawn_item_display(location(0,0,0,0,0), "custom_name", item("stick"));

//Или в сухую по ключам

world::spawn_item_display(spawn_location=location(0,0,0,0,0), custom_name="custom_name", displayed_item=item("stick"));
```

**Аргументы:**

| ID             | Тип            | Описание             |
|----------------|----------------|----------------------|
| spawn_location | Местоположение | Место создания       |
| custom_name    | Текст          | Имя                  |
| displayed_item | Предмет        | Отображаемый предмет |

<h3 id=game_spawn_item_frame>
  <code>world::spawn_item_frame</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать рамку\
**Тип:** Действие без значения\
**Описание:** Создаёт рамку в указанном местоположении.

**Пример использования:**
```ts
world::spawn_item_frame(location(0,0,0,0,0), item("stick"), "NONE", "NORTH", "TRUE", "TRUE", "TRUE");

//Или в сухую по ключам

world::spawn_item_frame(spawn_location=location(0,0,0,0,0), item=item("stick"), rotation="NONE", block_face="NORTH", glowing="TRUE", visible="TRUE", fixed="TRUE");
```

**Аргументы:**

| ID             | Тип                                                                                                                                                                                                                                                                                     | Описание           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| spawn_location | Местоположение                                                                                                                                                                                                                                                                          | Местоположение     |
| item           | Предмет                                                                                                                                                                                                                                                                                 | Предмет в рамке    |
| rotation       | Маркер<br/>**NONE** - Нет<br/>**CLOCKWISE_45** - 45 градусов<br/>**CLOCKWISE** - 90 градусов<br/>**CLOCKWISE_135** - 135 градусов<br/>**FLIPPED** - 180 градусов<br/>**FLIPPED_45** - 225 градусов<br/>**COUNTER_CLOCKWISE** - 270 градусов<br/>**COUNTER_CLOCKWISE_45** - 315 градусов | Поворот предмета   |
| block_face     | Маркер<br/>**NORTH** - Север<br/>**EAST** - Восток<br/>**SOUTH** - Юг<br/>**WEST** - Запад<br/>**UP** - Верх<br/>**DOWN** - Низ                                                                                                                                                         | Сторона блока      |
| glowing        | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет                                                                                                                                                                                                                                            | Свечение           |
| visible        | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет                                                                                                                                                                                                                                            | Видимость          |
| fixed          | Маркер<br/>**TRUE** - Да<br/>**FALSE** - Нет                                                                                                                                                                                                                                            | Защита содержимого |

<h3 id=game_spawn_lightning_bolt>
  <code>world::spawn_lightning_bolt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать молнию\
**Тип:** Действие без значения\
**Описание:** Создаёт молнию в указанном местоположении.

**Пример использования:**
```ts
world::spawn_lightning_bolt(location(0,0,0,0,0));

//Или в сухую по ключам

world::spawn_lightning_bolt(location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип            | Описание       |
|----------|----------------|----------------|
| location | Местоположение | Место создания |

<h3 id=game_spawn_mob>
  <code>world::spawn_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать моба\
**Тип:** Действие без значения\
**Описание:** Создаёт моба в указанном местоположении с выбранными параметрами.

**Пример использования:**
```ts
world::spawn_mob(item("stick"), location(0,0,0,0,0), 1, "custom_name", [potion("slow_falling"), potion("slow_falling")], item("stick"), item("stick"), item("stick"), item("stick"), item("stick"), item("stick"), "FALSE");

//Или в сухую по ключам

world::spawn_mob(mob=item("stick"), location=location(0,0,0,0,0), health=1, custom_name="custom_name", potion_effects=[potion("slow_falling"), potion("slow_falling")], main_hand=item("stick"), helmet=item("stick"), chestplate=item("stick"), leggings=item("stick"), boots=item("stick"), off_hand=item("stick"), natural_equipment="FALSE");
```

**Аргументы:**

| ID                | Тип                                                      | Описание                       |
|-------------------|----------------------------------------------------------|--------------------------------|
| mob               | Предмет                                                  | Тип моба                       |
| location          | Местоположение                                           | Место создания                 |
| health            | Число                                                    | Количество здоровья            |
| custom_name       | Текст                                                    | Имя                            |
| potion_effects    | Список\[Зелье\]                                          | Эффекты                        |
| main_hand         | Предмет                                                  | Предмет в основной руке        |
| helmet            | Предмет                                                  | Головной убор                  |
| chestplate        | Предмет                                                  | Нагрудник                      |
| leggings          | Предмет                                                  | Поножи                         |
| boots             | Предмет                                                  | Ботинки                        |
| off_hand          | Предмет                                                  | Предмет во второстепенной руке |
| natural_equipment | Маркер<br/>**FALSE** - Выключить<br/>**TRUE** - Включить | Стандартное снаряжение         |

<h3 id=game_spawn_painting>
  <code>world::spawn_painting</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать картину\
**Тип:** Действие без значения\
**Описание:** Создаёт картину в указанном местоположении.

**Пример использования:**
```ts
world::spawn_painting(location(0,0,0,0,0), "art", "NORTH");

//Или в сухую по ключам

world::spawn_painting(spawn_location=location(0,0,0,0,0), art="art", block_face="NORTH");
```

**Аргументы:**

| ID             | Тип                                                                                        | Описание         |
|----------------|--------------------------------------------------------------------------------------------|------------------|
| spawn_location | Местоположение                                                                             | Местоположение   |
| art            | Текст                                                                                      | Название картины |
| block_face     | Маркер<br/>**NORTH** - Север<br/>**EAST** - Восток<br/>**SOUTH** - Юг<br/>**WEST** - Запад | Сторона блока    |

<h3 id=game_spawn_primed_tnt>
  <code>world::spawn_primed_tnt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать подожжённый динамит\
**Тип:** Действие без значения\
**Описание:** Создаёт подожжённый динамит в указанном местоположении.

**Пример использования:**
```ts
world::spawn_primed_tnt(location(0,0,0,0,0), 1, 2, "custom_name", "minecraft:oak_log[axis=x]");

//Или в сухую по ключам

world::spawn_primed_tnt(location=location(0,0,0,0,0), tnt_power=1, fuse_duration=2, custom_name="custom_name", block="minecraft:oak_log[axis=x]");
```

**Аргументы:**

| ID            | Тип            | Описание                      |
|---------------|----------------|-------------------------------|
| location      | Местоположение | Место создания                |
| tnt_power     | Число          | Мощность динамита (от 0 до 4) |
| fuse_duration | Число          | Время задержки взрыва         |
| custom_name   | Текст          | Имя                           |
| block         | Блок           | Блок для маскировки           |

<h3 id=game_spawn_shulker_bullet>
  <code>world::spawn_shulker_bullet</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать снаряд Шалкера\
**Тип:** Действие без значения\
**Описание:** Создаёт снаряд Шалкера в указанном местоположении.

**Пример использования:**
```ts
world::spawn_shulker_bullet(location(0,0,0,0,0), "custom_name");

//Или в сухую по ключам

world::spawn_shulker_bullet(location=location(0,0,0,0,0), custom_name="custom_name");
```

**Аргументы:**

| ID          | Тип            | Описание       |
|-------------|----------------|----------------|
| location    | Местоположение | Место создания |
| custom_name | Текст          | Имя            |

<h3 id=game_spawn_text_display>
  <code>world::spawn_text_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать визуализатор текста\
**Тип:** Действие без значения\
**Описание:** Создаёт визуализатор текста на указанном местоположении.

**Пример использования:**
```ts
world::spawn_text_display(location(0,0,0,0,0), "custom_name", ["displayed_text", "displayed_text"], "CONCATENATION");

//Или в сухую по ключам

world::spawn_text_display(spawn_location=location(0,0,0,0,0), custom_name="custom_name", displayed_text=["displayed_text", "displayed_text"], merging_mode="CONCATENATION");
```

**Аргументы:**

| ID             | Тип                                                                                                                           | Описание           |
|----------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------|
| spawn_location | Местоположение                                                                                                                | Место создания     |
| custom_name    | Текст                                                                                                                         | Имя                |
| displayed_text | Список\[Текст\]                                                                                                               | Отображаемый текст |
| merging_mode   | Маркер<br/>**CONCATENATION** - Объединение<br/>**SEPARATE_LINES** - Разделение на строки<br/>**SPACES** - Разделение пробелом | Объединение текста |

<h3 id=game_spawn_vehicle>
  <code>world::spawn_vehicle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать транспорт\
**Тип:** Действие без значения\
**Описание:** Создаёт транспорт в указанном местоположении с выбранными параметрами.

**Пример использования:**
```ts
world::spawn_vehicle(item("stick"), location(0,0,0,0,0), "custom_name");

//Или в сухую по ключам

world::spawn_vehicle(vehicle=item("stick"), location=location(0,0,0,0,0), custom_name="custom_name");
```

**Аргументы:**

| ID          | Тип            | Описание       |
|-------------|----------------|----------------|
| vehicle     | Предмет        | Тип транспорта |
| location    | Местоположение | Место создания |
| custom_name | Текст          | Имя            |

<h3 id=game_uncancel_event>
  <code>world::uncancel_event</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Возврат события\
**Тип:** Действие без значения\
**Описание:** Возвращает отмену события, которое вызвало этот код.

**Пример использования:**
```ts
world::uncancel_event();
```

<h3 id=game_update_block>
  <code>world::update_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Обновить смежные блоки\
**Тип:** Действие без значения\
**Описание:** Обновляет соседние блоки на указанном местоположении, если блок на местоположении не является воздухом. Сам по себе блок на местоположении не обновляется, но может обновиться от соседних.

**Пример использования:**
```ts
world::update_block(location(0,0,0,0,0));

//Или в сухую по ключам

world::update_block(location=location(0,0,0,0,0));
```

**Аргументы:**

| ID       | Тип            | Описание       |
|----------|----------------|----------------|
| location | Местоположение | Местоположение |

<h3 id=if_game_block_equals>
  <code>world::block_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Блок равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, является ли блок в определённом местоположении определённым типом блока.

**Пример использования:**
```ts
if(world::block_equals(["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], location(0,0,0,0,0))){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::block_equals(blocks=["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], location=location(0,0,0,0,0))){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID       | Тип            | Описание               |
|----------|----------------|------------------------|
| blocks   | Список\[Блок\] | Тип блока для проверки |
| location | Местоположение | Местоположение блока   |

<h3 id=if_game_block_powered>
  <code>world::block_powered</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Блок запитан редстоуном\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, запитан ли блок в определённом местоположении редстоуном.

**Пример использования:**
```ts
if(world::block_powered([location(0,0,0,0,0), location(0,0,0,0,0)], "DIRECT")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::block_powered(locations=[location(0,0,0,0,0), location(0,0,0,0,0)], power_mode="DIRECT")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID         | Тип                                                                                | Описание                   |
|------------|------------------------------------------------------------------------------------|----------------------------|
| locations  | Список\[Местоположение\]                                                           | Местоположение блока       |
| power_mode | Маркер<br/>**DIRECT** - Прямое запитывание<br/>**INDIRECT** - Непрямое запитывание | Вид запитывания редстоуном |

<h3 id=if_game_chunk_is_loaded>
  <code>world::chunk_is_loaded</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Чанк загружен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, загружен ли чанк на местоположении.

**Пример использования:**
```ts
if(world::chunk_is_loaded(location(0,0,0,0,0))){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::chunk_is_loaded(location=location(0,0,0,0,0))){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID       | Тип            | Описание             |
|----------|----------------|----------------------|
| location | Местоположение | Местоположение чанка |

<h3 id=if_game_container_has>
  <code>world::container_has</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Контейнер имеет предмет\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли контейнер в определённом местоположении определённые предметы в его инвентаре.

**Пример использования:**
```ts
if(world::container_has([item("stick"), item("stick")], location(0,0,0,0,0), "ALL", "EXACTLY")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::container_has(items=[item("stick"), item("stick")], location=location(0,0,0,0,0), check_mode="ALL", comparison_mode="EXACTLY")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID              | Тип                                                                                                                                                                                                                         | Описание                  |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| items           | Список\[Предмет\]                                                                                                                                                                                                           | Предметы для проверки     |
| location        | Местоположение                                                                                                                                                                                                              | Местоположение контейнера |
| check_mode      | Маркер<br/>**ALL** - Все предметы<br/>**ANY** - Любые предметы                                                                                                                                                              | Вид сравнения             |
| comparison_mode | Маркер<br/>**EXACTLY** - Полное сравнение<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Игнорировать количество и прочность<br/>**IGNORE_STACK_SIZE** - Игнорировать только количество<br/>**TYPE_ONLY** - Только тип предмета | Режим сравнения           |

<h3 id=if_game_container_has_room_for_item>
  <code>world::container_has_room_for_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Контейнер имеет место для предметов\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли контейнер в определённом местоположении место для предметов в его инвентаре.

**Пример использования:**
```ts
if(world::container_has_room_for_item([item("stick"), item("stick")], location(0,0,0,0,0), "ALL")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::container_has_room_for_item(items=[item("stick"), item("stick")], location=location(0,0,0,0,0), check_mode="ALL")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID         | Тип                                                            | Описание                  |
|------------|----------------------------------------------------------------|---------------------------|
| items      | Список\[Предмет\]                                              | Предметы для проверки     |
| location   | Местоположение                                                 | Местоположение контейнера |
| check_mode | Маркер<br/>**ALL** - Все предметы<br/>**ANY** - Любые предметы | Вид сравнения             |

<h3 id=if_game_damage_cause_equals>
  <code>world::damage_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Источник урона события равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли источник урона события выбранному.

**Пример использования:**
```ts
if(world::damage_cause_equals("BLOCK_EXPLOSION")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::damage_cause_equals(cause="BLOCK_EXPLOSION")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID    | Тип                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Описание       |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| cause | Маркер<br/>**BLOCK_EXPLOSION** - Взрыв блока<br/>**CAMPFIRE** - Костёр<br/>**CONTACT** - Контакт<br/>**CRAMMING** - Толпёжка<br/>**CUSTOM** - Кастомный<br/>**DRAGON_BREATH** - Дыхание дракона<br/>**DROWNING** - Утопление<br/>**DRYOUT** - Высыхание<br/>**ENTITY_ATTACK** - Атака сущности<br/>**ENTITY_EXPLOSION** - Взрыв сущности<br/>**ENTITY_SWEEP_ATTACK** - Обширная атака сущности<br/>**FALL** - Падение<br/>**FALLING_BLOCK** - Падающий блок<br/>**FIRE** - Прямой огонь<br/>**FIRE_TICK** - Горение<br/>**FLY_INTO_WALL** - Кинетическая энергия<br/>**FREEZE** - Замерзание<br/>**HOT_FLOOR** - Магма<br/>**KILL** - Команда<br/>**LAVA** - Лава<br/>**LIGHTNING** - Молния<br/>**MAGIC** - Магия<br/>**MELTING** - Таяние<br/>**POISON** - Отравление<br/>**PROJECTILE** - Снаряд<br/>**SONIC_BOOM** - Взрывная волна<br/>**STARVATION** - Голод<br/>**SUFFOCATION** - Удушение<br/>**SUICIDE** - Суицид (грех)<br/>**THORNS** - Шипы<br/>**VOID** - Бездна<br/>**WITHER** - Иссушение<br/>**WORLD_BORDER** - Граница мира | Источник урона |

<h3 id=if_game_dummy>
  <code>world::is_dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** ...\
**Тип:** Действие, проверяющее условие\
**Описание:** ...

**Пример использования:**
```ts
if(world::is_dummy()){
    player::message("Условие верно");
}
```

<h3 id=if_game_event_attack_is_critical>
  <code>world::event_attack_is_critical</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Атака была критической\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, была ли атака в событии критической.

**Пример использования:**
```ts
if(world::event_attack_is_critical()){
    player::message("Условие верно");
}
```

<h3 id=if_game_event_block_equals>
  <code>world::event_block_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Блок события равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли блок текущего события определённому блоку.

**Пример использования:**
```ts
if(world::event_block_equals(["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], [location(0,0,0,0,0), location(0,0,0,0,0)])){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::event_block_equals(blocks=["minecraft:oak_log[axis=x]", "minecraft:oak_log[axis=x]"], locations=[location(0,0,0,0,0), location(0,0,0,0,0)])){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID        | Тип                      | Описание                           |
|-----------|--------------------------|------------------------------------|
| blocks    | Список\[Блок\]           | Типы блоков для проверки           |
| locations | Список\[Местоположение\] | Местоположения блоков для проверки |

<h3 id=if_game_event_has_input>
  <code>world::event_has_input</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Клавиша передвижения равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, является ли клавиша передвижения из события, выбранной клавишей.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок меняет нажатые клавиши передвижения"\
&nbsp;&nbsp;Событием "Игрок передвигается на транспорте"\
&nbsp;&nbsp;Событием "Игрок прыгает на транспорте"

**Пример использования:**
```ts
if(world::event_has_input("FORWARD")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::event_has_input(input_type="FORWARD")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID         | Тип                                                                                                                                                                         | Описание             |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| input_type | Маркер<br/>**FORWARD** - Вперёд<br/>**BACKWARDS** - Назад<br/>**LEFT** - Влево<br/>**RIGHT** - Вправо<br/>**JUMP** - Прыжок<br/>**SNEAK** - Приседание<br/>**SPRINT** - Бег | Клавиша передвижения |

<h3 id=if_game_event_is_canceled>
  <code>world::event_is_canceled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Событие отменено\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, отменено ли событие.

**Пример использования:**
```ts
if(world::event_is_canceled()){
    player::message("Условие верно");
}
```

<h3 id=if_game_event_item_equals>
  <code>world::event_item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет события равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли предмет текущего события определённому предмету.

**Пример использования:**
```ts
if(world::event_item_equals([item("stick"), item("stick")], "EXACTLY")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::event_item_equals(items=[item("stick"), item("stick")], comparison_mode="EXACTLY")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID              | Тип                                                                                                                                                                                                                         | Описание              |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| items           | Список\[Предмет\]                                                                                                                                                                                                           | Предметы для проверки |
| comparison_mode | Маркер<br/>**EXACTLY** - Полное сравнение<br/>**IGNORE_DURABILITY_AND_STACK_SIZE** - Игнорировать количество и прочность<br/>**IGNORE_STACK_SIZE** - Игнорировать только количество<br/>**TYPE_ONLY** - Только тип предмета | Режим сравнения       |

<h3 id=if_game_has_player>
  <code>world::has_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Игрок в игре\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли определённый игрок в игре.

**Пример использования:**
```ts
if(world::has_player(["names_or_uuids", "names_or_uuids"])){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::has_player(names_or_uuids=["names_or_uuids", "names_or_uuids"])){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID             | Тип             | Описание            |
|----------------|-----------------|---------------------|
| names_or_uuids | Список\[Текст\] | Ник игрока или UUID |

<h3 id=if_game_heal_cause_equals>
  <code>world::heal_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Источник исцеления равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли источник исцеления выбранному.

**Пример использования:**
```ts
if(world::heal_cause_equals("CUSTOM")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::heal_cause_equals(heal_cause="CUSTOM")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID         | Тип                                                                                                                                                                                                                                                                                                                                                                                                   | Описание           |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| heal_cause | Маркер<br/>**CUSTOM** - Кастомный<br/>**EATING** - От употребления пищи<br/>**ENDER_CRYSTAL** - От кристалла Энда<br/>**MAGIC** - От зелья или заклинания<br/>**MAGIC_REGEN** - Со временем от зелья или заклинания<br/>**REGEN** - Исцеление в Мирном режиме<br/>**SATIATED** - Исцеление при утолённом голоде<br/>**WITHER** - От эффекта Иссушение<br/>**WITHER_SPAWN** - При появлении Иссушителя | Источник исцеления |

<h3 id=if_game_ignite_cause_equals>
  <code>world::ignite_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Источник огня равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли источник огня выбранному.

**Пример использования:**
```ts
if(world::ignite_cause_equals("ARROW")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::ignite_cause_equals(cause="ARROW")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID    | Тип                                                                                                                                                                                                                                                                                                            | Описание      |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| cause | Маркер<br/>**ARROW** - Стрела<br/>**ENDER_CRYSTAL** - Кристалл Энда<br/>**EXPLOSION** - Взрыв<br/>**FALL** - Падение<br/>**FIREBALL** - Огненный заряд<br/>**FLINT_AND_STEEL** - Зажигалка<br/>**LAVA** - Лава<br/>**LIGHTNING** - Молния<br/>**SPREAD** - Распространение огня<br/>**SUFFOCATION** - Удушение | Источник огня |

<h3 id=if_game_instrument_equals>
  <code>world::instrument_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Инструмент равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли инструмент в событии выбранному.

**Пример использования:**
```ts
if(world::instrument_equals("BANJO")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::instrument_equals(instrument="BANJO")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID         | Тип                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Описание   |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| instrument | Маркер<br/>**BANJO** - Банджо<br/>**BASS_DRUM** - Бас-барабан<br/>**BASS_GUITAR** - Бас-гитара<br/>**BELL** - Колокол<br/>**BIT** - Бит<br/>**CHIME** - Чаймс<br/>**COW_BELL** - Ковбелл<br/>**CREEPER** - Крипер<br/>**CUSTOM_HEAD** - Кастомная голова<br/>**DIDGERIDOO** - Диджериду<br/>**DRAGON** - Эндер-дракон<br/>**FLUTE** - Флейта<br/>**GUITAR** - Гитара<br/>**IRON_XYLOPHONE** - Железный ксилофон<br/>**PIANO** - Пианино<br/>**PIGLIN** - Пиглин<br/>**PLING** - Плинг<br/>**SKELETON** - Скелет<br/>**SNARE_DRUM** - Малый барабан<br/>**STICKS** - Клаве<br/>**WITHER_SKELETON** - Визер-скелет<br/>**XYLOPHONE** - Ксилофон<br/>**ZOMBIE** - Зомби | Инструмент |

<h3 id=if_game_location_in_block>
  <code>world::location_in_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Если местоположение внутри блока\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли указанное местоположение внутри блока.

**Пример использования:**
```ts
if(world::location_in_block(location(0,0,0,0,0))){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::location_in_block(location=location(0,0,0,0,0))){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID       | Тип            | Описание                    |
|----------|----------------|-----------------------------|
| location | Местоположение | Местоположение для проверки |

<h3 id=if_game_sign_contains>
  <code>world::sign_contains</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Табличка содержит текст\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, содержит ли табличка в определённом местоположении определённый текст.

**Пример использования:**
```ts
if(world::sign_contains(location(0,0,0,0,0), ["texts", "texts"], "ANY", "ALL", "ALL")){
    player::message("Условие верно");
}

//Или в сухую по ключам

if(world::sign_contains(location=location(0,0,0,0,0), texts=["texts", "texts"], check_side="ANY", check_mode="ALL", lines="ALL")){
    player::message("Условие верно");
}
```

**Аргументы:**

| ID         | Тип                                                                                                                                                                                                                                                                       | Описание                |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| location   | Местоположение                                                                                                                                                                                                                                                            | Местоположение таблички |
| texts      | Список\[Текст\]                                                                                                                                                                                                                                                           | Текст для проверки      |
| check_side | Маркер<br/>**ANY** - Любая<br/>**BACK** - Задняя<br/>**FRONT** - Передняя                                                                                                                                                                                                 | Сторона таблички        |
| check_mode | Маркер<br/>**ALL** - creative_plus.action.if_game_sign_contains.argument.check_mode.enum.all.name<br/>**ANY** - creative_plus.action.if_game_sign_contains.argument.check_mode.enum.any.name<br/>**CONTAINS** - Сравнение по содержанию<br/>**EQUALS** - Полное сравнение | Вид сравнения           |
| lines      | Маркер<br/>**ALL** - Все строки<br/>**ANY** - Любая строка<br/>**FIRST** - 1 строка<br/>**FOURTH** - 4 строка<br/>**SECOND** - 2 строка<br/>**THIRD** - 3 строка                                                                                                          | Строки для сравнения    |

