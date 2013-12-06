"""
Count visits per User

input:
* modified anonymouse-web.data: add User ID at end of 'V' line

e.g.
...
C,10001,10001
V,1000,1,10001
V,1001,1,10001
V,1002,1,10001
...

output:
* user Id, visit count

e.g.
"10068" 23
"10348" 28
"10454" 22
...

"""

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopUsers(MRJob):

    def mapper(self, line_no, line):
        """Extracts the User that was visited"""
        cell = csv_readline(line)
        if cell[0] == 'V':  # e.g. V,1000,1,10001
            yield cell[3], 1

    def reducer(self, vroot, visit_counts):
        """Sumarizes the visit counts by adding them together.  If total visits
        is more than 20, yield the results"""
        total = sum(visit_counts)
        if total > 20:
            yield vroot, total

if __name__ == '__main__':
    TopUsers.run()
