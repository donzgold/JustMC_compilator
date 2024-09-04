<h3 id=call_function>
  <code>code::call_function</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Call Function\
**Type:** Action without value\
**Description:** Calls a function code string.

**Usage example:** 
```ts
code::call_function("function_name");
```

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
code::call_exception("id","message","WARNING");
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
code::wait(1,"TICKS");
```

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
code::start_process("process_name","CURRENT_TARGET","DONT_COPY");
```

