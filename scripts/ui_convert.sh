#!/bin/bash

source_path=$1
destination_path=$2

if [[ -z "$source_path" ]];
then
  source_path="."
fi

if [[ -z "$destination_path" ]];
then
  destination_path="ui_generated"
fi

if [[ ! -d "$destination_path" ]];
then
  mkdir $destination_path
fi

for file in ${source_path%.*}/*.ui
  do
    name="${file##*/}";
    echo $file
    pyuic5 -x $file -o $destination_path/ui_${name%.*}.py;
done

exit 0
