<h3 id=game_block_growth>
  <code>world::block_growth</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стадию роста блока\
**Тип:** Действие без значения\
**Описание:** Устанавливает стадию роста для блока на выбранном местоположении.

**Пример использования:** 
```ts
world::block_growth(location(0,0,0,0,0),1,"STAGE_NUMBER");
```

<h3 id=game_bloom_skulk_catalyst>
  <code>world::bloom_skulk_catalyst</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Продлить скалк-заражение к местоположению\
**Тип:** Действие без значения\
**Описание:** Продлевает скалк-заражение к местоположению.
**Работает с:**\
&nbsp;&nbsp;Скалк-каталистами

**Пример использования:** 
```ts
world::bloom_skulk_catalyst(location(0,0,0,0,0),location(0,0,0,0,0),1);
```

<h3 id=game_bone_meal_block>
  <code>world::bone_meal_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удобрить блок\
**Тип:** Действие без значения\
**Описание:** Удобряет блок на выбранном местоположении.

**Пример использования:** 
```ts
world::bone_meal_block(location(0,0,0,0,0),1);
```

<h3 id=game_break_block>
  <code>world::break_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сломать блок\
**Тип:** Действие без значения\
**Описание:** Разрушает блоки на указанных местоположениях, как если бы это сделал игрок в режиме выживания нужным инструментом.

**Пример использования:** 
```ts
world::break_block([location(0,0,0,0,0), location(0,0,0,0,0)],item("stick"),"TRUE");
```

<h3 id=game_cancel_event>
  <code>world::cancel_event</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отмена события\
**Тип:** Действие без значения\
**Описание:** Отменяет начальное событие, который вызвал этот код.

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
**Описание:** Удаляет все предметы из контейнера на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:** 
```ts
world::clear_container(location(0,0,0,0,0));
```

<h3 id=game_clear_container_items>
  <code>world::clear_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить предметы в контейнере\
**Тип:** Действие без значения\
**Описание:** Очищает указанные предметы из контейнера.
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:** 
```ts
world::clear_container_items(location(0,0,0,0,0),[item("stick"), item("stick")]);
```

<h3 id=game_clear_exploded_blocks>
  <code>world::clear_exploded_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить взорванные блоки\
**Тип:** Действие без значения\
**Описание:** Возвращает взорванные блоки в исходное положение.
**Работает с:**\
&nbsp;&nbsp;Событием взрыва сущности\
&nbsp;&nbsp;Событием взрыва блока

**Пример использования:** 
```ts
world::clear_exploded_blocks([location(0,0,0,0,0), location(0,0,0,0,0)]);
```

<h3 id=game_clear_region>
  <code>world::clear_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить регион\
**Тип:** Действие без значения\
**Описание:** Удаляет все блоки в регионе.

