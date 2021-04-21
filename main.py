# Copyright 2021 KASPAR NOOR

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import time
import traceback
import sys
import os
import string
import random
from tqdm import tqdm
import re


class Main:

    def __init__(the_list, the_file):
        self.the_list = the_list
        self.the_file = the_file

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

        if os.path.exists("log.html"):
            os.remove("log.html")

        y = open('output.txt', 'w', encoding='utf-8')

        what_to_do = input(
            "What would you like to do today?\n\n1 - show only chat messages\n2 - show chat messages and whispers (/msg and /reply)\n3 - do nothing (good if you just want the html)\n\nMode: ")

        if what_to_do != '1' and what_to_do != '2' and what_to_do != '3':
            print("\nInvalid choice, please enter 1, 2 or 3")
            quit()

        output_method = input(
            "How would you like to see the output?\n\n1 - plain old txt file\n2 - sexy html file\n\nOutput method: ")

        if output_method != '1' and output_method != '2':
            print("\nInvalid choice, please enter 1, or 2")
            quit()

        file_name_input = input(
            "\n\nWhat is your input log name? (eg log.txt)\n\nFile name: ")

        if '.' not in file_name_input:
            print("\nLooks like you didn't specify the file extensions (eg .txt)")
            quit()

        try:
            f = open(file_name_input, 'r', encoding='utf-8')
        except:
            print("\nThere was an error trying to open " + file_name_input +
                  "\n Are you sure that the file exists in this directory?")
            quit()

        all_lines = f.readlines()

        def generate_html(the_list):
            g = open('log.html', 'w', encoding='utf-8')
            print("\n\nProcessing:")
            g.write('''
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width,initial-scale=1.0">
                <meta name="title" content="Minecraft Logs Processor">
                <meta name="theme-color" content="#51AE59">
                <meta name="color" content="#51AE59">


                <link rel="stylesheet" href="style.css">
                <link rel="icon" href="favicon.ico">

                <title>Minecraft Logs Processor</title>
            </head>
            <body>
                <div id="view-post" style="">
                <table>
                    <tbody id="lines">
            ''')
            x_severe = False
            x_info = False
            x_warning = False
            x_normal = False
            print("Generating an html document:")
            for x in tqdm(all_lines):
                if all_lines.index(x) == 0:
                    continue

                insert = '<span class="console-col-white">'
                match = re.search('/INFO]:', x)
                x_matched = x
                if match != None:
                    n = match.span()[1]
                    string = str(x)
                    result = string[:n] + insert + string[n:] + "</span>"
                    x_matched = result

                if "ERROR" in x:
                    x_severe = True
                elif "INFO" in x:
                    x_info = True
                elif "WARN" in x:
                    x_warning = True
                else:
                    x_normal = True
                if x_severe == True:
                    g.write('''
                        <tr>
                            <td class="line-number unselectable" unselectable="on">''' + str(all_lines.index(x)) + ''' </td>
                            <td class="line-content pre-whitespace console-level-severe">''' + x_matched + ' </td>' + '''
                        </tr> ''')
                elif x_info == True:
                    g.write('''
                        <tr>
                            <td class="line-number unselectable" unselectable="on">''' + str(all_lines.index(x)) + ''' </td>
                            <td class="line-content pre-whitespace console-level-info">''' + x_matched + ' </td>' + '''
                        </tr> ''')
                elif x_warning == True:
                    g.write('''
                        <tr>
                            <td class="line-number unselectable" unselectable="on">''' + str(all_lines.index(x)) + ''' </td>
                            <td class="line-content pre-whitespace console-level-warning">''' + x_matched + ' </td>' + '''
                        </tr> ''')
                elif x_normal == True:
                    g.write('''
                        <tr>
                            <td class="line-number unselectable" unselectable="on">''' + str(all_lines.index(x)) + ''' </td>
                            <td class="line-content pre-whitespace">''' + x_matched + ' </td>' + '''
                        </tr> ''')
                x_severe = False
                x_info = False
                x_warning = False
                x_normal = False
            g.write('''
                        </tbody>
                    </table >
                </div >
            </body>''')
            g.close()

        def generate_txt(the_list, the_file):
            print("Generating a txt file:")
            for p in tqdm(the_list):
                the_file.write(p)
            the_file.close()

        seperator = input(
            "\n\nWhat seperator do you use for messages? (eg if message looks like this Notch > Hey! the seperator would be >)\n\nSeperator: ")

        new_x = []

        if what_to_do == '1':
            print("\n\nProcessing:")
            for x in tqdm(all_lines):
                if seperator not in x:
                    continue
                else:
                    new_x.append(x)
            if output_method == '1':
                generate_txt(new_x, y)
            if output_method == '2':
                generate_html(new_x)

        if what_to_do == '2':
            print("\n\nProcessing:")
            for x in tqdm(all_lines):
                if seperator not in x and "/msg" not in x and "/r" not in x and "/message" not in x and "/whisper" not in x:
                    continue
                else:
                    new_x.append(x)
            if output_method == '1':
                generate_txt(new_x, y)
            if output_method == '2':
                generate_html(all_lines)

        if what_to_do == '3':
            if output_method == '1':
                generate_txt(all_lines, y)
            if output_method == '2':
                generate_html(all_lines)

        print("\nFinished! You can find the results in log.html\nwhich will reset before next use.\n")

        save_choice = input("Would you like to save the output (y or n): ")

        if save_choice == 'n':
            print("\nThank you for using MLP!")
            f.close()
            y.close()
            g.close()
            time.sleep(3)
            quit()
        else:
            random_output_name = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=30))
            if output_method == 1:
                y = open('output.txt', 'r', encoding='utf-8')
                z = open('output-' + random_output_name +
                         '.txt', 'w', encoding='utf-8')
                finished_output = y.read()
                z.write(finished_output)
                z.write("Processed by Minecraft Logs Processor:")
                z.write("https://github.com/kasparnoor/minecraft-logs-processor")
                z.close()
                f.close()
            if output_method == 2:
                g = open('log.html', 'r', encoding='utf-8')
                z = open('log-' + random_output_name +
                         '.html', 'w', encoding='utf-8')
                finished_output = g.read()
                z.write(finished_output)
                g.close()
                z.close()
                f.close()
            y.close()
            print("\nSuccessfully saved output to " + 'output-' +
                  random_output_name + '.html' + "\nThank you for using MLP!")
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
