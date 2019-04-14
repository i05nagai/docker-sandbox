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