**Пример использования:** 
```ts
world::clear_region(location(0,0,0,0,0),location(0,0,0,0,0));
```

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
```

<h3 id=game_clone_region>
  <code>world::clone_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Клонировать блоки региона\
**Тип:** Действие без значения\
**Описание:** Клонирует регион на выбраное местоположение.

**Пример использования:** 
```ts
world::clone_region(location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),location(0,0,0,0,0),"TRUE","TRUE");
```

<h3 id=game_create_explosion>
  <code>world::create_explosion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать взрыв\
**Тип:** Действие без значения\
**Описание:** Создаёт взрыв в указанном местоположении.

**Пример использования:** 
```ts
world::create_explosion(location(0,0,0,0,0),1);
```

<h3 id=game_create_scoreboard>
  <code>world::create_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать скорборд\
**Тип:** Действие без значения\
**Описание:** Создаёт скорборд с определённым ID. Чтобы отобразить скорборд игроку используйте действие "Показать скорборд".

**Пример использования:** 
```ts
world::create_scoreboard("id","display_name");
```

<h3 id=game_fill_container>
  <code>world::fill_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заполнить контейнер\
**Тип:** Действие без значения\
**Описание:** Заполняет контейнер на выбранном местоположении указанными предметами.
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:** 
```ts
world::fill_container(location(0,0,0,0,0),[item("stick"), item("stick")]);
```

<h3 id=game_generate_tree>
  <code>world::generate_tree</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать дерево\
**Тип:** Действие без значения\
**Описание:** Создаёт дерево на выбранном местоположении.

**Пример использования:** 
```ts
world::generate_tree(location(0,0,0,0,0),"TREE");
```

<h3 id=game_hide_event_message>
  <code>world::hide_event_message</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Убрать сообщение события\
**Тип:** Действие без значения\
**Описание:** Убирает отправку сообщения события, который вызвал этот код.
**Работает с:**\
&nbsp;&nbsp;Событием входа игрока\
&nbsp;&nbsp;Событием выхода игрока\
&nbsp;&nbsp;Событием смерти игрока

**Пример использования:** 
```ts
world::hide_event_message("TRUE");
```

<h3 id=game_launch_firework>
  <code>world::launch_firework</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать фейерверк\
**Тип:** Действие без значения\
**Описание:** Запускает фейерверк в указанном местоположении.

**Пример использования:** 
```ts
world::launch_firework(item("stick"),location(0,0,0,0,0),"UPWARDS","TRUE");
```

<h3 id=game_launch_projectile>
  <code>world::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить снаряд\
**Тип:** Действие без значения\
**Описание:** Запускает снаряд в указанном местоположении.

**Пример использования:** 
```ts
world::launch_projectile(item("stick"),location(0,0,0,0,0),1,2,"custom_name",particle("fire"));
```

<h3 id=game_random_tick_block>
  <code>world::random_tick_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Вызвать случайный тик\
**Тип:** Действие без значения\
**Описание:** Вызывает случайный тик на выбранном местоположении.

**Пример использования:** 
```ts
world::random_tick_block(location(0,0,0,0,0),1);
```

<h3 id=game_remove_container_items>
  <code>world::remove_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить предметы из контейнера\
**Тип:** Действие без значения\
**Описание:** Удаляет из контейнера на выбранном местоположении указанные предметы.
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:** 
```ts
world::remove_container_items(location(0,0,0,0,0),[item("stick"), item("stick")]);
```

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
```

<h3 id=game_remove_scoreboard_score_by_name>
  <code>world::remove_scoreboard_score_by_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить значение скорборда по тексту\
**Тип:** Действие без значения\
**Описание:** Удаляет значение указанной строки в скорборде.

**Пример использования:** 
```ts
world::remove_scoreboard_score_by_name("id","text");
```

<h3 id=game_remove_scoreboard_score_by_score>
  <code>world::remove_scoreboard_score_by_score</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить значение скорборда по счёту\
**Тип:** Действие без значения\
**Описание:** Удаляет значение указанного скорборда по счёту.

**Пример использования:** 
```ts
world::remove_scoreboard_score_by_score("id",1);
```

<h3 id=game_replace_blocks_in_region>
  <code>world::replace_blocks_in_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заменить блоки в регионе\
**Тип:** Действие без значения\
**Описание:** Заменяет одни блоки на другие в выбранном регионе.

**Пример использования:** 
```ts
world::replace_blocks_in_region([item("stone"), item("stone")],location(0,0,0,0,0),location(0,0,0,0,0),item("stone"));
```

<h3 id=game_replace_container_items>
  <code>world::replace_container_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заменить предметы в контейнере\
**Тип:** Действие без значения\
**Описание:** Заменяет указанные предметы в контейнере на выбранном местоположении на определённый предмет.
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:** 
```ts
world::replace_container_items([item("stick"), item("stick")],location(0,0,0,0,0),item("stick"),1);
```

<h3 id=game_send_web_request>
  <code>world::send_web_request</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отправить веб-запрос\
**Тип:** Действие без значения\
**Описание:** Отправляет веб-запрос с выбранным методом и телом на выбранный URL.

**Пример использования:** 
```ts
world::send_web_request("url","content_body","GET","TEXT_PLAIN");
```

<h3 id=game_set_age>
  <code>world::set_age</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить возраст\
**Тип:** Действие без значения\
**Описание:** Устанавливает возраст блока на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Любыми блоками, которые могут иметь возраст

**Пример использования:** 
```ts
world::set_age(location(0,0,0,0,0),1);
```

<h3 id=game_set_block_analogue_power>
  <code>world::set_block_analogue_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить силу редстоун сигнала\
**Тип:** Действие без значения\
**Описание:** Устанавливает на выбранном местоположении определённую силу сигнала.
**Работает с:**\
&nbsp;&nbsp;Активируемыми блоками

