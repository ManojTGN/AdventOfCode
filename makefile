# EDIT ONLY THESE VARIABLES
# -------------------------
YEAR    = 2015
DAY     = 07
PART    = 1
RUN_AFTER_COMPILE = true
# -------------------------



# COMPILE VARIABLES
# -------------------------
CC = gcc
EXTENSION = c
ifeq ($(YEAR)$(DAY)$(PART),2015071)
  CC = g++
  EXTENSION = cpp
endif

VALID_YEAR := $(shell [ $(YEAR) -ge 2015 -a $(YEAR) -le 2024 ] && echo valid || echo invalid)
VALID_DAY := $(shell [ $(DAY) -ge 1 -a $(DAY) -le 25 ] && echo valid || echo invalid)
VALID_PART := $(shell [ $(PART) -eq 1 -o $(PART) -eq 2 ] && echo valid || echo invalid)

OUTPUT_DIR = ./build/$(YEAR)
OUTPUT = $(OUTPUT_DIR)/day_$(DAY)_$(PART)
# -------------------------


# MAIN START OF THE MAKE
# -------------------------
.PHONY: all validate clean

all: validate
	@mkdir -p $(OUTPUT_DIR)
	$(CC) ./$(YEAR)/day_$(DAY)_$(PART).$(EXTENSION) -o $(OUTPUT)
	@echo "Compiled successfully: $(OUTPUT)"
ifeq ($(RUN_AFTER_COMPILE),true)
	@$(OUTPUT)
endif
# ------------------------


# Basic Variable Validation
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
