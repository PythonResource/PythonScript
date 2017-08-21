#! /bin/sh
# cd到当前脚本所在目录
cd `dirname $0`

#获取.xcodeproj名称
projectFile=`ls | grep "\.xcodeproj$"`
projectFile=${projectFile/.xcodeproj/''}

PROJECT_NAME="$projectFile" #.xcodeproj名字
TARGET_NAME="$projectFile" #targetName
IPA_NAME="$projectFile.ipa" #输出文件名

#获取workspaceName
workspaceName=`ls | grep "\.xcworkspace"`
workspaceName=${workspaceName/.xcworkspace/''}

WORKSPACE_NAME="$workspaceName"

function buildXcodeproj(){

	xcodebuild -project $1.xcodeproj -target $1 -configuration Release
	if [[ $? == 0 ]]; then
		ipaName="$1`date "+%Y-%m-%d-%H-%M-%S"`.ipa"
		outPutPath=~/Desktop
		xcrun -sdk iphoneos -v PackageApplication ./build/Release-iphoneos/$1.app -o $outPutPath/$ipaName
		if [[ $? == 0 ]]; then
		    echo "ipa文件地址: $outPutPath"
		    open $outPutPath
		fi
	fi
	if [[ $? == 0 ]]; then
		rm -r -f build
	fi

}

function buildWorkspace(){
	buidDir="`pwd`/build"
	xcodebuild -workspace $1.xcworkspace -scheme $1 -configuration Release CONFIGURATION_BUILD_DIR=$buidDir
	if [[ $? == 0 ]]; then
		ipaName="$1`date "+%Y-%m-%d-%H-%M-%S"`.ipa"
		outPutPath=~/Desktop
		xcrun -sdk iphoneos -v PackageApplication ${buidDir}/${PROJECT_NAME}.app -o $outPutPath/$ipaName
		if [[ $? == 0 ]]; then
		    echo "ipa文件地址: $outPutPath"
		    open $outPutPath
		fi
	fi
	if [[ $? == 0 ]]; then
		rm -r -f build
	fi
}

if [[ $WORKSPACE_NAME != '' ]]; then
    buildWorkspace $PROJECT_NAME
    exit
else
    if [[ $PROJECT_NAME != '' ]]; then
        buildXcodeproj $PROJECT_NAME
    else
        echo "没有发现项目文件，请放到项目工程文件夹下!"
	    exit
    fi
fi











