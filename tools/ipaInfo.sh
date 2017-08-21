#! /usr/bin/bash

unzip $1

cd Payload

cd *.app

plistPath=~/Desktop/ipaInfo.plist

security cms -D -i embedded.mobileprovision > ${plistPath}

open ~/Desktop/ipaInfo.plist