class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')

        n1 = len(ver1)
        n2 = len(ver2)
        i = 0
        while i < n1 or i < n2:
            v1 = ver1[i].lstrip('0') or '0' if i < n1 else '0'
            v2 = ver2[i].lstrip('0') or '0' if i < n2 else '0'

            if int(v1) > int(v2):
                return 1

            if int(v2) > int(v1):
                return -1

            i += 1

        return 0
