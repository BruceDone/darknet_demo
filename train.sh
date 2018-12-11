#!/usr/bin/env bash
echo "use the old darknet53.conv.74 to transfer learning the model"
./darknet detector train data/train.data cfg/train.cfg weights/darknet53.conv.74 -gpus 1,2,3,4,5,6

#echo "train with last one "
#./darknet detector train data/train.data cfg/train.cfg session/train_10000.weights -gpus 1,2,3,4,5,6