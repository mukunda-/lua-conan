This is a simple Conan (conan.io) recipe to build Lua from source and spit out the library, interpreter, and compiler.

Current version is 5.3.5.

To install from the working directory:

    conan create . mukunda/stable

This isn't currently distributed by any official Conan repository.

Protip: Lua is a simple C library, so you can probably get away with linking your Debug builds against a Release version. You can set in a Conan profile the `build_type` and other compiler options for Lua specifically.
