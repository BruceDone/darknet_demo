#!/usr/bin/env bash
./darknet detector test data/train.data  cfg/train.cfg session/train_final.weights test_imgs/1.jpg -thresh 0.5 -gpus 0