#!/usr/bin/env bash
# requires https://github.com/jhawthorn/fzy

OPENER=$([[ "$OSTYPE" != "darwin"* ]] && echo xdg-open || echo open )

BOARDS=(
	"ankh+morpork+council"
	"djelibeybi+council"
	"newspaper"
	"alt.fan.pratchett"
	"announcements"
	"equality"
	"flame"
	"fluff"
	"frog"
	"never+wending+story"
	"player+killers"
	"role-playing"
	"assassinsguild"
	"foolsguild"
	"priestsguild"
	"thievesguild"
	"warriorsguild"
	"witchesguild"
	"wizardsguild"
)

SELECTION=$(printf "%s\n" "${BOARDS[@]}" | fzy -l 40)

[[ -z $SELECTION ]] && exit 0

eval "$OPENER 'https://discworld.starturtle.net/lpc/secure/boards.c?type=subject&threaded=0&board=$SELECTION'"
