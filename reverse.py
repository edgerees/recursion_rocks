# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    if len(ss) == 0:
        return ss
    else:
        print(f"ss[1:] is: {ss[1:]}, ss[0] is: {ss[0]} - {ss[1:]}/{ss[0]} ")
        return reverse(ss[1:]) + ss[0]
    pass

print(reverse("")) 
# => ""
print(reverse("a")) 
# => "a"
print(reverse("ab")) 
# => "ba"
print(reverse("computer")) 
# => "retupmoc"
print(reverse(reverse("computer"))) 
# => "computer"