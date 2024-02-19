class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')

        stack = []

        for i in path_list:
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '.' or i == '':
                continue
            else:
                stack.append(i)
        return  '/' + '/'.join(stack)