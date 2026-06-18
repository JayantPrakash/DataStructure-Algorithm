from typing import List
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.map_len = []
        for str in strs:
            self.map_len.append(len(str))

        self.encoded_string = "".join(strs)    

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []

        i = 0
        len_seen = 0
        for curr_len in self.map_len:
            curr_str = self.encoded_string[len_seen:len_seen + curr_len] 
            strs.append(curr_str)
            len_seen += curr_len

        return strs           



# Your Codec object will be instantiated and called as such:
codec = Codec()
dummy_input = ["Hello","World", "jayant ", "Prakash"]
dummy_input = [""]

print(codec.decode(codec.encode(dummy_input)))