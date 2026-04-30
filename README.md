# defword

A simple CLI tool for word definition lookups.

It relies on the [Free Dictionary API](https://freedictionaryapi.com/) for lookups and the [MyMemory API](https://mymemory.translated.net/) for definition translation. Languages are specified using standard ISO 639-1/639-3 language codes.

---

## Installation

You can quickly install the tool by running the following command:

```bash
curl -LO https://github.com/Mionuel/defword/releases/download/1.0.0/defword \
    && curl -L https://github.com/Mionuel/defword/releases/download/1.0.0/install.sh | bash
```

This downloads the `install.sh` script, which creates all the necessary directories for you and moves the binary into `/usr/local/bin` so that you can run the tool anywhere on your system.

**Data Storage:** The Python script will automatically create a directory at `$HOME/.local/share/defword`. This is where your lookup history and recent requests cache live.

---

## Uninstallation

To uninstall the tool, simply run the following command:

```bash
curl -L https://github.com/Mionuel/defword/releases/download/1.0.0/uninstall.sh | bash
```

It runs the `uninstall.sh` script, which completely removes the project's binary from `/usr/local/bin` and the `$HOME/.local/share/defword` directory.

---

## Usage

### Defining Words

**Basic Lookup**
If no input or output options are provided, the tool defaults to English.
```bash
defword define ambiguous
```
> Ambiguous (adjective) - Open to multiple interpretations.

**Translation**
Specify the input and output languages. In this example, the input is German (`de`) and the output is Italian (`it`).
```bash
defword define langsam -i de -o it
```
> Lento (aggettivo) - Impiega molto tempo per muoversi o percorrere una breve distanza, o per eseguire un'azione; non è veloce nel movimento; procede a bassa velocità.

**Multiple Output Languages**
You can provide multiple output languages:
```bash
defword define strasse -i de -o it -o pl -o es
```
> Strada (sostantivo) - Una parte di strada asfaltata, di solito in un villaggio o in una città.
> Ulica (rzeczownik) - utwardzona część drogi, zwykle we wsi lub mieście.
> Calle (sustantivo) - Una parte pavimentada de la carretera, generalmente en un pueblo o una ciudad.

### Viewing History

**Recent Lookups**

By default, this command prints out your last 5 lookups.
```bash
defword history
```
```text
[30-04-2026 20:10:23] slow:
[it] Lento (aggettivo) - Impiega molto tempo per muoversi o percorrere una breve distanza, o per eseguire un'azione; non è veloce nel movimento; procede a bassa velocità.
...
```

**Limit History Output**

Use the `-l` flag to print out a specific number of your latest lookups.
```bash
defword history -l 2
```
```text
[30-04-2026 20:17:42] slow:
[it] Lento (aggettivo) - Impiega molto tempo per muoversi o percorrere una breve distanza, o per eseguire un'azione; non è veloce nel movimento; procede a bassa velocità.

[30-04-2026 20:28:03] street:
[it] Strada (sostantivo) - Una parte di strada asfaltata, di solito in un villaggio o in una città.
[pl] Ulica (rzeczownik) - utwardzona część drogi, zwykle we wsi lub mieście.
[es] Calle (sustantivo) - Una parte pavimentada de la carretera, generalmente en un pueblo o una ciudad.
...
```

**Oldest Lookups**

Use the `-o` flag to print out your oldest lookups.
```bash
defword history -o 2
```
```text
[30-04-2026 20:05:47] apple:
[en] Apple (noun) - A common, firm, round fruit produced by a tree of the genus Malus.

[30-04-2026 20:06:11] ambiguous:
[en] Ambiguous (adjective) - Open to multiple interpretations.
```

**Frequent Lookups**

Use the `-d` flag to print out words that you have looked up multiple times.
```bash
defword history -d
```
```text
street - 3 times
slow - 3 times
```

---

## Development

If you want to run the development version, simply clone this repository to your machine and install the dependencies:

```bash
git clone https://github.com/Mionuel/defword.git
cd defword
pip install -r requirements.txt
```

This project was originally created with `venv`. Clone the repo, cd inside the cloned directory and start the venv setup script (`start_dev.sh`) for quick environment setup and a one-time alias for testing. 

*Note: The script will automatically create the `.venv` directory, install all the necessary dependencies, and activate the virtual environment.*

If you would prefer to used another environment manager (like conda) the environment.yml file was provided as well.

**Compilation:** PyInstaller was used to compile the project into a standalone binary.