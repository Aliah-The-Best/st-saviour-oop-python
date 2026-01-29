
class Music:
    def __init__ (self, title: str, artist: str, duration: float, drums: bool):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.drums = drums

    def listen(self) -> str:
        return f'you listen to {self.title} by {self.artist} for {self.duration} minutes!'
    

if __name__ == '__main__':
    circles = Music('Circles', 'Pierce the Veil', 2.1, True)
    print(circles.listen())

    Keep_Away = Music ('Keep_Away', 'Pierce the Veil', 4.50 )

    Lucky = Music ('Lucky', 'Radiohead', 3.09)

    Enjoy_The_Silence = Music ('Enjoy_The_Silence', 'Depeche Mode', 4.15 )

    ghost_girl = Music ('ghost_girl', 'lil peep', 3.06)

    star_shopping = Music ('star_shopping', 'lil peep', 2.22)