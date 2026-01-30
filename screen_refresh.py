class ScreenRefresh(plugins.Plugin):
    __author__ = 'pwnagotchi [at] rossmarks [dot] uk'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Refresh the e-ink display after X amount of updates'

    # Add default options
    __defaults__ = {
        "refresh_interval": 5  # default to 5 UI updates
    }

    def __init__(self):
        self.update_count = 0

    def on_loaded(self):
        logging.info("Screen refresh plugin loaded")

    def on_ui_update(self, ui):
        self.update_count += 1
        # Use get() with default to avoid KeyError
        interval = int(self.options.get('refresh_interval', self.__defaults__["refresh_interval"]))
        if self.update_count >= interval:
            ui.init_display()
            ui.set('status', "Screen cleaned")
            logging.info("Screen refreshing")
            self.update_count = 0
