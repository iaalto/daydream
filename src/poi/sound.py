from abc import ABCMeta

class AbstractPoi:
    """Abstract class for Points Of Interest (POI).

    """
    __metaclass__ = ABCMeta


class SoundPoi(AbstractPoi):
    """Point of interest containing audio.

    This class contains speech, music or other audio.
    """

    def __init__(self, location, content):
        """Initialize a new sound point of interest.

        :param location: Location of point of interest
        :param content: Pointer to audio content
        """
        pass

    def render(self):
        """Renders a visual representation of POI.

        """
        pass

    def play(self):
        """Play the audio content.

        :return:
        """
        pass

    def pause(self):
        """Pause the audio content.

        :return:
        """
        pass

    def stop(self):
        """Stop audio content.

        :return:
        """
        pass
