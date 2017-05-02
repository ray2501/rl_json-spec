# rl_json-spec

openSUSE rl_json RPM spec

[rl_json](https://github.com/RubyLane/rl_json) package adds a command `json` to the interpreter,
and defines a new Tcl_Obj type to store the parsed JSON document.
The `json` command directly manipulates values whose string representation is valid JSON,
in a similar way to how the `dict` command directly manipulates values whose string representation is a valid dictionary.
It is similar to `dict` in performance.
