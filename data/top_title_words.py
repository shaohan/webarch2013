"""
Count frequency of words in title

input:
* anonymouse-web.data

e.g.
...
A,1287,1,"International AutoRoute","/autoroute"
A,1288,1,"library","/library"
A,1289,1,"Master Chef Product Information","/masterchef"
...

output:
* word, frequence

e.g.
45      "ms"
36      "support"
14      "development"
...

"""

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopTitleWords(MRJob):

    def mapper_get_words(self, _, line):
        """Extracts words in title"""
        cell = csv_readline(line)
        if cell[0] == 'A':  # e.g. A,1287,1,"International AutoRoute","/autoroute"
            for word in cell[3].split():
                yield word.lower(), 1

    def combiner_count_words(self, word, counts):
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        """Summarize results with a same key"""
        yield None, (sum(counts), word)

    def reducer_find_top_words(self, _, word_count_pairs):
        list = [ w for w in word_count_pairs ]
        list.sort()
        list.reverse()
        for i in range(0, 10):
            yield list[i]

    def steps(self):
        return [
            self.mr(mapper=self.mapper_get_words,
                    combiner=self.combiner_count_words,
                    reducer=self.reducer_count_words),
            self.mr(reducer=self.reducer_find_top_words)
        ]

if __name__ == '__main__':
    TopTitleWords.run()
