class Radio:
    def __init__(self, mode="FM", frequency=87.5):
        self.mode = mode
        self.frequency = frequency

    def get_mode(self):
        return self.mode
    def set_mode(self, mode):
        if mode == "FM":
            self.frequency = 87.5
        elif mode == "AM":
            self.frequency = 150 
        self.mode = mode

    def get_frequency(self):
        return self.frequency
    def set_frequency(self, frequency):
        if self.mode == "FM" and 87.5 <= frequency <= 108:
            self.frequency = frequency
        elif self.mode == "AM" and 150 <= frequency <= 280:
            self.frequency = frequency

    def adjust_frequency(self, frequency): 
        if self.mode == "FM":
            if 87.5 <= self.frequency + frequency <= 108:
                self.frequency += frequency
                return True
        elif self.mode == "AM":
            if 150 <= self.frequency + frequency <= 280:
                self.frequency += frequency
                return True
        return False

    def __str__(self):
        if self.mode == "FM":
            unit = "M"
        elif self.mode == "AM":
            unit = "k"
        output = f"{self.mode} Radio: {self.frequency:.1f} {unit}Hz"
        return output