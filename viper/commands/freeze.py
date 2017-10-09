from viper.commands import CommandFactory


class FreezeCommand(CommandFactory):
    def __init__(self, parser):
        parser_freeze = parser.add_parser(
            "freeze",
            aliases=["ls"],
            help="display installed packages",
        )
        parser_freeze.set_defaults(action=self.run)

    @staticmethod
    def run():
        pass

if __name__ == "__main__":
    FreezeCommand.run()
