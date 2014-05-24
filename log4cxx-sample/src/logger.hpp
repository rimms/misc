#ifndef LOGGER_LOGGER_HPP_
#define LOGGER_LOGGER_HPP_

#include <string>

#include <log4cxx/logger.h>
#include <log4cxx/level.h>
#include <jubatus/util/lang/noncopyable.h>


namespace logger {

class logger : jubatus::util::lang::noncopyable {
 public:
  static void init(const std::string& config_file);

  static void log(log4cxx::LevelPtr level, const std::string& msg, const char* file, int line);
  static void log(const std::string& level, const std::string& msg, const char* file, int line);

  static void fatal(const std::string& msg, const char* file, int line);
  static void error(const std::string& msg, const char* file, int line);
  static void warn(const std::string& msg, const char* file, int line);
  static void info(const std::string& msg, const char* file, int line);
  static void debug(const std::string& msg, const char* file, int line);
  static void trace(const std::string& msg, const char* file, int line);
};

}  // logger

#define LOG_FATAL(msg) \
  logger::logger::fatal(msg, __FILE__, __LINE__)

#define LOG_ERROR(msg) \
  logger::logger::error(msg, __FILE__, __LINE__)

#define LOG_WARN(msg) \
  logger::logger::warn(msg, __FILE__, __LINE__)

#define LOG_INFO(msg) \
  logger::logger::info(msg, __FILE__, __LINE__)

#define LOG_DEBUG(msg) \
  logger::logger::debug(msg, __FILE__, __LINE__)

#define LOG_TRACE(msg) \
  logger::logger::trace(msg, __FILE__, __LINE__)

#define LOG(level, msg) LOG_##level(msg)

#endif  // LOGGER_LOGGER_HPP_
