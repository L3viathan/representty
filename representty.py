import os
import sys

import IPython
from rich.markdown import Markdown
from rich.console import Console


class Presentation:
    def __init__(self, filename):
        with open(filename) as file:
            self.slides = file.read().split("====")
        self._slide_no = 0
        self.console = Console()

    @property
    def slide_no(self):
        return self._slide_no

    @slide_no.setter
    def slide_no(self, new_value):
        if 0 <= new_value <= len(self.slides) - 1:
            self._slide_no = new_value

    def bind(presentation, fn):
        class ShowTheSlide:
            def __repr__(self):
                if fn(presentation) is not False:
                    return repr(presentation)
        return ShowTheSlide()

    def __repr__(self):
        print("\r")
        slide = self.slides[self.slide_no]
        lines = []
        for line in slide.split("\n"):
            if line.strip().startswith("!!"):
                os.system(line.strip()[2:])
                continue
            elif line.strip().startswith("//"):
                continue
            lines.append(line)
        markdown = Markdown("\n".join(lines).strip())
        for token in markdown.parsed:
            if token.tag == "code" and token.info.startswith("py"):
                exec(token.content, globals())

        self.console.print(markdown)
        self.draw_slide_number()
        return ""

    def draw_slide_number(self):
        display = f" {self.slide_no} "
        position = self.console.width - len(display)
        print(f"\x1b[1A\x1b[{position}G\x1b[1;46;30m{display}", end="", flush=True)

if len(sys.argv) != 2:
    print("Usage: name-of-tool path/to/slides.md", file=sys.stderr)
    os._exit(1)

PRES = Presentation(sys.argv[1])


@PRES.bind
def n(presentation):
    presentation.slide_no += 1


@PRES.bind
def p(presentation):
    presentation.slide_no -= 1


@PRES.bind
def g(presentation):
    print("\x1b[1Ago to slide: ", end="", flush=True)
    presentation.slide_no = int(input())


@PRES.bind
def d(presentation):
    # redraw
    pass


@PRES.bind
def q(presentation):
    os._exit(0)

IPython.embed(colors="neutral")
