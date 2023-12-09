class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        output = {}

        for i in paths:
            root, files = i.split()[0], i.split()[1:]
            for f in files:
                content_start = f.index('(')
                content_end = f.index(')')
                content = f[content_start + 1:content_end]
                file_path = root + '/' + f[:content_start]

                if content in output:
                    output[content].append(file_path)
                else:
                    output[content] = [file_path]

        return [files for files in output.values() if len(files) > 1]