#!/usr/bin/python
from os import listdir, rename
import sys
import copy

msg = '''
	MaSS v0.01 (beta)
	MASS RENAMING UTILITY.
'''

def validate(a,b):
	k = copy.deepcopy(b)	#assignment won't work; memory allocations
	for f in k:	#for every file in k (b)
		if f in a:	#check if it exists in a already
			#print "NOT renaming", f, "already exists"
			a.remove(f)	#remove from both lists
			b.remove(f)
def ren(src,dest):	#self expl;
	try:
		rename(src,dest)
	except:
		ercnt+=1
		return "ERROR renaming "+src
	return "SUCCESS "+src+" --> "+dest

def init(src):
	global sources, dests, ext, ercnt, nfiles
	ercnt=0
	try:
		sources = sorted(listdir(src))	#not really necessary
	except:
		print "Couldn't open directory.\n\t[-] Make sure this directory exists.\n\t[-] And you have read/write permissions."
		sys.exit(1)
	#ext = "." + sources[0][::-1][0:sources[0][::-1].find(".")][::-1]
	nfiles = len(sources)
	print nfiles, "files detected"
	dests	= list(str(x) + get_ext(sources[x]) for x in xrange(len(sources)))	#the destinations list
	validate(sources, dests)
	print "Renaming", len(sources), "files"

def get_ext(s):	#returns the extension
	if s.find(".") != -1:
		return s[::-1][0:s[::-1].find(".")+1][::-1]	#reverse; every char till "."; reverse;
	return ""	#just in case if there was no extension

if __name__ == "__main__":
	print msg
	src=""
	try:
		src = sys.argv[1]
	except:
		src = raw_input("Enter Source: ")
	if src[-1] != "/":
		src+="/"
	init(src)
	for i in xrange(len(sources)):
		print ren(src+sources[i],src+dests[i])
	print "\n\n", nfiles-ercnt, "of", nfiles, "successfully renamed."
