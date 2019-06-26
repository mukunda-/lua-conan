# CONAN Lua recipe.
#------------------------------------------------------------------------------
from conans import ConanFile, CMake, tools
import shutil

#------------------------------------------------------------------------------
class LuaConan(ConanFile):
   name            = "Lua"
   version         = "5.3.5"
   license         = "MIT"
   author          = "Mukunda Johnson (mukunda@mukunda.com)"
   url             = "http://github.com/mukunda-/lua-conan"
   description     = "Lua library and tools recipe."
   topics          = "lua", "scripting", "tools"
   exports_sources = "CMakeLists.txt", "luaconf.h", "lua.hpp"
   settings        = "os", "compiler", "arch", "build_type"
   generators      = "cmake"

   #---------------------------------------------------------------------------
   def source(self):
      tools.get( "http://www.lua.org/ftp/lua-5.3.5.tar.gz",
                 sha1="112eb10ff04d1b4c9898e121d6bdf54a81482447" )
      shutil.move( "lua-5.3.5/src", "src" )
      shutil.move( "luaconf.h", "src/luaconf.h" )
      shutil.move( "lua.hpp", "src/lua.hpp" )

   #---------------------------------------------------------------------------   
   def build(self):
      cmake = CMake( self )
      cmake.configure()
      cmake.build()

   #---------------------------------------------------------------------------
   def package(self):
      self.copy( "*.h",   src="src", dst="include" )
      self.copy( "*.hpp", src="src", dst="include" )
      
      self.copy( "*.lib",     dst="lib", keep_path = False )
      self.copy( "*.a",       dst="lib", keep_path = False )
      self.copy( "*lua.exe",  dst="bin", keep_path = False )
      self.copy( "*luac.exe", dst="bin", keep_path = False )

   #---------------------------------------------------------------------------
   def package_info(self):
      self.cpp_info.libs = ["lua53"]
