# MIT License
#
# Copyright (c) 2024 zen0-5338
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

from typing import Optional, SupportsFloat, Union

from pygame import error, Surface
from pygame.font import Font
from pygame.color import Color


from core.ui.fonts import GameFont
from core.utils import logger


class TextBox:
    """Class for creating game buttons"""

    def __init__(
        self,
        label: str,
        x: SupportsFloat,
        y: SupportsFloat,
        font: Optional[Union[Font, GameFont]] = None,
        color: Optional[Union[Color, str, int]] = None,
        background_color: Optional[Union[Color, str, int]] = None,
        **kwargs,
    ) -> None:
        """Instantiate a Text Box

        Args:
            label (str): Label text.
            x (SupportsFloat): X coordinate of text_box.
            y (SupportsFloat): Y coordinate of text_box.
            font (Optional[Font]): Font for rendering the text.
            scale_button (Optional[bool]): Whether to scale the text_box\
                according to screen. Defaults to True.
        """

        self.label = label
        self.font = font
        self.color = color
        self.background_color = background_color

        # Render Text Box
        try:
            self.text_box = self.font.render(
                label,
                True,
                ((0, 0, 0) or self.color),
                self.background_color,
            )
        except error as button_rendering_error:
            logger.error(f"Failed to render textbox for {label}. ", exc_info=True)
            self.text_box = Surface()

        self.rect = self.text_box.get_rect()
        self.rect.x, self.rect.y = x - self.rect.width() / 2, y
