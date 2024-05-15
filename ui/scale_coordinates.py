# MIT License
#
# Copyright (c) 2024 zen0
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, 8and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Optional, SupportsFloat, Tuple

from pygame import display

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCALE_X = display.get_surface().get_width()/SCREEN_WIDTH
SCALE_Y = display.get_surface().get_height()/SCREEN_HEIGHT


def scale_coordinates(
    x: SupportsFloat,
    y: SupportsFloat,
    scale_x: Optional[SupportsFloat],
    scale_y: Optional[SupportsFloat],
) -> Tuple[SupportsFloat, SupportsFloat]:
    """Return coordinates scaled to world

    Args:
        x (SupportsFloat): X coordinate of point.
        y (SupportsFloat): Y coordinate of point
        scale_x (Optional[SupportsFloat]): Custom X scale factor. Auto calculated by default.
        scale_y (Optional[SupportsFloat]): Custom Y scale factor. Auto calculated by default.

    Returns:
        Tuple[SupportsFloat, SupportsFloat]: Returns the coordinates as tuple(x, y)
    """

    scale_x = SCALE_X or scale_x
    scale_y = SCALE_Y or scale_y

    return (x * scale_x, y * scale_y)