**Пример использования:** 
```ts
world::set_block_analogue_power(location(0,0,0,0,0),1);
```

<h3 id=game_set_block>
  <code>world::set_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить блок\
**Тип:** Действие без значения\
**Описание:** Устанавливает выбранный тип блока на выбранных местоположениях.

**Пример использования:** 
```ts
world::set_block(item("stone"),[location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE");
```

<h3 id=game_set_block_custom_tag>
  <code>world::set_block_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** None\
**Тип:** Действие без значения\
**Описание:** None

**Пример использования:** 
```ts
world::set_block_custom_tag(location(0,0,0,0,0),"tag_name","tag_value");
```

<h3 id=game_set_block_data>
  <code>world::set_block_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить параметры блоку\
**Тип:** Действие без значения\
**Описание:** Устанавливает параметры блоку на определённом местоположении.

**Пример использования:** 
```ts
world::set_block_data(location(0,0,0,0,0),"block_data");
```

<h3 id=game_set_block_drops_enabled>
  <code>world::set_block_drops_enabled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить выпадение блоков\
**Тип:** Действие без значения\
**Описание:** Устанавливает правило в мире на выпадение блоков при их разрушении.

**Пример использования:** 
```ts
world::set_block_drops_enabled("TRUE");
```

<h3 id=game_set_block_single_data>
  <code>world::set_block_single_data</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить параметр блоку\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанный параметр блоку на местоположении на заданое значение.

**Пример использования:** 
```ts
world::set_block_single_data(location(0,0,0,0,0),"data","value");
```

<h3 id=game_set_brushable_block_item>
  <code>world::set_brushable_block_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет в подозрительный блок\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет в подозрительный блок (песок, гравий) на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Подозрительным песком\
&nbsp;&nbsp;Подозрительным гравием

**Пример использования:** 
```ts
world::set_brushable_block_item(location(0,0,0,0,0),item("stick"));
```

<h3 id=game_set_campfire_item>
  <code>world::set_campfire_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет в костёр\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет в костёр на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Кострами

**Пример использования:** 
```ts
world::set_campfire_item(location(0,0,0,0,0),item("stick"),1,"FIRST");
```

<h3 id=game_set_container>
  <code>world::set_container</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предметы в контейнере\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанные предметы в контейнер на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:** 
```ts
world::set_container([location(0,0,0,0,0), location(0,0,0,0,0)],[item("stick"), item("stick")]);
```

<h3 id=game_set_container_lock>
  <code>world::set_container_lock</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить ключ контейнера\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённый ключ контейнеру на выбранном местоположении.

**Пример использования:** 
```ts
world::set_container_lock(location(0,0,0,0,0),"container_key");
```

<h3 id=game_set_container_name>
  <code>world::set_container_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить имя контейнеру\
**Тип:** Действие без значения\
**Описание:** Устанавливает имя контейнеру на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:** 
```ts
world::set_container_name(location(0,0,0,0,0),"name");
```

<h3 id=game_set_decorate_pot_sherd>
  <code>world::set_decorate_pot_sherd</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить украшение кувшина\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанный черепок выбранной стороне кувшина на указанном местоположении.
**Работает с:**\
&nbsp;&nbsp;Кувшинами

**Пример использования:** 
```ts
world::set_decorate_pot_sherd(location(0,0,0,0,0),item("stick"),"BACK");
```

<h3 id=game_set_event_damage>
  <code>world::set_event_damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить урон события\
**Тип:** Действие без значения\
**Описание:** Устанавливает урон связанный с этим событием.
**Работает с:**\
&nbsp;&nbsp;Событиями урона

**Пример использования:** 
```ts
world::set_event_damage(1);
```

<h3 id=game_set_event_exhaustion>
  <code>world::set_event_exhaustion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить истощение события\
**Тип:** Действие без значения\
**Описание:** Устанавливает значение истощения связанного с этим событием.
**Работает с:**\
&nbsp;&nbsp;Событием истощения

**Пример использования:** 
```ts
world::set_event_exhaustion(1);
```

<h3 id=game_set_event_experience>
  <code>world::set_event_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить опыт события\
