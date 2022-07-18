import sys

class LoadingBar:
    def __init__(self, total):
        """
        It takes a number of files to process as an argument, and then prints the progress bar to the screen
        
        :param total: the total number of files to be processed
        """
        assert(total > 0)
        self.total_files = total
        self.cpt = 0
        self.nb = 0
        self.print_bar()

    def print_bar(self):
        """
        It prints the progress bar to the console
        """
        self.nb = int((self.cpt*100)/self.total_files)
        # Calculte %
        percent = str(self.nb) + " %"
        sys.stdout.write(("\u2588" * self.nb) + ("\u2591" * (100-self.nb)) + " " + percent)
        sys.stdout.flush()
        sys.stdout.write("\b" * (len(percent) + 101))

    def update(self):
        """
        It update progress and print the bar to the console
        """
        self.cpt += 1
        self.print_bar()

    def finish(self):
        """
        It prints 'Done.' after the progress is completed.
        """
        print("\nDone.")
