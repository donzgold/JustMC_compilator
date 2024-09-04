<h2 id=entity>
  <code>entity</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

### Селекторы

| **Имя**            | **Описание**          |
| ------------------ | --------------------- |
| `<current>`        | Текущая цель          |
| `<default_entity>` | Сущность по умолчанию |
| `<killer_entity>`  | Убийца                |
| `<shooter_entity>` | Стрелок               |
| `<projectile>`     | Снаряд стрелка        |
| `<victim_entity>`  | Жертва                |
| `<random_entity>`  | Случайная сущность    |
| `<all_mobs>`       | Все мобы              |
| `<all_entities>`   | Все сущности          |
| `<last_entity>`    | Последняя сущность    |

<h3 id=entity_attach_lead>
  <code>entity::attach_lead</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Привязать на поводок\
**Тип:** Действие без значения\
**Описание:** Привязывает существо на поводок к забору или существу.

**Пример использования:** 
```ts
entity::attach_lead("name_or_uuid",location(0,0,0,0,0));
```

<h3 id=entity_clear_merchant_recipes>
  <code>entity::clear_merchant_recipes</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить торги Жителю\
**Тип:** Действие без значения\
**Описание:** Очищает все торги Жителю.
**Работает с:**\
&nbsp;&nbsp;Жителями\
&nbsp;&nbsp;Странствующими торговцами

**Пример использования:** 
```ts
entity::clear_merchant_recipes();
```

<h3 id=entity_celar_potion_effects>
  <code>entity::clear_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить эффекты\
**Тип:** Действие без значения\
**Описание:** Очищает все эффекты у существа.

**Пример использования:** 
```ts
entity::clear_potion_effects();
```

<h3 id=entity_damage>
  <code>entity::damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Нанести урон\
**Тип:** Действие без значения\
**Описание:** Наносит урон существу.

**Пример использования:** 
```ts
entity::damage(1,"source");
```

<h3 id=entity_disguise_as_block>
  <code>entity::disguise_as_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать сущность под блок\
**Тип:** Действие без значения\
**Описание:** Маскирует сущность под блок.

**Пример использования:** 
```ts
entity::disguise_as_block(item("stone"));
```

<h3 id=entity_disguise_as_entity>
  <code>entity::disguise_as_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать под сущность\
**Тип:** Действие без значения\
**Описание:** Замаскировать сущность под сущность.

**Пример использования:** 
```ts
entity::disguise_as_entity(item("stick"));
```

<h3 id=entity_disguise_as_item>
  <code>entity::disguise_as_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать сущность под предмет\
**Тип:** Действие без значения\
**Описание:** Маскирует сущность под предмет.

**Пример использования:** 
```ts
entity::disguise_as_item(item("stick"));
```

<h3 id=entity_disguise_as_player>
  <code>entity::disguise_as_player</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать сущность под игрока\
**Тип:** Действие без значения\
**Описание:** Маскирует сущность под игрока.

**Пример использования:** 
```ts
entity::disguise_as_player("name_or_uuid","display_name","MOJANG");
```

<h3 id=entity_eat_grass>
  <code>entity::eat_grass</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Есть траву\
**Тип:** Действие без значения\
**Описание:** Заставляет овцу есть траву.
**Работает с:**\
&nbsp;&nbsp;Овцами

**Пример использования:** 
```ts
entity::eat_grass();
```

<h3 id=entity_eat_target>
  <code>entity::eat_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цель поедания\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу цель для поедания.
**Работает с:**\
&nbsp;&nbsp;Жабами

**Пример использования:** 
```ts
entity::eat_target("name_or_uuid");
```

<h3 id=entity_explode>
  <code>entity::explode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Взорваться\
**Тип:** Действие без значения\
**Описание:** Заставляет существо взорваться.
**Работает с:**\
&nbsp;&nbsp;Криперами\
&nbsp;&nbsp;Динамитом\
&nbsp;&nbsp;Фейерверками

**Пример использования:** 
```ts
entity::explode();
```

<h3 id=entity_face_location>
  <code>entity::face_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Повернуть к местоположению\
**Тип:** Действие без значения\
**Описание:** Поворачивает существо в сторону к местоположению.

**Пример использования:** 
```ts
entity::face_location(location(0,0,0,0,0));
```

<h3 id=entity_get_custom_tag>
  <code>entity::get_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Получить кастомный тег\
**Тип:** Действие, возращающее значение\
**Описание:** Получает кастомный нбт-тег существа.

**Пример использования:** 
```ts
a1 = entity::get_custom_tag("name","any value");

#Или в сухую

entity::get_custom_tag(a1,"name","any value");
```

<h3 id=entity_give_potion_effects>
  <code>entity::give_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выдать эффекты\
**Тип:** Действие без значения\
**Описание:** Выдаёт выбранные эффекты существу.

**Пример использования:** 
```ts
entity::give_potion_effects([potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");
```

<h3 id=entity_heal>
  <code>entity::heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Исцелить существо\
**Тип:** Действие без значения\
**Описание:** Исцеляет существо.

**Пример использования:** 
```ts
entity::heal(1);
```

<h3 id=entity_ignite_creeper>
  <code>entity::ignite_creeper</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Зажечь крипера\
**Тип:** Действие без значения\
**Описание:** Поджигает крипера, заставляя его взорваться после определённого периода.
**Работает с:**\
&nbsp;&nbsp;Криперами

**Пример использования:** 
```ts
entity::ignite_creeper();
```

<h3 id=entity_jump>
  <code>entity::jump</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Прыгнуть\
**Тип:** Действие без значения\
**Описание:** Заставляет существо прыгнуть.
**Работает с:**\
&nbsp;&nbsp;Мобами

**Пример использования:** 
```ts
entity::jump();
```

<h3 id=entity_launch_forward>
  <code>entity::launch_forward</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить вперёд\
**Тип:** Действие без значения\
**Описание:** Запускает существо вперёд или назад по направлению взгляда в зависимости от силы.

**Пример использования:** 
```ts
entity::launch_forward(1,"TRUE","YAW_AND_PITCH");
```

<h3 id=entity_launch_projectile>
  <code>entity::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить снаряд\
**Тип:** Действие без значения\
**Описание:** Запустить снаряд из местоположения существа.

**Пример использования:** 
```ts
entity::launch_projectile(item("stick"),location(0,0,0,0,0),"name",1,2,particle("fire"));
```

<h3 id=entity_launch_to_location>
  <code>entity::launch_to_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить к местоположению\
**Тип:** Действие без значения\
**Описание:** Запускает существа к выбранному местоположению.

**Пример использования:** 
```ts
entity::launch_to_location(location(0,0,0,0,0),1,"TRUE");
```

<h3 id=entity_launch_up>
  <code>entity::launch_up</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Подбросить вверх\
**Тип:** Действие без значения\
**Описание:** Подбрасывает существо вверх или вниз в зависимости от силы.

**Пример использования:** 
```ts
entity::launch_up(1,"TRUE");
```

<h3 id=entity_modify_piglin_barter_materials>
  <code>entity::modify_piglin_barter_materials</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Изменить торги пиглина\
**Тип:** Действие без значения\
**Описание:** Изменяет предметы, которые может дать пиглин при обмене.\
**Дополнительная информация:**\
&nbsp;&nbsp;Нельзя изменить предметы, которые пиглин продает по умолчанию.\
**Работает с:**\
&nbsp;&nbsp;Пиглинами

**Пример использования:** 
```ts
entity::modify_piglin_barter_materials([item("stick"), item("stick")],"ADD");
```

<h3 id=entity_modify_piglin_interested_materials>
  <code>entity::modify_piglin_interested_materials</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Изменить предметы для торга с пиглином\
