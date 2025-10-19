<h3 id=call_function>
  <code>code::call_function</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Call Function\
**Type:** Action without value\
**Description:** Calls a function code string.

**Usage example:** 
```ts
code::call_function("function_name", {"args":`args`});

//Or dry by keywords

code::call_function(function_name="function_name", args={"args":`args`});
```

**Arguments:**

| **Name**        | **Type**   | **Description** |
| --------------- | ---------- | --------------- |
| `function_name` | Text       | Function Name   |
| `args`          | Dictionary | None            |
<h3 id=control_call_exception>
  <code>code::call_exception</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Call Error\
**Type:** Action without value\
**Description:** Calls a specific error with the specified ID and message.\
**Additional info:**\
&nbsp;&nbsp;It is recommended to use this in the Catch Error action.

**Usage example:** 
```ts
code::call_exception("id", "message", "ERROR");

//Or dry by keywords

code::call_exception(id="id", message="message", type="ERROR");
```

**Arguments:**

| **Name**  | **Type**                                                                     | **Description** |
| --------- | ---------------------------------------------------------------------------- | --------------- |
| `id`      | Text                                                                         | Error ID        |
| `message` | Text                                                                         | Error Message   |
| `type`    | Marker<br/>**ERROR** - Error<br/>**FATAL** - Fatal<br/>**WARNING** - Warning | Error Type      |
<h3 id=control_dummy>
  <code>code::dummy</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** ...\
**Type:** Action without value\
**Description:** ...

**Usage example:** 
```ts
code::dummy();
```

<h3 id=control_end_thread>
  <code>code::break</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Stop Sequence\
**Type:** Action without value\
**Description:** Stops the current code block sequence. Any code after this block will not be executed.\
**Additional info:**\
&nbsp;&nbsp;If the action was used in functions, it will stop the parent line where the function was called.

**Usage example:** 
```ts
code::break();
```

<h3 id=control_return_function>
  <code>code::return_function</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Return From Function\
**Type:** Action without value\
**Description:** Stops the current sequence of code blocks in a function and returns to the function call block.\
**Additional info:**\
&nbsp;&nbsp;Returns up to the current function call block in the parent row.

**Usage example:** 
```ts
code::return_function();
```

<h3 id=control_skip_iteration>
  <code>code::skip_iteration</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Skip Iteration\
**Type:** Action without value\
**Description:** Skip one iteration in the current iteration.
**Work_with:**\
&nbsp;&nbsp;With repetitions

**Usage example:** 
```ts
code::skip_iteration();
```

<h3 id=control_stop_repeat>
  <code>code::stop_repeat</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Stop Repeat\
**Type:** Action without value\
**Description:** Completely stops the current repeat.
**Work_with:**\
&nbsp;&nbsp;Repeat

**Usage example:** 
```ts
code::stop_repeat();
```

<h3 id=control_wait>
  <code>code::wait</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Wait\
**Type:** Action without value\
**Description:** Pauses the current sequence of code blocks for a certain amount of time.\
**Additional info:**\
&nbsp;&nbsp;Minimum delay is 1 tick; in Tiki mode, only whole numbers can be set.

**Usage example:** 
```ts
code::wait(1, "MINUTES");

//Or dry by keywords

code::wait(duration=1, time_unit="MINUTES");
```

**Arguments:**

| **Name**    | **Type**                                                                         | **Description** |
| ----------- | -------------------------------------------------------------------------------- | --------------- |
| `duration`  | Number                                                                           | Wait Duration   |
| `time_unit` | Marker<br/>**MINUTES** - Minutes<br/>**SECONDS** - Seconds<br/>**TICKS** - Ticks | Time Unit       |
<h3 id=else>
  <code>code::else</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Else\
**Type:** Action without value\
**Description:** ...

**Usage example:** 
```ts
code::else(){
    player::message("Everything work");
}
```

<h3 id=start_process>
  <code>code::start_process</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Start Process\
**Type:** Action without value\
**Description:** Starts a line of process code.

**Usage example:** 
```ts
code::start_process("process_name", "DONT_COPY", "CURRENT_TARGET", {"args":`args`});

//Or dry by keywords

code::start_process(process_name="process_name", local_variables_mode="DONT_COPY", target_mode="CURRENT_TARGET", args={"args":`args`});
```

**Arguments:**

| **Name**               | **Type**                                                                                                                                                                       | **Description** |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `process_name`         | Text                                                                                                                                                                           | Process name    |
| `local_variables_mode` | Marker<br/>**DONT_COPY** - Don\'t duplicate<br/>**COPY** - Duplicate<br/>**SHARE** - General                                                                                   | Variable Mode   |
| `target_mode`          | Marker<br/>**CURRENT_TARGET** - Event Target<br/>**CURRENT_SELECTION** - Current Target<br/>**NO_TARGET** - No Target<br/>**FOR_EACH_IN_SELECTION** - Each Target in Selection | Process Target  |
| `args`                 | Dictionary                                                                                                                                                                     | None            |
