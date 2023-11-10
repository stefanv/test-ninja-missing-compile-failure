import nox


@nox.session
def build(session: nox.Session) -> None:
    session.install('spin', 'meson-python')
    session.run('spin', 'build', *session.posargs)
