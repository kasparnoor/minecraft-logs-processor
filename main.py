# Copyright 2021 KASPAR NOOR

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time
from tqdm import tqdm
import random
import string
import os
import sys
import traceback


def main():
    print(r'''
    ___  ___ _                                  __  _
    |  \/  |(_)                                / _|| |
    | .  . | _  _ __    ___   ___  _ __  __ _ | |_ | |_
    | |\/| || || '_ \  / _ \ / __|| '__|/ _` ||  _|| __|
    | |  | || || | | ||  __/| (__ | |  | (_| || |  | |_
    \_|  |_/|_||_| |_| \___| \___||_|   \__,_||_|   \__|
    | |
    | |  ___    __ _  ___
    | | / _ \  / _` |/ __|
    | || (_) || (_| |\__ \
    |_| \___/  \__, ||___/
                __/ |
    _ __   _ _|___/_    ___  ___  ___  ___   ___   _ __
    | '_ \ | '__|/ _ \  / __|/ _ \/ __|/ __| / _ \ | '__|
    | |_) || |  | (_) || (__|  __/\__ \\__ \| (_) || |
    | .__/ |_|   \___/  \___|\___||___/|___/ \___/ |_|
    | |
    |_|   by @kasparnoor

        ''')

    time.sleep(1)

    if os.path.exists("output.txt"):
        os.remove("output.txt")
    f = open('log.txt', 'r', encoding='utf-8')
    y = open('output.txt', 'w', encoding='utf-8')

    all_lines = f.readlines()

    what_to_do = input(
        "What would you like to do today?\n\n1 - show only chat messages\n2 - show chat messages and whispers (/msg and /reply)\n\nChoose: ")

    if what_to_do != '1' and what_to_do != '2':
        print("Invalid choice, please enter 1 or 2")
        quit()

    if what_to_do == '1':
        for x in tqdm(all_lines):
            if ">" not in x:
                continue
            else:
                y.write(x)

    if what_to_do == '2':
        for x in tqdm(all_lines):
            if ">" not in x and "/msg" not in x and "/r" not in x and "/message" not in x and "/whisper" not in x:
                continue
            else:
                y.write(x)

    print("\nFinished! You can find the results in output.txt\nwhich will reset before next use.\n")

    save_choice = input("Would you like to save the output (y or n): ")

    if save_choice == 'n':
        print("\nThank you for using MLP!")
        z.close()
        f.close()
        y.close()
        time.sleep(3)
        quit()
    else:
        y.close()
        y = open('output.txt', 'r', encoding='utf-8')
        random_output_name = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=30))
        z = open('output-' + random_output_name +
                 '.txt', 'w', encoding='utf-8')
        finished_output = y.read()
        z.write(finished_output)
        z.write("Processed by Minecraft Logs Processor:")
        z.write("https://github.com/kasparnoor/minecraft-logs-processor")
        z.close()
        f.close()
        print("\nSuccessfully saved output to " + 'output-' +
              random_output_name + '.txt' + "\nThank you for using MLP!")
        time.sleep(3)
        quit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n\n\nStopping program!\nThank you for using MLP!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
