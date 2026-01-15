<h2 id=select>
  <code>select</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

<h3 id=select_add_all_entities>
  <code>select::add_all_entities</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить всех сущностей\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку всех сущностей из мира.

**Пример использования:**
```ts
select::add_all_entities();
```

<h3 id=select_add_all_mobs>
  <code>select::add_all_mobs</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить всех мобов\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку всех мобов из мира.

**Пример использования:**
```ts
select::add_all_mobs();
```

<h3 id=select_add_all_players>
  <code>select::add_all_players</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить всех игроков\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку всех игроков из мира.

**Пример использования:**
```ts
select::add_all_players();
```

<h3 id=select_add_entity_by_conditional>
  <code>select::add_entity_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить сущность по условию\
**Тип:** Действие без значения\
**Описание:** Добавляет сущностей, если выполняется указанное условие.

**Пример использования:**
```ts
select::add_entity_by_conditional(a1.exists());
```

<h3 id=select_add_entity_by_name>
  <code>select::add_entity_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить сущность по имени/UUID\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку сущность с указанным именем/UUID.

**Пример использования:**
```ts
select::add_entity_by_name(["name_or_uuid", "name_or_uuid"]);

//Или в сухую по ключам

select::add_entity_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Аргументы:**

| ID           | Тип             | Описание                                                          |
|--------------|-----------------|-------------------------------------------------------------------|
| name_or_uuid | Список\[Текст\] | Имя или UUID сущности<br>Аргумент поддерживает разложение списков |

<h3 id=select_add_event_target>
  <code>select::add_event_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить цель события\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку цель, которая запустила событие.

**Пример использования:**
```ts
select::add_event_target("DAMAGER");

//Или в сухую по ключам

select::add_event_target(selection_type="DAMAGER");
```

**Аргументы:**

| ID             | Тип                                                                                                                                                                             | Описание         |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| selection_type | Маркер<br/>**DAMAGER** - Атакующий<br/>**DEFAULT** - По умолчанию<br/>**KILLER** - Убийца<br/>**PROJECTILE** - Снаряд стрелка<br/>**SHOOTER** - Стрелок<br/>**VICTIM** - Жертва | Тип цели выборки |

<h3 id=select_add_last_entity>
  <code>select::add_last_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить последнюю появившуюся сущность\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку последнюю появившуюся сущность из мира.

**Пример использования:**
```ts
select::add_last_entity();
```

<h3 id=select_add_last_mob>
  <code>select::add_last_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить последнего появившегося моба\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку последнего появившегося моба из мира.

**Пример использования:**
```ts
select::add_last_mob();
```

<h3 id=select_add_mob_by_name>
  <code>select::add_mob_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить моба по имени/UUID\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку моба с указанным именем/UUID.

**Пример использования:**
```ts
select::add_mob_by_name(["name_or_uuid", "name_or_uuid"]);

//Или в сухую по ключам

select::add_mob_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Аргументы:**

| ID           | Тип             | Описание                                                      |
|--------------|-----------------|---------------------------------------------------------------|
| name_or_uuid | Список\[Текст\] | Имя или UUID моба<br>Аргумент поддерживает разложение списков |

<h3 id=select_add_player_by_conditional>
  <code>select::add_player_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить игрока по условию\
**Тип:** Действие без значения\
**Описание:** Добавляет игроков, если выполняется указанное условие.

**Пример использования:**
```ts
select::add_player_by_conditional(a1.exists());
```

<h3 id=select_add_player_by_name>
  <code>select::add_player_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить игрока по имени/UUID\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку игрока с указанным именем/UUID.

