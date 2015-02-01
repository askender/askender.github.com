Title: 从零开始学scala
Date: 1980-01-01
Tags: study, coding
Slug: learn_scala_from_zero
Summary:

接触过各种编程语言，c, php，python, nodejs，java，go，lisp，其实都只会一点皮毛。一直认为语言得于具体的使用需求联系才能产生作用。
公司技术选型选定scala，现在学习新的语言scala，希望能更深入些。

以下是随意记录，仅仅当做备忘

- <http://qiujj.com/static/Scala-Handbook.htm>
-  “和别人分享你的知识，那才是永恒之道”——somebody
- Scala很好玩很有趣
- 语言特色能够塑造编程者的思维： C++也能使用抽象基类设计多重继承，但Java的接口引导你走得更远；Java也能设计类型安全的静态方法(final static)，但Scala鼓励你这样做并逐步从OOP到达FP的彼岸，而且来去自如
- 我们可以很容易地把过程语言、面向对象语言、函数式语言中的代码“翻译”成Scala代码。试想如果我们要把Haskell或者Lisp的某个尾递归算法翻译成Java代码，还得多花点时间；而要把C++的代码翻译成Hashkell，同样也不简单。Scala的混血性给我们的实际使用提供了便利。
- 适当地选用OOP或者FP，能够使表达相对另一种更加清晰准确
- 不用象动态语言那样测试代码比业务代码还多
- Scala虽然是一门彻头彻底的静态语言，但又具备了现代动态语言的很多方便和灵活
- Put productivity & creativity back in the hands of developers。其实不仅限于Scala，对于所有的编程语言来说，一门语言是否“好玩”有趣，能否激起创作欲，才是最关键的，这比语言风格、运行速度、工具支持、社区文化都来得重要。
- val 不可变，相当于const/final，但如果val为数组或者List，val的元素可以赋值
- val (x,y) = (10, "hello") // like python
- 向函数式风格推进的一个方式，就是尝试不用任何var来定义变量
- val regex = "(\\d+)/(\\d+)/(\\d+)".r
- val regex(year, month, day) = "2010/1/13"
- val f1 = System.currentTimeMillis //better, no need to import time
- lazy val f2 = System.currentTimeMillis
- 尽量使用大写形式： Int, Long, Double, Byte, Short, Char, Float, Double, Boolean. 编译时Scala自动对应到Java原始类型，提高运行效率。Unit对应java的void
- def i = 10.asInstanceOf[Double]
- List('A','B','C').map(c=>(c+32).asInstanceOf[Char])
- val b = 10.isInstanceOf[Int]
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
- "abc" * 0 // ""
- "abc"+"abcww"
- "google".reverse
- "Hello" map (_.toUpper) // 相当于 "Hello".toUpperCase
- "hello"=="Hello".toLowerCase()
- "101".toInt
- List("1","2","3") map (_.toInt)
- List("1","2","3") map Integer.parseInt

- val msg = java.text.MessageFormat.format(
-     "At {1,time} on {1,date}, there was {2} on planet {0}.",
-     "Hoth", new java.util.Date(), "a disturbance in the Force")

- "my name is %s, age is %d." format ("james", 30)
- "%s-%d：%1$s is %2$d." format ("james", 30)


- Null Trait，其唯一实例为null，是AnyRef的子类，*不是* AnyVal的子类
- Nothing Trait，所有类型（包括AnyRef和AnyVal）的子类，没有实例
- None Option的两个子类之一，另一个是Some，用于安全的函数返回值
- Unit 无返回值的函数的类型，和java的void对应
- Nil 长度为0的List

- val s1,s2 = "hello"
- val s3 = new String("hello")
- s1==s3 // true 值相同
- s1 eq s3 // false 不是同一个引用

- def p(map:Map[Int,Int]) = println(map get 3 getOrElse "...")
- p(Map(1->100,2->200)) // ...
- p(Map(1->100,3->300)) // 300


    def f(v:Any) = v match {
        case null => "null"
        case i:Int => i*100
        case s:String => s
        case _ => "others"
    }

- def fac(n:Int) = ((1:BigInt) to n).product
- def f(n:Int) = { require(n!=0, "n can't be zero"); 1.0/n }

- 1 to 11 by 2
- (1 to 3) forall (0<)
- def f(n:Int) = { require(n!=0, "n can't be zero"); 1.0/n }
- 更scalable的写法：
- def sum(L: Seq[Int]) = L.foldLeft(0)(_ + _)
- def sum(L: List[Int]) = (0/:L){_ + _}
- def multiply(L: Seq[Int]) = L.foldLeft(1)(_ * _)
- // def multiply(L: List[Int]) = (1/:L){_ * _}
- multiply(Seq(1,2,3,4,5)) // 120
- multiply(1 until 5+1) // 120
- List(1,2,3,4,5).scanLeft(0)(_+_)
- 1 to 10 by 2 take 3 // Range(1, 3, 5)
- 1 to 10 by 2 drop 3 // Range(7, 9)
- 1 to 10 by 2 splitAt 2 // (Range(1, 3),Range(5, 7, 9))

