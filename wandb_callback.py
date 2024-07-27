class WandbCustomCallback(BaseCallback):
    def __init__(self, verbose=0, **kwargs):
        super(WandbCustomCallback, self).__init__(verbose, **kwargs)
        self.step = 0
        self.hyperparams = kwargs  # Передача гиперпараметров через **kwargs
        self.rewards= []

    def _on_step(self) -> bool:
        self.step += 1
        infos = self.locals["infos"]

        for info in infos:
            if "episode" in info.keys():
                wandb.log({"reward": info["episode"]["r"], "length": info["episode"]["l"]}, step=self.step)

        return True

    def _on_episode_start(self) -> None:
        # Начало нового эпизода, создаем новый список для хранения вознаграждений
        self.reward.append([])

        return True
