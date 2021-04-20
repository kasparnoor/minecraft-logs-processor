<h1 align="center">Welcome to Minecraft Logs Processor 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/kefranabg/readme-md-generator/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/kasparnoor/minecraft-logs-processor/blob/master/LICENSE.md" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/kasparnoor/minecraft-logs-processor" />
  </a>
  <a href="https://github.com/kasparnoor/minecraft-logs-processor" target="_blank">
    <img alt="Stars" src="https://img.shields.io/github/stars/kasparnoor/minecraft-logs-processor" />
  </a>
</p>

> MLP is a python script that lets you process your Minecraft server logs to better understand them and gather important data from them.

### 🏠 [Homepage](https://github.com/kasparnoor/minecraft-logs-processor/)

## Install

Clone the repository from github:
```sh
git clone https://github.com/kasparnoor/minecraft-logs-processor/
```

## Usage

Go into the repository:
```sh
cd minecraft-logs-processor
```
Install requirements:
```sh
pip install -r requirements.txt
```
Run the script:
```sh
python main.py
```

## Features

1. Extract only messages sent by users
1. Extract messages sent by users and whispers (/msg, /r, etc)

More coming soon and false positives to be fixed!

## Notes

When using the first 2 methods, it's recommended to use a not-so-common seperator between user and message like `>` (then in chat it'd be: `[Iron] Notch > Hello world!`). I am trying to improve the script so it detects better without a special seperator.

## Author

👤 **Kaspar Noor**

* Github: [@kasparnoor](https://github.com/kasparnoor)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/kasparnoor/minecraft-logs-processor/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [Kaspar Noor](https://github.com/kasparnoor).<br />
This project is [MIT](https://github.com/kasparnoor/minecraft-logs-processor/LICENSE.md) licensed.
