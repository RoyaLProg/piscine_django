#/bin/sh

TARGET="$1"

if [ -z $TARGET ]; then
	exit 1
fi

curl -sli "$TARGET" | grep "Location" | cut -c 11-
