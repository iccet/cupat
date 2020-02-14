#!/bin/bash

for file in static/ui/*.ui;
      do
          name="${file##*/}";
          pyuic5 -x $file -o src/gui/ui_generated/ui_${name%.*}.py;
done

exit 0