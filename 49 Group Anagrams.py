def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    import collections
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())


    storage = [''.join(sorted(item)) for item in strs]
    output_dict = {}
    output = []
    for i in range(len(storage)):
        if storage[i] not in output_dict.keys():
            output_dict[storage[i]] = [strs[i]]
        else:
            output_dict[storage[i]].append(strs[i])
    return output_dict.values()

strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]
print(groupAnagrams(strs))