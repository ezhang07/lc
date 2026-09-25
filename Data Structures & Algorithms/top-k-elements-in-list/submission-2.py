class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        count frequencies using a hashmap

        after that we use bucket sort, where index of array => frequency

        nearest to the end has highest freq, based off of k, we just get the top k. 
        """

        freq_map = {}

        for n in nums: # count freqs using a hashmap
            freq_map[n] = 1 + freq_map.get(n, 0)

        bucket_sort = [[] for i in range(len(nums) + 1)]

        for n, freq in freq_map.items():
            bucket_sort[freq].append(n)
        
        res = []
        for i in range(len(bucket_sort) - 1, -1, -1):
            for val in bucket_sort[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        
        


        

        