1 to 10 takeWhile (n=>n*n<25) // (1, 2, 3, 4)
1 to 10 dropWhile (n=>n*n<25) // (5,6,7,8,9,10)
List(1,0,1,0) span (_>0) // ((1), (0,1,0))
List(1,0,1,0) partition (_>0) // ((1,1),(0,0))

('a' to 'z').slice(0,10).foreach(println)
type JDate = java.util.Date
// 函数中的泛型
def foo[T](a:T) = println("value is " + a)
List(1.0, 3, 6.2, 2.3, 0).sortWith(_<_)
@specialized  // ?
Curry化 // ?
tail-recursive会被优化成循环，所以没有堆栈溢出的问题
协变和逆变(co-|contra-)variance // ?
元素合并进List用::
val list2 = "a"::"b"::"c"::Nil // Nil是必须的
val list3 = list2 ++ list1
IndexSeq的缺省实现是Vector:
IndexSeq(1,2,3) // Vector(1, 2, 3)
('0' to '9') ++ ('A' to 'Z')
(1 to 5).toList
def fib(a: Int, b: Int): Stream[Int] = a #:: fib(b,  a+b)
val fibs = fib(1, 1).take(7).toList // List(1, 1, 2, 3, 5, 8, 13)
Stream.range(1,50000000).filter(_%13==0)(1) // 26
val ms = collection.mutable.Stack()
ms.push(1,3,5).push(7) // Stack(7, 5, 3, 1)
ms.head // 7
ms.pop // 7, ms = Stack(5,3,1)
val mq = collection.mutable.Queue[Int]()
mq += (1,3,5)
mq ++= List(7,9) // Queue(1, 3, 5, 7, 9)
mq dequeue // 1, mq= Queue(3, 5, 7, 9)
mq clear // Queue()
List("a","b","c").map(s=> s.toUpperCase()) // 方式1
List("a","b","c").map(_.toUpperCase())     // 方式2, 类似于Groovy的it
List(1,3,5,7,9) splitAt 2 // (List(1, 3),List(5, 7, 9))
List(1,3,5,7,9) groupBy (5<) // Map((true,List(7, 9)), (false,List(1, 3, 5)))
List(1,2,3,4,5).exists(_%3==0) // true
List(1,3,2,0,5,9,7).sorted //  List(0, 1, 2, 3, 5, 7, 9)
List(1,3,2,0,5,9,7).sortWith(_>_) // List(9, 7, 5, 3, 2, 1, 0)
List("abc", "cb", "defe", "z").sortBy(_.size) // List(z, cb, abc, defe)
List((1,'c'), (1,'b'), (2,'a')) .sortBy(_._2) // List((2,a), (1,b), (1,c))
def uniq[T](l:List[T]) = l.distinct
val a = List(100,200,300)
a.indices // (0,1,2)
a.zipWithIndex // ((100,0), (200,1), (300,2))
(a.indices) zip a // ((0,100), (1,200), (2,300))
List(100,200,300,400,500) slice (2,4)
val v1 = List(1,2,3,4)
v1.updated(3,10) // List(1, 2, 3, 10), v1还是List(1, 2, 3, 4)
1 to 5 contains 3 // true, 后一个参数是1个元素
1 to 5 containsSlice (2 to 4) // true, 后一个参数是1个集合
(1 to 5) startsWith (1 to 3) // true 后一个参数是1个集合
(1 to 5) endsWith (4 to 5)
(List(1,2,3) corresponds List(4,5,6)) (_<_) // true，长度相同且每个对应项符合判断条件
List(1,2,3,4) intersect List(4,3,6) // 交集 = List(3, 4)
List(1,2,3,4) diff List(4,3,6) // A-B = List(1, 2)
List(1,2,3,4) union List(4,3,6) // A+B = List(1, 2, 3, 4, 4, 3, 6)
// 相当于
List(1,2,3,4) ++ List(4,3,6) // A+B = List(1, 2, 3, 4, 4, 3, 6)
val a = Array(100,200,300) // a(0)=100, a(1)=200, a(3)=300
a(0) // 100, 相当于a.apply(0)
val t1 = ("a","b","c") // t1._1="a", t1._2="b", t1._3="c"
List(1,2,3).zip(List(100,200,300)).toMap
