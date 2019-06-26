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
   
   # lto: Use link-time optimization for Release build type.
   options         = { "lto": [True,False] }
   default_options = { "lto": True }

   #---------------------------------------------------------------------------
   def source( self ):
      tools.get( "http://www.lua.org/ftp/lua-5.3.5.tar.gz",
                 sha1="112eb10ff04d1b4c9898e121d6bdf54a81482447" )
      shutil.move( "lua-5.3.5/src", "src" )
      shutil.move( "luaconf.h", "src/luaconf.h" )
      shutil.move( "lua.hpp", "src/lua.hpp" )
   
   #---------------------------------------------------------------------------   
   #def use_lto( self ):
   #   return (self.options.lto and self.settings.compiler == "Visual Studio"
   #           and self.settings.build_type == "Release")
   
   def add_cmake_definition( self, cmake, key, value ):
      if not cmake.definitions[key]:
         cmake.definitions[key] = value
      else:
         cmake.definitions[key] += " " + value
              
   #---------------------------------------------------------------------------   
   def build( self ):
      cmake = CMake( self )
      
      #if self.use_lto():
         #if self.settings.compiler == "Visual Studio":
            
            #cmake.definitions["CONAN_C_FLAGS"] += " /GL /Oi"
            #cmake.definitions["CONAN_EXE_LINKER_FLAGS"] += " /LTCG:incremental"
            #self.add_cmake_definition( cmake, "CONAN_C_FLAGS", "/GL /Oi" )
            # for lua.exe and luac.exe
            #self.add_cmake_definition( cmake, "CONAN_EXE_LINKER_FLAGS", "/LTCG:incremental" )
            
      cmake.configure( 
         defs = {
            "CMAKE_INTERPROCEDURAL_OPTIMIZATION":
               self.options.lto 
               and self.settings.build_type == "Release"
         })
      
      cmake.build()

   #---------------------------------------------------------------------------
   def package( self ):
      self.copy( "*.h",   src="src", dst="include" )
      self.copy( "*.hpp", src="src", dst="include" )
      
      self.copy( "*.lib",     dst="lib", keep_path = False )
      self.copy( "*.a",       dst="lib", keep_path = False )
      self.copy( "*lua.exe",  dst="bin", keep_path = False )
      self.copy( "*luac.exe", dst="bin", keep_path = False )
   
   #---------------------------------------------------------------------------
   def package_info( self ):
      self.cpp_info.libs = ["lua53"]
      if self.options.lto and self.settings.build_type == "Release":
         self.user_info.using_lto = True
         #if self.settings.compiler == "msvc":
         #   self.cpp_info.cflags = ["/GL", "/Oi"]
         #   # Do we need this in the package info?
         #   #self.cpp_info.exelinkflags = ["/LTCG:incremental"]
      
      
