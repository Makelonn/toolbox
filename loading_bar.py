import sys

class LoadingBar:
    def __init__(self, total):
        assert(total > 0)
        self.total_files = total
        self.cpt = 0
        self.nb = 0
        self.print_bar()

    def print_bar(self):
        self.nb = int((self.cpt*100)/self.total_files)
        # Calculte %
        percent = str(self.nb) + " %"
        sys.stdout.write(("\u2588" * self.nb) + ("\u2591" * (100-self.nb)) + " " + percent)
        sys.stdout.flush()
        sys.stdout.write("\b" * (len(percent) + 101))

    def update(self):
        self.cpt += 1
        self.print_bar()

    def finish(self):
        print("\nDone.")
