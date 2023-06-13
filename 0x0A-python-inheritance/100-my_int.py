#!/usr/bin/python3
"""class my int"""

class MyInt(int):
    """reel clss"""
    def __eq__(self, value):
        """Override == opeartor with !="""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with =="""
        return self.real == value
