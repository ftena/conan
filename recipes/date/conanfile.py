from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get, replace_in_file, copy
import os

class DateConan(ConanFile):
    name = "date"
    version = "3.0.1"
    description = "A date and time library based on the C++11/14/17 <chrono> header"
    url = "https://github.com/ftena/conan"
    homepage = "https://github.com/HowardHinnant/date"
    author = "howard.hinnant@gmail.com"
    license = "MIT"
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False], "use_system_tz_db": [True, False],
               "use_tz_db_in_dot": [True, False]}
    default_options = {"shared": False, "fPIC": True, "use_system_tz_db": True, "use_tz_db_in_dot": False}

    def generate(self):
      deps = CMakeDeps(self)
      deps.generate()
      tc = CMakeToolchain(self)
      tc.generate()

    def requirements(self):
        if not self.options.use_system_tz_db:
            self.requires("libcurl/7.64.1@zinnion/stable")

    def source(self):
        get(self, "{0}/archive/v{1}.tar.gz".format(self.homepage, self.version),
                  sha256="7a390f200f0ccd207e8cff6757e04817c1a0aec3e327b006b7eb451c57ee3538")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        copy(self, "*.h", self.source_folder, os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "date"
        self.cpp_info.names["cmake_find_package_multi"] = "date"
        self.cpp_info.components["date"].names["cmake_find_package"] = "date"
        self.cpp_info.components["date"].includedirs = ["."]
        self.cpp_info.libs.append("pthread")
        use_system_tz_db = 0 if self.options.use_system_tz_db else 1
        defines = ["USE_AUTOLOAD={}".format(use_system_tz_db),
                   "HAS_REMOTE_API={}".format(use_system_tz_db)]
        self.cpp_info.defines.extend(defines)
