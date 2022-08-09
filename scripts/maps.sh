#!/usr/bin/env bash
# requires https://github.com/jhawthorn/fzy

OPENER=$([[ "$OSTYPE" != "darwin"* ]] && echo xdg-open || echo open )

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

eval "$OPENER 'https://dw.daftjunk.com/access.php?map=$SELECTION'"
