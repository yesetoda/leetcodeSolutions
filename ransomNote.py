class Solution:
    def canConstruct( ransomNote: str, magazine: str) -> bool:
        return ransomNote in magazine
    print(canConstruct(ransomNote = "bg", magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))