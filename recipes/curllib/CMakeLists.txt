cmake_minimum_required(VERSION 3.25)
set(FULL_PROJECT_VERSION "0.0.1")
project(curllib VERSION ${FULL_PROJECT_VERSION})

option(BUILD_SHARED_LIBS "Build using shared libraries" ON)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -fno-diagnostics-show-caret")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -O0 -g --coverage -fno-inline -fno-diagnostics-show-caret")

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})

add_library(${PROJECT_NAME}
    src/CurlLib.cpp
)

find_package(CURL REQUIRED)
find_package(RapidJSON REQUIRED)
find_package(date REQUIRED)
find_package(OpenSSL REQUIRED)
find_package(ZLIB REQUIRED)
find_package(spdlog REQUIRED)

target_link_libraries(${PROJECT_NAME} PRIVATE
    CURL::libcurl
    date::date
    rapidjson
    openssl::openssl # required for curl
    ZLIB::ZLIB # required for curl
    spdlog::spdlog
)

target_link_options(${PROJECT_NAME} PRIVATE -Wl,--exclude-libs,ALL)

target_include_directories(${PROJECT_NAME}
    PUBLIC ${PROJECT_SOURCE_DIR}/include
    PUBLIC ${CMAKE_INCLUDE_PATH}
)

install(DIRECTORY "${CMAKE_SOURCE_DIR}/include/curllib" # source directory
    DESTINATION "include"   # target directory
    FILES_MATCHING          # install only matched header files
    PATTERN "*.h"
)

install(TARGETS ${PROJECT_NAME}
    ARCHIVE
    LIBRARY
    RUNTIME
    COMPONENT ${PROJECT_NAME}
)
