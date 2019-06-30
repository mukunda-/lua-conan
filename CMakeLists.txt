#------------------------------------------------------------------------------
# CMake buildscript for Lua 5.3.5
#------------------------------------------------------------------------------
cmake_minimum_required( VERSION 3.15 )
project( lua C )

# Import compiler settings from CONAN.
include( ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake )
conan_basic_setup()

if( NOT LUA_DISABLE_IPO )
   set( CMAKE_INTERPROCEDURAL_OPTIMIZATION_RELEASE True )
endif()

#------------------------------------------------------------------------------
# List of source files.
#------------------------------------------------------------------------------
set( LIB_FILES
   src/lapi.c       src/lcode.c       src/lctype.c      src/ldebug.c
   src/ldo.c        src/ldump.c       src/lfunc.c       src/lgc.c
   src/llex.c       src/lmem.c        src/lobject.c     src/lopcodes.c
   src/lparser.c    src/lstate.c      src/lstring.c     src/ltable.c
   src/ltm.c        src/lundump.c     src/lvm.c         src/lzio.c
   src/lauxlib.c    src/lbaselib.c    src/lbitlib.c     src/lcorolib.c
   src/ldblib.c     src/liolib.c      src/lmathlib.c    src/loslib.c
   src/lstrlib.c    src/ltablib.c     src/lutf8lib.c    src/loadlib.c
   src/linit.c
)

#------------------------------------------------------------------------------
# Main Lua library target.
#------------------------------------------------------------------------------
add_library( lua53 ${LIB_FILES} )

#------------------------------------------------------------------------------
# Lua interpreter target.
#------------------------------------------------------------------------------
add_executable( lua src/lua.c )
target_link_libraries( lua lua53 )
set_target_properties( lua PROPERTIES DEBUG_POSTFIX "d" )

#------------------------------------------------------------------------------
# Lua compiler target.
#------------------------------------------------------------------------------
add_executable( luac src/luac.c )
target_link_libraries( luac lua53 )
