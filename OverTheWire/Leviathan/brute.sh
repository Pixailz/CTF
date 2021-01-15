#! /bin/bash

for pin in {0000..9999}; do
	~/leviathan6 $pin && echo "$pin"
done
