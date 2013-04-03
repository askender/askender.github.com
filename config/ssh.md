ssh-keygen -f ~/.ssh/blog_ask
scp blog_ask.pub server_hostname:~/.ssh/
ssh server_hostname
cat .ssh/id_rsa.pub >> .ssh/authorized_keys 即可
這樣子就可以 key 認證登入, 不需輸入密碼