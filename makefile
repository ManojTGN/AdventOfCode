CC = gcc
YEAR = 2015
DAY = 06
PART = 2

all: main clean

main:
	$(CC) $(YEAR)/day_$(DAY)_$(PART).c -o build/$(YEAR)/day_$(DAY)_$(PART)
	./build/$(YEAR)/day_$(DAY)_$(PART).exe

clean:
	rm -rf ./build/$(YEAR)/day_$(DAY)_$(PART).exe
