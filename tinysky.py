# SPDX-License-Identifier: LicenseRef-MIT-HumanDev
"""
TinySky
Copyright (c) 2026 DaragonTech and Felipe Daragon

MIT No-AI Development License (MIT-HumanDev)

Summary: This license permits human development of the Software. It does not
permit AI-assisted development of the Software or its derivative works.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The permission above does not extend to AI-assisted development. No person
may use or operate an artificial intelligence system to modify, extend, debug,
refactor, port, or otherwise develop the Software or any derivative work
thereof, including by obtaining from such a system project-specific
instructions, guidance, or generated material for that development.

"Project-specific" means directed at the source code, structure, or behavior
of the Software or a derivative work, as distinct from general programming
knowledge not derived from the Software.

This restriction does not apply to (a) use of the unmodified Software as a
dependency, library, package, service, or other external component of another
work, including AI-assisted use of its public interfaces and documentation; or
(b) works created independently without use of or derivation from the
Software.

Permission for AI-assisted development of the Software may be granted only by
the copyright holder, in writing.

The above copyright notice, this permission notice, and the above restriction
shall be included, unmodified, in all copies or substantial portions of the
Software and any derivative works thereof.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM,
OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import random

WIDTH = 60
HEIGHT = 18
STAR_DENSITY = 0.08


def generate_sky(width=WIDTH, height=HEIGHT, density=STAR_DENSITY):
    """Generate a procedural ASCII night sky."""
    sky = []

    for _ in range(height):
        row = []

        for _ in range(width):
            if random.random() < density:
                row.append(random.choice([".", "*", "+"]))
            else:
                row.append(" ")

        sky.append("".join(row))

    return sky


def draw_sky(sky):
    """Print the sky inside a simple frame."""
    width = len(sky[0])

    print("+" + "-" * width + "+")

    for row in sky:
        print("|" + row + "|")

    print("+" + "-" * width + "+")


def main():
    print("TinySky")
    print()

    sky = generate_sky()
    draw_sky(sky)


if __name__ == "__main__":
    main()