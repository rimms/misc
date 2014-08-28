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

  while (true) {
    jubatus::classifier::client::classifier client(host, port, name, 0);
    vector<labeled_datum> train_data;

    try {
      client.train(train_data);
    } catch (std::exception& e) {
      std::cerr << "fail to request: " << e.what() << std::endl;
      client.get_client().close();
    }
  }
}
