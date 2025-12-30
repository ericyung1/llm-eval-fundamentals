"""
Lesson 9: Code Quality - Starter Code

YOUR TASK: Add type hints and docstrings to all functions and classes.

Requirements:
1. Add type hints to ALL function parameters and return types
2. Add docstrings to ALL functions and classes (Google style)
3. Docstrings must include: description, Args, Returns, and Raises (where applicable)

Run tests with: pytest tests/test_lesson_09.py -v
"""

# TODO: Add type hints to this function
# TODO: Add docstring with Args, Returns, and example
def format_name(first, last, uppercase=False):
    """TODO: Add docstring."""
    full_name = f"{first} {last}"
    if uppercase:
        return full_name.upper()
    return full_name


# TODO: Add type hints
# TODO: Add docstring
def calculate_average(numbers):
    """TODO: Add docstring."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


# TODO: Add type hints
# TODO: Add docstring with Raises section
def parse_score(score_str):
    """TODO: Add docstring."""
    try:
        score = float(score_str)
    except ValueError:
        raise ValueError(f"Invalid score format: {score_str}")
    
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100: {score}")
    
    return score


# TODO: Add type hints
# TODO: Add docstring
def filter_by_threshold(items, threshold):
    """TODO: Add docstring."""
    return [item for item in items if item >= threshold]


# TODO: Add type hints
# TODO: Add docstring
def merge_dicts(dict1, dict2):
    """TODO: Add docstring."""
    result = dict1.copy()
    result.update(dict2)
    return result


# TODO: Add type hints
# TODO: Add docstring
def find_max_key(data):
    """TODO: Add docstring."""
    if not data:
        return None
    return max(data.keys(), key=lambda k: data[k])


# TODO: Add type hints to class and all methods
# TODO: Add class docstring and method docstrings
class TextAnalyzer:
    """TODO: Add class docstring with Attributes section."""
    
    # TODO: Add type hints
    def __init__(self, text):
        """TODO: Add docstring."""
        self.text = text
        self._word_count = None
    
    # TODO: Add type hints and docstring
    @property
    def word_count(self):
        """TODO: Add docstring."""
        if self._word_count is None:
            self._word_count = len(self.text.split())
        return self._word_count
    
    # TODO: Add type hints and docstring
    def char_count(self, include_spaces=True):
        """TODO: Add docstring."""
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(" ", ""))
    
    # TODO: Add type hints and docstring
    def contains_word(self, word):
        """TODO: Add docstring."""
        return word.lower() in self.text.lower()
    
    # TODO: Add type hints and docstring
    def get_unique_words(self):
        """TODO: Add docstring."""
        words = self.text.lower().split()
        return set(words)
    
    # TODO: Add type hints and docstring
    def get_word_frequency(self):
        """TODO: Add docstring."""
        words = self.text.lower().split()
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        return frequency


# TODO: Add type hints
# TODO: Add docstring
class Result:
    """TODO: Add class docstring."""
    
    # TODO: Add type hints
    def __init__(self, value, success=True, error=None):
        """TODO: Add docstring."""
        self.value = value
        self.success = success
        self.error = error
    
    # TODO: Add type hints and docstring
    def is_ok(self):
        """TODO: Add docstring."""
        return self.success
    
    # TODO: Add type hints and docstring
    def unwrap(self):
        """TODO: Add docstring."""
        if not self.success:
            raise RuntimeError(f"Cannot unwrap failed result: {self.error}")
        return self.value
    
    # TODO: Add type hints and docstring
    @classmethod
    def ok(cls, value):
        """TODO: Add docstring."""
        return cls(value, success=True)
    
    # TODO: Add type hints and docstring
    @classmethod
    def err(cls, error):
        """TODO: Add docstring."""
        return cls(None, success=False, error=error)

