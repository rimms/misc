#include <iostream>
#include <time.h>
#include <uuid/uuid.h>
#include <string>
#include <vector>

#include <jubatus/util/data/unordered_map.h>

using jubatus::util::data::unordered_map;


std::string gen_uuid() {
  uuid_t u;
  char buf[37];

  uuid_generate(u);
  uuid_unparse(u, buf);

  return std::string(buf);
}

int main() {
  std::vector<std::string> v1, v2;
  unordered_map<std::string, size_t> m1, m2;

  for (size_t i = 0; i < 10000000; ++i) {
    std::string uuid;
    uuid = gen_uuid();

    v1.push_back(uuid);
    m1[uuid] = 1;
    v2.push_back(uuid + uuid);
    m2[uuid + uuid] = 1;
  }

  std::string t1, t2;
  t1 = v1[v1.size() - 1];
  t2 = v2[v2.size() - 1];

  clock_t start, end;

  start= clock();
  for (size_t i = 0; i < v1.size(); ++i) {
    unordered_map<std::string, size_t>::iterator iter = m1.find(t1);
  }
  end = clock();
  std::cout << (double) (end - start) / CLOCKS_PER_SEC << std::endl;

  start = clock();
  for (size_t i = 0; i < v2.size(); ++i) {
    unordered_map<std::string, size_t>::iterator iter = m2.find(t2);
  }
  end = clock();
  std::cout << (double) (end - start) / CLOCKS_PER_SEC << std::endl;
}
