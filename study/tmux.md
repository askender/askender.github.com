Tmux操作方法
下表列出了tmux键盘操作的方法。

Ctrl+b	激活控制台；此时以下按键生效
系统操作
?	列出所有快捷键；按q返回
d	脱离当前会话；这样可以暂时返回Shell界面，输入tmux attach能够重新进入之前的会话
D	选择要脱离的会话；在同时开启了多个会话时使用
Ctrl+z	挂起当前会话
r	强制重绘未脱离的会话
s	选择并切换会话；在同时开启了多个会话时使用
:	进入命令行模式；此时可以输入支持的命令，例如kill-server可以关闭服务器
[	进入复制模式；此时的操作与vi/emacs相同，按q/Esc退出
~	列出提示信息缓存；其中包含了之前tmux返回的各种提示信息
窗口操作
c	创建新窗口
&	关闭当前窗口
数字键	切换至指定窗口
p	切换至上一窗口
n	切换至下一窗口
l	在前后两个窗口间互相切换
w	通过窗口列表切换窗口
,	重命名当前窗口；这样便于识别
.	修改当前窗口编号；相当于窗口重新排序
f	在所有窗口中查找指定文本
面板操作
”	将当前面板平分为上下两块
%	将当前面板平分为左右两块
x	关闭当前面板
!	将当前面板置于新窗口；即新建一个窗口，其中仅包含当前面板
Ctrl+方向键	以1个单元格为单位移动边缘以调整当前面板大小
Alt+方向键	以5个单元格为单位移动边缘以调整当前面板大小
Space	在预置的面板布局中循环切换；依次包括even-horizontal、even-vertical、main-horizontal、main-vertical、tiled
q	显示面板编号
o	在当前窗口中选择下一面板
方向键	移动光标以选择面板
{	向前置换当前面板
}	向后置换当前面板
Alt+o	逆时针旋转当前窗口的面板
Ctrl+o	顺时针旋转当前窗口的面板
四、Tmux的配置
Tmux的系统级配置文件为/etc/tmux.conf，用户级配置文件为~/.tmux.conf。配置文件实际上就是tmux的命令集合，也就是说每行配置均可在进入命令行模式后输入生效。

下面是一个~/.tmux.conf的示例，其中包括了一些常用的配置：

#此类配置可以在命令行模式中输入show-options -g查询
#窗口的初始序号；默认为0，这里设置为1
set-option -g base-index 1
#提示信息的持续时间；设置足够的时间以避免看不清提示，单位为毫秒
set-option -g display-time 5000
#控制台激活后的持续时间；设置合适的时间以避免每次操作都要先激活控制台，单位为毫秒
set-option -g repeat-time 1000
#操作状态栏时的默认键盘布局；可以设置为vi或emacs
set-option -g status-keys vi
#设置右状态栏的内容
set-option -g status-right "#(date +%H:%M' ')"
#设置右状态栏右方的内容长度；建议把更多的空间留给状态栏左方（用于列出当前窗口）
set-option -g status-right-length 10
#开启状态栏的UTF-8支持
set-option -g status-utf8 on

#此类设置可以在命令行模式中输入show-window-options -g查询
#复制模式中的默认键盘布局；可以设置为vi或emacs
set-window-option -g mode-keys vi
#开启窗口的UTF-8支持
set-window-option -g utf8 on

#将激活控制台的快捷键由Ctrl+b修改为Ctrl+a
set-option -g prefix C-a
unbind-key C-b
bind-key C-a send-prefix

#添加自定义快捷键
#按z结束当前会话；相当于进入命令行模式后输入kill-session
bind-key z kill-session
#按h将当前面板布局切换为even-horizontal
#相当于进入命令行模式后输入select-layout even-horizontal
bind-key h select-layout even-horizontal
#按v将当前面板布局切换为even-vertical
#相当于进入命令行模式后输入select-layout even-vertical
bind-key v select-layout even-vertical
参考文献:

http://www.wikivs.com/wiki/Screen_vs_tmux

http://wiki.freebsdchina.org/software/t/tmux

# Setting the prefix from `C-b` to `C-a`.
# By remapping the `CapsLock` key to `Ctrl`,
# you can make triggering commands more comfottable!
set -g prefix C-a

# Free the original `Ctrl-b` prefix keybinding.
unbind C-b

# Ensure that we can send `Ctrl-a` to other apps.
bind C-a send-prefix

# Reload the file with Prefix r.
bind r source-file ~/.tmux.conf \; display "Reloaded!"

# Splitting panes.
bind | split-window -h
bind - split-window -v

# Moving between panes.
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R

# Moveing between windows.
# Provided you've mapped your `CAPS LOCK` key to the `CTRL` key,
# you can now move between panes without moving your hands off the home row.
bind -r C-h select-window -t :-
bind -r C-l select-window -t :+

# Pane resizing.
bind -r H resize-pane -L 5
bind -r J resize-pane -D 5
bind -r K resize-pane -U 5
bind -r L resize-pane -R 5

# Maximize and restore a pane.
unbind Up
bind Up new-window -d -n tmp \; swap-pane -s tmp.1 \; select-window -t tmp
unbind Down
bind Down last-window \; swap-pane -s tmp.1 \; kill-window -t tmp

# Log output to a text file on demand.
bind P pipe-pane -o "cat >>~/#W.log" \; display "Toggled logging to ~/#W.log"

# Vimlike copy mode.
unbind [
bind Escape copy-mode
unbind p
bind p paste-buffer
bind -t vi-copy 'v' begin-selection
bind -t vi-copy 'y' copy-selection

# Setting the delay between prefix and command.
set -sg escape-time 1

# Set the base index for windows to 1 instead of 0.
set -g base-index 1

# Set the base index for panes to 1 instead of 0.
setw -g pane-base-index 1

# Mouse support - set to on if you want to use the mouse.
setw -g mode-mouse off
set -g mouse-select-pane off
set -g mouse-resize-pane off
set -g mouse-select-window off

# Set the default terminal mode to 256color mode.
set -g default-terminal "screen-256color"

# Enable activity alerts.
setw -g monitor-activity on
set -g visual-activity on

# Pane colors.
set -g pane-border-fg green
set -g pane-border-bg black
set -g pane-active-border-fg white
set -g pane-active-border-bg yellow

# Command / message line.
set -g message-fg white
set -g message-bg black
set -g message-attr bright

# Enable vi keys.
setw -g mode-keys vi

# Status bar
set -g status-left-length 52
set -g status-right-length 451
set -g status-fg white
set -g status-bg colour234
set -g window-status-activity-attr bold
set -g pane-border-fg colour245
set -g pane-active-border-fg colour39
set -g message-fg colour16
set -g message-bg colour221
set -g message-attr bold
set -g window-status-format "#[fg=white,bg=colour234] #I #W "