**Тип:** Действие без значения\
**Описание:** Изменяет предметы, требуемые для обмена с пиглином.\
**Дополнительная информация:**\
&nbsp;&nbsp;Нельзя изменить предметы, которые пиглин требует по умолчанию.\
**Работает с:**\
&nbsp;&nbsp;Пиглинами

**Пример использования:** 
```ts
entity::modify_piglin_interested_materials([item("stick"), item("stick")],"ADD");
```

<h3 id=entity_move_to_location>
  <code>entity::move_to_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить движение к местоположению\
**Тип:** Действие без значения\
**Описание:** Инструктирует ИИ существа всегда находить путь к определенному местоположению с определенной скоростью.
**Работает с:**\
&nbsp;&nbsp;Мобами

**Пример использования:** 
```ts
entity::move_to_location(location(0,0,0,0,0),1);
```

<h3 id=entity_move_to_location_stop>
  <code>entity::move_to_location_stop</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Остановить движение к местоположению\
**Тип:** Действие без значения\
**Описание:** Останавливает сущность, идущую к местоположению.
**Работает с:**\
&nbsp;&nbsp;Мобами

**Пример использования:** 
```ts
entity::move_to_location_stop();
```

<h3 id=entity_play_damage_animation>
  <code>entity::play_damage_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить анимацию урона\
**Тип:** Действие без значения\
**Описание:** Отображает анимацию урона существу.

**Пример использования:** 
```ts
entity::play_damage_animation("DAMAGE");
```

<h3 id=entity_play_hurt_animation>
  <code>entity::play_hurt_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить анимацию получения урона\
**Тип:** Действие без значения\
**Описание:** Отображает существу анимацию получения урона с определённым наклоном.

**Пример использования:** 
```ts
entity::play_hurt_animation(1);
```

<h3 id=entity_ram_target>
  <code>entity::ram_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Таранить сущность\
**Тип:** Действие без значения\
**Описание:** Заставляет козлов таранить указанную сущность.
**Работает с:**\
&nbsp;&nbsp;Козлами

**Пример использования:** 
```ts
entity::ram_target("name_or_uuid");
```

<h3 id=entity_remove>
  <code>entity::remove</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить сущность\
**Тип:** Действие без значения\
**Описание:** Удаляет сущность из мира.

**Пример использования:** 
```ts
entity::remove();
```

<h3 id=entity_remove_custom_tag>
  <code>entity::remove_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить кастомный тег\
**Тип:** Действие без значения\
**Описание:** Удаляет кастомный нбт-тег у существа.

**Пример использования:** 
```ts
entity::remove_custom_tag("name");
```

<h3 id=entity_remove_disguise>
  <code>entity::remove_disguise</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Убрать маскировку\
**Тип:** Действие без значения\
**Описание:** Убирает маскировку у сущности.

**Пример использования:** 
```ts
entity::remove_disguise();
```

<h3 id=entity_remove_merchant_recipe>
  <code>entity::remove_merchant_recipe</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить товар Жителю\
**Тип:** Действие без значения\
**Описание:** Удаляет товар Жителю по указанному индексу.
**Работает с:**\
&nbsp;&nbsp;Жителями\
&nbsp;&nbsp;Странствующими торговцами

**Пример использования:** 
```ts
entity::remove_merchant_recipe(1);
```

<h3 id=entity_remove_potion_effect>
  <code>entity::remove_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить эффект\
**Тип:** Действие без значения\
**Описание:** Удаляет выбранные эффекты у существа.

**Пример использования:** 
```ts
entity::remove_potion_effect([potion("slow_falling"), potion("slow_falling")]);
```

<h3 id=entity_reset_display_brightness>
  <code>entity::reset_display_brightness</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сбросить яркость\
