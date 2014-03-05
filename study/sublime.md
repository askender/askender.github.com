打开/前往

⌘T   前往文件
⌘⌃P  前往项目
⌘R   前往 method
⌘⇧P  命令提示
⌃G   前往行
⌃ `  python 控制台
编辑

⌘L   选择行 (重复按下将下一行加入选择)
⌘D   选择词 (重复按下时多重选择相同的词进行多重编辑)
⌃⇧M  选择括号内的内容
⌘⇧↩  在当前行前插入新行
⌘↩   在当前行后插入新行
⌃⇧K  删除行
⌘KK  从光标处删除至行尾
⌘K⌫  从光标处删除至行首
⌘⇧D  复制(多)行
⌘J   合并(多)行
⌘KU  改为大写
⌘KL  改为小写
⌘ /  注释
⌘⌥ /   块注释
⌘Y   恢复或重复
⌘⇧V  粘贴并自动缩进
⌃ space  自动完成(重复按下选择下一个提示)
⌃M   跳转至对应的括号
XML/HTML

⌘⇧A  选择标签内的内容
⌘⌥ .   闭合当前标签
查找/替换

⌘F   查找
⌘⌥F  替换
⌘⌥G  查找下一个符合当前所选的内容
⌘⌃G  查找所有符合当前所选的内容进行多重编辑
⌘⇧F  在所有打开的文件中进行查找
拆分窗口/标签页

⌘⌥1  单列
⌘⌥2  双列
⌘⌥5  网格 (4组)
⌃[1,2,3,4]   焦点移动至相应组
⌃⇧[1,2,3,4]  将当前文件移动至相应组
⌘[1,2,3…]  选择相应标签页
书签

⌘F2  添加/去除书签
F2   下一个书签
⇧F2  前一个书签
⌘⇧F2   清除书签
标记

⌘K space   设置标记
⌘KW  从光标位置删除至标记
⌘KA  从光标位置选择至标记
⌘KG  清除标记


Ctrl+L 选择整行（按住-继续选择下行）
Ctrl+KK 从光标处删除至行尾
Ctrl+Shift+K 删除整行
Ctrl+Shift+D 复制光标所在整行，插入在该行之前
Ctrl+J 合并行（已选择需要合并的多行时）
Ctrl+KU 改为大写
Ctrl+KL 改为小写
Ctrl+D 选词 （按住-继续选择下个相同的字符串）
Ctrl+M 光标移动至括号内开始或结束的位置
Ctrl+Shift+M 选择括号内的内容（按住-继续选择父括号）
Ctrl+/ 注释整行（如已选择内容，同“Ctrl+Shift+/”效果）
Ctrl+Shift+/ 注释已选择内容
Ctrl+Space 自动完成（win与系统快捷键冲突，需修改）
Ctrl+Z 撤销
Ctrl+Y 恢复撤销
Ctrl+Shift+V 粘贴并自动缩进（其它兄弟写的，实测win系统自动缩进无效）
Ctrl+M 光标跳至对应的括号
Alt+. 闭合当前标签
Ctrl+Shift+A 选择光标位置父标签对儿
Ctrl+Shift+[ 折叠代码
Ctrl+Shift+] 展开代码
Ctrl+KT 折叠属性
Ctrl+K0 展开所有
Ctrl+U 软撤销
Ctrl+T 词互换
Tab 缩进
Shift+Tab 去除缩进
Ctrl+Shift+UP 与上行互换
Ctrl+Shift+DOWN 与下行互换
Ctrl+K Backspace 从光标处删除至行首
Ctrl+Enter 插入行后
Ctrl+Shift Enter 插入行前
F9 行排序（按a-z）

http://cloudaice.com/subline-text2-shortcuts/

sudo add-apt-repository ppa:webupd8team/sublime-text-2
sudo apt-get update
sudo apt-get install sublime-text
按Ctrl+`调出console
粘贴以下代码到底部命令行并回车：
import urllib2,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();os.makedirs(ipp) if not os.path.exists(ipp) else None;open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())

subl plugins:
SublimeLinter
AutoPEP8
Python Pep8 Lint
Tag
git
JS Format
Js Minifier
LESS
Pretty JSON
Alignment
FileDiffs
SideBarEnhancements

GBK Encoding Support

git gutter

Ninja IDE (ninja-ide.org)
Ninja IDE(Ninja is not just another IDE) is a cross-platform Python integrated development environment. This IDE sports plenty of good features like built-in PEP8 checking,  linting, tools for managing Plugins and an extensible plugin interface.
Ninja IDE是一个跨平台的PyIDE，这个IDE支持很多的好的特性，比如内建PEP8检测，和一个很好的可拓展的插件界面

