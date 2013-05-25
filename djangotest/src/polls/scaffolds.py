'''
Created on May 24, 2013

@author: Steven Bluen
'''

import scaffolding
class UserScaffold(object):
    username = scaffolding.FirstName()
    password = scaffolding.RandInt(1, 1000)