**Тип:** Действие без значения\
**Описание:** Сбросить яркость сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::reset_display_brightness();
```

<h3 id=entity_reset_display_glow_color>
  <code>entity::reset_display_glow_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сбросить цвет свечения\
**Тип:** Действие без значения\
**Описание:** Сбросить цвет свечения сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами предмета\
&nbsp;&nbsp;Визуализаторами блока

**Пример использования:** 
```ts
entity::reset_display_glow_color();
```

<h3 id=entity_reset_text_display_background>
  <code>entity::reset_text_display_background</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сбросить цвет фона\
**Тип:** Действие без значения\
**Описание:** Сбросить цвет и прозрачность фона визуализатору текста.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами текста

**Пример использования:** 
```ts
entity::reset_text_display_background();
```

<h3 id=entity_ride_entity>
  <code>entity::ride_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Посадить на существо\
**Тип:** Действие без значения\
**Описание:** Сажает существо на другое существо или игрока.

**Пример использования:** 
```ts
entity::ride_entity("name_or_uuid");
```

<h3 id=entity_set_absorption_health>
  <code>entity::set_absorption_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дополнительное здоровье\
**Тип:** Действие без значения\
**Описание:** Устанавливает дополнительное здоровье существа.

**Пример использования:** 
```ts
entity::set_absorption_health(1);
```

<h3 id=entity_set_ai>
  <code>entity::set_ai</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить интеллект сущности\
**Тип:** Действие без значения\
**Описание:** Устанавливает интеллект сущности.

**Пример использования:** 
```ts
entity::set_ai("TRUE");
```

<h3 id=entity_set_allay_dancing>
  <code>entity::set_allay_dancing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сделать Тихоню танцующим\
**Тип:** Действие без значения\
**Описание:** Заставляет Тихоню отображать анимацию танца.
**Работает с:**\
&nbsp;&nbsp;Тихонями

**Пример использования:** 
```ts
entity::set_allay_dancing("TRUE");
```

<h3 id=entity_set_angry>
  <code>entity::set_angry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим гнева\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу режим гнева на определённую цель.\
**Дополнительная информация:**\
&nbsp;&nbsp;Для корректной работы сущности необходима цель.\
**Работает с:**\
&nbsp;&nbsp;Пчёлами\
&nbsp;&nbsp;Волками\
&nbsp;&nbsp;Зомбифицированными пиглинами\
&nbsp;&nbsp;Эндерменами\
&nbsp;&nbsp;Мобами

**Пример использования:** 
```ts
entity::set_angry("TRUE","target");
```

<h3 id=entity_set_animal_age>
  <code>entity::set_animal_age</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить возраст животному\
**Тип:** Действие без значения\
**Описание:** Устанавливает возраст животному.

**Пример использования:** 
```ts
entity::set_animal_age(1,"ENABLE");
```

<h3 id=entity_set_armor_items>
  <code>entity::set_armor_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить броню\
**Тип:** Действие без значения\
**Описание:** Устанавливает броню сущности.

**Пример использования:** 
```ts
entity::set_armor_items(item("stick"),item("stick"),item("stick"),item("stick"));
```

<h3 id=entity_set_armor_stand_parts>
  <code>entity::set_armor_stand_parts</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить детали стойки для брони\
**Тип:** Действие без значения\
**Описание:** Установить детали стойки для брони.
**Работает с:**\
&nbsp;&nbsp;Стойками для брони

**Пример использования:** 
```ts
entity::set_armor_stand_parts("ENABLE","ENABLE");
```

<h3 id=entity_set_armor_stand_pose>
  <code>entity::set_armor_stand_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить позу стойки для брони\
**Тип:** Действие без значения\
**Описание:** Устанавливает позу стойки для брони.
**Работает с:**\
&nbsp;&nbsp;Стойками для брони

**Пример использования:** 
```ts
entity::set_armor_stand_pose(1,2,3,"HEAD");
```

<h3 id=entity_set_attribute>
  <code>entity::set_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить атрибут\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанный атрибут на указанное значение существу.

**Пример использования:** 
```ts
entity::set_attribute(1,"MAX_HEALTH");
```

<h3 id=entity_set_aware>
  <code>entity::set_aware</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить осведомлённость моба\
**Тип:** Действие без значения\
**Описание:** В выключенном состоянии отключает ИИ моба, но оставляет взаимодействие с гравитацией, толканием и т.д.
**Работает с:**\
&nbsp;&nbsp;Мобами

**Пример использования:** 
```ts
entity::set_aware("TRUE");
```

<h3 id=entity_set_axolotl_type>
  <code>entity::set_axolotl_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип аксолотля\
**Тип:** Действие без значения\
**Описание:** Устанавливает тип аксолотля.
**Работает с:**\
&nbsp;&nbsp;Аксолотлями

**Пример использования:** 
```ts
entity::set_axolotl_type("BLUE");
```

<h3 id=entity_set_baby>
  <code>entity::set_baby</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим ребёнка\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу режим ребёнка.

**Пример использования:** 
```ts
entity::set_baby("TRUE");
```

<h3 id=entity_set_bee_nectar>
  <code>entity::set_bee_nectar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить пыльцу пчеле\
**Тип:** Действие без значения\
**Описание:** Устанавливает видимость пыльцы пчеле.
**Работает с:**\
&nbsp;&nbsp;Пчёлами

**Пример использования:** 
```ts
entity::set_bee_nectar("TRUE");
```

<h3 id=entity_set_block_display_block>
  <code>entity::set_block_display_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить отображаемый блок\
**Тип:** Действие без значения\
**Описание:** Устанавливает отображаемый блок визуализатору блока.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами блока

**Пример использования:** 
```ts
entity::set_block_display_block(item("stone"));
```

<h3 id=entity_set_camel_dashing>
  <code>entity::set_camel_dashing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить анимацию рывка верблюду\
**Тип:** Действие без значения\
**Описание:** Устанавливает анимацию рывка верблюду.
**Работает с:**\
&nbsp;&nbsp;Верблюдами

**Пример использования:** 
```ts
entity::set_camel_dashing("TRUE");
```

<h3 id=entity_set_carrying_chest>
  <code>entity::set_carrying_chest</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить видимость сундука\
**Тип:** Действие без значения\
**Описание:** Устанавливает видимость сундука на сущности.
**Работает с:**\
&nbsp;&nbsp;Ослами\
&nbsp;&nbsp;Мулами\
&nbsp;&nbsp;Ламами

**Пример использования:** 
```ts
entity::set_carrying_chest("TRUE");
```

<h3 id=entity_set_cat_lying_down>
  <code>entity::set_cat_lying_down</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим лежания коту\
**Тип:** Действие без значения\
**Описание:** Устанавливает режим лежания коту.
**Работает с:**\
&nbsp;&nbsp;Котами

**Пример использования:** 
```ts
entity::set_cat_lying_down("TRUE");
```

<h3 id=entity_set_cat_type>
  <code>entity::set_cat_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип кота\
**Тип:** Действие без значения\
**Описание:** Устанавливает тип кота.
**Работает с:**\
&nbsp;&nbsp;Котами

**Пример использования:** 
```ts
entity::set_cat_type("ALL_BLACK");
```

<h3 id=entity_set_celebrating>
  <code>entity::set_celebrating</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим празднования\
**Тип:** Действие без значения\
**Описание:** Устанавливает режим празднования существу.
**Работает с:**\
&nbsp;&nbsp;Пиглинами\
&nbsp;&nbsp;Рейдерами

**Пример использования:** 
```ts
entity::set_celebrating("TRUE");
```

<h3 id=entity_set_collidable>
  <code>entity::set_collidable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим столкновения\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу режим столкновения с другими существами.

**Пример использования:** 
```ts
entity::set_collidable("TRUE");
```

<h3 id=entity_set_creeper_charge>
  <code>entity::set_creeper_charge</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить заряженность криперу\
**Тип:** Действие без значения\
**Описание:** Устанавливает, будет ли крипер заряженным.
**Работает с:**\
&nbsp;&nbsp;Криперами

**Пример использования:** 
```ts
entity::set_creeper_charge("TRUE");
```

<h3 id=entity_set_creeper_fuse>
  <code>entity::set_creeper_fuse</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить криперу время до взрыва\
**Тип:** Действие без значения\
**Описание:** Устанавливает криперу время до взрыва.
**Работает с:**\
&nbsp;&nbsp;Криперами

**Пример использования:** 
```ts
entity::set_creeper_fuse(1);
```

<h3 id=entity_set_current_health>
  <code>entity::set_current_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить здоровье существа\
**Тип:** Действие без значения\
**Описание:** Устанавливает здоровье существа на выбранное количество.

**Пример использования:** 
```ts
entity::set_current_health(1);
```

<h3 id=entity_set_custom_name>
  <code>entity::set_custom_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить имя\
**Тип:** Действие без значения\
**Описание:** Устанавливает имя для существа.

**Пример использования:** 
```ts
entity::set_custom_name("custom_name");
```

<h3 id=entity_set_custom_name_visibility>
  <code>entity::set_custom_name_visibility</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить видимость имени\
**Тип:** Действие без значения\
**Описание:** Устанавливает видимость имени существа.

**Пример использования:** 
```ts
entity::set_custom_name_visibility("TRUE");
```

<h3 id=entity_set_custom_tag>
  <code>entity::set_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить кастомный тег\
**Тип:** Действие без значения\
**Описание:** Устанавливает кастомный нбт-тег существу.

**Пример использования:** 
```ts
entity::set_custom_tag("name","value");
```

<h3 id=entity_set_death_drops>
  <code>entity::set_death_drops</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить выпадение предметов\
**Тип:** Действие без значения\
**Описание:** Устанавливает, будет ли выпадать лут с существа.

**Пример использования:** 
```ts
entity::set_death_drops("TRUE");
```

<h3 id=entity_set_death_time>
  <code>entity::set_death_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить длительность смерти\
**Тип:** Действие без значения\
**Описание:** Устанавливает длительность смерти для существа.

**Пример использования:** 
```ts
entity::set_death_time(1);
```

<h3 id=entity_set_despawning>
  <code>entity::set_despawning</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить пропадание существа\
**Тип:** Действие без значения\
**Описание:** Устанавливает, будет ли пропадать существо.

**Пример использования:** 
```ts
entity::set_despawning("TRUE");
```

<h3 id=entity_set_display_billboard>
  <code>entity::set_display_billboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим отображения\
**Тип:** Действие без значения\
**Описание:** Устанавливает режим отображения сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_billboard("CENTER");
```

<h3 id=entity_set_display_brightness>
  <code>entity::set_display_brightness</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить яркость\
**Тип:** Действие без значения\
**Описание:** Устанавливает яркость сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_brightness(1,2);
```

<h3 id=entity_set_display_culling_suze>
  <code>entity::set_display_culling_suze</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить размер области видимости\
**Тип:** Действие без значения\
**Описание:** Устанавливает размер области видимости модели сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_culling_suze(1,2);
```

<h3 id=entity_set_display_glow_color>
  <code>entity::set_display_glow_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет свечения\
**Тип:** Действие без значения\
**Описание:** Устанавливает цвет свечения сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами предмета\
&nbsp;&nbsp;Визуализаторами блока

**Пример использования:** 
```ts
entity::set_display_glow_color("color_hexadecimal");
```

<h3 id=entity_set_display_interpolation>
  <code>entity::set_display_interpolation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить интерполяцию\
