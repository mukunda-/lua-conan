cmake_minimum_required( VERSION 3.10 )
project( PackageTest CXX )

include( ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake )
conan_basic_setup()
conan_global_flags()

add_executable( example example.cpp )
target_compile_features( example PRIVATE cxx_std_17 )
target_link_libraries( example ${CONAN_LIBS} )
