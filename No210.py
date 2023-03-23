from typing import List

class Solution:
    def get_element(self, target_key, target_dict):
        res_list = list()
        if target_key not in target_dict.keys():
            return [target_key]
        if target_dict[target_key]["status"] == 1:
            return [-1]
        if target_dict[target_key]["status"] == 2:
            return [target_key]
        target_dict[target_key]["status"] = 1
        for value in target_dict[target_key].get("value"):
            res = self.get_element(value, target_dict)
            res_list.extend(res)
        res_list.append(target_key)
        target_dict[target_key]["status"] = 2
        return res_list
                                
            
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            res = [i for i in range(numCourses)]
            return res
        else:
            res_list = list()
            temp_dict = dict()
            for prerequisite in prerequisites:
                if prerequisite[0] in temp_dict.keys():
                    temp_dict[prerequisite[0]]["value"].append(prerequisite[1])
                else:
                    temp_dict[prerequisite[0]] = {"value": [prerequisite[1]], "status": 0} # 0表示初始化，1表示查询中，2表示已完成
            
            for key, value_dict in temp_dict.items():
                if value_dict.get("status") == 2:
                    res_list.append(key)
                else:
                    temp_dict[key]["status"] = 1
                    for value in value_dict.get("value"):
                        res = self.get_element(value, temp_dict)
                        res_list.extend(res)
                    res_list.append(key)
                    temp_dict[key]["status"] = 2
                    
            if -1 in res_list:
                return []
            else:
                res_temp_list = list()
                for res in res_list:
                    if res not in res_temp_list:
                        res_temp_list.append(res)
                for i in range(numCourses):
                    if i not in res_temp_list:
                        res_temp_list.append(i)
                return res_temp_list
                        


                    

if __name__ == '__main__':
    solution = Solution()
    params = [
        # {"numCourses": 1, "prerequisites": []},
        {"numCourses": 2, "prerequisites": [[1,0]]},
        {"numCourses": 4, "prerequisites": [[1,0],[2,0],[3,1],[3,2]]},
        {"numCourses": 2, "prerequisites": [[0,1],[1,0]]},
        {"numCourses": 8, "prerequisites": [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]},
        {"numCourses": 3, "prerequisites": [[0,1],[0,2],[1,2]]}
    ]
    for param in params:
        print(solution.findOrder(param.get("numCourses"), param.get("prerequisites")))
