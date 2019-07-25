#! /bin/sh
PATH='dictation-kit-v4.3.1'
./$PATH/bin/osx/julius -C $PATH/main.jconf -C $PATH/am-dnn.jconf -module -dnnconf $PATH/julius.dnnconf $*
