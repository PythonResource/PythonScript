#!/bin/sh

# 重要: 一定要放在项目目录下执行脚本，否则你会很嗨.
# 删除安卓项目中的注释行

path=$(cd "$(dirname "$0")";pwd)
echo ${path}

# 删除不跨行 <!-- --> 在行首
find ${path} \( -name "*.java" -o -name "*.xml" \) | xargs sed -ig 's/<!--.*-->//g'

# 删除 //注释
find ${path} \( -name "*.java" -o -name "*.xml" \) | xargs sed -ig 's/^[[:space:]]*\/\/.*//g'

# 删除 //注释
find ${path} \( -name "*.java" -o -name "*.xml" \) | xargs sed -ig 's/[[:space:]]\/\/.*//g'

# 删除不跨行 /* */
find ${path} \( -name "*.java" -o -name "*.xml" \) | xargs sed -ig 's/\/\*.*\*\///g'

# 删除跨行 /* */在行内
find ${path} \( -name "*.java" -o -name "*.xml" \) | xargs sed -ig '/\W\/\*/,/\*\//d'

# 删除跨行 /* */在行首
find ${path} \( -name "*.java" -o -name "*.xml" \) | xargs sed -ig '/^[[:space:]]*\/\*/,/\*\//d'

# 删除备份文件
find ${path} \( -name "*.javag" -o  -name "*.xmlg" \) | xargs rm