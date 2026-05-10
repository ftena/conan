## Build

- mkdir build
- conan install .. -pr=../../../profiles/gcc11_cxx14_release
- cmake .. -DCMAKE_TOOLCHAIN_FILE=./Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
- make -j16
