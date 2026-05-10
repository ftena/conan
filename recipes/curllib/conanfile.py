from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout

class curllibRecipe(ConanFile):
    name = "curllib"
    package_type = "library"
    description = ""
    author = "Fran Tena"
    url = "https://github.com/ftena"
    license = "MIT"
    topics = ("")
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "CMakeLists.txt", "cmake/*", "src/*", "include/*"
    options = { "shared":[True,False] }
    default_options = { "shared": True }

    def requirements(self):
        self.requires("date/3.0.3")
        self.requires("libcurl/8.4.0", transitive_headers=True)
        self.requires("rapidjson/1.1.0")
        self.requires("spdlog/1.9.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)

        tc.variables["BUILD_SHARED_LIBS"] = self.options.shared
        tc.variables["CMAKE_ARCHIVE_OUTPUT_DIRECTORY"] = "lib"
        tc.variables["CMAKE_LIBRARY_OUTPUT_DIRECTORY"] = "lib"
        tc.variables["CMAKE_RUNTIME_OUTPUT_DIRECTORY"] = "bin"
        tc.variables['CMAKE_POSITION_INDEPENDENT_CODE'] = True
        tc.generate()

        cmake_deps = CMakeDeps(self)
        cmake_deps.generate()


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["curllib"]
