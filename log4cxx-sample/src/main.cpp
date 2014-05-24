#include "logger.hpp"

int main(int argc, char **argv) {
  using logger::logger;
  logger::init(argv[1]);

  // specify level on method
  logger::fatal("This log is Fatal level via logger::fatal", __FILE__, __LINE__);
  logger::error("This log is Error level via logger::error", __FILE__, __LINE__);
  logger::warn("This log is Warn level via logger::warn", __FILE__, __LINE__);
  logger::info("This log is Info level via logger::info", __FILE__, __LINE__);
  logger::debug("This log is Debug level via logger::debug", __FILE__, __LINE__);
  logger::trace("This log is Trace level via logger::trace", __FILE__, __LINE__);

  // specify level string
  logger::log("fatal", "This log is Fatal level via logger::log", __FILE__, __LINE__);
  logger::log("FATAL", "This log is FATAL level via logger::log", __FILE__, __LINE__);
  logger::log("error", "This log is Error level via logger::log", __FILE__, __LINE__);
  logger::log("warn", "This log is Warn level via logger::log", __FILE__, __LINE__);
  logger::log("info", "This log is Info level via logger::log", __FILE__, __LINE__);
  logger::log("debug", "This log is Debug level via logger::log", __FILE__, __LINE__);
  logger::log("trace", "This log is Trace level via logger::log", __FILE__, __LINE__);

  LOG(FATAL, "This log is Fatal level via macro");
  LOG(ERROR, "This log is Error level via macro");
  LOG(WARN, "This log is Warn level via macro");
  LOG(INFO, "This log is Info level via macro");
  LOG(DEBUG, "This log is Debug level via macro");
  LOG(TRACE, "This log is Trace level via macro");

  return 0;
}

