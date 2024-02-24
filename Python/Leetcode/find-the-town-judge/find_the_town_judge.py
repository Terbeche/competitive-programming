class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        not_town_judge = set()
        trustable_persons = {}
        if len(trust) == 0 and n == 1:
            return n

        for trustable in trust:
            person, potential_judje = trustable
            
            not_town_judge.add(person)

            if person in trustable_persons:
                del trustable_persons[person]

            if potential_judje not in not_town_judge:
                if potential_judje not in trustable_persons:
                    trustable_persons[potential_judje] = 1
                else:
                    trustable_persons[potential_judje] += 1
            else:
                if potential_judje in trustable_persons:
                    del trustable_persons[potential_judje]

        if len(trustable_persons) > 0:
            for key, value in trustable_persons.items():
                if n - 1 == value:
                    return key
                else:
                    return -1
        else:
            return -1
