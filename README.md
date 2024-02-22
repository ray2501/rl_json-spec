# rl_json-spec

openSUSE Tumbleweed RPM spec for rl_json

[rl_json](https://github.com/RubyLane/rl_json) package adds a command `json`
to the interpreter, and defines a new Tcl_Obj type to store the parsed JSON
document. The `json` command directly manipulates values whose string
representation is valid JSON, in a similar way to how the `dict` command
directly manipulates values whose string representation is a valid dictionary.
It is similar to `dict` in performance.

Warning:  
I don't know how to pass openSUSE Tumbleweed LTO check for static library,
even I add the related flags. So now the static library and header files is
removed.

