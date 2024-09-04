<h3 id=repeat_adjacently>
  <code>repeat::adjacently</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проход по смежным блокам\
**Тип:** Действие без значения\
**Описание:** Присваивает текущее местоположение в указанную переменную среди соседних блоков относительно заданного местоположения.

**Пример использования:** 
```ts
repeat::adjacently(location(0,0,0,0,0),"TRUE","TRUE","CARDINAL"){a1->
    player::message("Код в цикле")
}
```

<h3 id=repeat_for_each_in_list>
  <code>repeat::for_each_in_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проход по списку\
**Тип:** Действие без значения\
**Описание:** Обращается к каждому элементу из указанного списка и выдаёт его индекс и значение в указанные переменные.

**Пример использования:** 
```ts
repeat::for_each_in_list(`list`){a1, a2->
    player::message("Код в цикле")
}
```

<h3 id=repeat_for_each_map_entry>
  <code>repeat::for_each_map_entry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проход по словарю\
**Тип:** Действие без значения\
**Описание:** Обращается к каждому элементу из указанного словаря и выдаёт его индекс и значение в указанные переменные.

**Пример использования:** 
```ts
repeat::for_each_map_entry(`map`){a1, a2->
    player::message("Код в цикле")
}
```

<h3 id=repeat_forever>
  <code>repeat::forever</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Повторять вечно\
**Тип:** Действие без значения\
**Описание:** Постоянно повторяет код внутри поршней.

**Пример использования:** 
```ts
repeat::forever(){
    player::message("Всё работает");
}
```

<h3 id=repeat_multi_times>
  <code>repeat::multi_times</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Цикл со счётчиком\
**Тип:** Действие без значения\
**Описание:** Выполняет код заданное количество раз.

**Пример использования:** 
```ts
repeat::multi_times(1){a1->
    player::message("Код в цикле")
}
```

<h3 id=repeat_on_circle>
  <code>repeat::on_circle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проход по окружности\
**Тип:** Действие без значения\
**Описание:** Последовательно выдаёт местоположение каждого блока окружности с указанными параметрами.

**Пример использования:** 
```ts
repeat::on_circle(location(0,0,0,0,0),1,2,vector(0,0,0),3,"DEGREES"){a1->
    player::message("Код в цикле")
}
```

<h3 id=repeat_on_grid>
  <code>repeat::on_grid</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проход по региону\
**Тип:** Действие без значения\
**Описание:** Выдаёт местоположение каждого блока из заданного региона в указанную переменную.

**Пример использования:** 
```ts
repeat::on_grid(location(0,0,0,0,0),location(0,0,0,0,0)){a1->
    player::message("Код в цикле")
}
```

<h3 id=repeat_on_path>
  <code>repeat::on_path</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проход по пути\
**Тип:** Действие без значения\
**Описание:** Проходит от одного местоположения к другому с определённым шагом, присваивая текущее местоположение в указанную переменную.

**Пример использования:** 
```ts
repeat::on_path(1,[location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE"){a1->
    player::message("Код в цикле")
}
```

<h3 id=repeat_on_range>
  <code>repeat::on_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Цикл в диапазоне\
**Тип:** Действие без значения\
**Описание:** Присваивает текущее число в указанную переменную из заданного диапазона с определённым шагом.

**Пример использования:** 
```ts
repeat::on_range(1,2,3){a1->
    player::message("Код в цикле")
}
```

<h3 id=repeat_on_sphere>
  <code>repeat::on_sphere</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Проход по сфере\
**Тип:** Действие без значения\
**Описание:** Последовательно выдаёт местоположение каждой точки на сфере с указанными параметрами.

**Пример использования:** 
```ts
repeat::on_sphere(location(0,0,0,0,0),1,2,"NO_CHANGES"){a1->
    player::message("Код в цикле")
}
```

<h3 id=repeat_while>
  <code>repeat::while</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Цикл с условием\
**Тип:** Действие без значения\
**Описание:** Выполняет код до тех пор, пока выбранное условие является истиной.

**Пример использования:** 
```ts
repeat::while(a1.exists()){
    player::message("Всё работает");
}
```

