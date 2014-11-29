import abc


class AbstractPoi:
    """Abstract class for Points Of Interest (POI)."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, poi_id, poi, location, content):
        """Initialize a new point of interest.

        :param poi_id: se ID for the object. Database returns it when saved, initially None.
        :param poi: Description for point of interest
        :param location: Location of point of interest
        :param content: Pointer to POI content
        """
        self.poi_id = str(poi_id)
        self.poi = poi
        self._location = location
        self._content = content

    @abc.abstractmethod
    def render(self):
        """Renders a visual representation of POI."""
        pass

    @abc.abstractmethod
    def location(self):
        """Return location."""
        return

    @abc.abstractmethod
    def content(self):
        """Return content."""
        return
