set breakpoint pending on
set target-async on
set pagination off
set non-stop on

# RPC「do_mix」の処理でマスタロック取得後、MIX の処理を開始する前
#  https://github.com/jubatus/jubatus/blob/0.8.9/jubatus/server/framework/mixer/linear_mixer.cpp#L322

tbreak ../jubatus/server/framework/mixer/linear_mixer.cpp:322
