class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # Storing the decoded string, even just to the needed length,
        # exceeds the maximum memory use needed
        #
        # So we need to calculate the "virtual index" in the decoded
        # string. And to do that, we need to know the length of the
        # decoded string. This is actually pretty simple because if you
        # traverse the string, each time you encounter an integer you
        # double the length of the decoded string up to that point.
        #
        # Reason being, since each digit d extends the decoded string
        # so far by d-1 times; so if you encounter a 2 when decoding,
        # you just double what you have so far. Since finding a 2 means
        # you add another copy of what's been decoded so far, finding a
        # 3 means you add 2 more copies of what you have so far, and so
        # on up to 9.
        #
        # TODO: there's a one-liner formulation of this using something
        # like n-wise that I can't exactly get right now.
        decoded_length = 0
        for char in s:
            if '2' <= char <= '9':
                decoded_length = decoded_length * int(char)
            else:
                decoded_length = decoded_length + 1

        # Now we know the upper bound that the "virtual index" can be.
        # To find the character, we can't work forwards, since if we
        # start from the beginning of the string we will need to
        # track what has been decoded so far and where we were in
        # that decoding, which requires actually doing the decoding,
        # which means we'll run into the aforementioned memory limit.
        #
        # To do this, we have to decrement the virtual index based on
        # whether we're at a number or character.
        # If we're at a character, we just decrease it by one.
        # If we're at a number, we decrease it by that number times
        # (divide by the number).
        # This is exactly the inverse of the procedure to figure out
        # the decoded length.
        #
        # To find the actual character at decoded position k, we need
        # to remember that k is within [0, virtual_index). So we
        # modulo it by the virtual index every iteration backwards
        # through the string.
        # TODO: I'm not too comfortable with the "finding k" part of
        # that explanation.
        decoded_k = k
        virtual_index = decoded_length
        for char in reversed(s):
            decoded_k = decoded_k % virtual_index

            if decoded_k == 0 and 'a' <= char <= 'z':
                return char
            elif '2' <= char <= '9':
                virtual_index = virtual_index // int(char)
            else:
                virtual_index = virtual_index - 1
        return ''
