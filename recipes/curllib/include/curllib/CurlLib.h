#ifndef CURLLIB_H
#define CURLLIB_H

#include <atomic>
#include <string>

#include "curl/curl.h"

namespace curllib {

class CurlLib {
public:
    CurlLib(std::string uri);
    ~CurlLib();
    void set_uri(std::string uri);
    std::string get_uri() const;
    bool send(std::string data);
    std::string today() const;

private:
    CURL* _curl_handle = nullptr;
    std::string _uri;
    std::atomic<long> _timeout_milliseconds;
};

} // namespace curllib

#endif // !CURLLIB_H