import os
import sys


class  KubeUtil:
    def function1(self, name):
        if type(name) != str:
            print("Name should be string only...")
            return 1
        
        print(f'Heyyy, My name is "{name}"')
    
