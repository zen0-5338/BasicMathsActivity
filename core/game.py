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

from gettext import gettext
import random
import time

import pygame
import gi
from gi.repository import Gtk

gi.require_version("Gtk", "3.0")

from sugar3.activity.activity import Activity, get_activity_root

from utils import logger
from ui import GameButton, GAME_BACKGROUND_PATH, load_sprite, TextBox
from ui.fonts import GameFont


class Game:
    """Game class for Mathematics activity"""

    def __init__(self, parent_activity: Activity) -> None:
        """Create the game instance to play

        Args:
            parent_activity (Activity): Parent Sugar Activity.
        """

        self.parent_activity = parent_activity
        self.username = ""
        self.keys = tuple()

    def run(self) -> None:
        """Run the game instance"""

        self.screen = pygame.display.get_surface()
        if not self.screen:
            logger.warning("Could not load surface. Creating screen using set_mode.")
            self.screen = pygame.display.set_mode(
                (pygame.display.Info().current_w, pygame.display.Info().current_h)
            )

        self.background = load_sprite(GAME_BACKGROUND_PATH)
        self.screen.blit(self.background, (0, 0))

        self.font = GameFont.TIMES_NEW_ROMAN_12PT_SCALED
        self.running = True
        self.main_menu()

    def main_menu(self) -> None:
        self.play_button = GameButton(gettext("Play"), 475, 180)
        self.quit_button = GameButton(gettext("Quit"), 475, 360)
        self.buttons = [self.play_button, self.quit_button]
        self.title = TextBox(gettext("Select the correct shape"))

        self.screen.blit(self.play_button, self.play_button.rect)
        self.screen.blit(self.quit_button, self.quit_button.rect)
        self.screen.blit(self.title, self.title.rect)

        while Gtk.events_pending():
            Gtk.main_iteration()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

            elif event.type == pygame.MOUSEMOTION:
                for btn in self.buttons:
                    btn.check_mouse_hover()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.quit_button.check_mouse_hover():
                    self.stop()

    def stop(self) -> None:
        """Stop the running instance"""

        self.running = False
