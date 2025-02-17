from components.map_site import MapSite


class Wall(MapSite):
    def enter(self):
        print("Entered Wall")

    def __repr__(self) -> str:
        return "The Wall"
