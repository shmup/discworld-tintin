.PHONY: run

all: run

run: ; tt++ discworld.tin

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
