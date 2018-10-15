#!/bin/sh
../../crf_learn -f 3 -c 4.0 template bendibao.train model
../../crf_test -m model bendibao.test > $1