**Тип:** Действие без значения\
**Описание:** Устанавливает длительность интерполяции сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_interpolation(1,2);
```

<h3 id=entity_set_display_rotation_from_axis_angle>
  <code>entity::set_display_rotation_from_axis_angle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить поворот по осевому вектору\
**Тип:** Действие без значения\
**Описание:** Устанавливает левый или правый поворот по осевому вектору и углу сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_rotation_from_axis_angle(vector(0,0,0),1,"SET","DEGREES","LEFT_ROTATION");
```

<h3 id=entity_set_display_rotation_from_euler_angles>
  <code>entity::set_display_rotation_from_euler_angles</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить поворот по углам Эйлера\
**Тип:** Действие без значения\
**Описание:** Устанавливает левый или правый поворот по углам Эйлера сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_rotation_from_euler_angles(1,2,3,"SET","DEGREES","LEFT_ROTATION");
```

<h3 id=entity_set_display_scale>
  <code>entity::set_display_scale</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить размер\
**Тип:** Действие без значения\
**Описание:** Устанавливает размер сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_scale(vector(0,0,0),"SET");
```

<h3 id=entity_set_display_shadow>
  <code>entity::set_display_shadow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить настройки тени\
**Тип:** Действие без значения\
**Описание:** Устанавливает размер и прозрачность тени сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_shadow(1,2);
```

<h3 id=entity_set_display_teleport_duration>
  <code>entity::set_display_teleport_duration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить длительность телепорта визуализатора\
**Тип:** Действие без значения\
**Описание:** Устанавливает длительность телепорта визуализатора.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_teleport_duration(1);
```

<h3 id=entity_set_display_transformation_matrix>
  <code>entity::set_display_transformation_matrix</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить матрицу преобразования\
**Тип:** Действие без значения\
**Описание:** Устанавливает матрицу преобразования (ряд-столбец) сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_transformation_matrix([1, 2]);
```

<h3 id=entity_set_display_translation>
  <code>entity::set_display_translation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить смещение\
**Тип:** Действие без значения\
**Описание:** Устанавливает смещение сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_translation(vector(0,0,0),"SET");
```

<h3 id=entity_set_display_view_range>
  <code>entity::set_display_view_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дальность видимости\
**Тип:** Действие без значения\
**Описание:** Устанавливает дальность видимости сущности-визуализатору.
**Работает с:**\
&nbsp;&nbsp;Любой сущностью-визуализатором

**Пример использования:** 
```ts
entity::set_display_view_range(1);
```

<h3 id=entity_set_dragon_phase>
  <code>entity::set_dragon_phase</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить фазу Эндер-дракона\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённую фазу Эндер-дракону.
**Работает с:**\
&nbsp;&nbsp;Эндер-драконами

**Пример использования:** 
```ts
entity::set_dragon_phase("BREATH_ATTACK");
```

<h3 id=entity_set_dye_color>
  <code>entity::set_dye_color</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет сущности\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённый цвет существу.
**Работает с:**\
&nbsp;&nbsp;Овцами\
&nbsp;&nbsp;Шалкерами\
&nbsp;&nbsp;Ошейниками собак\
&nbsp;&nbsp;Ошейниками котов

**Пример использования:** 
```ts
entity::set_dye_color("BLACK");
```

<h3 id=entity_set_end_crystal_beam>
  <code>entity::set_end_crystal_beam</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Указать луч кристалла Энда\
**Тип:** Действие без значения\
**Описание:** Указывает луч кристалла Энда на определённое местоположение.
**Работает с:**\
&nbsp;&nbsp;Кристаллами Энда

**Пример использования:** 
```ts
entity::set_end_crystal_beam(location(0,0,0,0,0));
```

<h3 id=entity_set_enderman_block>
  <code>entity::set_enderman_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить блок Эндермену\
**Тип:** Действие без значения\
**Описание:** Устанавливает отображаемый блок Эндермену.
**Работает с:**\
&nbsp;&nbsp;Эндерменами

**Пример использования:** 
```ts
entity::set_enderman_block(item("stone"));
```

<h3 id=entity_set_equipment_item>
  <code>entity::set_equipment_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить экипировку\
**Тип:** Действие без значения\
**Описание:** Устанавливает предметы в один из слотов экипировки (броня и предметы в руках) сущности.

**Пример использования:** 
```ts
entity::set_equipment_item(item("stick"),"CHEST");
```

<h3 id=entity_set_explosive_power>
  <code>entity::set_explosive_power</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить силу взрыва\
**Тип:** Действие без значения\
**Описание:** Устанавливает силу взрыва сущности.
**Работает с:**\
&nbsp;&nbsp;Криперами\
&nbsp;&nbsp;Динамитом\
&nbsp;&nbsp;Огненными шарами

**Пример использования:** 
```ts
entity::set_explosive_power(1);
```

<h3 id=entity_set_fall_distance>
  <code>entity::set_fall_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дистанцию падения\
**Тип:** Действие без значения\
**Описание:** Устанавливает дистанцию, с которой падает существо.

**Пример использования:** 
```ts
entity::set_fall_distance(1);
```

<h3 id=entity_set_falling_block_type>
  <code>entity::set_falling_block_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип существу Падающий блок\
**Тип:** Действие без значения\
**Описание:** Устанавливает новый тип блока существу Падающий блок.
**Работает с:**\
&nbsp;&nbsp;Падающими блоками

**Пример использования:** 
```ts
entity::set_falling_block_type(item("stone"));
```

<h3 id=entity_set_fire_ticks>
  <code>entity::set_fire_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Поджечь существо\
**Тип:** Действие без значения\
**Описание:** Поджигает существо на выбранное время.

**Пример использования:** 
```ts
entity::set_fire_ticks(1);
```

<h3 id=entity_set_fishing_wait>
  <code>entity::set_fishing_wait</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить задержку рыбалки\
**Тип:** Действие без значения\
**Описание:** Устанавливает задержку рыбалки существу в тиках.
**Работает с:**\
&nbsp;&nbsp;Поплавком удочки

**Пример использования:** 
```ts
entity::set_fishing_wait(1);
```

<h3 id=entity_set_fox_leaping>
  <code>entity::set_fox_leaping</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить анимацию прыжка лисе\
**Тип:** Действие без значения\
**Описание:** Устанавливает анимацию прыжка лисе.
**Работает с:**\
&nbsp;&nbsp;Лисами

**Пример использования:** 
```ts
entity::set_fox_leaping("TRUE");
```

<h3 id=entity_set_fox_type>
  <code>entity::set_fox_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип лисы\
**Тип:** Действие без значения\
**Описание:** Устанавливает тип лисы.
**Работает с:**\
&nbsp;&nbsp;Лисами

**Пример использования:** 
```ts
entity::set_fox_type("RED");
```

<h3 id=entity_set_freeze_ticks>
  <code>entity::set_freeze_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время заморозки\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу время заморозки (количество тиков, которое сущность провела в рыхлом снегу).

**Пример использования:** 
```ts
entity::set_freeze_ticks(1,"TRUE");
```

<h3 id=entity_set_frog_type>
  <code>entity::set_frog_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип жабы\
**Тип:** Действие без значения\
**Описание:** Устанавливает окрас жабы.
**Работает с:**\
&nbsp;&nbsp;Жабами

**Пример использования:** 
```ts
entity::set_frog_type("COLD");
```

<h3 id=entity_set_gliding>
  <code>entity::set_gliding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить полёт на элитрах\
**Тип:** Действие без значения\
**Описание:** Устанавливает для существа состояние полёта на элитрах.

**Пример использования:** 
```ts
entity::set_gliding("TRUE");
```

