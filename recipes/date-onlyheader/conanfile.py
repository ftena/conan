from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get, replace_in_file, copy
import os

class DateConan(ConanFile):
    name = "date"
    url = "https://github.com/ftena/conan"
    homepage = "https://github.com/HowardHinnant/date"
    description = "A date and time library based on the C++11/14/17 <chrono> header"
    topics = ("datetime", "timezone", "calendar", "time", "iana-database")
    license = "MIT"

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
      tc = CMakeToolchain(self)
      tc.generate()
      deps = CMakeDeps(self)
      deps.generate()

    def source(self
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "LICENSE.txt", dst=os.path.join(self.package_folder, "licenses"), src=self.source_folder)
        src = os.path.join(self.source_folder, "include", "date")
        dst = os.path.join(self.package_folder, "include", "date")
        copy(self, "date.h", dst=dst, src=src)
        copy(self, "tz.h", dst=dst, src=src)
        copy(self, "ptz.h", dst=dst, src=src)
        copy(self, "iso_week.h", dst=dst, src=src)
        copy(self, "julian.h", dst=dst, src=src)
        copy(self, "islamic.h", dst=dst, src=src)

    def package_info(self):
        self.cpp_info.set_property("cmake_target_name", "date::date")
        self.cpp_info.names["cmake_find_package"] = "date"
        self.cpp_info.names["cmake_find_package_multi"] = "date"
        self.cpp_info.includedirs = ["include"]
