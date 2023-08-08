fun main() {
    val user = User("J", 23, "F")
    try {
        print("Name: ${user.component1()}")
    } catch (e: Exception) {

    }
}

data class User(val name:String, val age:Int, val country:String)