**Тип:** Действие без значения\
**Описание:** Устанавливает значение опыта связанное с этим событием.
**Работает с:**\
&nbsp;&nbsp;Событием рыбалки\
&nbsp;&nbsp;Событием получения опыта\
&nbsp;&nbsp;Событиями убийства

**Пример использования:** 
```ts
world::set_event_experience(1);
```

<h3 id=game_set_event_heal>
  <code>world::set_event_heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить лечение события\
**Тип:** Действие без значения\
**Описание:** Устанавливает значение лечения связанное с этим событием.
**Работает с:**\
&nbsp;&nbsp;Событием лечения игрока\
&nbsp;&nbsp;Событием лечения сущности

**Пример использования:** 
```ts
world::set_event_heal(1);
```

<h3 id=game_set_event_item>
  <code>world::set_event_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет события\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет связанный с этим событием.

**Пример использования:** 
```ts
world::set_event_item(item("stick"));
```

<h3 id=game_set_event_items>
  <code>world::set_event_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предметы события\
**Тип:** Действие без значения\
**Описание:** Устанавливает предметы связанные с этим событием.
**Работает с:**\
&nbsp;&nbsp;Событием нахождения предмета в инвентаре

**Пример использования:** 
```ts
world::set_event_items([item("stick"), item("stick")]);
```

<h3 id=game_set_event_move_allowed>
  <code>world::set_event_move_allowed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Разрешить передвижение\
**Тип:** Действие без значения\
**Описание:** Разрешает передвижение, если оно не удалось.
**Работает с:**\
&nbsp;&nbsp;Событием "Игроку не удалось передвинуться"

**Пример использования:** 
```ts
world::set_event_move_allowed("TRUE");
```

<h3 id=game_set_event_projectile>
  <code>world::set_event_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить снаряд события\
**Тип:** Действие без значения\
**Описание:** Заменяет снаряд, который связан с этим событием.

**Пример использования:** 
```ts
world::set_event_projectile(item("stick"),"name");
```

<h3 id=game_set_event_uery_info>
  <code>world::set_event_uery_info</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить теги в полученную информацию\
**Тип:** Действие без значения\
**Описание:** Добавляет дополнительные теги в полученную отладочную информацию, которые скопируются в буфер обмена, если событие не отменено.\
**Дополнительная информация:**\
&nbsp;&nbsp;Изменения касаются только дополнительной информации.\
**Работает с:**\
&nbsp;&nbsp;Событием "Игрок получает информацию о блоке"\
&nbsp;&nbsp;Событием "Игрок получает информацию о сущности"

**Пример использования:** 
```ts
world::set_event_uery_info("information");
```

<h3 id=game_set_event_sound>
  <code>world::set_event_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить звук события\
**Тип:** Действие без значения\
**Описание:** Устанавливает звук для проигрывания связанный с этим событием, заменяя изначальный.

**Пример использования:** 
```ts
world::set_event_sound(sound("entity.zombie.hurt"));
```

<h3 id=game_set_event_source_slot>
  <code>world::set_event_source_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить начальный слот события\
**Тип:** Действие без значения\
**Описание:** Устанавливает начальный слот связанный с этим событием.
**Работает с:**\
&nbsp;&nbsp;Событием нахождения предмета в инвентаре

**Пример использования:** 
```ts
world::set_event_source_slot(1);
```

<h3 id=game_set_event_target_slot>
  <code>world::set_event_target_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить конечный слот события\
**Тип:** Действие без значения\
**Описание:** Устанавливает конечный слот связанный с этим событием.
**Работает с:**\
&nbsp;&nbsp;Событием нахождения предмета в инвентаре

**Пример использования:** 
```ts
world::set_event_target_slot(1);
```

<h3 id=game_set_furnace_cook_time>
  <code>world::set_furnace_cook_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время готовки печи\
**Тип:** Действие без значения\
**Описание:** Устанавливает время готовки печи на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Печками\
&nbsp;&nbsp;Плавильнями\
&nbsp;&nbsp;Коптильнями

**Пример использования:** 
```ts
world::set_furnace_cook_time(location(0,0,0,0,0),1);
```

<h3 id=game_set_item_in_container_slot>
  <code>world::set_item_in_container_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет в слот контейнера\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет в указанный слот контейнера на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Любыми контейнерами

