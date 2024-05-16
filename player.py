class Player:
    def __init__(self,color , name = 'someone') :
        self.disks = 30
        self.color = color
        self.name =  name

    def update(self, disks):
        self.disks = disks       