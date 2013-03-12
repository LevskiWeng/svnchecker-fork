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

def run(transaction, config):
    keyword_list = [""]
    #The encoding of the file must be ansi
    #The keyword file stores every keyword per line
	#TODO: Currently the path is hard code, maybe someday I'll find a better solution.
    keyword_file_path = "F:/root/style_check/svnchecker-0.3/checks/checklog_keyword.txt"
    keyword_file = open(keyword_file_path).read()
    
    err_msg =  "The commit is for bug fix because I found one of the keywords in the log:\n"
    err_msg += keyword_file + "\n"
    err_msg += "But the log has an incorrect structure.\n"
    err_msg += "The first line of bug fixing log should look like:\n"
    err_msg += "ref #123, #456, fix #789\n"
    err_msg += "It means that the commit is relevant to bug number 123 and bug number 456, and the commit fixes bug number #789\n\n"
    err_msg += "Please modify your commit log and try again."
    
    commit_log =  transaction.getCommitMsg()
    log_list = [""]

    keyword_list = keyword_file.split('\n')
    for keyword in keyword_list:
        if (commit_log.find(keyword) != -1):
            log_list = commit_log.split('\n')
        
            if (log_list[0].upper().find("REF #") == -1) and (log_list[0].upper().find("FIX #") == -1):
                return (err_msg, 1)
        
    return ("",0)
