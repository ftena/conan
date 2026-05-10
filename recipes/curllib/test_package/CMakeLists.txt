cmake_minimum_required(VERSION 3.25)
project(test_package)

find_package(curllib CONFIG REQUIRED)

set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -fno-diagnostics-show-caret")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -O0 -g --coverage -fno-inline -fno-diagnostics-show-caret")

add_executable(test_package test_package.cpp)
target_link_libraries(test_package
    curllib::curllib
)
