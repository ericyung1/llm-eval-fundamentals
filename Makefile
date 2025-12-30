# LLM Eval Fundamentals Course - Makefile
# =========================================

PYTHON := python3
VENV := venv
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest

.PHONY: setup test lesson check progress clean help

# Default target
help:
	@echo "LLM Eval Fundamentals Course"
	@echo "============================"
	@echo ""
	@echo "Available commands:"
	@echo "  make setup      - Create virtual environment and install dependencies"
	@echo "  make test       - Run all pytest tests"
	@echo "  make lesson N   - Display lesson N instructions (e.g., make lesson 1)"
	@echo "  make check N    - Run checkpoint for lesson N (e.g., make check 1)"
	@echo "  make progress   - Show your current progress"
	@echo "  make clean      - Remove virtual environment and cache files"
	@echo ""

# Setup virtual environment and install dependencies
setup:
	@echo "🔧 Setting up virtual environment..."
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo ""
	@echo "✅ Setup complete!"
	@echo ""
	@echo "To activate the virtual environment, run:"
	@echo "  source venv/bin/activate"
	@echo ""
	@echo "Then start with:"
	@echo "  make lesson 1"

# Run all tests
test:
	@if [ -d "$(VENV)" ]; then \
		$(PYTEST) tests/ -v; \
	else \
		echo "❌ Virtual environment not found. Run 'make setup' first."; \
		exit 1; \
	fi

# Display lesson content
lesson:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Usage: make lesson N (e.g., make lesson 1)"; \
	else \
		LESSON_NUM=$$(printf "%02d" $(filter-out $@,$(MAKECMDGOALS))); \
		LESSON_FILE=$$(ls lessons/$${LESSON_NUM}_*.md 2>/dev/null | head -1); \
		if [ -f "$$LESSON_FILE" ]; then \
			echo ""; \
			echo "📖 Opening Lesson $(filter-out $@,$(MAKECMDGOALS))"; \
			echo "   File: $$LESSON_FILE"; \
			echo ""; \
			echo "─────────────────────────────────────────────────────"; \
			cat "$$LESSON_FILE"; \
			echo ""; \
			echo "─────────────────────────────────────────────────────"; \
			echo ""; \
			echo "When ready, run: make check $(filter-out $@,$(MAKECMDGOALS))"; \
		else \
			echo "❌ Lesson $(filter-out $@,$(MAKECMDGOALS)) not found."; \
			echo "Available lessons:"; \
			ls -1 lessons/*.md 2>/dev/null || echo "  No lessons found."; \
		fi \
	fi

# Run checkpoint for a lesson
check:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Usage: make check N (e.g., make check 1)"; \
	else \
		LESSON_NUM=$(filter-out $@,$(MAKECMDGOALS)); \
		PADDED_NUM=$$(printf "%02d" $$LESSON_NUM); \
		CHECK_SCRIPT="checkpoints/check_$${PADDED_NUM}.py"; \
		TEST_FILE="tests/test_lesson_$${PADDED_NUM}.py"; \
		echo ""; \
		echo "🔍 Running checkpoint for Lesson $$LESSON_NUM..."; \
		echo ""; \
		if [ -f "$$CHECK_SCRIPT" ]; then \
			$(PYTHON) "$$CHECK_SCRIPT" && echo "" && echo "✅ Checkpoint $$LESSON_NUM PASSED!" || echo "" && echo "❌ Checkpoint $$LESSON_NUM FAILED. Keep working!"; \
		elif [ -f "$$TEST_FILE" ]; then \
			if [ -d "$(VENV)" ]; then \
				$(PYTEST) "$$TEST_FILE" -v && echo "" && echo "✅ Checkpoint $$LESSON_NUM PASSED!" || (echo "" && echo "❌ Checkpoint $$LESSON_NUM FAILED. Keep working!"); \
			else \
				echo "❌ Virtual environment not found. Run 'make setup' first."; \
				exit 1; \
			fi \
		else \
			echo "❌ No checkpoint found for Lesson $$LESSON_NUM."; \
			echo "Looking for: $$CHECK_SCRIPT or $$TEST_FILE"; \
		fi \
	fi

# Show progress
progress:
	@echo ""
	@echo "📊 Your Progress"
	@echo "================"
	@echo ""
	@cat progress.md | grep -E "^\- \[.\]" | head -20
	@echo ""
	@echo "(Edit progress.md to update your checkboxes)"
	@echo ""

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf src/**/__pycache__
	rm -rf tests/__pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleaned!"

# Catch-all target for lesson/check numbers
%:
	@:

