cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES CXX)

find_package(date REQUIRED CONFIG)

add_executable(example src/main.cpp)

target_include_directories( example PUBLIC ${date_INCLUDE_DIRS} )

message(STATUS "Headers dir: ${date_INCLUDE_DIRS}" )

