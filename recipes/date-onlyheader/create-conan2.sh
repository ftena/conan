#!/bin/bash

conan create . --version=3.0.1 --user=ftena --channel=main \
    -pr:h=../../profiles/gcc11_cxx14_release \
    -pr:b=../../profiles/gcc11_cxx14_release
