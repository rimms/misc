#include "logger.hpp"

#include <log4cxx/logger.h>
#include <log4cxx/basicconfigurator.h>
#include <log4cxx/xml/domconfigurator.h>

namespace logger {

// enough to use only one logger
log4cxx::LoggerPtr main_logger = log4cxx::Logger::getLogger("sample");

void logger::init(const std::string& config_file) {
  if (config_file.empty()) {
    log4cxx::BasicConfigurator::configure();
  } else {
    // If failed to perse, not throw exception (maybe log4cxx's specification)
    log4cxx::xml::DOMConfigurator::configure(config_file);
  }
}

void logger::log(log4cxx::LevelPtr level, const std::string& msg, const char* file, int line) {
  if (main_logger->isEnabledFor(level)) {
    main_logger->forcedLog(level, msg, log4cxx::spi::LocationInfo(file, "", line));
  }
}

void logger::log(const std::string& level, const std::string& msg, const char* file, int line) {
  log(log4cxx::Level::toLevel(level), msg, file, line);
}

void logger::fatal(const std::string& msg, const char* file, int line) {
  log(log4cxx::Level::getFatal(), msg, file, line);
}

void logger::error(const std::string& msg, const char* file, int line) {
  log(log4cxx::Level::getError(), msg, file, line);
}

void logger::warn(const std::string& msg, const char* file, int line) {
  log(log4cxx::Level::getWarn(), msg, file, line);
}

void logger::info(const std::string& msg, const char* file, int line) {
  log(log4cxx::Level::getInfo(), msg, file, line);
}

void logger::debug(const std::string& msg, const char* file, int line) {
  if (LOG4CXX_UNLIKELY(main_logger->isDebugEnabled())) {
    main_logger->forcedLog(log4cxx::Level::getDebug(), msg, log4cxx::spi::LocationInfo(file, "", line));
  }
}

void logger::trace(const std::string& msg, const char* file, int line) {
  if (LOG4CXX_UNLIKELY(main_logger->isTraceEnabled())) {
    main_logger->forcedLog(log4cxx::Level::getTrace(), msg, log4cxx::spi::LocationInfo(file, "", line));
  }
}

}  // logger
