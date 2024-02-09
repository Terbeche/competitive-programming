class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        common_dict = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    common_dict[list1[i]] = i + j

        least_index = min(common_dict.values())
        return [restaurant for restaurant, index in common_dict.items() if index == least_index]