class MemSlice(object):
    #Data to be initialized on object creation
    def __init__(self, bytestream):
        self.head_size = bytestream[0]
        self.scene_size = bytestream[1]
        self.data_size = bytestream[2]
        self.offset = bytestream[3]
        
        self.scene = bytestream[self.head_size : self.head_size + self.scene_size]
        self.data = bytestream[(self.head_size + self.scene_size) : (self.head_size + self.scene_size) + self.data_size]
        
    #return header+scene+data as bytestream
    def to_bytestream():
        return bytearray(self.head_size).join(bytearray(self.scene_size)).join(bytearray(self.data_size)).join(bytearray(self.offset)).join(bytearray(self.scene)).join(bytearray(self.data))

