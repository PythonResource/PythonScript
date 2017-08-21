#!/bin/sh

# 重要: 一定要放在项目目录下执行脚本，否则你会很嗨.
# 删除iOS项目中的注释行

path=$(cd "$(dirname "$0")";pwd)
echo ${path}

files=`find . -name "*.xcodeproj"`

if [[ ! ${files} ]]; then
	echo "警告！！！！！当前脚本所在目录下没有iOS项目，请检查脚本所在目录:${path}.是否正确！是否忽略路径继续执行删除操作？"
	select isContinue in Yes NO;
	do
		break
	done
	if [[ ! ${isContinue} == 'Yes' ]]; then
		exit 0	
	fi
fi

# 删除 //注释
find ${path} \( -name "*.m" -o  -name "*.h" -o -name "*.mm" \) -print | xargs sed -ig 's/^[[:space:]]*\/\/.*//g'

# 删除 //注释
find ${path} \( -name "*.m" -o  -name "*.h" -o -name "*.mm" \) | xargs sed -ig 's/[[:space:]]\/\/.*//g'

# 删除不跨行 /* */
find ${path} \( -name "*.m" -o  -name "*.h" -o -name "*.mm" \) | xargs sed -ig 's/\/\*.*\*\///g'

# 删除跨行 /* */在行内
find ${path} \( -name "*.m" -o  -name "*.h" -o -name "*.mm" \) | xargs sed -ig '/\W\/\*/,/\*\//d'

# 删除跨行 /* */在行首
find ${path} \( -name "*.m" -o  -name "*.h" -o -name "*.mm" \) | xargs sed -ig '/^[[:space:]]*\/\*/,/\*\//d'

# 删除 #pragma
find ${path} \( -name "*.m" -o  -name "*.h" -o -name "*.mm" \) | xargs sed -ig '/#pragma/d'

# 删除 #warning
find ${path} \( -name "*.m" -o  -name "*.h" -o  -name "*.mm"  \) | xargs sed -ig '/#warning/d'

# 删除备份文件
find ${path} \( -name "*.mg" -o  -name "*.hg" -o  -name "*.mmg" \) | xargs rm