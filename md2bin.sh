#!/bin/bash

sed s/'^.*: '// $1 | sed s/'  .*'// | sed s/' '/'\n'/g | sed 's/..../&\n/' > dualimageheaderascii
python3 ascii2bin.py
rm -f dualimageheaderascii
