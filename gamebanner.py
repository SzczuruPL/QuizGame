from banner import Banner


class GameBanner:
    def __init__(self, level_band_img, level_score_img, n, qnumber, name, score):
        self.qnumber_ban = Banner(0, 0, level_band_img["up"], str(n + 1) + " z " + str(qnumber))
        self.name_ban = Banner(0, 707, level_band_img["down"], name)
        self.score_ban = Banner(849, 716, level_score_img, str(score))
        self.score_ban.set_color((255, 255, 255))

    def draw(self, surface):
        self.qnumber_ban.draw(surface)
        self.name_ban.draw(surface)
        self.score_ban.draw(surface)