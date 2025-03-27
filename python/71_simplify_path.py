class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        result_list = []
        for component in components:
            if component == "" or component == ".":
                continue
            if component == "..":
                if result_list:
                    result_list.pop()
            else:
                result_list.append(component)
        result = "/" + "/".join(result_list)
        return result
