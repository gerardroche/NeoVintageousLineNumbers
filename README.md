# NeoVintageous Line Numbers

NeoVintageous Line Numbers is a Sublime Text plugin that automates the disabling of relative line numbers when entering Insert mode. This feature seamlessly integrates with [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous), a popular Vim emulator plugin for Sublime Text.

## About Relative Line Numbers

Relative line numbers enhance your productivity by simplifying the use of the `count` feature with various vertical motion commands (e.g., `j`, `k`, `+`, `-`). They eliminate the need for manual counting, making them especially handy when combined with other commands like `y`, `d`, `c`, `<`, `>`, `gq`, `gw`, and `=`.

Support for relative line numbers is available in [Sublime Text 4](https://www.sublimetext.com/blog/articles/sublime-text-4) (build 4074) and can be controlled through the `relative_line_numbers` setting.

## Installation

### Method 1: Using Package Control

1. Open Sublime Text.
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the Command Palette.
3. Type "Package Control: Install Package" and press `Enter`.
4. In the input field, type "NeoVintageousLineNumbers" and select it from the list of available packages.

### Method 2: Manual Installation

1. Visit the [NeoVintageousLineNumbers GitHub repository](https://github.com/gerardroche/NeoVintageousLineNumbers).
2. Click on the "Code" button and select "Download ZIP."
3. Extract the downloaded ZIP file.
4. Open Sublime Text and go to `Preferences -> Browse Packages...` to open the Packages folder.
5. Copy the "NeoVintageousLineNumbers" folder from the extracted ZIP and paste it into the Packages folder.

### Method 3: Manual Git Repository Installation

1. Open a terminal or command prompt.
2. Navigate to the Sublime Text Packages directory:
    - On Windows: `%APPDATA%\Sublime Text\Packages`
    - On macOS: `~/Library/Application Support/Sublime Text/Packages`
    - On Linux: `~/.config/sublime-text/Packages`
3. Clone the plugin repository directly into the Packages directory using Git:
   ```
   git clone https://github.com/gerardroche/NeoVintageousLineNumbers.git NeoVintageousLineNumbers
   ```

## Line Numbers

The `relative_line_numbers` setting modifies the displayed line numbers to be relative to the cursor's position. When used in combination with the `line_numbers` setting, it offers three possible configurations (assuming the cursor is on line 3):

```
'nonu'          'nu'            'nu'
'nornu'         'nornu'         'rnu'

|apple          | 1 apple       | 2 apple
|pear           | 2 pear        | 1 pear
|nobody         | 3 nobody      | 0 nobody
|there          | 4 there       | 1 there
```

NeoVintageous supports both `'number` and `'relativenumber'` options, which mirror their underlying Sublime settings. Here are some related Vim commands:

| Command                   | Alias             | Description
| :-------------------------| :-----------------| :----------
| `:set number`             | `:set nu`         | Enable line numbers.
| `:set nonumber`           | `:set nonu`       | Disable line numbers.
| `:set number!`            | `:set nu!`        | Toggle line numbers.
| `:set relativenumber`     | `:set rnu`        | Enable relative line numbers.
| `:set norelativenumber`   | `:set nornu`      | Disable relative line numbers.
| `:set relativenumber!`    | `:set rnu!`       | Toggle relative line numbers.
| `yon`                     | `con`             | Toggle line numbers (Unimpaired plugin).
| `yor`                     | `cor`             | Toggle relative line numbers (Unimpaired plugin).

For comprehensive information about available options, please refer to this [Neovintageous Options blog post](https://blog.gerardroche.com/2023/06/05/neovintageous-options/).

## License

Released under the [GPL-3.0-or-later License](LICENSE).
