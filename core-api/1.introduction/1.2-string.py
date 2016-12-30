#!/usr/bin/python# -*- coding utf-8 -*-

text = "# This is not a comment because it's inside quotes."

text2 = '1234'

print "text"+"text2"


#-------


text = ('Put several strings within parentheses '
        'to have them joined together.')

print text


#------------

word = 'atthoN'
print word[-1]  # character in position 0
print word[5]  # character in position 5

print word[:2] 
print word[2:]


#------------

s = 'supercalifragilisticexpialidocious'
print len(s)



#----------
#unicode
print u'Hello\u0020World !'
print u"漩�" #æ¼©ï¿½

print u"漩�".encode('utf-8')
# print u"漩�".encode('gbk')



