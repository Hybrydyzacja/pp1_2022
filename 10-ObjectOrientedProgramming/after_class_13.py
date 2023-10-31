class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_list = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def volume_increase(self):
        if self.volume < 10 and self.volume >= 0:
            self.volume += 1
        else:
            print("Max volume, cannot increase")

    def volume_decrease(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Min volume, cannot decrease")

    def show_status(self):
        if self.is_on:
            print(f"Volume is {self.volume}")
            if self.channel_no <= len(self.channel_list):
                print(
                    f"TV is on, channel {self.channel_no} ({self.channel_list[self.channel_no-1]})")
            else:
                print("TV is on, channel out of range")
        else:
            print("TV is off")

    def set_channel(self, new_channel_number):
        self.channel_no = new_channel_number

    def set_channels(self, channel_list):
        self.channel_list = channel_list

    def show_channels(self):
        print(f"Available channels: {self.channel_list}")


new_tv = TV()
new_tv.show_status()
new_tv.turn_on()
# new_tv.show_channels()
new_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
new_tv.show_channels()
new_tv.set_channel(4)
# new_tv.show_status()
new_tv.volume_increase()
new_tv.volume_decrease()
new_tv.show_status()
new_tv.turn_off()
