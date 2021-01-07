# Problem:
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

Solution:
class Solution:
    def defangIPaddr(self, address: str) -> str:
        dot = "."
        address_final = ""
        for i in address:
            if i == dot:
                # print(i)
                address_final += "[.]"
            else:
                address_final += i
        print(address_final)
        return address_final
