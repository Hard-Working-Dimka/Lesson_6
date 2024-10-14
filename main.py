import urwid


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def is_very_long(password):
    return len(password) >= 12


def has_letters(password):
    return any(symbol.isalpha for symbol in password)


def as_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not symbol.isdigit() and not symbol.isalpha() for symbol in password)


def password_rating(password):
    rating = 0
    password_verification = [
        is_very_long(password),
        has_digit(password),
        has_letters(password),
        as_upper_letters(password),
        has_lower_letters(password), has_symbols(password),
    ]
    for check in password_verification:
        if check:
            rating = rating + 2
    return rating


def main():
    def on_ask_change(edit, new_password):
        reply.set_text("Ваш пароль имеет рейтинг: %s" % password_rating(new_password))

    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text('')
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == '__main__':
    main()
