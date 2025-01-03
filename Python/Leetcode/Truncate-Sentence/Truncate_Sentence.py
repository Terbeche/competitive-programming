class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        list_ = list(s.split())
        print(list_[0:k])
        return (" ").join(list_[0:k])