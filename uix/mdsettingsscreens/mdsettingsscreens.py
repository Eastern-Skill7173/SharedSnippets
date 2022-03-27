import os.path
from constants import UIX_DIRECTORY
from kivy.lang import Builder
from kivy.properties import ColorProperty, StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

__all__ = (
    "MDLogLayout",
    "MDInfoLayout",
)


class MDLogLayout(MDBoxLayout):
    logger_history = StringProperty()
    """
    Output of kivy's logging.
    
    :attr:`logger_history` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`
    """
    warning_note_color = ColorProperty(
        [1, 0.38823529411764707, 0.2784313725490196]
    )
    """
    Warning color for the `NOTE:` portion of the labels.
    
    :attr:`warning_note_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 0.38823529411764707, 0.2784313725490196]`
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        These widgets are meant to be initialized just once
        """
        if cls._instance is None:
            cls._instance = super(MDLogLayout, cls).__new__(cls)
        return cls._instance

    def __init__(self, **kwargs):
        super(MDLogLayout, self).__init__(**kwargs)
        self.register_event_type("on_save_changes")
        self.register_event_type("on_save_log")

    def on_save_changes(self) -> None:
        """
        Dummy method for registering 'on_save_changes' event type
        :return: None
        """

    def on_save_log(self) -> None:
        """
        Dummy method for registering 'on_save_log' event type
        :return: None
        """


class MDInfoLayout(MDBoxLayout):
    application_name = StringProperty()
    """
    Name of the application.
    
    :attr:`application_name` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """
    software_version = StringProperty("0.0.1")
    """
    Current version of the software.
    
    :attr:`software_version` is a :class:`~kivy.properties.StringProperty`
    and defaults to `"0.0.1"`.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        These widgets are meant to be initialized just once
        """
        if cls._instance is None:
            cls._instance = super(MDInfoLayout, cls).__new__(cls)
        return cls._instance


Builder.load_file(
    os.path.join(UIX_DIRECTORY, "mdsettingsscreens", "mdsettingsscreens_ui.kv")
)
