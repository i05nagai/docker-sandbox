def globalVariable = null

def returnTest1() {
	return 1
}

def returnTest2() {
	2
}

def returnTest() {
	
}

def returnTestDef() {
	def localVariable = 2
}

def returnTestSubstitute() {
	globalVariable = "substitute"
}

def returnTestClass() {
}

def returnTestGlobalVariable() {
	def globalVariable = 2
}

def runMatcher() {
	def moduleList = []
	def files = ["./foo.groovy", "/usr/name/foo.groovy", "./.", ""]
	for (path in files) {
		def matcher = path =~ /(.+?)\/.*/
		println "File: " + (new File(path).getParentFile().getPath())
		if (matcher.size()) {
			println "matcher[0][1]: " + matcher[0][1]
		  moduleList.push(matcher[0][1])
		}
	}
	return moduleList
}

def runMatcher2() {
	def moduleList = []
	def files = findFiles(glob: '*/*.groovy')
	for (path in files) {
		def matcher = path =~ /(.+?)\/.*/
		println "File: " + (new File(path).getParentFile().getPath())
		if (matcher.size()) {
			println "matcher[0][1]: " + matcher[0][1]
		  moduleList.push(matcher[0][1])
		}
	}
	return moduleList
}

def runStringTokenize() {
	"echo \n'aaa' dddd   eeeefdsa".tokenize()
}

def runFindFile() {
	findFile("dir000/dir010/file010.groovy")
}

def runClosure(Closure closure) {
	closure()
}


println "hello" 

byte  b = 1
char  c = 2
short s = 3
int   i = 4
long  l = 5
BigInteger bi =  6

// primitive types
float  f = 1.234
double d = 2.345

// infinite precision
BigDecimal bd =  3.456

def numbers = [1, "a", true]
println numbers.size()


String[] arrStr = ['Ananas', 'Banana', 'Kiwi']

def colors = [red: '#FF0000', green: '#00FF00', blue: '#0000FF']

println returnTest1()
println returnTest2()
println returnTest()
println returnTestDef()
println returnTestSubstitute()
println returnTestClass()
println returnTestGlobalVariable()
println globalVariable

// http://www.tothenew.com/blog/groovy-tokenize-vs-split/
println "runStringTokenize"
println runStringTokenize()

println "runFindFile"
println runFindFile()

println "runClosure"
for (num in [1, 2, 3, 4, 5]) {
    println num
    runClosure() {
        continue
    }
    println num
}

println runMatcher()
println runMatcher2()
