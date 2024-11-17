CC = gcc
YEAR = 2015
DAY = 06
PART = 1

all: clean main

main:
	if [ ! -d build/$(YEAR) ]; then mkdir build/$(YEAR); fi
	$(CC) $(YEAR)/day_$(DAY)_$(PART).c -o build/$(YEAR)/day_$(DAY)_$(PART)
	./build/$(YEAR)/day_$(DAY)_$(PART).exe

clean:
	rm -rf "./build/$(YEAR)/day_$(DAY)_$(PART).exe"