**Пример использования:** 
```ts
world::set_item_in_container_slot(location(0,0,0,0,0),item("stick"),1);
```

<h3 id=game_set_lectern_book>
  <code>world::set_lectern_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить книгу в кафедру\
**Тип:** Действие без значения\
**Описание:** Устанавливает книгу в кафедру на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Кафедрами

**Пример использования:** 
```ts
world::set_lectern_book(location(0,0,0,0,0),item("stick"),1);
```

<h3 id=game_set_player_head>
  <code>world::set_player_head</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить голову игрока\
**Тип:** Действие без значения\
**Описание:** Устанавливает голову игрока на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Головами игроков

**Пример использования:** 
```ts
world::set_player_head(location(0,0,0,0,0),"name_or_uuid","NAME_OR_UUID");
```

<h3 id=game_set_block_powered>
  <code>world::set_block_powered</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Активировать блок\
**Тип:** Действие без значения\
**Описание:** Активирует блок на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Активируемыми блоками

**Пример использования:** 
```ts
world::set_block_powered(location(0,0,0,0,0),"TRUE");
```

<h3 id=game_set_region>
  <code>world::set_region</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить блоки в регионе\
**Тип:** Действие без значения\
**Описание:** Устанавливает выбранный тип блока на весь выбранный регион.

**Пример использования:** 
```ts
world::set_region(item("stone"),location(0,0,0,0,0),location(0,0,0,0,0));
```

<h3 id=game_set_scoreboard_line>
  <code>world::set_scoreboard_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить линию в скорборде\
**Тип:** Действие без значения\
**Описание:** Устанавливает линию в скорборде.

**Пример использования:** 
```ts
world::set_scoreboard_line("id","line","display",1,"format_content","BLANK");

#Или от объекта

"id".set_scoreboard_line("line","display",1,"format_content","BLANK");
```

<h3 id=game_set_scoreboard_line_display>
  <code>world::set_scoreboard_line_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить отображаемый текст линии скорборда\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанной линии скорборда отображаемый текст.

**Пример использования:** 
```ts
world::set_scoreboard_line_display("id","line","display");

#Или от объекта

"id".set_scoreboard_line_display("line","display");
```

<h3 id=game_set_scoreboard_line_format>
  <code>world::set_scoreboard_line_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить формат текста линии скорборда\
**Тип:** Действие без значения\
**Описание:** Устанавливает форматирование текста указанной линии скорборда.

**Пример использования:** 
```ts
world::set_scoreboard_line_format("id","line","format_content","BLANK");

#Или от объекта

"id".set_scoreboard_line_format("line","format_content","BLANK");
```

<h3 id=game_set_scoreboard_number_format>
  <code>world::set_scoreboard_number_format</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить форматирование значений скорборда\
**Тип:** Действие без значения\
**Описание:** Устанавливает форматирование значений для скорборда.

**Пример использования:** 
```ts
world::set_scoreboard_number_format("id","format_content","BLANK");

#Или от объекта

"id".set_scoreboard_number_format("format_content","BLANK");
```

<h3 id=game_set_scoreboard_score>
  <code>world::set_scoreboard_score</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить значение скорборда\
**Тип:** Действие без значения\
**Описание:** Устанавливает значение указанной строке в скорборде.

**Пример использования:** 
```ts
world::set_scoreboard_score("id","text",1);
```

<h3 id=game_set_scoreboard_title>
  <code>world::set_scoreboard_title</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Изменить заголовок скорборда\
**Тип:** Действие без значения\
**Описание:** Изменяет заголовок указанного скорборда.

**Пример использования:** 
```ts
world::set_scoreboard_title("id","title");
```

<h3 id=game_set_sculk_shrieker_can_summon>
  <code>world::set_sculk_shrieker_can_summon</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить скалк-крикуну возможность призыва\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанному скалк-крикуну возможность призыва Вардена.
**Работает с:**\
&nbsp;&nbsp;Скалк-крикунами

**Пример использования:** 
```ts
world::set_sculk_shrieker_can_summon(location(0,0,0,0,0),"TRUE");
```

<h3 id=game_set_sculk_shrieker_shrieking>
  <code>world::set_sculk_shrieker_shrieking</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить состояние скалк-крикуну\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанному скалк-крикуну состояние.