BrowserRefresh-Sublime (github.com)
After this plugin you can hit ‘command + shift + r’ on any window in Sublime Text 2 and your Google Chrome window will come to the foreground and reload the active tab. If the current file is unsaved, it
 will be saved before Chrome is activated and reloaded. Awesome!
简单的来说这就是一个live coding，配合Sublime Text 2 和Chrome 快捷键command + shift + r’如果这个文件还没有保存，在这之后它会被保存在Chrome被激活和重载之前



 sublime text 2快捷键总结
一：编辑（我们使用一个编辑器最频繁的事情就是编辑了。）
   （1）基本操作：

         【1】Command+A:全选

         【2】Command+C:复制

         【3】Command+V:粘贴

         【4】 Command+X:剪切

         【5】Command+Z：撤销

         【6】Command+Y：重做

        对于代码来说：Command+V还有一个高级一点的快捷键就是：

         【7】Shift+Command+V：它的作用是粘贴并处理缩进。

  （2 ）行操作，Eclipse有丰富的行操作快捷键。我很喜欢。sublime text 2 也有很多。

        【1】Ctrl+Command+Up：将行上移。

        【2】Ctrl+Command+Down:将行下移.

        【3】Command+X：剪切当前行（可以当成删除当前行来用）（如果有选中的区域就是剪切行踪区域啦。）

        【5】Shift+Command+D:向上复制当前行（即在当前行的上面插入同样的一行内容，光标还在当前行）

        【6】Command+C:在没有选择区域时，复制当前行。（Shift+Command+D:相当于Command+C然后Command+V)

        【7】Command+] 增加缩进(即将行向右移）

        【8】Command+[ 减少缩进（即将行向左移）

        【9】Ctrl+Shift+K：删除当前行。（这个是真的删除了。Command+X是剪切）

        【10】Ctrl+K:删除到行尾。(Kill)

        【11】 Coman+Backspace ：删除到行开头

        【12】Command+Enter:在当前行下面插入一行

        【13】Shift+Command+Enter:在当前行上面插入一行。

        【14】Command+/:注释或者反注释当前行（或者 选中行）

   （3）文本操作

          【1】 Command+K,Commamnd+U:将所选或所在单词转成大小。(Convert(K) to Uppcase)

          【2】 Command+K,Command+L:将所选或所在单词转成小写(Convert(K) to Lower)


 二： 移动操作
 在Vim中这是一个很重要的方面，但是在其它编辑器中这个问题却容易被忽略。

          【1】Command+Left ：移动到行首。mac 通用

          【2】Command+Right:移动到行尾。mac 通用

          【3】 Home :移动到文件头（还可以用Command+Up)

          【4】 End:移动到文件尾(还可以用Command+Down)

          【5】Ctrl+G:跳转到指定行。(Go

          【6】Ctrl+L:将所在行滚动到屏幕中（如果可以的话）(Locate)

          【7】Ctrl+M:移到所匹配的对应的括号去。(Matching Bracket


四：多行编辑
这是Sublime text 2的一个特色。

          【1】Ctrl+Shift+Down:加上下面的一行

          【2】Ctrl+Shift+Up:加上上面的一行。

          【3】Command+D: (word)加上下一个同样的单词（用于重构局部变量名特别实用。）

五：选择
      很多时候，我们都习惯了用鼠标来选择。但是有时候，熟练的使用一些快捷键来选择效果更好。

      【1】 Command+L:选择当前行(Line),这个命令可以不常用，因为可以使用行操作中的命令来代替。

      【2】Ctrl+Shift+M:选择最近的匹配的括号对（Matching)

      【3】  Shift+Command+J:选择当前有同样的缩进的连续（包括空行）行。

六：文件
     （1）基本操作

         【1】 Command+N:新建
         【2】 Command+O:打开

         【3】 Command+S:保存

         【4】 Alt+Command+S:全部保存


    （2）多文件编辑

             【1】Command+N:N表示切换到第N个标签页去。

             【2】Alt+Command+Left:下一个文件。

             【3】Alt+Command+Right:上一个文件

             【4】Command+P:根据文件名，或者文件中的内容定位文件。

             【5】Command+R:根据符号定位。（可以根Comand+P中使用@符号来定位包含某符号的文件 ）

        (如果你也用Eclipse那么这个命令相当于Ctrl+O

      （3）多窗口

              【1】Alt+Command+N:N指同时显示的窗口列数。


七：使用命令
   【1】Shift+Command+P:打开命令命令。可以在这里输入你想执行的操作。Sublime text 2的模糊搜索很快很强大。这也是一个很受人喜欢的命令啦。

   【2】Command+` :打开控制台
