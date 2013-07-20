# Copyright 2013 Levski Weng <levskiweng@hotmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Checks subversion log style """

#import codecs
from modules import Process
import re

## {{{ http://code.activestate.com/recipes/410692/ (r8)
# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False
 
    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
     
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def run(transaction, config):
	
	checklog_mode = config.getString("checklog.mode")
	err_msg = ""
	
	for case in switch(checklog_mode):
		if case('Keyword'):
			keywordFilePath = config.getString("checklog.KeywordFile")
			#The encoding of the file must be ansi	
			keywordFile = open(keywordFilePath).read()
			keywordList = keywordFile.split('\n')
			
			commitLog =  transaction.getCommitMsg()
			
			for keyword in keywordList:
				keywordPair = keyword.split('=')
				if (commitLog.find(keywordPair[0]) != -1):
					match = re.match(keywordPair[1].encode('string-escape'), commitLog)
					if not match:
						err_msg = "I found the keyword :" + keywordPair[0] + " in your commit log, but the log style doesn't obey the pre-defined regular expression :\r\n" + keywordPair[1]
						return (err_msg, 1)
			break
		if case():
			return ( "Currently the checklog engin doesn't support '" + checklog_mode + "'mode")

	return (err_msg,0)