<h3 id=entity_set_glowing>
  <code>entity::set_glowing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить свечение сущности\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу эффект свечения.

**Пример использования:** 
```ts
entity::set_glowing("TRUE");
```

<h3 id=entity_set_glow_squid_dark>
  <code>entity::set_glow_squid_dark</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время тьмы спруту\
**Тип:** Действие без значения\
**Описание:** Устанавливает время тьмы в тиках светящемуся спруту.
**Работает с:**\
&nbsp;&nbsp;Светящимся спрутами

**Пример использования:** 
```ts
entity::set_glow_squid_dark(1);
```

<h3 id=entity_set_goat_screaming>
  <code>entity::set_goat_screaming</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить козла кричащим\
**Тип:** Действие без значения\
**Описание:** Устанавливает тег "кричащий" козлу.
**Работает с:**\
&nbsp;&nbsp;Козлами

**Пример использования:** 
```ts
entity::set_goat_screaming("TRUE");
```

<h3 id=entity_set_gravity>
  <code>entity::set_gravity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить гравитацию\
**Тип:** Действие без значения\
**Описание:** Устанавливает, будет ли сущность подчиняться гравитации.

**Пример использования:** 
```ts
entity::set_gravity("TRUE");
```

<h3 id=entity_set_horse_jump>
  <code>entity::set_horse_jump</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить лошади силу прыжка\
**Тип:** Действие без значения\
**Описание:** Устанавливает лошади силу прыжка.
**Работает с:**\
&nbsp;&nbsp;Лошадьми\
&nbsp;&nbsp;Ослами\
&nbsp;&nbsp;Мулами\
&nbsp;&nbsp;Ламами

**Пример использования:** 
```ts
entity::set_horse_jump(1);
```

<h3 id=entity_set_horse_pattern>
  <code>entity::set_horse_pattern</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить узор лошади\
**Тип:** Действие без значения\
**Описание:** Устанавливает окрас и узор лошади.
**Работает с:**\
&nbsp;&nbsp;Лошадьми

**Пример использования:** 
```ts
entity::set_horse_pattern("WHITE","NONE");
```

<h3 id=entity_set_immune_to_zombification>
  <code>entity::set_immune_to_zombification</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить иммунитет к зомбифицированию\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу иммунитет к зомбифицированию.
**Работает с:**\
&nbsp;&nbsp;Пиглинами\
&nbsp;&nbsp;Брутальными пиглинами\
&nbsp;&nbsp;Хоглинами

**Пример использования:** 
```ts
entity::set_immune_to_zombification("TRUE");
```

<h3 id=entity_set_interaction_responsive>
  <code>entity::set_interaction_responsive</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить отзывчивость сущности взаимодействия\
**Тип:** Действие без значения\
**Описание:** Устанавливает, будет ли сущность взаимодействия отзываться на взаимодействия.

**Пример использования:** 
```ts
entity::set_interaction_responsive("TRUE");
```

<h3 id=entity_set_interaction_size>
  <code>entity::set_interaction_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить размер сущности взаимодействия\
**Тип:** Действие без значения\
**Описание:** Устанавливает горизонтальный и вертикальный размеры сущности взаимодействия.

**Пример использования:** 
```ts
entity::set_interaction_size(1,2);
```

<h3 id=entity_set_invisible>
  <code>entity::set_invisible</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим невидимости\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу режим невидимости.

**Пример использования:** 
```ts
entity::set_invisible("TRUE");
```

<h3 id=entity_set_invulnerability_ticks>
  <code>entity::set_invulnerability_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить длительность неуязвимости\
**Тип:** Действие без значения\
**Описание:** Устанавливает длительность неуязвимости для существа.

**Пример использования:** 
```ts
entity::set_invulnerability_ticks(1);
```

<h3 id=entity_set_invulnerable>
  <code>entity::set_invulnerable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить неуязвимость сущности\
**Тип:** Действие без значения\
**Описание:** Устанавливает неуязвимости сущности, но в режиме креатива можно нанести урон.

**Пример использования:** 
```ts
entity::set_invulnerable("TRUE");
```

<h3 id=entity_set_item>
  <code>entity::set_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип существу Предмет\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённый тип (ID) существу Предмет.
**Работает с:**\
&nbsp;&nbsp;Предметами

**Пример использования:** 
```ts
entity::set_item(item("stick"));
```

<h3 id=entity_set_item_display_item>
  <code>entity::set_item_display_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить отображаемый предмет\
**Тип:** Действие без значения\
**Описание:** Устанавливает отображаемый предмет визуализатору предмета.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами предмета

**Пример использования:** 
```ts
entity::set_item_display_item(item("stick"));
```

<h3 id=entity_set_item_display_model_type>
  <code>entity::set_item_display_model_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип модели предмета\
**Тип:** Действие без значения\
**Описание:** Устанавливает тип отображаемой модели предмета визуализатору предмета.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами предмета

**Пример использования:** 
```ts
entity::set_item_display_model_type("FIRSTPERSON_LEFTHAND");
```

<h3 id=entity_set_item_in_frame>
  <code>entity::set_item_in_frame</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет в рамку\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанный предмет в рамку.
**Работает с:**\
&nbsp;&nbsp;Рамками

**Пример использования:** 
```ts
entity::set_item_in_frame(item("stick"));
```

<h3 id=entity_set_llama_type>
  <code>entity::set_llama_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет ламы\
**Тип:** Действие без значения\
**Описание:** Устанавливает цвет ламы.
**Работает с:**\
&nbsp;&nbsp;Ламами

**Пример использования:** 
```ts
entity::set_llama_type("BROWN");
```

<h3 id=entity_set_marker>
  <code>entity::set_marker</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим маркера\
**Тип:** Действие без значения\
**Описание:** Устанавливает режим маркера стойке для брони.
**Работает с:**\
&nbsp;&nbsp;Стойками для брони

**Пример использования:** 
```ts
entity::set_marker("TRUE");
```

<h3 id=entity_set_max_health>
  <code>entity::set_max_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить максимальное здоровье существа\
**Тип:** Действие без значения\
**Описание:** Устанавливает максимальное количество здоровья для существа.

**Пример использования:** 
```ts
entity::set_max_health(1,"TRUE");
```

<h3 id=entity_set_merchant_recipe>
  <code>entity::set_merchant_recipe</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить товар Жителю\
**Тип:** Действие без значения\
**Описание:** Устанавливает товар Жителю за определённые предметы по указанному индексу.
**Работает с:**\
&nbsp;&nbsp;Жителями\
&nbsp;&nbsp;Странствующими торговцами

**Пример использования:** 
```ts
entity::set_merchant_recipe(item("stick"),item("stick"),item("stick"),1,"MERGE",2,3,4,5,6,7,"TRUE","TRUE");
```

<h3 id=entity_set_minecart_block>
  <code>entity::set_minecart_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить блок в вагонетку\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанный блок в вагонетку.
**Работает с:**\
&nbsp;&nbsp;Вагонетками

**Пример использования:** 
```ts
entity::set_minecart_block(item("stone"),1);
```

<h3 id=entity_set_mob_aggressive>
  <code>entity::set_mob_aggressive</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить агрессивность\
**Тип:** Действие без значения\
**Описание:** Устанавливает агрессивность сущности.

**Пример использования:** 
```ts
entity::set_mob_aggressive("TRUE");
```

<h3 id=entity_set_mushroom_cow_type>
  <code>entity::set_mushroom_cow_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип грибной коровы\
**Тип:** Действие без значения\
**Описание:** Устанавливает тип грибной коровы.
**Работает с:**\
&nbsp;&nbsp;Грибными коровами

