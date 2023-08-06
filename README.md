# NeoVintageous Line Numbers

Auto-disable relative line numbers when entering Insert mode. This functionality is supported by [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous), a Vim emulator plugin for Sublime Text.

Relative line numbers help you use the `count` that you can precede some vertical motion commands (e.g., `j`, `k`, `+`, `-`) with, without having to calculate it yourself. They are especially useful in combination with other commands (e.g., `y`, `d`, `c`, `<`, `>`, `gq`, `gw`, `=`).

Support for relative line numbers is available in [Sublime Text 4](https://www.sublimetext.com/blog/articles/sublime-text-4) (build 4074) and is controlled by the `relative_line_numbers` setting.

## Installation

Install [NeoVintageousLineNumbers](https://packagecontrol.io/packages/NeoVintageousLineNumbers) via Package Control.

## Line Numbers

The `relative_line_numbers` setting changes the displayed numbers to be relative to the cursor. Together relative to the cursor.  Together with `line_numbers` there are these three combinations (cursor in line 3):

    'nonu'          'nu'            'nu'
    'nornu'         'nornu'         'rnu'

    |apple          | 1 apple       | 2 apple
    |pear           | 2 pear        | 1 pear
    |nobody         | 3 nobody      | 0 nobody
    |there          | 4 there       | 1 there

NeoVintageous supports both `'number` and `'relativenumber'` options. They both "proxy" to their underlying Sublime setting. Here are some related Vim commands:

| Command                   | Alias             | Description
| :-------------------------| :-----------------| :----------
| `:set number`             | `:set nu`         | Enable line numbers.
| `:set nonumber`           | `:set nonu`       | Enable line numbers.
| `:set number!`            | `:set nu!`        | Toggle line numbers.
| `:set relativenumber`     | `:set rnu`        | Enable line numbers.
| `:set norelativenumber`   | `:set nornu`      | Enable line numbers.
| `:set relativenumber!`    | `:set rnu!`       | Toggle line numbers.
| `yon`                     | `con`             | Toggle line numbers (Unimpaired plugin).
| `yor`                     | `cor`             | Toggle relative line numbers (Unimpaired plugin).

For detailed information about the available options, please refer to this blog post: [Neovintageous Options](https://blog.gerardroche.com/2023/06/05/neovintageous-options/).

## License

Released under the [GPL-3.0-or-later License](LICENSE).
