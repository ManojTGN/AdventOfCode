CC = gcc
YEAR = 2015
DAY = 01

all: main clean

main:
	$(CC) $(YEAR)/day_$(DAY).c -o build/$(YEAR)/day_$(DAY)
	./build/$(YEAR)/day_$(DAY).exe

clean:
	rm -rf ./build/$(YEAR)/day_$(DAY).exe
