<h3 id=controller_async_run>
  <code>controller::async_run</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Запуск в отдельном потоке\
**Тип:** Действие без значения\
**Описание:** Запускает код внутри поршней в отдельном потоке, что может уменьшить нагрузку. Отмена и возврат события не будут работать после поршней.

**Пример использования:** 
```ts
controller::async_run(){
    player::message("Всё работает");
}
```

<h3 id=controller_exception>
  <code>controller::catch_exception</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Уловить ошибку\
**Тип:** Действие без значения\
**Описание:** Улавливает ошибку кода внутри поршней в виде словаря "ID - Сообщение", результат присваивает к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Не улавливает глобальные и критические ошибки.

**Пример использования:** 
```ts
controller::catch_exception(a1,"WARNING"){
    player::message("Всё работает");
}
```

<h3 id=controller_measure_time>
  <code>controller::measure_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Имя:** Замерить время выполнения\
**Тип:** Действие без значения\
**Описание:** Замеряет время выполнения кода внутри поршней и присваивает результат к переменной.\
**Дополнительная информация:**\
&nbsp;&nbsp;Учитывает блоки "Ждать".

**Пример использования:** 
```ts
controller::measure_time(a1,"NANOSECONDS"){
    player::message("Всё работает");
}
```

