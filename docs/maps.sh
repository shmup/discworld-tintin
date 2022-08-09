#!/usr/bin/env bash
# requires https://github.com/jhawthorn/fzy

MAPS=(
	"Ankh-Morpork"
	"Bes_Pelargic"
	"Djelibeybi"
	"Ramtops"
	"Genua"
	"Sto_Lat"
	"Uberwald"
)

SELECTION=$(printf "%s\n" "${MAPS[@]}" | fzy -l 40)

[[ -z $SELECTION ]] && exit 0

xdg-open "https://dw.daftjunk.com/access.php?map=$SELECTION"
