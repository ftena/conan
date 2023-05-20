cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(date REQUIRED)

add_executable(example src/main.cpp)

target_include_directories( example PUBLIC ${date_INCLUDE_DIRS} )

message(STATUS "Looking for someheader.h - found ${date_INCLUDE_DIRS}" )
