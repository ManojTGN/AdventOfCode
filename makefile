# EDIT ONLY THESE VARIABLES
# -------------------------
YEAR    = 2015
DAY     = 09
PART    = 1
RUN_AFTER_COMPILE = true
# -------------------------



# COMPILE VARIABLES
# -------------------------
CC 			= gcc
CONST_CC 	= gcc
FLAGS 		= -Wall -Wextra -Werror
EXTENSION 	= c
DEBUGGING 	= -g

MATCHES 	= 2015071 2015072 2015091
ifneq ($(filter $(YEAR)$(DAY)$(PART),$(MATCHES)),)
  CC = g++
  EXTENSION = cpp
endif

SPL_FLAGS =
ifeq ($(YEAR)$(DAY)$(PART),2015031)
  SPL_FLAGS = -lm
else ifeq ($(YEAR)$(DAY)$(PART),2015032)
  SPL_FLAGS = -lm
else ifeq ($(YEAR)$(DAY)$(PART),2015052)
  SPL_FLAGS = -lm
endif

SPL_FILE =
ifeq ($(YEAR)$(DAY)$(PART),2015041)
  SPL_FILE = ./Utils/md5.c
else ifeq ($(YEAR)$(DAY)$(PART),2015042)
  SPL_FILE = ./Utils/md5.c
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
	$(CC) $(DEBUGGING) $(FLAGS) ./$(YEAR)/day_$(DAY)_$(PART).$(EXTENSION) $(BUILD_DIR)/utils.o $(SPL_FILE) $(SPL_FLAGS) -o $(BUILD_DIR)/$(BUILD_NAME).exe
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
