def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Approach:
        1. Build a hash table (dict) mapping each magazine character to how
           many times it appears. This is a single O(m) pass.
        2. Walk the ransom note, "spending" one of each character from the
           table. Dictionary lookups are O(1) on average, so this pass is O(n).
        3. If a character is missing or its count is already used up, the note
           can't be built, so return False immediately.

    Overall: O(n + m) time, O(k) space where k is the number of distinct
    characters in the magazine.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Quick exit: a longer note can never be built from a shorter magazine.
    if len(ransomNote) > len(magazine):
        return False

    # Hash table of available characters -> remaining count.
    available = {}
    for char in magazine:
        available[char] = available.get(char, 0) + 1

    # Use up one character from the table for each character in the note.
    for char in ransomNote:
        if available.get(char, 0) == 0:
            # Missing entirely or already depleted.
            return False
        available[char] -= 1

    return True
