#ifndef LOGGER_LOGGER_HPP_
#define LOGGER_LOGGER_HPP_

#include <sstream>
#include <log4cxx/level.h>

#include <jubatus/util/lang/noncopyable.h>

#define FATAL ::log4cxx::Level::FATAL_INT
#define ERROR ::log4cxx::Level::ERROR_INT
#define WARN  ::log4cxx::Level::WARN_INT
#define INFO  ::log4cxx::Level::INFO_INT
#define DEBUG ::log4cxx::Level::DEBUG_INT
#define TRACE ::log4cxx::Level::TRACE_INT

#define LOG(level) ::logger::stream_logger(level, __FILE__, __LINE__)

namespace logger {

class stream_logger : jubatus::util::lang::noncopyable {
 public:
  stream_logger(const int level, const char* file, const int line);
  ~stream_logger();

  template <typename T>
  inline stream_logger& operator<<(const T& msg) {
    buf_ << msg;
    return *this;
  }

 private:
  const int level_;
  const char* file_;
  const int line_;
  std::ostringstream buf_;
};

/**
 * Initializes the logging library. (standard output)
 */
void init();

/**
 * Initializes the logging library with given config file.
 */
void init(const std::string&);

}  // namespace logger

#endif  // LOGGER_LOGGER_HPP_
