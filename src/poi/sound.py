from src.poi.abstract import AbstractPoi


class SoundPoi(AbstractPoi):
    """Point of interest containing audio.

    This class contains speech, music or other audio.
    """

    def __init__(self, poi_id, poi, location, content):
        """Initialize a new sound point of interest.

        :param poi_id: Database ID for the object. Database returns it when saved, initially None.
        :param poi: Description for point of interest
        :param location: Location of point of interest
        :param content: Pointer to audio content
        """
        super().__init__(poi_id, poi, location, content)

    def render(self):
        """Renders a visual representation of POI."""
        print('POI ID: ' + self.poi_id)
        print('Description: ' + self.poi)
        print('Location: ' + self.location)
        print('Content: ' + self.content)

    def play(self):
        """Play the audio content."""
        pass

    def pause(self):
        """Pause the audio content."""
        pass

    def stop(self):
        """Stop audio content."""
        pass

    @property
    def location(self):
        """Return location."""
        return self._location

    @property
    def content(self):
        """ Return content."""
        return self._content
