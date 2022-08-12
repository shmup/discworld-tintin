#!/usr/bin/env bash
# requires https://github.com/junegunn/fzf

FUZZ="fzf --no-color --no-sort --info=hidden"
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

SELECTION=$(printf "%s\n" "${BOARDS[@]}" | $FUZZ)

[[ -z $SELECTION ]] && exit 0

eval "$OPENER 'https://discworld.starturtle.net/lpc/secure/boards.c?type=subject&threaded=0&board=$SELECTION'"
