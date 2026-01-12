<h2 id=controller>
  <code>controller</code>
  <a href="./actions.md" style="font-size: 14px; margin-left:">↩️</a>
</h2>

<h3 id=controller_async_run>
  <code>controller::async_run</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Run On Separate Thread\
**Action type:** Action without value\
**Description:** Runs the code inside the pistons on a separate thread, which can reduce load. Undo and redo events will not work after pistons.\
**Additional info:**\
&nbsp;&nbsp;Some actions inside pistons may not work.

**Usage example:**
```ts
controller::async_run(){
    player::message("Condition is true");
}
```

<h3 id=controller_do_not_run>
  <code>controller::do_not_run</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.controller_do_not_run.name\
**Action type:** Action without value\
**Description:** creative_plus.action.controller_do_not_run.description

**Usage example:**
```ts
controller::do_not_run(){
    player::message("Condition is true");
}
```

<h3 id=controller_exception>
  <code>controller::catch_exception</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Catch Error\
**Action type:** Action without value\
**Description:** Catches a code error inside the pistons as a "ID - Message" dictionary, assigns the result to a variable.\
**Additional info:**\
&nbsp;&nbsp;Does not catch global or fatal errors.

**Usage example:**
```ts
controller::catch_exception(`variable`, "ALL"){
    player::message("Condition is true");
}

//Or dry by keywords

controller::catch_exception(variable=`variable`, exception_type="ALL"){
    player::message("Condition is true");
}
```

**Arguments:**

| ID             | Type                                                                     | Description        |
|----------------|--------------------------------------------------------------------------|--------------------|
| variable       | Variable                                                                 | Variable to Assign |
| exception_type | Marker<br/>**ALL** - All<br/>**ERROR** - Error<br/>**WARNING** - Warning | Error Type         |

<h3 id=controller_isolated_selection>
  <code>controller::isolated_selection</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** creative_plus.action.controller_isolated_selection.name\
**Action type:** Action without value\
**Description:** creative_plus.action.controller_isolated_selection.description\
**Additional info:**\
&nbsp;&nbsp;creative_plus.action.controller_isolated_selection.additional_information.info\
&nbsp;&nbsp;creative_plus.action.controller_isolated_selection.additional_information.you_can_use_return_with_for_each_in_selection

**Usage example:**
```ts
controller::isolated_selection("DEFAULT"){
    player::message("Condition is true");
}

//Or dry by keywords

controller::isolated_selection(selection_mode="DEFAULT"){
    player::message("Condition is true");
}
```

**Arguments:**

| ID             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                     |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| selection_mode | Marker<br/>**DEFAULT** - creative_plus.action.controller_isolated_selection.argument.selection_mode.enum.default.name<br/>**CURRENT** - creative_plus.action.controller_isolated_selection.argument.selection_mode.enum.current.name<br/>**EMPTY** - creative_plus.action.controller_isolated_selection.argument.selection_mode.enum.empty.name<br/>**FOR_EACH** - creative_plus.action.controller_isolated_selection.argument.selection_mode.enum.for_each.name | creative_plus.action.controller_isolated_selection.argument.selection_mode.name |

<h3 id=controller_measure_time>
  <code>controller::measure_time</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Measure Execution Time\
**Action type:** Action without value\
**Description:** Measures the execution time of the code inside the pistons and assigns the result to a variable.\
**Additional info:**\
&nbsp;&nbsp;Accounts for "Wait" blocks.

**Usage example:**
```ts
controller::measure_time(`variable`, "MICROSECONDS"){
    player::message("Condition is true");
}

//Or dry by keywords

controller::measure_time(variable=`variable`, duration="MICROSECONDS"){
    player::message("Condition is true");
}
```

**Arguments:**

| ID       | Type                                                                                                             | Description        |
|----------|------------------------------------------------------------------------------------------------------------------|--------------------|
| variable | Variable                                                                                                         | Variable to Assign |
| duration | Marker<br/>**MICROSECONDS** - Microseconds<br/>**MILLISECONDS** - Milliseconds<br/>**NANOSECONDS** - Nanoseconds | Time Format        |

