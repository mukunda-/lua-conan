// CONAN Lua test code.
//
// A small program that consumes the Lua library.
///////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string_view>
#include <lua.hpp>

// A simple Lua program to print some text.
const std::string_view luacode = R"///(

   print( "Hello from Lua! :)" )

)///";

///////////////////////////////////////////////////////////////////////////////
// RAII Lua state.
struct LuaState {
   lua_State *state = nullptr;
   
   LuaState() {
      state = luaL_newstate();
      luaL_openlibs( state );
   };
   
   ~LuaState() {
      if( state )
         lua_close( state );
   }
   
   operator lua_State *() {
      return state;
   }
};

///////////////////////////////////////////////////////////////////////////////
int main( int argc, char *argv[] ) {
   // Create a new Lua state, load our Lua snippet, and then execute it.
   LuaState L;
   int error = luaL_loadbuffer( L, luacode.data(), luacode.length(), "func" )
               || lua_pcall( L, 0, 0, 0 );
   
   // Report any errors.
   if( error ) {
      std::cout << "Got error from Lua: " << lua_tostring( L, -1 ) << "\n";
      return -1;
   }
   
   return 0;
}
///////////////////////////////////////////////////////////////////////////////
