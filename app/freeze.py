from flask_frozen import Freezer

import sys
import time
import threading
import main
freezer = Freezer(main.app)


class progress_bar_loading(threading.Thread):

    def run(self):
        global stop
        global kill
        msg = ("\tL a  c o p i a  c o m p a r t e  c u l t u r a!")

        print("[!] Generando la biblioteca")
        sys.stdout.flush()
        i = 0
        while stop is not True:
            msg_ = msg[:i] + msg[i].upper() + msg[i + 1:]

            sys.stdout.write('%s' % msg_)
            sys.stdout.write("\b" * len(msg))
            sys.stdout.flush()
            time.sleep(0.07)
            i += 1
            # Para mantenernos siempre dentro del largo del string
            i = i % len(msg)
            msg_ = ""

        if kill:
            print('\nAlgo Fallo!')
        else:
            print('\nListo!')


if __name__ == '__main__':
    kill = False
    stop = False
    p = progress_bar_loading()
    p.start()

    try:
        # anything you want to run.
        freezer.freeze()
        stop = True
    except KeyboardInterrupt or EOFError:
        kill = True
        stop = True