**Пример использования:** 
```ts
entity::set_mushroom_cow_type("BROWN");
```

<h3 id=entity_set_panda_gene>
  <code>entity::set_panda_gene</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить ген панды\
**Тип:** Действие без значения\
**Описание:** Устанавливает ген панды. Это влияет на их поведение и внешний вид.
**Работает с:**\
&nbsp;&nbsp;Пандами

**Пример использования:** 
```ts
entity::set_panda_gene("MAIN","NORMAL");
```

<h3 id=entity_set_parrot_type>
  <code>entity::set_parrot_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип попугая\
**Тип:** Действие без значения\
**Описание:** Устанавливает тип попугая.
**Работает с:**\
&nbsp;&nbsp;Попугаями

**Пример использования:** 
```ts
entity::set_parrot_type("BLUE");
```

<h3 id=entity_set_persistence>
  <code>entity::set_persistence</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить исчезание существа\
**Тип:** Действие без значения\
**Описание:** Устанавливает, будет ли предмет или падающий блок исчезать.
**Работает с:**\
&nbsp;&nbsp;Предметами\
&nbsp;&nbsp;Падающими блоками

**Пример использования:** 
```ts
entity::set_persistence("TRUE");
```

<h3 id=entity_set_pickup_delay>
  <code>entity::set_pickup_delay</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить задержку для поднятия\
**Тип:** Действие без значения\
**Описание:** Устанавливает количество тиков, за которое предмет не может быть поднят.
**Работает с:**\
&nbsp;&nbsp;Предметами

**Пример использования:** 
```ts
entity::set_pickup_delay(1);
```

<h3 id=entity_set_piglin_able_to_hunt>
  <code>entity::set_piglin_able_to_hunt</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить состояние охоты\
**Тип:** Действие без значения\
**Описание:** Устанавливает пиглину состояние охоты на хоглинов.
**Работает с:**\
&nbsp;&nbsp;Пиглинами

**Пример использования:** 
```ts
entity::set_piglin_able_to_hunt("TRUE");
```

<h3 id=entity_set_piglin_charging_crossbow>
  <code>entity::set_piglin_charging_crossbow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить состояние зарядки арбалета\
**Тип:** Действие без значения\
**Описание:** Устанавливает пиглину состояние зарядки арбалета.
**Работает с:**\
&nbsp;&nbsp;Пиглинами

**Пример использования:** 
```ts
entity::set_piglin_charging_crossbow("TRUE");
```

<h3 id=entity_set_piglin_dancing>
  <code>entity::set_piglin_dancing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стадию танца\
**Тип:** Действие без значения\
**Описание:** Устанавливает пиглину стадию танца на указанное время.\
**Дополнительная информация:**\
&nbsp;&nbsp;Если значение продолжительности меньше 0, то танец будет длиться бесконечно.\
**Работает с:**\
&nbsp;&nbsp;Пиглинами

**Пример использования:** 
```ts
entity::set_piglin_dancing(1);
```

<h3 id=entity_set_pose>
  <code>entity::set_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить позу сущности\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённую позу существу.

**Пример использования:** 
```ts
entity::set_pose("CROAKING");
```

<h3 id=entity_set_potion_cloud_radius>
  <code>entity::set_potion_cloud_radius</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить радиус облака эффекта\
**Тип:** Действие без значения\
**Описание:** Устанавливает радиус облака эффекта и скорость его расширения.
**Работает с:**\
&nbsp;&nbsp;Облаком эффекта

**Пример использования:** 
```ts
entity::set_potion_cloud_radius(1,2);
```

<h3 id=entity_set_primed_tnt_block>
  <code>entity::set_primed_tnt_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать зажженный динамит под блок\
**Тип:** Действие без значения\
**Описание:** Маскирует зажженный динамит под указанный блок.
**Работает с:**\
&nbsp;&nbsp;Зажженным динамитом

**Пример использования:** 
```ts
entity::set_primed_tnt_block(item("stone"));
```

<h3 id=entity_set_projectile_display_item>
  <code>entity::set_projectile_display_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет снаряда\
**Тип:** Действие без значения\
**Описание:** Устанавливает видимый предмет снаряду.

**Пример использования:** 
```ts
entity::set_projectile_display_item(item("stick"));
```

<h3 id=entity_set_projectile_shooter>
  <code>entity::set_projectile_shooter</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стрелка снаряду\
**Тип:** Действие без значения\
**Описание:** Устанавливает указанное существо как стрелка для снаряда.

**Пример использования:** 
```ts
entity::set_projectile_shooter("uuid");
```

<h3 id=entity_set_rabbit_type>
  <code>entity::set_rabbit_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тип кролика\
**Тип:** Действие без значения\
**Описание:** Устанавливает тип кролика.
**Работает с:**\
&nbsp;&nbsp;Кроликами

**Пример использования:** 
```ts
entity::set_rabbit_type("BLACK");
```

<h3 id=entity_set_rearing>
  <code>entity::set_rearing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить позу лошади\
**Тип:** Действие без значения\
**Описание:** Устанавливает, будет ли лошадь стоять на задних ногах.
**Работает с:**\
&nbsp;&nbsp;Лошадьми

**Пример использования:** 
```ts
entity::set_rearing("TRUE");
```

<h3 id=entity_set_riptiding>
  <code>entity::set_riptiding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить анимацию Тягун\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу анимацию использования зачарования трезубца Тягун.

**Пример использования:** 
```ts
entity::set_riptiding("TRUE");
```

<h3 id=entity_set_rotation>
  <code>entity::set_rotation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить поворот\
**Тип:** Действие без значения\
**Описание:** Устанавливает поворот сущности.

**Пример использования:** 
```ts
entity::set_rotation(1,2);
```

<h3 id=entity_set_rotation_by_vector>
  <code>entity::set_rotation_by_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить поворот по вектору\
**Тип:** Действие без значения\
**Описание:** Устанавливает поворот сущности по вектору.

**Пример использования:** 
```ts
entity::set_rotation_by_vector(vector(0,0,0));
```

<h3 id=entity_set_sheep_sheared>
  <code>entity::set_sheep_sheared</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить шерсть овце\
**Тип:** Действие без значения\
**Описание:** Устанавливает, будет ли шерсть на овце.
**Работает с:**\
&nbsp;&nbsp;Овцами

**Пример использования:** 
```ts
entity::set_sheep_sheared("TRUE");
```

<h3 id=entity_set_shulker_bullet_target>
  <code>entity::set_shulker_bullet_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цель снаряду Шалкера\
**Тип:** Действие без значения\
**Описание:** Устанавливает цель атаки снаряду Шалкера.
**Работает с:**\
&nbsp;&nbsp;Снарядами Шалкера

**Пример использования:** 
```ts
entity::set_shulker_bullet_target("target");
```

<h3 id=entity_set_silenced>
  <code>entity::set_silenced</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заглушить сущность\
**Тип:** Действие без значения\
**Описание:** Убирает звуки сущности.

**Пример использования:** 
```ts
entity::set_silenced("TRUE");
```

<h3 id=entity_set_sitting>
  <code>entity::set_sitting</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим сидения\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу режим сидения.
**Работает с:**\
&nbsp;&nbsp;Волками\
&nbsp;&nbsp;Котами\
&nbsp;&nbsp;Попугаями\
&nbsp;&nbsp;Лисами\
&nbsp;&nbsp;Пандами

**Пример использования:** 
```ts
entity::set_sitting("TRUE");
```

<h3 id=entity_set_size>
  <code>entity::set_size</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить размер существа\
