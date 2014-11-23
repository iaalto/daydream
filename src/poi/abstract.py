import abc

class AbstractPoi:
    """Abstract class for Points Of Interest (POI)."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, location, content):
        """Initialize a new sound point of interest.

        :param location: Location of point of interest
        :param content: Pointer to POI content
        """
        self._location = location
        self._content = content

    @abc.abstractmethod
    def location(self):
        """Return location."""
        return

    @abc.abstractmethod
    def content(self):
        """Return content."""
        return