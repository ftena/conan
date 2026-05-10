#include "curllib/CurlLib.h"

#include "date/date.h"
#include "spdlog/spdlog.h"

namespace curllib {

CurlLib::CurlLib(std::string uri): _uri(uri), _timeout_milliseconds(2000)
{ 
    curl_global_init(CURL_GLOBAL_DEFAULT);
    _curl_handle = curl_easy_init();
}

CurlLib::~CurlLib() {
    if (_curl_handle) {
        curl_easy_cleanup(_curl_handle);
        _curl_handle = nullptr;
    }
    curl_global_cleanup();
}

void CurlLib::set_uri(std::string uri) {
    spdlog::info("{} - New URI: {}", today(), uri);
    _uri = uri;
}

std::string CurlLib::get_uri() const {
    spdlog::info("{} - Current URI: {}", today(), _uri);
    return _uri;
}

bool CurlLib::send(std::string data)
{
    bool result = false;

    if (!_curl_handle) {
        spdlog::error("curl_easy_init() failed.");
        return result;
    }

    try {
        curl_easy_setopt(_curl_handle, CURLOPT_URL, _uri.c_str());
        curl_easy_setopt(_curl_handle, CURLOPT_TIMEOUT_MS, 1000);
        curl_easy_setopt(_curl_handle, CURLOPT_NOSIGNAL, 1);
        curl_easy_setopt(_curl_handle, CURLOPT_COPYPOSTFIELDS, data.c_str()); // force to copy data

        CURLcode res = curl_easy_perform(_curl_handle); // perform the request
        if (CURLE_OK == res) {
            spdlog::info("curl_easy_perform() successful. URI {}", _uri);
            result = true;
        } else {
            spdlog::error("curl_easy_perform() failed. URI: {} , error {}", _uri, curl_easy_strerror(res));
        }
    } catch(const std::exception& e) {
        spdlog::error("Error, exception: {}", e.what());
    }

    return result;
}

std::string CurlLib::today() const {
    auto today = date::floor<date::days>(std::chrono::system_clock::now());
    return date::format("%F", today);
}

} // namespace curllib
