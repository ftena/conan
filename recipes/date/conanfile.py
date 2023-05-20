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
    exports_sources = "CMakeLists.txt"
    settings = "os", "arch", "compiler", "build_type"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "header_only": [True, False],
        "use_system_tz_db": [True, False],
        "use_tz_db_in_dot": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "header_only": True,
        "use_system_tz_db": False,
        "use_tz_db_in_dot": False,
    }

    def generate(self):
      deps = CMakeDeps(self)
      deps.generate()
      tc = CMakeToolchain(self)
      tc.generate()

    def requirements(self):
        if not self.options.header_only and not self.options.use_system_tz_db:
            self.requires("libcurl/8.0.1")

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        if self.options.header_only:
            src = os.path.join(self.source_folder, "include", "date")
            dst = os.path.join(self.package_folder, "include", "date")
            copy(self, "date.h", dst=dst, src=src)
            copy(self, "tz.h", dst=dst, src=src)
            copy(self, "ptz.h", dst=dst, src=src)
            copy(self, "iso_week.h", dst=dst, src=src)
            copy(self, "julian.h", dst=dst, src=src)
            copy(self, "islamic.h", dst=dst, src=src)
        else:
            cmake = CMake(self)
            cmake.install()
            rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))
            rmdir(self, os.path.join(self.package_folder, "CMake"))

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "date"
        self.cpp_info.names["cmake_find_package_multi"] = "date"
        self.cpp_info.includedirs = ["."]
        use_system_tz_db = 0 if self.options.use_system_tz_db else 1
        defines = ["USE_AUTOLOAD={}".format(use_system_tz_db),
                   "HAS_REMOTE_API={}".format(use_system_tz_db)]
        self.cpp_info.defines.extend(defines)
