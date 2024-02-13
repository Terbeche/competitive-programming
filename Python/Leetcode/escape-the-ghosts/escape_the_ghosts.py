class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        player_target_distance = abs(target[0]) + abs(target[1])
        print(player_target_distance)
        for ghost in ghosts:
            ghost_target_distance = abs(target[0] - ghost[0])  + abs(target[1] - ghost[1])
            print(ghost_target_distance)

            if ghost_target_distance <= player_target_distance:
                return False
        
        return True
