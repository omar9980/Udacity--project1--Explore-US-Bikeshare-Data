Notes For The reviwer 

1-- when i was writing the code i found that udacity workspace as old version of pandas 
as when i tried to use dt.day_name()
it gives me an error telling me that datetime properties has no attribute "day_name()"
it worked will for weekday_name 
i searched for the problem and i found that weekday_name is no longer in pandas library
and they replaced it with day_name()

2-- in the 104 line i wrote a function to give me the month by name with respect to index of month 
i found that there is a function called callednder which will do the same also 
but i don't know if i should use external libraries and functions 
so i went with the first option 
which is writting my own function  