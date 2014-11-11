__author__ = 'Daniel'

import subprocess

class QueryExecuter:


    @staticmethod
    def excuteQuery(string):
        p = subprocess.Popen(" echo "+string+" | osqueryi", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        return output