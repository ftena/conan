#include "curllib/CurlLib.h"

#include <iostream>
#include <memory>

int main() {
    int result = EXIT_SUCCESS;

    try {
        auto curl_lib = std::make_shared<curllib::CurlLib>("http://example.com/api");
        curl_lib->get_uri();
        curl_lib->set_uri("http://example.com");
        curl_lib->get_uri();
        std::cout << "OK" << std::endl;
    } catch(const std::exception& ex) {
        std::cout << "ERROR: " << ex.what() << std::endl;
        result = EXIT_FAILURE;
    } catch(...) {
        std::cout << "ERROR unknown" << std::endl;
        result = EXIT_FAILURE;
    }

    return result;
}
