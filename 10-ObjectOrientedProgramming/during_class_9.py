class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print("TV is on")
            print(f'TV channel: {self.channel_no}')
        else:
            print("TV is off")

    def set_channel(self, new_channel_number):
        self.channel_no = new_channel_number


#new tv is an object
new_tv = TV()
new_tv.show_status()
new_tv.turn_on()
new_tv.set_channel(5)
new_tv.show_status()
new_tv.turn_off()
new_tv.show_status()