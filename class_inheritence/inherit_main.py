# Importing all inheritence files
# made alias
import hierarchieal_inherit as hierarchy
import hybrid_inherit as hybrid           # aka diamond inherietence
import method_override as my_override
import method_resol_order as my_mro
import multi_inherit as multi_inh
import multiLevel_inherit as multilevel
import polymorph as polymorph
import single_inherit as single_inh
import super_inherit as super_inh

# display menu
def displayMenu()->None:
    print("------------- Menu ------------------")
    print("1.Single inheritence")
    print("2.Multi inheritence")
    print("3.Multi level inheritence")
    print("4.hierarchieal inheritence")
    print("5.Hybrid inheritence")
    print("6.Super inheritence")
    print("7.Method resolution order")
    print("8.Method Override")
    print("9.Polymorphism")

    # print("Enter your choice: ")

# --------- main() ----------------------------
def main():
    cont = 'y'
    choice = 0
    while(cont == 'y'):

        print("---------------------------------------------------\n")
        displayMenu()
        choice = int(input("\nEnter your choice: "))
        print("---------------------------------------------------\n")
        if choice == 1:     #Single
            single_inh.single_inherit()
        elif choice == 2:   #multi
            multi_inh.multi_inherit()
        elif choice == 3:   # multilevel
            multilevel.multilevel_inheritence()
        elif choice == 4:   #Hierarchial
            hierarchy.Hierarchical()
        elif choice == 5:   #hybrid
            hybrid.Hybrid()
        elif choice == 6:   #Super
            super_inh.super_inherit()
        elif choice == 7:   # MRO
            my_mro.M_R_O()
        elif choice == 8:   # Override
            my_override.method_override()
        elif choice == 9:   # polymorphism
            polymorph.polymorph()
        else:
            print("Invalid choice.... ")
                        
        print("---------------------------------------------------\n")

        cont = input("Do you want to continue....??? y/n ")

        print("---------------------------------------------------\n")

main()



"""
---------------------------------------------------
OUTPUT: 
------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 1
---------------------------------------------------

Inside Vehicle class
Inside Car class
---------------------------------------------------

Do you want to continue....??? y/n y
---------------------------------------------------

---------------------------------------------------

------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 2
---------------------------------------------------

Inside Person class
Name: Jessa Age: 28
Inside Company class
Name: Google location: Atlanta
Inside Employee class
Salary: 12000 Skill: Machine Learning
---------------------------------------------------

Do you want to continue....??? y/n y
---------------------------------------------------

---------------------------------------------------

------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 3
---------------------------------------------------

Inside Vehicle class
Inside Car class
Inside SportsCar class
---------------------------------------------------

Do you want to continue....??? y/n y
---------------------------------------------------

---------------------------------------------------

------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 4
---------------------------------------------------

This is Vehicle
Car name is: BMW
This is Vehicle
Truck name is: Ford
---------------------------------------------------

Do you want to continue....??? y/n y
---------------------------------------------------

---------------------------------------------------

------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 5
---------------------------------------------------

Inside Vehicle class
Inside Car class
Inside SportsCar class
---------------------------------------------------

Do you want to continue....??? y/n y
---------------------------------------------------

---------------------------------------------------

------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 6
---------------------------------------------------

Jessa works at Google
---------------------------------------------------

Do you want to continue....??? y/n y
---------------------------------------------------

---------------------------------------------------

------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 7
---------------------------------------------------

 In class C
[<class 'method_resol_order.C'>, <class 'method_resol_order.B'>, <class 'method_resol_order.A'>, <class 'object'>]
---------------------------------------------------

Do you want to continue....??? y/n y
---------------------------------------------------

---------------------------------------------------

------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 8
---------------------------------------------------

max speed is 200 Km/Hour
---------------------------------------------------

Do you want to continue....??? y/n y
---------------------------------------------------

---------------------------------------------------

------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 9
---------------------------------------------------

3
10
---------------------------------------------------

Do you want to continue....??? y/n y
---------------------------------------------------

---------------------------------------------------

------------- Menu ------------------
1.Single inheritence
2.Multi inheritence
3.Multi level inheritence
4.hierarchieal inheritence
5.Hybrid inheritence
6.Super inheritence
7.Method resolution order
8.Method Override
9.Polymorphism

Enter your choice: 0
---------------------------------------------------

Invalid choice.... 
---------------------------------------------------

Do you want to continue....??? y/n n
---------------------------------------------------
"""