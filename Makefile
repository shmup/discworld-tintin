.PHONY: map all build-docs chat run setup standalone-setup clean test

all: setup

build-docs:
	rm -rf docs/manual
	mkdir -p tmp/manual
	cd tmp/manual && \
		time httrack \
		  --max-rate=0 \
		  --disable-security-limits \
		  --sockets=99 \
		  --keep-alive \
		  --connection-per-second= \
		  "https://tintin.mudhalla.net/manual/"
	rm -rf manual
	mv tmp/manual/tintin.mudhalla.net/manual docs/manual

chat:
	tail -f logs/chat.log

donk-routes:
	cat txt/donk_routes.txt | scripts/graphroutes.py
	mv donk_routes.png pics/
	rm donk_routes

play:
	tt++ discworld.tin

map:
	tail -f data/map.txt

setup:
	mkdir -p logs && touch logs/chat.log
	./scripts/tmux-setup.sh


sync-to-dyngeon:
	rsync -avzp . dungeon.red:backups/Ark/Games/muds/discworld-tt/


standalone-setup:
	mkdir -p logs && touch logs/chat.log
	./scripts/tmux-setup.sh standalone
