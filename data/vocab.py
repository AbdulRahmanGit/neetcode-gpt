from typing import Dict, List, Tuple

class Solution:
    def build_vocab(self, text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
        # Return (stoi, itos) where:
        # - stoi maps each unique character to a unique integer (sorted alphabetically)
        # - itos is the reverse mapping (integer to character)
        chars = sorted(set(text))
        unique_c_to_int = {ch: i for i, ch in enumerate(chars)}
        uniqnue_int_to_c = {i: ch for ch,i in unique_c_to_int.items()}
        return unique_c_to_int, uniqnue_int_to_c


    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:
        # Convert a string to a list of integers using stoi mapping
        return [stoi[ch] for ch in text]

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:
        # Convert a list of integers back to a string using itos mapping
        return ''.join(itos[i] for i in ids)