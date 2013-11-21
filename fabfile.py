from fabric.api import local


def commit():
    try:
        # local("git add -p && git add . && git commit -a")
        local("git add . && git commit -am 'new' ")
    except:
        pass


def push():
    local("git push origin master")


def deploy():
    commit()
    push()