**Работает с:**\
&nbsp;&nbsp;Скалк-крикунами

**Пример использования:** 
```ts
world::set_sculk_shrieker_shrieking(location(0,0,0,0,0),"TRUE");
```

<h3 id=game_set_sculk_shrieker_warning_level>
  <code>world::set_sculk_shrieker_warning_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить скалк-крикуну уровень опасности\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанному скалк-крикуну уровень опасности.
**Работает с:**\
&nbsp;&nbsp;Скалк-крикунами

**Пример использования:** 
```ts
world::set_sculk_shrieker_warning_level(location(0,0,0,0,0),1);
```

<h3 id=game_set_sign_text>
  <code>world::set_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить текст таблички\
**Тип:** Действие без значения\
**Описание:** Устанавливает текст таблички на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Табличками

**Пример использования:** 
```ts
world::set_sign_text(location(0,0,0,0,0),"text",1,"FRONT");
```

<h3 id=game_set_sign_text_color>
  <code>world::set_sign_text_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет текста таблички\
**Тип:** Действие без значения\
**Описание:** Устанавливает цвет текста таблички на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Табличками

**Пример использования:** 
```ts
world::set_sign_text_color(location(0,0,0,0,0),"FRONT","BLACK","TRUE");
```

<h3 id=game_set_sign_waxed>
  <code>world::set_sign_waxed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить вощённость таблички\
**Тип:** Действие без значения\
**Описание:** Устанавливает вощённость таблички на выбранном местоположении.
**Работает с:**\
&nbsp;&nbsp;Табличками

**Пример использования:** 
```ts
world::set_sign_waxed(location(0,0,0,0,0),"TRUE");
```

<h3 id=game_set_spawner_entity>
  <code>world::set_spawner_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить сущность в спавнере\
**Тип:** Действие без значения\
**Описание:** Устанавливает спавнеру на выбранном местоположении сущность внутри.
**Работает с:**\
&nbsp;&nbsp;Спавнерами

**Пример использования:** 
```ts
world::set_spawner_entity(location(0,0,0,0,0),item("stick"));

#Или от объекта

location(0,0,0,0,0).set_spawner_entity(item("stick"));
```

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
```

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
```

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
```

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
world::set_world_weather("CLEAR",1);
```

<h3 id=game_spawn_armor_stand>
  <code>world::spawn_armor_stand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать стойку для брони\
**Тип:** Действие без значения\
**Описание:** Создаёт стойку для брони в указанном местоположении.

**Пример использования:** 
```ts
world::spawn_armor_stand(item("stick"),item("stick"),item("stick"),item("stick"),item("stick"),item("stick"),"TRUE","TRUE","TRUE","TRUE","TRUE","TRUE",location(0,0,0,0,0),"custom_name");
```

<h3 id=game_spawn_block_display>
  <code>world::spawn_block_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать визуализатор блока\
**Тип:** Действие без значения\
**Описание:** Создаёт визуализатор блока на указанном местоположении

**Пример использования:** 
```ts
world::spawn_block_display(location(0,0,0,0,0),"custom_name",item("stone"));
```

<h3 id=game_spawn_effect_cloud>
  <code>world::spawn_effect_cloud</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать облако туманного зелья\
**Тип:** Действие без значения\
**Описание:** Создаёт облако туманного зелья, которое пропитывает эффектами сущностей в нём.

**Пример использования:** 
```ts
world::spawn_effect_cloud(location(0,0,0,0,0),[potion("slow_falling"), potion("slow_falling")],1,2,particle("fire"),"custom_name");
```

<h3 id=game_spawn_end_crystal>
  <code>world::spawn_end_crystal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать кристалл Энда\
**Тип:** Действие без значения\
**Описание:** Создаёт кристалл Энда в указанном местоположении.

**Пример использования:** 
```ts
world::spawn_end_crystal(location(0,0,0,0,0),"custom_name","TRUE");
```

<h3 id=game_spawn_evoker_fangs>
  <code>world::spawn_evoker_fangs</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать челюсти заклинателя\
**Тип:** Действие без значения\
**Описание:** Создаёт челюсти заклинателя в указанном местоположении.

**Пример использования:** 
```ts
world::spawn_evoker_fangs(location(0,0,0,0,0),"custom_name");
```

