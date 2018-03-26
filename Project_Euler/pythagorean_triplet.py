"""This program answers the question what is the only pythagorean triplet
which sums to 1000.  We multiply the triplet together and return that as well."""

#c must be at least 334 or else a,b,c could never sum to 1000
#c <= 998 since a>=1, b>=1
for c in range(334, 999):
    #b can't be as large as c.  We may as well assume b >= a
    #1000-c = a+b.  Thus b is at least (1000-c)/2.  We need this to be an integer
    for b in range((1000-c)//2, c):
        if b**2 + (1000-c-b)**2 == c**2:
            if 1000-c-b > 0:
                a = 1000-b-c
                print(a,b,c)
                print(a*b*c)
