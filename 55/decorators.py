def make_bold(func):
    def bold():
        return f"<b>{func()}</b>"

    return bold


def make_emphasis(func):
    def emphasis():
        return f"<i>{func()}</i>"

    return emphasis


def make_underline(func):
    def underline():
        return f"<u>{func()}</u>"

    return underline
