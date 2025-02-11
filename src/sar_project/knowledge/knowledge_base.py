class KnowledgeBase:
    def __init__(self):
        """
        Initializes the knowledge base with empty datasets for terrain, weather,
        resources, and mission history.
        """
        self.terrain_data = {}
        self.weather_data = {}
        self.resource_status = {}
        self.mission_history = []
        self.clues = {}
        self.clue_tags = {}
        self.query_queue = []

    def update_terrain(self, location, data):
        """
        Updates terrain data for a specific location.

        Args:
            location (str): Name or identifier of the location.
            data (dict): Terrain-related data (e.g., elevation, obstacles).
        """
        self.terrain_data[location] = data

    def update_weather(self, location, conditions):
        """
        Updates weather data for a specific location.

        Args:
            location (str): Name or identifier of the location.
            conditions (dict): Weather conditions (e.g., temperature, wind speed).
        """
        self.weather_data[location] = conditions

    def update_resource_status(self, resource_name, status):
        """
        Updates the status of a resource.

        Args:
            resource_name (str): Name of the resource (e.g., drone, vehicle).
            status (dict): Resource status (e.g., availability, location).
        """
        self.resource_status[resource_name] = status

    def log_mission_event(self, event):
        """
        Logs an event in the mission history.

        Args:
            event (dict): Event details (e.g., timestamp, action, outcome).
        """
        self.mission_history.append(event)

    def query_terrain(self, location):
        """
        Retrieves terrain data for a specific location.

        Args:
            location (str): Name or identifier of the location.

        Returns:
            dict: Terrain-related data or an empty dictionary if not found.
        """
        return self.terrain_data.get(location, {})

    def query_weather(self, location):
        """
        Retrieves weather data for a specific location.

        Args:
            location (str): Name or identifier of the location.

        Returns:
            dict: Weather-related data or an empty dictionary if not found.
        """
        return self.weather_data.get(location, {})

    def query_resource_status(self, resource_name):
        """
        Retrieves the status of a resource.

        Args:
            resource_name (str): Name of the resource.

        Returns:
            dict: Resource status or an empty dictionary if not found.
        """
        return self.resource_status.get(resource_name, {})

    def get_mission_history(self):
        """
        Retrieves the complete mission history.

        Returns:
            list: A list of logged mission events.
        """
        return self.mission_history

    def get_clues(self):
        """
        Retrieves the list of available clues.

        Returns:
            list: A list of available clues.
        """
        return self.clues

    def get_clue(self, id: int):
        """
        Retrieves a specific clue by its ID.

        Args:
            id (int): The ID of the clue to retrieve.

        Returns:
            str: The text of the clue or an empty string if not found.
        """
        return self.clues.get(id, "")
    
    def add_clue_tag(self, id: int, tag: str):
        if tag not in self.clue_tags:
            self.clue_tags[tag] = []
        self.clue_tags[tag].append(id)

    def add_clue(self, id: int, clue: str):
        """
        Adds a new clue to the knowledge base.

        Args:
            clue (str): Text describing the clue.
        """
        self.clues[id] = clue
    
    def add_query(self, query: str):
        """
        Adds a new query to the query queue.

        Args:
            query (str): The query to be added.
        """
        self.query_queue.append(query)