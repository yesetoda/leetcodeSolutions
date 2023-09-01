class Solution:
    @staticmethod
    def numUniqueEmails(emails: list[str]) -> int:
        uniques = set()
        for i in emails:
            at = i.index("@")
            for _ in range(max(i[:at].count("."), i[:at].count("+"))):
                if "." in i:
                    ind1 = i.index(".")
                    if at > ind1:
                        i = i[:ind1] + i[ind1 + 1:]
                if "+" in i:
                    ind2 = i.index("+")
                    if at > ind2:
                        i = i[:i.index("+")] + i[i.index("@"):]
            uniques.add(i)
        return len(uniques)
    print(numUniqueEmails(emails=["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))