<h3 id=game_spawn_experience_orb>
  <code>world::spawn_experience_orb</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать сферу опыта\
**Тип:** Действие без значения\
**Описание:** Создаёт сферу опыта в указанном местоположении с выбранными параметрами.

**Пример использования:** 
```ts
world::spawn_experience_orb(location(0,0,0,0,0),1,"custom_name");
```

<h3 id=game_spawn_eye_of_ender>
  <code>world::spawn_eye_of_ender</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать око Энда\
**Тип:** Действие без значения\
**Описание:** Создаёт в указанном местоположении око Энда, которое будет двигаться в сторону цели.

**Пример использования:** 
```ts
world::spawn_eye_of_ender(location(0,0,0,0,0),location(0,0,0,0,0),1,"custom_name","DROP");
```

<h3 id=game_spawn_falling_block>
  <code>world::spawn_falling_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать падающий блок\
**Тип:** Действие без значения\
**Описание:** Создаёт падающий блок в указанном местоположении.

**Пример использования:** 
```ts
world::spawn_falling_block(item("stone"),location(0,0,0,0,0),"name","TRUE");
```

<h3 id=game_spawn_interaction_entity>
  <code>world::spawn_interaction_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать сущность взаимодействия\
**Тип:** Действие без значения\
**Описание:** Создаёт сущность взаимодействия на указанном местоположении

**Пример использования:** 
```ts
world::spawn_interaction_entity(location(0,0,0,0,0),"custom_name",1,2,"TRUE");
```

<h3 id=game_spawn_item>
  <code>world::spawn_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать предмет\
**Тип:** Действие без значения\
**Описание:** Создаёт предмет в указанном местоположении с выбранными параметрами.

**Пример использования:** 
```ts
world::spawn_item(item("stick"),location(0,0,0,0,0),"custom_name","TRUE","TRUE","TRUE");
```

<h3 id=game_spawn_item_display>
  <code>world::spawn_item_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать визуализатор предмета\
**Тип:** Действие без значения\
**Описание:** Создаёт визуализатор предмета на указанном местоположении

**Пример использования:** 
```ts
world::spawn_item_display(location(0,0,0,0,0),"custom_name",item("stick"));
```

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
```

<h3 id=game_spawn_mob>
  <code>world::spawn_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать моба\
**Тип:** Действие без значения\
**Описание:** Создаёт моба в указанном местоположении с выбранными параметрами.

**Пример использования:** 
```ts
world::spawn_mob(item("stick"),location(0,0,0,0,0),1,"custom_name",[potion("slow_falling"), potion("slow_falling")],item("stick"),item("stick"),item("stick"),item("stick"),item("stick"),item("stick"),"TRUE");
```

<h3 id=game_spawn_primed_tnt>
  <code>world::spawn_primed_tnt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать подожженный динамит\
**Тип:** Действие без значения\
**Описание:** Создаёт подожжённый динамит в указанном местоположении.

**Пример использования:** 
```ts
world::spawn_primed_tnt(location(0,0,0,0,0),1,2,"custom_name",item("stone"));
```

<h3 id=game_spawn_shulker_bullet>
  <code>world::spawn_shulker_bullet</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать снаряд Шалкера\
**Тип:** Действие без значения\
**Описание:** Создаёт снаряд Шалкера в указанном местоположении.

**Пример использования:** 
```ts
world::spawn_shulker_bullet(location(0,0,0,0,0),"custom_name");
```

<h3 id=game_spawn_text_display>
  <code>world::spawn_text_display</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать визуализатор текста\
**Тип:** Действие без значения\
**Описание:** Создаёт визуализатор текста на указанном местоположении

**Пример использования:** 
```ts
world::spawn_text_display(location(0,0,0,0,0),"custom_name","SPACES",["displayed_text", "displayed_text"]);
```

<h3 id=game_spawn_vehicle>
  <code>world::spawn_vehicle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Создать транспорт\
**Тип:** Действие без значения\
**Описание:** Создаёт транспорт в указанном местоположении с выбранными параметрами.

**Пример использования:** 
```ts
world::spawn_vehicle(item("stick"),location(0,0,0,0,0),"custom_name");
```

<h3 id=game_uncancel_event>
  <code>world::uncancel_event</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Возврат события\
**Тип:** Действие без значения\
**Описание:** Возвращает отмену события, который вызвал этот код.

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
```

