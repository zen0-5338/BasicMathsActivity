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

from typing import Optional, SupportsFloat
from os import PathLike

from pygame import error, image, Surface, transform

from core.utils import logger


def load_sprite(
    sprite_path: PathLike,
    transparent: Optional[bool] = False,
    scale_sprite: Optional[bool] = True,
    scale_x: Optional[SupportsFloat] = None,
    scale_y: Optional[SupportsFloat] = None,
    **kwargs,
) -> Surface:
    """Load a sprite from given path, 

    Args:
        sprite_path (PathLike): The path to sprite
        transparent (Optional[bool]): Load the sprite as transparent.\
            Defaults to False.
        scale_sprite (Optional[bool]): Scale the sprite to fit in the world.\
            Defaults to true.
        scale_x (Optional[SupportsFloat]): X scaling factor.\
            Defaults to 1.0.
        scale_y (Optional[SupportsFloat]): Y scaling factor.\
            Defaults to 1.0.

    Returns:
        Surface: Surface instance of the loaded sprite
    """

    try:
        sprite = image.load(sprite_path)
        if scale_sprite:
            sx, sy = sprite.get_rect().size
            scale_x = scale_x or 1.0
            scale_y = scale_y or 1.0
            sprite = transform.scale(sprite, (int(sx * scale_x), int(sy * scale_y)))

    except error as sprite_loading_exception:
        logger.warning(
            "Unable to load sprite. Loading default surface.",
            exc_info=True,
        )
        sprite = Surface()

    sprite = sprite.convert()
    return sprite