**Пример использования:**
```ts
select::add_player_by_name(["name_or_uuid", "name_or_uuid"]);

//Или в сухую по ключам

select::add_player_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Аргументы:**

| ID           | Тип             | Описание                                                        |
|--------------|-----------------|-----------------------------------------------------------------|
| name_or_uuid | Список\[Текст\] | Имя или UUID игрока<br>Аргумент поддерживает разложение списков |

<h3 id=select_add_random_entity>
  <code>select::add_random_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить случайную сущность\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку случайную сущность из мира.

**Пример использования:**
```ts
select::add_random_entity();
```

<h3 id=select_add_random_mob>
  <code>select::add_random_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить случайного моба\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку случайного моба из мира.

**Пример использования:**
```ts
select::add_random_mob();
```

<h3 id=select_add_random_player>
  <code>select::add_random_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить случайного игрока\
**Тип:** Действие без значения\
**Описание:** Добавляет в выборку случайного игрока из мира.

**Пример использования:**
```ts
select::add_random_player();
```

<h3 id=select_all_entities>
  <code>select::all_entities</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать всех сущностей\
**Тип:** Действие без значения\
**Описание:** Выбирает всех сущностей в мире.

**Пример использования:**
```ts
select::all_entities();
```

<h3 id=select_all_mobs>
  <code>select::all_mobs</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать всех мобов\
**Тип:** Действие без значения\
**Описание:** Выбирает всех мобов в мире.

**Пример использования:**
```ts
select::all_mobs();
```

<h3 id=select_all_players>
  <code>select::all_players</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать всех игроков\
**Тип:** Действие без значения\
**Описание:** Выбирает всех игроков в мире.

**Пример использования:**
```ts
select::all_players();
```

<h3 id=select_dummy>
  <code>select::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** ...\
**Тип:** Действие без значения\
**Описание:** ...

**Пример использования:**
```ts
select::dummy();
```

<h3 id=select_entity_by_conditional>
  <code>select::entity_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать сущность по условию\
**Тип:** Действие без значения\
**Описание:** Выбирает сущностей, если выполняется указанное условие.

**Пример использования:**
```ts
select::entity_by_conditional(a1.exists());
```

<h3 id=select_entity_by_name>
  <code>select::entity_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать сущность по имени\
**Тип:** Действие без значения\
**Описание:** Выбирает сущность или сущностей по имени или UUID.

**Пример использования:**
```ts
select::entity_by_name(["name_or_uuid", "name_or_uuid"]);

//Или в сухую по ключам

select::entity_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Аргументы:**

| ID           | Тип             | Описание                                                      |
|--------------|-----------------|---------------------------------------------------------------|
| name_or_uuid | Список\[Текст\] | Имя или UUID цели<br>Аргумент поддерживает разложение списков |

<h3 id=select_event_target>
  <code>select::event_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать цель события\
**Тип:** Действие без значения\
**Описание:** Выбирает цель, которая запустила событие.

**Пример использования:**
```ts
select::event_target("DAMAGER");

//Или в сухую по ключам

select::event_target(selection_type="DAMAGER");
```

**Аргументы:**

| ID             | Тип                                                                                                                                                                             | Описание         |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| selection_type | Маркер<br/>**DAMAGER** - Атакующий<br/>**DEFAULT** - По умолчанию<br/>**KILLER** - Убийца<br/>**PROJECTILE** - Снаряд стрелка<br/>**SHOOTER** - Стрелок<br/>**VICTIM** - Жертва | Тип цели выборки |

<h3 id=select_filter_by_conditional>
  <code>select::filter_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отфильтровать выборку по условию\
**Тип:** Действие без значения\
**Описание:** Оставляет в выборке те цели, которые подходят под выбранное условие.

**Пример использования:**
```ts
select::filter_by_conditional(a1.exists());
```

<h3 id=select_filter_by_distance>
  <code>select::filter_by_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отфильтровать выборку по расстоянию\
**Тип:** Действие без значения\
**Описание:** Оставляет в выборке те цели, которые находятся на расстоянии до местоположения.

**Пример использования:**
```ts
select::filter_by_distance(location(0,0,0,0,0), 1, "FALSE", "FARTHEST");

//Или в сухую по ключам

select::filter_by_distance(location=location(0,0,0,0,0), selection_size=1, ignore_y_axis="FALSE", compare_mode="FARTHEST");
```

**Аргументы:**

| ID             | Тип                                                                     | Описание              |
|----------------|-------------------------------------------------------------------------|-----------------------|
| location       | Местоположение                                                          | Местоположение центра |
| selection_size | Число                                                                   | Количество целей      |
| ignore_y_axis  | Маркер<br/>**FALSE** - Не игнорировать<br/>**TRUE** - Игнорировать      | Игнорировать ось Y    |
| compare_mode   | Маркер<br/>**FARTHEST** - Дальние цели<br/>**NEAREST** - Ближайшие цели | Тип сравнения         |

<h3 id=select_filter_by_raycast>
  <code>select::filter_by_raycast</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Фильтр рейкастом\
**Тип:** Действие без значения\
**Описание:** Оставляет в выборке только те цели, в которые попал запущенный луч. Ширина луча работает только на сущностей (увеличивает или уменьшает хитбоксы существ).

**Пример использования:**
```ts
select::filter_by_raycast(`variable`, location(0,0,0,0,0), 1, 2, 3, "FALSE", "FALSE", "ALWAYS");

//Или в сухую по ключам

select::filter_by_raycast(variable=`variable`, origin=location(0,0,0,0,0), max_distance=1, ray_size=2, selection_size=3, consider_blocks="FALSE", ignore_passable_blocks="FALSE", fluid_collision_mode="ALWAYS");
```

**Аргументы:**

