from fabric.api import local


def commit():
    local("git add -p && git add . && git commit -a")


def push():
    local("git push ae_gh")


def deploy():
    commit()
    # push()
