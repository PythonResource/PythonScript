#!/bin/sh

# 重要: 最好放在项目主目录下执行脚本，否则你会很嗨. 如果不在会出现提示, 请慎重选择
# 删除iOS项目中的注释行

if [[ ! $1 ]]; then
	echo "缺少参数, eg: bash /path/$0 /project/path ."
	exit 0
fi

if [[ ! -d $1 ]]; then
	echo "输入的参数: $1 不是文件夹 ."
	exit 0
fi

# path=$(cd "$(dirname "$0")";pwd)
path=$1
echo ${path}

files=`find ${path} -name "*.xcodeproj"`

if [[ ! ${files} ]]; then
	echo "警告！！！！！当前脚本所在目录下没有iOS项目，请检查脚本所在目录:${path}是否正确！是否忽略路径继续执行删除操作？"
	select isContinue in Yes NO;
	do
		break
	done
	if [[ ! ${isContinue} == 'Yes' ]]; then
		echo "已结束执行!"
		exit 0	
	fi
fi

export LC_COLLATE='C'
export LC_CTYPE='C'

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