**Тип:** Действие без значения\
**Описание:** Устанавливает размер существу.
**Работает с:**\
&nbsp;&nbsp;Слизнями\
&nbsp;&nbsp;Фантомами

**Пример использования:** 
```ts
entity::set_size(1);
```

<h3 id=entity_set_sniffer_state>
  <code>entity::set_sniffer_state</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить состояние нюхача\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённое состояние нюхачу.
**Работает с:**\
&nbsp;&nbsp;Нюхачами

**Пример использования:** 
```ts
entity::set_sniffer_state("DIGGING");
```

<h3 id=entity_set_snowman_pumpkin>
  <code>entity::set_snowman_pumpkin</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тыкву снеговику\
**Тип:** Действие без значения\
**Описание:** Устанавливает видимость тыквы снеговику.
**Работает с:**\
&nbsp;&nbsp;Снежными големами

**Пример использования:** 
```ts
entity::set_snowman_pumpkin("TRUE");
```

<h3 id=entity_set_tame>
  <code>entity::set_tame</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Приручить существо\
**Тип:** Действие без значения\
**Описание:** Устанавливает привязанность существа к указанному хозяину.
**Работает с:**\
&nbsp;&nbsp;Волками\
&nbsp;&nbsp;Котами\
&nbsp;&nbsp;Лошадьми\
&nbsp;&nbsp;Мулами\
&nbsp;&nbsp;Ламами\
&nbsp;&nbsp;Попугаями

**Пример использования:** 
```ts
entity::set_tame("name_or_uuid");
```

<h3 id=entity_set_target>
  <code>entity::set_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цель существу\
**Тип:** Действие без значения\
**Описание:** Инструктирует ИИ существа нацеливаться на определенное существо.\
**Дополнительная информация:**\
&nbsp;&nbsp;Оставьте пустой слот в поле Текст, чтобы убрать цель.\
**Работает с:**\
&nbsp;&nbsp;Мобами

**Пример использования:** 
```ts
entity::set_target("name_or_uuid");
```

<h3 id=entity_set_text_display_alignment>
  <code>entity::set_text_display_alignment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить выравнивание текста\
**Тип:** Действие без значения\
**Описание:** Устанавливает выравнивание текста визуализатору текста.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами текста

**Пример использования:** 
```ts
entity::set_text_display_alignment("CENTER");
```

<h3 id=entity_set_text_display_background>
  <code>entity::set_text_display_background</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цвет фона\
**Тип:** Действие без значения\
**Описание:** Устанавливает цвет и прозрачность фона визуализатору текста.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами текста

**Пример использования:** 
```ts
entity::set_text_display_background("color_hexadecimal",1);
```

<h3 id=entity_set_text_display_line_width>
  <code>entity::set_text_display_line_width</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить ширину строки\
**Тип:** Действие без значения\
**Описание:** Устанавливает максимальную ширину строки визуализатору текста.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами текста

**Пример использования:** 
```ts
entity::set_text_display_line_width(1);
```

<h3 id=entity_set_text_display_opacity>
  <code>entity::set_text_display_opacity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить прозрачность текста\
**Тип:** Действие без значения\
**Описание:** Устанавливает прозрачность текста визуализатору текста.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами текста

**Пример использования:** 
```ts
entity::set_text_display_opacity(1);
```

<h3 id=entity_set_text_display_see_through>
  <code>entity::set_text_display_see_through</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить видимость через блоки\
**Тип:** Действие без значения\
**Описание:** Устанавливает видимость текста через блоки визуализатору текста.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами текста

**Пример использования:** 
```ts
entity::set_text_display_see_through("TRUE");
```

<h3 id=entity_set_text_display_text>
  <code>entity::set_text_display_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить отображаемый текст\
**Тип:** Действие без значения\
**Описание:** Устанавливает отображаемый текст визуализатору текста.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами текста

**Пример использования:** 
```ts
entity::set_text_display_text(["displayed_text", "displayed_text"],"SPACES");
```

<h3 id=entity_set_text_display_text_shadow>
  <code>entity::set_text_display_text_shadow</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тень текста\
**Тип:** Действие без значения\
**Описание:** Устанавливает видимость тени текста визуализатору текста.
**Работает с:**\
&nbsp;&nbsp;Визуализаторами текста

**Пример использования:** 
```ts
entity::set_text_display_text_shadow("TRUE");
```

<h3 id=entity_set_tropical_fish_pattern>
  <code>entity::set_tropical_fish_pattern</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить узор рыбы\
**Тип:** Действие без значения\
**Описание:** Устанавливает окрас и узор тропической рыбе.
**Работает с:**\
&nbsp;&nbsp;Тропической рыбой

**Пример использования:** 
```ts
entity::set_tropical_fish_pattern("WHITE","WHITE","KOB");
```

<h3 id=entity_set_location>
  <code>entity::set_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить по вектору\
**Тип:** Действие без значения\
**Описание:** Запускает существо по указанному вектору.

**Пример использования:** 
```ts
entity::set_location(vector(0,0,0),"TRUE");
```

<h3 id=entity_set_vex_charging>
  <code>entity::set_vex_charging</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить Вредине злость\
**Тип:** Действие без значения\
**Описание:** Устанавливает Вредине стадию злости.
**Работает с:**\
&nbsp;&nbsp;Врединами

**Пример использования:** 
```ts
entity::set_vex_charging("TRUE");
```

<h3 id=entity_set_vex_limited_lifetime_ticks>
  <code>entity::set_vex_limited_lifetime_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время жизни Вредины\
**Тип:** Действие без значения\
**Описание:** Устанавливает время жизни Вредины в тиках.
**Работает с:**\
&nbsp;&nbsp;Врединами

**Пример использования:** 
```ts
entity::set_vex_limited_lifetime_ticks(1);
```

<h3 id=entity_set_villager_biome>
  <code>entity::set_villager_biome</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить биом жителю\
**Тип:** Действие без значения\
**Описание:** Устанавливает жителю окрас в зависимости от выбранного биома.
**Работает с:**\
&nbsp;&nbsp;Жителями

**Пример использования:** 
```ts
entity::set_villager_biome("DESERT");
```

<h3 id=entity_set_villager_experience>
  <code>entity::set_villager_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить опыт жителю\
**Тип:** Действие без значения\
**Описание:** Устанавливает жителю количество опыта.
**Работает с:**\
&nbsp;&nbsp;Жителями

**Пример использования:** 
```ts
entity::set_villager_experience(1);
```

<h3 id=entity_set_villager_profession>
  <code>entity::set_villager_profession</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить профессию жителю\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённую профессию жителю.
**Работает с:**\
&nbsp;&nbsp;Жителями\
&nbsp;&nbsp;Зомби-жителями

**Пример использования:** 
```ts
entity::set_villager_profession("NONE");
```

<h3 id=entity_set_visual_fire>
  <code>entity::set_visual_fire</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отображать огонь\
**Тип:** Действие без значения\
**Описание:** Отображает огонь на существе.

**Пример использования:** 
```ts
entity::set_visual_fire("TRUE");
```

<h3 id=entity_set_warden_anger_level>
  <code>entity::set_warden_anger_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить уровень гнева Хранителя\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённый уровень гнева Хранителя на указанное существо.\
**Дополнительная информация:**\
&nbsp;&nbsp;Если уровень гнева на сущность достигает 80, Хранитель начинает активно преследовать её.\
**Работает с:**\
&nbsp;&nbsp;Хранителями

**Пример использования:** 
```ts
entity::set_warden_anger_level("name_or_uuid",1);
```

<h3 id=entity_set_warden_digging>
  <code>entity::set_warden_digging</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** None\
