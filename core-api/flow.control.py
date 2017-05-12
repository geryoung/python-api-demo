#! /usr/bin/env python


#######################################
# if, elif, 
#######################################

print "#######################################"
print "# if, elif, "
print "#######################################"

x = 100

if x < 0:
  x = 0
  print 'Negative changed to zero'
elif x == 0:
  print 'Zero'
elif x == 1:
  print 'Single'
else:
  print 'More'

print " "
print " "



#######################################
# for 
#######################################

print "#######################################"
print "# for "
print "#######################################"

words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)

for i, w in enumerate(words) :
    print i, w, len(w)
    
print words

print " "
print " "
#######################################
# range
#######################################

print "#######################################"
print "# range "
print "#######################################"

r = range(10)
print r

r = range(2, 10)
print r

r = range(0, 10, 3)
print r





print " "
print " "
#######################################
# def function
#######################################

print "#######################################"
print "# def function "
print "#######################################"


def doprint(sth):
  print sth
  return 

result = doprint('123')
print result


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

ask_ok("aaa input")
