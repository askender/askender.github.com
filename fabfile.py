from fabric.api import local
from datetime import datetime


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


TEMPLATE = """
{title}
{hashes}

:date: {year}-{month}-{day} {hour}:{minute:02d}
:tags:
:category:
:slug: {slug}
:summary:
:status: draft


"""


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '_')
    f_create = "content/{}{:0>2}{:0>2}_{}.md".format(
        str(today.year)[2:], today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)
