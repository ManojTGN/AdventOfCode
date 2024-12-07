# EDIT ONLY THESE VARIABLES
# -------------------------
YEAR    = 2015
DAY     = 08
PART    = 2
RUN_AFTER_COMPILE = false
# -------------------------



# COMPILE VARIABLES
# -------------------------
CC = gcc
CONST_CC = gcc
FLAGS = -Wall -Wextra -Werror
EXTENSION = c
DEBUGGING = -g
ifeq ($(YEAR)$(DAY)$(PART),2015071)
  CC = g++
  EXTENSION = cpp
else ifeq ($(YEAR)$(DAY)$(PART),2015072)
  CC = g++
  EXTENSION = cpp
endif

VALID_YEAR := $(shell [ $(YEAR) -ge 2015 -a $(YEAR) -le 2024 ] && echo valid || echo invalid)
VALID_DAY := $(shell [ $(DAY) -ge 1 -a $(DAY) -le 25 ] && echo valid || echo invalid)
VALID_PART := $(shell [ $(PART) -eq 1 -o $(PART) -eq 2 ] && echo valid || echo invalid)

BUILD_NAME = main
BUILD_DIR = ./build
OUTPUT_DIR = $(BUILD_DIR)/$(YEAR)
OUTPUT = $(OUTPUT_DIR)/day_$(DAY)_$(PART)
# -------------------------


# MAIN START OF THE MAKE
# -------------------------
.PHONY: all validate clean

all: validate
	@mkdir -p $(BUILD_DIR)
	$(CONST_CC) $(DEBUGGING) -c ./Utils/utils.c -o $(BUILD_DIR)/utils.o
	$(CC) $(DEBUGGING) -c $(FLAGS) ./$(YEAR)/day_$(DAY)_$(PART).$(EXTENSION) -o $(BUILD_DIR)/$(BUILD_NAME).o
	$(CC) $(DEBUGGING) $(BUILD_DIR)/$(BUILD_NAME).o $(BUILD_DIR)/utils.o -o $(BUILD_DIR)/$(BUILD_NAME).exe
	@echo "Compiled successfully: $(OUTPUT)"
ifeq ($(RUN_AFTER_COMPILE),true)
	@$(BUILD_DIR)/$(BUILD_NAME).exe
endif
# ------------------------


# BASIC VARIABLE VALIDATION
# -------------------------
validate:
	@if [ "$(VALID_YEAR)" = "invalid" ]; then \
		echo "Error: YEAR should be between 2015 and 2024."; \
		exit 1; \
	fi
	@if [ "$(VALID_DAY)" = "invalid" ]; then \
		echo "Error: DAY should be between 01 and 25."; \
		exit 1; \
	fi
	@if [ "$(VALID_PART)" = "invalid" ]; then \
		echo "Error: PART should be either 1 or 2."; \
		exit 1; \
	fi
# -------------------------


# CLEANING OUTPUT BUILDS
# -------------------------
clean:
	@rm -rf ./build
	@echo "Cleaned build files."
# -------------------------
