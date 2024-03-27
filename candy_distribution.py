"""
Candy Distribution

Imagine you have a lot of candy, but you have very specific rules about how to give candy to your friends.

 - Your first friend gets 1 piece of candy
 - Your second friend gets 4 pieces of candy
 - Your third friend gets 9 pieces of candy
 - Your nth friend gets n^2 pieces of candy

And so on — do you see the pattern? Here's a sample run of a working solution to get the big idea of how your program should behave:
 - candy = 10
 - You can give candy to 2 friend(s).
    """

total_candy = 1000
candy_given = 0
friends = 0
while (candy_given <= total_candy):
    friends = friends + 1
    candy_given = candy_given + friends**2
    print(friends, candy_given, candy_given//friends)
    # The last friend didn't get enough candy

friends = friends - 1
print("You can give candy to " + str(friends) + " friend(s).")
