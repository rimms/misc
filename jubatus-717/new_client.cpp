#include <iostream>
#include <string>
#include <vector>

#include <jubatus/client.hpp>

using std::string;
using std::vector;
using jubatus::classifier::labeled_datum;

int main() {
  string host = "127.0.0.1";
  int port = 9199;
  string name = "test";

  int cnt = 0;
  int err = 0;

  while (true) {
    jubatus::classifier::client::classifier client(host, port, name, 0);
    vector<labeled_datum> train_data;

    try {
      ++cnt;
      client.train(train_data);
    } catch (std::exception& e) {
      ++err;
      std::cerr << "fail to request(" << cnt << ") : " << e.what() << std::endl;
      client.get_client().close();
    }

    if (err > 10 || cnt > 100000) break;
  }
}
