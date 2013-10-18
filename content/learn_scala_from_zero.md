Title: 从零开始学scala
Date: 1980-01-01
Tags: study, coding
Slug: learn_scala_from_zero
Summary: 

接触过各种编程语言，c, php，python, nodejs，java，go，lisp，其实都只会一点皮毛。一直认为语言得于具体的使用需求联系才能产生作用。
公司技术选型选定scala，现在学习新的语言scala，希望能更深入些。

先从一份中文资料看起
<http://qiujj.com/static/Scala-Handbook.htm>

- 以下是一些摘录，//后面是吐槽
-  “和别人分享你的知识，那才是永恒之道”——somebody
- Scala很好玩很有趣 //真是这样的话，我喜欢
- 语言特色能够塑造编程者的思维： C++也能使用抽象基类设计多重继承，但Java的接口引导你走得更远；Java也能设计类型安全的静态方法(final static)，但Scala鼓励你这样做并逐步从OOP到达FP的彼岸，而且来去自如
- 我们可以很容易地把过程语言、面向对象语言、函数式语言中的代码“翻译”成Scala代码。试想如果我们要把Haskell或者Lisp的某个尾递归算法翻译成Java代码，还得多花点时间；而要把C++的代码翻译成Hashkell，同样也不简单。Scala的混血性给我们的实际使用提供了便利。
- 适当地选用OOP或者FP，能够使表达相对另一种更加清晰准确
- 不用象动态语言那样测试代码比业务代码还多 //我目前的几个python小项目中测试代码很少，确实有很多运行中才发现的bug
- Scala虽然是一门彻头彻底的静态语言，但又具备了现代动态语言的很多方便和灵活 //really?
- Put productivity & creativity back in the hands of developers。其实不仅限于Scala，对于所有的编程语言来说，一门语言是否“好玩”有趣，能否激起创作欲，才是最关键的，这比语言风格、运行速度、工具支持、社区文化都来得重要。
- val 不可变，相当于const/final，但如果val为数组或者List，val的元素可以赋值
- val (x,y) = (10, "hello") //like python
- 向函数式风格推进的一个方式，就是尝试不用任何var来定义变量
- val regex = "(\\d+)/(\\d+)/(\\d+)".r
- val regex(year, month, day) = "2010/1/13"
- val f1 = System.currentTimeMillis //better, no need to import time
- lazy val f2 = System.currentTimeMillis
- 尽量使用大写形式： Int, Long, Double, Byte, Short, Char, Float, Double, Boolean. 编译时Scala自动对应到Java原始类型，提高运行效率。Unit对应java的void
- def i = 10.asInstanceOf[Double]
- List('A','B','C').map(c=>(c+32).asInstanceOf[Char])
- val b = 10.isInstanceOf[Int]
- 而在match ... case 中可以直接判断而不用此方法 //? 等后文
- 用Any统一了原生类型和引用类型 //不错
- -3.abs // 3 **
- -3 max -2 // -2
- -3 min -2 // -3
- 1.4.round // 1 四舍五入 **
- 1.1.ceil // 2.0 天花板 **
- 1.1.floor // 1.0 地板 **
- def abs(n: Int): Int = if (n > 0) n else -n 
- def even(n:Int) = 0==(n & 1)
- def odd(n:Int) = !even(n)
- BigInt("10000000000000000000000000")
- "jamesqiu".max // **
- ('a' to 'f') map (_.toString*3)
- "12345" map (_.toInt) // **
- def  fac(n:Int):BigInt = if (n==0) 1 else fac(n-1)*n
- fac(1000)
- println("""|Welcome to Ultamix 3000.  
-            |Type "HELP" for help.""".stripMargin)
- "abc" * 0 // ""
- "abc"+"abcww"

	"abc" * 0 // ""
	"abc"+"abcww"
