all: new_client one_client

new_client: new_client.cpp
	g++ -O2 -o new_client new_client.cpp `pkg-config jubatus-client --libs --cflags`

one_client: one_client.cpp
	g++ -O2 -o one_client one_client.cpp `pkg-config jubatus-client --libs --cflags`

clean:
	rm -f new_client one_client
