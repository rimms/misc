all: test

test: test.cpp
	g++ -O2 -o test test.cpp `pkg-config jubatus_core --libs --cflags` -luuid

clean:
	rm -f test