<h3 id=if_game_block_equals>
  <code>world::block_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Блок равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, является ли блок в определённом местоположении определённым типом блока.

**Пример использования:** 
```ts
if(world::block_equals(location(0,0,0,0,0),[item("stone"), item("stone")]){
    player::message("Условие верно");
}
```

<h3 id=if_game_block_powered>
  <code>world::block_powered</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Блок запитан редстоуном\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, запитан ли блок в определённом местоположении редстоуном.

**Пример использования:** 
```ts
if(world::block_powered([location(0,0,0,0,0), location(0,0,0,0,0)],"DIRECT"){
    player::message("Условие верно");
}
```

<h3 id=if_game_chunk_is_loaded>
  <code>world::chunk_is_loaded</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Чанк загружен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, загружен ли чанк на местоположении

**Пример использования:** 
```ts
if(world::chunk_is_loaded(location(0,0,0,0,0)){
    player::message("Условие верно");
}
```

<h3 id=if_game_container_has>
  <code>world::container_has</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Контейнер имеет предмет\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли контейнер в определённом местоположении определённые предметы в его инвентаре.

**Пример использования:** 
```ts
if(world::container_has(location(0,0,0,0,0),[item("stick"), item("stick")],"ANY","EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_game_container_has_room_for_item>
  <code>world::container_has_room_for_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Контейнер имеет место для предметов\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли контейнер в определённом местоположении место для предметов в его инвентаре.

**Пример использования:** 
```ts
if(world::container_has_room_for_item(location(0,0,0,0,0),[item("stick"), item("stick")],"ANY"){
    player::message("Условие верно");
}
```

<h3 id=if_game_damage_cause_equals>
  <code>world::damage_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Источник урона события равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли источник урона события выбранному.

**Пример использования:** 
```ts
if(world::damage_cause_equals("BLOCK_EXPLOSION"){
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
if(world::event_attack_is_critical(){
    player::message("Условие верно");
}
```

<h3 id=if_game_event_block_equals>
  <code>world::event_block_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Блок события равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли блок текущего события определенному блоку.

**Пример использования:** 
```ts
if(world::event_block_equals([item("stone"), item("stone")],[location(0,0,0,0,0), location(0,0,0,0,0)]){
    player::message("Условие верно");
}
```

<h3 id=if_game_event_is_canceled>
  <code>world::event_is_canceled</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Событие отменено\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, отменено ли событие.

**Пример использования:** 
```ts
if(world::event_is_canceled(){
    player::message("Условие верно");
}
```

<h3 id=if_game_event_item_equals>
  <code>world::event_item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет события равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли предмет текущего события определенному предмету.

**Пример использования:** 
```ts
if(world::event_item_equals([item("stick"), item("stick")],"EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_game_has_player>
  <code>world::has_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Игрок в игре\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли определённый игрок в игре.

**Пример использования:** 
```ts
if(world::has_player(["names_or_uuids", "names_or_uuids"]){
    player::message("Условие верно");
}
```

<h3 id=if_game_heal_cause_equals>
  <code>world::heal_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Источник исцеления равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли источник исцеления выбранному.

**Пример использования:** 
```ts
if(world::heal_cause_equals("CUSTOM"){
    player::message("Условие верно");
}
```

<h3 id=if_game_ignite_cause_equals>
  <code>world::ignite_cause_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Источник огня равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли источник огня выбранному.

**Пример использования:** 
```ts
if(world::ignite_cause_equals("ARROW"){
    player::message("Условие верно");
}
```

<h3 id=if_game_instrument_equals>
  <code>world::instrument_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Инструмент равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли инструмент в событии выбранному.

**Пример использования:** 
```ts
if(world::instrument_equals("BANJO"){
    player::message("Условие верно");
}
```

<h3 id=if_game_sign_contains>
  <code>world::sign_contains</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Табличка содержит текст\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, содержит ли табличка в определённом местоположении определённый текст.

**Пример использования:** 
```ts
if(world::sign_contains(location(0,0,0,0,0),["texts", "texts"],"ANY","ANY","FIRST"){
    player::message("Условие верно");
}
```

