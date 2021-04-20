import time
from tqdm import tqdm
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

f = open('log.txt', 'r', encoding='utf-8')
y = open('output.txt', 'w', encoding='utf-8')

all_lines = f.readlines()

what_to_do = input(
    "What would you like to do today?\n\n1 - show only chat messages\n2 - show chat messages and whispers (/msg and /reply)\n\nChoose: ")

if what_to_do != '1' and what_to_do != '2':
    print("Invalid choice, quitting...")
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

print("\nFinished! You can find the results in output.txt\nwhich will reset before next use, would you like to save the output?\n\n")

save_choice = input("y or n\n\nChoose: ")

if save_choice == 'n':
    print("\nThank you for using MLP!")
    time.sleep(3)
    quit()
else:
    random_output_name = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=30))
    z = open('output-' + random_output_name + .txt, 'w', encoding='utf-8')
    finished_output = y.read()
    z.write(finished_output)
    z.write("Processed by Minecraft Logs Processor:")
    z.write("")
f.close()
y.close()
