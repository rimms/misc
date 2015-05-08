set breakpoint pending on
set target-async on
set pagination off
set non-stop on
set check range off
set check type off
set language c++

# Jubatus 0.6.6
# https://github.com/jubatus/jubatus/blob/0.6.6/jubatus/server/framework/mixer/push_mixer.cpp#L417
break ../jubatus/server/framework/mixer/push_mixer.cpp:417
