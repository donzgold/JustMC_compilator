<h3 id=control_dummy>
  <code>controller::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action without value\
**Description:** ...

**Usage example:** 
```ts
controller::dummy();
```

<h3 id=controller_async_run>
  <code>controller::async_run</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Run On Separate Thread\
**Type:** Action without value\
**Description:** Runs the code inside the pistons on a separate thread, which can reduce load. Undo and redo events will not work after pistons.\
**Additional info:**\
&nbsp;&nbsp;Some actions inside pistons may not work.

**Usage example:** 
```ts
controller::async_run(){
    player::message("Everything work");
}
```

<h3 id=controller_exception>
  <code>controller::catch_exception</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Catch Error\
**Type:** Action without value\
**Description:** Catches a code error inside the pistons as a \"ID - Message\" dictionary, assigns the result to a variable.\
**Additional info:**\
&nbsp;&nbsp;Does not catch global or fatal errors.

**Usage example:** 
```ts
controller::catch_exception(`variable`, "ALL"){
    player::message("Everything work");
}

#Or dry by keywords

controller::catch_exception(variable=`variable`, exception_type="ALL"){
    player::message("Everything work");
}
```

**Arguments:**

| **Name**         | **Type**                                                                 | **Description**    |
| ---------------- | ------------------------------------------------------------------------ | ------------------ |
| `variable`       | Variable                                                                 | Variable to Assign |
| `exception_type` | Marker<br/>**ALL** - All<br/>**ERROR** - Error<br/>**WARNING** - Warning | Error Type         |
<h3 id=controller_measure_time>
  <code>controller::measure_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Measure Execution Time\
**Type:** Action without value\
**Description:** Measures the execution time of the code inside the pistons and assigns the result to a variable.\
**Additional info:**\
&nbsp;&nbsp;Accounts for \"Wait\" blocks.

**Usage example:** 
```ts
controller::measure_time(`variable`, "MICROSECONDS"){
    player::message("Everything work");
}

#Or dry by keywords

controller::measure_time(variable=`variable`, duration="MICROSECONDS"){
    player::message("Everything work");
}
```

**Arguments:**

| **Name**   | **Type**                                                                                                         | **Description**    |
| ---------- | ---------------------------------------------------------------------------------------------------------------- | ------------------ |
| `variable` | Variable                                                                                                         | Variable to Assign |
| `duration` | Marker<br/>**MICROSECONDS** - Microseconds<br/>**MILLISECONDS** - Milliseconds<br/>**NANOSECONDS** - Nanoseconds | Time Format        |
