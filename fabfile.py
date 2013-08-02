from fabric.api import local


def commit():
    try:
        local("git add -p && git add . && git commit -a")
    except:
        pass


def push():
    local("git push blog_ask master")


def deploy():
    commit()
    push()
