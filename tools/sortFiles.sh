#! /usr/bin/bash

# 将指定文件夹下的所有文件(不包括文件夹)按文件名首字符分类

if [[ $# != 1 ]]; then
	echo error: missing parameter;
	echo Usage: bash $0 /directory/path;
	exit;
fi

path=$1
final=${path: -1}
# echo final : $final
if [[ "${final}" != "/" ]]; then
	path=$path/;
	# echo Woking in directory: + $path;
fi
echo Woking in directory: $path

for file in `ls $path`;do
	subDir=${file:0:1};
	subDir="$(echo $subDir | tr '[A-Z]' '[a-z]')"
	dirPath=$path$subDir;
	filePath=$path$file;

	if [[ -d $filePath ]]; then
		continue;
	fi

	echo Coping: $filePath;
	
	if [[ ! -d $dirPath ]]; then
		mkdir $dirPath;	
	fi
	cp $filePath $dirPath;
done