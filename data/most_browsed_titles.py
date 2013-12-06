"""
Find the title of the most frequently visited page

input:
* anonymouse-web.data

e.g.
...
A,1287,1,"International AutoRoute","/autoroute"
A,1288,1,"library","/library"
A,1289,1,"Master Chef Product Information","/masterchef"
...
C,"33424",33424
V,1287,1
V,1289,1
...

output:
* word, frequence

"""

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopVisitedTitle(MRJob):

    def mapper_get_count_and_title(self, _, line):
        """Extracts words in title"""
        cell = csv_readline(line)
        if cell[0] == 'A':  # e.g. A,1287,1,"International AutoRoute","/autoroute"
            yield cell[1], (0, cell[3])
        elif cell[0] == 'V': # e.g. V,1287,1
            yield cell[1], (1, None)

    def combiner_count_visits(self, vroot, count_title_pairs):
        count = 0
        title = None
        for count_title_pair in count_title_pairs:
            count += count_title_pair[0]
            if count_title_pair[1]:
                title = count_title_pair[1]
        yield vroot, (count, title)

    def reducer_count_visits(self, vroot, count_title_pairs):
        """Summarize results with a same key"""
        count = 0
        title = None
        for count_title_pair in count_title_pairs:
            count += count_title_pair[0]
            if count_title_pair[1]:
                title = count_title_pair[1]
        yield None, (count, title)

    def reducer_find_top_title(self, _, word_count_pairs):
        list = [ w for w in word_count_pairs ]
        list.sort()
        list.reverse()
        yield list[0]

    def steps(self):
        return [
            self.mr(mapper=self.mapper_get_count_and_title,
                    combiner=self.combiner_count_visits,
                    reducer=self.reducer_count_visits),
            self.mr(reducer=self.reducer_find_top_title)
        ]

if __name__ == '__main__':
    TopVisitedTitle.run()
