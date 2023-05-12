# representty

`representty` is a tiny presentation framework. TL;DR: You write your slides in
Markdown, `rich` renders individual slides, and the whole thing happens in an
IPython shell.

[![asciicast](https://asciinema.org/a/584388.svg)](https://asciinema.org/a/584388)

## File Format

A slide deck is mostly a Markdown file. Individual slides are seperated by a
bunch of equals signs.

Additionally, you can start a line with:

- `//`: comment; the line is ignored (unless the environment variable
  `PRACTICE` is set).
- `!`: special instruction. The line is not included in the output, but can do
  a variety of things:
    - `!!some command`: execute the command with `os.system()` the first time
      this slide is visited.
    - `!import somemodule`: silently import the given module.
    - `!set flag`/`!unset flag`: set/unset a named flag. These can influence
      `representty` behaviour. See [flags](#flags).
    - `!setlocal flag`/`!unsetlocal flag`: (un)set a flag, but reset to
      original value at the end of the slide.
    - `!image someimage`: Display an image. This only works if you have
      `viu` installed.
    - `!up some_int`: Move the cursor up by some amount. Useful for drawing
      over images.
    - `!printf something`: Call `printf` with the given args. Better than
      plain `!!printf`, because it will be executed every time the slide is
      displayed by default.

Python code blocks (language starts with `py`) are not just rendered, but also
executed.

## Commands

The presenter is dropped into a more-or-less normal IPython shell. A few
single-letter commands exist which control the slide show:

- `d`: (Re)draw the current slide.
- `n`: Go to the next slide.
- `p`: Go to the previous slide.
- `q`: Quit.
- `g`: Go to a numbered slide (you will be prompted for a slide number).
- `s`: Go to a slide by searching for a keyword (you will be prompted).

## Flags

- `exec`: whether to execute Python code in code blocks. Default: set.
- `alwaysexec`: Always execute shell commands (`!!`), rather than just at the
  first printing of the slide. Default: unset.
