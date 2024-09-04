<h2 id=player>
  <code>player</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

### Селекторы

| **Имя**            | **Описание**       |
|--------------------| -------------------|
| `<current>`        | Текущая цель       |
| `<default_player>` | Игрок по умолчанию |
| `<killer_player>`  | Убийца             |
| `<damager_player>` | Атакующий          |
| `<shooter_player>` | Стрелок            |
| `<victim_player>`  | Жертва             |
| `<random_player>`  | Случайный игрок    |
| `<all_players>`    | Все игроки         |

<h3 id=if_player_chat_message_equals>
  <code>player::chat_message_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сообщение равно\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равно ли сообщение игрока выбранному.

**Пример использования:** 
```ts
if(player::chat_message_equals(["chat_messages", "chat_messages"]){
    player::message("Условие верно");
}
```

<h3 id=if_player_collides_at_location>
  <code>player::collides_at_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сталкивается на местоположении\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, сталкивается ли игрок с блоками, шалкерами, лодками и границей мира на указанном местоположении.

**Пример использования:** 
```ts
if(player::collides_at_location(location(0,0,0,0,0)){
    player::message("Условие верно");
}
```

<h3 id=if_player_collides_using_hitbox>
  <code>player::collides_using_hitbox</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сталкивается используя кастомный хитбокс\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, сталкивается ли игрок с блоками, шалкерами, лодками и границей мира используя кастомный хитбокс.

**Пример использования:** 
```ts
if(player::collides_using_hitbox(location(0,0,0,0,0),location(0,0,0,0,0)){
    player::message("Условие верно");
}
```

<h3 id=if_player_collides_with_entity>
  <code>player::collides_with_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сталкивается с сущностью\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, сталкивается ли хитбокс игрока с хитбоксом указанной сущности.

**Пример использования:** 
```ts
if(player::collides_with_entity("name_or_uuid","OVERLAPS"){
    player::message("Условие верно");
}
```

<h3 id=if_player_cursor_item_equals>
  <code>player::cursor_item_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет на курсоре равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли предмет, находящийся на курсоре игрока, выбранному предмету.

