#include "logger.hpp"

int main(int argc, char **argv) {
  logger::init(argv[1]);

  LOG(FATAL) << "This log is Fatal level via macro: " << 123 << ", " << 4.56;
  LOG(ERROR) << "This log is Error level via macro";
  LOG(WARN) << "This log is Warn level via macro";
  LOG(INFO) << "This log is Info level via macro";
  LOG(DEBUG) << "This log is Debug level via macro";
  LOG(TRACE) << "This log is Trace level via macro";

  return 0;
}

