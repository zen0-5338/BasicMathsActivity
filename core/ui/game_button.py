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

from typing import Optional, SupportsFloat

from pygame import error, Surface, mouse
from pygame.font import Font
from pygame.color import Color


from core.ui.fonts import GameFont
from core.utils import logger


class GameButton:
    """Class for creating game buttons"""

    def __init__(
        self,
        label: str,
        x: SupportsFloat,
        y: SupportsFloat,
        font: Optional[Font | GameFont] = None,
        color: Optional[Color | str | int] = None,
        background_color: Optional[Color | str | int] = None,
        **kwargs,
    ) -> None:
        """Instantiate a button

        Args:
            label (str): Label text.
            x (SupportsFloat): X coordinate of button.
            y (SupportsFloat): Y coordinate of button.
            font (Optional[Font]): Font for rendering the text.
        """

        self.label = label
        self.font = font or GameFont.TIMES_NEW_ROMAN_12PT
        self.color = color
        self.background_color = background_color

        # Render Button
        try:
            self.button = self.font.render(
                label,
                True,
                ((0, 0, 255) or self.color),
                self.background_color,
            )
        except error as button_rendering_error:
            logger.error(f"Failed to render button for {label}. ", exc_info=True)
            self.button = Surface()

        self.rect = self.button.get_rect()
        self.rect.x, self.rect.y = x, y

        self.hovered = False

    def check_mouse_hover(self) -> bool:
        """Checks whether mouse is hovering over button\
        and updates its hover state accordingly"""
        if self.rect.collidepoint(mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                self.button = self.font.render(
                    self.label,
                    True,
                    (122, 245, 61),
                    (102, 110, 98),
                )
                return True
        else:
            self.hovered = False
            self.object = self.font.render(
                self.label,
                True,
                ((0, 0, 255) or self.color),
                self.background_color,
            )
            return False
