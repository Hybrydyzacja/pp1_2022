class TV():
    def __init__(self):
        self.is_on = False
        self.channel_list = []

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")

    def set_channels(self, channel_list):
        self.channel_list = channel_list

    def show_channels(self):
        print(f"Available channels: {self.channel_list}")


new_tv = TV()
new_tv.show_status()
new_tv.turn_on()
new_tv.show_status()
new_tv.show_channels()
new_tv.set_channels(["TVP1, TVP2, Polsat, TVN, Filmbox, Discovery"])
new_tv.show_channels()
new_tv.show_status()
new_tv.turn_off()