**Пример использования:** 
```ts
if(player::cursor_item_equals([item("stick"), item("stick")],"EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_gamemode_equals>
  <code>player::gamemode_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Режим игры равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равен ли режим игры игрока выбранному.

**Пример использования:** 
```ts
if(player::gamemode_equals("SURVIVAL"){
    player::message("Условие верно");
}
```

<h3 id=if_player_has_item>
  <code>player::has_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имеет предмет\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли игрок предмет в своем инвентаре.

**Пример использования:** 
```ts
if(player::has_item([item("stick"), item("stick")],"ANY","EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_has_item_at_least>
  <code>player::has_item_at_least</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имеет предмет в количестве\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли игрок предмет в определенном количестве.

**Пример использования:** 
```ts
if(player::has_item_at_least(item("stick"),1,"EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_has_item_in_slot>
  <code>player::has_item_in_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имеет предмет в слоте\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли игрок предмет в определенном слоте инвентаря.

**Пример использования:** 
```ts
if(player::has_item_in_slot([item("stick"), item("stick")],[1, 2],"EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_has_potion_effect>
  <code>player::has_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имеет эффект от зелья\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли игрок эффект от зелья.

**Пример использования:** 
```ts
if(player::has_potion_effect([potion("slow_falling"), potion("slow_falling")],"ANY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_has_privilege>
  <code>player::has_privilege</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имеет права\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли игрок определённые права в мире.\
**Дополнительная информация:**\
&nbsp;&nbsp;При включённом маркере "Точность проверки", проверка на права строительства и разработки будет осуществлятся, даже если игрок добавлен в белый список.

**Пример использования:** 
```ts
if(player::has_privilege("BUILDER","TRUE"){
    player::message("Условие верно");
}
```

<h3 id=if_player_has_room_for_item>
  <code>player::has_room_for_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имеет место для предметов\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли игрок в своем инвентаре место для одного или нескольких предметов.

**Пример использования:** 
```ts
if(player::has_room_for_item([item("stick"), item("stick")],"ANY","ENTIRE_INVENTORY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_hotbar_slot_equals>
  <code>player::hotbar_slot_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Слот в хот-баре равен\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, совпадает ли текущий слот хот-бара игрока со слотом от 1 до 9 в сундуке.

**Пример использования:** 
```ts
if(player::hotbar_slot_equals(1){
    player::message("Условие верно");
}
```

<h3 id=if_player_inventory_menu_slot_equals>
  <code>player::inventory_menu_slot_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Слот в инвентаре содержит\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, содержит ли сейчас игрок с открытым инвентарем определенный предмет в слоте.

**Пример использования:** 
```ts
if(player::inventory_menu_slot_equals([item("stick"), item("stick")],[1, 2],"EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_inventory_type_open>
  <code>player::inventory_type_open</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Открыт инвентарь типа\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, открыт ли инвентарь определенного типа у игрока.

**Пример использования:** 
```ts
if(player::inventory_type_open("CHEST"){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_blocking>
  <code>player::is_blocking</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Использует щит\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, использует ли игрок щит.

**Пример использования:** 
```ts
if(player::is_blocking(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_disguised>
  <code>player::is_disguised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскирован для всех\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, замаскирован ли игрок для остальных игроков.

**Пример использования:** 
```ts
if(player::is_disguised(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_flying>
  <code>player::is_flying</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Летит\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, летит ли игрок.

**Пример использования:** 
```ts
if(player::is_flying(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_gliding>
  <code>player::is_gliding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Парит\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, парит ли игрок на элитрах.

**Пример использования:** 
```ts
if(player::is_gliding(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_holding>
  <code>player::holding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Держит предмет\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, держит ли игрок предмет в своих руках.

**Пример использования:** 
```ts
if(player::holding([item("stick"), item("stick")],"EITHER_HAND","EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_in_area>
  <code>player::in_area</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Внутри региона\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли игрок в определённом регионе.

**Пример использования:** 
```ts
if(player::in_area(location(0,0,0,0,0),location(0,0,0,0,0),"TRUE","POINT","OVERLAPS"){
    player::message("Условие верно");
}
```

<h3 id=if_player_item_is_not_on_cooldown>
  <code>player::item_is_not_on_cooldown</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Предмет не имеет задержку\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, не имеет ли предмет у игрока задержку, применимую к определенному типу предметов.

**Пример использования:** 
```ts
if(player::item_is_not_on_cooldown([item("stick"), item("stick")]){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_looking_at_block>
  <code>player::is_looking_at_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Смотрит на блок\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, смотрит ли игрок на определенный блок или местоположение.

**Пример использования:** 
```ts
if(player::is_looking_at_block([item("stone"), item("stone")],[location(0,0,0,0,0), location(0,0,0,0,0)],1,"NEVER"){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_near>
  <code>player::is_near</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Рядом с местоположением\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, находится ли игрок рядом с указанным местоположением (По умолчанию: 5 блоков).

**Пример использования:** 
```ts
if(player::is_near("TRUE",location(0,0,0,0,0),1){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_on_ground>
  <code>player::is_on_ground</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Стоит на земле\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, не находится ли игрок в воздухе.

**Пример использования:** 
```ts
if(player::is_on_ground(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_online_mode>
  <code>player::is_online_mode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имеет лицензионный аккаунт\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, имеет ли игрок лицензионный аккаунт.

**Пример использования:** 
```ts
if(player::is_online_mode(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_riding_entity>
  <code>player::is_riding_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Оседлал существо\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, оседлал ли игрок существо (включая транспорт).

**Пример использования:** 
```ts
if(player::is_riding_entity(["entity_ids", "entity_ids"],"NEAREST"){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_self_disguised>
  <code>player::is_self_disguised</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскирован для себя\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, замаскирован ли игрок для себя.

**Пример использования:** 
```ts
if(player::is_self_disguised(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_sleeping>
  <code>player::is_sleeping</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Спит\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, спит ли игрок.

**Пример использования:** 
```ts
if(player::is_sleeping(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_sneaking>
  <code>player::is_sneaking</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Крадется\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, крадется ли игрок.

**Пример использования:** 
```ts
if(player::is_sneaking(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_sprinting>
  <code>player::is_sprinting</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Бежит\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, бежит ли игрок или использует клавишу бега при плавании.

**Пример использования:** 
```ts
if(player::is_sprinting(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_standing_on_block>
  <code>player::is_standing_on_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Стоит на блоке\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, стоит ли игрок на блоке определенном блоке или местоположении.

**Пример использования:** 
```ts
if(player::is_standing_on_block([item("stone"), item("stone")],[location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE"){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_swimming>
  <code>player::is_swimming</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Плавает\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, плавает ли игрок в воде или лаве.

**Пример использования:** 
```ts
if(player::is_swimming(){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_using_item>
  <code>player::is_using_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Использует предмет\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, использует ли игрок лук, щит или любой другой предмет, который возможно использовать.

**Пример использования:** 
```ts
if(player::is_using_item([item("stick"), item("stick")],"EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_is_wearing_item>
  <code>player::is_wearing_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Одет в предмет\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, одет ли игрок в предмет.

**Пример использования:** 
```ts
if(player::is_wearing_item([item("stick"), item("stick")],"ANY","EXACTLY"){
    player::message("Условие верно");
}
```

<h3 id=if_player_name_equals>
  <code>player::name_equals</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Имя равно\
**Тип:** Действие, проверяющее условие\
**Описание:** Проверяет, равно ли имя игрока имени в сундуке.

**Пример использования:** 
```ts
if(player::name_equals(["names_or_uuids", "names_or_uuids"]){
    player::message("Условие верно");
}
```

<h3 id=player_add_inventory_menu_row>
  <code>player::add_inventory_menu_row</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Добавить строку меню\
**Тип:** Действие без значения\
**Описание:** Добавляет строку с указанными предметами в инвентаре типа "Сундук".

**Пример использования:** 
```ts
player::add_inventory_menu_row([item("stick"), item("stick")],"TOP");
```

<h3 id=player_allow_placing_breaking_blocks>
  <code>player::allow_placing_breaking_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** None\
**Тип:** Действие без значения\
**Описание:** None

**Пример использования:** 
```ts
player::allow_placing_breaking_blocks("TRUE",[item("stone"), item("stone")]);
```

<h3 id=player_boost_elytra>
  <code>player::boost_elytra</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Ускорить полёт на Элитрах\
**Тип:** Действие без значения\
**Описание:** Ускоряет полёт игрока на Элитрах с силой указанного фейерверка.

**Пример использования:** 
```ts
player::boost_elytra(item("stick"));
```

<h3 id=player_clear_chat>
  <code>player::clear_chat</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить чат\
**Тип:** Действие без значения\
**Описание:** Удаляет все сообщения из окна чата выбранных игроков.

**Пример использования:** 
```ts
player::clear_chat();
```

<h3 id=player_clear_debug_markers>
  <code>player::clear_debug_markers</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить отладочные маркеры\
**Тип:** Действие без значения\
**Описание:** Удаляет все отладочные маркеры для игрока.

**Пример использования:** 
```ts
player::clear_debug_markers();
```

<h3 id=player_clear_ender_chest_contents>
  <code>player::clear_ender_chest_contents</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить содержимое Эндер-сундука\
**Тип:** Действие без значения\
**Описание:** Очищает предметы в инвентаре Эндер-сундука игрока.

**Пример использования:** 
```ts
player::clear_ender_chest_contents();
```

<h3 id=player_clear_inventory>
  <code>player::clear_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить инвентарь\
**Тип:** Действие без значения\
**Описание:** Очищает инвентарь игрока.

**Пример использования:** 
```ts
player::clear_inventory("ENTIRE");
```

<h3 id=player_clear_items>
  <code>player::clear_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить предметы\
**Тип:** Действие без значения\
**Описание:** Удаляет все выбранные предметы из инвентаря игрока.

**Пример использования:** 
```ts
player::clear_items([item("stick"), item("stick")]);
```

<h3 id=player_clear_potion_effects>
  <code>player::clear_potion_effects</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Очистить эффекты\
**Тип:** Действие без значения\
**Описание:** Очищает все эффекты у игрока.

**Пример использования:** 
```ts
player::clear_potion_effects();
```

<h3 id=player_close_inventory>
  <code>player::close_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Закрыть меню\
**Тип:** Действие без значения\
**Описание:** Закрывает открытое инвентарное меню игрока.

**Пример использования:** 
```ts
player::close_inventory();
```

<h3 id=player_damage>
  <code>player::damage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Нанести урон\
**Тип:** Действие без значения\
**Описание:** Наносит урон игроку.

**Пример использования:** 
```ts
player::damage(1,"source");
```

<h3 id=player_disguise_as_block>
  <code>player::disguise_as_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать игрока под блок\
**Тип:** Действие без значения\
**Описание:** Маскирует игрока под выбранный блок.

**Пример использования:** 
```ts
player::disguise_as_block(item("stone"),"TRUE");
```

<h3 id=player_disguise_as_entity>
  <code>player::disguise_as_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать игрока под сущность\
**Тип:** Действие без значения\
**Описание:** Маскирует игрока под выбранную сущность.

**Пример использования:** 
```ts
player::disguise_as_entity(item("stick"),"TRUE");
```

<h3 id=player_disguise_as_item>
  <code>player::disguise_as_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать игрока под предмет\
**Тип:** Действие без значения\
**Описание:** Маскирует игрока под предмет.

**Пример использования:** 
```ts
player::disguise_as_item(item("stick"),"TRUE");
```

<h3 id=player_display_bell_ring>
  <code>player::display_bell_ring</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать удар в колокол\
**Тип:** Действие без значения\
**Описание:** Показывает игроку анимацию удара в колокол, не влияя на других игроков.\
**Дополнительная информация:**\
&nbsp;&nbsp;Направление "Вниз (down)" останавливает анимацию удара.\
**Работает с:**\
&nbsp;&nbsp;Колоколами

**Пример использования:** 
```ts
player::display_bell_ring(location(0,0,0,0,0),"DOWN");

#Или от объекта

location(0,0,0,0,0).display_bell_ring("DOWN");
```

<h3 id=player_display_block>
  <code>player::display_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать блок\
**Тип:** Действие без значения\
**Описание:** Показать игроку блок, не влияя на других игроков.

**Пример использования:** 
```ts
player::display_block([location(0,0,0,0,0), location(0,0,0,0,0)],item("stone"));
```

<h3 id=player_set_block_opened_state>
  <code>player::set_block_opened_state</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Открыть/Закрыть блок\
**Тип:** Действие без значения\
**Описание:** Отобразить игроку закрытие/открытие блока не меняя состояния блока для других игроков.
**Работает с:**\
&nbsp;&nbsp;Сундуком\
&nbsp;&nbsp;Сундуком-ловушкой\
&nbsp;&nbsp;Эндер-сундуком\
&nbsp;&nbsp;Шалкеровым ящиком\
&nbsp;&nbsp;Бочкой

**Пример использования:** 
```ts
player::set_block_opened_state(location(0,0,0,0,0),"TRUE");
```

<h3 id=player_display_end_gateway_beam>
  <code>player::display_end_gateway_beam</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать анимацию луча Врат Энда\
**Тип:** Действие без значения\
**Описание:** Показывает анимацию луча Врат Энда на определённом местоположении.

**Пример использования:** 
```ts
player::display_end_gateway_beam(location(0,0,0,0,0),"LIGHT_PURPLE");
```

<h3 id=player_display_hologram>
  <code>player::display_hologram</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать голограмму\
**Тип:** Действие без значения\
**Описание:** Показывает игроку голограмму. Чтобы удалить голограмму на местоположении, оставьте текст пустым.\
**Дополнительная информация:**\
&nbsp;&nbsp;Чтобы перенести текст на новую строку, используйте символы "n", к примеру: "Строка1nСтрока2".

**Пример использования:** 
```ts
player::display_hologram(location(0,0,0,0,0),"text");
```

<h3 id=player_display_lightning>
  <code>player::display_lightning</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить эффект молнии\
**Тип:** Действие без значения\
**Описание:** Отобразить молнию игроку, не показывая её для других игроков и не поджигая местность.

**Пример использования:** 
```ts
player::display_lightning(location(0,0,0,0,0));
```

<h3 id=player_display_particle>
  <code>player::display_particle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить эффект частицы\
**Тип:** Действие без значения\
**Описание:** Отображает игроку эффект частицы на выбранном местоположении.

**Пример использования:** 
```ts
player::display_particle([particle("fire"), particle("fire")],[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

<h3 id=player_display_particle_circle>
  <code>player::display_particle_circle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить окружность частиц\
**Тип:** Действие без значения\
**Описание:** Отображает игроку окружность из эффекта частиц с указанными параметрами.

**Пример использования:** 
```ts
player::display_particle_circle(particle("fire"),location(0,0,0,0,0),1,2,3,vector(0,0,0),"DEGREES");
```

<h3 id=player_display_particle_cube>
  <code>player::display_particle_cube</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить куб частиц\
**Тип:** Действие без значения\
**Описание:** Отображает игроку куб из эффекта частиц с указанными параметрами.

**Пример использования:** 
```ts
player::display_particle_cube(particle("fire"),location(0,0,0,0,0),location(0,0,0,0,0),1,"SOLID");
```

<h3 id=player_display_particle_line>
  <code>player::display_particle_line</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить линию частиц\
**Тип:** Действие без значения\
**Описание:** Отображает игроку линию эффекта частиц от начального местоположения до конечного с определённым расстоянием.

**Пример использования:** 
```ts
player::display_particle_line(particle("fire"),location(0,0,0,0,0),location(0,0,0,0,0),1,"POINTS");
```

<h3 id=player_display_particle_ray>
  <code>player::display_particle_ray</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить луч частиц\
**Тип:** Действие без значения\
**Описание:** Отображает игроку луч эффекта частиц от начального местоположения по указанному вектору с определённым расстоянием.

**Пример использования:** 
```ts
player::display_particle_ray(particle("fire"),location(0,0,0,0,0),vector(0,0,0),1,"POINTS");
```

<h3 id=player_display_particle_sphere>
  <code>player::display_particle_sphere</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить сферу частиц\
**Тип:** Действие без значения\
**Описание:** Отображает игроку сферу из эффекта частиц с указанными параметрами.

**Пример использования:** 
```ts
player::display_particle_sphere(particle("fire"),location(0,0,0,0,0),1,2);
```

<h3 id=player_display_particle_spiral>
  <code>player::display_particle_spiral</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить спираль частиц\
**Тип:** Действие без значения\
**Описание:** Отображает игроку спираль из эффекта частиц с указанными параметрами.

**Пример использования:** 
```ts
player::display_particle_spiral(particle("fire"),location(0,0,0,0,0),1,2,3,4,5,"DEGREES");
```

<h3 id=player_display_pick_up_animation>
  <code>player::display_pick_up_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать анимацию подбора предмета\
**Тип:** Действие без значения\
**Описание:** Показывает игроку анимацию подбора предмета.\
**Дополнительная информация:**\
&nbsp;&nbsp;Действие работает с любой сущностью, в том числе игроком.

**Пример использования:** 
```ts
player::display_pick_up_animation("collected_name_or_uuid","collector_name_or_uuid",1);
```

<h3 id=player_display_sign_text>
  <code>player::display_sign_text</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать текст таблички\
**Тип:** Действие без значения\
**Описание:** Показать игроку изменение текста таблички, не изменяя её текст для других игроков.

**Пример использования:** 
```ts
player::display_sign_text(location(0,0,0,0,0),"line_1","line_2","line_3","line_4");
```

<h3 id=player_display_vibration>
  <code>player::display_vibration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отобразить частицу вибрации\
**Тип:** Действие без значения\
**Описание:** Отображает игроку частицу вибрации движущуюся с одной точки на другую.

**Пример использования:** 
```ts
player::display_vibration(location(0,0,0,0,0),location(0,0,0,0,0),1);
```

<h3 id=player_expand_inventory_menu>
  <code>player::expand_inventory_menu</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Расширить меню\
**Тип:** Действие без значения\
**Описание:** Расширяет открытое инвентарное меню игрока на выбранное количество строк и заполняет его указанными предметами.

**Пример использования:** 
```ts
player::expand_inventory_menu([item("stick"), item("stick")],1);
```

<h3 id=player_face_location>
  <code>player::face_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Повернуть к местоположению\
**Тип:** Действие без значения\
**Описание:** Поворачивает игрока в сторону к местоположению.

**Пример использования:** 
```ts
player::face_location(location(0,0,0,0,0));
```

<h3 id=player_force_flight_mode>
  <code>player::force_flight_mode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** None\
**Тип:** Действие без значения\
**Описание:** None

**Пример использования:** 
```ts
player::force_flight_mode("TRUE");
```

<h3 id=player_give_experience>
  <code>player::give_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Прибавить уровень\
**Тип:** Действие без значения\
**Описание:** Прибавляет уровень игроку.

**Пример использования:** 
```ts
player::give_experience(1,"POINTS");
```

<h3 id=player_give_items>
  <code>player::give_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выдать предмет\
**Тип:** Действие без значения\
**Описание:** Выдает игроку предметы из сундука.

**Пример использования:** 
```ts
player::give_items([item("stick"), item("stick")],1);
```

<h3 id=player_give_potion_effect>
  <code>player::give_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выдать эффект\
**Тип:** Действие без значения\
**Описание:** Выдаёт выбранные эффекты игроку.

**Пример использования:** 
```ts
player::give_potion_effect([potion("slow_falling"), potion("slow_falling")],"TRUE","TRUE","REGULAR");
```

<h3 id=player_give_random_item>
  <code>player::give_random_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выдать случайный предмет\
**Тип:** Действие без значения\
**Описание:** Выдает игроку случайный предмет или стак из предметов в сундуке.

**Пример использования:** 
```ts
player::give_random_item([item("stick"), item("stick")]);
```

<h3 id=player_heal>
  <code>player::heal</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Исцелить игрока\
**Тип:** Действие без значения\
**Описание:** Исцеляет игрока.

**Пример использования:** 
```ts
player::heal(1);
```

<h3 id=player_hide_entity>
  <code>player::hide_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Скрыть сущность игроку\
**Тип:** Действие без значения\
**Описание:** Скрывает указанную сущность для игрока.

**Пример использования:** 
```ts
player::hide_entity(["name_or_uuid", "name_or_uuid"],"TRUE");
```

<h3 id=player_hide_scoreboard>
  <code>player::hide_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Скрыть скорборд\
**Тип:** Действие без значения\
**Описание:** Скрывает текущий скорборд игрока.

**Пример использования:** 
```ts
player::hide_scoreboard();
```

<h3 id=player_kick>
  <code>player::kick</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Выгнать игрока\
**Тип:** Действие без значения\
**Описание:** Выгоняет игрока из мира.

**Пример использования:** 
```ts
player::kick();
```

<h3 id=player_launch_forward>
  <code>player::launch_forward</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить вперёд\
**Тип:** Действие без значения\
**Описание:** Запускает игрока вперёд или назад по направлению взгляда в зависимости от силы.

**Пример использования:** 
```ts
player::launch_forward(1,"TRUE","YAW_AND_PITCH");
```

<h3 id=player_launch_projectile>
  <code>player::launch_projectile</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить снаряд\
**Тип:** Действие без значения\
**Описание:** Запустить снаряд из местоположения игрока.

**Пример использования:** 
```ts
player::launch_projectile(item("stick"),location(0,0,0,0,0),"name",1,2,particle("fire"));
```

<h3 id=player_launch_to_location>
  <code>player::launch_to_location</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить к местоположению\
**Тип:** Действие без значения\
**Описание:** Запускает игрока к выбранному местоположению.

**Пример использования:** 
```ts
player::launch_to_location(location(0,0,0,0,0),1,"TRUE");
```

<h3 id=player_launch_up>
  <code>player::launch_up</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Подбросить вверх\
**Тип:** Действие без значения\
**Описание:** Подбрасывает игрока вверх или вниз в зависимости от силы.

**Пример использования:** 
```ts
player::launch_up(1,"TRUE");
```

<h3 id=player_load_inventory>
  <code>player::load_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Загрузить сохраненный инвентарь\
**Тип:** Действие без значения\
**Описание:** Загружает выбранный сохраненный инвентарь.

**Пример использования:** 
```ts
player::load_inventory();
```

<h3 id=player_open_book>
  <code>player::open_book</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Открыть книгу\
**Тип:** Действие без значения\
**Описание:** Открывает книгу определённому игроку.

**Пример использования:** 
```ts
player::open_book(item("stick"));
```

<h3 id=player_open_container_inventory>
  <code>player::open_container_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Открыть меню блока\
**Тип:** Действие без значения\
**Описание:** Открывает для игрока меню блока в указанном местоположении.

**Пример использования:** 
```ts
player::open_container_inventory(location(0,0,0,0,0));
```

<h3 id=player_play_animation_action>
  <code>player::play_animation_action</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проиграть анимацию игроку\
**Тип:** Действие без значения\
**Описание:** Проигрывает для игрока определённую анимацию.

**Пример использования:** 
```ts
player::play_animation_action("DAMAGE");
```

<h3 id=player_play_hurt_animation>
  <code>player::play_hurt_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проиграть анимацию получения урона\
**Тип:** Действие без значения\
**Описание:** Проигрывает для игрока анимацию получения урона с определённым наклоном.

**Пример использования:** 
```ts
player::play_hurt_animation(1);
```

<h3 id=player_play_sound>
  <code>player::play_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проиграть звук\
**Тип:** Действие без значения\
**Описание:** Проигрывает звук игроку.

**Пример использования:** 
```ts
player::play_sound(sound("entity.zombie.hurt"),location(0,0,0,0,0));
```

<h3 id=player_play_sound_from_entity>
  <code>player::play_sound_from_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проиграть звук от сущности\
**Тип:** Действие без значения\
**Описание:** Проигрывает звук игроку от указанной сущности.\
**Дополнительная информация:**\
&nbsp;&nbsp;Стерео звуки не будут проигрываться.

**Пример использования:** 
```ts
player::play_sound_from_entity([sound("entity.zombie.hurt"), sound("entity.zombie.hurt")],"name_or_uuid");
```

<h3 id=player_play_sound_sequence>
  <code>player::play_sound_sequence</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проиграть последовательность звуков\
**Тип:** Действие без значения\
**Описание:** Проигрывает игроку последовательность звуков с задержкой между каждым звуком.

**Пример использования:** 
```ts
player::play_sound_sequence([sound("entity.zombie.hurt"), sound("entity.zombie.hurt")],1,location(0,0,0,0,0));
```

<h3 id=player_randomized_teleport>
  <code>player::randomized_teleport</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Случайная телепортация\
**Тип:** Действие без значения\
**Описание:** Телепортирует игрока в случайное местоположение.

**Пример использования:** 
```ts
player::randomized_teleport([location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE","TRUE","TRUE");
```

<h3 id=player_redirect_world>
  <code>player::redirect_world</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Переместить игрока в другой мир\
**Тип:** Действие без значения\
**Описание:** Перемещает игрока в мир с указанным ID.

**Пример использования:** 
```ts
player::redirect_world("world_id");
```

<h3 id=player_remove_boss_bar>
  <code>player::remove_boss_bar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить босс-бар\
**Тип:** Действие без значения\
**Описание:** Удаляет имеющийся босс-бар у определенного игрока.

**Пример использования:** 
```ts
player::remove_boss_bar("id");
```

<h3 id=player_remove_disguise>
  <code>player::remove_disguise</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Убрать маскировку\
**Тип:** Действие без значения\
**Описание:** Убирает маскировку игроку.

**Пример использования:** 
```ts
player::remove_disguise();
```

<h3 id=player_remove_display_blocks>
  <code>player::remove_display_blocks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Скрыть отображаемые блоки\
**Тип:** Действие без значения\
**Описание:** Скрывает от игрока все отображаемые блоки в выбранном пространстве, не влияя на других игроков (максимальный размер пространства - 500 блоков).

**Пример использования:** 
```ts
player::remove_display_blocks(location(0,0,0,0,0),location(0,0,0,0,0));
```

<h3 id=player_remove_inventory_menu_row>
  <code>player::remove_inventory_menu_row</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Убрать строки меню\
**Тип:** Действие без значения\
**Описание:** Убирает одну или несколько строк в инвентаре типа "Сундук".

**Пример использования:** 
```ts
player::remove_inventory_menu_row(1,"TOP");
```

<h3 id=player_remove_items>
  <code>player::remove_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить предметы\
**Тип:** Действие без значения\
**Описание:** Удаляет указанные предметы из инвентаря игрока.

**Пример использования:** 
```ts
player::remove_items([item("stick"), item("stick")]);
```

<h3 id=player_remove_pose>
  <code>player::remove_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сбросить позу игроку\
**Тип:** Действие без значения\
**Описание:** Сбрасывает позу игроку.

**Пример использования:** 
```ts
player::remove_pose();
```

<h3 id=player_remove_potion_effect>
  <code>player::remove_potion_effect</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить эффект\
**Тип:** Действие без значения\
**Описание:** Удаляет выбранные эффекты у игрока.

**Пример использования:** 
```ts
player::remove_potion_effect([potion("slow_falling"), potion("slow_falling")]);
```

<h3 id=player_remove_self_disguise>
  <code>player::remove_self_disguise</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Убрать свою маскировку\
**Тип:** Действие без значения\
**Описание:** Убирает маскировку игрока, которую видно только ему.

**Пример использования:** 
```ts
player::remove_self_disguise();
```

<h3 id=player_remove_skin>
  <code>player::remove_skin</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Убрать скин\
**Тип:** Действие без значения\
**Описание:** Возвращает обычный скин цели события.

**Пример использования:** 
```ts
player::remove_skin();
```

<h3 id=player_remove_world_border>
  <code>player::remove_world_border</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Удалить границу мира\
**Тип:** Действие без значения\
**Описание:** Установить границу мира для игрока на значение по умолчанию.

**Пример использования:** 
```ts
player::remove_world_border();
```

<h3 id=player_replace_items>
  <code>player::replace_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Заменить предметы\
**Тип:** Действие без значения\
**Описание:** Заменяет указанные предметы в инвентаре на определенный предмет.

**Пример использования:** 
```ts
player::replace_items([item("stick"), item("stick")],item("stick"),1);
```

<h3 id=player_reset_weather>
  <code>player::reset_weather</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сбросить погоду\
**Тип:** Действие без значения\
**Описание:** Сбрасывает погоду игроку

**Пример использования:** 
```ts
player::reset_weather();
```

<h3 id=player_ride_entity>
  <code>player::ride_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Посадить на существо\
**Тип:** Действие без значения\
**Описание:** Сажает игрока на существо или другого игрока.

**Пример использования:** 
```ts
player::ride_entity("name_or_uuid");
```

<h3 id=player_save_inventory>
  <code>player::save_inventory</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Сохранить текущий инвентарь\
**Тип:** Действие без значения\
**Описание:** Сохраняет текущий инвентарь игрока. Его можно будет загрузить позже с помощью 'Загрузить сохраненный инвентарь'.

**Пример использования:** 
```ts
player::save_inventory();
```

<h3 id=player_self_disguise_as_block>
  <code>player::self_disguise_as_block</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать себя под блок\
**Тип:** Действие без значения\
**Описание:** Маскирует игрока под блок, но эту маскировку видно только этому игроку.

**Пример использования:** 
```ts
player::self_disguise_as_block(item("stone"));
```

<h3 id=player_self_disguise_as_entity>
  <code>player::self_disguise_as_entity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать себя под сущность\
**Тип:** Действие без значения\
**Описание:** Маскирует игрока под сущность, но эту маскировку видно только этому игроку.

**Пример использования:** 
```ts
player::self_disguise_as_entity(item("stick"));
```

<h3 id=player_self_disguise_as_item>
  <code>player::self_disguise_as_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замаскировать себя под предмет\
**Тип:** Действие без значения\
**Описание:** Маскирует игрока под предмет, но эту маскировку видно только этому игроку.

**Пример использования:** 
```ts
player::self_disguise_as_item(item("stick"));
```

<h3 id=player_send_action_bar>
  <code>player::send_action_bar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отправить экшн-бар\
**Тип:** Действие без значения\
**Описание:** Высвечивает выбранному игроку экшн-бар.

**Пример использования:** 
```ts
player::send_action_bar(["messages", "messages"],"SPACES");
```

<h3 id=player_send_advancement>
  <code>player::send_advancement</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отправить достижение игроку\
**Тип:** Действие без значения\
**Описание:** Высвечивает игроку пользовательское  всплывающее достижение.

**Пример использования:** 
```ts
player::send_advancement("TASK","name",item("stick"));
```

<h3 id=player_send_break_animation>
  <code>player::send_break_animation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать анимацию ломания блока\
**Тип:** Действие без значения\
**Описание:** Показывает анимацию ломания блока (трещины) для игрока, не влияя на других игроков.

**Пример использования:** 
```ts
player::send_break_animation([location(0,0,0,0,0), location(0,0,0,0,0)],1);
```

<h3 id=player_send_dialogue>
  <code>player::send_dialogue</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Диалог\
**Тип:** Действие без значения\
**Описание:** Отправляет несколько сообщений в чат выбранным игрокам с задержкой после каждого сообщения.

**Пример использования:** 
```ts
player::send_dialogue(["messages", "messages"],1);
```

<h3 id=player_send_hover>
  <code>player::send_hover</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отправить сообщение с наведением\
**Тип:** Действие без значения\
**Описание:** Отправляет сообщение выбранному игроку. Когда игрок 'наводит' на него курсор, появляется второе сообщение.

**Пример использования:** 
```ts
player::send_hover("message","hover");
```

<h3 id=player_send_message>
  <code>player::message</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отправить сообщение\
**Тип:** Действие без значения\
**Описание:** Отправляет сообщение в чат указанным игрокам.

**Пример использования:** 
```ts
player::message(["messages", "messages"],"SPACES");
```

<h3 id=player_send_minimessage>
  <code>player::send_minimessage</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отправить сообщение формата MiniMessage\
**Тип:** Действие без значения\
**Описание:** Отправляет игроку сообщение в чат в формате MiniMessage.

**Пример использования:** 
```ts
player::send_minimessage("minimessage");
```

<h3 id=player_send_title>
  <code>player::send_title</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отправить титул\
**Тип:** Действие без значения\
**Описание:** Высвечивает выбранному игроку две надписи на экран - титул и подтитул.

**Пример использования:** 
```ts
player::send_title("title","subtitle",1,2,3);
```

<h3 id=player_set_absorption_health>
  <code>player::set_absorption_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дополнительное здоровье\
**Тип:** Действие без значения\
**Описание:** Устанавливает дополнительное здоровье игрока.

**Пример использования:** 
```ts
player::set_absorption_health(1);
```

<h3 id=player_set_air_ticks>
  <code>player::set_air_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить оставшийся воздух\
**Тип:** Действие без значения\
**Описание:** Устанавливает оставшийся воздух игроку.

**Пример использования:** 
```ts
player::set_air_ticks(1);
```

<h3 id=player_set_allow_flying>
  <code>player::set_allow_flying</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить разрешение полёта игрока\
**Тип:** Действие без значения\
**Описание:** Устанавливает разрешение полёта для игрока.

**Пример использования:** 
```ts
player::set_allow_flying("TRUE");
```

<h3 id=player_set_armor>
  <code>player::set_armor</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить броню\
**Тип:** Действие без значения\
**Описание:** Устанавливает броню игрока.

**Пример использования:** 
```ts
player::set_armor(item("stick"),item("stick"),item("stick"),item("stick"));
```

<h3 id=player_set_arrows_in_body>
  <code>player::set_arrows_in_body</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить стрелы на игроке\
**Тип:** Действие без значения\
**Описание:** Отображает определённое количество стрел на игроке.

**Пример использования:** 
```ts
player::set_arrows_in_body(1);
```

<h3 id=player_set_attack_speed>
  <code>player::set_attack_speed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить скорость атаки\
**Тип:** Действие без значения\
**Описание:** Устанавливает скорость атаки игроку.

**Пример использования:** 
```ts
player::set_attack_speed(1);
```

<h3 id=player_set_attribute>
  <code>player::set_attribute</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить атрибут\
**Тип:** Действие без значения\
**Описание:** Устанавливает игроку указанное значение атрибута.

**Пример использования:** 
```ts
player::set_attribute(1,"MAX_HEALTH");
```

<h3 id=player_set_bee_stingers_in_body>
  <code>player::set_bee_stingers_in_body</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить жало пчелы на игроке\
**Тип:** Действие без значения\
**Описание:** Отображает определённое количество жал пчёл на игроке.

**Пример использования:** 
```ts
player::set_bee_stingers_in_body(1);
```

<h3 id=player_set_boss_bar>
  <code>player::set_boss_bar</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить босс-бар\
**Тип:** Действие без значения\
**Описание:** Устанавливает у определённого игрока пользовательский босс-бар.

**Пример использования:** 
```ts
player::set_boss_bar("id","title",1,"PINK","PROGRESS","NONE");
```

<h3 id=player_set_chat_completions>
  <code>player::set_chat_completions</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Обновление подсказок в чате\
**Тип:** Действие без значения\
**Описание:** Обновляет игроку подсказки показываемые при вводе текста в чате.

**Пример использования:** 
```ts
player::set_chat_completions(["completions", "completions"],"ADD");
```

<h3 id=player_set_collidable>
  <code>player::set_collidable</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим столкновения\
**Тип:** Действие без значения\
**Описание:** Устанавливает игроку режим столкновения с существами.

**Пример использования:** 
```ts
player::set_collidable("TRUE");
```

<h3 id=player_set_compass_target>
  <code>player::set_compass_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить цель компаса\
**Тип:** Действие без значения\
**Описание:** Установить цель компаса для игрока, в сторону которой будет крутиться стрелка компаса.

**Пример использования:** 
```ts
player::set_compass_target(location(0,0,0,0,0));
```

<h3 id=player_set_cursor_item>
  <code>player::set_cursor_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет на курсор\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет на курсор игрока.

**Пример использования:** 
```ts
player::set_cursor_item(item("stick"));
```

<h3 id=player_set_death_drops>
  <code>player::set_death_drops</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить выпадение предметов\
**Тип:** Действие без значения\
**Описание:** Устанавливает выпадение предметов из игрока при смерти.

**Пример использования:** 
```ts
player::set_death_drops("TRUE");
```

<h3 id=player_set_ender_chest_contents>
  <code>player::set_ender_chest_contents</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить содержимое Эндер-сундука\
**Тип:** Действие без значения\
**Описание:** Устанавливает предметы в инвентарь Эндер-сундука игрока.

**Пример использования:** 
```ts
player::set_ender_chest_contents([item("stick"), item("stick")]);
```

<h3 id=player_set_entity_glowing>
  <code>player::set_entity_glowing</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить свечение сущности\
**Тип:** Действие без значения\
**Описание:** Включает или выключает свечение сущности для данного игрока.

**Пример использования:** 
```ts
player::set_entity_glowing(["name_or_uuid", "name_or_uuid"],"WHITE","TRUE");
```

<h3 id=player_set_equipment>
  <code>player::set_equipment</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить экипировку\
**Тип:** Действие без значения\
**Описание:** Устанавливает предметы в один из слотов экипировки (броня и предметы в руках) игрока.

**Пример использования:** 
```ts
player::set_equipment(item("stick"),"CHEST");
```

<h3 id=player_set_exhaustion>
  <code>player::set_exhaustion</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить уровень истощения\
**Тип:** Действие без значения\
**Описание:** Устанавливает уровень истощения игроку.

**Пример использования:** 
```ts
player::set_exhaustion(1,"SET");
```

<h3 id=player_set_experience>
  <code>player::set_experience</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить уровень\
**Тип:** Действие без значения\
**Описание:** Устанавливает уровень игроку.

**Пример использования:** 
```ts
player::set_experience(1,"POINTS");
```

<h3 id=player_set_fall_distance>
  <code>player::set_fall_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дистанцию падения\
**Тип:** Действие без значения\
**Описание:** Устанавливает дистанцию, с которой падает игрок.

**Пример использования:** 
```ts
player::set_fall_distance(1);
```

<h3 id=player_set_fire_ticks>
  <code>player::set_fire_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Поджечь игрока\
**Тип:** Действие без значения\
**Описание:** Поджигает игрока на выбранное время.

**Пример использования:** 
```ts
player::set_fire_ticks(1);
```

<h3 id=player_set_flying>
  <code>player::set_flying</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить полёт\
**Тип:** Действие без значения\
**Описание:** Устанавливает для игрока состояние полёта.

**Пример использования:** 
```ts
player::set_flying("TRUE");
```

<h3 id=player_set_fog_distance>
  <code>player::set_fog_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дистанцию прорисовки\
**Тип:** Действие без значения\
**Описание:** Устанавливает дистанцию прорисовки чанков для игрока. Значение "-1" сбрасывает до стандартной.

**Пример использования:** 
```ts
player::set_fog_distance(1);
```

<h3 id=player_set_food>
  <code>player::set_food</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить голод\
**Тип:** Действие без значения\
**Описание:** Устанавливает уровень голода игроку.

**Пример использования:** 
```ts
player::set_food(1,"SET");
```

<h3 id=player_set_freeze_ticks>
  <code>player::set_freeze_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время заморозки\
**Тип:** Действие без значения\
**Описание:** Устанавливает игроку время заморозки (количество тиков, которое игрок провёл в рыхлом снегу).

**Пример использования:** 
```ts
player::set_freeze_ticks(1,"TRUE");
```

<h3 id=player_set_gamemode>
  <code>player::set_gamemode</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить режим игры\
**Тип:** Действие без значения\
**Описание:** Устанавливает режим игры для игрока.

**Пример использования:** 
```ts
player::set_gamemode("SURVIVAL","RESPECT_GAMEMODE");
```

<h3 id=player_set_gliding>
  <code>player::set_gliding</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить полёт на элитрах\
**Тип:** Действие без значения\
**Описание:** Устанавливает для игрока состояние полёта на элитрах.

**Пример использования:** 
```ts
player::set_gliding("TRUE");
```

<h3 id=player_set_health>
  <code>player::set_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить здоровье игрока\
**Тип:** Действие без значения\
**Описание:** Устанавливает здоровье игрока на выбранное количество.

**Пример использования:** 
```ts
player::set_health(1);
```

<h3 id=player_set_hotbar_slot>
  <code>player::set_hotbar_slot</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить слот\
**Тип:** Действие без значения\
**Описание:** Устанавливает выбранный слот игроку.

**Пример использования:** 
```ts
player::set_hotbar_slot(1);
```

<h3 id=player_set_instant_respawn>
  <code>player::set_instant_respawn</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить мгновенное возрождение\
**Тип:** Действие без значения\
**Описание:** Устанавливает мгновенное возрождение игроку.

**Пример использования:** 
```ts
player::set_instant_respawn("TRUE");
```

<h3 id=player_set_inventory_kept>
  <code>player::set_inventory_kept</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить сохранение инвентаря\
**Тип:** Действие без значения\
**Описание:** Устанавливает игроку сохранение инвентаря при смерти.

**Пример использования:** 
```ts
player::set_inventory_kept("TRUE");
```

<h3 id=player_set_inventory_menu_item>
  <code>player::set_inventory_menu_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет в слот\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет в указанный слот открытого инвентарного меню игрока.

**Пример использования:** 
```ts
player::set_inventory_menu_item(item("stick"),1);
```

<h3 id=player_set_inventory_menu_name>
  <code>player::set_inventory_menu_name</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить название меню\
**Тип:** Действие без значения\
**Описание:** Устанавливает новое название для открытого инвентарного меню игрока.

**Пример использования:** 
```ts
player::set_inventory_menu_name("text");
```

<h3 id=player_set_invulnerability_ticks>
  <code>player::set_invulnerability_ticks</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить длительность неуязвимости\
**Тип:** Действие без значения\
**Описание:** Устанавливает длительность неуязвимости для игрока.

**Пример использования:** 
```ts
player::set_invulnerability_ticks(1);
```

<h3 id=player_set_item_cooldown>
  <code>player::set_item_cooldown</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить задержку предмета\
**Тип:** Действие без значения\
**Описание:** Применяет визуальный эффект шкалы задержки для всех предметов выбранного типа.

**Пример использования:** 
```ts
player::set_item_cooldown(item("stick"),1,sound("entity.zombie.hurt"));
```

<h3 id=player_set_items>
  <code>player::set_items</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предметы\
**Тип:** Действие без значения\
**Описание:** Устанавливает в инвентарь игрока соответственно предметы из сундука.

**Пример использования:** 
```ts
player::set_items([item("stick"), item("stick")]);
```

<h3 id=player_set_max_health>
  <code>player::set_max_health</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить максимальное здоровье игрока\
**Тип:** Действие без значения\
**Описание:** Устанавливает максимальное количество здоровья для игрока.

**Пример использования:** 
```ts
player::set_max_health(1,"TRUE");
```

<h3 id=player_set_movement_speed>
  <code>player::set_movement_speed</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить скорость движения\
**Тип:** Действие без значения\
**Описание:** Устанавливает скорость движения игроку.

**Пример использования:** 
```ts
player::set_movement_speed(1,"WALK");
```

<h3 id=player_set_nametag_visible>
  <code>player::set_nametag_visible</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Отображение ника игрока\
**Тип:** Действие без значения\
**Описание:** Отобразит или скроет ник над головой.

**Пример использования:** 
```ts
player::set_nametag_visible("TRUE");
```

<h3 id=player_set_player_list_info>
  <code>player::set_player_list_info</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить текст в списке игроков\
**Тип:** Действие без значения\
**Описание:** Устанавливает текст над или под списком игроков для игрока.

**Пример использования:** 
```ts
player::set_player_list_info(["text", "text"],"HEADER","SPACES");
```

<h3 id=player_set_pose>
  <code>player::set_pose</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить позу игроку\
**Тип:** Действие без значения\
**Описание:** Устанавливает определённую позу игроку.

**Пример использования:** 
```ts
player::set_pose("CROAKING","TRUE");
```

<h3 id=player_set_pvp>
  <code>player::set_pvp</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить разрешение атаковать игроков\
**Тип:** Действие без значения\
**Описание:** Устанавливает разрешение игроку атаковать других игроков и наносить им урон.

**Пример использования:** 
```ts
player::set_pvp("TRUE");
```

<h3 id=player_set_rain_level>
  <code>player::set_rain_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить уровень дождя\
**Тип:** Действие без значения\
**Описание:** Устанавливает уровень дождя игроку.

**Пример использования:** 
```ts
player::set_rain_level(1);
```

<h3 id=player_set_rotation>
  <code>player::set_rotation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить поворот\
**Тип:** Действие без значения\
**Описание:** Устанавливает поворот игрока.

**Пример использования:** 
```ts
player::set_rotation(1,2);
```

<h3 id=player_set_rotation_by_vector>
  <code>player::set_rotation_by_vector</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить поворот по вектору\
**Тип:** Действие без значения\
**Описание:** Устанавливает поворот игрока по вектору.

**Пример использования:** 
```ts
player::set_rotation_by_vector(vector(0,0,0));
```

<h3 id=player_set_saturation>
  <code>player::set_saturation</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить насыщенность\
**Тип:** Действие без значения\
**Описание:** Устанавливает второстепенный уровень голода (насыщенность) игроку.

**Пример использования:** 
```ts
player::set_saturation(1,"SET");
```

<h3 id=player_set_simulation_distance>
  <code>player::set_simulation_distance</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить дистанцию симуляции\
**Тип:** Действие без значения\
**Описание:** Устанавливает дистанцию симуляции чанков для игрока.

**Пример использования:** 
```ts
player::set_simulation_distance(1);
```

<h3 id=player_set_skin>
  <code>player::set_skin</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить скин\
**Тип:** Действие без значения\
**Описание:** Устанавливает скин указанного игрока для цели события.

**Пример использования:** 
```ts
player::set_skin("name_or_uuid","MOJANG");
```

<h3 id=player_set_slot_item>
  <code>player::set_slot_item</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить предмет в слот\
**Тип:** Действие без значения\
**Описание:** Устанавливает предмет в слот в инвентаре игрока.

**Пример использования:** 
```ts
player::set_slot_item(item("stick"),1);
```

<h3 id=player_set_spawn_point>
  <code>player::set_spawn_point</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить местоположение возрождения\
**Тип:** Действие без значения\
**Описание:** Устанавливает игроку новое местоположение возрождения.

**Пример использования:** 
```ts
player::set_spawn_point(location(0,0,0,0,0));
```

<h3 id=player_set_thunder_level>
  <code>player::set_thunder_level</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить уровень грозы\
**Тип:** Действие без значения\
**Описание:** Устанавливает уровень грозы игроку.\
**Дополнительная информация:**\
&nbsp;&nbsp;Для установки необходима дождливая погода.

**Пример использования:** 
```ts
player::set_thunder_level(1);
```

<h3 id=player_set_tick_rate>
  <code>player::set_tick_rate</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить тик-рейт\
**Тип:** Действие без значения\
**Описание:** Устанавливает игроку тик-рейт, не влияя на других игроков.

**Пример использования:** 
```ts
player::set_tick_rate(1);
```

<h3 id=player_set_time>
  <code>player::set_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить время игрока\
**Тип:** Действие без значения\
**Описание:** Установить время игроку, не меняя его для остальных игроков.

**Пример использования:** 
```ts
player::set_time(1);
```

<h3 id=player_set_velocity>
  <code>player::set_velocity</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запустить по вектору\
**Тип:** Действие без значения\
**Описание:** Запускает игрока по указанному вектору.

**Пример использования:** 
```ts
player::set_velocity(vector(0,0,0),"TRUE");
```

<h3 id=player_set_visual_fire>
  <code>player::set_visual_fire</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить визуальный огонь\
**Тип:** Действие без значения\
**Описание:** Устанавливает игроку эффект горения.

**Пример использования:** 
```ts
player::set_visual_fire("TRUE");
```

<h3 id=player_set_weather>
  <code>player::set_weather</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить погоду\
**Тип:** Действие без значения\
**Описание:** Установить погоду для игрока, не влияя на других игроков.

**Пример использования:** 
```ts
player::set_weather("DOWNFALL");
```

<h3 id=player_set_world_border>
  <code>player::set_world_border</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Установить границу мира игроку\
**Тип:** Действие без значения\
**Описание:** Установить границу мира для игрока, не меняя её для других игроков.

**Пример использования:** 
```ts
player::set_world_border(location(0,0,0,0,0),1,2);
```

<h3 id=player_shift_world_border>
  <code>player::shift_world_border</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Передвинуть границу мира\
**Тип:** Действие без значения\
**Описание:** Передвинуть границу мира для игрока, не меняя её для других игроков.

**Пример использования:** 
```ts
player::shift_world_border(1,2,3);
```

<h3 id=player_show_debug_marker>
  <code>player::show_debug_marker</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать отладочный маркер\
**Тип:** Действие без значения\
**Описание:** Показывает игроку отладочный маркер на местоположении на указанное время. Красный и синий цвет работают для игроков на версии 1.19.4 и выше.\
**Дополнительная информация:**\
&nbsp;&nbsp;Оставьте аргумент "Отображаемое имя" пустым, чтобы полностью скрыть имя.

**Пример использования:** 
```ts
player::show_debug_marker(location(0,0,0,0,0),"name",1,2,3,4,5);
```

<h3 id=player_show_demo_screen>
  <code>player::show_demo_screen</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать экран демо-режима\
**Тип:** Действие без значения\
**Описание:** Показывает игроку экран демо-режима.

**Пример использования:** 
```ts
player::show_demo_screen();
```

<h3 id=player_show_inventory_menu>
  <code>player::show_inventory_menu</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать меню\
**Тип:** Действие без значения\
**Описание:** Показывает игроку инвентарное меню с выбранными предметами и названием.

**Пример использования:** 
```ts
player::show_inventory_menu([item("stick"), item("stick")],"name","CHEST");
```

<h3 id=player_show_scoreboard>
  <code>player::show_scoreboard</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать скорборд\
**Тип:** Действие без значения\
**Описание:** Отображает определённый скорборд игроку. Для отображения указанный скорборд должен иметь минимум одно значение.

**Пример использования:** 
```ts
player::show_scoreboard("id");
```

<h3 id=player_show_win_screen>
  <code>player::show_win_screen</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Показать экран титров\
**Тип:** Действие без значения\
**Описание:** Показывает игроку экран титров.

**Пример использования:** 
```ts
player::show_win_screen();
```

<h3 id=player_spectate_target>
  <code>player::spectate_target</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Следить за целью\
**Тип:** Действие без значения\
**Описание:** Устанавливает цель слежения игрока в режиме наблюдателя.

**Пример использования:** 
```ts
player::spectate_target("name_or_uuid");
```

<h3 id=player_stop_sound>
  <code>player::stop_sound</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Остановить звук\
**Тип:** Действие без значения\
**Описание:** Останавливает все или определенные звуки для игрока.

**Пример использования:** 
```ts
player::stop_sound([sound("entity.zombie.hurt"), sound("entity.zombie.hurt")]);
```

<h3 id=player_stop_sounds_by_source>
  <code>player::stop_sounds_by_source</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Остановить звуки по источнику\
**Тип:** Действие без значения\
**Описание:** Останавливает все звуки по определённому источнику.

**Пример использования:** 
```ts
player::stop_sounds_by_source("AMBIENT");
```

<h3 id=player_swing_hand>
  <code>player::swing_hand</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проиграть анимацию взмаха руки\
**Тип:** Действие без значения\
**Описание:** Проигрывает для игрока анимацию взмаха руки.

**Пример использования:** 
```ts
player::swing_hand("MAIN");
```

<h3 id=player_teleport>
  <code>player::teleport</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Телепортация\
**Тип:** Действие без значения\
**Описание:** Телепортирует игрока в выбранное местоположение.\
**Дополнительная информация:**\
&nbsp;&nbsp;Закрывает открытое инвентарное меню.

**Пример использования:** 
```ts
player::teleport(location(0,0,0,0,0),"TRUE","TRUE","TRUE");
```

<h3 id=player_teleport_sequence>
  <code>player::teleport_sequence</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Последовательность телепортаций\
**Тип:** Действие без значения\
**Описание:** Телепортирует игрока между местоположениями с заданной задержкой.

**Пример использования:** 
```ts
player::teleport_sequence(1,[location(0,0,0,0,0), location(0,0,0,0,0)]);
```

