This is a simple Conan (conan.io) recipe to build Lua from source and spit out the library, interpreter, and compiler.

Current version is 5.3.5.

To install from the working directory:

    conan create . mukunda/stable

This isn't currently distributed by any official Conan repository.

Protip: When consuming Lua, it's a C library so you can probably get away with linking against a full Release version. To do that you can specify the `build_type` and other compiler configuration specifically for `Lua` in a Conan profile.
