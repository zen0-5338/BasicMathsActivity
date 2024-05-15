#!/usr/bin/env python3

# MIT License
#
# Copyright (c) <2024:year> zen0
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

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from gettext import gettext
from core.utils import logger

import pygame
from sugar3.activity.activity import Activity
from sugar3.activity.widgets import ActivityToolbarButton, StopButton
from sugar3.graphics.toolbarbox import ToolbarBox

logger.debug("Started Sugar.")

import sugargame.canvas as sugar_canvas
from core import Game


class BasicMathsActivity(Activity):
    """
    Activity class wrapper to run the mathematics game
    inside Sugar Application
    """

    def __init__(self, handle: Activity):
        """
        Initiate main instance, can only have one activity instance
        and one instance can have only one game inside.

        Args:
            handle (SugarObject): Parent sugar object.
        """
        try:
            Activity.__init__(self, handle)
        except Exception as activity_instantiation_exception:
            logger.critical("Failed to instantiate Activity class", exc_info=True)

        # No collaboration for the alpha version
        self.max_participants = 1

        # Initialise game
        try:
            self.game_instance = Game(self)
        except Exception as game_instantiation_exception:
            logger.critical("Failed to instantiate Game class", exc_info=True)

        # Initialise UI
        self.build_ui()

        # Run game
        self.game_canvas = sugar_canvas.PygameCanvas(
            self,
            main=self.game_instance.run,
            modules=[pygame.display, pygame.font, pygame.mixer],
        )
        self.set_canvas(self.game_canvas)
        self.game_canvas.grab_focus()

    def build_ui(self) -> None:
        """Function for initial creation of UI"""

        toolbar_box = ToolbarBox()

        # Activity Button
        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        # Separator between buttons
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        # Stop Button
        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(self.stop_button, -1)
        stop_button.connect("clicked", self.stop)
        stop_button.show()

        # Show toolbar
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

    def stop(self, button: StopButton) -> None:
        """Stop the running activity instance. Also stops all child processes

        Args:
            button (StopButton): The UI button that calls this function.
        """

        self.game_instance.stop()
        self.close()
