import cog

class Predictor(cog.Predictor):
    def setup(self):
        self.prefix = 'dong'

    @cog.input('ding', type=str, help='Ding anything will get a `dong` reply')
    def predict(self, ding):
        return f'\n\n{self.prefix} {ding}\n\n'