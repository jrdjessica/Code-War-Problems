class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = [[strs[0]]]

        for i in range(1, len(strs)):
            for array in output:
                if sorted(array[0]) == sorted(strs[i]):
                    array.append(strs[i])
                    break
                elif array == output[-1]:
                    output.append([strs[i]])
                    break

        return output
