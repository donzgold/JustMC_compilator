<h3 id=repeat_adjacently>
  <code>repeat::adjacently</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat Adjacently\
**Type:** Action without value\
**Description:** Assigns the current location to the specified variable among blocks adjacent to the specified location.

**Usage example:** 
```ts
repeat::adjacently(location(0,0,0,0,0),"TRUE","TRUE","CARDINAL"){a1->
    player::message("Code in cycle")
}
```

<h3 id=repeat_for_each_in_list>
  <code>repeat::for_each_in_list</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat For List Values\
**Type:** Action without value\
**Description:** Retrieves each item in the specified list and outputs its index and value to the specified variables.

**Usage example:** 
```ts
repeat::for_each_in_list(`list`){a1, a2->
    player::message("Code in cycle")
}
```

<h3 id=repeat_for_each_map_entry>
  <code>repeat::for_each_map_entry</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat For Dictionary Values\
**Type:** Action without value\
**Description:** Retrieves each element from the specified dictionary and outputs its index and value to the specified variables.

**Usage example:** 
```ts
repeat::for_each_map_entry(`map`){a1, a2->
    player::message("Code in cycle")
}
```

<h3 id=repeat_forever>
  <code>repeat::forever</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat Forever\
**Type:** Action without value\
**Description:** Persistently repeats the code inside the pistons.

**Usage example:** 
```ts
repeat::forever(){
    player::message("Everything work");
}
```

<h3 id=repeat_multi_times>
  <code>repeat::multi_times</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat N Times\
**Type:** Action without value\
**Description:** Runs the code the specified number of times.

**Usage example:** 
```ts
repeat::multi_times(1){a1->
    player::message("Code in cycle")
}
```

<h3 id=repeat_on_circle>
  <code>repeat::on_circle</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Circle\
**Type:** Action without value\
**Description:** Repeat the location of each circle block with the given parameters in sequence.

**Usage example:** 
```ts
repeat::on_circle(location(0,0,0,0,0),1,2,vector(0,0,0),3,"DEGREES"){a1->
    player::message("Code in cycle")
}
```

<h3 id=repeat_on_grid>
  <code>repeat::on_grid</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Grid\
**Type:** Action without value\
**Description:** Repeat the location of each block in the given region into the given variable.

**Usage example:** 
```ts
repeat::on_grid(location(0,0,0,0,0),location(0,0,0,0,0)){a1->
    player::message("Code in cycle")
}
```

<h3 id=repeat_on_path>
  <code>repeat::on_path</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Path\
**Type:** Action without value\
**Description:** Repeat from one location to another in increments, assigning the current location to the specified variable.

**Usage example:** 
```ts
repeat::on_path(1,[location(0,0,0,0,0), location(0,0,0,0,0)],"TRUE"){a1->
    player::message("Code in cycle")
}
```

<h3 id=repeat_on_range>
  <code>repeat::on_range</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Range\
**Type:** Action without value\
**Description:** Assigns the current number to the specified variable from the specified range in increments.

**Usage example:** 
```ts
repeat::on_range(1,2,3){a1->
    player::message("Code in cycle")
}
```

<h3 id=repeat_on_sphere>
  <code>repeat::on_sphere</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat On Sphere\
**Type:** Action without value\
**Description:** Sequentially returns the location of each point on a sphere with the specified parameters.

**Usage example:** 
```ts
repeat::on_sphere(location(0,0,0,0,0),1,2,"NO_CHANGES"){a1->
    player::message("Code in cycle")
}
```

<h3 id=repeat_while>
  <code>repeat::while</code>
  <a href="#" style="font-size: 12px; margin-left:">⬆️</a>
</h3>

**Name:** Repeat By Condition\
**Type:** Action without value\
**Description:** Runs code as long as the selected condition is true.

**Usage example:** 
```ts
repeat::while(a1.exists()){
    player::message("Everything work");
}
```

