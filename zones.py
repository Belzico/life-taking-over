import globals

class Zone:

    def __init__(self, tileCount, ZoneType):
        self.TileCount = tileCount
        self.ZoneType = ZoneType
        self.Danger = globals.ZoneDanger[ZoneType]
        self.TileList = []

    
    def ChangeDanger(self, newDangerInt):
        self.Danger = newDangerInt