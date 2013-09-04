ssh-keygen -f ~/.ssh/blog_ask
scp ~/.ssh/blog_ask.pub server_hostname:~/.ssh/
ssh server_hostname
cat .ssh/blog_ask.pub >> .ssh/authorized_keys 即可
