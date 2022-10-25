-----------------------------------
Internal Assessment [10 Marks] 
--------------------------------
Create a class named Creature  
	# Class Variable 
	 Category = "Mammal"
	#Class Method 
	 get_category()
	 set_category(rcv_category)
    #instance variables 
     uniqueId,gender, current_activity
	#instance methods
	eat() --> prints "I am eating"
	sleep()--> prints "I am sleeping"

Create a sub class named Human of parent class Creature
   # instance variables 
   name,age,city
   #instance functions	
	play() --> prints "I am playing"
	work() --> prints "I am working"
	display_details() --> display details of the Human object

	start_current_activity(rcv_current_activity) --> starts either one of the activity eat()/sleep()/work()/play
	raise an exception if Human is said to perform any other activity

main function 
1) create an object of Human class -- (4 marks) 
# ( class variables - 1 marks  , Inheritance - 1 marks , instance variables , 1 marks , instance functions - 1 marks )
3) Display details of Human object -- ( 2 marks )
4) make the human eat, if possible  --( 2 marks )
5) make the human dance ,if possible -- (2 marks)