**Тип:** Действие без значения\
**Описание:** None

**Пример использования:** 
```ts
entity::set_warden_digging("EMERGE");
```

<h3 id=entity_set_wearing_saddle>
  <code>entity::set_wearing_saddle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить видимость седла\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу седло.
**Работает с:**\
&nbsp;&nbsp;Свиньями\
&nbsp;&nbsp;Лошадьми\
&nbsp;&nbsp;Лавомерками

**Пример использования:** 
```ts
entity::set_wearing_saddle("TRUE");
```

<h3 id=entity_set_wither_invulnerability_ticks>
  <code>entity::set_wither_invulnerability_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить неуязвимость иссушителю\
**Тип:** Действие без значения\
**Описание:** Устанавливает длительность неуязвимости иссушителю.
**Работает с:**\
&nbsp;&nbsp;Иссушителем

**Пример использования:** 
```ts
entity::set_wither_invulnerability_ticks(1);
```

<h3 id=entity_set_zombie_arms_raised>
  <code>entity::set_zombie_arms_raised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить поднятие рук зомби\
**Тип:** Действие без значения\
**Описание:** Устанавливает анимацию поднятия рук для зомби.

**Пример использования:** 
```ts
entity::set_zombie_arms_raised("TRUE");
```

<h3 id=entity_shear_sheep>
  <code>entity::shear_sheep</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Подстричь овцу\
**Тип:** Действие без значения\
**Описание:** Подстригает овцу.
**Работает с:**\
&nbsp;&nbsp;Овцами

**Пример использования:** 
```ts
entity::shear_sheep();
```

<h3 id=entity_sleep>
  <code>entity::sleep</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить анимацию сна\
**Тип:** Действие без значения\
**Описание:** Устанавливает существу анимацию сна. Лучше всего использовать это действие в цикле.
**Работает с:**\
&nbsp;&nbsp;Лисами

**Пример использования:** 
```ts
entity::sleep("TRUE");
```

<h3 id=entity_swing_hand>
  <code>entity::swing_hand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проиграть анимацию взмаха руки\
**Тип:** Действие без значения\
**Описание:** Проигрывает для сущности анимацию взмаха руки.

**Пример использования:** 
```ts
entity::swing_hand("MAIN");
```

<h3 id=entity_teleport>
  <code>entity::teleport</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Телепортация\
**Тип:** Действие без значения\
**Описание:** Телепортирует существо в выбранное местоположение.

**Пример использования:** 
```ts
entity::teleport(location(0,0,0,0,0),"TRUE");
```

<h3 id=entity_use_item>
  <code>entity::use_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Использовать предмет\
**Тип:** Действие без значения\
**Описание:** Инструктирует ИИ существа на использование предмета в его руке.
**Работает с:**\
&nbsp;&nbsp;Мобами

**Пример использования:** 
```ts
entity::use_item("MAIN_HAND","TRUE");
```

<h3 id=if_entity_collides_at_location>
  <code>entity::collides_at_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сталкивается на местоположении\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, сталкивается ли сущность с блоками, шалкерами, лодками и границей мира на указанном местоположении.

**Пример использования:** 
```ts
if(entity::collides_at_location(location(0,0,0,0,0)){
    player::message("Условие верно");
}
```

<h3 id=if_entity_collides_using_hitbox>
  <code>entity::collides_using_hitbox</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сталкивается используя кастомный хитбокс\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, сталкивается ли сущность с блоками, шалкерами, лодками и границей мира используя кастомный хитбокс.

**Пример использования:** 
```ts
if(entity::collides_using_hitbox(location(0,0,0,0,0),location(0,0,0,0,0)){
    player::message("Условие верно");
}
```

<h3 id=if_entity_collides_with_entity>
  <code>entity::collides_with_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сталкивается с сущностью\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, сталкивается ли хитбокс сущности с хитбоксом другой указанной сущности.

**Пример использования:** 
```ts
if(entity::collides_with_entity("name_or_uuid","OVERLAPS"){
    player::message("Условие верно");
}
```

<h3 id=if_entity_exists>
  <code>entity::exists</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Существует\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли существо в мире.

**Пример использования:** 
```ts
if(entity::exists(){
    player::message("Условие верно");
}
```

<h3 id=if_entity_has_custom_tag>
  <code>entity::has_custom_tag</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имеет кастомный тег\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли существо кастомный тег с указанным значением.

**Пример использования:** 
```ts
if(entity::has_custom_tag("tag","tag_value"){
    player::message("Условие верно");
}
```

<h3 id=if_entity_has_potion_effect>
  <code>entity::has_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имеет эффект от зелья\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли существо эффект от зелья.

**Пример использования:** 
```ts
if(entity::has_potion_effect([potion("slow_falling"), potion("slow_falling")],"ANY"){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_disguised>
  <code>entity::is_disguised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскирована\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, замаскирована ли сущность.

**Пример использования:** 
```ts
if(entity::is_disguised(){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_grounded>
  <code>entity::is_grounded</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Касается поверхности блока\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, касается ли существо поверхности блока.

**Пример использования:** 
```ts
if(entity::is_grounded(){
    player::message("Условие верно");
}
```

<h3 id=if_entity_in_area>
  <code>entity::in_area</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Внутри региона\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли сущность в определённом регионе.

**Пример использования:** 
```ts
if(entity::in_area(location(0,0,0,0,0),location(0,0,0,0,0),"TRUE","POINT","OVERLAPS"){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_item>
  <code>entity::is_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Является предметом\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, является ли существо предметом.

**Пример использования:** 
```ts
if(entity::is_item(){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_mob>
  <code>entity::is_mob</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Является мобом\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, является ли существо мобом.

**Пример использования:** 
```ts
if(entity::is_mob(){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_near_location>
  <code>entity::is_near_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Рядом с местоположением\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли существо рядом с указанным местоположением.

**Пример использования:** 
```ts
if(entity::is_near_location("TRUE",location(0,0,0,0,0),1){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_projectile>
  <code>entity::is_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Является снарядом\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, является ли существо снарядом.

**Пример использования:** 
```ts
if(entity::is_projectile(){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_riding_entity>
  <code>entity::is_riding_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сущность оседлала сущность\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, оседлала ли сущность любую из других указанных сущностей.

**Пример использования:** 
```ts
if(entity::is_riding_entity(["entity_ids", "entity_ids"],"NEAREST"){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_standing_on_block>
  <code>entity::is_standing_on_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Стоит на блоке\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, стоит ли сущность на блоке определенном блоке или местоположении.

**Пример использования:** 
```ts
if(entity::is_standing_on_block([item("stone"), item("stone")],[location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE"){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_type>
  <code>entity::is_type</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Тип существа равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли тип существа типу в сундуке.

**Пример использования:** 
```ts
if(entity::is_type([item("stick"), item("stick")]){
    player::message("Условие верно");
}
```

<h3 id=if_entity_is_vehicle>
  <code>entity::is_vehicle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Является транспортом\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, является ли существо транспортом.

**Пример использования:** 
```ts
if(entity::is_vehicle(){
    player::message("Условие верно");
}
```

<h3 id=if_entity_name_equals>
  <code>entity::name_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имя равно\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равно ли имя существа имени в сундуке.

**Пример использования:** 
```ts
if(entity::name_equals(["names_or_uuids", "names_or_uuids"]){
    player::message("Условие верно");
}
```

<h3 id=if_entity_spawn_reason_equals>
  <code>entity::spawn_reason_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Причина появления равна\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равна ли причина появления существа определённому значению.

**Пример использования:** 
```ts
if(entity::spawn_reason_equals("BEEHIVE"){
    player::message("Условие верно");
}
```