| ID                     | Тип                                                                                                                                     | Описание                          |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| variable               | Переменная                                                                                                                              | Точка конца луча                  |
| origin                 | Местоположение                                                                                                                          | Начало луча                       |
| max_distance           | Число                                                                                                                                   | Длина луча                        |
| ray_size               | Число                                                                                                                                   | Ширина луча                       |
| selection_size         | Число                                                                                                                                   | Максимальное количество сущностей |
| consider_blocks        | Маркер<br/>**FALSE** - Не учитывать<br/>**TRUE** - Учитывать                                                                            | Учитывать блоки                   |
| ignore_passable_blocks | Маркер<br/>**FALSE** - Не игнорировать<br/>**TRUE** - Игнорировать                                                                      | Игнорировать проходимые блоки     |
| fluid_collision_mode   | Маркер<br/>**ALWAYS** - Не игнорировать<br/>**NEVER** - Полностью игнорировать<br/>**SOURCE_ONLY** - Учитывать только источник жидкости | Игнорировать жидкость             |

<h3 id=select_filter_randomly>
  <code>select::filter_randomly</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отфильтровать выборку случайно\
**Тип:** Действие без значения\
**Описание:** Оставляет в выборке указанное количество случайных целей.

**Пример использования:**
```ts
select::filter_randomly(1);

//Или в сухую по ключам

select::filter_randomly(size=1);
```

**Аргументы:**

| ID   | Тип   | Описание         |
|------|-------|------------------|
| size | Число | Количество целей |

<h3 id=select_invert>
  <code>select::invert</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Инвертировать выборку\
**Тип:** Действие без значения\
**Описание:** Создаёт новую выборку, в которую входят все существа, кроме выбранных.

**Пример использования:**
```ts
select::invert();
```

<h3 id=select_last_entity>
  <code>select::last_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать последнюю появившуюся сущность\
**Тип:** Действие без значения\
**Описание:** Выбирает последнюю появившуюся сущность в мире.

**Пример использования:**
```ts
select::last_entity();
```

<h3 id=select_last_mob>
  <code>select::last_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать последнего появившегося моба\
**Тип:** Действие без значения\
**Описание:** Выбирает последнего появившегося моба в мире.

**Пример использования:**
```ts
select::last_mob();
```

<h3 id=select_mob_by_name>
  <code>select::mob_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать моба по имени\
**Тип:** Действие без значения\
**Описание:** Выбирает моба или мобов по имени или UUID.

**Пример использования:**
```ts
select::mob_by_name(["name_or_uuid", "name_or_uuid"]);

//Или в сухую по ключам

select::mob_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Аргументы:**

| ID           | Тип             | Описание                                                      |
|--------------|-----------------|---------------------------------------------------------------|
| name_or_uuid | Список\[Текст\] | Имя или UUID цели<br>Аргумент поддерживает разложение списков |

<h3 id=select_player_by_conditional>
  <code>select::player_by_conditional</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать игрока по условию\
**Тип:** Действие без значения\
**Описание:** Выбирает игроков, если выполняется указанное условие.

**Пример использования:**
```ts
select::player_by_conditional(a1.exists());
```

<h3 id=select_player_by_name>
  <code>select::player_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать игрока по имени\
**Тип:** Действие без значения\
**Описание:** Выбирает игрока или игроков по имени или UUID.

**Пример использования:**
```ts
select::player_by_name(["name_or_uuid", "name_or_uuid"]);

//Или в сухую по ключам

select::player_by_name(name_or_uuid=["name_or_uuid", "name_or_uuid"]);
```

**Аргументы:**

| ID           | Тип             | Описание                                                      |
|--------------|-----------------|---------------------------------------------------------------|
| name_or_uuid | Список\[Текст\] | Имя или UUID цели<br>Аргумент поддерживает разложение списков |

<h3 id=select_random_entity>
  <code>select::random_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать случайную сущность\
**Тип:** Действие без значения\
**Описание:** Выбирает случайную сущность в мире.

**Пример использования:**
```ts
select::random_entity();
```

<h3 id=select_random_mob>
  <code>select::random_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать случайного моба\
**Тип:** Действие без значения\
**Описание:** Выбирает случайного моба в мире.

**Пример использования:**
```ts
select::random_mob();
```

<h3 id=select_random_player>
  <code>select::random_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выбрать случайного игрока\
**Тип:** Действие без значения\
**Описание:** Выбирает случайного игрока в мире.

**Пример использования:**
```ts
select::random_player();
```

<h3 id=select_reset>
  <code>select::reset</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сбросить выборку\
**Тип:** Действие без значения\
**Описание:** Сбрасывает всю выборку.

**Пример использования:**
```ts
select::reset();
```

